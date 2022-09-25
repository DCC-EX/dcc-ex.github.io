.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CONTRIBUTING-LOGO|

*********************
Recommended Software
*********************

|tinkerer| |engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

On this page we will outline the software we recommend for project contributions, including both development and documentation.

Git client
===========

Firstly, in order to work with our code, you will require access to a Git client.

If you have a Linux based system (including macOS), you more than likely have Git installed already, so probably don't need to install it.

However, for Windows, you will need to install Git, so follow the instructions in the `Pro Git book <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_.

Once you've installed Git, you will need to set some variables to tell Git who you are when committing code to a repository.

To do this, open a command prompt and run the following two commands, where ``user`` is your GitHub username, and ``email`` is the email address associated with your GitHub account (the same commands apply across all operating systems):

.. code-block:: 

  git config --global user.name <user>
  git config --global user.email <email>

.. tip:: 

  If using our `recommended editor (vscode)`_, once you've installed a Git client, you can do all of your repository work (branches, forks, etc.) directly in VSCode.

Other handy Git software
------------------------

GitHub Desktop is an application by GiHub that provides a graphical user interface for managing Git repositories and so forth:

Download `GitHub Desktop <https://desktop.github.com/>`_

Another graphical alternative is Sourcetree:

Download `Sourcetree <https://www.sourcetreeapp.com/>`_

Arduino IDE
============

If you're already using |DCC-EX|, then it's likely you've already installed the Arduino IDE.

However, if you haven't, it's recommended to have this installed, even if using our recommended editor (VSCode). It's handy to see the same interface that most of our users can see, as they will almost certainly be using the Arduino IDE, and providing support is so much easier when you can use the same tools as the users.

To get up and running with the Arduino IDE, follow the `Getting started with Arduino products <https://www.arduino.cc/en/Guide>`_ page.

ESP32 support
-------------

If you need ESP32 support in addition to the standard Arduino AVR boards, follow the official `Espressif Arduino ESP32 documentation <https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html>`_.

Python 3.x
===========

.. note:: 

  If you won't be contributing to the website documentation, you can skip this step.

All website documentation is written in reStructuredText format and built using sphinx, which is outlined on our :doc:`/about/contributing/website/index` page.

In order to correctly preview changes to the website documentation locally on your computer before publishing to the website, you will need to install Python, preferably the latest 3.x version available.

You can obtain Python from `python.org <https://www.python.org/downloads/>`_ or, alternatively, you can install it from the Microsoft store for Windows users.

For Windows users, follow the official Python documentation here: `Using Python on Windows <https://docs.python.org/3/using/windows.html>`_.

Note that you will need to ensure Python is added to your `PATH` environment variable which is outlined on that page also.

Once installed, you will need to install three Python packages in order to successfully build the website locally. To do this, open a command prompt and run the following command:

.. code-block:: 

  pip install sphinx-toolbox
  pip install sphinx 
  pip install sphinx_rtd_theme
  pip install sphinxcontrib-spelling

Recommended editor (VSCode)
============================

While any text editor will do, even the most simple one, we highly recommend using the free VSCode (Visual Studio Code) which provides additional components that will make your editing easier with syntax highlighting, text snippets, and live preview of the rendering of the file, as well as integration with GitHub. Using a simple text editor will require you handling the Git integration yourself.

VSCode is great whether you're contributing as a developer or documenter, and we cover the requirements for both use cases here.

You can download VSCode `here <https://code.visualstudio.com/download>`_.

VSCode includes many different extensions and configuration options to enable the various syntax checks and other additional components, so please review the below to ensure the right configuration and extensions are in place to make things easier for yourself.

Recommended extensions
----------------------

To install and manage extensions, either click the manage extensions icon in the left menu section or press <Ctrl> + <Shift> + <x>.

For development, the following extensions are recommended:

* C/C++ by Microsoft
* PlatformIO IDE by PlatformIO

For documentation, the following extensions are recommended:

* reStructuredText by LeXtudio Inc.
* reStructuredText Syntax highlighting by Trond Snekvik.
* Python by Microsoft.

Enabling live documentation previews
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The reStructuredText extension installed with VSCode allows live previewing of the web pages using the "Esbonio language server".

Note, however, that the Esbonio server will only generate live previews of the pages you are actively editing, and therefore it will not give you a complete updated view of the entire website.

Once you've installed the extensions above, it is recommended you close then reopen VSCode, and upon reopening VSCode, you should be prompted in the bottom right hand corner to install the Esbonion language server. It is recommended you do so now.

Refer to the :doc:`/about/contributing/website/index` contribution page for more info on generating reliable local previews.

Recommended configuration options
---------------------------------

Once VSCode is installed, it is recommended you update the default spacing for code indents as we standardise this to two spaces across our code base (including documentation).

To do this:

1. Click the Settings cog icon in the bottom left corner and select "Settings" (alternatively, press <Ctrl> + ",").
2. Locate "Editor: Tab size" (should be about the fourth item down).
3. Set this to "2", and close the "Settings" tab which will auto-save the change.

In addition to the above, if you are contributing to documentation and are using the recommended extensions, you should ignore certain reStructuredText syntax warnings that are irrelevant.

To configure these:

1. Click the Settings cog icon in the bottom left corner and select "Settings" (alternatively, press <Ctrl> + ","").
2. Enter "restructured" in the search bar, then click on "Edit in settings.json".
3. Add this section:

  .. code-block:: 

    "restructuredtext.linter.doc8.extraArgs": [ 
        "--ignore D001", 
        "--ignore D002", 
        "--ignore D004"
    ]

4. Save and close the settings, and the irrelevant warnings should no longer bother you.

Use VSCode for git
------------------

If you wish to use VSCode as your default editor for Git, open a command prompt and run the following command:

.. code-block:: 

  git config --global core.editor "code --wait"

