.. include:: /include/include.rst
.. include:: /include/include-l2.rst
*************************
Folder and Page Structure
*************************

|conductor| |tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :depth: 4
      :local:

This page aims to describe the preferred general structure of how files (pages, images, downloads etc.) should be arranged and named, along with the preferred structure of the individual pages.

By being consistent with these, it will be a) a better user experience, and b) be easier to maintain the documentation.

reStructuredText Standards
===========================

Please ensure to follow the standards below when creating or updating documentation to ensure the look and feel of the website remains consistent.

.. highlight:: rst

Elements
========

The elements of the documentation fall into the following broad categories:

* `Folders`_
* `Pages`_
* :ref:`about/contributing/website/basic-rst:Image Types`
* :ref:`about/contributing/website/basic-rst:Documents / Files`
* :ref:`about/contributing/website/basic-rst:Image Artifacts` / originals   (used to create the images, but not part of the documentation)

Folders
=======

Folders *follow* the basic structure:

* Folder name

  * index.rst
  * getting-started.rst   or    overview.rst
  * ... .rst (as needed)

Every folder SHOULD have a 'index.rst' file which is the primary navigation point for the pages in the folder |BR| There are exceptions to this rule, but use them carefully.

Every folder SHOULD have either a 'getting-started.rst' OR and 'overview.rst' file which is the second navigation point for the pages in the folder |BR| There are exceptions to this rule (e.g. the Throttle options), but use them carefully.

Pages
=====

Pages *generally* follow the basic structure:

* Page Name (.rst file)
  
  * `Meta Keywords`_
  * `Includes`_
  * `Product Icon`_ (where appropriate)
  * `Page Heading`_
  * `Comfort Level Logos`_
  * `On This Page - Table of Contents`_ (on longer pages with multiple headings)
  * `Page Content`_
    * `Page Heading <Headings and Sub Headings>`_
    * Description or purpose of the page
    * `Other Headings <Headings and Sub Headings>`_

      * Text, links, images, etc.
      * ...
    
    * Next Steps Heading  (if it is part of sequence of pages this is mandatory)

Meta Keywords
-------------

The meta keywords help search entries find find the page based on key words. 

By using the recommended includes (below) several key meta keywords are included in all pages.  i.e. ``DCC DCC++ EX DCC++EX DCC-EX``
Generally each page should start with any additional meta keywords that are appropriate to the page.


For example, the meta tags for levels.rst are:

.. admonition:: Example

  ::

    .. meta::
    :keywords: Comfort Levels Conductor Tinkerer Engineer

Includes
--------

All pages MUST include two standard include files. ``/include/include.rst`` and, depending on the depth in the folder structure, one of following as the second file:

* ``/include/include-l0.rst``
* ``/include/include-l1.rst``
* ``/include/include-l2.rst``
* ``/include/include-l3.rst``

For example:

.. admonition:: Example

  ::

    .. include:: /include/include.rst
    .. include:: /include/include-l2.rst


.. note:: 
  :class: note-float-right

  The expansion must be followed by a blank line.

Product Icon
------------

If the page specifically and only relates to of the |DCC-EX| products, the specify  the product icon immediately after include files, but using the appropriate expansion:

For example:

.. admonition:: Example

  ::


    .. include:: /include/include.rst
    .. include:: /include/include-l3.rst
    |EX-CS-LOGO|

    ***************************************

Page Heading
------------

Each page must have a Main Heading. Main Headings MUST have asterisks above and below them:

.. admonition:: Example

  ::

    *************
    Main Heading
    *************

See below for more information about heading.

Comfort level logos
-------------------

On our :doc:`/levels` page, we refer to Conductor, Tinkerer, and Engineer level users, and where possible, we should be using these logos to help users understand what level the documentation is targeted at.

There are two types of logos available, one suitable for callouts or panels which are simply a square graphic, and one suitable for page headings that contains the graphic and the text.

* Where possible, use the expansions for the level images:

  * \|conductor\| |conductor|
  * \|tinkerer\| |tinkerer|
  * \|engineer\| |engineer|
  * \|conductor-no-text\| |conductor-no-text|
  * \|tinkerer-no-text\| |tinkerer-no-text|
  * \|engineer-no-text\| |engineer-no-text|

* Where possible, use the Team and Product names the expansions (not possible in headings)
  
  * \|DCC-EX\| for |DCC-EX|
  * \|EX-CS\| for |EX-CS|
  * \|EX-I\| for |EX-I|
  * \|EX-R\| for |EX-R|
  * \|EX-TT\| for |EX-TT|
  * \|EX-DCCI\| for |EX-DCCI|
  * \|BSC\| for |BSC|

* Where possible, use the expansions for the level text 

  * \|conductor-text\| |conductor-text|
  * \|tinkerer-text\| |tinkerer-text|
  * \|engineer-text\| |engineer-text|

Only if really necessary use image tags:

.. code-block:: 

  .. image:: /_static/images/conductor.png
    :alt: Conductor Level
    :scale: 40%
  
  .. image:: /_static/images/conductor-level.png
    :alt: Conductor Level 
    :scale: 40%

Refer to :ref:`about/contributing/website/basic-rst:images` below for details on how to include images, and set the scale as appropriate. A good example of the use of the different types of logos is the |EX-TT| :doc:`/ex-turntable/assembly` page.

----

On This Page - Table of Contents
--------------------------------

.. todo:: On This Page - Table of Contents

**todo** On This Page - Table of Contents



----

Page Content
------------

Page content can include:

* `Headings and Sub Headings`_
* `Text`_
* :ref:`about/contributing/website/basic-rst:Links / Hyperlinks`
* :ref:`about/contributing/website/basic-rst:Tables`
* `Including Images / Drawings <Images>`_

After the heading, the page should start with an explanation of the purpose of the page.

Headings and Sub Headings
^^^^^^^^^^^^^^^^^^^^^^^^^

* Main Headings have asterisks above and below them:

  .. code-block:: 

    ************
    Main Heading
    ************

* Subheadings are underlined with equals signs:

  .. code-block:: 

    Subheading
    ==========

* The next level is underlined with hyphens:

  .. code-block:: 

    Next level
    ----------

* And the next level is underlined with carets:

  .. code-block:: 

    Next level
    ^^^^^^^^^^

* The next one we use is underlined with tildes:

  .. code-block:: 

    Next level
    ~~~~~~~~~~

* The last one we use is underlined with underscores:

  .. code-block:: 

    Next level
    __________

All heading underlines and overlines must be at least as long as the text of the heading text.

----

Text
^^^^

.. todo::   text content

**TODO** text content

Refer to the :doc:`/about/contributing/website/basic-rst` and :doc:`/about/contributing/website/style-guide` 

----

Next steps - ReStucturedText Basics
===================================

Click next to learn how to enhance your content with links, tales, images, etc.