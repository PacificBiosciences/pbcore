#region Copyright (c) 2010, Pacific Biosciences of California, Inc.
//
// All rights reserved.
//
// THIS SOFTWARE CONSTITUTES AND EMBODIES PACIFIC BIOSCIENCES’ CONFIDENTIAL
// AND PROPRIETARY INFORMATION.
//
// Disclosure, redistribution and use of this software is subject to the
// terms and conditions of the applicable written agreement(s) between you
// and Pacific Biosciences, where “you” refers to you or your company or
// organization, as applicable.  Any other disclosure, redistribution or
// use is prohibited.
//
// THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS CONTRIBUTORS "AS
// IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
// PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR ITS
// CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
// EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
// PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
// OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
// WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
// OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
// ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
#endregion

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices;
using PacBio.Analysis.Codec;
using PacBio.Analysis.Data.ICD;
using PacBio.Analysis.Primary.Native;
using PacBio.Analysis.Sequence;
using PacBio.Common.Chunk;
using PacBio.Common.Chunk.HDF;
using PacBio.Common.Diagnostics;
using PacBio.Common.Extensions;
using PacBio.Common.Numeric;
using PacBio.Common.Threading;


namespace PacBio.Analysis.Data
{
    /// <summary>
    /// Provides access to raw trace data for a Zmw. This implementation lazily load the raw data.
    /// See IZmwTrace for field documentation.
    /// </summary>
    class ZmwTrace : IZmwTrace 
    {
        private readonly TraceReader reader;
        private readonly ISequencingZmw zmw;
        private readonly int readerIndex;
        
        internal ZmwTrace(TraceReader reader, ISequencingZmw zmw, int idx)
        {
            this.reader = reader;
            this.zmw = zmw;
            readerIndex = idx;
        }

        public void TraceDataDispose() {}

        public void Dispose() {}

        public void Data(float[,] buffer)
        {
            // Use the same mechanism as the Data() implementation for memoization.
            var tp = reader.ReadTracePhotons(readerIndex);

            clippedInfo = tp.Stats;
            Seq.FastCopy2(tp.Data, buffer);
        }
        
        public void DyeWeight(float[,] buffer)
        {
            Data(buffer);
        }

        public TraceRepresentation Representation
        {
            get { return reader.TraceRepresentation; }
        }

        public bool ClientCooptsTraceData { get; set; }

        private RangeStats clippedInfo;
        public RangeStats ClippedInfo
        {
            get
            {
                if (clippedInfo == null)
                {
                    // The data has not yet been read
                    var tp = reader.ReadTracePhotons(readerIndex);
                    clippedInfo = tp.Stats;
                }

                return clippedInfo;
            }
        }

        public float[,] Data()
        {
            var tp = reader.ReadTracePhotons(readerIndex);

            clippedInfo = tp.Stats;
            return tp.Data;
        }

        public byte[,] RawData()
        {
            return reader.ReadTraceRawData(readerIndex);
        }

        public float[,] DyeWeight()
        {
            return Data();
        }

        public float[,] Spectra
        {
            get { return reader.ReadSpectrum(readerIndex); }
        }

        public int NumChannels
        {
            get { return (Representation == TraceRepresentation.Camera ? NumCams : NumDyes); }
        }

        public int FrameOffset
        {
            get { return (int) reader.FrameOffset; }
        }

        public int NumDyes
        {
            get { return zmw.Movie.Analogs.Count; }
        }

        public int NumCams
        {
            get { return SpectralVariance.Length; }
        }

        public int NumVirtualCams { get { return reader.NumVirtualCams; } }

        public int NumFrames
        {
            get { return (int) reader.NumFrames; }
        }

        public float[] SpectralVariance
        {
            get { return reader.ReadSpectralVariance(readerIndex); }
        }

        public float[] InFocusVarianceScale
        {
            get { return reader.ReadInFocusVarianceScale(readerIndex); }
        }

        public float[] OutFocusBackgroundMean
        {
            get { return reader.ReadOutFocusBackgroundMean(readerIndex); }
        }

        public float[] OutFocusBackgroundVariance
        {
            get { return reader.ReadOutFocusBackgroundVariance(readerIndex); }
        }

        public ISequencingZmw Zmw
        {
            get { return zmw; }
        }

        public float[] SpectralReadVariance
        {
            get { return reader.ReadSpectralReadVariance(readerIndex); }
        }

        public float[] HolePhase
        {
            get { return reader.ReadRawHolePhase(readerIndex); }
        }

        public float[] DyeWeightedReadVariance
        {
            get { return reader.ReadDyeWeightedReadVariance(readerIndex); }
        }
    }

    /// <summary>
    /// Provides access to raw trace data for a Zmw. This implementation loads the companded HDF5
    /// data into a TLMemoryPool buffer in the constructor.  When the Data() methods are called,
    /// the companded data is decompanded on the calling thread.
    /// See IZmwTrace for field documentation
    /// </summary>
    class ZmwTraceStrict : IZmwTrace
    {
        static readonly ILog Logger = DiagManager.LogManager.LocalLogger();

        public void Log(LogLevel level, string msg)
        {
            Logger.Log(new AnalysisPipelineLogEvent(msg, level));
        }

        public void Log(LogLevel level, string format, params object[] args)
        {
            Log(level, String.Format(format, args));
        }

        private readonly ISequencingZmw zmw;

        private TLMemoryPool2D<float>.Ref traceRef;
        private readonly float[,] spectra;
        private readonly float[] spectralVariance;
        private readonly float[] spectralReadVariance;
        private readonly float[] dyeWeightedReadVariance;
        private readonly float[] inFocusVarianceScale;
        private readonly float[] outFocusBackgroundMean;
        private readonly float[] outFocusBackgroundVariance;
        private readonly float[] holePhase;

        private readonly Func<byte[,]> rawDataReadThunk;
        
        private readonly int nChannels;
        private readonly TraceRepresentation traceRepresentation;

        // Actually decompand the data into our buffer -- only use this once!
        private Action<AcquisitionTrace> readThunk;
        private readonly Func<Action<AcquisitionTrace>> makeReadThunk;

        internal ZmwTraceStrict(TraceReader reader, ISequencingZmw zmw, int idx)
        {
            this.zmw = zmw;
            var readerIndex = idx;

            nChannels = (int) (reader.TraceRepresentation == TraceRepresentation.Camera ? 
                reader.NumCams : reader.NumDyes);

            NumVirtualCams = reader.NumVirtualCams;
            NumFrames = (int) reader.NumFrames;
            FrameOffset = (int) reader.FrameOffset;

            // The data is decompanded into this buffer.  
            traceRef = TLMemoryPool2D<float>.Instance.Create(nChannels, NumFrames);

            var sw = new Stopwatch();
            sw.Start();
                      
            // readThunk is a function that holds a copy of the raw trace data and decompands
            // it into the the supplied buffer when called.  This lets the decompanding
            // operation happen on a worker thread.
            //
            makeReadThunk = () =>  reader.ReadTraceIntoBufferGetExpand(readerIndex);
            readThunk = makeReadThunk();

            spectra = reader.ReadSpectrum(readerIndex);
            
            // Variance and background mtrics
            spectralVariance = reader.ReadSpectralVariance(readerIndex);
            spectralReadVariance = reader.ReadSpectralReadVariance(readerIndex);
            dyeWeightedReadVariance = reader.ReadDyeWeightedReadVariance(readerIndex);
            inFocusVarianceScale = reader.ReadInFocusVarianceScale(readerIndex);
            outFocusBackgroundMean = reader.ReadOutFocusBackgroundMean(readerIndex);
            outFocusBackgroundVariance = reader.ReadOutFocusBackgroundVariance(readerIndex);
            holePhase = reader.ReadRawHolePhase(readerIndex);
            
            // Provide a way to get the raw data for this trace.
            rawDataReadThunk = () => reader.ReadTraceRawData(readerIndex);
            
            // Trace data representation (i.e., Camera or DyeWeighted)
            traceRepresentation = reader.TraceRepresentation;

            sw.Stop();

            if (idx % 50 == 0)
                Log(LogLevel.INFO, "Trace read took: {0} ms, for {1} frames", sw.ElapsedMilliseconds, NumFrames);
        }

