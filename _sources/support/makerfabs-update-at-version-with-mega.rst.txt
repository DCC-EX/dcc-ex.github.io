:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: WiFi setup Espressif AT version

|EX-CS-LOGO|

**********************************************************
Makerfabs ESP8266 - Update AT Version with an Arduino Mega
**********************************************************

|tinkerer| |engineer| |support-button|

.. sidebar::

   .. contents:: On this page
      :local:
      :depth: 3

Unfortunately many of the Espressif ESP8266 based WiFi Boards that are available for sale routinely come with versions of the firmware that simply do not work with |EX-CS|. The only boards guaranteed to work out of the box are the ones designed in a partnership between DCC-EX and Makerfabs. The board are the `EX-WifiShield 8266 <https://store.dcc-ex.com/products/EX-WiFiShield-8266-p625876731>`_ |EXTERNAL-LINK| available through our reseller network, and the `Makerfabs ESP8266 WiFi Shield <https://www.makerfabs.com/esp8266-wifi-shield.html>`_ |EXTERNAL-LINK|. If you have a Makerfabs shield that was made between May 2023 and October 2023, your board may have faulty firmware.

.. warning:: 

   The instructions on this page have been proven to work on Linux PCs, so will probably work on macOS PCs (Apple), however attempts to get them to work on **Microsoft Windows PCs** :dcc-ex-red-bold:`have so far been unsuccessful`. 

Introduction
============

Out of the box, the small run of MakerFabs ESP8266 shields made in late 2023 mentioned above shipped with a broken firmware on the chips from the Expressif factory that Makerfabs use in their production. This version is unstable when used with DCC-EX as well as other applications. To flash version 1.7.4 onto the board follow these instructions. Do NOT use these instructions to update any EX-WiFiShield 8266 boards since they do not need updating. Known good boards have the DCC-EX logo on the bottom and are stamped with v1.1 or later. The joint DCC-EX/Makerfabs board have a much easier process to update them should they ever need new firmware in the future.

Requirements
============

* The WiFi Shield itself - The previous version of the one shown here: https://www.makerfabs.com/esp8266-wifi-shield.html |EXTERNAL-LINK|
* An Arduino Uno or Arduino mega
* 2x female to male jumper wires |br| (or the two small, simple jumpers/plugs that came with the WiFi shield)
* 3x male to male jumper wire
* A Windows, iOS or Linux PC
* The esptool app
* The 1.7.4 firmware image (as a single file)

How To
======

|hr-dashed|

Step 1. Get esptool
-------------------

The ``esptool`` can be download separately, but the easiest way to get it is to use our |EX-I| which will automatically download it if you select the appropriate options.

1.1. If you have not already installed the |EX-I|, download the :ref:`EX-Installer <download/ex-commandstation:ex-Installer>` app.

1.2. Use the EX-Installer and run it 

   * For **Microsoft Windows**:
   
   * Open the Windows *File Manager*
   * Find the folder in which the **EX-Installer-Win64.exe** or **EX-Installer-Win32.exe** was saved. |BR| Generally this will default to downloading to the *downloads* folder but your browser may be configured differently.
   * **Run** ``EX-Installer-Win64.exe`` (or **EX-Installer-Win32.exe**) |BR| |BR| Note: depending on the configuration of your computer the '.exe' may or may not appear. This is not of concern.  |BR| |BR|

   * For **Apple macOS**:

   * Open a terminal window and navigate to the that folder that you downloaded the file to.  e.g.: |BR| ``cd Downloads``
   * Enter the following command to tell the OS that it is an executable: |BR| ``chmod +x EX-Installer-macOS``
   * **Run the installer with** the following command: |BR| ``./EX-Installer-macOS`` |BR| |BR|

   * For **Linux**:

   * Right-click on the file, go to Properties, then the Permissions tab, and check "Allow executing file as program"
   * Open a terminal window and navigate to that folder
   * **Run the installer with** the following command: |BR| ``./EX-Installer-Linux64`` |BR| |BR|

1.3 Select the options as if you are installing on a ESP32 until it fails (if you do not have an ESP32).

   * Connect your Arduino Mega to the PC with a USB cable
   * On the "Manage the Arduino CLI" page make sure the `Expressif ESP32` option is enabled
   * Click :guilabel:`Select your device`
   * Select ``ESP32 Dev Kit``
   * Click :guilabel:`Select product to install`


