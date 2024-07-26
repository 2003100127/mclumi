## Input

The input file in [BAM](https://support.illumina.com/help/BS_App_RNASeq_Alignment_OLH_1000000006112/Content/Source/Informatics/BAM-Format.htm) format is only acceptable by mclUMI with each read umi attached to the read name. If you hold [FASTQ](https://knowledge.illumina.com/software/general/software-general-reference_material-list/000002211) file, you need to map the `*.fastq.gz` to a reference genome to yield a bam file using a mapping tool, such as Minimap2, HISAT2, or STAR, according to different sequencing reads.

!!! note

    In single cell sequencing read analysis, barcodes will be attached to the read name yet prior to their UMIs.

## Output

mclUMI outputs a series of files after UMI deduplication or collapsing. It has two files for recording statistics involved and one bam file as deduplicated reads. Please see details at <a href="https://2003100127.github.io/mclumi/tutorial/I.-UMI-deduplication/1.-Single-locus/">4 different UMI deduplication levels</a>.