        public void Data(float[,] buffer)
        {
            if (isDisposed == false)
            {
                if (traceRef == null && isDisposed == false)
                {
                    traceRef = TLMemoryPool2D<float>.Instance.Create(nChannels, NumFrames);
                    readThunk = makeReadThunk();
                }

                if (readThunk != null)
                {
                    var acqTrc = new AcquisitionTrace(traceRef.Contents);
                    readThunk(acqTrc);
                    readThunk = null;

                    // Save the range stats
                    clippedInfo = acqTrc.Stats;
                }
            }
            
            Seq.FastCopy2(traceRef.Contents, buffer);
        }

        public void DyeWeight(float[,] buffer)
        {
            Data(buffer);
        }

        public TraceRepresentation Representation
        {
            get { return traceRepresentation; }
        }

        public bool ClientCooptsTraceData { get; set; }

        private RangeStats clippedInfo;
        public RangeStats ClippedInfo
        {
            get
            {
                if (clippedInfo == null)
                {
                    // The data has not yet been read
                    Data();
                }

                return clippedInfo;
            }
        }

        public float[,] Data()
        {
            if (isDisposed == false)
            {
                if (traceRef == null)
                {
                    traceRef = TLMemoryPool2D<float>.Instance.Create(nChannels, NumFrames);
                    readThunk = makeReadThunk();
                }

                if (readThunk != null)
                {
                    var acqTrc = new AcquisitionTrace(traceRef.Contents);
                    readThunk(acqTrc);
                    readThunk = null;

                    // Save the range stats
                    clippedInfo = acqTrc.Stats;
                }
            }

            return traceRef.Contents;
        }

        public byte[,] RawData()
        {
            // Access to raw data.
            return rawDataReadThunk();
        }

        public float[,] DyeWeight()
        {
            return Data();
        }

        public float[,] Spectra
        {
            get { return spectra; }
        }

        public int NumChannels
        {
            get { return (Representation == TraceRepresentation.Camera ? NumCams : NumDyes); }
        }

        public int NumFrames { get; private set; }

        public int FrameOffset { get; private set; }

        public int NumDyes
        {
            get { return zmw.Movie.Analogs.Count; }
        }

        public int NumCams
        {
            get { return spectralVariance.Length; }    
        }

        public int NumVirtualCams { get; private set; }

        public float[] SpectralVariance
        {
            get { return spectralVariance; }
        }

        public float[] InFocusVarianceScale
        {
            get { return inFocusVarianceScale; }
        }

        public float[] OutFocusBackgroundMean
        {
            get { return outFocusBackgroundMean; }
        }

        public float[] OutFocusBackgroundVariance
        {
            get { return outFocusBackgroundVariance; }
        }

        public float[] HolePhase
        {
            get { return holePhase; }
        }

        public ISequencingZmw Zmw
        {
            get { return zmw; }
        }

        public void TraceDataDispose()
        {
            traceRef.Dispose();
            traceRef = null;
        }

        private bool isDisposed = false; 
        public void Dispose()
        {
            TraceDataDispose();
            isDisposed = true;
        }

        public float[] SpectralReadVariance
        {
            get { return spectralReadVariance; }
        }

        public float[] DyeWeightedReadVariance
        {
            get { return dyeWeightedReadVariance; }
        }
    }

    public class ZmwTraceAndPulse
    {
        public IZmwTrace ZmwTrace { get; set;  }
        public IZmwPulses ZmwPulses { get; set;  }
    }

    public class FrameSet : IFrameSet
    {
        public IDataset HPFrameSet { get; private set; }

        public IDataset RVFrameSet { get; private set; }

        public IDataset VFrameSet { get; private set; }

        public FrameSet(IDataset hpFrameSet, IDataset rvFrameSet, IDataset vFrameSet)
        {
            HPFrameSet = hpFrameSet;
            RVFrameSet = rvFrameSet;
            VFrameSet = vFrameSet;
        }
    }

    /// <summary>
    /// Provides access to trace data stored in the PacBio HDF5 Trace file format (*.trc.h5).
    /// This class provides access to a series of IZmwTrace objects, either sequentially according
    /// to the data stored in the trace file, or by ZMW Number.
    /// </summary>
    [HdfIcdEntry(
        Path = "/TraceData",
        Detail = "Top-level container group for trace data")
    ]
    public class TraceReader : DataSource<IZmwTrace>, ITraceSource
    {
        #region Logging

        static readonly ILog Logger = DiagManager.LogManager.LocalLogger();

        public void Log(LogLevel level, string msg)
        {
            Logger.Log(new AnalysisPipelineLogEvent(msg, level));
        }

        public void Log(LogLevel level, string format, params object[] args)
        {
            Log(level, String.Format(format, args));
        }

        #endregion

        #region Interface Control Documentation

        public class Icd : HdfIcd<TraceReader>
        {
            // Define all ICD entries that are not covered by member annotations here
            private static IEnumerable<HdfIcdEntry> Mine()
            {
                return new HdfIcdEntry[]
                {
                    // TraceData attributes
                    new HdfIcdEntry
                        {
                            Path = "TraceOrder",
                            Detail = "Ordering of the traces block, using the encoding 0 == hole (ZMW) dimension, 1 == dye or spectral channel dimension, 2 == frame (time) dimension",
                        },
                    new HdfIcdEntry
                        {
                            Path = "Look",
                            Detail = "Look number, with 0 as the first look"
                        },
                    new HdfIcdEntry
                        {
                            Path = "Version",
                        },
                    new HdfIcdEntry
                        {
                            Path = "DateCreated",
                            Detail = "Date/Time that this group was written in ISO 8601 compliant format"
                        },
                       
                    // Codec entries
                    new HdfIcdEntry
                        {
                            Path = "Codec",  
                            Detail = "Top-level container group for Codec"
                        },
                    new HdfIcdEntry
                        {
                            Path = "Codec/Name",
                            Detail = "Unique name of the codec",
                            Units = "Currently \"MuLaw\" or \"FixedPoint\""
                        },
                    new HdfIcdEntry
                        {
                            Path = "Codec/Config",
                            Detail = "List of codec params, by attribute name",
                        },
                    new HdfIcdEntry
                        {
                            Path = "Codec/BitDepth",       
                            Detail = "Mu-law and FixedPoint16 codec bit-depth parameter"
                        },
                    new HdfIcdEntry
                        {
                            Path = "Codec/DynamicRange",       
                            Detail = "Mu-law only codec dynamic range parameter"
                        },
                    new HdfIcdEntry
                        {
                            Path = "Codec/Bias", 
                            Detail = "Mu-law and FixedPoint16 codec bias parameter"
                        },
                    new HdfIcdEntry
                        {
                            Path = "Codec/Mu",       
                            Detail = "Mu-law only codec mu parameter"
                        },
                    new HdfIcdEntry
                        {
                            Path = "Codec/Decode",       
                            Detail = "Mu-law only Lookup table to decode signal values to 32-bit floating point"
                        },
                       
                    // TraceData entries
                    new HdfIcdEntry
                        {
                            Path = "HoleNumber",
                            Detail = "Number assigned to each ZMW on the chip"
                        },
                    new HdfIcdEntry
                        {
                            Path = "HoleXY",
                            Detail = "Grid coordinates assigned to each ZMW on the chip"
                        },
                    new HdfIcdEntry
                        {
                            Path = "HoleXY/Look",
                            Detail = "Look number"
                        },
                    new HdfIcdEntry
                        {
                            Path = "HoleChipLook",                          
                            Detail = "Look of ZMW in chip layout"
                        },
                    new HdfIcdEntry
                        {
                            Path = "HoleStatus",
                            Detail = "Type of ZMW that produced the data"
                        },
                    new HdfIcdEntry
                        {
                            Path = "HoleXYPlot",
                            Detail = "The (unique) location of each ZMW in normalized chip coordinates"
                        },

                    new HdfIcdEntry
                        {
                            Path = "HPFrameSet",
                            Detail = "Block start frame number (0-based) for HolePhase values"
                        },
                    new HdfIcdEntry
                        {
                            Path = "RVFrameSet",
                            Detail = "Block start frame number (0-based) for ReadVariance estimates"
                        },
                    new HdfIcdEntry
                        {
                            Path = "VFrameSet",
                            Detail = "Block start frame number (0-based) for Variance estimates"
                        },

                };
            }

