# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'python-reference'
copyright = '2024, Xiang Wang'
author = 'Xiang Wang'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        "myst_parser",
        "sphinx_design",
        "sphinx.ext.todo",
        "sphinx.ext.autodoc",
        'sphinxcontrib.mermaid',
        "sphinxmermaid",
        ]

templates_path = ['_templates']
exclude_patterns = [
        '_build',
        '.DS_Store',
        '.git'
        'Thumbs.db',
        ]

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
myst_enable_extensions = [
        "colon_fence",
        "strikethrough",
        "tasklist",
        "deflist",
        "fieldlist",
        "attrs_inline",
]
myst_heading_anchors = 7
html_css_files = [
        "custom.css"
        ]
source_encoding = "UTF-8"
todo_include_todos = True
latex_use_xindy = True
smartquotes = True
# mermaid_elk_use_local = "js"
# mermaid_use_local = "js"
# d3_use_local = "js"
suppress_warnings = [
    "myst.header",
    "myst.xref_missing",
]
html_css_files = [
    "custom.css"
]
todo_include_todos = True
latex_use_xindy = True
smartquotes = True
sphinxmermaid_mermaid_init = {
  'theme': 'base',
  'themeVariables': {
    'fontSize': '40px',
  }
}
