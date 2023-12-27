__version__ = "v1.0"
__copyright__ = "Copyright 2024"
__license__ = "MIT"
__developer__ = "Jianfeng Sun"
__maintainer__ = "Jianfeng Sun"
__email__="jianfeng.sunmt@gmail.com"
__lab__ = "Cribbslab"

import click
from pyfiglet import Figlet

from mclumi import onepos
from mclumi import multipos
from mclumi import gene
from mclumi import sc

from mclumi.util.Parameter import Parameter
from mclumi.util.Console import Console

vignette1 = Figlet(font='slant')

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

console = Console()
console.verbose = True


class HelpfulCmd(click.Command):
    def format_help(self, ctx, formatter):
        click.echo(vignette1.renderText('mclUMI'))
        click.echo(
            """
            tool 
                locus | loci | bulk | sc
            
            method
                mcl | mcl_val | mcl_ed | unique | cluster | adjacency | directional

            example commands
                locus:
                    mclumi locus -m mcl -ed 1 -pfpn ./mclumi/data/params.yml -bfpn ./mclumi/data/example_.bam -wd ./mclumi/data/ -vb True
                loci:
                    mclumi loci -m mcl -ed 1 -pfpn ./mclumi/data/params.yml -bfpn ./mclumi/data/example_bundle.bam -wd ./mclumi/data/ -vb True
                bulk:
                    mclumi bulk -m mcl -ed 1 -pfpn ./mclumi/data/params.yml -bfpn ./mclumi/data/RM82CLK1_S3_featurecounts_gene_sorted.bam -wd ./mclumi/data/ -vb True
                sc:
                    mclumi sc -m mcl -ed 1 -pfpn ./mclumi/data/params.yml -bfpn ./mclumi/data/hgmm_100_STAR_FC_sorted.bam -wd ./mclumi/data/ -vb True
            
            """
        )


@click.command(cls=HelpfulCmd)
# @click.command()
@click.argument('tool', type=str)
@click.option(
    '-m', '--method', type=str, required=True,
    help="""
        method to use for UMI deduplication
    """
)
@click.option(
    '-ed', '--edit_distance', type=int, required=True,
    help="""
        an edit distance between two UMI sequences
    """
)
@click.option(
    '-pfpn', '--param_fpn', type=str, required=True,
    # required=True,
    help="""
        Path to a YMAL file
    """
)
@click.option(
    '-bfpn', '--bam_fpn', type=str, required=True,
    help="""
        Path to a bam file
    """
)
@click.option(
    '-wd', '--work_dir', type=str, required=True,
    help="""
        Path to store results in the work directory
    """
)
@click.option(
    '-vb', '--verbose', type=bool, default=True,
    help="""
        verbose prompts
    """
)
def main(
        tool,
        method,
        param_fpn,
        bam_fpn,
        work_dir,
        edit_distance,
        verbose,
):
    print(vignette1.renderText('mclUMI'))
    params = Parameter(param_fpn)
    print(params.dedup)
    print("===>The {} tool is being used...".format(tool))
    print("===>The {} method is being used...".format(method))
    tool_ins = {
        'locus': onepos,
        'loci': multipos,
        'bulk': gene,
        'sc': sc,
    }
    param_keys = [
        'mcl_fold_thres',
        'inflat_val',
        'exp_val',
        'iter_num',
        'pos_tag',
        'gene_assigned_tag',
        'gene_is_assigned_tag',
    ]
    if 'mcl_fold_thres' in param_keys:
        mcl_fold_thres = params.dedup["mcl_fold_thres"]
    if 'inflat_val' in param_keys:
        inflat_val = params.dedup["inflat_val"]
    if 'exp_val' in param_keys:
        exp_val = params.dedup["exp_val"]
    if 'iter_num' in param_keys:
        iter_num = params.dedup["iter_num"]
    if 'pos_tag' in param_keys:
        pos_tag = params.tag["pos_tag"]
    if 'gene_assigned_tag' in param_keys:
        gene_assigned_tag = params.tag["gene_assigned_tag"]
    if 'gene_is_assigned_tag' in param_keys:
        gene_is_assigned_tag = params.tag["gene_is_assigned_tag"]
    ### @@@ dedup
    tool_ins[tool].run(
        method=method,
        bam_fpn=bam_fpn,
        work_dir=work_dir,
        ed_thres=edit_distance,
        verbose=verbose,
        mcl_fold_thres=mcl_fold_thres,
        inflat_val=inflat_val,
        exp_val=exp_val,
        iter_num=iter_num,
        pos_tag=pos_tag,
        gene_assigned_tag=gene_assigned_tag,
        gene_is_assigned_tag=gene_is_assigned_tag,
    )
    return