            public Icd(bool flatten = false)
                : base(Mine(), flatten)
            {
            } 
        }

        /// <summary>
        /// Return the ICD in flattened form (for the Writer class).
        /// </summary>
        /// <returns></returns>
        public static ICD.Icd GetIcd() { return new Icd(true); }

        #endregion

        #region Members

        private readonly Uri sourceUri;
        private readonly bool strict;

        protected static long[] Ones3D = new long[] { 1, 1, 1 };
        protected static long[] Ones2D = new long[] { 1, 1 };

        protected IChunkFile Chunks { get; set; }
        protected IGroup TraceGroup { get; set; }
        protected IGroup ScanDataGroup { get; set; }

        [HdfIcdEntry(
            Path = "Traces",
            Detail = "Trace data, each datum compressed to a byte using the compression algorithm described by Codec")]
        public IDataset TraceDataset { get; set; }
        protected IDataset SpectraDataset { get; set; }
        
        private ICompand Compander { get; set; }
        private Func<IZmwTrace>[] ZmwTraces { get; set; }

        // Zmws x Channels dataset giving the shift in frames to be applied to each channel
        protected byte[,] ChannelShift;

        // Trace reader functions
        internal Func<int, AcquisitionTrace> ReadTracePhotons;
        internal Func<int, AcquisitionTrace> ReadTraceCounts;

            // Spectra reader functions
        [HdfIcdEntry(
            Path = "Spectra",
            Detail = "The dye calibration spectra")]
        public Func<int, float[,]> ReadSpectrum;
        
        // Trace camera-metric readers.  These are organized by VFrameSet,
        // but there is no support yet in the API for updates.
        [HdfIcdEntry(
            Path = "HolePhase",
            Detail = "The time delay of each ZMW for each camera",
            Units = "Fraction of the frame interval [0,1]")]
        public Func<int, int[]> ReadHolePhase;

        public Func<int, float[]> ReadRawHolePhase;

        [HdfIcdEntry(
            Path = "Variance",
            Detail = "The channel variance estimates used to construct the weights for DWS reduction",
            Units = "Correspond to decoded trace units")]
        public Func<int, float[]> ReadSpectralVariance;

        [HdfIcdEntry(
            Path = "ReadVariance",
            Detail = "The variance estimates corresponding to camera read noise contribution",
            Units = "Correspond to decoded trace units")]
        public Func<int, float[]> ReadSpectralReadVariance;

        [HdfIcdEntry(
            Path = "IFVarianceScale",
            Detail = "The in-focus variance scaling factor")]
        public Func<int, float[]> ReadInFocusVarianceScale;

        [HdfIcdEntry(
            Path = "OFBackgroundMean",
            Detail = "The out-of-focus background mean",
            Units = "Correspond to decoded trace units")]
        public Func<int, float[]> ReadOutFocusBackgroundMean;

        [HdfIcdEntry(
            Path = "OFBackgroundVariance",
            Detail = "The out-of-focus background mean",
            Units = "Correspond to decoded trace units")]
        public Func<int, float[]> ReadOutFocusBackgroundVariance;

        // Derived metric readers
        internal Func<int, float[]> ReadDyeWeightedReadVariance;

        // Counts to photo-electron conversion
        protected float PhotonScale;

        // HDF5 chunking/caching - ye old TailorChunkCache is always TRUE
        // 30 min movie at 100FPS at full (float) resolution, w/ 200-hole chunking:
        // (30 x 60 x 100 x 200 x 4(bytes) x 4(dyes)) = 576 MB.
        // That's a 2-hr movie at 1-byte resolution.  So we can cut this down based on that.
        // We can also decrease the ZMW chunk size (e.g., to 100) to cut down this cache.
        private const long maxChunkCacheBytes = (long)580e6;

        public long ChunkCacheBytes = maxChunkCacheBytes;
        public long ChunkCacheChunks = (int)5e4;

        #endregion

        #region Properties

        // Source Info
        [HdfIcdEntry(
            Path = "Representation",
            Detail = "Representation of the data in the Traces block in a controlled vocabulary",
            Units = "Camera,DyeWeightedSum,Multicomponent")]
        public TraceRepresentation TraceRepresentation { get; private set; }

        // Dimensions
        public long NumZmws { get; private set; }
        public long NumDyes { get; private set; }

        // The number of cameras used in the aquisition, period.
        // I.e., the number of spectral channels in the dye spectra stored in the file.
        private int nRawCams;

        /// <summary>
        /// The number of cameras (i.e. spectral channels) presented in served-up spectra.
        /// This number may be altered from the 'raw' number of cameras if a CameraProjection is applied.
        /// </summary>
        public int NumCams { get; private set; }
        
        /// <summary>
        /// The true number of camera channels that contain relevant data.  When camera data is
        /// projected down to (or read in as) fewer than four (4) cameras, the served-up data may be
        /// buffered out to 4 channels, to maintain the optimized RS processing paths of 4-camera data. 
        /// </summary>
        public int NumVirtualCams { get { return NumCams - nGhostCams; } }

        // The number of channels stored in the file to-be-read, period.
        private long nRawChans;

        /// <summary>
        /// The number of channels (array size) presented in served-up trace data.
        /// This number may be altered from nRawChans if a CameraProjection is applied.
        /// </summary>
        public long NumChans { get; private set; }
        
        public uint NumFrames { get; private set; }
        public long FrameOffset { get; private set; }

        public IGroup CodecGroup { get; private set; }

        public IFrameSet FrameSet { get; private set; }

        public long FrameChunkSize { get; private set; }

        public IAttribute[] TraceDataAttributes { get; private set; }

        #endregion

        #region Structors
        // ReSharper disable DoNotCallOverridableMethodsInConstructor

        /// <summary>
        /// Factory method for creating the appropriate type of trace source from a trc URI.
        /// Clients should use this method for correct handling of single- or multi-part files.
        /// </summary>
        /// <param name="uri"></param>
        /// <param name="zmws"></param>
        /// <returns></returns>
        public static ITraceSource CreateSource(Uri uri, IZmwSource zmws)
        {
            var partUris = Helpers.GetMultiPartUris(uri);

            if (partUris != null)
            {
                var tr = new TraceMultiPartReader(partUris);
                tr.ValidateSource();
                return tr;
            }
            else
            {
                var tr = new TraceReader(uri, zmws);
                tr.ValidateSource();
                return tr;
            }
        }

