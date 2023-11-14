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

|conductor| |Tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :local:
      :depth: 3

Unfortunately the Espressif ESP8266 based WiFi Boards that are available for sale routinely come with versions of the firmware that simply do not work with |EX-CS|. This now seems to include the recommended `Makerfabs ESP8266 WiFi Shield <https://www.makerfabs.com/esp8266-wifi-shield.html>`_.

Introduction
============

Out of the box, the MakerFabs ESP8266 shield appears to be shipping with a broken firmware that is unstable when used with DCC-EX. To flash version 1.7.4 onto the board follow these instructions.

Requirements
============

* The WiFi Shield itself - https://www.makerfabs.com/esp8266-wifi-shield.html
* An Arduino Uno or Arduino mega
* 2x female to male jumper wires
* 2x male to male jumper wire
* A Windows, iOS or Linux PC
* The esptool app
* The 1.7.4 firmware image (as a single file)

How To
======

Step 1. Get esptool
-------------------

1.1. Use the EX-Installer and run it like you would install on a ESP32 until it fails (if you do not have an ESP32).

1.2. Now the esptool is on your computer:

   Windows: |br|
   C:\Users\<userName>\AppData\Local\Arduino15\packages\esp32\tools\esptool_py\4.5.1\esptool.exe |br|
   Mac: |br|
   ~/Library/Arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool_py |br|
   Linux: |br|
   ~/.arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool.py

Step 2. Get the 1.7.4 as a whole image
--------------------------------------

2.1 Open https://cdn.discordapp.com/attachments/735194734611398676/1171788863539261461/ESP8266_1MB_AT1_7.bin?ex=655df46b&is=654b7f6b&hm=dae2e165ba51eef1808caa5462e2b2a7887c1e2bc7b47f0bb1f933fe6cda83c7&

This should give you a file called ``ESP8266_1MB_AT1_7.bin`` size 1MB md5sum b3019e7e85bdc0878324118b8e002236

Step 3. Prepare the hardware
----------------------------

3.1. Put the makerfabs shield on the Arduino Mega.

3.2 Connect the jumpers so that:

   * the RX of the ESP8266 is connected to the RX/D0 of the Arduino, and 
   * the TX of the ESP8266 is connected to the TX/D1 of the Arduino

3.3 Connect the Reset of the Arduino to GND

3.4 Prepare two jumper wires to GND (loose ends)

Step 4.  Connect your computer
------------------------------

4.1 Use the Device monitor of the EX-Installer to connect to the Arduino

4.2 Remember the USB serial port name/number

4.3 Use one of the jumper wires to reset the ESP8266. This should first produce gibbrish and then "ready". |br| 
Note: The GPIO0 pin is the fourth pin from the bottom on the right, next to the "P" in "ESP-12F". See picture below.

.. figure:: /_static/images/wifi/mega-for-flashing-makerfabs-wifi-2.jpg
   :alt: Reset ESP8266
   :scale: 20%

   Reset ESP8266

4.4 Close the device monitor and installer (important).

Step 5. Flash with esptool
--------------------------

5.1 Prepare the long command line. |br|
    For ESPTOOL and PORTNAME insert values from above

``ESPTOOL --baud 38400 --port PORTNAME write_flash --erase-all --flash_freq 40m --flash_mode dout --flash_size 1MB 0x0 ESP8266_1MB_AT1_7.bin``

If the program is python you need to prepend python3 like this for my Linux computer:

``python3 ~/.arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool.py  --baud 38400 --port /dev/ttyUSB0 write_flash --erase-all --flash_freq 40m --flash_mode dout --flash_size 1MB 0x0 ESP8266_1MB_AT1_7.bin``

5.2 Locate the Reset and GPIO0 pads on the ESP8266.

5.3 Press enter on the above command line. You should see "connecting" and dots and dashes.

5.4 Take one GND jumper and HOLD (keep holding) to GPIO0 pad

5.5 Take other GND jumper and touch Reset pad

5.6 Now you should see text and "Writing....(xx %)" Keep holding GPIO0 until you see "Hash of data verified".

Step 6. Check that flash was successful
---------------------------------------

6.1 Connect according to 4.x above

6.2 Type AT+GMR and "enter/return"

6.2 Your shield should answer with the new 1.7.4 version number.

Step 7. Connect to Arduino
--------------------------

7.1 Remove TX-TX and RX-RX jumpers

7.2 Connect the TX to RX and RX to TX pins as per the initial assembly instructions for the |EX-CS|

.. figure:: /_static/images/assembly/wifi_jumpers2.png
   :alt: Install the Jumper wires
   :scale: 50%

   Install the jumper wires

7.3 Remove Arduino Reset jumper

You should now be able to assemble your EX-CommandStation setup, and if all went well it should work.