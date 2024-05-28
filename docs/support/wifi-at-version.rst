.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: WiFi setup Espressif AT version

|EX-CS-LOGO|

*******************************************************
ESP8266 (WiFi Boards) - AT Version Issues and Solutions
*******************************************************

|conductor| |tinkerer| |engineer| |support-button|

.. sidebar::

   .. contents:: On this page
      :local:
      :depth: 3

Unfortunately, other than the recommended *DCC-EX EX-WiFiShield 8266* and *Makerfabs ESP8266 WiFi Shield*, the Espressif ESP8266 based WiFi Boards that are available for sale routinely come with versions of the firmware that simply do not work with |EX-CS|. There was a run of Makerfabs boards from around May 2023 through October 2023 that had defective firmware from Expressif. You can use this tutorial to upgrade one of those boards if you have one. All boards manufactured after November 2023 have the correct firmware. These boards carry the DCC-EX logo on the bottom and display version 1.1 or later.

Which is correct version of the AT firmware
===========================================

:dcc-ex-text-size-200pct:`ONLY Version 1.7.4 is known to work reliably.`  

That means all versions both before or after 1.7.4 are *not* suitable.  So don't be fooled in thinking that if it has a version later than that it will be ok.  **It won't!**

Symptoms of an Incorrect firmware Version
=========================================

There several common symptoms of a an incorrect firmware version:

* If you set up the command station in |Access Point mode|, then the SSID (Network Name) the displayed will be "DCCEX_SAYS_BROKEN_FIRMWARE" or "UPDATE_ESP_FIRMWARE".
* You can't connect to the displayed Access Point.
* Your phone can connect to the Access Point, but can't connect your WiFi throttle (e.g. Engine Driver or WiThrottle) to the |EX-CS|. 
* You can connect and use a phone once, but it will not connect again unless you re-start the |EX-CS|.
* You can connect and use one phone, but it will not allow connection of a second phone, or the second phone works, but it disconnects the first phone.

|hr-heavy|

Find Your AT Version
====================

It is important to find out which version of the firmware you board has and correct it if necessary.

There are two basic ways that you can check:

* :ref:`AFTER you load the EX-CommandStation software <support/wifi-at-version:Checking AFTER you load the EX-CommandStation software>`
* :ref:`BEFORE you load the EX-CommandStation software <support/wifi-at-version:Checking BEFORE you load the EX-CommandStation software>`

----

Checking AFTER you load the EX-CommandStation software
--------------------------------------------------------

One you have loaded the |EX-CS| software you will be able to see the AT version in the start-up log by connecting the serial monitor in either the |EX-I| or **Arduino IDE** (whichever you used to upload the |EX-CS| onto your device).

You can check the AT version two ways. Which is best for you depends on how you loaded the |EX-CS| software:

* :ref:`Using EX-Installer <support/wifi-at-version:Checking the AT version using EX-Installer>`
* :ref:`Using the Arduino IDE <support/wifi-at-version:Checking the AT version with the Arduino IDE>`

|hr-dashed|

Checking the AT version using EX-Installer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have successfully loaded the |EX-CS| software:

1. Click back through the pages of the |EX-I| till you get to the 'Select your Device' screen
2. Click on the :guilabel:`View device monitor` button |BR| A new window will open and a lot of text will appear
3. You need to look for a line that will have a section highlighted in green

e.g. ``AT version:1.7.4.0(May 11 2020 19:13:04)``

Alternately, you can enter the command ``<+GMR>`` and click :guilabel:`Send`.  A similar line will be shown.

If it says **anything other than** 1.7.4 in that line, then you have the wrong version you will need to :ref:`follow the instructions at the end of this page <support/wifi-at-version:What to do if you have the wrong AT Firmware version>` to correct it.

|hr-dashed|

Checking the AT version with the Arduino IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you loaded the |EX-CS| software using the Arduino, once you have successfully loaded the |EX-CS| software:

1. select **Tools** -> **Serial monitor** from the menus
2. A new pane will open at the bottom of the IDE window will open and a lot of text will appear
3. you need to look for a line similar to the following

