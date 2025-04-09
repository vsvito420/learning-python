# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'learning-python'
copyright = '2025, v.skolan'
author = 'v.skolan'

# -- General configuration ---------------------------------------------------
import sys
import os

# Add path to extensions
sys.path.append(os.path.abspath('.'))

extensions = [
    'recommonmark',
    'sphinx_rtd_theme',
]

# Add source file types
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document
master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Language settings
language = 'de'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------
def setup(app):
    from recommonmark.transform import AutoStructify
    app.add_config_value('recommonmark_config', {
            'enable_eval_rst': True,
            'auto_toc_tree_section': 'Contents',
            'enable_math': True,
            'enable_inline_math': True,
            'enable_auto_doc_ref': True,
        }, True)
    app.add_transform(AutoStructify)
