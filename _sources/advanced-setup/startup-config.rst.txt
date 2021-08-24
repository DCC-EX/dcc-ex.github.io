**********************
Startup Configuration
**********************

Sometimes, you will need to configure your DCC++ EX with settings which are not saved by the Command Station when restarted, for example the `ACK min <../reference/software/diagnostic-d-ack-command.html#d-ack-limit-ma>`_ for the Hornby R7150 Decoder (which seemed to need its minimum ACK pulse duration limit set to `2600µS` to be recognised).

To automatically run commands at start up, a new file can be created called `mySetup.h` to contain these commands.



Make sure you are running the Arduino IDE
=========================================

This will need to be done in the `Arduino-IDE <../get-started/arduino-ide.html>`_, so first make sure you have followed these steps to load up the Arduino IDE.


Create a new tab
================

First you will need to add a new file, just like the `config.h file <../get-started/arduino-ide.html#copy-the-config-example-h-file-or-rename-it>`_. Create a new tab using the following menu option.

.. image:: /_static/images/arduino-ide/arduino_ide_newtab.jpg
   :alt: Arduino IDE New Tab
   :scale: 40%

**Figure 1** - Creating a new tab in the Arduino IDE

Creating the mySetup.h file
===========================

At the bottom of the IDE window, a yellow bar will appear asking for a `Name for new file`, here make sure to enter ``mySetup.h`` (case sensitive, so upper case S in setup) and click ``OK`` to create the new file.

.. image:: /_static/images/arduino-ide/arduino_ide_mysetup.jpg
   :alt: Arduino IDE New Tab
   :scale: 40%

**Figure 2** - Choosing a file name for the new file

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

Finally, upload the code to the Arduino as you would do during the standard `Arduino IDE Setup <../get-started/arduino-ide.html#upload-the-software>`_. Restart the Command Station and these commands will have run at start up.