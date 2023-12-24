__version__ = "v1.0"
__copyright__ = "Copyright 2024"
__license__ = "MIT"
__developer__ = "Jianfeng Sun"
__maintainer__ = "Jianfeng Sun"
__email__="jianfeng.sunmt@gmail.com"
__lab__ = "Cribbslab"

import time
import pandas as pd

from mclumi.deduplicate.OnePos import OnePos as onepos


def unique(
        bam_fpn,
        ed_thres,
        work_dir,
        verbose,
        **kwargs
):
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )
    return mclumi.unique()


def cluster(
        bam_fpn,
        ed_thres,
        work_dir,
        verbose,
        **kwargs
):
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )
    return mclumi.cluster()


def adjacency(
        bam_fpn,
        ed_thres,
        work_dir,
        verbose,
        **kwargs
):
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )
    return mclumi.adjacency()


def directional(
        bam_fpn,
        ed_thres,
        work_dir,
        verbose,
        **kwargs
):
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )
    return mclumi.directional()


def mcl(
        bam_fpn,
        ed_thres,
        work_dir,
        verbose,
        **kwargs
):
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )
    return mclumi.mcl()


def mcl_val(

):
    onepos(
        bam_fpn=bam_fpn,
        mcl_fold_thres=1.5,
        inflat_val=1.6,
        exp_val=2,
        iter_num=100,
        ed_thres=1,
        work_dir=to('data/'),

        verbose=True,

    )
    return umiche.mcl_val()


def mcl_ed(

):
    onepos(
        bam_fpn=bam_fpn,
        mcl_fold_thres=1.5,
        inflat_val=1.6,
        exp_val=2,
        iter_num=100,
        ed_thres=1,
        work_dir=to('data/'),
        verbose=True,
    )
    return umiche.mcl_ed()
