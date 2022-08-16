.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|
   
****************
Advanced Options
****************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

These pages describe the major supported hardware options for building a |EX-CS|, along with some guidance for some of the unsupported options. They are primarily targeted at |tinkerer-text| and |engineer-text| level.  However there are some options that are suitable for a |conductor-text|.  If however, you identify as a |conductor-text| and only wish to install the recommended hardware we suggest that you look at the simplified :doc:`/ex-commandstation/get-started/index` page.


Steps to Build an EX-CommandStation
===================================

#. Choose a `Microcontroller <Microcontrollers>`_
#. Choose a `Motor Driver <Motor Drivers>`_
#. Choose a `Connection Method <Connection Options>`_ and if required choose a:

  #. WiFi board,
  #. Ethernet board,
  #. Bluetooth board, 
  #. Or none of the above (Direct Connection)

#. Choose a `LCD/oLED screen <LED/oLED Screens>`_ (if desired)
#. Choose a `Controller (throttle) <Controller Options>`_
#. Choose an `installation method <Installation options>`_
#. Set your `startup options <Startup Configuration>`_ (if required)
#. `Install the software <Installation options>`_
#. Run your trains

----

Microcontrollers
================

There are several different supported microcontrollers you can use as your |EX-CS| as per the following list.

The Arduino Mega2560 is by far the simplest option and is well proven with many users choosing this option.

Whilst the Uno and Nano options are fairly popular and also relatively simple, there are limitations due to the lack of available RAM available, and therefore some features (such as WiFi and EX-RAIL) are limited.

The other item of specific note is the Mega2560 + WiFi which, while appearing a good alternative to a standard Mega2560, suffers from quality control issues, and numerous users have had poor experiences getting this to function correctly. While this option is supported, it is definitely *buyer beware!*

.. note:: 

  Our developers are always experimenting with new microcontrollers and hardware platforms, so while a specific option may not be explicitly listed on here, it may be on our roadmap or under active development. Feel free to :doc:`/support/contact-us` to see if something that's taken your eye is on the agenda.

.. toctree::
    :maxdepth: 2
    
    supported-microcontrollers/index


Motor Drivers
=============

As with microcontrollers, there is a selection of supported motor drivers to choose from. For those who desire simplicity, stick with the recommended Arduino and Deek-Robot motor shields.

However, if you need more current than these can provide, then you need to consider the IBT_2 or IRF3205 options.

.. toctree::
    :maxdepth: 2
    
    supported-motorboards/index

Connection Options
==================

How you connect to your |EX-CS| is going to depend entirely on your personal choices of how you wish to interact with it. Are you a JMRI user? Do you only want to use wireless hand-held throttles?

To faciliate a variety of these choices, there are four ways to connect: direct via USB, WiFi, Ethernet, and/or Bluetooth.

Depending on your platform choice for your |EX-CS|, the connectivity options aren't mutually exclusive, and you can use multiple methods.

Direct Connection (USB)
-----------------------

If you are a JMRI user, then a direct USB connection is all you need. JMRI will connect to your |EX-CS| via the USB port, and you won't require any other connection method to be available.

Note for Uno and Nano users, this is your only option for connectivity.

WiFi Shields
------------

.. toctree::
    :maxdepth: 2
    
    supported-connections/index
    supported-wifi/index

Ethernet Boards
---------------

.. toctree::
    :maxdepth: 2
    
    supported-ethernet/index

Bluetooth Boards
----------------

.. toctree::
    :maxdepth: 1
    
    supported-bluetooth/index

LED/oLED Screens
================

refer to :doc:`/reference/hardware/i2c-displays`

Installation options
====================

.. todo:: URGENT description needed for Installation options

.. toctree::
    :maxdepth: 2
    
    installation-options/index


Startup Configuration
=====================

.. todo:: URGENT description needed for Startup Configuration

.. toctree::
    :maxdepth: 1
    
    startup-config

Controller Options
==================
Choosing a Controller (Throttle) - Advanced

.. toctree::
    :maxdepth: 2
    
    controllers

