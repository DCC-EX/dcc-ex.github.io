.. include:: /include/include-ex-cs.rst
.. include:: /include/include.rst
.. include:: /include/include-l3.rst
|EX-CS-LOGO|

***************
WiFi Connection
***************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

This page describes all the supported WiFi options of the |EX-CS|.  If you identify as an a |conductor-text| and have installed only the recommended hardware we suggest that you look at the guide on the :doc:`/ex-commandstation/get-started/wifi-setup` page.

----

The purpose of this WiFi solution is for connecting up to 5 WiFi Throttles DIRECTLY to the |EX-CS|, eliminating the need for a computer and another software controller. However, WiFi is optional. If you wish to simply use your computer connected via a USB cable to to the Command Station using something like |JMRI|, you can :doc:`skip ahead to the next page </ex-commandstation/get-started/installer>`.

There are many ways to add WiFi to your Command Station. We will cover four supported methods here.

You should be able to apply what you learn here to using other boards, but you can ask us for help using any of the contact links on our :doc:`Support Page </support/index>` if you have a question.

Note that you can click on any of the images to make them larger.

.. sidebar:: Optional connection direct to a computer running JMRI
   
   |conductor|

   The instructions on this page are NOT for making a connection to |JMRI|. Use a USB cable instead (or wireless USB Bridge like the HC-12). The WiFi and Ethernet solutions are designed to allow throttles (controllers) to connect directly to the |EX-CS| without the need for any other software such as |JMRI|. While using a WiFi/Ethernet connection to |JMRI| will work, the overhead required internally will slow performance, take up valuable system memory, and prevent broadcast messages for sensors and power state.

For a video to help you, click below.

   .. raw:: html
      
      <iframe width="336" height="189" src="https://www.youtube.com/embed/N6TWR7fIl0A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Why Use WiFi?
=============

**BEFORE you purchase a Wifi card, please consider whether you actually need it:**

With the base Command Station (CS) consisting of just an Arduino Mega and an Arduino Motor Driver (no WiFi board), you must use a USB cable to connect to a computer to run |JMRI| or our |EX-WT|, or to connect to another controller. The controller (aka Throttle) is what sends commands to the Command Station to run your trains and control your accessories.

If you intend to run trains from a PC or Raspberry Pi, either by entering <DCC++> commands, by using |EX-WT|, |JMRI|, Rocrail, or similar, then YOU DO NOT NEED WiFi ON THE Command Station. Save yourself some money, and a lot of hassle, by buying a longer USB cable (or a Wireless USB bridge (HC-12) if you prefer). Using Wifi (OR Ethernet) to talk between |JMRI| and CommandStation is complex, slow and functionally limited and is therefore NOT SUPPORTED. However, you can STILL use a wireless throttle with a |JMRI| setup. The computer or Pi you use to run your train software will already have WiFi capability, and you can connect through THAT instead of directly to the Command Station, while the Command Station gets its commands through the USB connection.

If you wish to disconnect your PC/Pi and run trains from your phone or tablet using ONLY |Engine Driver| (or other |WiThrottle Protocol| devices) connected directly to the |EX-CS|, then you will need Wifi, and will have to budget some setup and learning time.

Compatible Boards
=================

Most boards based on the ESP8266 should work with |EX-CS|. However, with all the variations and software versions out there, we've compiled this list of known tested, working hardware. We will add more over time.


* `Makerfabs ESP8266 WiFi Shield (recommended) <https://www.makerfabs.com/esp8266-wifi-shield.html>`_
* `Duinopeak ESP8266 WiFi Expansion Board (plus an ESP-01 or 01s) <https://usa.banggood.com/Duinopeak-ESP8266-ESP-01-WiFi-Expansion-Board-Shield-Without-ESP8266-Module-p-1391961.html?cur_warehouse=CN>`_
* `ESP-01 or ESP-01S Board (This is not a shield. You will need to use jumpers) <https://www.amzn.com/B00O34AGSU/>`_

Fore more boards you may be able to use, see the :doc:`WiFi Boards Section </reference/hardware/wifi-boards>`

What you will need (for WiFi)
=============================

.. NOTE:: 
   :class: note-float-right
   
   While it may be possible to run WiFi on an Uno, Nano or Pro Mini, it is currently not supported. The Uno simply does not have enough memory to run networking in addition to all the other Command Station features (network code takes about 10kB of progmem and about 2kB of RAM). Also, there is only one hardware serial port. There would be a conflict with the USB port used for logging and connection to software like |JMRI| being shared.

**Either:**

* A |EX-CS| - Command Station (CS) made from a **Mega** and an **Arduino Motor Shield**
* One of the above WiFi boards
* Two (2) Male to Female Jumpers (plus 3 more if you are using an ESP-01 or 01s)

**Or:**

* A |EX-CS| - Command Station (CS) made from a **Mega+WiFi Combo Board**

Supported Boards
================

* :doc:`/reference/hardware/wifi-boards/makerfabs-esp8266`
* :doc:`/reference/hardware/wifi-boards/duinopeak-esp8266`
* :doc:`/reference/hardware/wifi-boards/esp-01`
* :doc:`/reference/hardware/wifi-boards/mega-wifi`


Install the Software
====================

If you already have the Command Station software running and are just adding WiFi, there is nothing further you need to do if you want to use the |EX-CS| as an Access Point (AP) and connect a |WiThrottle Protocol| compatible CAB (|Engine Driver|). The next time you power up the Command Station, it will automatically find your WiFi board and which port it is connected to. See the detailed instructions here: :doc:`WiFi Configuration </ex-commandstation/advanced-setup/supported-wifi/wifi-config>`

.. note:: LOGIN PASSWORD - If you use |Access Point Mode|, you must connect your throttle to the DCCEX network, not your home network. The |Access Point| will be called DCCEX_abcdef and the password will be PASS_abcdef, where "abcdef" is the last 6 characters of the ESP MAC address. Just look at the list of available networks on your phone and you can see this information. It is also shown in the boot log if you connect your Command Station to a computer running a serial monitor. Please click on the "WiFi Configuration" link above for more detailed instruction.

If you are setting up your Command Station for the first time, or are making changes to the basic setup, navigate to :doc:`Command Station Downloads </download/ex-commandstation>` to load firmware onto the Command Station.

.. note:: You may run into an ESP-01s board that has the wrong firmware on it. This is easy to test by connecting it and looking at the startup log for the CS in the serial monitor. If the board does not respond to AT commands, you will need to install new firmware on the ESP board. This is called "flashing". You can find how to do this, as well as some other interesting things in the `Geoff Bunza article on creating a signal only command station. <https://forum.mrhmag.com/post/sma42-socs-signal-only-command-station-for-dcc-wifi-control-direct-to-your-logo-12289064?pid=1332020138_>`_ .Skip to the "The ESP-01S - The Wifi Connection" section
   