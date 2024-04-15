.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst

|EX-CS-LOGO|
   
****************
Advanced Options
****************

|tinkerer| |engineer| |support-button| |githublink-ex-commandstation-button2|

.. sidebar::

  .. contents:: On this page
      :depth: 1
      :local:

These pages describe the major supported hardware options for building a |EX-CS|, along with some guidance for some of the unsupported options. They are primarily targeted at |tinkerer-text| and |engineer-text| level.  However there are some options that are suitable for a |conductor-text|.  If however, you identify as a |conductor-text| and only wish to install the recommended hardware we suggest that you look at the simplified :doc:`/ex-commandstation/get-started/index` page.


Steps to Build an EX-CommandStation
===================================

1. Choose a `Microcontroller <#microcontrollers>`_
2. Choose a `Motor Driver <#motor-drivers>`_
3. Choose a `Connection Method <#connection-options>`_ and if required choose a:

  a. WiFi board,
  b. Ethernet board,
  c. Bluetooth board, 
  d. Or none of the above (Direct Connection)

4. Choose a `LCD/oLED screen <#lcd-oled-screens>`_ (if desired)
5. Choose an `installation method <#installation-options>`_
6. Set your `startup options <#startup-configuration>`_ (if required)
7. `Install the software <#installation-options>`_
8. Choose a `Throttle (Controller) <#throttle-controller-options>`_
9. Run your trains

----

Microcontrollers
=================

There are several different supported microcontrollers you can use as your |EX-CS| as per the following list.

The Arduino Mega2560 is by far the simplest option and is well proven with many users choosing this option.

Whilst the Uno and Nano options are fairly popular and also relatively simple, there are limitations due to the lack of available RAM available, and therefore some features (such as WiFi and EX-RAIL) are limited.

The other item of specific note is the Mega2560 + WiFi which, while appearing a good alternative to a standard Mega2560, suffers from quality control issues, and numerous users have had poor experiences getting this to function correctly. While this option is supported, it is definitely *buyer beware!*

.. toctree::
  :maxdepth: 2
  
  /reference/hardware/microcontroller-boards


Motor Drivers
=============

As with microcontrollers, there is a selection of supported motor drivers to choose from. For those who desire simplicity, stick with the recommended Arduino and Deek-Robot motor shields.

However, if you need more current than these can provide, then you need to consider the IBT_2 or IRF3205 options.

.. toctree::
  :maxdepth: 2
  
  /reference/hardware/motor-boards

Connection Options
==================

How you connect to your |EX-CS| is going to depend entirely on your personal choices of how you wish to interact with it. Are you a JMRI user? Do you only want to use wireless hand-held throttles?

To facilitate a variety of these choices, there are four ways to connect: direct via USB, WiFi, Ethernet, and/or Bluetooth.

Depending on your platform choice for your |EX-CS|, the connectivity options aren't mutually exclusive, and you can use multiple methods.

Direct Connection (USB)
-----------------------

If you are a JMRI user, then a direct USB connection is all you need. JMRI will connect to your |EX-CS| via the USB port, and you won't require any other connection method to be available.

Note for Uno and Nano users, this is your only option for connectivity as mentioned in :ref:`ex-commandstation/advanced-setup/index:microcontrollers`.

If you are using a physical throttle that requires a serial connection, then this is also the appropriate connection option, although your throttle will connect to the Arduino onboard serial interface rather than the USB port most likely.

WiFi
----

To be able to connect directly to your |EX-CS| from a |wiThrottle| app or |Engine Driver|, you will need a network connection to connect to.

A WiFi connection can provide this network connection, either in |Access Point Mode| or in |Station Mode|.

To use WiFi, you will need something other than an Uno or Nano with a connected WiFi shield or board. Follow the links below to understand the supported options.

.. toctree::
  :maxdepth: 2
  
  supported-connections/index
  supported-wifi/index

Ethernet
--------

If you prefer a physical network connection, you will need an Ethernet shield or board to provide a network connection for |wiThrottle| apps or |Engine Driver| to connect to.

.. toctree::
  :maxdepth: 2
  
  supported-ethernet/index

Bluetooth
---------

.. toctree::
  :maxdepth: 1
  
  /reference/hardware/bluetooth

LCD/OLED Screens
================

If you wish to have some sort of display connected to your |EX-CS|, there are various supported options for both LCD or OLED displays depending on your preference.

These can display various items such as the version, IP address (if using WiFi or Ethernet), as well as some user configurable parameters.

refer to :doc:`/reference/hardware/i2c-displays`

Installation options
====================

Depending on your comfort level with using different software and computers in general, there are two options for installing the |EX-CS| software, both of which should be within the reach of |conductor-text| level users.

The simplest option, requiring only a simple download, is to use |EX-I|. There are limitations on what options you can select using this method, so if you are using any options that require configuration beyond what's prompted for during the install process, you will need to use the Arduino IDE instead.

The Arduino IDE requires some software to be installed on your computer, however due to the flexibility this provides can be a better alternative than |EX-I|.

.. toctree::
  :maxdepth: 2
  
  installation-options/index


Startup Configuration
=====================

In general, modifying the startup configuration should not be required.

However, there are occasions when the startup configuration does need modification to ensure any changed parameters persist after the |EX-CS| is shutdown or restarted. These changes are usually as a result of a conversation with the developers.

.. toctree::
  :maxdepth: 1
  
  startup-config

Throttle (Controller) Options
=============================

If you wish to take your |EX-CS| experience further, then there are various different controller options available including commercial and DIY throttles as well as an API if you want to design and build your own controller.

These tend to be aimed more at the |tinkerer-text| and |engineer-text| levels.

.. toctree::
  :maxdepth: 2
  
  controllers


DCC-EX Commands
===============

.. toctree::
  :maxdepth: 1

  Native Commands Summary </reference/software/command-summary-consolidated>

Features under development
==========================

|NOT-IN-PROD-VERSION|
  
We always have new features under development for |EX-CS| and |EX-R|, and as these features get incorporated into the development branch of the software, we will endeavour to keep these documented in our development pages.

Remember that these features will continue to change and evolve as bugs are found and fixed, and better ways of doing things are discovered, so it's best to keep up to date with any discussions via our `Discord server <https://discord.gg/PuPnNMp8Qf>`_.

Refer to :doc:`/under-development/index` for more information.