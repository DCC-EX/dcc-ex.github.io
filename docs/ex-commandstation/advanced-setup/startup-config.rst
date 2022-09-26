.. include:: /include/include-ex-cs.rst 
.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|
  
**********************
Startup Configuration
**********************

|tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :depth: 1
      :local:

Sometimes, you will need to configure your |EX-CS| with settings which are not saved by the Command Station when restarted, for example the :ref:`ACK min <reference/tools/diagnostic-d-ack-command:\<D ACK LIMIT mA\>>` for the Hornby R7150 Decoder (which seemed to need its minimum ACK pulse duration limit set to `2600µS` to be recognised).

To automatically run commands at start up, a new file can be created called `mySetup.h` to contain these commands.

.. todo:: MEDIUM - Explain how this can be be done using EX-Installer

.. todo:: MEDIUM - Include example of automatically powering up the track


Make sure you are running the Arduino IDE
=========================================

This will need to be done in the :doc:`/ex-commandstation/advanced-setup/installation-options/arduino-ide`, so first make sure you have followed these steps to load up the Arduino IDE.


Create a new tab
================

First you will need to add a new file, just like the :ref:`config.h file <ex-commandstation/advanced-setup/installation-options/arduino-ide:Copy the config.example.h file (or rename it)>`. Create a new tab using the following menu option.

.. figure:: /_static/images/arduino-ide/arduino_ide_newtab.jpg
   :alt: Arduino IDE New Tab
   :scale: 40%

   Creating a new tab in the Arduino IDE

Creating the mySetup.h file
===========================

At the bottom of the IDE window, a yellow bar will appear asking for a `Name for new file`, here make sure to enter ``mySetup.h`` (case sensitive, so upper case S in setup) and click ``OK`` to create the new file.

.. figure:: /_static/images/arduino-ide/arduino_ide_mysetup.jpg
   :alt: Arduino IDE New Tab
   :scale: 40%

   Choosing a file name for the new file

Adding in the startup commands
==============================

Within the new file that has been created, you can add in the commands that you wish the Command Station to run at startup. For example, if you need to run the following command each time your Command Station starts up: 

.. code-block:: none

   <D ACK MIN 2600>

Then you would need to enter into the `mySetup.h` file:

.. code-block:: none

   SETUP("<D ACK MIN 2600>");

Note the upper case word ``SETUP`` at the start.

Adding in more than one startup command
=======================================

If you need to have multiple commands run at start up, you will need to enter each additional command on a new line, so a longer ``mySetup.h`` file could look like:

.. code-block:: none

   SETUP("<D ACK MAX 9200>"); // Set ACK detection to allow pulses up to 9200uS
   SETUP("<D ACK LIMIT 60>"); // 60mA is the default
   SETUP("<0>"); // tracks off at startup
   SETUP("<D CMD 0>"); // can be set to ON for testing in the serial monitor

Here you can add comments on each line, these can be added by using the double forward slash character ``//`` and then your comments. This makes it easier to remember why you added these start up commands.

Upload the new version of the software
======================================

Finally, upload the code to the Arduino as you would do during the standard :ref:`Arduino IDE Setup <ex-commandstation/advanced-setup/installation-options/arduino-ide:Upload the software>`. Restart the Command Station and these commands will have run at start up.
