__version__ = "v1.0"
__copyright__ = "Copyright 2024"
__license__ = "MIT"
__developer__ = "Jianfeng Sun"
__maintainer__ = "Jianfeng Sun"
__email__="jianfeng.sunmt@gmail.com"
__lab__ = "Cribbslab"

import yaml
from mclumi.util.Console import Console


class Parameter:

    def __init__(
            self,
            param_fpn=None,
            verbose=True,
    ):
        self.console = Console()
        self.console.verbose = verbose
        if param_fpn:
            with open(param_fpn, "r") as f:
                self.params = yaml.safe_load(f)
                for i, (k, item) in enumerate(self.params.items()):
                    self.console.print("======>key {}: {}".format(i+1, k))
                    self.console.print("=========>value: {}".format(item))

    @property
    def dedup(self, ):
        return self.params['dedup']

    @property
    def tag(self, ):
        return self.params['tag']

    @property
    def work_dir(self, ):
        return self.params['work_dir']

    @property
    def bam_fpn(self, ):
        return self.params['bam_fpn']

    @property
    def bundle_umi_tools(self, ):
        return {
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



if __name__ == "__main__":
    p = Parameter(
        param_fpn='./params/param_fpn.txt'
    )