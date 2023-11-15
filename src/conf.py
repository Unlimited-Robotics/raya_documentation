# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
import importlib 
# sys.path.insert(0, os.path.abspath(os.getenv('PYRAYA_PATH')+"/src"))
sys.path.append(os.path.abspath("./_ext"))
PYRAYA_PATH=str(os.getenv('PYRAYA_PATH'))+'/src'
print('PYRAYA_PATH:', PYRAYA_PATH)
sys.path.append(PYRAYA_PATH)
print('Updated sys.path:', sys.path)
importlib.import_module('raya') 

project = 'Raya Documentation'
copyright = '2023, Unlimited Robotics'
author = 'Unlimited Robotics'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'myst_parser', 'raya_directives', 'sphinx_copybutton']

autodoc_default_options = {
    'members': True,
}
autodoc_member_order = 'groupwise'
autodoc_typehints = "description"


templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store', 'api/src.rst']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_show_sphinx = False
