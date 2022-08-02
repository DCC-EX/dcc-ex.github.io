.. include:: /include/include.rst
.. include:: /include/include-l2.rst
************
Requirements
************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

We assume, since you got here, that you already have a computer up and running being either a Linux, macOS, or Windows machine, as well as a working internet connection and some disk space available. 

A 64 bit operating system is preferred, running as much as possible the latest version of your chosen OS. This in any case is good practice to keep your environment healthy and up-to-date.

The following sections describe what else you need for participating in the different efforts.

Documentation
==============

If you concentrate on documentation, no additional hardware requirements exist. Keep reading on, but be reassured if you don't feel comfortable with the following don't worry, we will find a way to have you contributing by other means.
Just go to the Contact Us section, and we will find a way of getting you on board, or help you out getting things set up.

reStructuredText
_________________

All documentation is done using reStructuredText, for which you can find information on the official website: `reStructuredText <https://docutils.sourceforge.io/rst.html>`_
or the `Sphinx <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ document builder tool website, which we discuss later on in this chapter.
reStructuredText is a markdown type language, for typesetting documents from websites to PDF or LaTeX documents. Our Website is built upon this technology, so you should make yourself familiar with this by looking through the links provided.

reStructuredText `QuickReference Guide <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_ 

Git & GitHub
_____________

You should have some knowledge about Git and GitHub, as we manage all of our documentation (as well as the development) there. Depending on the editing platform of your choice, you may get all the Git functionality you need. You may want to install GitHub Desktop or Sourcetree for getting a good idea on the state of the DCC++EX documentation GitHub repository (dcc-ex.github.io).

If you don't have Git installed, now is as good a time as any, follow the instructions in the `Pro Git book <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_

Download `GitHub Desktop <https://desktop.github.com/>`_

Download `SourceTree <https://www.sourcetreeapp.com/>`_

Editing
________

You will also need to choose a text editor. Yes, any text editor will do, even the most simple one, but they will not provide editing help. We suggest you use the free VSCode (Visual Studio Code) which provides additional components that will make your editing easier with syntax highlighting, text snippets, and live preview of the rendering of the file, as well as integration with GitHub. Using a simple text editor will require you handling the Git integration yourself.

Download VSCode `here <https://code.visualstudio.com/download>`_

Install the following extensions:

* reStructuredText by LeXtudio Inc.
* reStructuredText Syntax highlighting by Trond Snekvik.

The final website will be rendered from the rst text files using Sphinx, which you also need to install with some options which you'll find in the next paragraph.

VSCode rst warnings
^^^^^^^^^^^^^^^^^^^^

Note you will likely encounter various syntax warnings in VSCode using the recommended extensions, and these should simply be ignored.

To ignore these, navigate to Settings in VSCode (<Ctrl + ,>), enter "restructured" in the search bar, and click on "Edit in settings.json".

Add this section:

.. code-block:: 

  "restructuredtext.linter.doc8.extraArgs": [ 
      "--ignore D001", 
      "--ignore D002", 
      "--ignore D004"
  ]

Save and close the settings, and the irrelevant warnings should no longer bother you.

Sphinx
_______

Sphinx is a transformation tool, taking rst formatted documents and turning them into a static html website, PDF, or LaTex documents.

Sphinx needs Python v3, so if you don't have python installed, it's time to do this now.

The simplest way to install Python on Windows is via the Microsoft Store. Install the latest version of Python 3 available.

Live preveiew
^^^^^^^^^^^^^^

The reStructuredText extension installed with VSCode allows live previewing of the web pages.

When installing you will be prompted to choose the preview method, with the "Esbonio language server" being the better option of the two, albeit more resource intensive as it will generate the preview every time you save.

Note, however, that the Esbonio server will only generate live previews of the pages you are actively editing, and therefore it will not give you a complete updated view of the entire website.

Refer to the :doc:`/about/contributing/website` contributing page for more info on generating reliable local previews.

Images
_______

We typically like compressed PNG files, but can take JPG as well. The resolution should be 72dpi and at least 600 pixels wide (maximum 1200). We can size the images using Sphinx to reduce them as necessary to fit where we need them on the page.

Graphs & Schemas
_________________

Use draw.io to keep compatibility and allow group collaboration on the same document. Not everyone has access to Microsoft Visio. Export any schema or graph from draw.io in PNG format, with settings if possible as outlined above.

--- to be done graphviz to be added ---

Hidden Pages (Not ready for release)
_____________________________________

Use the ``:orphan:`` tag with a comment below it saying "Remove orphan field when the document is added to a toctree". This will allow us to easily search for the word "orphan" to find incomplete pages and avoids triggering an error that there are pages without an entry in a toctree

Hidden comments
________________

You can hide notes or searchable placeholders by putting placing the text on a line with a space above and below and preceding it with two period and a space, ex: ".. This is a hidden comment"


Summary
________

Code documentation
___________________

*Work in progress*

Once you have gone through all this, head to the documentation section to see how it all works.

Development
============

Additional hardware
- Arduino / motorshield setup as you can find in :ref: 


*Work in progress*
