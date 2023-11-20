# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
import importlib.util
sys.path.append(os.path.abspath("./_ext"))
# sys.path.append("/pyraya/src")
# import raya

sys.path.insert(0, os.path.abspath("."))
import test_module

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

html_context = {
  'display_github': True,
  'github_user': 'Unlimited-Robotics',
  'github_repo': 'raya_documentation',
  'github_version': 'main'
}

html_sidebars = {
    '**': [
        'versioning.html',
    ],
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_show_sphinx = False
