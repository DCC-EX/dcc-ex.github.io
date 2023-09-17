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
      :depth: 2

Unfortunately the Espressif ESP8266 based WiFi Boards that are available for sale routinely come with versions of the firmware that simply do not work with |EX-CS|. This now seems to include the recommended `Makerfabs ESP8266 WiFi Shield <https://www.makerfabs.com/esp8266-wifi-shield.html>`_.

Which is correct version of the AT firmware
===========================================

Only **version 1.7.4** is known to work reliably.  

That means all versions bother before or after 1.7.4 are *not* suitable.  So don't be fooled in thinking that if it has a version later than that it will be ok.  **It won't!**

Symptoms of an Incorrect firmware Version
=========================================

There several common symptoms of a an incorrect firmware version

# You can't connect to the SSID
# You can connect to the SSID, but can't connect your WiFi throttle to the CommandStation (e.g.g Engine Driver or wiThrottle)
# You can connect once, but it will not connect again unless you shut down the |EX-CS|


Find out Your AT Version
========================

It is important to find out which version of the firmware you board has and correct it if necessary.

There are two basic ways that you can check:

* after you load the |EX-CS| software
* before you load the |EX-CS| software

Checking after you load the |EX-CS| software
--------------------------------------------

One you have loaded the |EX-CS| software you will be able to the AT version in the start-up log, but connecting the serial monitor in either the |EX-I| or Arduino IDE (whichever you used to upload the |EX-CS| onto your device).

Checking using EX-Installer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have successfully loaded the |EX-CS| software:

1. click back through the pages of the |EX-I| till you get to the 'Select your Device' screen
2. Click on the :guilabel:`View device monitor` button |BR| A new window will open lot of text will appear
3. you need to look for a line that will have a section highlighted in green

e.g. ``AT version:1.7.4.0(May 11 2020 19:13:04)``

If it says **anything other than** 1.7.4 in that link, then you have the wrong version you will need to follow the instructions at the end of this page to correct it.

Checking with the Arduino IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..todo:: `Checking AT version with the Arduino IDE`


Checking before you load the |EX-CS| software
---------------------------------------------

How to check before you load the |EX-CS| software will depend on which WiFi shield or board you are using.

Checking ESP-01
^^^^^^^^^^^^^^^

..todo:: `Checking AT version ESP-01 prior to upload`


Checking ESP8266 Wifi Shield
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..todo:: `Checking AT version ESP8266 Wifi Shield prior to upload`


Checking Duinopeak ESP8266 WiFi Expansion Board 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Checking Mega+WiFi
^^^^^^^^^^^^^^^^^^

..todo:: `Checking AT version Mega+WiFi prior to upload`


----

What to do if you have the wrong version
========================================

The steps necessary to correct the version will depend on you hardware.

We highly recommend upgrading or downgrading to the "NonOS AT" version 1.7.4 available on our :doc:`/download/esp8266` download page prior to reaching out for support from the team.


Correcting the AT version on a ESP-01
-------------------------------------

..todo:: `Correcting AT version ESP-01`


Correcting the AT version on a ESP8266 Wifi Shield
--------------------------------------------------

..todo:: `Correcting AT version ESP8266 Wifi Shield`

Correcting the AT version on a Duinopeak ESP8266 WiFi Expansion Board 
---------------------------------------------------------------------

Correcting the AT version on a Mega+WiFi
----------------------------------------

Flashing the ESP8266 chip on a Mega+WiFi is covered in detail :doc:`here </reference/hardware/microcontrollers/wifi-mega>`.

