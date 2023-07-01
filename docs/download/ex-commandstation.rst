.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-DL-LOGO|

*****************
EX-CommandStation
*****************

|conductor| |tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
     :depth: 2
     :local:

Welcome to the |EX-CS| download page. You have several choices:

* **[RECOMMENDED]** If you are a |conductor-text|, or you just want an easy installer to do the work for you, go to the `ex-Installer`_ section.
* If you are a |tinkerer-text|, or you would like to download a zip file and install the firmware using the Arduino IDE, go to the `Latest EX-CommandStation Official Release`_ section.
* To get the latest unreleased development version, go to the `Latest EX-CommandStation Unreleased Development Version`_.
* If you are an |engineer-text| or developer, and want to clone the repository onto your computer, go to the `EX-CommandStation Repository (project source files)`_ section.
* If you're still looking for |BSC|, go to the `Getting BaseStation-Classic`_ section.

----

|EX-I-LOGO-SMALL|

EX-Installer
=============

.. note:: 
   :class: note-float-right

   If you have any difficulties with the automated installer link try these:

      .. rst-class:: dcclink

         `For Windows x64 <https://github.com/DCC-EX/EX-Installer/raw/main/dist/EX-Installer-Win64.exe>`_

      .. rst-class:: dcclink

         `For Windows x32 <https://github.com/DCC-EX/EX-Installer/raw/main/dist/EX-Installer-Win32.exe>`_

         `For MacOS / OSX <https://github.com/DCC-EX/EX-Installer/raw/main/dist/EX-Installer-macOS>`_

      .. rst-class:: dcclink

         `For Linux x64 <https://github.com/DCC-EX/EX-Installer/raw/main/dist/EX-Installer-Linux64>`_

This is the new version of the EX-Installer.  

Clicking on the link below will automatically find the correct version for your Computer and Operating system (Windows, Mac, Linux) and download it.

This downloads a self contained app that can load automatically load the software from your computer to your Arduino or other supported board. Click here for :doc:`EX-Installer installation instructions </ex-commandstation/get-started/installer>`.


.. raw:: html 

   <p class="dcclink"><a onclick="getNewLink()"><span class="problematic">Automated Installer</span></a></p>

|force-break|

----

|EX-CS-LOGO-SMALL|

Manually loading the software
=============================

If you plan to use the the Arduino IDE or VCS to configure your |EX-CS| you can use the links below to download the appropriate version.

Latest EX-CommandStation Official Release
-----------------------------------------

.. note:: On the releases page, select the most recent version and download the .zip file. You will see the 2 files for download, choose the compression format you prefer: CommandStation-EX.zip or CommandStation-EX.tar.gz. The zip/tar file contains the Arduino Sketch file for |EX-CS|. You will need either the Arduino IDE or the PlatformIO development environment in order to upload it to your microcontroller board. Click here for :doc:`Arduino IDE installation instructions </ex-commandstation/advanced-setup/installation-options/arduino-ide>`.

   .. rst-class:: dcclink

   `Official Release page <https://github.com/DCC-EX/CommandStation-EX/releases>`_


Latest EX-CommandStation Unreleased Development Version
-------------------------------------------------------

.. note:: The link below is to the "devel" branch in GitHub. You can use the "Download ZIP" option from the "Code" pulldown menu to obtain a local copy of this code. Please open the zip file, go into the "CommandStation-EX-master" folder, and unzip all the files in that folder into your "CommandStation-EX" sketch folder. Make sure you **DO NOT** just unzip the entire zip file, since it will have the incorrect folder name. The Arduino IDE requires that the folder name and the .ino file inside that folder match names exactly, i.e.: "CommandStation-EX" not "CommandStation-EX-master".

.. attention:: `Discord <https://discord.gg/y2sB4Fp>`_ is the best place to keep up-to-date on new code releases, and you may be directed to download the latest version here from time to time, as new features are added and updated often.

   .. rst-class:: dcclink

   `Development Version <https://github.com/DCC-EX/CommandStation-EX/tree/devel>`_

|force-break|

EX-CommandStation Repository (project source files)
---------------------------------------------------

.. note:: The link below will take you the the EX-CommandStation GitHub repository, where you can clone the project to your computer. Click on the green button to get a clone link or to download the zip file. We have made sure that you can still use the Arduino IDE if you like, but we recommend developers use the PlatformIO development environment. See the :doc:`Contributing Page </about/contributing/index>` for more information.

   .. rst-class:: dcclink

      `EX-CommandStation GitHub <https://github.com/DCC-EX/CommandStation-EX>`_

|force-break|

----

|EX-BSC-LOGO-SMALL|

Getting BaseStation-Classic
============================

.. warning:: 
   :class: warning-float-right

   This version is not actively maintained, and will only be updated with bug fixes.

The new |EX-I| :dcc-ex-red-bold:`does not provide an option to install BaseStation-Classic` so if you wish to install it you will need to use the Arduino IDE or VSC and download the links below. 

We recommend using the newer |EX-CS| as it will run on the same hardware and is better supported. 


   .. rst-class:: dcclink

      `BaseStation-Classic .zip file <https://github.com/DCC-EX/BaseStation-Classic/archive/master.zip>`_

   .. rst-class:: dcclink

      `BaseStation-Classic GitHub <https://github.com/DCC-EX/BaseStation-Classic>`_
