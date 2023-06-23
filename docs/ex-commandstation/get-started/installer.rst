.. include:: /include/include-ex-cs.rst
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
      :depth: 4
      :local:
    
This page is specifically intended for a |conductor-text| who has installed *just* the recommended hardware (including WiFi). If you are a |tinkerer-text| or |engineer-text| or have installed some of the additional, or different, hardware from that recommended for a |conductor-text| then we suggest that you look at the :doc:`/ex-installer/index` page for the full instructions.

----

Once you have assembled your |EX-CS| hardware you need to load our software onto it make is usable. |br| To make it as simple as possible we have created the |EX-I| app.

|force-break|

Requirements (for installing)
=============================

.. sidebar:: **USB Cable**
   
   Make sure your USB Cable is connected from your computer to the |EX-CS|. Make sure no other programs (like the Arduino IDE) are using the same USB port.

* a Windows, Linux or MacOS X **Computer**
* an |EX-CS| (Arduino Mega/Uno + Motor shield and optional WiFi shield)
* a **USB cable** to connect your computer to the Microcontroller

.. note:: 

   The new |EX-I| is currently only supported on Microsoft Windows x64 computers.
   If you have a Microsoft Windows x32, Apple MacOS or Linux based computer you will need use the old installer for now.

1. Getting Ready 
================

**Instruction for Windows, Mac OS X, and Linux (including the Raspberry Pi)**

.. warning::
   :class: warning-float-right
   
   **Antivirus Software** |BR| You *may* need to turn off your antivirus software before you try to install. |BR| Sometimes our software gets blocked by antivirus apps. If you see any errors on the install screen, this is usually the issue.

* **Connect** your |EX-CS| to your computer
* Determine which COM Port the |EX-CS| is plugged into 

  * This step is not required for the new EX-Installer (on Microsoft Windows x64 computers).

  * for Microsoft x32 Windows (using the original installer):

    * open (run) the 'Device Manager' app and look at the 'Ports (COM & LPT)' as you plug or unplug the |EX-CS|
    * take note of the COM number (in brackets after the name of the device)

  * for Mac OS or Linux:
  
    * open a terminal screen and run the command ``ls /dev/tty.usbmodem*``
    * this should result in displaying a device name such as ``/dev/tty.usbmodem12033``
    * if multiple devices are listed, you may need to unplug your |EX-CS|, re-run the command to see which device is left, then plug it in again to note the difference

2. Download and Run EX-Installer 
================================

.. warning::
   
   Note that currently there are two versions of the EX-Installer. |BR| The *new* version currently is only supported on **Microsoft x64 Windows Computers**. 
   If you have a Microsoft Windows x32, Apple MacOS or Linux based computer use the *original* Installer.

* Download the correct :ref:`EX-Installer <download/ex-commandstation:ex-Installer>` app |BR| depending on your computer's operating system.


* For **Microsoft Windows x64**:

  * Open the Windows *File Manager*
  * Find the folder in which the **EX-Installer-Win64.exe** was saved. |BR| Generally this will default to downloading to the *downloads* folder but your browser may be configured differently.
  * **Run** ``EX-Installer-Win64.exe`` |BR| |BR| Note: depending on the configuration of your computer the '.exe' may or may not appear. This is not of concern. |BR| |BR|
  * You will be presented with the following screens...

* for **Microsoft Windows x32**:

  * Extract the downloaded **Installer** into its own folder with your favourite unzip program.
  * Open *File Manager*
  * **Run** ``exInstaller.exe`` |BR| |BR|

* For **Mac OS or Linux**:

  * Open a terminal window and navigate to that folder.
  * **Run the installer with** the following command: ``./exInstaller`` |BR| |BR|

* You will be presented with the following screen...

----

3a. For Microsoft Windows x64 computers
=======================================

The 'EX-Installer Welcome' screen
---------------------------------

.. figure:: /_static/images/ex-installer/welcome.png
   :alt: EX-Installer - Welcome
   :scale: 40%
   :align: left

This screen provides some basic information about the process of loading the Software.

If you are using the recommended Mega hardware, you should not need to adjust the other setting on this page.

To proceed, click the :guilabel:`Manage Arduino CLI` button.

|force-break|

'Manage Arduino CLI' screen
---------------------------

.. figure:: /_static/images/ex-installer/manage_cli.png
   :alt: EX-Installer - Manage CLI
   :scale: 40%
   :align: left

