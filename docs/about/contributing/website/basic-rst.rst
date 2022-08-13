.. include:: /include/include.rst
.. include:: /include/include-l2.rst
***********************
ReStructuredText Basics
***********************

|conductor| |tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :depth: 4
      :local:

This page aims to describe the basics of using ReStructuredText for the |DCC-EX| documentation/website to enhance the basic text.

By being consistent with these, it will be a) a better user experience, and b) be easier to maintain the documentation.

reStructuredText Standards
===========================

Please ensure to follow the standards below when creating or updating documentation to ensure the look and feel of the website remains consistent.

.. highlight:: rst


Links / Hyperlinks
^^^^^^^^^^^^^^^^^^

Internal - Same Page
~~~~~~~~~~~~~~~~~~~~

.. todo::   internal links - same page

Sphinx cross-references are used for internal links in the same document/page. This ensures they are correct and by default will use the destination heading text as the link text.

These take either of two forms. **Preferred form**:

.. admonition:: Example

  ::

    `Internal - Same page`_

    `some other text to apper in the apage <Internal - Same page>`_

or 

.. admonition:: Example

  ::

    :ref:`Internal - Same page`

    :ref:`some other text to apper in the apage <Internal - Same page>`


Internal - To a Different Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sphinx cross-references are used for internal links. This ensures they are correct and by default will use the destination heading text as the link text.

To link to a page use ``:doc:``:

.. admonition:: Example

  ::

    :doc:`/reference/hardware/motor-boards`

  :doc:`/reference/hardware/motor-boards`

The document name is a relative or absolute (within the documentation) file
path, without the .rst suffix.  Absolute are generally safer.

Internal - To a Sub Heading of a Different Page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To link to a position within a page use ``:ref:``. A reST label can be used as
the reference, but on the |DCC-EX| website headings are made available to use as
references:

.. admonition:: Example

  ::

    :ref:`advanced-setup/motor-board-config:Configure Using the Installer`

  :ref:`ex-commandstation/advanced-setup/motor-board-config:Configure Using the Installer`

The reference is the full name of the document (the absolute path without
a leading /), a colon, and the section heading. The full name must be used
even when referring to headings in the same source file.

Alternative text can be used for the link:

.. admonition:: Example

  ::

    :ref:`WiFi configuration <advanced-setup/supported-microcontrollers/wifi-mega:Short Version of Network Setup>`

  :ref:`WiFi configuration <ex-commandstation/advanced-setup/supported-microcontrollers/wifi-mega:Short Version of Network Setup>`

External
~~~~~~~~

For URLs that are shown, just use the URL:

.. admonition:: Example

    ::

        https://dcc-ex.com/index.html

    https://dcc-ex.com/index.html

To show link text instead of the URL:

.. admonition:: Example

    ::

        `TrainBoard Thread <https://www.trainboard.com/highball/index.php?threads/dcc-voltage-and-n-scale-locomotives.56342/>`_

    `TrainBoard Thread <https://www.trainboard.com/highball/index.php?threads/dcc-voltage-and-n-scale-locomotives.56342/>`_

For better accessibility, and generally clearer content, use `strong link text <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#accessibility>`_.

If the link will be used multiple times, or to keep the URL separate in the
source file, define a target:

.. admonition:: Example

    ::

        Link to the `DCC-EX home page`_.

        .. _DCC-EX home page: https://dcc-ex.com/index.html

    Link to the `DCC-EX home page <https://dcc-ex.com/index.html>`_.

Downloads or Important Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download buttons are created using the ``dcclink`` class, added using the
``.. rst-class::`` directive:

.. admonition:: Example

    ::

        .. rst-class:: dcclink

           `Official Release page <https://github.com/DCC-EX/CommandStation-EX/releases>`_

    .. rst-class:: dcclink

       `Official Release page <https://github.com/DCC-EX/CommandStation-EX/releases>`_

|force-break|

    .. rst-class:: dcclink-right

       `Official Release page <https://github.com/DCC-EX/CommandStation-EX/releases>`_

