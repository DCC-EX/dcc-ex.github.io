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

   The instructions on this page refer to the *new* |EX-I|.  This is currently only supported on Microsoft x64 Windows Computers. |BR| If you have a Microsoft Windows x32, Apple MacOS or Linux based computer use the :doc:`original Installer </ex-installer/installing-original-installer>` instead.

.. sidebar::

   .. contents:: On this page
      :depth: 4
      :local:

Requirements (for installing)
==============================

* a Microsoft Windows x64  **computer**
* |EX-CS| **hardware**, comprising of:

  * an **Arduino microprocessor**, based on any of:
    
    * Arduino Mega, Arduino Uno or Nano
    * Expressif ESP32
    * STMicroelectronicsm Nucleo/STM32

  * a **motor shield**
  * optionally, a **WiFi shield** or ethernet shield
  * optionally, an **LCD or oLED display**
  
* a **USB cable** to connect your computer to the Microcontroller

.. sidebar:: **USB Cable**
   
   Make sure your USB Cable is connected from your computer to the |EX-CS|. Make sure no other programs (like the Arduino IDE) are using the same USB port.

1. Getting Ready 
================

.. warning::
   :class: warning-float-right
   
   **Antivirus Software** |BR| You *may* need to turn off your antivirus software before you try to install. |BR| Sometimes our software gets blocked by antivirus apps. If you see any errors on the install screen, this is usually the issue.

* **Connect** your |EX-CS| **hardware** to your computer via USB.

2. Download and Run EX-Installer 
================================

* Download the **new** :ref:`EX-Installer <download/ex-commandstation:ex-Installer>` app.
* For Microsoft Windows x64:
  
  * Open the Windows *File Manager*
  * Find the folder in which the **EX-Installer-Win64.exe** was saved. |BR| Generally this will default to downloading to the *downloads* folder but your browser may be configured differently.
  * **Run** ``EX-Installer-Win64.exe`` |BR| |BR| Note: depending on the configuration of your computer the '.exe' may or may not appear. This is not of concern.

* You will be presented with the following screen...

|force-break|

a. The 'EX-Installer Welcome' screen
------------------------------------

.. figure:: /_static/images/ex-installer/welcome.png
   :alt: EX-Installer - Welcome
   :scale: 40%
   :align: left

   EX-Installer - Welcome

This screen provides some basic information about the process of loading the Software.

There is *debugging* option on this page. If enabled this provides additional information about what is happening during the loading process. Unless you are having difficulties, or have been requested to enable this by one of our team, you do not need to select this.

To proceed, click the :guilabel:`Manage Arduino CLI` button.

|force-break|

b. 'Manage Arduino CLI' screen
------------------------------

.. figure:: /_static/images/ex-installer/manage_cli.png
   :alt: EX-Installer - Manage CLI
   :scale: 40%
   :align: left

   Manage CLI

This screen allows you to install or update the *Arduino Command Line Interface (CLI)*.

We use the *Arduino Command Line Interface (CLI)* to upload the DCC-EX products to your Arduino.  The CLI eliminates the need to install the more daunting Arduino IDE.  EX-Installer is able to manage the installation and updating of the Arduino CLI for you at the click of a button.

If you have not installed the CLI previously you will see a :guilabel:`Install Arduino CLI` button. 

If have previously installed the CLI you will see a :guilabel:`Refresh Arduino CLI` button.

.. note::
   :class: note-float-right

   Enabling additional platforms is likely to add several minutes to the installation process. Maybe grab a cup of tea or a coffee!

If you are using an Espressif or STMicroelectronics device, as opposed to the more common Uno or Mega based Arduinos, you will need to enable support for these by selecting the appropriate additional platform option.

You *must* have Arduino CLI installed to proceed, simply click the :guilabel:`Install Arduino CLI` button if it is showing.

If you already have the Arduino CLI installed, it is recommended that you refresh it periodically (e.g. weekly) to ensure support for the various device details are kept up to date. To refresh the CLI, simply click the ::guilabel:`Refresh Arduino CLI` button.

Once the CLI is installed, To proceed, click the ::guilabel:`Select your device` button.

|force-break|

c. 'Select Your Device' screen
------------------------------

.. figure:: /_static/images/ex-installer/select_device.png
   :alt: EX-Installer - Select Device
   :scale: 40%
   :align: left

   EX-Installer - Select Device

On this screen you will need to |BR| a) select the type of device you wish to load the |EX-CS| software onto, and |BR| b) the USB port you have connected the device to on your computer.

