import h5py
import numpy as np
import CmpH5Factory

class CmpH5Error( Exception ):
    pass

INTEGER_TYPES = ( int, long, np.uint32, np.int32 )

bases = 'ACGTacgt-N'
cMap = dict(zip('ACGTacgt-N','TGCAtgca-N'))

base2hexMap = {"A":1, "C":2, "G":4, "T":8, "a":1, "c":2, "g":4, "t":8, "-":0, "N":15}
rBase2hexMap = {"T":1, "G":2, "C":4, "A":8, "t":1, "g":2, "c":4, "a":8, "-":0, "N":15}
alignmentPairMap = {}
rAlignmentPairMap = {}

for b1 in bases:
    for b2 in bases:
        alignmentPairMap[ (base2hexMap[b1]<< 4) | base2hexMap[b2] ] = (b1,b2) 

for b1 in bases:
    for b2 in bases:
        rAlignmentPairMap[ (rBase2hexMap[b1]<< 4) | rBase2hexMap[b2] ] = (b1,b2) 

Basemap = np.array(['-', 'A', 'C', '-', 'G', '-', '-', '-',
                    'T', '-', '-', '-', '-', '-', '-', 'N'])
RBasemap = np.array(['-', 'T', 'G', '-', 'C', '-', '-', '-',
                     'A', '-', '-', '-', '-', '-', '-', 'N'])

fastQueryMap    = np.array([ alignmentPairMap[x][0] \
                                    if x in alignmentPairMap else "!" \
                                        for x in range(2**8) ])
fastTargetMap   = np.array([ alignmentPairMap[x][1] \
                                    if x in alignmentPairMap else "!" \
                                        for x in range(2**8) ])



# define the variable length string type.
# I put it here to make it easy to find
# and import.
VLSTR = h5py.new_vlen(str)

# These ID table relationships are defined
# by the .cmp.h5 spec, and so unless we want
# to change it so they have a defined 
# relationship (ie name+'ID'), we'll need
# to specify the relationships here.
idTableMapping = {  "/AlnGroup/Path"    : "/AlnGroup/ID",
                    "/MovieInfo/Exp"    : "/MovieInfo/ID",
                    "/MovieInfo/Run"    : "/MovieInfo/ID",
                    "/MovieInfo/Name"   : "/MovieInfo/ID",
                    "/RefGroup/Path"    : "/RefGroup/ID",
                    "/RefGroup/RefInfoID":"/RefGroup/ID",
                    "/RefInfo/FullName" : "/RefInfo/ID",
                    "/RefInfo/Length"   : "/RefInfo/ID",
                    "/RefInfo/MD5"      : "/RefInfo/ID" }

# Explicitly describes the mapping of foreign keys in a cmpH5 file
idMap = { "RefInfo"   : ( "RefGroup", "RefInfoID" ),
          "MovieInfo" : ( "AlnInfo",  "MovieID" ),
          "RefGroup"  : ( "AlnInfo",  "RefGroupID" ),
          "AlnGroup"  : ( "AlnInfo",  "AlnGroupID" ) }

V1_2_0 = "1.2.0"
V1_2_0_PB = "1.2.0.PB"
V1_2_0_SF = "1.2.0.SF"
V1_3_1  = "1.3.1"
V1_3_1_PB = "1.3.1.PB"
V1_3_1_SF = "1.3.1.SF"

DEFAULT_CMPH5_VER = V1_3_1_SF
SUPPORTED_VERSIONS = (V1_2_0, V1_2_0_PB, V1_2_0_SF, V1_3_1, V1_3_1_PB, V1_3_1_SF)


h5vlen = h5py.special_dtype( vlen=str )
uint32t = np.dtype("<u4")
uint8t = np.dtype(np.uint8)
float32t = np.dtype(np.float32)

type2str = { h5vlen:"VLEN_STR", uint32t:"uint32", uint8t:"uint8", float32t:"float32" }

# Here we define the set of possible pulse metric tables. 
# These may or may not exist in any given cmp.h5 file.
pulseTables = [ "PulseWidth", "pkmid", "StartTime", "IPD", "Light", "ClassifierQV", "QualityValue", "DeletionQV", "DeletionTag", "SubstitutionQV", "SubstitutionTag" ]

