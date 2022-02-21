***************
Documentation
***************

Thank you for your offer to help. Here's some instructions for how to contribute. You might want to check in with an admin from the DCC++ EX team before working on documentation changes to identify current needs.

Submission Procedure
======================

Simple changes to existing pages can be created without installing any tools,
by using the "Edit on GitHub" link. However, the preview provided on GitHub
does not fully reflect the final result. The steps listed here provide guidance
on how to make and preview more complex changes.

We will assume that you have an appropriate text editor and Git installed on
your machine. For Windows we recommend the free `Visual Studio Code IDE (VSC)
<https://code.visualstudio.com/>`_ and `GitHub Desktop <https://desktop.github.com/>`_
or `Git Bash (the command line interface in Git) <https://git-scm.com/downloads>`_.

1. Clone the `dcc-ex.github.io <https://github.com/DCC-EX/dcc-ex.github.io>`_
   website repository, to your local machine. After cloning make sure you're on
   the sphinx branch. (`Cloning a repository in GitHub
   <https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository>`_).

2. Install a current version of Python 3 (which also installs pip). The
   Microsoft Store contains Python published by the Python Software Foundation
   for Windows. Then use pip to install the required packages
   ``pip install sphinx sphinx_rtd_theme sphinxcontrib-spelling``.

3. Change location to the "website" folder ``dcc-ex.github.io`` and make a branch
   using GitHub desktop or this command: ``git checkout -b your-branch-name``.

4. Edit the files in the ``dcc-ex.github.io/docs`` folder. Save,
   then check and preview your changes by running ``make github`` from the root of the
   ``dcc-ex.github.io`` folder. *This must be done from cmd.exe in Windows, not
   PowerShell*. If any warnings are reported, fix these and run ``make github``
   again. Then go to the directory ``dcc-ex.github.io/docs/_build/html``
   and open ``index.html`` in Chrome or another browser.

5. Use ``git add`` and ``git commit -m "MY CHANGE DESCRIPTION"`` often to save
   changes. If you're using GitHub Desktop these are combined in the commit button.

6. Push it to GitHub: ``git push origin {your-branch-name}``.

7. Go to GitHub and issue a pull request for your branch to be pulled into the
   sphinx branch. Once it's merged in by one of the admins, your changes will
   go live!

Standards
==========

.. highlight:: rst

Headings
--------

* Main Headings have asterisks above and below them
* Subheadings are underlined with equals signs
* The next level is underlined with underscores
* And the next level is underlined with carets
* The last one we use is underlined with tildes

All heading underlines and overlines must be at least as long as the text of the heading

Links
-----

Internal
^^^^^^^^

Sphinx cross-references are used for internal links. This ensures they are
correct and by default will use the destination heading text as the link text.

To link to a page use ``:doc:``:

.. admonition:: Example

    ::

        :doc:`/reference/hardware/motor-boards`

    :doc:`/reference/hardware/motor-boards`

The document name is a relative or absolute (within the documentation) file
path, without the .rst suffix.

To link to a position within a page use ``:ref:``. A reST label can be used as
the reference, but on the DCC++EX website headings are made available to use as
references:

.. admonition:: Example

    ::

        :ref:`advanced-setup/motor-board-config:Configure Using the Installer`

    :ref:`advanced-setup/motor-board-config:Configure Using the Installer`

The reference is the full name of the document (the absolute path without
a leading /), a colon, and the section heading. The full name must be used
even when referring to headings in the same source file.

Alternative text can be used for the link:

.. admonition:: Example

    ::

        :ref:`WiFi configuration <advanced-setup/supported-microcontrollers/wifi-mega:Short Version of Network Setup>`

    :ref:`WiFi configuration <advanced-setup/supported-microcontrollers/wifi-mega:Short Version of Network Setup>`

External
^^^^^^^^

For URLs that are shown, just use the URL:

.. admonition:: Example

    ::

        https://dcc-ex.com/index.html

    https://dcc-ex.com/index.html

To show link text instead of the URL:

.. admonition:: Example

    ::

        `Trainboard Thread <https://www.trainboard.com/highball/index.php?threads/dcc-voltage-and-n-scale-locomotives.56342/>`_

    `Trainboard Thread <https://www.trainboard.com/highball/index.php?threads/dcc-voltage-and-n-scale-locomotives.56342/>`_

For better accessibility, and generally clearer content, use `strong link text <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#accessibility>`_.

If the link will be used multiple times, or to keep the URL separate in the
source file, define a target:

.. admonition:: Example

    ::

        Link to the `DCC++EX home page`_.

        .. _DCC++EX home page: https://dcc-ex.com/index.html

    Link to the `DCC++EX home page <https://dcc-ex.com/index.html>`_.

Downloads
^^^^^^^^^

Download buttons are created using the ``dcclink`` class, added using the
``.. rst-class::`` directive:

.. admonition:: Example

    ::

        .. rst-class:: dcclink

           `Official Release page <https://github.com/DCC-EX/CommandStation-EX/releases>`_

    .. rst-class:: dcclink

       `Official Release page <https://github.com/DCC-EX/CommandStation-EX/releases>`_

Images
------

Include images with the ``.. image::`` and ``.. figure::`` directives.
Horizontal positioning using the ``:align:`` option needs a bit of care.
Where possible e.g. if just presenting a single image, either don't use it, or
choose ``:align: center``.
``:align: left`` (or right) allows multiple images to be shown on the same
line (if the browser window is wide enough), or text to flow around the image.
But you may have to cancel this behaviour for the next content yourself:
a single ``|`` adds an additional blank line before the next paragraph in the
output; before a heading, or if a blank line is not wanted use
``.. rst-class:: clearer``.

Use a figure when including a caption. Sphinx will automatically number the
figure. Add a ``:name:`` option to be able to refer to the figure in the text
using ``:numref:`<figure name>```.

Tables
------

For titled tables use the ``.. table::`` directive, followed by the title.
Sphinx will automatically number the table. Add a ``:name:`` option to be able
to refer to the figure in the text using ``:numref:`<table name>```.

*Work in progress*
