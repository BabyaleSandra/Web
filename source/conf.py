import sphinx_rtd_theme

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Your Project'
author = 'Your Name'
release = '0.1'

# -- General configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
]

todo_include_todos = True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