|EX-I| will attempt to work out both of these for you, but it may need assistance.

Click on the :guilabel:`Scan for Devices` button. 

If you see **No devices found** to means that you either a) have not connected the device to the computer, or b) the device was not recognised by the computer.

If you have not connected the device, connect it now and click the :guilabel:`Scan for Devices` button again.

.. todo::  If the device is not recognised.

.. figure:: /_static/images/ex-installer/select_device_multiple_devices.png
   :alt: EX-Installer - Select Device - Multiple Devices
   :scale: 30%

   Select Device - Multiple Devices

If more than one device is found (on different USB ports), you will need to select which one you wish to load the software on to.

.. figure:: /_static/images/ex-installer/select_device_selection.png
   :alt: EX-Installer - Select Device - Selection
   :scale: 30%

   Select Device - Selection

|EX-I| will attempt to work out what type of Arduino you have connected, but some cases it will not be able to do so. (This is especially common with cheap clone devices.) 

Check and select the appropriate board from the drop down list.

Once you have a port and device type selected, to proceed, click the :guilabel:`Select product to install` button.

|force-break|

d. 'Select the Product to Install' screen
-----------------------------------------

.. figure:: /_static/images/ex-installer/select_product.png
   :alt: EX-Installer - Select EX-CommandStation version
   :scale: 40%
   :align: left

   Select EX-CommandStation version

Currently only the |EX-CS| product can be installed by the |EX-I|.

Click on the |EX-CS| logo to proceed.

|force-break|

e. Product Specific screens
---------------------------

Currently only the installation of the |EX-CS| is supported.

EX-CommandStation
^^^^^^^^^^^^^^^^^

i) 'Select EX-CommandStation Version' screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/images/ex-installer/select_cs_version.png
   :alt: EX-Installer - Select EX-CommandStation version
   :scale: 40%
   :align: left

   Select EX-CommandStation version

On this screen you need to select:

* Which version of the EX-CommandStation software you wish to load
* How you wish to configure the software

*Which version*

Select which version of the |EX-CS| software to load onto your hardware.  If you are unsure, or unless you have been otherwise directed by the support team, we recommend you select ``Latest Production``.

Options are:

* Latest Production - Recommended!
* Latest Development
* Select a specific version

*How to configure*

Select how you wish to configure your |EX-CS|. Unless you are updating a previous version that you manually configured, or want to manually make advanced configuration changes, select ``Configure options on the next screen``

Options are:

* Configure options on the next screen
* Use my existing configuration files

If you select ``Use my existing configuration files`` your will be prompted to find the folder where the configuration files are located.

If you have selected ``Configure options on the next screen``, to proceed, click the :guilabel:`Configure EX-CommandStation` button.

If you have selected ``Use my existing configuration files``, to proceed, click the :guilabel:`Complie and Upload` button.

|force-break|

ii) 'Install EX-CommandStation' - Configuration screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/images/ex-installer/ex_cs_configure.png
   :alt: EX-Installer - EX-CommandStation Configuration
   :scale: 40%
   :align: left

   EX-CommandStation Configuration

Only if you have selected ``Configure options on the next screen`` on the previous screen will you be presented with this screen. 

On this screen you can select some of the flexible and optional features of the |EX-CS|:abbr:

* Motor Driver type
* LCD or oLED display
* Wifi
* Ethernet
* Set track modes
* Advanced Config

|force-break|

**Motor Driver**

.. figure:: /_static/images/ex-installer/ex_cs_configure_motor_shield.png
   :alt: EX-Installer - EX-CommandStation - Configure Motor Driver
   :scale: 70%

   Configure Motor Driver

You *must* select the motor driver type that you have installed.  The installer can't detect this, so you must select the correct board or the |EX-CS| may not work. 

The options include:

* STANDARD_MOTOR_SHIELD
* EX8874_SHIELD
* POLOLU_MOTOR_SHIELD
* FIREBOX_MK1
* FIREBOX_MK1S
* FUNDUMOTO_SHIELD
* IBT_2_WITH_ARDUINO
* YFROBOT_MOTOR_SHIELD
* ORION_UNO_INTEGRATED_SHIELD
* NANOEVERY_EXAMPLE

**Optional Display**

.. figure:: /_static/images/ex-installer/ex_cs_configure_screen.png
   :alt: EX-Installer - EX-CommandStation - Configure Display Driver
   :scale: 70%

   Configure Display Driver

If you have installed and optional oLED or LED display, enable the ``I have a display`` option, which will present you with a drop down list to select the type of display you have.

