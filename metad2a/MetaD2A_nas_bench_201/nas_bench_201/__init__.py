import sys
from pathlib import Path

from metad2a.MetaD2A_nas_bench_201.nas_bench_201.architecture import (
    train_single_model,
)

dir_path = (Path(__file__).parent).resolve()
if str(dir_path) not in sys.path:
    sys.path.insert(0, str(dir_path))

__all__ = ["train_single_model"]
