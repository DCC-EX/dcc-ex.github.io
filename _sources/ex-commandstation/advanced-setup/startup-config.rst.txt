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
      :depth: 2
      :local:

Sometimes, you may want to configure your |EX-CS| with settings which are not otherwise saved by the Command Station when restarted. For example the :ref:`ACK min <reference/tools/diagnostic-d-ack-command:\<D ACK LIMIT mA\>>` for the Hornby R7150 Decoder (which seemed to need its minimum ACK pulse duration limit set to `2600µS` to be recognised).

To automatically run commands at start up, you can create a new file called `mySetup.h` to contain these commands.

How you create the file will depend on how you load the |EX-CS| software onto your Arduino.

* By using |EX-I|
* By using the Arduino IDE

----

If you are using EX-Installer
=============================

You need to create a text file in the `CommandStation-EX` folder below where you uncompressed the |EX-I| files, and rename it to `mySetup.h`

For example, in Microsoft Windows:

* Open the `File Explorer` app
* Navigate to where you unzipped the |EX-I| files that you downloaded from this site.
* Open the `CommandStation-EX` sub-folder
* In the 'Home' tab, click ``New Item`` and then ``Text Document``
* Replace the name with `mySetup.h` and press ``Enter``  It will warn you about chnaging the extension (the bit after the '.'). Click ``yes``.
* [Right click] on the new file, and select :menuselection:`Open With --> Notepad`
* The file will open in the 'Notepad' app
* Enter the commands you need to perform.  For Example:

.. code-block:: none
  
  SETUP("<1>");  // Turn track power on at startup

* Select :menuselection:`File --> Exit`.  |BR| It will ask you the save the file.  Click ``Save``
* You now need to upload the software using the |EX-I| jast the same as you originally did ( :doc:`/ex-commandstation/get-started/installer`)

See examples and information below for adding multiple instructions to `mySetup.h`.

If you need to change the `mySetup.h` later, simply find the file you created above, then [Right click] on it, and select :menuselection:`Open With --> Notepad`.  Then follow the remaining steps.

----

If you are using the Arduino IDE
================================

This will need to be done in the :doc:`/ex-commandstation/advanced-setup/installation-options/arduino-ide`, so first make sure you have followed these steps to load up the Arduino IDE.


Create a new tab
----------------

First you will need to add a new file, just like the :ref:`config.h file <ex-commandstation/advanced-setup/installation-options/arduino-ide:Copy the config.example.h file (or rename it)>`. Create a new tab using the following menu option.

.. figure:: /_static/images/arduino-ide/arduino_ide_newtab.jpg
   :alt: Arduino IDE New Tab
   :scale: 40%

   Creating a new tab in the Arduino IDE

Creating the mySetup.h file
---------------------------

At the bottom of the IDE window, a yellow bar will appear asking for a `Name for new file`, here make sure to enter ``mySetup.h`` (case sensitive, so upper case S in setup) and click ``OK`` to create the new file.

.. figure:: /_static/images/arduino-ide/arduino_ide_mysetup.jpg
   :alt: Arduino IDE New Tab
   :scale: 40%

   Choosing a file name for the new file

Adding in the startup commands
------------------------------

Within the new file that has been created, you can add in the commands that you wish the Command Station to run at startup. For example, if you need to run the following command each time your Command Station starts up: 

.. code-block:: none

   <D ACK MIN 2600>

Then you would need to enter into the `mySetup.h` file:

.. code-block:: none

   SETUP("<D ACK MIN 2600>");

Note the upper case word ``SETUP`` at the start.

Adding in more than one startup command
---------------------------------------

If you need to have multiple commands run at start up, you will need to enter each additional command on a new line, so a longer ``mySetup.h`` file could look like:

.. code-block:: none

   SETUP("<D ACK MAX 9200>"); // Set ACK detection to allow pulses up to 9200uS
   SETUP("<D ACK LIMIT 60>"); // 60mA is the default
   SETUP("<0>"); // tracks off at startup
   SETUP("<D CMD 0>"); // can be set to ON for testing in the serial monitor

Here you can add comments on each line, these can be added by using the double forward slash character ``//`` and then your comments. This makes it easier to remember why you added these start up commands.

Upload the new version of the software
--------------------------------------

Finally, upload the code to the Arduino as you would do during the standard :ref:`Arduino IDE Setup <ex-commandstation/advanced-setup/installation-options/arduino-ide:Upload the software>`. Restart the Command Station and these commands will have run at start up.

----

Examples
========

Automatically Turning Track Power on at Startup
-----------------------------------------------

Adding this line to `mySetup.h` will cause the track power to turn on automatically when the |EX-CS| powers up.

.. code-block:: none
  
  SETUP("<1>");  // Turn track power on at startup
