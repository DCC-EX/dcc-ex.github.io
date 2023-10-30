:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: WiFi setup Espressif AT version

|EX-CS-LOGO|

*******************************************************
Makerfabs ESP8266 - Update AT Version with Uno or Mega
*******************************************************

|conductor| |Tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :local:
      :depth: 3

Unfortunately the Espressif ESP8266 based WiFi Boards that are available for sale routinely come with versions of the firmware that simply do not work with |EX-CS|. This now seems to include the recommended `Makerfabs ESP8266 WiFi Shield <https://www.makerfabs.com/esp8266-wifi-shield.html>`_.

These instructions have been adapted from https://gist.github.com/nathankellenicki/7008540322c617869cec17226cff579d by Nathan Kellenicki. 

Introduction
============

Out of the box, the MakerFabs ESP8266 shield appears to be shipping with a broken firmware that is unstable when used with DCC-EX. I needed to flash version 1.7.4 onto the board. Here's how I did it - hopefully it works for you.

Requirements
============

* The WiFi Shield itself - https://www.makerfabs.com/esp8266-wifi-shield.html
* An Arduino Uno or Arduino mega
* 4x female to female jumper wires
* 1x male to male jumper wire
* The flash download tool and firmware files from DCC-EX - https://dcc-ex.com/download/esp8266.html
* A Windows PC

How To
======

Step 1 - Set up the download tool
---------------------------------

1. Extract both the download tool and firmware files zips
2. Open the download tool, select "Developer Mode", then "ESP8266 DownloadTool".
3. Ensure **all these settings** in the screenshow are set. Take special note of the files and the offset number next to them.
4. Ensure all five files are green - enable the checkbox next to each file after setting it.
5. Ensure the COM port is set to that of your adapter (You can find this in device manager after plugging it in and installing drivers).
6. Leave the window open, but DO NOT PRESS START YET.

.. image:: https://user-images.githubusercontent.com/2862695/228994914-942a9006-e119-4311-9524-eca5e632def2.png

Step 2 - Preparation
--------------------

* The UNO should be **unplugged from the USB port** at this stage.
* **No other power supply should be connected** to the Arduino or Motor Shield during this process.

Step 3 - Connect the Jumper Wires
---------------------------------

Connect the following:

1. Assemble the Wifi shield onto the Arduino. |BR| The WiFi Shield should be connected to the Arduino as per the |EX-CS| instructions.  The Motor Shield can also be in the stack.
2. Connect one jumper wire from the "RESET" to "GND".
3. Connect one jumper from the Wifi Shield "ESP_TXD" to the "RX" header or to "D0" on the shield. 
4. Connect one jumper from the Wifi Shield "ESP_RXD" to the "TX" header or to "D1" on the shield.

Your connections should look like this:

.. figure:: /_static/images/wifi/mega-for-flashing-makerfabs-wifi.png
   :alt: Arduino Mega - Wiring for flashing Makerfabs Wifi Shield
   :scale: 60%


Step 4 - Plug in the Arduino
----------------------------

The Arduino should still be unplugged from the USB port at this stage.

1. Connect one end of the the male-to-male jumper to the top of the "GND" pin on the WiFi shield.
2. Hold the other end of the male-to-male jumper onto the GPIO0 pin on the ESP-12F. (Note: The GPIO0 pin is the fourth pin from the bottom on the right, next to the "P" in "ESP-12F". See picture below.
3. KEEP HOLDING THE JUMPER ON THE PIN
4. Plug the adapter into a free USB port on your PC
5. KEEP HOLDING THE JUMPER ON THE PIN

.. image:: https://user-images.githubusercontent.com/2862695/228995714-de006673-56df-48ec-8428-ae78b2abc892.jpg

Step 5 - Start the flashing
---------------------------

1. KEEP HOLDING THE JUMPER ON THE PIN
2. Return to the download tool.
3. Press start.
4. KEEP HOLDING THE JUMPER ON THE PIN
5. Wait until the green box in the tool says "FINISH".
6. You can let go of the jumper now. :)

If you get an error, unplug the adapter, plug it back in, and press Start again. It can take a couple of tries. BUT KEEP HOLDING THE JUMPER ON THE PIN.

If at any point you let go of the jumper, unplug the adapter from the USB port, place the jumper back on the pin, and plug it back in, then click Start again. Remember to keep holding it.

When finished, it should look like this.

.. image:: https://user-images.githubusercontent.com/2862695/228996044-b6677ca0-5e58-4d7b-bf49-e8602fbdcd41.png

Step 6 - Use the WiFi shield
============================

You should now be able to disconnect the jumpers, place the shield it onto your DCC-EX setup, and if all went well it should work.