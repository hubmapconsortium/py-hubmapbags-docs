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


# -- Project information -----------------------------------------------------

project = 'HuBMAP-BAGS'
copyright = '2021-2022 The Human BioMolecular Atlas Program'
author = 'Ivan Cao-Berg and Zishen Wen'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_issues', 'sphinx.ext.todo', 'sphinx.ext.viewcode', \
		'sphinx.ext.autodoc', 'sphinx.ext.mathjax', \
		'sphinx.ext.ifconfig','sphinx.ext.viewcode', \
		'sphinxcontrib.gist']

# GitHub issues
# Path to GitHub repo {group}/{project}  (note that `group` is the GitHub user or organization)
issues_github_path = "hubmapconsortium/py-hubmapbags"

# which is the equivalent to:
issues_uri = "https://github.com/{group}/{project}/issues/{issue}"
issues_prefix = "#"
issues_pr_uri = "https://github.com/{group}/{project}/pull/{pr}"
issues_pr_prefix = "#"
issues_commit_uri = "https://github.com/{group}/{project}/commit/{commit}"
issues_commit_prefix = "@"
issues_user_uri = "https://github.com/{user}"
issues_user_prefix = "@"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'logo_only': True,
                      'style_nav_header_background':'#efefef',
                      'titles_only': False,}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/logo.jpg'

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
