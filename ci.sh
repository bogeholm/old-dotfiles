#! /bin/bash

set -x

# Line lenght comfortable on 13" MacBook Pro in VS Code
black . --line-length 105

flake8

mypy --config-file=mypy.ini sync/ tests/

pylint sync/ #tests/

python -m pytest