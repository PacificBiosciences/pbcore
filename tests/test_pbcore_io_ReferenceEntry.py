from pbcore.io import ReferenceEntry, ReferenceIndex
import os

class TestReferenceRepository:

    def test_ReferenceEntry(self):
        outdir = os.system( 'mkdir -p .tmp' )
        outfile = open( '.tmp/tmp.xml', 'w' )
        print >>outfile, \
"""<?xml version="1.0"?>
<reference_info id='hsapiens.36.3' name="reference.info.xml" version="1.0.0">
  <reference>
    <description>Homo sapiens</description>
    <num_contigs>24</num_contigs>
    <max_contig_length>250000000</max_contig_length>
  </reference>
  <contigs>
    <contig id="ref000001" displayName="chr1" length="225000000">
      <file>homo_sapiens/sequence/whole_genome_human.fasta</file>
      <source>internal assembly from ftp://ftp.ncbi.nih.gov/genomes/MapView/Homo_sapiens/sequence/BUILD.36.3/initial_release</source>
    </contig>
  </contigs>
  <ideogram>
    <file>homo_sapiens/NCBI/ideogram.gz</file>
    <source>ftp://ftp.ncbi.nih.gov/genomes/MapView/Homo_sapiens/sequence/BUILD.36.3/initial_release/ideogram.gz</source>
  </ideogram>
  <image>
    <file>homo_sapiens/human.image.jpg</file>
  </image>
  <web>
    <home>http://genome.ucsc.edu</home>
    <rss_feed>http://www.pacificbiosciences.com/rss?homo_sapiens</rss_feed>
  </web>
  <annotations>
    <annotation name="SMRTbell Adapters" type="adapter">
      <file format="text/gff3">./annotations/bsub_adapters.gff</file>
    </annotation>
  </annotations>
</reference_info>"""
        outfile.close()
        entry = ReferenceEntry( '.tmp' ) 
        print 'entry id is %s' % entry.id
        for contig in entry.contigs:
            print str(contig)
        for annotation in entry.annotations:
            print str(annotation)
        os.system( 'rm -rf .tmp' )

    def test_ReferenceIndex(self):
        outdir = os.system( 'mkdir -p .tmp' )
        outfile = open( '.tmp/tmp.xml', 'w' )
        print >>outfile, \
"""<?xml version="1.0"?>
<reference_index>
  <properties>
    <test>Testing</test>
  </properties>
  <reference>
    <name>1_WRM0639cE06 Fosmid (C. elegans)</name>
    <version>1</version>
    <id>1_WRM0639cE06</id>
    <fasta>celegans/1_WRM0639cE06/sequence/1_WRM0639cE06.fsta</fasta>
    <metadata>celegans/1_WRM0639cE06/reference.info.xml</metadata>
    <last_modified>Fri Dec 04 15:03:31 PDT 2009</last_modified>
    <type>control</type>
  </reference>
</reference_index>"""
        outfile.close()
        index = ReferenceIndex( '.tmp/tmp.xml' )
        print index.toXml()
        os.system( 'rm -rf .tmp' )
