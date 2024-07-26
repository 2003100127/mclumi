__version__ = "v1.0"
__copyright__ = "Copyright 2024"
__license__ = "MIT"
__developer__ = "Jianfeng Sun"
__maintainer__ = "Jianfeng Sun"
__email__="jianfeng.sunmt@gmail.com"
__lab__ = "Cribbslab"

import os

from mclumi.bam.Bundle import Bundle
from mclumi.util.Parameter import Parameter


def run(
        method: str,
        bam_fpn : str,
        work_dir : str,
        verbose : bool,
        **kwargs
):
    controller = {
        'umi-tools': umi_tools,
    }
    return controller[method](
        bam_fpn=bam_fpn,
        work_dir=work_dir,
        verbose=verbose,
        **kwargs
    )


def umi_tools(
        bam_fpn,
        work_dir,
        params=None,
        verbose=False,
        **kwargs,
):
    print("===>Start converting reads to the bundle format by UMI-tools")
    if not params:
        params = Parameter().bundle_umi_tools
    file_name = os.path.basename(bam_fpn)
    base_name = os.path.splitext(file_name)[0]
    sv_fpn = work_dir + base_name + '_bundle.bam'
    df = Bundle(verbose=verbose).convert(
        options=params,
        in_fpn=bam_fpn,
        out_fpn=sv_fpn,
    )
    print("===>Conversion from reads to bundle finished!")
    return df


if __name__ == "__main__":
    from mclumi.path import to

    print(umi_tools(
        bam_fpn=to('data/example.bam'),
        params=Parameter().bundle_umi_tools,
        work_dir=to('data/'),
        verbose=True,
    ))

    print(run(
        method='umi-tools',
        bam_fpn=to('data/example.bam'),
        # params=Parameter().bundle_umi_tools,
        work_dir=to('data/'),
        verbose=True,
    ))
