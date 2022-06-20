*********************
Recommended software
*********************

.. sidebar:: On this page

   .. contents:: 
      :depth: 1
      :local:

On this page we will outline the software we recommend for project contributions, including both development and documentation.

Git client
===========

Firstly, in order to work with our code, you will require access to a Git client.

If you have a Linux based system (including macOS), you more than likely have Git installed already, so probably don't need to install it.

However, for Windows, you will need to install Git, so follow the instructions in the `Pro Git book <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_.

Once you've installed Git, you will need to set some variables to tell Git who you are when committing code to a repository.

To do this, open a command prompt and run the following two commands, where `user` is your GitHub username, and `email` is the email address associated with your GitHub account (the same commands apply across all operating systems):

.. code-block:: 

  git config --global user.name <user>
  git config --global user.email <email>

Other handy Git software
_________________________

GitHub Desktop is an application by GiHub that provides a graphical user interface for managing Git repositories and so forth:

Download `GitHub Desktop <https://desktop.github.com/>`_

Another graphical alternative is Sourcetree:

Download `Sourcetree <https://www.sourcetreeapp.com/>`_

Arduino IDE
============

If you're already using DCC++ EX, then it's likely you've already installed the Arduino IDE.

However, if you haven't, it's recommended to have this installed, even if using our recommended editor (VSCode) as it's handy to see the same interface that most of our users can see, as they will almost certainly be using the Arduino IDE.

To get up and running with the Arduino IDE, follow the `Getting started with Arduino products <https://www.arduino.cc/en/Guide>`_ page.

ESP32 support
______________

If you need ESP32 support in addition to the standard Arduino AVR boards, follow the official `Espressif Arduino ESP32 documentation <https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html>`_.

Python 3.x
===========

All website documentation is written in reStructuredText format and built using sphinx, which is outlined on our :doc:`/contributing/website` page.

In order to correctly preview changes to the website documentation locally on your computer before publishing to the website, you will need to install Python, preferably the latest 3.x version available.

You can obtain Python from `python.org <https://www.python.org/downloads/>`_.

Once installed, you will need to install three Python packages in order to successfully build the website locally. To do this, open a command prompt and run the following command:

.. code-block:: 

  pip install sphinx sphinx_rtd_theme sphinxcontrib-spelling

Recommended editor (VSCode)
============================

While any text editor will do, even the most simple one, we highly recommend using the free VSCode (Visual Studio Code) which provides additional components that will make your editing easier with syntax highlighting, text snippets, and live preview of the rendering of the file, as well as integration with GitHub. Using a simple text editor will require you handling the Git integration yourself.

VSCode is great whether you're contributing as a developer or documenter, and we cover the requirements for both use cases here.

You can download VSCode `here <https://code.visualstudio.com/download>`_.

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

Refer to the :doc:`/contributing/website` contributing page for more info on generating reliable local previews.