1.4. Now the ``esptool`` will be installed on your computer |br| It is important to be aware of where will be, as this is needed in later steps. (``ESPTOOL``)

   Windows: |BR|
   ``C:\Users\<userName>\AppData\Local\Arduino15\packages\esp32\tools\esptool_py\4.5.1\esptool.exe`` |BR|
   Mac: |BR|
   ``~/Library/Arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool_py`` |BR|
   Linux: |BR|
   ``~/.arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool.py``

|hr-dashed|

Step 2. Get the 1.7.4 as a whole image
--------------------------------------

2.1 Open `https://cdn.discordapp.com/attachments/735194734611398676/1171788863539261461/ESP8266_1MB_AT1_7.bin?ex=655df46b&is=654b7f6b&hm=dae2e165ba51eef1808caa5462e2b2a7887c1e2bc7b47f0bb1f933fe6cda83c7& <https://cdn.discordapp.com/attachments/735194734611398676/1171788863539261461/ESP8266_1MB_AT1_7.bin?ex=655df46b&is=654b7f6b&hm=dae2e165ba51eef1808caa5462e2b2a7887c1e2bc7b47f0bb1f933fe6cda83c7&>`_

This should give you a file called ``ESP8266_1MB_AT1_7.bin`` size 1MB md5sum b3019e7e85bdc0878324118b8e002236

|hr-dashed|

Step 3. Prepare the hardware
----------------------------

3.1. Disconnect the Arduino Mega from the PC

3.2. Put the Makerfabs ESP8266 WiFi shield on the Arduino Mega (if it is not already)

3.3 Connect the jumpers so that:

   * the RX of the ESP8266 is connected to the RX/D0 of the Arduino, and 
   * the TX of the ESP8266 is connected to the TX/D1 of the Arduino

3.4 Connect the ``RST`` (Reset) of the Arduino to ``GND`` on the Arduino

3.5 Prepare two jumper wires to ``GND`` (loose ends)

   .. figure:: /_static/images/wifi/mega-for-flashing-makerfabs-wifi-3.png
      :alt: Stacked Mega and WiFi Shield - Jumpers
      :scale: 50%

      Stacked Mega and Wifi Shield - Jumpers. |BR| Note: White and Black wires will be loose are this point

   *Alternate*

   .. figure:: /_static/images/wifi/mega-for-flashing-makerfabs-wifi-3-simple-jumpers.png
      :alt: Stacked Mega and WiFi Shield - Simple Jumpers
      :scale: 50%

      Stacked Mega and Wifi Shield - Using the small, simple jumpers/plugs that came with the shield. |BR| Note: the White and Black wires will be loose are this point


|hr-dashed|

Step 4.  Connect your computer
------------------------------

4.1 Connect your Arduino Mega to the PC with a USB cable

4.2 Use the "Select your device" page of the EX-Installer to connect to the Arduino

4.3 Remember the USB serial port name/number (``PORTNAME``) from your selection

4.4 Open the Device Monitor by clicking on :guilabel:`View Device Monitor`

4.5 Reset the ESP8266 by "touching" one of the jumper wires to ``Reset`` pad on the ESP8266 

   The ``Reset`` pad is the top pad on the left, closest to the resister labelled R6. 

   This should first produce gibberish and then "ready". 

   Note: The ``GPIO0`` (used in later steps) is "hold down", but the ``Reset`` is only "touch". 

4.6 Close the device monitor and installer :dcc-ex-red-bold:`(Important)`.

|hr-dashed|

Step 5. Flash with esptool
--------------------------

Make sure the Installer has been closed before continuing.

5.1 open a command prompt

   For Windows

      * click :guilabel:`Start Menu`
      * Type ``cmd`` and press the :guilabel:`Enter` key
      * Go to the folder you downloaded the ``ESP8266_1MB_AT1_7.bin`` file to (normally 'Downloads') by entering:
         
         ``c:`` :guilabel:`Enter` |BR|
         ``cd \user\<username>\downloads`` :guilabel:`Enter` |br| (Replace ``<username>`` with your username on the PC) 

   For Apple macOS

      * Click the Launchpad icon  in the Dock, type Terminal in the search field, then click Terminal or |BR| In the Finder , open the /Applications/Utilities folder, then double-click ``Terminal``.
      * Go to the folder you downloaded the ``ESP8266_1MB_AT1_7.bin`` file to by entering:
      
         ``cd ~\Downloads`` :guilabel:`Enter` 

   For Linux

      * On Ubuntu, you can hit ``ctrl+alt+T`` together to open a terminal. |br| Or right-click anywhere on the desktop and select ``Open in Terminal`` which will open the terminal with the desktop folder selected. |br| Or press the :guilabel:`Windows` key and type ``terminal``
      * Go to the folder you downloaded the ``ESP8266_1MB_AT1_7.bin`` file to by entering:

         ``cd ~\Downloads`` :guilabel:`Enter` 

