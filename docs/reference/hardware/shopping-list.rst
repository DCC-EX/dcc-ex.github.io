.. include:: /include/include.rst
.. include:: /include/include-l2.rst
**************
Shopping List
**************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

.. NOTE:: There are many sources and sometimes different names for Mega and Motor Shield clones. Please see the Microcontroller Boards and Motor Boards page for info on specific motor boards and links of where to find them.

:doc:`/reference/hardware/motor-boards`
:doc:`/reference/hardware/microcontroller-boards`

CS Hardware
============

`Elegoo Mega 2560 <https://www.amazon.com/ELEGOO-ATmega2560-ATMEGA16U2-Projects-Compliant/dp/B01H4ZLZLQ/>`_

`Deek-Robot Motor Shield <https://www.aliexpress.com/item/32832049214.html>`_

`12V 5Amp Power Supply for the Track <https://www.amazon.com/LEDMO-Power-Supply-Transformers-Adapter/dp/B01461MOGQ/>`_ (connects to the motor shield)

`9V 1Amp Power Supply for the Arduino <https://www.amazon.com/Arduino-Power-Supply-Adapter-110V/dp/B018OLREG4/>`_ for options

`Raspberry Pi 4B <https://www.google.com/search?q=raspberry+pi+4&tbm=shop>`_

.. note:: You may use your own computer instead of the Raspberry Pi. However, the image software below saves you installing software on your computer and does a lot more. See: "My Computer vs. Raspberry Pi" <insert link here> 

You can check Amazon, eBay, AliExpress, Banggood, Adafruit, SparkFun and others for all the above

Software
=========

* `EX-Installer <https://github.com/DCC-EX/BaseStation-Installer/releases/tag/v2.1>`_
* `Steve Todd's Raspberry Pi Image (If you wannt to use a Pi) <https://mstevetodd.com/rpi>`__
* `JMRI (If you want to use a laptop or desktop) <https://www.jmri.org/>`_
* `Arduino Software IDE to edit and upload changes (Optional) <https://www.arduino.cc/>`_
* `WebThrottle-EX Controller <https://DCC-EX.github.io/WebThrottle-EX>`_

CS Build Review
================

This can be a little confusing, so let explain it a different way:

  1. You will need to build a command station with An Arduino and a Motor Controller and, optionally, an ESP8266 WiFi shield

  2. You will need a power supply connected to the motor shield to power your track and will need a separate source of power for the Arduino (or perhaps not, keep reading)

  3. You will need a computer and a USB cable to download software and then upload it to the Arduino. You may also want to download an SDCard image to use a Raspberry Pi instead of a computer to upload your Command Station software and run a controller.

  4. You will need a controller that sends commands to the CS and controls your trains. That controller can be any one of the following:

    1. A computer capable of running a Chromium based browser to use our WebThrottle-EX to connect to the CS via a USB cable. This computer does not need to be connected to the internet once you download the WebThrottle-EX files to your computer.

    2. A computer running JMRI. JMRI connects via the USB cable to the CS and you control your trains with the Throttles built into JMRI. You can also use the WiThrottle server built into JMRI to connect any |WiThrottle Protocol| controller (such as the |Engine Driver| mobile app) via WiFi to JMRI and control your layout that way. 
    
    3. A Raspberry Pi as a computer. You can do any of the things mentioned in 1 and 2 above. With Steve Todd's image burned to an SDCard and installed in the Raspberry Pi, JMRI, the WiThrottle Server with networking, and more is installed and running when you boot. You still need a USB cable to connect the Pi to the CS.

    4. If you install an ESP8266 WiFi Shield, you don't need a computer or a Pi if you don't want it once you upload the software to the Arduino. You can connect directly to the CS via WiFi using any |WiThrottle Protocol| controller such as |Engine Driver| running on a WiFi device like your mobile phone.

.. note:: The computer USB port in option 1, 2, or 3 may be able to be the power supply for the Arduino (but you will still need a 12-14V DC power supply for the motor shield) See :doc:`Power Supplies <power-supplies>` for information on how to choose the right power supplies and different ways you can power the Arduino.
  
Add-Ons
========

This is just the beginning. You may want to add some items, like a display, or a board to control accessories like lights, motors, and servos. See the :doc:`Hardware Index Page </reference/hardware/index>` for information and more shopping list links.



