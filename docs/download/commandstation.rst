**************************
Command Station Downloads
**************************

Welcome to the Command Station download page. You have several choices:

* **[RECOMMENDED]** If you are a Conductor, or you just want an easy installer to do the work for you, go to the :ref:`download/commandstation:exInstaller` section.
* If you are a Tinkerer, or you would like to download a zip file and install the firmware using the Arduino IDE, go to the :ref:`download/commandstation:Latest DCC++ EX Official Release` section.
* To get the latest unreleased development version, go to the :ref:`download/commandstation:Latest DCC++ EX Unreleased Development Version`, including the excitement of **EX-RAIL Automation**!
* If you are an Engineer or developer, and want to clone the repository onto your computer, go to the :ref:`download/commandstation:CommandStation-EX Repository (project source files)` section.
* If you're still looking for BaseStation-Classic, go to the :ref:`download/commandstation:Getting BaseStation-Classic` section.

exInstaller
=============

.. note:: Clicking on the link below will automatically find the correct version for your Computer and Operating system (Windows, Mac, Linux) and download it. After unzipping the files to a folder on your computer and running the "exInstaller" program, you will have the opportunity to select either CommandStation-EX or BaseStation-Classic, and options, such as your Arduino type and motor shield type. It will automatically upload the software to your Arduino or other supported board. Click here for :doc:`exInstaller installation instructions <../get-started/installer>`. If you have an issue with the web page getting you the correct version, click on the :ref:`download/commandstation:Latest DCC++ EX Official Release` button in the next section to manually download the correct version.

.. raw:: html 

   <p><a class="dcclink" onclick="getLink()"><span class="problematic">Automated Installer</span></a></p>

|

Latest DCC++ EX Official Release
==================================

.. note:: On the releases page, select the most recent version and download the .zip file. You will see the 2 files for download, choose the compression format you prefer: CommandStation-EX.zip or CommandStation-EX.tar.gz. The zip/tar file contains the Arduino Sketch file for DCC++ EX. You will need either the Arduino IDE or the PlatformIO development environment in order to upload it to your microcontroller board. Click here for :doc:`Arduino IDE installation instructions <../get-started/arduino-ide>`.

.. raw:: html

   <p><a class="dcclink" href="https://github.com/DCC-EX/CommandStation-EX/releases">Official Release page</a></p>

|

Latest DCC++ EX Unreleased Development Version
===============================================

.. note:: The link below will download the latest *unreleased* development version in zip file format. Please open the zip file, go into the "CommandStation-EX-master" folder, and unzip all the files in that folder into your "CommandStation-EX" sketch folder. Make sure you **DO NOT** just unzip the entire zip file, since it will have the incorrect folder name. The Arduino IDE requires that the folder name and the .ino file inside that folder match names exactly, ie: "CommandStation-EX" not "CommandStation-EX-master".

.. attention:: `Discord <https://discord.gg/y2sB4Fp>`_ is the best place to keep up-to-date on new code releases, and you may be directed to download the latest version here from time to time, as new features are added and updated often.

.. raw:: html

   <p><a class="dcclink" href="https://github.com/DCC-EX/CommandStation-EX/archive/refs/heads/master.zip">Development Version</a></p>

|

CommandStation-EX Repository (project source files)
=====================================================

.. note:: The link below will take you the the CommandStation-EX GitHub repository, where you can clone the project to your computer. Click on the green button to get a clone link or to download the zip file. We have made sure that you can still use the Arduino IDE if you like, but we recommend developers use the PlatformIO development environment. See the :doc:`Contributing Page <../contributing/index>` for more information.

.. raw:: html

   <p><a class="dcclink" href="https://github.com/DCC-EX/CommandStation-EX">CommandStation-EX GitHub</a></p>

|

Getting BaseStation-Classic
============================

The installer will allow you to install BaseStation-Classic. We recommend using the newer CommandStation-EX. If you are looking for the original source for the project (with some minor bug fixes and improvements), see the links below.

.. warning:: This version is not actively maintained, and will only be updated with bug fixes.

.. raw:: html

   <p><a class="dcclink" href="https://github.com/DCC-EX/BaseStation-Classic/archive/master.zip">BaseStation-Classic .zip file</a></p>
   <p><a class="dcclink" href="https://github.com/DCC-EX/BaseStation-Classic">BaseStation-Classic GitHub</a></p>

|