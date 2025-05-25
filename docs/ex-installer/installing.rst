.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-i.rst
.. meta::
   :keywords: EX-Installer

|EX-I-LOGO|

***********************************
Dowloading and Running EX-Installer
***********************************

|SUITABLE| |conductor| |tinkerer| |support-button| |githublink-ex-installer-button-small|

|force-break|

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On this page
      :depth: 2
      :local:

If you are assembling a DIY |EX-CS|, |EX-IO|, or |EX-TT| device, you need to load our software onto it to make it usable. To make this process as simple as possible we have created |EX-I|.

If you have purchased an |EX-CSB1| it will have come with the |EX-CS| software already installed.  You only need to look at this page if you want to change the default configuration or upgrade to a newer version.

.. warning::

   We have found that there are a small number of users who can have an issue when trying to update firmware or upload EXRAIL scripts to an EX-CSB1 Command Station (or any ESP32 based device).

   If you are having problems, look at our `uploading troubleshooting guide <https://dcc-ex.com/news/posts/20250128.html>`_.

|force-break|

----

**Instructions for Windows, macOS, and Linux**

Requirements (for installing)
==============================

To run |EX-I| you need:

* A Microsoft Windows, Apple macOS, or Linux based computer
* Your |EX-CSB1-SHORT|, |EX-CS|, |EX-IO|, or |EX-TT| device
* A USB cable to connect your computer to the Microcontroller - **NOTE** this must be a **DATA** cable, not a charging only cable.

Download and Install EX-Installer
=================================

As of |EX-I| version 0.0.21, Windows users will need to run an install process for |EX-I| rather than just downloading the executable file. This should prevent the majority of antivirus software programs quarantining it. Linux and macOS users can continue to just download and run it as normal at this stage.

.. warning:: 
  
   **Antivirus Software** |BR| You *may* need to turn off your antivirus software before you try to install. |BR| Sometimes our software gets blocked by antivirus apps. If you see any errors on the install screen, this is usually the issue.

* If you haven't done so already, download |EX-I|:

.. rst-class:: dcclink

   :doc:`Download EX-Installer </download/ex-installer>`

* For Linux and macOS users, skip to :ref:`ex-installer/installing:getting ready`
* Windows users must continue to install |EX-I| with the steps below.
* Note when downloading on Windows, you may note that *Windows Defender* issues a warning in the browser that this file is not commonly downloaded:

   .. image:: /_static/images/ex-installer/not-commonly-downloaded-warning.png
      :alt: File not commonly downloaded warning
      :scale: 55%

* To ensure the file is downloaded successfully, click the ``...`` three dots beside the trash icon and select ``Keep``:

   .. image:: /_static/images/ex-installer/not-commonly-downloaded-keep.png
      :alt: File not commonly downloaded - Keep
      :scale: 55%

* You will then be prompted with another warning, cick the down arrow beside ``Show more`` and select ``Keep anyway``:

   .. image:: /_static/images/ex-installer/not-commonly-downloaded-keep-anyway.png
      :alt: File not commonly downloaded - Keep Anyway
      :scale: 55%

* Now that |EX-I| has been downloaded, open *Windows Explorer*
* Find the folder in which the **EX-Installer-Win64.exe** was saved and run it (Note the '.exe' may or may not appear)
* You will be prompted to all changes to be made to your computer, click ``Yes``

   .. image:: /_static/images/ex-installer/ex-installer-setup-allow-changes.png
      :alt: EX-Installer - Allow Changes
      :scale: 55%

* Next you must agree to the license agreement, scroll down to read and if you accept, select ``I accept the agreement`` then click ``Next``

   .. figure:: /_static/images/ex-installer/ex-installer-setup-license.png
      :alt: EX-Installer - Accept License Agreement
      :scale: 55%

* If you wish to install to a different location to default, you can specify that now, otherwise just click ``Next``

   .. figure:: /_static/images/ex-installer/ex-installer-setup-destination.png
      :alt: EX-Installer - Select Destination
      :scale: 55%

* By default, a new start menu folder called "DCC-EX" will be created and you may change that here, or just click ``Next``

   .. figure:: /_static/images/ex-installer/ex-installer-setup-start-menu.png
      :alt: EX-Installer - Select Start Menu Folder
      :scale: 55%

* By default, a shortcut will be created to |EX-I| on your desktop, and you can deselect that here or just click ``Next``

   .. figure:: /_static/images/ex-installer/ex-installer-setup-shortcut.png
      :alt: EX-Installer - Select Additional Tasks
      :scale: 55%

* A confirmation screen outlines the installation is ready, click ``Next`` and |EX-I| will commence installing

   .. figure:: /_static/images/ex-installer/ex-installer-setup-ready.png
      :alt: EX-Installer - Ready to Install
      :scale: 55%

   .. figure:: /_static/images/ex-installer/ex-installer-setup-install.png
      :alt: EX-Installer - Installing
      :scale: 55%

* When complete, |EX-I| will be launched by default, or you can deslect this option, and click ``Finish``

   .. figure:: /_static/images/ex-installer/ex-installer-setup-finish.png
      :alt: EX-Installer - Completing Setup
      :scale: 55%

* |EX-I| is now installed and ready to be used continue with the :ref:`ex-installer/temp:getting ready` section

|force-break|

----

Getting Ready
=============

.. warning:: 
  
   Close all other programs that might be using the USB port.  (Like the |Arduino IDE|, |EX-WT| or |JMRI|.)

To begin with, connect your |EX-CSB1-SHORT|, DIY |EX-CS|, |EX-IO|, or |EX-TT| device to your computer via a **DATA** USB cable.

