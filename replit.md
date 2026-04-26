# PixelMDL

A small interactive Python package providing simple console utilities (a quiz, a void challenge, a sprint printer, hello world, etc.).

## Project Layout

- `pixelmdl/__init__.py` — package source with the public functions (`hello`, `sprint`, `quiz`, `dumby`, `void`).
- `s.py` — entry-point script that imports the package and runs `px.quiz()`.
- `pyproject.toml` — Python project metadata.
- `.replit` — Replit environment config (Python 3.12 module).

## Running

The "PixelMDL Quiz" workflow runs `python s.py` in a console. Open the console to interact with the quiz prompts.

## Notes / Changes Made During Setup

- Renamed `PixelMDL/` → `pixelmdl/` so the package name is importable on Linux (case-sensitive filesystem) matching `import pixelmdl` in `s.py`.
- Renamed `__Init__.py` → `__init__.py` so Python recognizes it as the package's init module.
- Cleaned up `pyproject.toml` (the original had a malformed line where `modules = [...]` ran into the `authors` line).
