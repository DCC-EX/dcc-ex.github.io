.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-CS-LOGO|

*****************
EX-CommandStation
*****************

|conductor| |tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

Welcome to the |EX-CS| download page. You have several choices:

* **[RECOMMENDED]** If you are a |conductor-text|, or you just want an easy installer to do the work for you, go to the `ex-Installer`_ section.
* If you are a |tinkerer-text|, or you would like to download a zip file and install the firmware using the Arduino IDE, go to the `Latest EX-CommandStation Official Release`_ section.
* To get the latest unreleased development version, go to the `Latest EX-CommandStation Unreleased Development Version`_.
* If you are an |engineer-text| or developer, and want to clone the repository onto your computer, go to the `EX-CommandStation Repository (project source files)`_ section.
* If you're still looking for |BSC|, go to the `Getting BaseStation-Classic`_ section.

EX-Installer
=============

.. note:: Clicking on the link below will automatically find the correct version for your Computer and Operating system (Windows, Mac, Linux) and download it. After unzipping the files to a folder on your computer and running the "EX-Installer" program, you will have the opportunity to select either |EX-CS| or BaseStation-Classic, and options, such as your Arduino type and motor driver type. It will automatically upload the software to your Arduino or other supported board. Click here for :doc:`EX-Installer installation instructions </ex-commandstation/get-started/installer>`. If you have an issue with the web page getting you the correct version, click on the `Latest EX-CommandStation Official Release`_ button in the next section to manually download the correct version.

.. raw:: html 

   <p class="dcclink"><a onclick="getLink()"><span class="problematic">Automated Installer</span></a></p>

|

Latest EX-CommandStation Official Release
=========================================

.. note:: On the releases page, select the most recent version and download the .zip file. You will see the 2 files for download, choose the compression format you prefer: CommandStation-EX.zip or CommandStation-EX.tar.gz. The zip/tar file contains the Arduino Sketch file for |EX-CS|. You will need either the Arduino IDE or the PlatformIO development environment in order to upload it to your microcontroller board. Click here for `Arduino IDE installation instructions :doc:`</ex-commandstation/advanced-setup/installation-options/arduino-ide>`.

.. rst-class:: dcclink

  `Official Release page <https://github.com/DCC-EX/CommandStation-EX/releases>`_

|

Latest EX-CommandStation Unreleased Development Version
=======================================================

.. note:: The link below will download the latest *unreleased* development version in zip file format. Please open the zip file, go into the "CommandStation-EX-master" folder, and unzip all the files in that folder into your "EX-CommandStation-EX" sketch folder. Make sure you **DO NOT** just unzip the entire zip file, since it will have the incorrect folder name. The Arduino IDE requires that the folder name and the .ino file inside that folder match names exactly, i.e.: "CommandStation-EX" not "CommandStation-EX-master".

.. attention:: `Discord <https://discord.gg/y2sB4Fp>`_ is the best place to keep up-to-date on new code releases, and you may be directed to download the latest version here from time to time, as new features are added and updated often.

.. rst-class:: dcclink

   `Development Version <https://github.com/DCC-EX/CommandStation-EX/archive/refs/heads/master.zip>`_

|

EX-CommandStation Repository (project source files)
=====================================================

.. note:: The link below will take you the the EX-CommandStation GitHub repository, where you can clone the project to your computer. Click on the green button to get a clone link or to download the zip file. We have made sure that you can still use the Arduino IDE if you like, but we recommend developers use the PlatformIO development environment. See the :doc:`Contributing Page </about/contributing/index>` for more information.

.. rst-class:: dcclink

   `EX-CommandStation GitHub <https://github.com/DCC-EX/CommandStation-EX>`_

|

|EX-BSC-LOGO|

Getting BaseStation-Classic
============================

|EX-I| will allow you to install BaseStation-Classic. However, we recommend using the newer |EX-CS| as it will run on the same hardware and is better supported. 

If you are looking for the original source for the project (with some minor bug fixes and improvements), see the links below.

.. warning:: This version is not actively maintained, and will only be updated with bug fixes.

.. rst-class:: dcclink

   `BaseStation-Classic .zip file <https://github.com/DCC-EX/BaseStation-Classic/archive/master.zip>`_

.. rst-class:: dcclink

   `BaseStation-Classic GitHub <https://github.com/DCC-EX/BaseStation-Classic>`_
