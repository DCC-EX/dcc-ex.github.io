.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-i.rst
.. meta::
   :keywords: EX-CommandStation Command Station EX-Installer

|EX-I-LOGO|

****************************************
Managing config files with the Installer 
****************************************

|tinkerer| |engineer| |githublink-ex-installer-button2|

.. sidebar::

   .. contents:: On this page
      :depth: 4
      :local:

Custom config files
===================

|EX-CS| uses three main config files that allow you to modify aspects of the command station to suit your needs. These files are:

* config.h
* myAutomation.h
* mySetup.h

Note: the *case* of characters the names is very important.

config.h
--------

The **config.h** file contains the core information for how your |EX-CS| will be configured, including:

* The motor driver type
* The WiFi network configuration
* etc.

If you are using the |EX-I| then this file will be automatically created for you based on your answers to the question.  However you can supply your own file (which you can create manually, or may have been previously created by the installer)

myAutomation.h
--------------

The **myAutomation** file can contain any customisations, including:

* Your Roster
* Turnouts/Points
* Routes
* Servos
* |EX-R| automations 
* Turntables (Not available in the current 'Release' version)

This can be created manually, or by the |EX-I| if you select the `Create MyAutomation.h` option.

mySetup.h
---------

The **mySetup.h** file can contain:

* Sensors
* ???

This file must be created manually.

----

Creating Custom Config files
============================

You can create and manage custom config files several ways:

* By using the editing features in |EX-I|
* Manually using any text Editor


Using EX-Installer
------------------

Note: if you are just starting out this is the recommended approach.

* Run |EX-I| following the instructions 
* in the 'Install EX-CommandStation' screen, make sure you select `Create MyAutomation.h` and `advanced config` along with any other options you need for your Command Station.
* Click the :guilabel:`Advanced Config` button you will be shown the 'Advanced Configuration' Screen where you can make additional edits to **config.h** and **myAutomation.h** 
* on the 'Load EX-CommandStation' screen, after you click :guilabel:`Load` and the software has been loaded, you will see a :guilabel:`Backup config files` button
* Follow the instructions to backup your files

The next time you run |EX-I|

* On the 'Select EX-CommandStation version' screen, select the version you wish to install 
* Then select `Use my existing config files` and locate the files you saved as a backup previously. |BR| Select any of the files you backed up. (Even though you select only one file, all the files will be included.)
* Then click :guilabel:`Advanced Config`
* Follow the instructions above for the 'Advanced Configuration' screen and the following steps.

Note: this process does not automatically create **mySetup.h**.  This file can be manually added to the other two files using the text editor instructions below if needed.


Using any text Editor
---------------------

Any app that can edit plain text files can be used.

* Create a folder to store the files.  This *MUST NOT* be inside the folders created by the installer.
* Copy `config-sample.h` from github of the |EX-I| install folders.
* Rename `config-sample.h` to `config.h` and edit as needed
* If needed, create `myAutomation.h` and edit as needed
* If needed, create `mySetup.h` and edit as needed
* Run |EX-I| following the instructions 
* On the 'Select EX-CommandStation version' select the version you wish to install 
* Then select `Use my existing config files` and locate the files you saved as a backup previously, and select any of the files you backed up. (Even though you select only one file, all the files will be included.)
* Then click :guilabel:`Advanced Config`
* Continue to the 'Load Configuration' screen and load the software

If you had previously used the Arduino IDE of VSC to create custom config files, you can use these files, from where you originally created them or copy them to a separate folder.


