# lovely-planet

Endor Labs POC - sample Python project with known vulnerable dependencies. Uses `pyproject.toml` for pip-based builds.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
python -m lovelyplanet.app
```

## Test

```bash
pytest
```
