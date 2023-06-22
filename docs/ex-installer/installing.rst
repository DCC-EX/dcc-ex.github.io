.. meta::
   :keywords: EX-CommandStation Command Station EX-Installer

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-I-LOGO|

*********************************
Using the Installer (Windows x64) 
*********************************

|tinkerer| |engineer| |githublink-ex-installer-button2|

.. warning::

   The instructions on this page refer to the new |EX-I|.  This is currently only supported on Microsoft x64 Windows Computers. |BR| If you have a Microsoft Windows x32, Apple MacOS or Linux based computer use the :doc:`original Installer </ex-installer/installing-original-installer>` instead.


.. sidebar::

   .. contents:: On this page
      :depth: 3
      :local:


Requirements (for installing)
==============================

* a Microsoft Windows x64  **computer**
* |EX-CS| hardware, comprising of:

  * an Arduino microprocessor, based on any of:
    
    * Arduino Mega, Arduino Uno or Nano
    * Expressif ESP32
    * STMicroelectronicsm Nucleo/STM32

  * a motor shield
  * optionally, a WiFi shield or ethernet shield
  * optionally, an LCD or oLED display
  
* a **USB cable** to connect your computer to the Microcontroller

.. sidebar:: **USB Cable**
   
   Make sure your USB Cable is connected from your computer to the |EX-CS|. Make sure no other programs (like the Arduino IDE) are using the same USB port.

1. Getting Ready 
================

**For Windows x64**

.. warning::
   :class: warning-float-right
   
   **Antivirus Software** |BR| You *may* need to turn off your antivirus software before you try to install. |BR| Sometimes our software gets blocked by antivirus apps. If you see any errors on the install screen, this is usually the issue.

* **Connect** your |EX-CS| to your computer

2. Download and Run EX-Installer 
================================

* Download the new :ref:`EX-Installer <download/ex-commandstation:ex-Installer>` app.
* For Microsoft Windows x64:
  
  * Open the Windows *File Manager*
  * Find the folder in which the **EX-Installer-Win64.exe** was saved. |BR| Generally this will default to downloading to the *downloads* folder but your browser may be configured differently.
  * **Run** ``EX-Installer-Win64.exe`` |BR| |BR| Note: depending on the configuration of your computer the '.exe' may or may not appear. This is not of concern.

* You will be presented with the following screen...

|force-break|

a. The EX-Installer Welcome screen
----------------------------------

.. figure:: /_static/images/ex-installer/welcome.png
   :alt: EX-Installer - Welcome
   :scale: 40%
   :align: left

This screen provides some basic information about the process.

It also provides a debugging option. If enabled this provides additional information about what is happening during the loading process. Unless you are having difficulties, or have been requested to enable this by one of our team, you do not need to select this.

To proceed, click the ::guilabel:`Manage Arduino CLI` button.

|force-break|

b. Manage CLI screen
--------------------

.. figure:: /_static/images/ex-installer/manage_cli.png
   :alt: EX-Installer - Manage CLI
   :scale: 40%
   :align: left

This screen allows you to Install or update the Arduino Command Line Interface (CLI).

We use the Arduino Command Line Interface (CLI) to upload the DCC-EX products to your Arduino.  The CLI eliminates the need to install the more daunting Arduino IDE.  EX-Installer is able to manage the installation and updating of the Arduino CLI for you at the click of a button.

If you have not installed the CLi previously you will see a ::guilabel:`Install Arduino CLI` button. 

If have previously installed the CLI you will see a ::guilabel:`Refresh Arduino CLI` button.

.. note::
   :class: note-float-right

   Enabling additional platforms is likely to add several minutes to the installation process. Maybe grab a cup of tea or a coffee!

If you are using an Espressif or STMicroelectronics device, as opposed to the more common Uno or Mega based Arduinos, you will need to enable support for these by selecting the appropriate additional platform option.

You must have Arduino CLI installed to proceed, simply click the ::guilabel:`Install Arduino CLI` button if it is showing.

If you already have the Arduino CLI installed, it is recommended to refresh it periodically (e.g. weekly) to ensure support for the various devices is kept up to date. To refresh the CLI, simply click the ::guilabel:`Refresh Arduino CLI` button.

Once the CLI is installed, To proceed, click the ::guilabel:`Select your device` button.

|force-break|

c. Select Your Device screen
----------------------------

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

If more than one device (on different USB ports) is found, you will need to select which one you wish to work with.

.. figure:: /_static/images/ex-installer/select_device_selection.png
   :alt: EX-Installer - Select Device - Selection
   :scale: 30%

|EX-I| will attempt to work out what type of Arduino you have connect but some cases (especially with cheap clone devices) it will not be able to do so.

Check and select the appropriate board from the drop down list.

Once you have a port and device type selected, to proceed, click the :guilabel:`Select product to install` button.

|force-break|

d. Select the Product to Install screen
---------------------------------------

.. figure:: /_static/images/ex-installer/select_product.png
   :alt: EX-Installer - Select Product
   :scale: 40%
   :align: left

Currently only the |EX-CS| product can be installed by the |EX-I|.

Click on the |EX-CS| logo to proceed.

|force-break|

e. Product Specific screens
---------------------------

Currently only the installation of the |EX-CS| is supported.

EX-CommandStation
^^^^^^^^^^^^^^^^^

i) Select EX-CommandStation Version screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/images/ex-installer/select_cs_version.png
   :alt: EX-Installer - Select EX-CommandStation version
   :scale: 40%
   :align: left

*Which version*

* Latest Production - Recommended!
* Latest Development
* Select a specific version

*How to configure*

* Configure options on the next screen
* Use my existing configuration files


Once you have selected version and chose how to configure, To proceed, click the :guilabel:`xxx` button.

|force-break|

ii) Install EX-CommandStation - Configuration screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. figure:: /_static/images/ex-installer/ex_cs_configure.png
   :alt: EX-Installer - EX-CommandStation Configuration
   :scale: 40%
   :align: left

stuff goes here

|force-break|

.. figure:: /_static/images/ex-installer/ex_cs_configure_motor_shield.png
   :alt: EX-Installer - EX-CommandStation - Configure Motor Driver
   :scale: 30%

Select your motor driver

.. figure:: /_static/images/ex-installer/ex_cs_configure_screen.png
   :alt: EX-Installer - EX-CommandStation - Configure Display Driver
   :scale: 30%

I have a display


I have WiFi

.. figure:: /_static/images/ex-installer/ex_cs_configure_wifi_access_point.png
   :alt: EX-Installer - EX-CommandStation - Configure WiFi Access Point
   :scale: 30%

Use my EX-CommandStation as an Access Point

  Select WiFi Channel

.. figure:: /_static/images/ex-installer/ex_cs_configure_wifi_station.png
   :alt: EX-Installer - EX-CommandStation - Configure Wifi - Station Mode
   :scale: 30%

Connect my EX-CommandStation to my existing wireless network

   Wifi SSID
   WiFi Password
   


To proceed, click the :guilabel:`Complie and Load` button.

|force-break|

iii) Compile and Load screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/images/ex-installer/ex_cs_load.png
   :alt: EX-Installer - Load
   :scale: 40%
   :align: left

To proceed, click the :guilabel:`Load` button.

Results are in the lower half of the screen


If there are no errors, you can proceed to testing you setup.

.. todo:: if there are errors


----

.. note:: 

   If you have any difficulties check the :doc:`/support/ex-cs-troubleshooting` page for assistance.

----

Next Steps - Test your setup
============================

.. NOTE:: The programming track is for programming only. Make sure you are on the main track if you expect your loco to move or respond to light or sound commands.