        /// <summary>
        /// Factory method for creating the appropriate type of trace source from a trc URI.
        /// Clients should use this method for correct handling of single- or multi-part files.
        /// </summary>
        /// <param name="uri"></param>
        /// <param name="strict"></param>
        /// <param name="startOffsetSec"></param>
        /// <param name="durationInSec"></param>
        /// <returns></returns>
        public static ITraceSource CreateSource(Uri uri, bool strict = false, int startOffsetSec = 0, int durationInSec = 0)
        {
            var partUris = Helpers.GetMultiPartUris(uri);

            if (partUris != null)
            {
                var tr = new TraceMultiPartReader(partUris, strict, startOffsetSec, durationInSec);
                tr.ValidateSource();
                return tr;
            } 
            else 
            {
                var tr = new TraceReader(uri, strict, startOffsetSec, durationInSec);
                tr.ValidateSource();
                return tr;
            }
        }

        /// <summary>
        /// Open a TraceReader o from data in the provided Uri
        /// </summary>
        /// <param name="uri">Uri to trace data</param>
        internal TraceReader(Uri uri)
            : this(uri, false)
        {
            
        }

        /// <summary>
        /// Open a TraceReader o from data in the provided Uri
        /// External clients should use TraceReader.CreateSource() for support of the multi-part layout as of Release 1.4.
        /// </summary>
        /// <param name="uri">Uri to trace data</param>
        /// <param name="strict"></param>
        /// <param name="startOffsetSec">Time offset (sec) at which to start reading</param>
        /// <param name="durationInSec">Time duration (sec) to read for each trace</param>
        internal TraceReader(Uri uri, bool strict, int startOffsetSec = 0, int durationInSec = 0)
        {
            this.strict = strict;
            
            try
            {
                sourceUri = uri;
                Init(startOffsetSec, durationInSec);
            }
            catch (IOException e)
            {
                throw new IOException(
                    String.Format("Error Reading HDF Trace file: {0}", uri), e);
            }
        }

        /// <summary>
        /// Open a TraceReader o from data in the provided Uri.
        /// External clients should use TraceReader.CreateSource() for support of the multi-part layout as of Release 1.4.
        /// </summary>
        /// <param name="uri">Uri to trace data</param>
        /// <param name="zmws">An IZmwSource providing metadata about the traces contained in the file</param>
        /// <param name="strict"></param>
        internal TraceReader(Uri uri, IZmwSource zmws, bool strict = false)
        {
            this.strict = strict;
            try
            {
                sourceUri = uri;
                ZmwSource = zmws;
                Init();
            }
            catch (IOException e)
            {
                throw new IOException(
                    String.Format("Error Reading HDF Trace file: {0}, Message: {1}", uri, e.Message), e);
            }
        }

        public override void Dispose()
        {
            Chunks.Dispose();
        }

        /// Open the HDF5 file
        private void Init(int startOffsetSec = 0, int durationInSec = 0)
        {
            // A target analysis time-chunk of 0 is "to the end of the dataset"
            durationInSec = durationInSec <= 0 ? int.MaxValue : durationInSec;

            // Open the file
            Chunks = HDFFile.Open(sourceUri, FileMode.Open, FileAccess.Read);

            // Open up the Trace Group
            var hdfGroup = (HDFGroup)Chunks.GetChild("TraceData");
            TraceGroup = hdfGroup;
            var hdfScanData = (HDFGroup)Chunks.GetChild("ScanData");
            ScanDataGroup = hdfScanData;

            // Read the trace data attributes.
            TraceDataAttributes = TraceGroup.GetAttributes();

            // Access the metadata
            ZmwSource = MetadataReader.GetMetadataReader(ScanDataGroup, TraceGroup);

            // Determine the representation of the trace data
            TraceRepresentation = ReadRepresentation(hdfGroup);

            // Convert target offset/duration times to frames
            var frameRate = ZmwSource.FrameRate;
            var tgtStart = (long) Math.Round(startOffsetSec*frameRate);
            var tgtCount = (long) Math.Round(durationInSec*frameRate);

            // Open up 'Traces' dataset temporarily so we can get the dimensions and chunking info))
            using (var tempTraces = (IDataset) TraceGroup.GetChild("Traces"))
            {
                var elemSize = Marshal.SizeOf(tempTraces.Datatype.NativeType);
                var dataDims = tempTraces.Dataspace.Dimensions;
                var chunkSizes = ((HDFDataset) tempTraces).ChunkDimensions;
                FrameChunkSize = chunkSizes[2];

                // Set class size properties here
                NumZmws = dataDims[0];
                nRawChans = (int) dataDims[1];
                
                // Enforce that the target offset leaves at least one frame of data
                if (tgtStart >= dataDims[2])
                    throw new ArgumentException("Requested frame offset is beyond the end of the dataset");

                // Set the start-frame offset (returned)
                FrameOffset = tgtStart;

                // Then this is safely set: we truncate (silently) at the dataset boundary
                // if the requested count goes beyond that.
                NumFrames = (uint)Math.Min(dataDims[2] - FrameOffset, tgtCount);

                // We need to be able to hold all the chunks spanning a trace in cache simultaneously
                var traceChunkBytes = (long)(NumFrames * nRawChans * elemSize * chunkSizes[0] * 1.5);

                // Limit the cache size at, well, ... something
                ChunkCacheBytes = Math.Min(traceChunkBytes, maxChunkCacheBytes);
                ChunkCacheChunks = MathUtils.ModUp((int) (1.5*NumFrames/chunkSizes[2]), 16);
            }

            // Re-open Traces with the customized chunk size
            var plist = new HDFDatasetAccessProperty();
            plist.SetCache((uint) ChunkCacheChunks, (uint) ChunkCacheBytes, 0.5);
            TraceDataset = hdfGroup.OpenDataset("Traces", plist);

            SpectraDataset = (IDataset)TraceGroup.GetChild("Spectra");
            if(SpectraDataset == null)
                throw new ApplicationException("No Spectral data in trace file. The trc.h5 file needs to be merged with the upd.h5 file");

            long nZmwSpectra; 
            switch (SpectraDataset.Dataspace.Dimensions.Length)
            {
                case 3:               
                    NumDyes = (int)SpectraDataset.Dataspace.Dimensions[0];
                    nZmwSpectra = SpectraDataset.Dataspace.Dimensions[1];
                    nRawCams = (int)SpectraDataset.Dataspace.Dimensions[2];
                    break;

                case 2: // Handle single channel movies -- they are 2d
                    NumDyes = 1;
                    nZmwSpectra = SpectraDataset.Dataspace.Dimensions[0];
                    nRawCams = (int)SpectraDataset.Dataspace.Dimensions[1];                 
                    break;

                default:
                    throw new ApplicationException("Invalid Spectra dataset in trace file.");
            }

            // Since this method is used in construction, none of the channel-related
            // dimensions are modified by a potential CameraProjection... yet.
            NumCams = nRawCams;
            NumChans = nRawChans;

            // Check Dimensions derived from Spectra against the Trace dataDims:
            var nExpectedTraceChannels = (TraceRepresentation == TraceRepresentation.Camera ? NumCams : NumDyes);

            if (nExpectedTraceChannels != nRawChans)
                throw new ApplicationException("Mismatch in Trace NumChannels with Spectra Dataset.");

            if (nZmwSpectra != NumZmws)
                throw new ApplicationException("Mismatch in Trace NumZmws with Spectra Dataset.");            

            // We keep an array of thunks that yield the ZmwTrace object.  
            // We either give lazy one or strict ZmwTrace wrappers depending on how we were constructed.  
            ZmwTraces = strict ? 
                ZmwSource.Map<ISequencingZmw, Func<IZmwTrace>>((z, idx) => (() => new ZmwTraceStrict(this, z, idx))) : 
                ZmwSource.Map<ISequencingZmw, Func<IZmwTrace>>((z, idx) => (() => new ZmwTrace(this, z, idx))); 
            
            // Set the scale to convert from counts to photons
            PhotonScale = ZmwSource.AduGain / ZmwSource.CameraGain;

            // Bust out the Compander need to decompress the traces
            SetupCodec();

            // Set the frame set update datasets.
            SetupFrameSet();

            // Memoize the trace reader functions. 
            // This should be expanded / combined with the reader function to attempt to do read-ahead caching,
            // if someone figures out that we're doing too many seeks by reading a trace at a time.
            //
            // ReSharper disable RedundantTypeArgumentsOfMethod
            ReadTracePhotons = Memoize.IndexedWeakMemoize<AcquisitionTrace>(ReadTraceByIdxPhotons, (int)NumZmws);
            ReadTraceCounts = Memoize.IndexedWeakMemoize<AcquisitionTrace>(ReadTraceByIdxCounts, (int)NumZmws);

            // Set up the reader for dye spectra
            ReadSpectrum = strict
                               ? ReadSpectrumByIdxCached
                               : Memoize.IndexedWeakMemoize<float[,]>(ReadSpectrumByIdx, (int) NumZmws);

            // Set up readers for the trace metrics
            ReadHolePhase = MakeCameraMetricLookup<float, int>("HolePhase", false, 0, TransformHolePhase);
            ReadRawHolePhase = MakeCameraMetricLookup<float, float>("HolePhase", false, 0, r => r);
            ReadSpectralVariance = MakeCameraMetricLookup<float, float>("Variance", true, 0.0f, ProjectAndRescaleVariance);
            ReadSpectralReadVariance = MakeCameraMetricLookup<float, float>("ReadVariance", false, 0.0f, ProjectAndRescaleVariance);
            ReadInFocusVarianceScale = MakeCameraMetricLookup<float, float>("IFVarianceScale", false, 1.0f, ProjectScale);
            ReadOutFocusBackgroundMean = MakeCameraMetricLookup<float, float>("OFBackgroundMean", false, 0.0f, ProjectAndRescaleSignal);
            ReadOutFocusBackgroundVariance = MakeCameraMetricLookup<float, float>("OFBackgroundVariance", false, 0.0f, ProjectAndRescaleVariance);
            
            // Derived trace metrics
            ReadDyeWeightedReadVariance = Memoize.IndexedWeakMemoize<float[]>(DyeWeightedReadVariance, (int)NumZmws);
        }