The options include:

* LCD - 16 columns x 2 rows
* LCD - 16 columns x 4 rows
* OLED 128 x 32
* OLED 128 x 64

**WiFi**

If you have installed and optional WiFi board, or are using a microcontroller board with integrated WiFi, enable the ``I have WiFi`` option, which will present you with additional options.

You can configure the WiFi for EX-CommandStation two ways:

* Access Point mode |BR| Select ``Use my EX-CommandStation as an Access Point`` |BR| You can configure for EX-CommandStation to have its own, completely isolated, WiFi Network. This is referred to as *Access Point Mode*. (Most useful if your layout is away from the house, or you transport your layout frequently.)
* Station mode |BR| Select ``Connect my EX-CommandStation to my existing wireless network`` |BR| The EX-CommandStation can be setup so that it connects to your existing home WiFi Network. This is referred to as *Station Mode*. 

**Use my EX-CommandStation as an Access Point**

.. figure:: /_static/images/ex-installer/ex_cs_configure_wifi_access_point.png
   :alt: EX-Installer - EX-CommandStation - Configure WiFi - Access Point
   :scale: 70%

   Configure WiFi - Access Point

   If ``Use my EX-CommandStation as an Access Point`` is selected, two additional options are presented:

   * WiFi Password
   * WiFi Channel

   *WiFi Password* is optional.  If not entered it will default to "PASS_xxxxx" where 'xxxxx' id will be the same as the SSID that will be automatically configured.

   *WiFi Channel* can be any value from 1-11.  If possible choose a channel that is unused by other networks around your location.

**Connect my EX-CommandStation to my existing wireless network** 

.. figure:: /_static/images/ex-installer/ex_cs_configure_wifi_station.png
   :alt: EX-Installer - EX-CommandStation - Configure Wifi - Station Mode
   :scale: 70%

   Configure Wifi - Station Mode

   If ``Connect my EX-CommandStation to my existing wireless network`` is selected, two additional options are presented:

   * Wifi SSID
   * WiFi Password

   Both are required, Though it is possible, but unlikely, that the WiFi Password for your network is blank.

   *Wifi SSID* is the name of your home network.

   *WiFi Password* is the password for your home network.

**I have Ethernet**   

   If you have installed and Ethernet board, select this option.

   Note that it is not possible to have both WiFi and Ethernet enabled at the same time.

**Set track modes**

.. figure:: /_static/images/ex-installer/ex_cs_configure_set_track_mode_options.png
   :alt: EX-Installer - EX-CommandStation - Configure Wifi - Station Mode
   :scale: 70%

The tracks (channels) on your motor driver can be configured in a variety of different ways.

* MAIN - DCC main
* PROG - DCC Programming Track
* DC
* DCX - DC with the positive/negative inverted
* OFF

By default track (channel) **A** will default to ``MAIN`` and Track (channel) **B** to ``PROG``.

**Advanced Config**

.. figure:: /_static/images/ex-installer/ex_cs_configure_advanced_config.png
   :alt: EX-Installer - EX-CommandStation - Configure Wifi - Station Mode
   :scale: 70%

If you wish to edit the 'config' files directly, select this option.  An additional screen will be presented for to edit the main config files.

Unless you have selected *Advanced Config*, to proceed, click the :guilabel:`Compile and Load` button. See *iv* below.

If you have selected *Advanced Config*, to proceed, click the :guilabel:`Advanced Config` button.  See *iii* below.

|force-break|

iii) 'Advanced Configuration' screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/images/ex-installer/ex_cs_advanced_config.png
   :alt: EX-Installer - EX-CommandStation - Configure Wifi - Station Mode
   :scale: 40%
   :align: left

Only if you have selected ``Advanced Config`` on the previous screen will you be presented with this screen. 

On this screen you can edit the two main configuration files.

To proceed, click the :guilabel:`Compile and Load` button. See *iv* below.

|force-break|

iv) 'Compile and Load' screen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/images/ex-installer/ex_cs_load.png
   :alt: EX-Installer - Load
   :scale: 40%
   :align: left

To proceed, click the :guilabel:`Load` button.

Results are shown in the lower half of the screen.


If there are no errors, you can proceed to testing your setup.

.. todo:: if there are errors

----

.. note:: 

   If you have any difficulties check the :doc:`/support/ex-cs-troubleshooting` page for assistance.

----

Next Steps - Test your setup
============================

.. NOTE:: The programming track is for programming only. Make sure you are on the main track if you expect your loco to move or respond to light or sound commands.