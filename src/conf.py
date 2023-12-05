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

# sys.path.insert(0, os.path.abspath("."))
# import test_module

project = 'Raya Documentation'
copyright = '2023, Unlimited Robotics'
author = 'Unlimited Robotics'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 
              'myst_parser', 
              'raya_directives', 
              'sphinx_copybutton', 
              'notfound.extension', 
              'sphinx_search.extension', 
              'sphinx.ext.intersphinx', 
              'sphinxcontrib.youtube']

autodoc_default_options = {
    'members': True,
}

autodoc_member_order = 'groupwise'
autodoc_typehints = "description"



templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store', 'api/src.rst', 'doc/raya_python_library/controllers/folder_example_structure', 'pyraya']

html_context = {
  'display_github': False,
  'github_user': 'Unlimited-Robotics',
  'github_repo': 'raya_documentation',
  'github_version': 'main'
}

# html_sidebars = {
#     '**': [
#         'versioning.html',
#     ],
# }

# html_sidebars = {
#     "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
# }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']
html_show_sphinx = False
html_logo = "_static/logo.png"
html_favicon = '_static/favicon.png'


# # Material theme options (see theme.conf for more information)
# html_theme_options = {

#     # Set the name of the project to appear in the navigation.
#     'nav_title': 'Raya Documentation',

#     # Specify a base_url used to generate sitemap.xml. If not
#     # specified, then no sitemap will be built.
#     'base_url': 'https://unlimited-robotics.github.io/raya_documentation',

#     # Set the color and the accent color
#     'color_primary': 'blue',
#     'color_accent': 'dark-blue',
#     'html_minify': True,
#     'css_minify': True,

#     # Set the repo location to get a badge with stats
#     'repo_url': 'https://github.com/Unlimited-Robotics/raya_documentation/',
#     'repo_name': 'Raya Documentation',

#     # Visible levels of the global TOC; -1 means unlimited
#     'globaltoc_depth': 3,
#     # If False, expand all TOC entries
#     'globaltoc_collapse': False,
#     # If True, show hidden TOC entries
#     'globaltoc_includehidden': False,
# }


html_show_sourcelink = False
# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = "Raya Documentation",
    header_links = "Top 1|http://example.com/one, Top 2|http://example.com/two",
    logo = "logo_white.png",
    logo_alt = "Raya Documentation",
    logo_height = 720,
    logo_width = 153,
    # logo_url = "/raya_documentation",
    github_url = "https://github.com/Unlimited-Robotics/raya_documentation/tree/main/src/",
    footer_links = ",".join([
        "About Us|http://example.com/",
        "Contact|http://example.com/contact",
        "Legal|http://example.com/dev/null",
    ]),
)