or (float right)...

.. admonition:: Example

    ::

        .. rst-class:: dcclink-right

           `Official Release page <https://github.com/DCC-EX/CommandStation-EX/releases>`_

Tables
^^^^^^

There are two recommended table types to use within our website.

The recommended option for tables that have CSS controlled formatting and are relatively easy to update, use the ``list-table`` reStructuredText directive.

.. code-block:: 

  .. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * - Heading 1
      - Heading 2
      - Heading 3
    * - Row 1 column 1
      - Row 1 column 2
      - Row 1 column 3
    * - Row 2 column 1
      - Row 2 column 2
      - Row 2 column 3
    * - Row 3 column 1
      - Row 3 column 2
      - Row 3 column 3

This will render a table like this:

.. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * - Heading 1
      - Heading 2
      - Heading 3
    * - Row 1 column 1
      - Row 1 column 2
      - Row 1 column 3
    * - Row 2 column 1
      - Row 2 column 2
      - Row 2 column 3
    * - Row 3 column 1
      - Row 3 column 2
      - Row 3 column 3

Alternatively, for simple tables that don't require specific formatting and aren't updated often, you can use the simple markdown style.

.. code-block:: 

  +----------------+----------------+----------------+
  | Heading 1      | Heading 2      | Heading 3      |
  +================+================+================+
  | Row 1 column 1 | Row 1 column 2 | Row 1 column 3 |
  +----------------+----------------+----------------+
  | Row 2 column 1 | Row 2 column 2 | Row 2 column 3 |
  +----------------+----------------+----------------+
  | Row 3 column 1 | Row 3 column 2 | Row 3 column 3 |
  +----------------+----------------+----------------+

This will render a table like this:

+----------------+----------------+----------------+
| Heading 1      | Heading 2      | Heading 3      |
+================+================+================+
| Row 1 column 1 | Row 1 column 2 | Row 1 column 3 |
+----------------+----------------+----------------+
| Row 2 column 1 | Row 2 column 2 | Row 2 column 3 |
+----------------+----------------+----------------+
| Row 3 column 1 | Row 3 column 2 | Row 3 column 3 |
+----------------+----------------+----------------+

Note that while these tables look very similar, adding and editing the markdown style table becomes quite cumbersome compared with ``list-table``.

Images
^^^^^^

Including images
~~~~~~~~~~~~~~~~

Include images with the ``.. image::`` and ``.. figure::`` directives. Horizontal positioning using the ``:align:`` option needs a bit of care.

Where possible e.g. if just presenting a single image, either don't use it, or choose ``:align: center``.

``:align: left`` (or right) allows multiple images to be shown on the same line (if the browser window is wide enough), or text to flow around the image. You may have to cancel this behaviour for the next content yourself.

A single ``|`` adds an additional blank line before the next paragraph in the output; before a heading, or if a blank line is not wanted use ``.. rst-class:: clearer``.  
  
The expansion ``\|force-break\|`` will create blank line that CANNOT be overlapped with 'FloatRight' element (e.g. an image, note or warning.)

Use a figure when including a caption. Sphinx will automatically number the figure. Add a ``:name:`` option to be able to refer to the figure in the text using ``:numref:`<figure name>```.


Image Types
===========

We typically prefer compressed PNG files, but can take JPG as well. The resolution should be 72dpi and at least 600 pixels wide (maximum 1200). We can size the images using Sphinx to reduce them as necessary to fit where we need them on the page.

Drawing and saving graphs and schemas
_____________________________________

Use `draw.io <https://app.diagrams.net/>`_ to keep compatibility and allow group collaboration on the same document. Not everyone has access to Microsoft Visio. Export any schema or graph from draw.io in PNG format, with settings if possible as outlined above.

Images, diagrams, and any other artefacts created by draw.io that aren't published on the website should still be committed to the documentation repository in GitHub to ensure other contributors can use these.

An `image-artefacts <https://github.com/DCC-EX/dcc-ex.github.io/tree/sphinx/image-artefacts/>`_ directory has been created in the documentation repository for this purpose. Any draw.io artefacts can be saved here and will not be published as part of the website build.

