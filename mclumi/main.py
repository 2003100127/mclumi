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
                dedup_op | dedup_mp | dedup_bulk | dedup_sc
            @@@ gmat_bulk
                phylotres gmat_bulk -rfpn D:/Programming/R/R-4.3.2/ -nspl 2 -ngene 10 -gsimulator spsimseq -wd ./phylotres/data/spsimseq_bulk.h5 -is True -vb True

            """
        )


# @click.command(cls=HelpfulCmd)
@click.command()
@click.argument('tool', type=str)
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
    '-ed', '--edit_distance', type=int, required=True,
    help="""
        an edit distance between two UMI sequences
    """
)
@click.option(
    '-m', '--method', type=str, required=True,
    help="""
        method to use for UMI deduplication
    """
)
@click.option(
    '-vb', '--verbose', type=int,
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
    params.dedup['dedup']
    ### @@@ dedup
    if tool == "dedup_op":
        onepos.run(
            method=method,
            bam_fpn=bam_fpn,
            work_dir=work_dir,
            ed_thres=edit_distance,
            verbose=verbose,
        )
    return