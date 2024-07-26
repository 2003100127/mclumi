Example data used in this tutorial can be obtained as follows.

!!! info

    :simple-microgenetics:1. iCLIP. The Müller-McNicoll iCLIP dataset[^1] can be downloaded [here](https://github.com/cribbslab/mclumi/releases/download/v0.0.1/example_bundle.bam) and it contained 1,175,027 reads with 20,683 raw unique UMI sequences and 12,047 genomic positions tagged by running the `get_bundles` method of UMI-tools or the `mclumi.prep.run` function in mclUMI.

    :fontawesome-solid-code-fork:2. Single-cell RNA-seq. A single-cell dataset from 10X Genomics was downloaded from [here](http://cf.10xgenomics.com/samples/cell-exp/1.3.0/hgmm_100/hgmm_100_fastqs.tar). It contained 3,553,230 raw reads and left 588,963 reads after STAR (v2.7.9a)[^2] mapping against GRCh38 and gene annotations using featureCounts (v2.0.1)[^3]. The 100 barcodes were generated using the whitelist function of UMI-tools.

[^1]: Müller-McNicoll M, Botti V, de Jesus Domingues AM, Brandl H, Schwich OD, Steiner MC, et al. SR proteins are NXF1 adaptors that link alternative RNA processing to mRNA export. Genes Dev [Internet]. 2016;30:553–66. Available from: http://genesdev.cshlp.org/content/30/5/553.abstract

[^2]: Dobin A, Davis CA, Schlesinger F, Drenkow J, Zaleski C, Jha S, et al. STAR: ultrafast universal RNA-seq aligner. Bioinformatics [Internet]. 2012;29:15–21. Available from: https://doi.org/10.1093/bioinformatics/bts635 

[^3]: Liao Y, Smyth GK, Shi W. featureCounts: an efficient general purpose program for assigning sequence reads to genomic features. Bioinformatics [Internet]. 2013;30:923–30. Available from: https://doi.org/10.1093/bioinformatics/btt656
