__version__ = "v1.0"
__copyright__ = "Copyright 2024"
__license__ = "MIT"
__developer__ = "Jianfeng Sun"
__maintainer__ = "Jianfeng Sun"
__email__="jianfeng.sunmt@gmail.com"
__lab__ = "Cribbslab"

import pysam
import numpy as np
import pandas as pd
# import umi_tools.sam_methods as sam_methods
# UMItoolsSamMethods is originally from UMI-tools
from mclumi.external import UMItoolsSamMethods as sam_methods
from mclumi.util.Hamming import Hamming
from mclumi.util.Console import Console


class Bundle:

    def __init__(
            self,
            verbose=False,
    ):
        self.console = Console()
        self.console.verbose = verbose

    def edave(
            self,
            x,
            d,
    ):
        repr_nodes = d[x[1]]
        node_len = len(repr_nodes)
        if node_len != 1:
            ed_list = []
            for i in range(node_len):
                for j in range(i + 1, node_len):
                    ed_list.append(Hamming().general(
                        s1=repr_nodes[i],
                        s2=repr_nodes[j]
                    ))
            return np.ceil(sum(ed_list) / (len(ed_list)))
        else:
            return -1

    def convert(
            self,
            options,
            in_fpn,
            out_fpn,
    ):
        bundle_iterator = sam_methods.get_bundles(
            options,
            metacontig_contig=None,
        )
        infile = pysam.Samfile(in_fpn, 'rb')
        inreads = infile.fetch()
        num_bundled_pos = 0
        umis = []
        nInput = 0
        reads = []
        uniq_umi_cnt = 0
        write_to_bam = pysam.AlignmentFile(out_fpn, "wb", template=infile)
        for i, (bundle, key, status) in enumerate(bundle_iterator(inreads)):
            # print([bundle[umi]["read"] for umi in bundle])
            for j, umi in enumerate(bundle):
                read = bundle[umi]["read"]
                read.set_tag('PO', i)
                for _ in range(bundle[umi]["count"]):
                    reads.append(bundle[umi]["read"])
                uniq_umi_cnt += 1
            nInput += sum([bundle[umi]["count"] for umi in bundle])

            umis.append([i.decode('utf-8') for i in bundle.keys()])
            num_bundled_pos += 1

        for y in reads:
            write_to_bam.write(y)
        write_to_bam.close()

        self.console.print('======># of unique reads: {}'.format(len(reads)))
        self.console.print('======># of bundled pos: {}'.format(num_bundled_pos))
        self.console.print('======># of repeated UMIs in total: {}'.format(nInput))
        df = pd.DataFrame(index=np.arange(num_bundled_pos))
        df[1] = np.arange(num_bundled_pos)
        df[2] = df.apply(lambda x: self.edave(x, umis), axis=1)
        return df[2].value_counts()