        // ReSharper restore DoNotCallOverridableMethodsInConstructor
        #endregion

        #region Public Methods

        // Camera Projection matrices
        private float[,] fCamProj;
        private float[,] fCamProjT;
        private float[,] fCamProj2;     // Element-wise square of CameraProjection
        private float[] fCamProjRSum;   // Sum along rows of CameraProjection
        private int nGhostCams;

        /// <summary>
        /// Projection to virtual cameras:  all relevant camera data will be transformed appropriately
        /// on input by this projection when it it set. Matrix dimensions are [nVirtCam x nPhysCam].
        /// </summary>
        public float[,] CameraProjection
        {
            get { return fCamProj; }

            set
            {
                if (value == null)
                {
                    // Un-set the projection
                    fCamProj = fCamProjT = fCamProj2 = null;
                    fCamProjRSum = null;
                    
                    NumCams = nRawCams;
                    NumChans = nRawChans;
                    nGhostCams = 0;

                    return;
                }

                // The case of nProjCam < 4 is a special case, handled by appending
                // (4 - nProjCam) null rows to the projection matrix.  This enables
                // the fast 4-camera trace processing used by Springfield/RS. 
                // The case nProjCam > nPhysCam (i.e. nRawCam) is not allowed.
                //
                int nProjCam = value.GetLength(0);
                int nPhysCam = value.GetLength(1);

                if (nPhysCam != nRawCams)
                    throw new ArgumentException(
                        "The number of physical cameras in the projection do not match the input data");

                if (nProjCam > nPhysCam)
                    throw new ArgumentException(
                        "The number of virtual cameras must be <= the number of physical cameras");

                // Keep at least 4 camera channels, to enable fast RS-based camera trace processing.
                nProjCam = Math.Max(nProjCam, 4);
                
                fCamProj = new float[nProjCam, nPhysCam];
                value.CopyTo(fCamProj, 0, 0);

                // Used in (approx) variance scale xform:
                fCamProj2 = fCamProj.Map(v => v * v);       // Element-wise square
                fCamProjRSum = fCamProj.Sum();              // Sum along rows
              
                // Transpose is used for the spectra, which are [nDyes x nCams]
                fCamProjT = fCamProj.Transpose();

                // The number of camera channels served up is now determined by the projection:
                NumCams = nProjCam;
                NumChans = (TraceRepresentation == TraceRepresentation.Camera ? nProjCam : NumDyes);

                // The number of "ghost" cameras -- i.e., taken out of play by the projection
                nGhostCams = fCamProjRSum.Count(v => v == 0);
            }
        }
        
        /// <summary>
        /// The function that reads Traces in 'counts' given an index into the stored trace array.
        /// This index must be converted from the zmwNumber by referencing the HoleNumber field
        /// </summary>
        /// <param name="n">Trace array index</param>
        /// <returns></returns>
        internal AcquisitionTrace ReadTraceByIdxCounts(int n)
        {
            // For no compander (traces stored as float), implied units are photons 
            return ReadTraceByIdx(n, Compander == null ? 1f / PhotonScale : Compander.ToCounts(PhotonScale));
        }

        /// <summary>
        /// The function that reads Traces in 'photons' given an index into the stored trace array.
        /// This index must be converted from the zmwNumber by referencing the HoleNumber field
        /// </summary>
        /// <param name="n">Trace array index</param>
        /// <returns></returns>
        internal AcquisitionTrace ReadTraceByIdxPhotons(int n)
        {
            // For no compander (traces stored as float), implied units are photons 
            return ReadTraceByIdx(n, Compander == null ? 1f : Compander.ToPhotons(PhotonScale));
        }

        /// <summary>
        /// This function reads the Traces "raw" given an index into the stored trace array.
        /// </summary>
        /// <param name="n"></param>
        /// <returns></returns>
        internal byte[,] ReadTraceRawData(int n)
        {
            var targetRef = new byte[(int) nRawChans,(int) NumFrames];
            var start = new[] { n, 0, FrameOffset };
            var count = new[] { 1, nRawChans, NumFrames };

            // Make a new dataspace to be used for this access
            using (var rspace = TraceDataset.Dataspace)
            {
                rspace.SelectHyperslab(start, Ones3D, count, Ones3D);

                var target = (Array)targetRef;
                TraceDataset.Read(ref target, rspace);
                
            }

            return targetRef;
        }

        public override void ValidateSource()
        {
            // Bug 19851
            // Check that we have a valid base map and all bases are accounted for.
            var bases = new char[] { 'T', 'G', 'A', 'C' }.Except(ZmwSource.Movie.Analogs.Select(a => Char.ToUpper(a.Base))).ToArray();
            if (bases.Length > 0)
            {
                var errMsg = String.Format("Incomplete base map detected, no analogs for bases: {0}", bases.Join(','));
                throw new PipelineTraceReaderMetadataException(errMsg); 
            }
        }

        #endregion

        #region Private Methods

        // Logic for applying a CameraProjection to trace data output
        private bool DoCamProjection
        {
            get { return TraceRepresentation == TraceRepresentation.Camera && CameraProjection != null; }
        }

        // Read the representation of the stored trace data.
        private TraceRepresentation ReadRepresentation(HDFGroup traceDataGroup)
        {
            string repStr;
            try
            {
                repStr = traceDataGroup.GetAttribute("Representation").ReadSingleton<string>();
            }
            catch (Exception)
            {
                Log(LogLevel.WARN, "Missing Representation attribute in TraceData group, assuming DyeWeightedSum.");
                return TraceRepresentation.DyeWeightedSum;
            }

            switch (repStr)
            {
                case "DyeWeightedSum":
                    return TraceRepresentation.DyeWeightedSum;
                case "Camera":
                    return TraceRepresentation.Camera;
                case "Multicomponent":
                    return TraceRepresentation.Multicomponent;
                default:
                    Log(LogLevel.ERROR,"Unknown /TraceData/Representation attribute: {0}",repStr);
                    throw new Exception("Invalid value read for attribute /TraceData/Representation.");
            }
        }

