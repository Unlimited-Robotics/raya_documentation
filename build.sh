#!/bin/bash
set -e
source ./raya-documentation-venv/bin/activate

# Remove old generated files
rm -R ./docs || true

# Compile documentation
(cd ./src; sphinx-build -M html . ./_build)
mv ./src/_build/html ./docs
rm -r ./src/_build/*

deactivate