.. note:: 

   If you already have, or wish to create, your own custom config files, we recommend that you :doc:`read this page first <managing-config-files>`.

.. important:: 
   
   EX-Installer creates a folder (<home>\\ex-installer) to hold the information it needs. :dcc-ex-red-bold:`Do not directly modify anything in this folder` as anything you modify will be overwritten or deleted, and will cause the installer to fail to load.

----

Run EX-Installer 
================

* For **Microsoft Windows**:
  
  * Click ``Start`` and select ``EX-Installer`` from the ``DCC-EX`` folder, or double click the ``EX-Installer`` icon on your desktop
  
* For **Apple macOS**:

  * Open a terminal window and navigate to the that folder that you downloaded the file to.  e.g.: |BR| ``cd Downloads``
  * Enter the following command to tell the OS that it is an executable: |BR| ``chmod +x EX-Installer-macOS``
  * **Run the installer with** the following command: |BR| ``./EX-Installer-macOS`` |BR| |BR|

* For **Linux**:

  * Right-click on the file, go to Properties, then the Permissions tab, and check "Allow executing file as program"
  * Open a terminal window and navigate to that folder
  * **Run the installer with** the following command: |BR| ``./EX-Installer-Linux64`` |BR| |BR|

----

**You will be presented with the following screen...**

a. The 'EX-Installer Welcome' screen
------------------------------------

.. figure:: /_static/images/ex-installer/welcome.png
   :alt: EX-Installer - Welcome
   :scale: 40%
   :align: left

   EX-Installer - Welcome screen

This screen provides some basic information about the process of loading the Software.

To proceed, click the :guilabel:`Manage Arduino CLI` button.

|force-break|

|HR-DASHED|

b. 'Manage Arduino CLI' screen
------------------------------

.. important:: 

   You must enable **Expressif ESP32** support if you are using an |EX-CSB1-SHORT|

.. figure:: /_static/images/ex-installer/manage_cli.png
   :alt: EX-Installer - Manage CLI
   :scale: 40%
   :align: left

   EX-Installer - Manage CLI screen

This screen allows you to install or update the *Arduino Command Line Interface (CLI)*.

If you have not installed the CLI previously you will see a :guilabel:`Install Arduino CLI` button. 

If have previously installed the CLI you will see a :guilabel:`Refresh Arduino CLI` button.

If you are using an Espressif or STMicroelectronics device (including the |EX-CSB1-SHORT|, as opposed to the more common Uno or Mega based Arduinos, you will need to enable support for these by selecting the appropriate additional platform option after the CLI has been installed.

You *must* have Arduino CLI installed to proceed, simply click the :guilabel:`Install Arduino CLI` button if it is showing.

If you already have the Arduino CLI installed, it is recommended that you refresh it periodically (e.g. weekly) to ensure support for the various device details are kept up to date. To refresh the CLI, simply click the :guilabel:`Refresh Arduino CLI` button.

Installing the CLI can take some time.  Maybe grab a cup of tea or a coffee!

Once the CLI is installed, click the :guilabel:`Select your device` button. 

|force-break|

|HR-DASHED|

c. 'Select Your Device' screen
------------------------------

.. figure:: /_static/images/ex-installer/select_device.png
   :alt: EX-Installer - Select Device
   :scale: 40%
   :align: left

   EX-Installer - Device screen

On this screen you will need to select the type of device you have and the USB port you have connected the device to on your computer.

|EX-I| will attempt to work out both of these for you, but it may need assistance.

When navigating to this page, a scan for devices will start automatically.

If you see **No devices found** it means that either the device is not connected, or the device was not recognised by the computer.

|force-break|

No Devices Found
~~~~~~~~~~~~~~~~

If you have not connected the device, connect it now then click the :guilabel:`Scan for Devices` button again.

If the device *is* connected but not found refer to the :doc:`/support/ex-cs-diagnose` page for assistance.

Multiple Devices Found
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/images/ex-installer/select_device_multiple_devices.png
   :alt: EX-Installer - Select Device - Multiple Devices
   :scale: 50%
   :align: center

   EX-Installer - Device - Multiple Devices

If more than one device is found (on different USB ports), you will need to select which one you wish to load the software on to.

.. figure:: /_static/images/ex-installer/select_device_selection.png
   :alt: EX-Installer - Select Device - Selection
   :scale: 50%
   :align: center

   EX-Installer - Device - Selection

.. hint:: 
   :class: hint-float-right-narrow

   For the |EX-CSB1-SHORT| select '**DCC-EX EX-CSB1**'

|EX-I| will attempt to work out what type of Arduino you have connected, but in some cases it will not be able to do so. (This is especially common with cheap clone devices.) 

Check and select the appropriate board from the drop down list.

Once you have a port and device type selected click the :guilabel:`Select product to install` button.

|force-break|

|HR-DASHED|

d. 'Select the Product to Install' screen
-----------------------------------------

.. figure:: /_static/images/ex-installer/select_product.png
   :alt: EX-Installer - Select Product
   :scale: 40%
   :align: left

   EX-Installer - Product Screen

Currently, |EX-CS|, |EX-IO|, and |EX-TT| can be installed by the |EX-I|, and to continue installing the appropriate product:

* For |EX-CSB1-SHORT| users, refer to the ready-to-run :doc:`/ex-commandstation/installer-rtr` page
* For DIY |EX-CS| users, refer to the do-it-yourself :doc:`/ex-commandstation/installer-diy` page
* For |EX-IO|, refer to :ref:`ex-ioexpander/overview:install ex-ioexpander with ex-installer`
* For |EX-TT| refer to :ref:`ex-turntable/assembly:install ex-turntable with ex-installer`

|force-break|