        // Read noise (variance) in the Dye-Weighted-Sum trace representation
        private float[] DyeWeightedReadVariance(int idx)
        {
            var spectra = ReadSpectrum(idx);
            var specVariance = ReadSpectralVariance(idx);
            var specReadNoise = ReadSpectralReadVariance(idx);

            var dwReadNoise = new float[NumDyes];

            for (int ch = 0; ch < NumDyes; ch++)
            {
                int ch1 = ch;
                var n = NumCams.Fill(p => Math.Pow(spectra[ch1, p], 2.0) / specVariance[p]).Sum();
                var w = NumCams.Fill(p => spectra[ch1, p] / specVariance[p] / n);

                dwReadNoise[ch1] = (float)w.Map((ww, i) => Math.Pow(ww, 2.0) * specReadNoise[i]).Sum();
            }

            return dwReadNoise;
        }

        // Load the codec spec from the HDF5 file, and get a Compander
        private void SetupCodec()
        {
            // See if we've got an explicit decode dataset
            CodecGroup = (IGroup)TraceGroup.GetChild("Codec");

            // Allow for a missing Codec (case of Traces stored as float[])
            if (CodecGroup != null)
            {
                var decodeDataset = CodecGroup.GetChild("Decode") as IDataset;

                // Use the explicit LUT if available
                if (decodeDataset != null)
                {
                    var codecAttributes = CodecAttributes.FromHdfAttributes(CodecGroup);
                    var lut = (float[])decodeDataset.Read();
                    Compander = new LutCompand(lut, codecAttributes);
                }
                // Otherwise fallback to the old way.
                else
                {
                    var codecAttributes = CodecAttributes.FromHdfAttributes(CodecGroup);
                    Compander = CodecAttributes.GetCompander(codecAttributes);
                }
            }
        }

        private void SetupFrameSet()
        {
            FrameSet = new FrameSet(
                (IDataset)TraceGroup.GetChild("HPFrameSet"),
                (IDataset)TraceGroup.GetChild("RVFrameSet"),
                (IDataset)TraceGroup.GetChild("VFrameSet"));
        }

        private float[, ,] spectraCache;
        private float[, ,] ReadAllRawSpectra()
        {
            var start = new long[] { 0, 0, 0 };
            var count = new[] { NumDyes, NumZmws, nRawCams };
            var outCount = new[] { NumDyes, NumZmws, nRawCams };
            
            // This appears to be an error - an unused allocation.
            //spectraCache = new float[NumDyes, NumZmws, NumCams];

            using (var rspace = SpectraDataset.Dataspace)
            {
                // Make a new dataspace to be used for this access
                rspace.SelectHyperslab(start, Ones3D, count, Ones3D);

                var target = Array.CreateInstance(typeof(float), outCount);
                SpectraDataset.Read(ref target, rspace);

                return (float[,,]) target;
            }
        }

        private float[,] ReadSpectrumByIdxCached(int n)
        {
            if (spectraCache == null)
                spectraCache = ReadAllRawSpectra();

            var spectra = Array2.Init((int)NumDyes, nRawCams, (i, j) => spectraCache[i, n, j]);

            // Transform here if there is a CameraProjection
            return fCamProjT == null ? spectra : fCamProjT.NativeLeftMultiply(spectra);
        }

        /// <summary>
        /// Apply CameraProjection to a signal vector.
        /// </summary>
        /// <param name="r"></param>
        /// <returns></returns>
        private float[] ProjectSignal(float[] r)
        {
            return fCamProj == null ? r : r.LeftMultiply(fCamProj);
        }

        /// <summary>
        /// A special transformation for the in-focus variance scale:
        /// This is an approximation; it produces the correct variance prediction in the special cases of:
        /// (1) Signals combined from two physical cameras into a virtual camera are equal in magnitude, and
        /// (2) There is a 1-1 mapping between a physical camera and a virtual camera (e.g., camera elimination).
        /// </summary>
        /// <param name="a"></param>
        /// <returns></returns>
        private float[] ProjectScale(float[] a)
        {
            return fCamProj == null
                       ? a
                       : a.LeftMultiply(fCamProj2).Select(
                           (v, i) => v == 0f ? 0f : v / fCamProjRSum[i]).ToArray();
        }

        /// <summary>
        /// Return input data or mean value in photons.
        /// This function may modify the values of the input array.
        /// </summary>
        /// <param name="r"></param>
        /// <returns></returns>
        private float[] ProjectAndRescaleSignal(float[] r)
        {
            return ToPhotonScale(ProjectSignal(r), PhotonScale);
        }

        /// <summary>
        /// Return input variance in photons^2.
        /// This function may modify the values of the input array.
        /// </summary>
        /// <returns></returns>
        private float[] ProjectAndRescaleVariance(float[] r)
        {
            // Handle the standard case (no projection)
            if (fCamProj2 == null)
            {
                return ToPhotonScale(r, (PhotonScale * PhotonScale));
            }

            // We have a diagonal camera co-variance matrix, and we
            // only keep diagonal elements, regardless of CamProjection.                
            //
            var vp = r.LeftMultiply(fCamProj2);

            // Zero variances are assigned +Infinity: they should
            // correspond to unused channels.
            //
            vp = vp.Select(v => v == 0f ? float.PositiveInfinity : v).ToArray();

            // Apply the rescaling)
            return ToPhotonScale(vp, (PhotonScale * PhotonScale));
        }

        /// <summary>
        /// Convert input values to an appropriate photon-based scale.
        /// </summary>
        /// <returns></returns>
        private float[] ToPhotonScale(float[] r, float countsToPhotons)
        {
            float cf = (Compander == null ? 1f : Compander.ToPhotons(countsToPhotons));

            // Just do the re-scaling.  A check for necessity here is a performance problem
            // in mono, since this method is used in function objects and Single.CompareTo()
            // is very slow.
            //
            for (int i = 0; i < r.Length; i++)
                r[i] *= cf;

            return r;
        }

        /// <summary>
        /// In channels that have a HolePhase = 1, frames are integrated at time n+1,  but stored in frame n.
        /// Therefore we must delay these channels by 1 frame. Currently the HolePhase handling only supports
        /// one frame of phase delay
        /// </summary>
        /// <typeparam name="T"></typeparam>
        /// <param name="n"></param>
        /// <param name="array"></param>
        private void FixHolePhase<T>(int n, T[,] array)
        {
            var holePhase = ReadHolePhase(n); // ReadHolePhaseByIdx(n);

            for(int i = 0; i < nRawChans; i++)
            {
                if(holePhase[i] == 1)
                {
                    for(var f = (int) (NumFrames - 1); f >= 1; f--)
                    {
                        array[i, f] = array[i, f - 1];
                    }
                }
                else if(holePhase[i] != 0)
                {
                    throw new PipelineTraceReaderException("HolePhase in subtracted, rounded frame must be 0 or 1 -- other values are not supported");
                }
            }
        }

        /// <summary>
        /// The function that reads Traces given an index into the stored trace array.
        /// This index must be converted from the zmwNumber by referencing the HoleNumber field
        /// Trace values are returned in units as defined by the file.
        /// </summary>
        /// <param name="n">Trace array index</param>
        /// <param name="factor">Multiplicative factor applied to the expanded data</param>
        /// <returns></returns>
        private AcquisitionTrace ReadTraceByIdx(int n, float factor = 1f)
        {
            // Create the container to hold the trace data
            var acqTrc = new AcquisitionTrace((int)NumChans, (int)NumFrames);
            
            // Read the raw data array
            var expand = ReadTraceIntoBufferGetExpand(n, factor);
            
            // Expand into the container
            expand(acqTrc);
            
            return acqTrc;
        }

