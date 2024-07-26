## UMI-tools

UMI-tools provides a Bundle method to filter reads with high quality. Users can access this method through the `mu.prep.run` function as follows.

``` py linenums="1"
import mclumi as mu

df_mcl = mu.prep.run(
    method='umi-tools',
    bam_fpn=to('data/example.bam'),
    # params=Parameter().bundle_umi_tools,
    work_dir=to('data/'),
    verbose=True,
)
```

The following vignette shows how this function filters reads.

``` py
# Parameter().bundle_umi_tools

{
    'stats': 'deduplicated',
    'get_umi_method': 'read_id',
    'umi_sep': '_',
    'umi_tag': 'RX',
    'umi_tag_split': None,
    'umi_tag_delim': None,
    'cell_tag': None,
    'cell_tag_split': '-',
    'cell_tag_delim': None,
    'filter_umi': None,
    'umi_whitelist': None,
    'umi_whitelist_paired': None,
    'method': 'directional',
    'threshold': 1,
    'spliced': False,
    'soft_clip_threshold': 4,
    'read_length': False,
    'per_gene': False,
    'gene_tag': None,
    'assigned_tag': None,
    'skip_regex': '^(__|Unassigned)',
    'per_contig': False,
    'gene_transcript_map': None,
    'per_cell': False,
    'whole_contig': False,
    'detection_method': None,
    'mapping_quality': 0,
    'output_unmapped': False,
    'unmapped_reads': 'discard',
    'chimeric_pairs': 'use',
    'unpaired_reads': 'use',
    'ignore_umi': False,
    'ignore_tlen': False,
    'chrom': None,
    'subset': None,
    'in_sam': False,
    'paired': False,
    'out_sam': False,
    'no_sort_output': False,
    'stdin': "<_io.TextIOWrapper name='example.bam' mode='r' encoding='UTF-8'>",
    'stdlog': "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>", 'log2stderr': False,
    'compresslevel': 6,
    'timeit_file': None,
    'timeit_name': 'all',
    'timeit_header': None,
    'loglevel': 1,
    'short_help': None,
    'random_seed': None
}
```

As an example, the `example.bam` file can be downloaded [here](https://github.com/cribbslab/mclumi/releases/download/v0.0.1/example_bundle.bam). After conversion, the bam file will be named `example_bundle.bam`, which contains 1,175,027 reads having 20,683 raw unique UMI sequences observed at 12,047 genomic positions.

!!! info

    The bundle function from UMI-tools is currently the only method in mclUMI for filtering reads. Please stay tuned for more as the development of mclUMI.
