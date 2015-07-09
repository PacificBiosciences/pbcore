MOVIE1 := m140905_042212_sidney_c100564852550000001823085912221377_s1_X0

all: $(MOVIE1).subreads.bam $(MOVIE1).aligned_subreads.cmp.h5 $(MOVIE1).aligned_subreads.bam

$(MOVIE1).subreads.bam: $(MOVIE1).1.bax.h5
	bax2bam $<
	samtools index $@
	pbindex $@

$(MOVIE1).aligned_subreads.bam: $(MOVIE1).subreads.bam lambdaNEB.fa
	pbalign $^ $@
	samtools index $@
	pbindex $@

$(MOVIE1).aligned_subreads.cmp.h5: $(MOVIE1).1.bax.h5 lambdaNEB.fa
	pbalign-2.3 --forQuiver $^ $@
