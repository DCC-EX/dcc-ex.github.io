# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'DCC++ EX'
copyright = '2020, Dave Cutting, Fred Decker, Mani Kumar'
author = 'Dave Cutting, Fred Decker, Mani Kumar'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autosectionlabel"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "./_static/images/logo.png"

html_theme_options = {
    'logo_only': False,
    'style_nav_header_background': 'white',
    'logo_only': True,
    # Toc options
    'includehidden': True,
    'titles_only': True
}

html_additional_pages = {
    'exwebthrottle': 'exwebthrottle/index.html',
}

# add the extra js and css files needed for exwebthrottle
def setup(app):
    app.add_css_file('css/layout.css')
    app.add_css_file('css/roundslider.min.css')
    app.add_css_file('css/throttle.css')
    app.add_js_file('js/commandController.js')
    app.add_js_file('js/exwebthrottle.js')
    app.add_js_file('js/fnMaster.js')
    app.add_js_file('js/jquery-3.2.1.min.js')
    app.add_js_file('js/jquery-ui.min.js')
    app.add_js_file('js/roundslider.min.js')
    app.add_js_file('js/storageController.js')