e.g. ``AT version:1.7.4.0(May 11 2020 19:13:04)``

Alternately, you can enter the command ``<+GMR>`` and click :guilabel:`Send`.  A similar line will be shown.

If it says **anything other than** 1.7.4 in that line, then you have the wrong version you will need to :ref:`follow the instructions at the end of this page <support/wifi-at-version:What to do if you have the wrong AT Firmware version>` to correct it.

|hr-heavy|

Checking BEFORE you load the EX-CommandStation software
-------------------------------------------------------

How to check before you load the |EX-CS| software will depend on which WiFi shield or board you are using:

* :ref:`ESP-01 or ESP-01s <support/wifi-at-version:Checking the AT version of a ESP-01 or ESP-01s>`
* :ref:`Makerfabs ESP8266 Wifi Shield <support/wifi-at-version:Checking the AT version of a Makerfabs ESP8266 Wifi Shield>`
* :ref:`Duinopeak ESP8266 WiFi Expansion board <support/wifi-at-version:Checking the AT version of a Duinopeak ESP8266 WiFi Expansion Board>`
* :ref:`Mega+WiF board <support/wifi-at-version:Checking the AT version of a Mega+WiFi>`

----

Checking the AT version of a ESP-01 or ESP-01s
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /_static/images/esp-01/esp-01.png
   :alt: ESP-01
   :scale: 20%

   ESP-01

There are a number of ways that you can check the AT version an a ESP-01 or ESP-01s:

* with a USB Serial Adapter
* with a USB to TTL CH340G Converter Module Adapter
* with a Arduino Uno

|hr-dashed|

Checking the AT version of a ESP-01 with a USB Serial Adapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /_static/images/esp-01/CH340G-USB-to-TTL(serial)-converter.png
   :class: image-float-right
   :alt: CH340G USB to TTL(serial) Converter
   :scale: 35%

1. Connect the ESP01 to the serial adapter with the instructions on here: https://remotexy.com/en/help/esp8266-firmware-update (see the section on 'Connection via the USB-UARt adapter') |BR| Note the orange wire is not needed for checking the AT version.
2. Plug the serial adapter it the PC
3. Open the Arduino IDE 
4. Select **Tools** -> **Serial monitor** from the menus
5. Select baud: ``115200`` and ``Both NL & CR``
6. A new pane will open at the bottom of the IDE window will open
7. Enter the command ``AT+RST`` and click :guilabel:`Send`.
8. Enter the command ``AT+GMR`` and click :guilabel:`Send`.

It will reply with something like ``AT version:1.7.4.0(May 11 2020 19:13:04)``

If it says **anything other than** 1.7.4 in that line, then you have the wrong version you will need to :ref:`follow the instructions at the end of this page <support/wifi-at-version:What to do if you have the wrong AT Firmware version>` to correct it.

|hr-dashed|

Checking the AT version of a ESP-01 a with a USB to TTL CH340G Converter Module Adapter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: `Checking AT version with a USB to TTL CH340G Converter Module Adapter prior to upload`

.. image:: /_static/images/esp-01/USB-to-ESP-01-adapter-early.png
   :class: image-float-right
   :alt: Early ESP-01 USB adapter
   :scale: 20%

.. image:: /_static/images/esp-01/USB-to-ESP-01-adapter.png
   :class: image-float-right
   :alt: ESP-01 USB adapter
   :scale: 25%

.. image:: /_static/images/esp-01/USB-to-ESP-01s-adapter.png
   :class: image-float-right
   :alt: ESP-01s USB adapter
   :scale: 20%

1. Connect the ESP01 to the adapter
2. Plug the adapter it the PC
3. Open the Arduino IDE 
4. Select **Tools** -> **Serial monitor** from the menus
5. Select baud: ``115200`` and ``Both NL & CR``
6. A new pane will open at the bottom of the IDE window will open
7. Enter the command ``AT+RST`` and click :guilabel:`Send`.
8. Enter the command ``AT+GMR`` and click :guilabel:`Send`.

It will reply with something like ``AT version:1.7.4.0(May 11 2020 19:13:04)``