This screen allows you to install or update the *Arduino Command Line Interface (CLI)*.

We use the *Arduino Command Line Interface (CLI)* to upload the DCC-EX products to your Arduino.

If you have not installed the CLI previously you *must* have Arduino CLI installed to proceed, simply click the :guilabel:`Install Arduino CLI` button if it is showing.

If you already have the Arduino CLI installed, it is recommended that you refresh it periodically (e.g. weekly) to ensure support for the various device details are kept up to date. To refresh the CLI, simply click the ::guilabel:`Refresh Arduino CLI` button.

If you are using the recommended Mega hardware, you should not need to adjust the other settings on this page.

Once the CLI is installed, To proceed, click the ::guilabel:`Select your device` button.

|force-break|

'Select Your Device' screen
---------------------------

.. figure:: /_static/images/ex-installer/select_device.png
   :alt: EX-Installer - Select Device
   :scale: 40%
   :align: left

On this screen you will need to |BR| a) select the type of device you wish to load the |EX-CS| software onto, and |BR| b) the USB port you have connected the device to on your computer.

|EX-I| will attempt to work out both of these for you, but it may need assistance.

Click on the :guilabel:`Scan for Devices` button. 

If you see **No devices found** to means that you either a) have not connected the device to the computer, or b) the device was not recognised by the computer.

If you have not connected the device, connect it now and click the :guilabel:`Scan for Devices` button again.

.. todo::  If the device is not recognised.

.. figure:: /_static/images/ex-installer/select_device_multiple_devices.png
   :alt: EX-Installer - Select Device - Multiple Devices
   :scale: 30%

If more than one device is found (on different USB ports), you will need to select which one you wish to load the software on to.

.. figure:: /_static/images/ex-installer/select_device_selection.png
   :alt: EX-Installer - Select Device - Selection
   :scale: 30%

|EX-I| will attempt to work out what type of Arduino you have connected, but some cases it will not be able to do so. (This is especially common with cheap clone devices.) 

Check and select the appropriate board from the drop down list.

Once you have a port and device type selected, to proceed, click the :guilabel:`Select product to install` button.

|force-break|

'Select the Product to Install' screen
--------------------------------------

.. figure:: /_static/images/ex-installer/select_product.png
   :alt: EX-Installer - Select Product
   :scale: 40%
   :align: left

Currently only the |EX-CS| product can be installed by the |EX-I|.

Click on the |EX-CS| logo to proceed.

|force-break|

'Select EX-CommandStation Version' screen
-----------------------------------------

.. figure:: /_static/images/ex-installer/select_cs_version.png
   :alt: EX-Installer - Select EX-CommandStation version
   :scale: 40%
   :align: left

On this screen you need to select:

* Which version of the EX-CommandStation software you wish to load
* How you wish to configure the software

*Which version*

Select which version of the |EX-CS| software to load onto your hardware.  If you are unsure, or unless you have been otherwise directed by the support team, we recommend you select ``Latest Production``.

*How to configure*

Select how you wish to configure your |EX-CS|. Unless you are updating a previous version that you manually configured, or want to manually make advanced configuration changes, select ``Configure options on the next screen``

If you do want to manually make advanced configuration changes, see the :doc:`/ex-installer/installing` page for instructions on how to enable them.

If you have selected ``Configure options on the next screen``, to proceed, click the :guilabel:`Configure EX-CommandStation` button.

|force-break|

'Install EX-CommandStation' - Configuration screen
--------------------------------------------------

.. figure:: /_static/images/ex-installer/ex_cs_configure.png
   :alt: EX-Installer - EX-CommandStation Configuration
   :scale: 40%
   :align: left

On this screen you can select some of the flexible and optional features of the |EX-CS|:abbr:

* Motor Driver type
* LCD or oLED display
* Wifi
* Ethernet

Only the Motor Driver and WiFi will be covered here.  If you have installed different hardware to that recommended, see the :doc:`/ex-installer/installing` page for instructions.

|force-break|

**Motor Driver**

.. figure:: /_static/images/ex-installer/ex_cs_configure_motor_shield.png
   :alt: EX-Installer - EX-CommandStation - Configure Motor Driver
   :scale: 30%

You *must* select the motor driver type that you have installed.  The installer can't detect this, so you must select the correct board or the |EX-CS| may not work. If you have installed the recommended Motor Driver, select `STANDARD_MOTOR_SHIELD`.

