"""Whether torch is installed, for the modules that use it only in their torch ops and host helpers.

`importlib.util.find_spec("torch")` and a bare `import torch` are not reliable checks: CuTe DSL
appends its `base_dsl` directory, which holds a `torch.py`, to `sys.path`.
"""

import importlib.metadata


def torch_installed() -> bool:
    try:
        importlib.metadata.distribution("torch")
    except importlib.metadata.PackageNotFoundError:
        return False
    return True