If it says **anything other than** 1.7.4 in that line, then you have the wrong version you will need to :ref:`follow the instructions at the end of this page <support/wifi-at-version:What to do if you have the wrong AT Firmware version>` to correct it.


|hr-dashed|

Checking the AT version of a ESP-01 a with a Arduino Uno
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: `Checking AT version with a Arduino Uno prior to upload`

----

Checking the AT version of a Makerfabs ESP8266 WiFi Shield
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /_static/images/wifi/makerfabs-esp8266-wifi-shield.png
   :class: image-float-right
   :alt: Makefabs ESP8266 WiFi Shield
   :scale: 25%

.. todo:: `Checking AT version ESP8266 Wifi Shield prior to upload`

|force-break|

-----

Checking the AT version of a Duinopeak ESP8266 WiFi Expansion Board 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /_static/images/wifi/duinopeak.png
   :class: image-float-right
   :alt: Duinopeak ESP8266 WiFi Expansion Board
   :scale: 25%

.. todo:: `Checking AT version ESP8266 WiFi Expansion Board prior to upload`

|force-break|

----

Checking the AT version of a Mega+WiFi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /_static/images/assembly/mega_wifi.png
   :class: image-float-right
   :alt: Mega + WiFi
   :scale: 25%

.. todo:: `Checking AT version Mega+WiFi prior to upload`

|force-break|

|hr-heavy|

|hr-heavy|

What to do if you have the wrong AT Firmware version
====================================================

The steps necessary to correct the AT version will depend on your hardware:

* :ref:`ESP-01 or ESP-01s <support/wifi-at-version:Correcting the AT version on a ESP-01>`
* :ref:`Makerfabs ESP8266 Wifi Shield <support/wifi-at-version:Correcting the AT version on a Makerfabs ESP8266 Wifi Shield>`
* :ref:`Duinopeak ESP8266 WiFi Expansion board <support/wifi-at-version:Correcting the AT version on a Duinopeak ESP8266 WiFi Expansion Board>`
* :ref:`Mega+WiF board <support/wifi-at-version:Correcting the AT version on a Mega+WiFi>`

We strongly recommend upgrading or downgrading to the "NonOS AT" version 1.7.4 available on our :doc:`/download/esp8266` download page **prior** to reaching out for support from the team.

----

Correcting the AT version on a ESP-01
-------------------------------------

Correcting the AT version of a ESP-01or ESP01s requires additional hardware. One of following is required:

* A USB to ESP-01 Adapter
* A USB to TTL CH340G Converter Module Adapter
* An Arduino Uno

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

Correcting a ESP-01 with a USB Serial Adapter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /_static/images/esp-01/CH340G-USB-to-TTL(serial)-converter.png
   :class: image-float-right
   :alt: CH340G USB to TTL(serial) Converter
   :scale: 35%

See https://remotexy.com/en/help/esp8266-firmware-update/

|force-break|

|hr-dashed|

Correcting a ESP-01 with a USB to ESP-01 Adapter Board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Correcting a ESP-01 or ESP-01s with a USB to TTL CH340G Converter Module Adapter

.. image:: /_static/images/esp-01/USB-to-ESP-01-adapter-early.png
   :class: image-float-right
   :alt: Early ESP-01 USB adapter
   :scale: 20%

.. image:: /_static/images/esp-01/USB-to-ESP-01-adapter.png
   :class: image-float-right
   :alt: ESP-01 USB adapter
   :scale: 25%

.. image:: /_static/images/esp-01/USB-to-ESP-01s-adapter.png
   :class: image-float-right
   :alt: ESP-01s USB adapter
   :scale: 20%

The early/normal boards needs to be modified to be able to temporarily connect GND to GPIO 0.

See here for the modification needed https://www.mogtour.com/wp-content/uploads/2021/01/ch340g.pdf

Later boards do not require the modification.

See https://www.allaboutcircuits.com/projects/update-the-firmware-in-your-esp8266-wi-fi-module/

|force-break|

|hr-dashed|

Correcting a ESP-01 with a Arduino Uno
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See https://cordobo.com/2300-flash-esp8266-01-with-arduino-uno/

