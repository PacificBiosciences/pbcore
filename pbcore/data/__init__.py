#################################################################################
# Copyright (c) 2011-2015, Pacific Biosciences of California, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Pacific Biosciences nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE.  THIS SOFTWARE IS PROVIDED BY PACIFIC BIOSCIENCES AND ITS
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL PACIFIC BIOSCIENCES OR
# ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#################################################################################

from pkg_resources import Requirement, resource_filename

DATA_FILES = {'aligned_reads_1.cmp.h5':
                  ['m110818_075520_42141_c100129202555500000315043109121112_s1_p0.bas.h5',
                   'm110818_075520_42141_c100129202555500000315043109121112_s2_p0.bas.h5']}

MOVIE_NAME_14 = "m110818_075520_42141_c100129202555500000315043109121112_s1_p0"
MOVIE_NAME_20 = "m130522_092457_42208_c100497142550000001823078008081323_s1_p0"
MOVIE_NAME_21 = "m130731_192718_42129_c100564662550000001823085912221321_s1_p0"
MOVIE_NAME_23 = "m140912_020930_00114_c100702482550000001823141103261590_s1_p0"
MOVIE_NAME_CCS = "m130727_114215_42211_c100569412550000001823090301191423_s1_p0"
MOVIE_NAME_BC = "m140307_221913_42203_c100626172550000001823119008061414_s1_p0"

def _getAbsPath(fname):
    return resource_filename(Requirement.parse('pbcore'),'pbcore/data/%s' % fname)

def getBasH5_v20():
    return _getAbsPath(MOVIE_NAME_20 + '.bas.h5')

def getBaxH5_v20():
    return [_getAbsPath('.'.join((MOVIE_NAME_20, str(k), 'bax.h5')))
            for k in range(1,4)]

def getBasH5_v21():
    return _getAbsPath(MOVIE_NAME_21 + '.bas.h5')

def getBaxH5_v21():
    return [_getAbsPath('.'.join((MOVIE_NAME_21, str(k), 'bax.h5')))
            for k in range(1,4)]

def getBasH5_v23():
    return _getAbsPath(MOVIE_NAME_23 + '.bas.h5')

def getBaxH5_v23():
    return [_getAbsPath('.'.join((MOVIE_NAME_23, str(k), 'bax.h5')))
            for k in range(1,4)]

def getCCSH5():
    return _getAbsPath(MOVIE_NAME_CCS + '.1.ccs.h5')

def getCCSBAM():
    return _getAbsPath(MOVIE_NAME_CCS + '.ccs.bam')

def getBcH5s():
    return [_getAbsPath('.'.join((MOVIE_NAME_BC, str(k), 'bc.h5')))
            for k in range(1,4)]

def getCmpH5s():
    '''
    Returns a list of dictionaries containing 2 keys: cmph5 and
    bash5s. The latter are the bash5s that were used to generate the
    cmp.h5 file.
    '''
    return [{'cmph5' : _getAbsPath(cmph5),
             'bash5s': map(_getAbsPath, bash5s)}
            for cmph5, bash5s in DATA_FILES.items()]

def getCmpH5AndBas():
    '''
    The returned value is a dictionary containing 2 keys: cmph5
    and bash5s. The latter are the bash5s that were used to generate
    the cmp.h5 file.
    '''
    return getCmpH5s()[0]

def getCmpH5():
    return getCmpH5AndBas()["cmph5"]

def getBasH5s():
    return getCmpH5AndBas()["bash5s"]

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
    return map(_getAbsPath,
               ["1.4_bas_files.fofn",
                "2.0_bax_files.fofn",
                "2.1_bax_files.fofn",
                "2.1_ccs_files.fofn"])

def getBcFofn():
    return _getAbsPath("bc_files.fofn")


def getBamAndCmpH5():
    """
    Get a "matched" (aligned) BAM and cmp.h5 file
    """
    return (_getAbsPath("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0.aligned_subreads.bam"),
            _getAbsPath("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0.aligned_subreads.cmp.h5"))

def getBaxForBam():
    """
    Get the bax file that was mapped to produce the bam
    """
    return _getAbsPath("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0.1.bax.h5")

def getUnalignedBam():
    """
    Get the unaligned BAM file, corresponding to the same bax above
    """
    return _getAbsPath("m140905_042212_sidney_c100564852550000001823085912221377_s1_X0.subreads.bam")

def getEmptyBam():
    return _getAbsPath("empty.ccs.bam")
