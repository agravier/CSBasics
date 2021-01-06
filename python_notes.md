## New project and repo

### Poetry

```shell
poetry new FOLDERNAME --name PACKAGENAME

cd FOLDERNAME

poetry install
```

In PyCharm, use `$HOME/.cache/pypoetry/virtualenvs/<VENV>/bin/python` as project
interpreter.

### Repo

```shell
git init

git add *

git commit -m "Create project structure"

git branch -M master
```

```shell
git remote add origin git@github.com:agravier/....

git push -u origin master
```

## CLI, basic i/o

Create _PACKAGENAME/cli.py_.

In _pyproject.toml_:

```toml
[tool.poetry.scripts]
ALIAS_NAME = 'PACKAGENAME.cli:cli'
```


### Standard library

```python
from __future__ import annotations
import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import IO, List


@dataclass
class Settings:
    input_file: Path

    @classmethod
    def from_cmdline_args(cls, args: argparse.Namespace) -> Settings:
        return cls(input_file=Path(args.input_file))


def parse_args() -> Settings:
    parser = argparse.ArgumentParser(
        description="Find gantry version specified in Buildkite pipeline file"
    )
    parser.add_argument(
        "--input-file",
        dest="input_file",
        help="Path to the input file",
        required=True,
    )
    args = parser.parse_args()
    return Settings.from_cmdline_args(args)


def parse_input_file(f: IO[str]) -> List[int]:
    return [int(e) for e in f]


def cli():
    settings = parse_args()
    with settings.input_file.open() as f:
        contents = parse_input_file(f)
    print(contents)

if __name__ == "__main__":
    cli()
```

### Typer + rich

```shell
poetry add typer
```

#### Simple case

```python
from typing import IO, List

import typer


def parse_input_file(f: IO[str]) -> List[int]:
    return [int(e) for e in f]


def cli(input_file: typer.FileText = typer.Option(...)):
    contents = parse_input_file(f=input_file)
    print(contents)


if __name__ == "__main__":
    typer.run(cli)
```

#### Subcommands and click arguments/options

```python
from typing import List

import click
import typer

cli = typer.Typer()


@cli.command()
def echo(text: str):
    print(text)


@cli.command()
@click.argument("numbers", type=int, nargs=-1)
def sort(numbers: List[int]):
    print(sorted(int(i) for i in numbers))


if __name__ == "__main__":
    cli()
```

### Click

TBC

```python

```

## Dev env and utilities

### Setup

```shell
poetry add --dev pytest mypy black isort dephell
```

Create _mypy.ini_:

```ini
[mypy]

python_version = 3.9
disallow_untyped_defs = True
allow_redefinition = True
warn_return_any = True
warn_unreachable = True
warn_unused_configs = True
```

Add to _pyproject.toml_:

```toml
[tool.dephell.main]
from = {format = "poetry", path = "pyproject.toml"}
to = {format = "setuppy", path = "setup.py"}

[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-q"
testpaths = [
    "tests",
]

[tool.isort]
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true
line_length = 88
```

Create editable installation of package.

```shell
dephell deps convert
pip install -e .
```

### Test / formatting scripts

_run_tests.py_

```shell
poetry run mypy PACKAGENAME &&
poetry run pytest
```

_run_formatters.py_

```shell
poetry run isort PACKAGENAME tests
poetry run black PACKAGENAME tests
```

## Serving basics

Based on FastAPI:

- [uvicorn-gunicorn-fastapi-docker](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker).
- [full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql)

Flask and variants:

- TBC

## Correctness and utility

- [attr](https://www.attrs.org/en/stable/examples.html)
- [pydantic]()