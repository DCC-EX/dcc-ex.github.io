.. meta::
   :keywords: EX-CommandStation Command Station EX-Installer

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-I-LOGO|

*******************
Using the Installer 
*******************

|tinkerer| |engineer| |githublink-ex-installer-button2|

.. warning:: 

  Please be advised that our installer currently does not work reliably on Linux or macOS which is a known issue.

  For Linux users we recommend using the Arduino IDE. You can find instructions on the :doc:`/ex-commandstation/advanced-setup/installation-options/arduino-ide` page.

  We hope to have a new version available soon.

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:

Requirements (for installing)
==============================

* a Windows, Linux or MacOS X **Computer**
* a |EX-CS|

  * Arduino Mega or Arduino Uno 
  * Motor shield
  * optional WiFi shield or ethernet shield
  * optional LCD or oLED display
  
* a **USB cable** to connect your computer to the Microcontroller

.. sidebar:: **USB Cable**
   
   Make sure your USB Cable is connected from your computer to the |EX-CS|. Make sure no other programs (like the Arduino IDE) are using the same USB port.

1. Getting Ready 
================

**(for Windows, Mac OS X, and Linux (including the Raspberry Pi))**

.. warning::
   :class: warning-float-right
   
   **Antivirus Software** |BR| You *may* need to turn off your antivirus software before you try to install. |BR| Sometimes our software gets blocked by antivirus apps. If you see any errors on the install screen, this is usually the issue.

* **Connect** your |EX-CS| to your computer
* Determine which COM Port the |EX-CS| is plugged into 

  * for Microsoft Windows:

    * open (run) the 'Device Manager' app and look at the 'Ports (COM & LPT)' as you plug or unplug the |EX-CS|
    * take note of the COM number (in brackets after the name of the device)

  * for Mac OS or Linux:
  
    * Open a command terminal and run the command ``ls /dev/tty.usbmodem*``
    * The device will have a name such as ``/dev/tty.usbmodem12033``
    * if there are more than one devices listed, unplug |EX-CS|, re-run the command to note the device that remains, then plug |EX-CS| back in again to obtain the correct device name
    * For Linux you *will* need add yourself to the dialout group to gain permissions access to the serial devices. The easiest way is to run the command ``sudo adduser yourusername dialout`` with your Linux username inserted

2. Download and Run EX-Installer 
================================

* Download the :ref:`EX-Installer <download/ex-commandstation:ex-Installer>` app |BR| depending on your computer's operating system it will automatically determine the version you need and download it
* Extract the downloaded **Installer** into its own folder with your favorite unzip program |BR| |BR|
* For Microsoft Windows:
  
  * Open File Manager
  * **Run** ``exInstaller.exe`` |BR| |BR|

* For Mac OS or Linux:

  * Open a terminal window and navigate to that folder
  * **Run the installer with** the following command: ``./exInstaller`` |BR| |BR|

* You will be presented with the following screen...

3. The EX-Installer Window
==========================

.. warning:: **Wait!**
   :class: warning-float-right
   
   The |EX-I| takes a little while to load everything it needs, so wait till you have seen about a dozen lines of text appear in the right pane before you try to select anything in the drop down menus.

.. figure:: /_static/images/installer/installer.png
   :alt: EX-Installer
   :scale: 30%

   Installer Window

There will be a lot of information appearing in the log window, which can help us debug things if anything goes wrong. The installer needs to connect online to download the latest packages to support your hardware. It will take a few seconds to complete; this is normal. If you have a very slow internet connection it will take longer.

Choose your options
-------------------


In the left side options pane, use the dropdown selector boxes to choose the following options:

.. figure:: /_static/images/installer/installer-options.png
   :alt: Options Pane
   :scale: 60%

   Options Pane

.. sidebar:: 

   |BSC| is now only in a maintenance support state only.  If you are still using it, we recommend that you move to |EX-CS|.  It will function on the same hardware a |BSC|.

1. Select your **Command Station Type** |BR| This should (almost always) be **'Command Station EX'**
2. Select your **Arduino Board Type**
3. Select your **Motor Shield** |BR|
4. Select your **COM Port** |BR| The installer will usually find it for you but check against the COM port your took note of earlier
5. Check the checkbox for your networking method if you have a Network Shield or WiFi Shield installed
6. Check the checkbox for your display type if using an LCD or OLED display
7. Check the Free Mem warning if you need to diagnose memory issues
8. Press the :guilabel:`Compile and Upload` button

