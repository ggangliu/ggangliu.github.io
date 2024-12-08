# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import sphinx
import datetime

project = 'ggangliu-doc'
copyright = '2024, ggangliu'
author = 'ggangliu'
release = 'v0.01'
version = 'v0.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

master_doc = 'index'

extensions = []

templates_path = ['_templates']
exclude_patterns = []

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' #'alabaster'
html_static_path = ['_static']
html_logo = ''
html_favicon = ''
html_css_files = ['_variables.scss',]
html_copy_source = False
html_show_sphinx = True

simplepdf_vars = {
    'cover-overlay': 'rgba(26, 150, 26, 0.7)',
    'primary-opaque': 'rgba(26, 150, 26, 0.7)',
    'cover-bg': 'url(bg_cover.jpg) no-repeat center',
    'primary': '#1a961a',
    'secondary': '#379683',
    'cover': '#ffffff',
    'white': '#ffffff',
    'links': '#1a961a',
    'top-left-content': '',
    'top-center-content': 'string(heading)',
    'top-right-content': '',
    'bottom-left-content': 'counter(page)',
    'bottom-center-content': '',
    'bottom-right-content': '"ggangliu-doc"',
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

source_parsers = {
    '.md': 'myst_parser',
}


# conf.py 
extensions = ['myst_parser',  
              #'recommonmark',
              'sphinx_simplepdf', 
              'sphinx.ext.todo',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              #'rst2pdf.pdfbuilder', 
              'sphinx_markdown_parser',
              'sphinx_markdown_tables',
              'sphinxcontrib.mermaid',
              #'sphinx.ext.autosectionlabel',
              #'sphinxcontrib.pdfembed',
              ]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

latex_elements = {
'preamble': '''
\\hypersetup{unicode=true}
\\usepackage{CJKutf8}
\\AtBeginDocument{\\begin{CJK}{UTF8}{gbsn}}
\\AtEndDocument{\\end{CJK}}
''',
}

mermaid_cmd = 'mmdc'