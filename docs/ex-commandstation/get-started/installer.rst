.. include:: /include/include.rst
**************************************
Install using the Automated Installer
**************************************

Requirements (for installing)
==============================

* Windows/Linux/macOS Computer
* DCC-EX Compatible motor shield / motor controller board
* DCC-EX Compatible Microcontroller (Arduino Mega/Uno)
* USB cable to connect your computer to the Microcontroller

.. note:: For all versions, make sure your USB Cable is connected from your computer to the Command Station (CS). Make sure no other programs are using the computer's serial port.

Instructions for Windows, Mac OS X, and Linux (including the Raspberry Pi
============================================================================

* Download the :ref:`DCC-EX Installer <download/ex-commandstation:exInstaller>` which will automatically determine the version you need and download it
* Extract the Installer into its own folder with your favorite unzip program
* Open File Manager for Windows or a terminal window in Mac OS and Linux and navigate to that folder
* Windows users run ``exInstaller.exe``
* Mac and Linux users run the following command: ``./exInstaller``


.. warning::
   You may need to turn off your antivirus software before you try to install. We need a piece of Arduino software to be able to compile and upload the Command Station software which sometimes gets blocked. If you see errors on the install screen, this is usually the issue.

The Installer Window
=====================

.. figure:: /_static/images/installer/installer.jpg
   :alt: DCC-EX Installer
   :scale: 75%

   Installer Window

There will be a lot of information appearing in the log window, which can help us debug things if anything goes wrong. The installer needs to connect online to download the latest packages to support your hardware. It will take a few seconds to complete; this is normal. If you have a very slow internet connection it will take longer.

Choose your options
====================

In the left side options pane, use the dropdown selector boxes to choose the following options:

.. figure:: /_static/images/installer/inst_options.jpg
   :alt: Options Pane
   :scale: 75%

   Options Pane

1. Select your Command Station Type
2. Select your Arduino Board Type
3. Select your Motor Shield
4. Select your COM Port (The installer should usually find it for you)
5. Check the checkbox for your networking method if you have a Network Shield or WiFi Shield installed
6. Check the checkbox for your display type if using an LCD or OLED display
7. Check the Free Mem warning if you need to diagnose memory issues
8. Press the "Compile and Upload" button

WiFi Checkbox
--------------

MAKE SURE THIS BOX IS CHECKED - If you want WiFi, this box **must** be checked. If you don't want WiFi, you can leave it checked anyway so that if you add WiFi later, you won't have to upload the sketch again. The WiFi check only takes a few seconds, after which it will report no WiFi was found and start the Command Station. If you aren't using WiFi and want to save a few seconds of boot time, you can uncheck the box. If you need extra memory on the Arduino and aren't going to use WiFi, unchecking the box will free about 10kb of progmem and about 2kb of RAM.

If you have installed a WiFi board, DCC++ EX will scan all the serial ports on your Mega and find it. If you wish to use Access Point Mode (aka AP Mode), this will set up the CS to be its own network router. To use it, you connect your phone or other WiFi device to this network instead of your home network. You will see a new network when you use the connect option on your phone that looks like "DCC-EX-xxxxxx", where the "xxxxxx" are the last 6 characters of the MAC address of your WiFi board. Simply connect to that network and you have a direct connection to your CS.

If you wish to connect to your home network instead (connect to your router using "Station Mode"), then check this box. You will then need to enter your credentials to login to your network just like you would from any of your other WiFi devices:


.. figure:: /_static/images/installer/wifi.jpg
   :alt: WiFi Options
   :scale: 90%

   Wifi Options

* **WiFi SSID** - The name of your home network.\ 

* **WiFi Password** - The password required to connect to your home network.\ 

* **Host Name** - If your WiFi Board supports it, this name can be used in addition to the IP address.\ 

* **Server Port** - This is the communication port our internal WiThrottle server uses to communicate with devices like Engine Driver. We recommend leaving it set to 2560 because JMRI also uses that port should you ever want to use JMRI.\ 

* **IP Address** - Normally, the DHCP server for your network will assign an IP address and you should leave this blank. But if you want to assign an IP address so the CS always uses the same one, you can enter it here.\ 

Ethernet Checkbox
------------------

If you have an Ethernet shield and check this box, you will see options to change the following settings:

.. figure:: /_static/images/installer/ethernet.jpg
   :alt: Ethernet Options
   :scale: 90%

   Ethernet Options

* **Host Name** - If your Ethernet Board supports it, this name can be used in addition to the IP address.\ 

* **Server Port** - This is the communication port our internal WiThrottle server uses to communicate with devices like Engine Driver. We recommend leaving it set to 2560 because JMRI also uses that port should you ever want to use JMRI.\ 

* **MAC Address** - This is the unique identifier for your Ethernet Shield. We recommend leaving this setting as is. If you ever have more than one Ethernet shield on your network and there is a conflict, you can change this setting.

* **IP Address** - Normally, the DHCP server for your network will assign an IP address and you should leave this blank. But if you want to assign an IP address so the CS always uses the same one, you can enter it here.\ 

LCD Checkbox
-------------

If you have a 2 or 4 line LCD display connected and check this box, you will see the following options you can edit for your display:

.. figure:: /_static/images/installer/lcd.jpg
   :alt: LCD Options
   :scale: 90%

   LCD Options

* **LCD Address (in Decimal format)** - This is the address of your display, it is usually 39 (for 0x27) or 63 (for 0x3F)

* **LCD Columns** - The number of vertical columns on your display

* **LCD Rows** - The number of horizontal rows or lines on your display

For more information about using displays, see :doc:`I2C Displays </reference/hardware/i2c-displays>`

OLED CheckBox
---------------

If you have an OLED display connected and check this box, you will see the following options you can edit for your display:

.. figure:: /_static/images/installer/oled.jpg
   :alt: OLED Options
   :scale: 90%

   OLED Options

* **OLED Width (in pixels)** - Enter the width or number of horizontal pixels on your display

* **OLED Height (in pixels)** - Enter the height or number of vertical pixels on your display

For more information about using displays, see :doc:`I2C Displays </reference/hardware/i2c-displays>`

Refresh Ports Button
----------------------

This button allows you to refresh the serial ports in case you didn't have the Arduino connected when you opened the program, or if you will be programming multiple Arduinos. When you plug in a new board, refresh the ports so it can find your device.

Compile and Upload Button
--------------------------

Once you have configured your options, press this button to compile all the source code and upload it to your Command Station.

Test your setup
=================

.. NOTE:: The programming track is for programming only. Make sure you are on the main track if you expect your loco to move or respond to light or sound commands.

Using the Arduino IDE Serial Monitor
-------------------------------------

To test with the Arduino Serial Monitor, download the Arduino IDE from the following link and install it on your computer.

`Download the Arduino IDE <https://www.arduino.cc/en/Main/software>`_

To do a quick test, open the Arduino application:

.. figure:: /_static/images/installer/arduino_ide.jpg
   :alt: Arduino IDE
   :scale: 100%

   The Arduino IDE

* Select "Tools -> Serial Monitor" from the Arduino IDE menu


.. figure:: /_static/images/installer/arduino_ide2.jpg
   :alt: Open the Serial Monitor
   :scale: 100%

   Open the Serial Monitor from the Tools Menu

You will see the following screen:


.. figure:: /_static/images/installer/serial_monitor.jpg
   :alt: Serial Monitor
   :scale: 100%

   Serial Monitor


* Select "115200" as the baud rate in the dropdown in the lower right
* Select "Both NL & CR" from the dropdown next to the baud rate

When you open the serial monitor you will see at least one line sent out as status information. If you have a WiFi board or Ethernet Shield you will see a page full of log information as it configures and connects to your network.

At the top of the serial monitor type ``<s>`` (lowercase "s") into the command textbox and press "Send". You should see:

.. code-block::

   <iDCC-EX V-0.2.1 / MEGA / STANDARD_MOTOR_SHIELD G-9db6d36>

This is the "status" command and reports your version, types of boards you are using, and a build number.

There are a lot of other commands you can enter here. As a matter of fact, you could use the serial monitor to test any of the DCC-EX API (application programming interface) commands. Please see the `DCC++ EX Wiki <https://github.com/DCC-EX/CommandStation-EX/wiki>`_ for a list of commands.

Using WebThrottle-EX
--------------------

.. figure:: /_static/images/installer/exwebthrottle.jpg
   :alt: WebThrottle-EX
   :scale: 100%

   WebThrottle-EX

Click this link: :doc:`WebThrottle-EX </throttles/ex-webthrottle>` to run WebThrottle-EX hosted on our site, or visit `GitHub <https://github.com/DCC-EX/WebThrottle-EX>`_ to get the latest version to run on your computer.

Using Engine Driver (or other WiThrottle Cab) - Requires WiFi
--------------------------------------------------------------

.. figure:: /_static/images/installer/engine_driver.png
   :alt: Engine Driver
   :scale: 100%

   Engine Driver

You will need to install Engine Driver on your mobile device and then connect to the CS, either directly with AP mode or through your router with Station Mode. You can then use your phone to control your trains.
