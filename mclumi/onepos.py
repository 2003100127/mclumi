__version__ = "v1.0"
__copyright__ = "Copyright 2024"
__license__ = "MIT"
__developer__ = "Jianfeng Sun"
__maintainer__ = "Jianfeng Sun"
__email__="jianfeng.sunmt@gmail.com"
__lab__ = "Cribbslab"

import pandas as pd
from pyfiglet import Figlet

from mclumi.deduplicate.OnePos import OnePos as onepos

from mclumi.util.Console import Console

vignette1 = Figlet(font='slant')

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

console = Console()
console.verbose = True


def run(
        method: str,
        bam_fpn : str,
        ed_thres : float,
        work_dir : str,
        verbose : bool,
        **kwargs
):
    controller = {
        'unique': unique,
        'cluster': cluster,
        'adjacency': adjacency,
        'directional': directional,
        'mcl': mcl,
        'mcl_val': mcl_val,
    }
    return controller[method](
        bam_fpn,
        ed_thres,
        work_dir,
        verbose,
        **kwargs
    )


def unique(
        bam_fpn : str,
        ed_thres : float,
        work_dir : str,
        verbose : bool,
        **kwargs
) -> pd.DataFrame:
    print(vignette1.renderText('mclUMI'))
    console.print('===>You are using method Unique to deduplicate UMIs observed at a genomic loci.')
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )
    return mclumi.unique()


def cluster(
        bam_fpn : str,
        ed_thres : float,
        work_dir : str,
        verbose : bool,
        **kwargs
) -> pd.DataFrame:
    print(vignette1.renderText('mclUMI'))
    console.print('===>You are using method Cluster to deduplicate UMIs observed at a genomic loci.')
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )
    return mclumi.cluster()


def adjacency(
        bam_fpn : str,
        ed_thres : float,
        work_dir : str,
        verbose : bool,
        **kwargs
) -> pd.DataFrame:
    print(vignette1.renderText('mclUMI'))
    console.print('===>You are using method Adjacency to deduplicate UMIs observed at a genomic loci.')
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )
    return mclumi.adjacency()


def directional(
        bam_fpn : str,
        ed_thres : float,
        work_dir : str,
        verbose : bool,
        **kwargs
) -> pd.DataFrame:
    print(vignette1.renderText('mclUMI'))
    console.print('===>You are using method Directional to deduplicate UMIs observed at a genomic loci.')
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )
    return mclumi.directional()


def mcl(
        bam_fpn : str,
        ed_thres : float,
        work_dir : str,
        verbose : bool,
        **kwargs
) -> pd.DataFrame:
    print(vignette1.renderText('mclUMI'))
    console.print('===>You are using method MCL to deduplicate UMIs observed at a genomic loci.')
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )
    return mclumi.mcl()


def mcl_val(
        bam_fpn : str,
        ed_thres : float,
        work_dir : str,
        verbose : bool,
        **kwargs
) -> pd.DataFrame:
    print(vignette1.renderText('mclUMI'))
    console.print('===>You are using method MCL-val to deduplicate UMIs observed at a genomic loci.')
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs,
    )
    return mclumi.mcl_val()


def mcl_ed(
        bam_fpn : str,
        ed_thres : float,
        work_dir : str,
        verbose : bool,
        **kwargs
) -> pd.DataFrame:
    print(vignette1.renderText('mclUMI'))
    console.print('===>You are using method MCL-ed to deduplicate UMIs observed at a genomic loci.')
    mclumi = onepos(
        bam_fpn=bam_fpn,
        ed_thres=ed_thres,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs,
    )
    return mclumi.mcl_ed()


if __name__ == "__main__":
    from mclumi.path import to

    # df_unique = unique(
    #     bam_fpn=to('data/example_bundle.bam'),
    #     ed_thres=1,
    #     work_dir=to('data/'),
    #     verbose=False,  # False True
    #
    #     heterogeneity=False,  # False True
    # )
    # print(df_unique)
    #
    # df_cluster = cluster(
    #     bam_fpn=to('data/example_bundle.bam'),
    #     ed_thres=1,
    #     work_dir=to('data/'),
    #     verbose=False,  # False True
    #
    #     heterogeneity=False,  # False True
    # )
    # print(df_cluster)
    #
    # df_adjacency = adjacency(
    #     bam_fpn=to('data/example_bundle.bam'),
    #     ed_thres=1,
    #     work_dir=to('data/'),
    #     verbose=False,  # False True
    #
    #     heterogeneity=False,  # False True
    # )
    # print(df_adjacency)
    #
    # df_directional = directional(
    #     bam_fpn=to('data/example_bundle.bam'),
    #     ed_thres=1,
    #     work_dir=to('data/'),
    #     verbose=False,  # False True
    #
    #     heterogeneity=False,  # False True
    # )
    # print(df_directional)

    df_mcl = mcl(
        bam_fpn=to('data/example_bundle.bam'),
        ed_thres=1,
        work_dir=to('data/'),
        verbose=False,  # False True

        heterogeneity=False,  # False True

        inflat_val=1.6,
        exp_val=2,
        iter_num=100,
    )
    print(df_mcl)

    df_mcl_val = mcl_val(
        bam_fpn=to('data/example_bundle.bam'),
        ed_thres=1,
        work_dir=to('data/'),
        verbose=False,  # False True

        heterogeneity=False,  # False True

        mcl_fold_thres=1.5,
        inflat_val=1.6,
        exp_val=2,
        iter_num=100,
    )
    print(df_mcl_val)

    df_mcl_ed = mcl_ed(
        bam_fpn=to('data/example_bundle.bam'),
        ed_thres=1,
        work_dir=to('data/'),
        verbose=False,  # False True

        heterogeneity=False,  # False True

        mcl_fold_thres=1.5,
        inflat_val=1.6,
        exp_val=2,
        iter_num=100,
    )
    print(df_mcl_ed)

