.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: WiFi setup Espressif

|EX-CS-LOGO|

*******************************************************
ESP8266 (WiFi Boards) - AT Version Issues and Solutions
*******************************************************

|conductor| |Tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :local:
      :depth: 3

Unfortunately the Espressif ESP8266 based WiFi Boards that are available for sale routinely come with versions of the firmware that simply do not work with |EX-CS|. This now seems to include the recommended `Makerfabs ESP8266 WiFi Shield <https://www.makerfabs.com/esp8266-wifi-shield.html>`_.

Which is correct version of the AT firmware
===========================================

Only **version 1.7.4** is known to work reliably.  

That means all versions both before or after 1.7.4 are *not* suitable.  So don't be fooled in thinking that if it has a version later than that it will be ok.  **It won't!**

Symptoms of an Incorrect firmware Version
=========================================

There several common symptoms of a an incorrect firmware version

* You can't connect to the SSID.
* You can connect to the SSID, but can't connect your WiFi throttle (e.g. Engine Driver or wiThrottle) to the CommandStation. 
* You can connect once, but it will not connect again unless you re-start the |EX-CS|.

----

Find out Your AT Version
========================

It is important to find out which version of the firmware you board has and correct it if necessary.

There are two basic ways that you can check:

* After you load the |EX-CS| software
* Before you load the |EX-CS| software

|hr-dashed|

Checking *after* you load the |EX-CS| software
----------------------------------------------

One you have loaded the |EX-CS| software you will be able to see the AT version in the start-up log by connecting the serial monitor in either the |EX-I| or Arduino IDE (whichever you used to upload the |EX-CS| onto your device).

Checking the AT version using EX-Installer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have successfully loaded the |EX-CS| software:

1. click back through the pages of the |EX-I| till you get to the 'Select your Device' screen
2. Click on the :guilabel:`View device monitor` button |BR| A new window will open and a lot of text will appear
3. you need to look for a line that will have a section highlighted in green

e.g. ``AT version:1.7.4.0(May 11 2020 19:13:04)``

Alternately, you can enter the command ``<+GMR>`` and click :guilabel:`Send`.  A similar line will be shown.

If it says **anything other than** 1.7.4 in that line, then you have the wrong version you will need to follow `the instructions at the end of this page <What to do if you have the wrong version>`_ to correct it.

Checking the AT version with the Arduino IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you loaded the |EX-CS| software using the Arduino, once you have successfully loaded the |EX-CS| software:

1. select **Tools** -> **Serial monitor** from the menus
2. A new pane will open at the bottom of the IDE window will open and a lot of text will appear
3. you need to look for a line similar to the following

e.g. ``AT version:1.7.4.0(May 11 2020 19:13:04)``

Alternately, you can enter the command ``<+GMR>`` and click :guilabel:`Send`.  A similar line will be shown.

If it says **anything other than** 1.7.4 in that line, then you have the wrong version you will need to follow `the instructions at the end of this page <What to do if you have the wrong version>`_ to correct it.

|hr-dashed|

Checking *before* you load the |EX-CS| software
-----------------------------------------------

How to check before you load the |EX-CS| software will depend on which WiFi shield or board you are using.

Checking the AT version of a ESP-01 or ESP-01s
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: `Checking AT version ESP-01 prior to upload`

There are a number of ways that you can check the AT version an a ESP-01 or ESP-01s:

* with a USB Serial Adapter
* with a USB to TTL CH340G Converter Module Adapter
* with a Arduino Uno
* ESP8266 Wifi Shield

Checking the AT version of a with a USB Serial Adapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect the ESP01 to the serial adapter
2. Plug the serial adapter it the PC
3. Open the Arduino IDE 
4. Select **Tools** -> **Serial monitor** from the menus
5. Select baud: ``115200`` and ``Both NL & CR``
6. A new pane will open at the bottom of the IDE window will open
7. Enter the command ``AT+GMR`` and click :guilabel:`Send`.

It will reply with something like ``AT version:1.7.4.0(May 11 2020 19:13:04)``

If it says **anything other than** 1.7.4 in that line, then you have the wrong version you will need to follow `the instructions at the end of this page <What to do if you have the wrong version>`_ to correct it.

Checking the AT version of a with a USB to TTL CH340G Converter Module Adapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: `Checking AT version with a USB to TTL CH340G Converter Module Adapter prior to upload`

Checking the AT version of a with a Arduino Uno
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: `Checking AT version with a Arduino Uno prior to upload`

|hr-dashed|

Checking the AT version of a ESP8266 Wifi Shield
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: `Checking AT version ESP8266 Wifi Shield prior to upload`


|hr-dashed|

Checking the AT version of a Duinopeak ESP8266 WiFi Expansion Board 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: `Checking AT version ESP8266 WiFi Expansion Board prior to upload`

|hr-dashed|

Checking the AT version of a Mega+WiFi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: `Checking AT version Mega+WiFi prior to upload`

----

What to do if you have the wrong version
========================================

The steps necessary to correct the version will depend on you hardware.

We highly recommend upgrading or downgrading to the "NonOS AT" version 1.7.4 available on our :doc:`/download/esp8266` download page **prior** to reaching out for support from the team.

|hr-dashed|

Correcting the AT version on a ESP-01
-------------------------------------

.. todo:: `Correcting AT version ESP-01`

Correcting ESP-01 With a USB Serial Adapter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: `Correcting AT version ESP-01 With a USB Serial Adapter` 

Correcting ESP-01 With a USB to TTL CH340G Converter Module Adapter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: `Correcting AT version ESP-01 With a USB to TTL CH340G Converter Module Adapter`

Correcting ESP-01 With a Arduino Uno
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See https://cordobo.com/2300-flash-esp8266-01-with-arduino-uno/

|hr-dashed|

Correcting the AT version on a ESP8266 Wifi Shield
--------------------------------------------------

See https://www.allaboutcircuits.com/projects/update-the-firmware-in-your-esp8266-wi-fi-module/

Correcting the ESP8266 Wifi Shield With a USB to TTL Converter Module Adapter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See https://gist.github.com/nathankellenicki/7008540322c617869cec17226cff579d   

Correcting the AT version on a Duinopeak ESP8266 WiFi Expansion Board 
---------------------------------------------------------------------

.. todo:: `Correcting AT version Duinopeak ESP8266 WiFi Expansion Board`

Correcting the AT version on a Mega+WiFi
----------------------------------------

Flashing the ESP8266 chip on a Mega+WiFi is covered in detail :doc:`here </reference/hardware/microcontrollers/wifi-mega>`.