        private Array readBuffer;
        private long bufferStartZmw = -1;
        private long bufferNumZmws = -1;

        // Do the HDF5 read into the pre-allocated dataArray
        private void DoRawTraceRead<T>(T[,] dataArray, int n)
        {
            var start = new[] { n, 0, FrameOffset };
            var count = new[] { 1, nRawChans, NumFrames };

            // Make a new dataspace to be used for this access
            using (var rspace = TraceDataset.Dataspace)
            {
                rspace.SelectHyperslab(start, Ones3D, count, Ones3D);

                var target = (Array)dataArray;
                TraceDataset.Read(ref target, rspace);
                
                FixHolePhase(n, (T[,])target);
            }           
        }

        /// <summary>
        /// Returns a function that expands the trace data for zmw n into the the supplied buffer.
        /// The read happens at the time this function is called, but any 'expanding' happens
        /// when the function is executed.  ReadTraceIntoBufferGetExpand() should be called on the
        /// HDF5 thread, the returned function can be called on a worker thread, so the expand()
        /// step is multithreaded.
        /// </summary>
        /// <param name="n">Trace array index</param>
        /// <param name="factor">An optional multiplicative factor, to specify units</param>
        /// <returns></returns>
        internal Action<AcquisitionTrace> ReadTraceIntoBufferGetExpand(int n, float factor = 0f)
        {
            // Multiplication factor to apply during expand operation
            if (factor == 0f)
            {
                // If not supplied, default to photon scale
                factor = (Compander == null ? 1f : Compander.ToPhotons(PhotonScale));
            }

            // Determine (.NET) the native data type
            var dataType = TraceDataset.Datatype.NativeType;

            // Determine the projection, if any
            var cproj = DoCamProjection ? fCamProj : null;

            // uint8 representation must have a Compander
            if (dataType == typeof (byte))
            {
                var targetRef = TLMemoryPool2D<byte>.Instance.Create((int) nRawChans, (int) NumFrames);
                DoRawTraceRead(targetRef.Contents, n);
                return acqTrc =>
                           {
                               acqTrc.Expand(targetRef.Contents, Compander, factor, cproj);
                               targetRef.Dispose();
                           };
            }

            // uint16 representation must have a Compander
            if (dataType == typeof (UInt16))
            {
                var targetRef = TLMemoryPool2D<UInt16>.Instance.Create((int) nRawChans, (int) NumFrames);
                DoRawTraceRead(targetRef.Contents, n);
                return acqTrc =>
                           {
                               acqTrc.Expand(targetRef.Contents, Compander, factor, cproj);
                               targetRef.Dispose();
                           };
            }

            // float representation is un-compressed
            if (dataType == typeof (float))
            {
                var targetRef = TLMemoryPool2D<float>.Instance.Create((int) nRawChans, (int) NumFrames);
                DoRawTraceRead(targetRef.Contents, n);
                return acqTrc =>
                           {
                               acqTrc.Expand(targetRef.Contents, factor, cproj);
                               targetRef.Dispose();
                           };
            }

            throw new Exception("Unsupported trace datatype");
            /*
            if (n % 250 == 0)
            {
                var leaks = new HDFLeakChecker((HDFFile) Chunks, true);
                Log(LogLevel.TRACE, "Trace Reader HDF Leak check: {0}", leaks.ToString());
            }
            */
        }

        /// <summary>
        /// The function that reads the Spectral matrix given an index into the stored trace array.
        /// This index must be converted from the zmwNumber by referencing the HoleNumber field
        /// </summary>
        /// <param name="n">Trace array index</param>
        /// <returns></returns>
        private float[,] ReadSpectrumByIdx(int n)
        {
            float[,] spectra;

            if (SpectraDataset.Dataspace.Dimensions.Length == 3)
            {
                var start = new long[] { 0, n, 0 };
                var count = new[] { NumDyes, 1, nRawCams };
                var outCount = new[] { NumDyes, nRawCams };

                using (var rspace = SpectraDataset.Dataspace)
                {
                    // Make a new dataspace to be used for this access
                    rspace.SelectHyperslab(start, Ones3D, count, Ones3D);

                    var target = Array.CreateInstance(typeof (float), outCount);
                    SpectraDataset.Read(ref target, rspace);
                    spectra = (float[,])target;
                }
            }
            else if (SpectraDataset.Dataspace.Dimensions.Length == 2)
            {
                var start = new long[] { n, 0 };
                var count = new long[] { 1, nRawCams };
                var outCount = new long[] { 1, nRawCams };

                using (var rspace = SpectraDataset.Dataspace)
                {
                    // Make a new dataspace to be used for this access
                    rspace.SelectHyperslab(start, Ones2D, count, Ones2D);

                    var target = Array.CreateInstance(typeof(float), outCount);
                    SpectraDataset.Read(ref target, rspace);
                    spectra = (float[,])target;
                }
            }
            else
                throw new Exception("Unrecognized data in Spectra");

            // Transform here if there is a CameraProjection
            return fCamProjT == null ? spectra : fCamProjT.NativeLeftMultiply(spectra);
        }

        /// <summary>
        /// The gizmo that converts the HolePhase as float to an int value
        /// </summary>
        /// <param name="hp"></param>
        /// <returns></returns>
        private static int[] TransformHolePhase(float[] hp)
        {
            var min = hp.Min();

            return hp.Map(v => (int)Math.Round(v - min));
        }
 
        /// <summary>
        /// Build a function to access a camera metric by ZMW index.  A camera metric has one 
        /// value per camera, so a total of NumCams values in the terminology used here.
        /// If <paramref name="isRequired"/> is true, an exception will be thrown if the
        /// dataset corresponding to <paramref name="name"/> is not found; otherwise
        /// a function will be built to supply the default <paramref name="defValue"/>.
        /// </summary>
        /// <typeparam name="T">The type stored in the HDF5 file</typeparam>
        /// <typeparam name="TR">The type returned by the access function</typeparam>
        /// <param name="name">Name of the metric in the trace HDF5</param>
        /// <param name="isRequired">Set to false for backward compatibility on new data</param>
        /// <param name="defValue">Default value to used when <paramref name="isRequired"/>=false and not found.</param>
        /// <param name="tform">A function to transform the data from its stored representation</param>
        /// <returns></returns>
        private Func<int, TR[]> MakeCameraMetricLookup<T,TR>(string name, bool isRequired,
                                                             TR defValue, Func<T[], TR[]> tform)
        {
            // Access the dataset
            var dataset = (IDataset)TraceGroup.GetChild(name);

            if (dataset == null)
            {
                if (isRequired)
                    throw new Exception(string.Format("Required dataset '{0}' not found.", name));

                // Otherwise, the default value will be supplied.
                return idx => nRawCams.Fill(chan => defValue);
            }

            // The reader function to return
            Func<int, TR[]> f;

            if (strict)
            {
                T[,,] cache = null;

                // In the strict case, we read everything up front once, cache it,
                // and return a function that doles out the data from the cache.
                f = delegate(int n)
                        {
                            if (cache == null)
                            {
                                // Here's the equivalent of the ReadAll method
                                var nFrameSets = dataset.Dataspace.Dimensions[1];
                                var start = new[] {0, nFrameSets - 1, 0};
                                var count = new[] { NumZmws, 1, nRawCams };
                                var outCount = new[] { NumZmws, 1, nRawCams };

                                using (var rspace = dataset.Dataspace)
                                {
                                    // Make a new dataspace to be used for this access
                                    rspace.SelectHyperslab(start, Ones3D, count, Ones3D);

                                    var target = Array.CreateInstance(typeof(T), outCount);
                                    dataset.Read(ref target, rspace);

                                    // Assigne the cache
                                    cache = (T[,,]) target;
                                }
                            }

                            // For the cached case, recale here.
                            return tform(nRawCams.Fill(i => cache[n, 0, i]));
                        };

                return f;
            }

            // Otherwise, return the (memoized) function that reads on demand
            f = delegate(int n)
                    {
                        var nFrameSets = dataset.Dataspace.Dimensions[1];
                        var start = new[] {n, nFrameSets - 1, 0};
                        var count = new long[] { 1, 1, nRawCams };
                        var outCount = new long[] { nRawCams };

                        using (var rspace = dataset.Dataspace)
                        {
                            // Make a new dataspace to be used for this access
                            rspace.SelectHyperslab(start, Ones3D, count, Ones3D);

                            var target = Array.CreateInstance(typeof (T), outCount);
                            dataset.Read(ref target, rspace);

                            return tform((T[]) target);
                        }
                    };

            return f.IndexedWeakMemoize((int) NumZmws);
        }

