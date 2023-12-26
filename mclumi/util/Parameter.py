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
            param_fpn,
            verbose=True,
    ):
        self.console = Console()
        self.console.verbose = verbose
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



if __name__ == "__main__":
    p = Parameter(
        param_fpn='./params/param_fpn.txt'
    )