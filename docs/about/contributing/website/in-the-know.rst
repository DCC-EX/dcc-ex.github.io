.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CONTRIBUTING-LOGO|

*********************************
Creating DCC-EX In the Know posts
*********************************

|conductor| |tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 3
    :local:

What is DCC-EX In the Know?
===========================

"DCC-EX In the Know" is our new announcements/news feed, using the Sphinx extension `ABlog <https://ablog.readthedocs.io/en/stable/>`_.

Given our website is static HTML pages hosted on GitHub Pages, we are limited on available options to provide a feed based content delivery system, so utilising existing blog functionality is the only suitable option.

Posting new content
===================

Posting new content is a simple matter of creating a reStructuredText formatted file in the "in-the-know/posts" directory of our website repository using the provided "post-template.txt" located in that same directory.

Providing the correct template format is maintained, there is no need to edit anything outside of the individual file being created, and the website should build correctly once a PR is submitted and merged with the Sphinx branch of the repository.

Using the post-template.txt template
====================================

To create a new post, copy the file "post-template.txt" to a new .rst file, with the name in reverse date format <yyyymmdd>.rst eg. 20230308.rst for a post on the 8th of March, 2023.

This new file must reside in the "in-the-know/posts" directory along with the other posts.

The content of the file should start like this:

.. code-block::

  .. include:: /include/include.rst
  .. include:: /include/include-l2.rst

  :blogpost: true
  :date: <date in format day month, year eg. 8 March, 2023>
  :author: <Your name, either Discord/GitHub username or real name>
  :category: <Refer to the doco for the category>
  :tags: <Refer to the doco for tags to use (comma separated list)>
  :excerpt: 1

  Post title
  ==========

  A catchy one-liner here to get people's interest, and this will show on the front page and in RSS/Atom feeds.

  The rest of the content goes here.

  Feel free to use our product shortcuts such as |DCC-EX|, |EX-CS|, |EX-TT|, |EX-R|, |EX-IO|, |EX-DCCI|, |EX-FC|.

Updating the metadata (date, author, category, tags)
----------------------------------------------------

The `:date:`, `:author:`, `:category:`, and `:tags:` metadata fields must be updated for each post.

- `:date:` - Add the date of the post eg. `:date: 8 March, 2023`
- `:author` - Your Discord or GitHub username, or full name if you're comfortable with that eg. `:author: peteGSX` or `:author: Peter Cole`
- `:category:` - One or more categories the post falls into, can be a comma separated list eg. `:category: News` or `:category: News, Release` (see :ref:`about/contributing/website/in-the-know:Valid categories and tags`)
- `:tags:` - One or more tags related to the post eg. `:tags: release, ex-commandstation` (see :ref:`about/contributing/website/in-the-know:Valid categories and tags`)
  
.. note::

  All other metadata/RST directives must remain intact as provided in the template, including the ".. include" lines, `:blogpost:`, and `:excerpt:`.

Valid categories and tags
^^^^^^^^^^^^^^^^^^^^^^^^^

Where possible, try to use consistent categories and tags for posts to make these easier to search for in future.

Suggested categories and tags are outlined below, more will occur naturally as these posts progress.

Categories:
~~~~~~~~~~~

- News - Use this for anything that is a general update on activities in general, probably relevant to most posts, and especially those that are just general activity updates
- Release - Use this when we have a new release happening, may relate to development, prod, bug fix, etc.

Tags:
~~~~~

- bug - Use this when we've identified a bug that needs to be fixed (probably used in conjunction with News category)
- bugfix - Use when a bug has been fixed, and when advising which version fixes it (probably used in conjunction with Release category)
- ex-commandstation
- ex-rail
- ex-installer
- ex-webthrottle
- ex-turntable
- ex-fastclock
- ex-ioexpander
- ex-dccinspector

Update the title
----------------

Provide a brief title that brings the reader's eye to the content.

Update the content
------------------

When updating the content, the first paragraph will appear as an excerpt on the front page of our website, so make it catchy to grab the reader's attention, but don't make it too long, as the goal is to encourage the reader to view the full post.

This paragraph will also appear in RSS/Atom feed readers as the preview.

When populating the rest of the content, you will be able to use all the product and other expansion names, logos, and so forth as we use throughout the website, and you can include images etc. just like any other documentation page.