        #endregion

        #region IList

        public override IZmwTrace this[int zmwNum]
        {
            get
            {
                if (zmwNum >= 0 && zmwNum < NumZmws)
                    return ZmwTraces[zmwNum]();

                throw new IndexOutOfRangeException(String.Format(
                    "The requested zmwNum {0} is not available: {1}", zmwNum, sourceUri));
            }

            set { throw new NotImplementedException("Can't set to a TraceReader"); }
        }

        #endregion

        #region ISourceIdentifier

        public override string SoftwareVersion
        {
            get
            {
                try
                {
                    return ScanDataGroup.GetAttribute("SoftwareVersion").ReadSingleton<string>();
                }
                catch (Exception)
                {
                    return "Unknown Version";
                }
            }
        }

        public override string ChangelistID
        {
            get
            {
                try
                {
                    return ScanDataGroup.GetAttribute("ChangelistID").ReadSingleton<string>();
                }
                catch (Exception)
                {
                    return "Unknown Changelist";
                }
            }
        }

        public override Uri SourceDataUri
        {
            get { return sourceUri; }
        }

        public override DateTime DateCreated
        {
            get
            {
                try
                {
                    DateTime dateCreated;
                    var dateAttribute = TraceGroup.GetAttribute("DateCreated");
                    var dateString = dateAttribute.ReadSingleton<string>();
                    if (!DateTime.TryParse(dateString, out dateCreated))
                        throw new Exception();

                    return dateCreated;
                }
                catch (Exception)
                {
                    // Cheesy default value -- maybe we should fail if this doesn't exist
                    return new DateTime(1900, 1, 1);
                }
            }
        }

        #endregion
    }

    /// <summary>
    /// Provides access to trace data stored in the PacBio HDF5 Trace file format (*.trc.h5).
    /// This class implements ITraceSource for the multi-part trc.h5 case. 
    /// This class provides access to a series of IZmwTrace objects, either sequentially according
    /// to the data stored in the trace files, or by ZMW Number.
    /// </summary>
    /// </summary>
    public class TraceMultiPartReader : MultiPartSource<IZmwTrace>, ITraceSource
    {
        public TraceMultiPartReader(IEnumerable<Uri> uris, bool strict = false, int startOffsetSec = 0, int durationInSec = 0) :
            base(uris.Select(v => new TraceReader(v, strict, startOffsetSec, durationInSec) as DataSource<IZmwTrace>))
        {
 
        }

        public long FrameChunkSize
        {
            get { return ((TraceReader) parts[0]).FrameChunkSize; }
        }

        public IFrameSet FrameSet
        {
            get { return ((TraceReader) parts[0]).FrameSet; }
        }

        public IGroup CodecGroup
        {
            get { return ((TraceReader) parts[0]).CodecGroup;  }
        }

        public IAttribute[] TraceDataAttributes
        {
            get { return ((TraceReader) parts[0]).TraceDataAttributes;  }
        }

        public float[,] CameraProjection
        {
            // Return the projection of the first part
            get { return ((TraceReader)parts[0]).CameraProjection; }

            // Set the projection to each part
            set { parts.Apply(p => ((TraceReader)p).CameraProjection = value); }
        }

        public override void ValidateSource()
        {
            // Bug 19851
            // Check that we have a valid base map and all bases are accounted for.
            var bases = new char[] { 'T', 'G', 'A', 'C' }.Except(ZmwSource.Movie.Analogs.Select(a => Char.ToUpper(a.Base))).ToArray();
            if (bases.Length > 0)
            {
                var errMsg = String.Format("Incomplete base map detected, no analogs for bases: {0}", bases.Join(','));
                throw new PipelineTraceReaderMetadataException(errMsg);
            }
        }
    }

    public class ZmwMultiPartSource : MultiPartSource<ISequencingZmw>, IZmwSource
    {
        public ZmwMultiPartSource(IEnumerable<IZmwSource> zmwSources) :
            base(zmwSources.Select(v => v as DataSource<ISequencingZmw>))
        {
            
        }

        public string MovieName
        {
            get { return parts[0].Movie.MovieName; }
        }

        public string RunCode
        {
            get { return parts[0].Movie.RunCode; }
        }

        public string InstrumentName
        {
            get { return parts[0].Movie.InstrumentName; }
        }

        public uint InstrumentId
        {
            get { return parts[0].Movie.InstrumentId; }
        }

        public uint PlatformId
        {
            get { return parts[0].Movie.PlatformId; }
        }

        public string PlatformName
        {
            get { return parts[0].Movie.PlatformName; }
        }

        public CameraType CameraType
        {
            get { return parts[0].Movie.CameraType; }
        }

        public float FrameRate
        {
            get { return parts[0].Movie.FrameRate; }
        }

        public uint NumFrames
        {
            get { return parts[0].Movie.NumFrames; }
        }

        public int LaserOnFrame
        {
            get { return parts[0].Movie.LaserOnFrame; }
        }

        public int HotStartFrame
        {
            get { return parts[0].Movie.HotStartFrame; }
        }

        public float[] LaserIntensity
        {
            get { return parts[0].Movie.LaserIntensity; }
        }

        public float[] LaserPower
        {
            get { return parts[0].Movie.LaserPower; }
        }

        public float CameraBias
        {
            get { return parts[0].Movie.CameraBias; }
        }

        public float CameraBiasStd
        {
            get { return parts[0].Movie.CameraBiasStd; }
        }

        public float CameraGain
        {
            get { return parts[0].Movie.CameraGain; }
        }

        public float AduGain
        {
            get { return parts[0].Movie.AduGain; }
        }

        public sbyte[,] ChipMask
        {
            get { return parts[0].Movie.ChipMask; }
        }

        public uint NumLines
        {
            get { return parts[0].Movie.NumLines; }
        }

        public uint HolesPerLine
        {
            get { return parts[0].Movie.HolesPerLine; }
        }

        public IList<IAnalogSpec> Analogs
        {
            get { return parts[0].Movie.Analogs; }
        }

        public BaseMap BaseMap
        {
            get { return parts[0].Movie.BaseMap; }
        }

        public TemplateSpec? Template
        {
            get { return parts[0].Movie.Template; }
        }

        public IGroup ScanDataGroup
        {
            get { return parts[0].Movie.ScanDataGroup; }
        }

        public int GetIndexByHoleNumber(int holeNumber)
        {
            return HoleNumToIndex(holeNumber);
        }

        public int GetIndexByHoleXY(int x, int y)
        {
            return XYToIndex(x, y);
        }

        public ZmwIndexer ZmwIndexer
        {
            // No indexer obj is provided for the multi-part zmw source.
            get { throw new NotImplementedException(); }
        }
    }
}
