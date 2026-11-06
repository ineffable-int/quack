# Ineffable's copy of Quack

[Dao-AILab/quack](https://github.com/Dao-AILab/quack) (Apache-2.0) at the tag named in this
branch's history, plus the commits on branch `ineffable`. We install it as a uv git dependency
pinned to a commit.

What differs from upstream:

- The kernels import without torch. `quack/__init__.py`, `quack/dsl/__init__.py` and
  `quack/blockscaled/__init__.py` import their torch ops only when torch is installed
  (`quack/_optional.py`), and `quack/cute_dsl_utils.py`, `quack/epilogue/ops.py`,
  `quack/epilogue/quantize_out.py` and `quack/operand_transform/kinds.py` import torch only
  where their torch host interface needs it. With torch installed, imports behave as upstream.
- `pyproject.toml` moves torch, torch-c-dlpack-ext and einops from the dependencies to a
  `torch` extra.
- `quack.__version__` carries a `+ineffable.N` local label.

To move to a new upstream release, rebase `ineffable` onto its tag, bump the label, and check that
`import quack.gemm_default_epi` works without torch installed.
