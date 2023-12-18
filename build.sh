#!/bin/bash
set -e
source ./raya-documentation-venv/bin/activate

# Remove old generated files
rm -R ./docs/html/* ./docs/doctrees/* || true

# Compile documentation
(cd ./src; sphinx-build -M html . ./_build)
cp -r ./src/_build/html ./docs

deactivate