Or https://remotexy.com/en/help/esp8266-firmware-update/

|force-break|

----

Correcting the AT version on a Makerfabs ESP8266 Wifi Shield
------------------------------------------------------------

.. image:: /_static/images/wifi/makerfabs-esp8266-wifi-shield.png
   :class: image-float-right
   :alt: Makefabs ESP8266 WiFi Shield
   :scale: 25%

There are **two** options for correcting the AT version on a Makerfabs ESP8266 Wifi Shield:

* With a USB to TTL Converter Module Adapter (recommended)
* With an Arduino Mega

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

Correcting the Makerfabs ESP8266 WiFi Shield With a USB to TTL Converter Module Adapter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Recommended approach**

.. note:: 

   Some people have experienced problems with v3.8.5 of the flash download tool (available from the DCC-EX Downloads) when following the instructions of the linked page. They have had more success with v2.3 (`available here <https://bbs.espressif.com/viewtopic.php?f=57&t=433>`_ or `here <https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.14core.com%2Fwp-content%2Fuploads%2F2015%2F11%2FFLASH_DOWNLOAD_TOOLS_v2.4_150924.rar%3Ffbclid%3DIwAR0fbvEFz8kDSJA2gTxfoELxjCpgJ4gLrUMIVEAAT7-ZijUz-zuw2u_IEJA&h=AT3orFt4zGDT6TJWu5vN8gZR0KZFSn4hRPNNlBdQKeKx1LjnKgFjnu9JoOstmKL7q90ov6R72eVhyEwr1Y_ihZHSSB-QH1uWg4WNtooVT410DOxdcDxu-ULhKLdj6BWlEuyJ&__tn__=R]-R&c[0]=AT0mJaTY7Uijw9oHkwCS233Z0qIwndZX4AYG3yer1G5pY4U9f9osL8pTpec-sKJbToYfoS3uqUEKouusXV1zj8Kidqz8fH2PgtWFNWo0UeXthti6kuASi3JyJftjnOACvcXV6PF1YAZW_3xKKmLERyurXizuFx7V>`_.) 

   If you don't succeed after several attempts with v3.8.5 try v2.3 instead.

See https://gist.github.com/nathankellenicki/7008540322c617869cec17226cff579d   

Also see a detailed video by Andrew from `Wotton Tor <https://www.youtube.com/@AndrewH561>`_ - `Flashing the Makerfabs wifi board <https://www.youtube.com/watch?v=mNHlDmCnPMU>`_  (The flashing demo starts about 9 minutes into the video.)

|hr-dashed|

Correcting the Makerfabs ESP8266 WiFi Shield With an Arduino Mega
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning:: 

   The instructions on the following page have been proven to work on Linux PCs, so will probably work on macOS PCs (Apple), however attempts to get them to work on **Microsoft Windows PCs** :dcc-ex-red-bold:`have so far been unsuccessful`. We need to do more testing. If you have an issue with this method, simply purchase a USB to TTL converter module and use the recommended process in the previous heading. This should not be an issue for most people since they will have the DCC-EX EX-WiFi Shield 8266 which has the correct firmware and a much easier upgrade process should that be required in the future.

Flashing the ESP8266 WiFi Shield :doc:`using an Arduino Mega is covered here </support/makerfabs-update-at-version-with-mega>`.

|force-break|

----

Correcting the AT version on a Duinopeak ESP8266 WiFi Expansion Board 
---------------------------------------------------------------------

.. image:: /_static/images/wifi/duinopeak.png
   :class: image-float-right
   :alt: Duinopeak ESP8266 WiFi Expansion Board
   :scale: 25%

.. todo:: `Correcting AT version Duinopeak ESP8266 WiFi Expansion Board`

|force-break|

----

Correcting the AT version on a Mega+WiFi
----------------------------------------

.. image:: /_static/images/assembly/mega_wifi.png
   :class: image-float-right
   :alt: Mega + WiFi
   :scale: 25%

Flashing the ESP8266 chip on a Mega+WiFi is covered in detail :doc:`here </reference/hardware/microcontrollers/wifi-mega>`.

|force-break|
