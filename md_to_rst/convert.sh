#!/bin/bash
pandoc $1 --from markdown --columns=100 --to rst -s -o out.rst