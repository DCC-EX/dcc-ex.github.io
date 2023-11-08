:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: WiFi setup MakerFabs Espressif AT version CP2104

|EX-CS-LOGO|

*****************************************************************************
Makerfabs ESP8266 - Update AT Version with Makerfabs USB to TTL flasher board
*****************************************************************************

|conductor| |Tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :local:
      :depth: 3

Unfortunately the Espressif ESP8266 based WiFi Boards that are available for sale routinely come with versions of the firmware that simply do not work with |EX-CS|. This now seems to include the recommended `Makerfabs ESP8266 WiFi Shield <https://www.makerfabs.com/esp8266-wifi-shield.html>`_.

Introduction
============

Out of the box, the MakerFabs ESP8266 shield appears to be shipping with a broken firmware that is unstable when used with DCC-EX. To flash version 1.7.4 onto the board follow these instructions.

.. figure:: /_static/images/wifi/CP2104-USB-to-Serial-Converter-Arduino-Programmer.png
   :alt: CP2104 USB to Serial Converter Arduino Programmer
   :scale: 60%

   CP2104 USB to Serial Converter Arduino Programmer - back

.. note:: 
   
   These instructions are specific to using Makerfabs' own **CP2104 USB to Serial Converter Arduino Programmer**, not USB to TTL boards from other manufacturers.

Requirements
============

* The WiFi Shield itself - https://www.makerfabs.com/esp8266-wifi-shield.html
* An CP2104 USB to Serial Converter Arduino Programmer - https://www.makerfabs.com/cp2104-usb-to-serial-converter.html
* 4x female to male jumper wires
* 2x male to male jumper wire
* The flash download tool and firmware files from DCC-EX - https://www.espressif.com/sites/default/files/tools/flash_download_tool_3.9.3_0.zip
* A Windows PC

How To
======

Step 1 - Set up the download tool
---------------------------------

1. Extract both the download tool and firmware files zips
2. Do not connect the USB yet

Step 2 - Connect the Jumper Wires
---------------------------------

Connect the following:

1. Adjust the switch to 5V
2. Connect jumpers from the **ESP12F USB to Serial Converter** to the **WiFi Shield** as follows:
 
   * VCC --> 5V
   * GND --> GND
   * RXD --> ESP_TX
   * TXD --> ESP_R
   * BOOT --> GPIO0
   * RES --> RST

.. figure:: /_static/images/wifi/CP2104-USB-to-Serial-Converter-Arduino-Programmer_back.png
   :alt: CP2104 USB to Serial Converter Arduino Programmer - back
   :scale: 60%

   CP2104 USB to Serial Converter Arduino Programmer - back

Step 3 - Start the flashing
---------------------------

1. Plug a USB into to PC and the CP2104 USB to Serial Converter Arduino Programmer
2. Start Espressif's download tool
3. Select ESP8266 and set it as follows:

   * It is recommended to increase the baud rate to 1152000, which will make the download faster.

5. Click START. If there is no response, repeat step 2.
6. Wait for the download to complete
7. A successful result should look like:

.. figure:: /_static/images/wifi/CP2104-USB-to-Serial-Converter-Arduino-Programmer-flashing.png
   :alt: CP2104 USB to Serial Converter Arduino Programmer - flashing 
   :scale: 60%

   CP2104 USB to Serial Converter Arduino Programmer - flashing 

Step 4 - Use the WiFi shield
----------------------------

You should now be able to disconnect the jumpers, place the shield it onto your DCC-EX setup, and if all went well it should work.