INDEX_DTYPE = 'u4'
INDEX_COLS = [   "AlnID", 
                 "AlnGroupID",
                 "MovieID", 
                 "RefGroupID",
                 "tStart",
                 "tEnd",
                 "RCRefStrand", 
                 "HoleNumber",
                 "SetNumber",
                 "StrobeNumber",
                 "MoleculeID",
                 "rStart",
                 "rEnd",
                 "MapQV",
                 "nM",
                 "nMM",
                 "nIns",
                 "nDel",
                 "Offset_begin",
                 "Offset_end",
                 "nBackRead",
                 "nReadOverlap" ] 

MAX_HOLE_NUMBER = 320000

REF_GROUP_PATH_TEMPLATE = "/ref%06d"
REF_GROUP_PATH_REGEX = "/ref(\d+)"

def revCompSeq(s):
    return "".join([cMap[c] for c in s[::-1]])

def basename(p): # hdf5 equivalent of os.path.basename()
    return p.split("/")[-1]

def astro_id_to_springfield_fields( id ):
    """try to convert an astro read identifier into a Springfield-compliant
    identifier."""
    # it would be better to get this redundant code by importing
    # but we don't want Springfield code dependent on Astro code
    # set defaults
    movieDate = "m000000"; movieTime = "000000"; 
    machine = "2nd"; block = "b00"; 
    segment = "0"; panel = "p0"; subreadId = "";
    zmwX = "x0"; zmwY = "y0"; runName = "1000000-1000";

    # parse the various flavors of ids
    id = id.split("|")[0] # remove any annotations
    if "/" in id:
        id, subreadId = id.split("/")
    fields = id.split("_")
    if len(fields) == 8:
        zmwX, zmwY, runName, movieDate, movieTime, machine, \
                                       panel, block = fields
        if len(block.split(".")) > 1:
            ( block, segment ) = block.split(".") # _block.subread
            subreadId = segment[1:]
    elif len(fields) == 9:
        zmwX, zmwY, runName, movieDate, movieTime, machine, \
                             panel, block, segment = fields
        subreadId = int(segment[1:])
    elif len(fields) == 5:
        zmwX, zmwY, runName, panel, subreadId = fields
        subreadId = int(subreadId[1:])
    elif len(fields) == 3 and "-" in fields[2]:
        zmwX, zmwY, runName = fields
    else:
        # if we get here, we're probably going to fail...
        # help debug this
        print >>sys.stderr, "Trying to parse unknown id format %s" % id 
        zmwX = "x%i" % int(fields[0]) # TODO is this really the best way to handle naive ids?
        # raise SystemExit, "Unknown len of fields %i" % len(fields)

    x, y = int(zmwX[1:]), int(zmwY[1:])
    zmwHoleNumber = (x-1)*93 + (y-1)

    return movieDate, movieTime, machine, int(panel[1:]), int(block[1:]), zmwHoleNumber, subreadId

def astro_id_to_springfield_id( id ):
    ( movieDateStamp, movieTimeStamp, machine,
    zmwSet, partOfStrobe, 
    zmwHoleNumber, subreadId ) = astro_id_to_springfield_fields(id)
   
    # changed the movie name back to match astro to save on headache (we need this to match a real file!) -drw
    movieName = '%s_%s_%s_p%d_b%d' % (movieDateStamp, movieTimeStamp, machine, zmwSet, partOfStrobe)
    readId = '%s/%d' % ( movieName, zmwHoleNumber )
    if len(subreadId) > 0:
        readId += "/%s" % subreadId
    return readId

def get_num_aligned_reads( cmpH5FN ):
    """Return the number of aligned reads in the supplied cmp.h5 file.
    Returns -1 if there's an exception."""
    reader = None
    try:
        reader = factory.create( cmpH5FN, 'r' )
        return reader.numReads
    finally:
        if reader: reader.close()
    return -1

def asPath( *args ):
    """Simple conversion from groups/datasets to a path"""
    return "/" + "/".join( args )

factory = CmpH5Factory.factory
