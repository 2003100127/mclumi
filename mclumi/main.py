__version__ = "v1.0"
__copyright__ = "Copyright 2024"
__license__ = "MIT"
__developer__ = "Jianfeng Sun"
__maintainer__ = "Jianfeng Sun"
__email__="jianfeng.sunmt@gmail.com"
__lab__ = "Cribbslab"

import os
import sys
import yaml
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
                locus | loci | bulk | single-cell
            @@@ gmat_bulk
                mclumi locus -pfpn ./mclumi/data/params.yml -bfpn ./mclumi/data/example_.bam -wd ./mclumi/data/ -ed 1 -m directional

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
    print(vignette1.renderText('PhyloTres'))
    params = Parameter(param_fpn)
    print(params.dedup)
    ### @@@ dedup
    if tool == "locus":
        print("===>The {} tool is being used...".format(tool))
        print("===>The {} method is being used...".format(method))
        mcl_fold_thres = params.dedup["mcl_fold_thres"]
        inflat_val = params.dedup["inflat_val"]
        exp_val = params.dedup["exp_val"]
        iter_num = params.dedup["iter_num"]
        onepos.run(
            method=method,
            bam_fpn=bam_fpn,
            work_dir=work_dir,
            ed_thres=edit_distance,
            verbose=verbose,
            mcl_fold_thres=mcl_fold_thres,
            inflat_val=inflat_val,
            exp_val=exp_val,
            iter_num=iter_num,
        )
    return