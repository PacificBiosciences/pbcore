from __future__ import absolute_import, division, print_function

from builtins import map

from pkg_resources import Requirement, resource_filename

MOVIE_NAME_14 = "m110818_075520_42141_c100129202555500000315043109121112_s1_p0"
MOVIE_NAME_20 = "m130522_092457_42208_c100497142550000001823078008081323_s1_p0"
MOVIE_NAME_21 = "m130731_192718_42129_c100564662550000001823085912221321_s1_p0"
MOVIE_NAME_23 = "m140912_020930_00114_c100702482550000001823141103261590_s1_p0"
MOVIE_NAME_CCS = "m130727_114215_42211_c100569412550000001823090301191423_s1_p0"
MOVIE_NAME_BC = "m140307_221913_42203_c100626172550000001823119008061414_s1_p0"

def _getAbsPath(fname):
    return resource_filename(Requirement.parse('pbcore'),'pbcore/data/%s' % fname)

def getCCSBAM():
    return _getAbsPath(MOVIE_NAME_CCS + '.ccs.bam')

def getGff3():
    '''
    Returns the filename of an example GFFv3 file
    '''
    return _getAbsPath("variants.gff")

def getFasta():
    '''
    Returns the filename of an example FASTA file.
    '''
    return _getAbsPath('Fluidigm_human_amplicons.fasta')


def getTinyFasta():
    """
    Returns the filename of an example FASTA file.
    """
    return _getAbsPath('Fluidigm_human_amplicons_tiny.fasta')

def getLambdaFasta():
    """
    Returns the filename of the FASTA of the lambda phage reference.
    """
    return _getAbsPath('lambdaNEB.fa')

def getDosFormattedFasta():
    """
    Returns the filename of an example FASTA file with DOS line endings
    """
    return _getAbsPath('barcodes-ed65-450.fasta')

def getBlasrM4():
    return _getAbsPath('blasr-output.m4')

def getBlasrM5():
    return _getAbsPath('blasr-output.m5')

def getFofns():
    """
    Returns a list of FOFN files
    """
    return list(map(_getAbsPath,
               ["datasets/fofn.fofn"]))

def getBcFofn():
    return _getAbsPath("bc_files.fofn")


def getAlignedBam():
    """
    Get a mapped BAM file
    """
    return _getAbsPath("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0.aligned_subreads.bam")

def getUnalignedBam():
    """
    Get the unaligned BAM file, corresponding to the same bax above
    """
    return _getAbsPath("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0.subreads.bam")

def getEmptyBam():
    return _getAbsPath("empty.ccs.bam")

def getEmptyAlignedBam():
    return _getAbsPath("empty.aligned_subreads.bam")

def getMappingXml():
    return _getAbsPath("chemistry.xml")

def getWeird():
    return _getAbsPath("weird.fa")

def getEmptyBam2():
    return _getAbsPath("empty2.bam")