WiFi Checkbox
^^^^^^^^^^^^^

MAKE SURE THIS BOX IS CHECKED - If you want WiFi, this box **must** be checked. If you don't want WiFi, you can leave it checked anyway so that if you add WiFi later, you won't have to upload the sketch again. The WiFi check only takes a few seconds, after which it will report no WiFi was found and start the Command Station. If you aren't using WiFi and want to save a few seconds of boot time, you can uncheck the box. If you need extra memory on the Arduino and aren't going to use WiFi, unchecking the box will free about 10kb of progmem and about 2kb of RAM.

If you have installed a WiFi board, |EX-CS| will scan all the serial ports on your Mega and find it. If you wish to use Access Point Mode (aka AP Mode), this will set up the Command Station to be its own network router. To use it, you connect your phone or other WiFi device to this network instead of your home network. You will see a new network when you use the connect option on your phone that looks like "DCC-EX-xxxxxx", where the "xxxxxx" are the last 6 characters of the MAC address of your WiFi board. Simply connect to that network and you have a direct connection to your CS.

If you wish to connect to your home network instead (connect to your router using "Station Mode"), then check this box. You will then need to enter your credentials to login to your network just like you would from any of your other WiFi devices:


.. figure:: /_static/images/installer/wifi.png
   :alt: WiFi Options
   :scale: 30%

   Wifi Options

* **WiFi SSID** - The name of your home network.\ 

* **WiFi Password** - The password required to connect to your home network.\ 

* **Host Name** - If your WiFi Board supports it, this name can be used in addition to the IP address.\ 

* **Server Port** - This is the communication port our internal |WiThrottle server| uses to communicate with devices like |Engine Driver|. We recommend leaving it set to 2560 because |JMRI| also uses that port should you ever want to use |JMRI|.\ 

* **IP Address** - Normally, the DHCP server for your network will assign an IP address and you should leave this blank. But if you want to assign an IP address so the Command Station always uses the same one, you can enter it here.\ 

Ethernet Checkbox
^^^^^^^^^^^^^^^^^

If you have an Ethernet shield and check this box, you will see options to change the following settings:

.. figure:: /_static/images/installer/ethernet.jpg
   :alt: Ethernet Options
   :scale: 90%

   Ethernet Options

* **Host Name** - If your Ethernet Board supports it, this name can be used in addition to the IP address.\ 

* **Server Port** - This is the communication port our internal |WiThrottle server| uses to communicate with devices like |Engine Driver|. We recommend leaving it set to 2560 because JMRI also uses that port should you ever want to use |JMRI|.\ 

* **MAC Address** - This is the unique identifier for your Ethernet Shield. We recommend leaving this setting as is. If you ever have more than one Ethernet shield on your network and there is a conflict, you can change this setting.

* **IP Address** - Normally, the DHCP server for your network will assign an IP address and you should leave this blank. But if you want to assign an IP address so the Command Station always uses the same one, you can enter it here.\ 

LCD Checkbox
^^^^^^^^^^^^

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
^^^^^^^^^^^^^

If you have an OLED display connected and check this box, you will see the following options you can edit for your display:

.. figure:: /_static/images/installer/oled.jpg
   :alt: OLED Options
   :scale: 90%

   OLED Options

* **OLED Width (in pixels)** - Enter the width or number of horizontal pixels on your display

* **OLED Height (in pixels)** - Enter the height or number of vertical pixels on your display

For more information about using displays, see :doc:`I2C Displays </reference/hardware/i2c-displays>`

Refresh Ports Button
^^^^^^^^^^^^^^^^^^^^

This button allows you to refresh the serial ports in case you didn't have the Arduino connected when you opened the program, or if you will be programming multiple Arduinos. When you plug in a new board, refresh the ports so it can find your device.

Compile and Upload
------------------

:guilabel:`Compile and Upload` **Button**

Once you have configured your options, press this button to compile all the source code and upload it to your Command Station.

.. note:: 

   If you have any difficulties check the :doc:`/support/ex-cs-troubleshooting` page for assistance.

----

Next Steps - Test your setup
============================

.. NOTE:: The programming track is for programming only. Make sure you are on the main track if you expect your loco to move or respond to light or sound commands.