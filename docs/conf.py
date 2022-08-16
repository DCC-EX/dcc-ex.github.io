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

project = 'DCC-EX Model Railroading'
copyright = '2020-2022 - Fred Decker, Mani Kumar'
author = 'Dave Cutting, Fred Decker, Mani Kumar'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
   # 'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
   # 'sphinx.ext.coverage',
   # 'sphinx.ext.mathjax',
   # 'sphinx.ext.ifconfig',
   # 'sphinx.ext.viewcode',
   # 'sphinx.ext.graphviz',
   # 'sphinx_sitemap',
   # 'sphinx.ext.inheritance_diagram',
    'sphinxcontrib.spelling',
]  

autosectionlabel_prefix_document = True

spelling_lang='en_US'
tokenizer_lang='en_US'
spelling_word_list_filename = ['spelling_wordlist.txt']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store',
]

# Set the default for literal blocks and code-block
highlight_language = 'none'

# Automatically number figure captions
numfig = True

numfig_format = {'figure': 'Figure %s'}

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

html_favicon = "./_static/images/favicon.ico"

# Added commented out lines below for 'titles_only' and 'navigation_depth'.
# If we wish to have the menu expand to lower levels than just page titles,
# uncomment these lines and comment the other option out to enable this in
# the menu.
html_theme_options = {
    'style_nav_header_background': 'white',
    'logo_only': True,
    # Toc options
    'includehidden': True,
    # 'titles_only': False,
    'titles_only': True,
    'collapse_navigation': False,
    # 'navigation_depth': 3
     'navigation_depth': -1 
}
 
html_context = {
    'display_github': True,
    'github_user': 'DCC-EX',
    'github_repo': 'dcc-ex.github.io',
    'github_version': 'flash62au_restruct/docs/',
}

#leave this off to have todos invisible, set to true to render them and make the easy to see
#A list of all the todos in the document can be shown in the about page
todo_include_todos = True

#html_additional_pages = {
#    'exwebthrottle': 'exwebthrottle/index.html',
#}

html_css_files = [
    'css/dccex_theme.css',
    'css/big_picture_theme.css',
#    'css/layout.css',
#    'css/roundslider.min.css',
#    'css/throttle.css' 
]

html_js_files = [
    'js/platform.js',
    'js/extra.js',
#    'js/commandController.js',
#    'js/exwebthrottle.js',
#    'js/fnMaster.js',
#    'js/jquery-3.2.1.min.js',
#    'js/jquery-ui.min.js',
#    'js/roundslider.min.js',
#    'js/storageController.js'
]
