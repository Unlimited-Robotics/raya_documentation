# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = src
BUILDDIR      = docs

# API docstring options
SPHINX_APIDOC_OPTIONS ?= members,undoc-members
export SPHINX_APIDOC_OPTIONS

# Python RaYa library path
PYRAYA_PATH = $(HOME)/ur_dev/pyraya
export PYRAYA_PATH

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

buildapi:
	sphinx-apidoc -fMeET --templatedir=./src/_templates $(PYRAYA_PATH)/src/raya -o ./src/api
	@echo "Auto-generation of API documentation finished. " \
			"The generated files are in 'api/'"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
