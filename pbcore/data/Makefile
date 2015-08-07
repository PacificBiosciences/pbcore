MOVIE1 := m140905_042212_sidney_c100564852550000001823085912221377_s1_X0

all: $(MOVIE1).subreads.bam $(MOVIE1).aligned_subreads.cmp.h5 $(MOVIE1).aligned_subreads.bam testdata upstream_testdata

$(MOVIE1).subreads.bam: $(MOVIE1).1.bax.h5
	bax2bam $<
	samtools index $@
	pbindex $@

$(MOVIE1).aligned_subreads.bam: $(MOVIE1).subreads.bam lambdaNEB.fa
	pbalign $^ $@
	samtools index $@
	pbindex $@

$(MOVIE1).aligned_subreads.cmp.h5: $(MOVIE1).1.bax.h5 lambdaNEB.fa
	pbalign-2.3 --forQuiver --metrics IPD,DeletionQV,DeletionTag,InsertionQV,MergeQV,SubstitutionQV $^ $@

testdata:
	dataset.py create --type ReferenceSet --relative datasets/pbalchemysim0.referenceset.xml datasets/pbalchemysim0.reference.fasta
	bax2bam datasets/pbalchemysim0.bas.h5 -o datasets/pbalchemysim0 --pulsefeatures DeletionTag,DeletionQV,InsertionQV,MergeQV,SubstitutionQV && \
	samtools index datasets/pbalchemysim0.subreads.bam
	pbindex datasets/pbalchemysim0.subreads.bam
	dataset.py create --type SubreadSet --relative datasets/pbalchemysim0.subreadset.xml datasets/pbalchemysim0.subreads.bam
	pbalign datasets/pbalchemysim0.subreads.bam datasets/pbalchemysim0.reference.fasta datasets/pbalchemysim0.pbalign.bam && \
	dataset.py create --type AlignmentSet --relative datasets/pbalchemysim0.alignmentset.xml datasets/pbalchemysim0.pbalign.bam
	dataset.py split --contigs --chunks 2 datasets/pbalchemysim0.alignmentset.xml
	dataset.py create --type AlignmentSet --relative datasets/pbalchemysim0.alignmentset.chunk0contigs.xml datasets/pbalchemysim0.alignmentset.chunk0contigs.xml
	dataset.py create --type AlignmentSet --relative datasets/pbalchemysim0.alignmentset.chunk1contigs.xml datasets/pbalchemysim0.alignmentset.chunk1contigs.xml
	bax2bam datasets/pbalchemysim1.bas.h5 -o datasets/pbalchemysim1 --pulsefeatures DeletionTag,DeletionQV,InsertionQV,MergeQV,SubstitutionQV && \
	samtools index datasets/pbalchemysim1.subreads.bam
	pbindex datasets/pbalchemysim1.subreads.bam
	dataset.py create --type SubreadSet --relative datasets/pbalchemysim1.subreadset.xml datasets/pbalchemysim1.subreads.bam
	pbalign datasets/pbalchemysim1.subreads.bam datasets/pbalchemysim0.reference.fasta datasets/pbalchemysim1.pbalign.bam && \
	dataset.py create --type AlignmentSet --relative datasets/pbalchemysim1.alignmentset.xml datasets/pbalchemysim1.pbalign.bam
	dataset.py create --type AlignmentSet --relative datasets/pbalchemysim.alignmentset.xml datasets/pbalchemysim0.alignmentset.xml datasets/pbalchemysim1.alignmentset.xml
	dataset.py create --type SubreadSet --relative datasets/subreadSetWithStats.xml datasets/pbalchemysim0.subreadset.xml
	dataset.py loadstats datasets/subreadSetWithStats.xml datasets/m150430_142051_Mon_p1_b25.sts.xml
	dataset.py loadstats datasets/subreadSetWithStats.xml datasets/m150616_053259_ethan_c100710482550000001823136404221563_s1_p0.sts.xml
	dataset.py create --type SubreadSet --relative datasets/subreadSetWithStats.xml datasets/subreadSetWithStats.xml
	dataset.py create --type HdfSubreadSet --relative datasets/pbalchemysim0.hdfsubreadset.xml datasets/pbalchemysim0.bas.h5
	dataset.py create --type HdfSubreadSet --relative datasets/pbalchemysim1.hdfsubreadset.xml datasets/pbalchemysim1.bas.h5
	dataset.py create --type HdfSubreadSet --relative datasets/pbalchemysim.hdfsubreadset.xml datasets/pbalchemysim0.bas.h5 datasets/pbalchemysim1.bas.h5

upstream_testdata:
	dataset.py create --type ReferenceSet --relative datasets/lambda.referenceset.xml lambdaNEB.fa
	dataset.py create --type AlignmentSet --relative datasets/lambda.alignmentset.xml $(MOVIE1).aligned_subreads.bam

xsdupdate:
	cp ../../../../../doc/FileFormats/examples/datasets/*.xml datasets/.

