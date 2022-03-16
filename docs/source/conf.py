# Configuration file for the Sphinx documentation builder.

project = 'TecPOS Point of Sale'
copyright = '2022, TecMeet Management'
author = 'TecMeet Management'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'myst_parser',
#     'sphinx.ext.duration',
#     'sphinx.ext.doctest',
#     'sphinx.ext.autodoc',
#     'sphinx.ext.autosummary',
#     'sphinx.ext.intersphinx',
#     'sphinx.ext.autosectionlabel',
]

# Make sure the target is unique
# autosectionlabel_prefix_document = True

# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
# }
# intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