5.2 Prepare the long command line. (but **don't** press :guilabel:`Enter` yet)

   For ``ESPTOOL`` and ``PORTNAME`` insert values from the steps above

   ``ESPTOOL --baud 38400 --port PORTNAME write_flash --erase-all --flash_freq 40m --flash_mode dout --flash_size 1MB 0x0 ESP8266_1MB_AT1_7.bin``

   For Example for Windows PCs : (if the Arduino is connected on COM3) |BR|
   ``C:\Users\<userName>\AppData\Local\Arduino15\packages\esp32\tools\esptool_py\4.5.1\esptool --baud 38400 --port COM3 write_flash --erase-all --flash_freq 40m --flash_mode dout --flash_size 1MB 0x0 ESP8266_1MB_AT1_7.bin`` |BR|
   Note: that ``<username>`` needs to be replaced with 'your' user name on the PC.

   If the program is python (iOS or Linux) you need to prepend python3 like this: (If the Arduino is connect on /dev/ttyUSB0) |BR|
   ``python3 ~/.arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool.py  --baud 38400 --port /dev/ttyUSB0 write_flash --erase-all --flash_freq 40m --flash_mode dout --flash_size 1MB 0x0 ESP8266_1MB_AT1_7.bin``

5.3 Locate the Reset and GPIO0 pads on the ESP8266.

   The ``GPIO0`` pad is the fourth pad from the bottom on the right, next to the "P" in "ESP-12F".  |BR|
   The ``Reset`` pad is the top pad on the left, closest to the resister labelled "R6". 

5.4 Press :guilabel:`enter` on the above command line. 

   You should see ``connecting`` and dots and dashes.

5.5 Take one GND jumper and HOLD (keep holding) to ``GPIO0`` pad

   Note: The GPIO0 pin is the fourth pin from the bottom on the right, next to the "P" in "ESP-12F". See picture below.

   .. figure:: /_static/images/wifi/mega-for-flashing-makerfabs-wifi-2.jpg
      :alt: GPIO0 ESP8266
      :scale: 10%

      GPIO0 ESP8266

   If you loose contact on the GPIO0 you need to Reset again and start over.

5.6 Take other GND jumper and TOUCH ``Reset`` pad (While still holding the other jumper to ``GPIO0`` pad)

   The ``Reset`` pad is the top pad on the left, closest to the resister labelled "R6". 

   Note: The ``GPIO0`` is "hold down" but the ``Reset`` is "touch". 

5.7 Now you should see text and "Writing....(xx %)". Keep holding the ``GPIO0`` jumper until you see "Hash of data verified".

   If you loose contact on the GPIO0 you need to Reset again and start over.

|hr-dashed|

Step 6. Check that flash was successful
---------------------------------------

6.1 Connect according to 4.x above

6.2 Type AT+GMR and :guilabel:`Send``

6.2 Your shield should answer with the new 1.7.4 version number.

Step 7. Prepare your EX-CommandStation
--------------------------------------

7.1. Disconnect the Arduino Mega from the PC

7.2 Remove Arduino ``RST`` (Reset) to ``GND`` jumper

7.3 Remove TX-TX and RX-RX jumpers

7.4 Assemble your EX-CommandStation setup including the Motor Shield and WiFi shield

7.5 Connect the TX to RX and RX to TX pins as per the initial assembly instructions for the |EX-CS|

   * Esp TX -> arduino RX1
   * Esp RX -> arduino RX1

   Remember: The wires are crossed.

   .. figure:: /_static/images/assembly/wifi_jumpers2.png
      :alt: Install the Jumper wires
      :scale: 50%

      Install the jumper wires

7.6 If you have not already done so, run the |EX-I| and configure your |EX-CS| to use the WiFi shield. |BR| Note: this is not necessary if it was done before you started flashing the WiFi firmware.  i.e. Flashing the firmware *does not* upset the software you loaded on the Arduino.

----

You should now be able to set your EX-CommandStation to use, and if all went well it should work.
