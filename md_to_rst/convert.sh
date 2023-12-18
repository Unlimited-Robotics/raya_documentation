#!/bin/bash
pandoc $1 --from markdown --preserve-tabs --columns=1000 --to rst -s -o out.rst