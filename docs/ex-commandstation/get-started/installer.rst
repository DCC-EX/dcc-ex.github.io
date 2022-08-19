.. meta::
   :keywords: EX-CommandStation Command Station EX-Installer

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

********************
Install the Software
********************

|conductor|

.. sidebar::

  .. contents:: On this page
    :depth: 3
    :local:
    
This page is specifically intended for a |conductor-text| who has installed *just* the recommended hardware (including WiFi). If you are a |tinkerer-text| or |engineer-text| or have installed some of the additional, or different, hardware from that recommended for a |conductor-text| then we suggest that you look at the :doc:`/ex-installer/index` page for the full instructions.

----

Once you have assembled your |EX-CS| hardware you need to load our software onto it make is usable. |br| To make it as simple as possible we have created the |EX-I| app.

Requirements (for installing)
=============================

.. sidebar:: **USB Cable**
   
   Make sure your USB Cable is connected from your computer to the |EX-CS|. Make sure no other programs (like the Arduino IDE) are using the same USB port.

* a Windows, Linux or MacOS X **Computer**
* a |EX-CS| (Arduino Mega/Uno + Motor shield and optional WiFi shield)
* a **USB cable** to connect your computer to the Microcontroller

1. Getting Ready 
================

**Instruction for Windows, Mac OS X, and Linux (including the Raspberry Pi)**

.. warning::
   :class: warning-float-right
   
   **Antivirus Software** |BR| You *may* need to turn off your antivirus software before you try to install. |BR| Sometimes our software gets blocked by antivirus apps. If you see any errors on the install screen, this is usually the issue.

* **Connect** your |EX-CS| to your computer
* Determine which COM Port the |EX-CS| is plugged into 

  * for Microsoft Windows:

    * open (run) the 'Device Manager' app and look at the 'Ports (COM & LPT)' as you plug or unplug the |EX-CS|
    * take note of the COM number (in brackets after the name of the device)

  * for Mac OS or Linux:
  
    * open a terminal screen and run the command ``ls /dev/tty.usbmodem*``
    * this should result in displaying a device name such as ``/dev/tty.usbmodem12033``
    * if multiple devices are listed, you may need to unplug your |EX-CS|, re-run the command to see which device is left, then plug it in again to note the difference

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

1. The EX-Installer Window
==========================

.. warning:: **Wait!**
   :class: warning-float-right-narrow
   
   The |EX-I| takes a little while to load everything it needs, so wait till you have seen about a dozen lines of text appear in the right pane before you try to select anything in the drop down menus.

.. figure:: /_static/images/installer/installer.jpg
   :alt: EX-Installer
   :scale: 75%

   Installer Window

There will be a lot of information appearing in the log window, which can help us debug things if anything goes wrong. The installer needs to connect online to download the latest packages to support your hardware. It will take a few seconds to complete; this is normal. If you have a very slow internet connection it will take longer.

Choose your options
-------------------

In the left side options pane, use the dropdown selector boxes to choose the following options:

.. figure:: /_static/images/installer/inst_options.jpg
   :alt: Options Pane
   :scale: 75%

   Options Pane

.. sidebar:: Refresh Ports Button
   
   The :guilabel:`Refresh Ports` button allows you to refresh the serial ports in case you didn't have the Arduino connected when you opened the program. When you plug in a new board, refresh the ports so it can find your device.

1. Select your **Command Station (Base Station) Type** |BR| If you are |conductor-text| following our recommended instructions, choose ``Command Station EX`` |br| |br|
2. Select your **Arduino Board Type** |BR| If you are |conductor-text| following our recommended instructions, choose ``Mega`` |br| |br|
3. Select your **Motor Shield** |BR| If you are |conductor-text| following our recommended instructions, choose ``Arduino Motor Shield`` |br| |br|
4. Select your **COM Port** |BR| The installer will usually find it for you but check against the COM port your took not of earlier |br| |br|
5. If you have installed an optional a **WiFi Shield** you MUST check the **WiFi box** |br| If you are a |conductor-text| following our recommended instructions, check this box regardless (see below) |br| |br|
6. Press the :guilabel:`Compile and Upload` button

Station Mode VS Access Point Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The instructions on this page are specifically for setting up your |EX-CS| to have its own, completely isolated, WiFi Network. This is referred to as |Access Point Mode|.  (Most useful if your layout is away from the house, or you transport your layout frequently.)

The |EX-CS| can be setup so that it connects to your existing home WiFi Network.  This is referred to as |Station Mode|. See the sidebar on this page or the :doc:`/ex-installer/index` page for the full instructions if you are interested in this option.

.. sidebar:: Station Mode (Alternate)

   |conductor| |BR| This alternate WiFi configuration will make your |EX-CS| connect to your existing home WiFi Network. 

   1. Check the ``WiFi`` box. 
   
   2. Enter your Home WiFi Network Details

      * **WiFi SSID** - The name of your home network.\ 

      * **WiFi Password** - The password required to connect to your home network.\ 

      * **Host Name** - If your WiFi Board supports it, this name can be used in addition to the IP address.\ 

      * **Server Port** - This is the communication port our internal |WiThrottle server| uses to communicate with devices like |Engine Driver|. We recommend leaving it set to 2560.\ 

      * **IP Address** - Normally, the DHCP server for your network will assign an IP address and you should leave this blank. But if you want to assign an IP address so the Command Station always uses the same one, you can enter it here.


Access Point Mode
^^^^^^^^^^^^^^^^^

WiFi Checkbox
~~~~~~~~~~~~~

Check the ``WiFi`` box.  That's it, there is nothing more to do here.

   .. figure:: /_static/images/installer/wifi.jpg
      :alt: WiFi Options
      :scale: 90%

      Wifi Options

Even if you didn't install a WiFi shield, we recommend that this box be checked. If left checked and later you add a WiFi Shield, you won't have to upload the sketch again. The WiFi check only takes a few seconds, after which it will report no WiFi was found and start the Command Station.  (If you aren't using WiFi and want to save a few seconds of boot time, you can uncheck the box.)

|force-break|

.. note::
   :class: note-float-right 

   If you have any difficulties check the :doc:`diagnosing-issues` page for assistance.

Compile and Upload
------------------

**Compile and Upload Button**

Once you have configured your options, press this button to upload the software to your |EX-CS|.

----

Next Steps - Selecting a Controller 
===================================

Click :doc:`here <controllers>` or click the "next" button to learn how to select a controller suitable to test and use your |EX-CS|.

----

.. todo:: LOW - need to update installer screenshots