SVG images
__________

We are currently experimenting with using SVG images to provide contextual links to be embedded within the images so users can be linked directly to relevant documentation. For example, a Fritzing diagram of a CommandStation connected to some peripherals can be given context, and clicking on the relevant component can take you directly to that documentation page.

The simplest options for generating SVG images are `draw.io <https://app.diagrams.net/>`_ or `Inkscape <https://inkscape.org/>`_.

.. tip:: 

  Note that draw.io's native format is XML, with SVG as an export format, whereas Inkscape is a native SVG editor. There are some idiosyncrasies as a result, refer to the CSS section below.

Including SVG images within reStructuredText is a little more complex than a simple bitmap image, and will require some CSS to be used in addition to including the file. This section will be updated with further details when available.

To include the SVG file, use the ``raw:: html`` directive:

.. code-block:: 

  .. raw:: html
    :file: ../_static/images/image.svg

CSS for SVG images
__________________

SVG images can be effectively controlled by CSS, and the implementation of this is controlled via the overall "svg" CSS directive and/or standard CSS classes and IDs.

Given Inkscape is a native SVG editor, you can define the SVG ID relatively simply in the editor itself by using the built-in XML editor.

Draw.io,however, has no way to do this, meaning you need to edit the exported SVG by hand to set the SVG ID.

To cater for this, we've incorporated the generic behaviour of SVG images to be responsive by including the overall "svg" CSS directive in our CSS theme (dccex_theme.css):

.. code-block:: 

  svg {
    max-width: 100%;
    height: auto;
  }

This will ensure your SVG image's size is no larger than the width of the web browser's content window, and will scale up and down with the size of the browser window.

If you have a need to override this behaviour, you can either set the SVG image's ID tag as per the below, or you can implement a reStructuredText container element with an associated class.

.. code-block:: 

  .. container:: svg-override

    .. raw:: html
      :file: ../_static/images/image.svg

You would then need to add an appropriate CSS class to the theme:

.. code-block:: 

  .svg-override {
    width: 50%;
    height: 50%;
  }

If your SVG image contains an ID tag, you can simply use this "id" entry to map to the CSS theme, for example:

.. code-block:: 

  <svg id="svg-css-entry">...</svg>

To then ensure the SVG only occupies 50% of the page, this is added to the CSS theme:

.. code-block:: 

  #svg-css-entry {
    width: 50%;
    height: 50%;
  }

Going any further into the details and options of controlling SVGs via CSS is beyond the scope of this documentation, and beyond the knowledge of the author! The Internet or your local, friendly CSS guru are your best options to understand what is possible.

Documents / Files
=================

.. todo:: documents description

Image Artifacts
===============

.. todo:: image Artifacts description

Hiding pages and comments
==========================

If there is a need to hide a page from the toctree, or a need for a specific comment on a page that isn't part of the published content, use the techniques below.

Hidden Pages
_____________

Use the ``:orphan:`` tag with a comment below it saying "Remove orphan field when the document is added to a toctree". This will allow us to easily search for the word "orphan" to find incomplete pages and avoids triggering an error that there are pages without an entry in a toctree

.. code-block:: 

  :orphan:
  Remove orphan field above when the document is added to a toctree.

This is a handy tip for pages that are a long time in the making and aren't quite ready for publishing, or for pages that provide context in one specific scenario and could be confusing or misleading if included directly in a toctree.

Hidden comments
________________

You can hide notes or searchable placeholders by putting placing the text on a line with a space above and below and preceding it with two period and a space, for example ``.. This is a hidden comment``.

.. note:: 

  Remember to perform a :ref:`about/contributing/website/getting-started:sphinx build` prior to submitting any pull requests.

At this point, go to GitHub and issue a pull request for your branch to be pulled into the sphinx branch. Once it's merged in by one of the admins, your changes will go live!

----

Next steps - Style Guide
========================

Click next to learn how to best to write your content