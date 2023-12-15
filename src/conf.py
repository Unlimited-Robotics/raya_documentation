# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
sys.path.append(os.path.abspath("./_ext"))

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
              'sphinxcontrib.youtube',
              'sphinx.ext.autosectionlabel']

autodoc_default_options = {
    'members': True,
}

autodoc_member_order = 'groupwise'
autodoc_typehints = "description"

PYRAYA_PATH = os.path.abspath("./pyraya/src/raya")+'/'

templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store', 'api/src.rst', 'doc/raya_python_library/controllers/folder_example_structure', 'pyraya', 'sphinx-wagtail-theme']

html_context = {
  'display_github': False,
  'github_user': 'Unlimited-Robotics',
  'github_repo': 'raya_documentation',
  'github_version': 'main'
}

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

html_show_sourcelink = False
# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    collapse_navigation = True,
    project_name = "Raya Documentation",
    header_links = "Top 1|http://example.com/one, Top 2|http://example.com/two",
    logo = "logo.png",
    logo_dark = "logo_white.png",
    logo_url = "https://www.unlimited-robotics.com/",
    logo_alt = "Raya Documentation",
    logo_height = 720,
    logo_width = 153,
    favicon= "favicon2.png",
    github_url = "https://github.com/Unlimited-Robotics/raya_documentation/tree/main/src/",
    footer_links = ",".join([
        "About Us|http://example.com/",
        "Contact|http://example.com/contact",
        "Legal|http://example.com/dev/null",
    ]),
    discord_url = 'https://discord.com/invite/Db7hrrePhn',
    github_url_project = 'https://github.com/Unlimited-Robotics',
    developers_url = 'https://developers.unlimited-robotics.com/',
)