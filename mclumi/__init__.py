__all__ = [
    'deduplicate',
    'fastq',
    'util',
]

from .deduplicate import *
from .fastq import *
from .util import *
from .main import *
from .path import *

# ## /*** block. local ***/
# try:
#     from mclumi.deduplicate import *
#     from mclumi.fastq import *
#     from mclumi.util import *
#     from mclumi.Main import *
#     from mclumi.Path import *
# except ImportError:
#     pass