**WiFi**

If you have installed and optional WiFi board, or are using a microcontroller board with integrated WiFi, enable the ``I have WiFi`` option, which will present you with additional options.

You can configure the WiFi for EX-CommandStation two ways:

* Access Point mode |BR| Select ``Use my EX-CommandStation as an Access Point`` |BR| You can configure for EX-CommandStation to have its own, completely isolated, WiFi Network. This is referred to as *Access Point Mode*. (Most useful if your layout is away from the house, or you transport your layout frequently.)
* Station mode |BR| Select ``Connect my EX-CommandStation to my existing wireless network`` |BR| The EX-CommandStation can be setup so that it connects to your existing home WiFi Network. This is referred to as *Station Mode*. 

.. figure:: /_static/images/ex-installer/ex_cs_configure_wifi_access_point.png
   :alt: EX-Installer - EX-CommandStation - Configure WiFi Access Point
   :scale: 30%

   **Use my EX-CommandStation as an Access Point**

   If ``Use my EX-CommandStation as an Access Point`` is selected, two additional options are presented:

   * WiFi Password
   * WiFi Channel

   *WiFi Password* is optional.  If not entered it will default to "PASS_xxxxx" where 'xxxxx' id will be the same as the SSID that will be automatically configured.

   *WiFi Channel* can be any value from 1-11.  If possible choose a channel that is unused by other networks around your location.

.. figure:: /_static/images/ex-installer/ex_cs_configure_wifi_station.png
   :alt: EX-Installer - EX-CommandStation - Configure Wifi - Station Mode
   :scale: 30%

   **Connect my EX-CommandStation to my existing wireless network** 

   If ``Connect my EX-CommandStation to my existing wireless network`` is selected, two additional options are presented:

   * Wifi SSID
   * WiFi Password

   Both are required, Though it is possible, but unlikely, that the WiFi Password for your network is blank.

   *Wifi SSID* is the name of your home network.

   *WiFi Password* is the password for your home network.

To proceed, click the :guilabel:`Compile and Load` button.

|force-break|

'Compile and Load' screen
-------------------------

.. figure:: /_static/images/ex-installer/ex_cs_load.png
   :alt: EX-Installer - Load
   :scale: 40%
   :align: left

To proceed, click the :guilabel:`Load` button.

Results are shown in the lower half of the screen.


If there are no errors, you can proceed to testing your setup.


|force-break|

----

3b. For Windows x32, Apple MacOS or Linux computers
===================================================

The EX-Installer Window
-----------------------

.. warning:: **Wait!**
   :class: warning-float-right-narrow
   
   The |EX-I| takes a little while to load everything it needs, so wait till you have seen about a dozen lines of text appear in the right pane before you try to select anything in the drop down menus.

.. figure:: /_static/images/installer/installer.jpg
   :alt: EX-Installer
   :scale: 75%

   Installer Window

There will be a lot of information appearing in the log window, which can help us debug things if anything goes wrong. The installer needs to connect online to download the latest packages to support your hardware. It will take a few seconds to complete; this is normal. If you have a very slow internet connection it will take longer.

Choose your options
^^^^^^^^^^^^^^^^^^^

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~

WiFi Checkbox
'''''''''''''

Check the ``WiFi`` box.  That's it, there is nothing more to do here.

   .. figure:: /_static/images/installer/wifi.jpg
      :alt: WiFi Options
      :scale: 90%

      Wifi Options

Even if you didn't install a WiFi shield, we recommend that this box be checked. If left checked and later you add a WiFi Shield, you won't have to upload the sketch again. The WiFi check only takes a few seconds, after which it will report no WiFi was found and start the Command Station.  (If you aren't using WiFi and want to save a few seconds of boot time, you can uncheck the box.)

|force-break|

.. note::
   :class: note-float-right 

   If you have any difficulties check the :doc:`/support/ex-cs-troubleshooting` page for assistance.

Compile and Upload
^^^^^^^^^^^^^^^^^^

**Compile and Upload Button**

Once you have configured your options, press this button to upload the software to your |EX-CS|.

----

Next Steps - Selecting a Throttle (Controller) 
==============================================

Click :doc:`here <controllers>` or click the "next" button to learn how to select a throttle (controller) suitable to test and use your |EX-CS|.

----

.. todo:: `LOW - need to update installer screenshots <https://github.com/DCC-EX/dcc-ex.github.io/issues/417>`_
