from pkg_resources import Requirement, resource_filename

DATA_FILES = {'aligned_reads_1.cmp.h5':
                  ['m110818_075520_42141_c100129202555500000315043109121112_s1_p0.bas.h5',
                   'm110818_075520_42141_c100129202555500000315043109121112_s2_p0.bas.h5']}

def _getAbsPath(fname):
    return resource_filename(Requirement.parse('pbcore'),'pbcore/data/%s' % fname)

def getCmpH5s():
    '''
    Returns a list of dictionaries containing 2 keys: cmph5 and
    bash5s. The latter are the bash5s that were used to generate the
    cmp.h5 file.
    '''
    return [{'cmph5' : _getAbsPath(cmph5),
             'bash5s': map(_getAbsPath, bash5s)}
            for cmph5, bash5s in DATA_FILES.items()]

def getCmpH5():
    '''
    Returns the first cmp.h5 file in the list of available files. The
    returned value is a dictionary containing 2 keys: cmph5 and
    bash5s. The latter are the bash5s that were used to generate the
    cmp.h5 file.
    '''
    return getCmpH5s()[0]

def getBasH5s():
    return getCmpH5s()[0]["bash5s"]

def getGff3():
    '''
    Returns the filename of an example GFFv3 file
    '''
    return _getAbsPath("gff_example1.gff3")

def getFasta():
    '''
    Returns the filename of an example FASTA file.
    '''
    return _getAbsPath('Fluidigm_human_amplicons.fasta')
