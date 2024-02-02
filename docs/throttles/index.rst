.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-throttles.rst
|EX-THROTTLES-LOGO|

***********************
Throttles (Controllers)
***********************

This page contains lists of compatible Throttles (Controllers) that currently support the |EX-CS|.  They are listed two ways:

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:


* :ref:`By Client Technology <throttles/index:throttles - by client technology>`  (e.g. Android, iOS, Web Browser, PC)
* :ref:`By Communication Technology <throttles/index:throttles - by communication technology>` (e.g. |DCC-EX Native Commands|, wiThrottle Protocol)

|conductor|

For an more introductory overview of throttles and how to choose one, please read the :doc:`Getting Started - Throttles Page </ex-commandstation/get-started/controllers>` 

|tinkerer| |engineer|

For additional options for throttles and how to choose one, please read the :doc:`Advanced Options - Throttles Page </ex-commandstation/advanced-setup/controllers>`

----

Throttles - By Client Technology
================================

Web Browser (Windows, OSX, Linux)
---------------------------------

- :doc:`EX-Web-Throttle (Web Browser) </ex-webthrottle/index>`

Android (Phones and Tablets)
----------------------------

- :doc:`Engine Driver (Android)<software/engine-driver>`
- :doc:`DCCpp CAB (android) <software/dccpp-cab>`
- :doc:`Cab Engineer: DCC Throttle (Andriod) <software/cab-engineer>`
- :doc:`DigiTrainsPro (Android) <software/digitrainspro>` *- Requires JMRI*
- :doc:`RtDtive DCC++ (Android) <software/rtdrive-dccpp>`

Apple iOS (Phones and Tablets)
------------------------------

- :doc:`Locontrol (iOS) <software/locontrol>` *- Requires JMRI*
- :doc:`WiThrottle (iOS)<software/withrottle>`
- :doc:`SRCP Client (iOS) <software/srcpclient>`
- :doc:`Train Driver (iOS) <software/train-driver>`

Dedicated Hardware
------------------

- :doc:`miniThrottle (Physical) <hardware/minithrottle>`
- :doc:`miniThrottle (Physical) <hardware/minithrottle>`
- :doc:`WiTcontroller (Physical) <hardware/witcontroller>`
- :doc:`TCS UWT-50 (Physical) <hardware/uwt50>`
- :doc:`Elgato Stream Deck (Physical) <hardware/streamdeck>`
- :doc:`DCC-EX Native command library - DCCEXProtocol </throttles/native-protocol-library>`

Personal Computers
------------------

- :doc:`EX-WebThrottle </ex-webthrottle/index>`
- :doc:`JMRI (Windows, iOS, Linux) <software/jmri>`

----

Throttles - By Communication technology
=======================================

|EX-CS| can use a number of different technologies to communicate with a throttle. While each technology has advantages and disadvantages, none is substantially better that the others.

General
-------

- :doc:`WiThrottle Server, Web Server, DCC-EX Native Commands Explained <protocols>`
- :doc:`connect_wifi_throttle_via_usb`

DCC-EX (DCC-EX Native Commands)
-------------------------------

- :doc:`EX-WebThrottle </ex-webthrottle/index>`
- :doc:`Engine Driver (Android)<software/engine-driver>`
- :doc:`SRCP Client (iOS) <software/srcpclient>`
- :doc:`miniThrottle (Physical) <hardware/minithrottle>`
- :doc:`JMRI <software/jmri>`
- :doc:`RtDtive DCC++ (Android) <software/rtdrive-dccpp>`
- :doc:`DCCpp CAB (Android) <software/dccpp-cab>`
- :doc:` DCC-EX Native command library - DCCEXProtocol <throttles/native-protocol-library>`

wiThrottle Protocol Based Throttles
-----------------------------------

- :doc:`Engine Driver (Android)<software/engine-driver>`
- :doc:`Cab Engineer: DCC Throttle (Andriod) <software/cab-engineer>`
- :doc:`WiThrottle (iOS)<software/withrottle>`
- :doc:`SRCP Client (iOS) <software/srcpclient>`
- :doc:`Train Driver (iOS) <software/train-driver>`
- :doc:`miniThrottle (Physical) <hardware/minithrottle>`
- :doc:`WiTcontroller (Physical) <hardware/witcontroller>`
- :doc:`TCS UWT-50 (Physical) <hardware/uwt50>`
- :doc:`Elgato Stream Deck (Physical) <hardware/streamdeck>`

USB Based Throttles
-------------------------------

- :doc:`EX-WebThrottle </ex-webthrottle/index>`
- Also see: :doc:`connect_wifi_throttle_via_usb`

JMRI Web Server Based Throttles
-------------------------------

- :doc:`Locontrol (iOS) <software/locontrol>`
- :doc:`DigiTrainsPro (Android) <software/digitrainspro>`

----

Table - Throttles by Technology and Feature 
===========================================

.. list-table::
    :widths: auto
    :header-rows: 3
    :class: command-table

    * -  Name
      -  Licence
      -  Interface
      -  Tech- |BR| nology
      -  
      -  Also |BR| Requires
      -  Form |BR| Factor
      -  
      -  
      -  
      -  
      -  
      -  CV Pro- |BR| gramming

    * -  
      -  
      -  
      -  
      -  
      -  
      -  Mobile
      -  
      -  
      -  PC
      -  
      -  
      -  

    * -  
      -  
      -  
      -  Protocol
      -  UI
      -  
      -  Physical |BR| Device
      -  Android
      -  iOS
      -  Win
      -  MacOS
      -  Linux
      -  

    * -  JMRI
      -  Free
      -  USB / Net
      -  Native
      -  Web
      -  
      -  
      -  Web
      -  Web
      -  X
      -  X
      -  X
      -  X

    * -  Railroad Automation
      -  
      -  Net / LocoNet
      -  LocoNet
      -  Web
      -  IoTT Red hat
      -  
      -  Web
      -  Web
      -  X
      -  X
      -  X
      -  

    * -  EX-WebThrottle
      -  Free
      -  USB
      -  Native / WiT
      -  Web
      -  
      -  
      -  
      -  
      -  X
      -  X
      -  X
      -  X

    * -  Engine Driver
      -  Free
      -  Net
      -  Native
      -  App
      -  
      -  
      -  X
      -  
      -  
      -  
      -  
      -  X (native only)

    * -  DCCpp CAB
      -  
      -  Net
      -  Native
      -  App
      -  
      -  
      -  X
      -  
      -  
      -  
      -  
      -  

    * -  Cab Engineer: DCC Throttle
      -  
      -  Net
      -  WiT
      -  App
      -  
      -  
      -  X
      -  
      -  
      -  
      -  
      -  

    * -  RtDrive DCC++
      -  
      -  Net
      -  Native
      -  App
      -  
      -  
      -  X
      -  
      -  
      -  
      -  
      -  

    * -  DigiTrainsPro
      -  Free / Paid
      -  Net
      -  JMRI Web
      -  App
      -  JMRI
      -  
      -  X
      -  X
      -  X
      -  
      -  
      -  

    * -  Locontrol
      -  
      -  Net
      -  JMRI Web
      -  App
      -  JMRI
      -  
      -  
      -  X
      -  
      -  
      -  
      -  

    * -  WiThrottle
      -  Free / Paid
      -  Net
      -  WiT
      -  App
      -  
      -  
      -  
      -  X
      -  
      -  
      -  
      -  

    * -  SRCP Client
      -  
      -  Net
      -  Native
      -  App
      -  
      -  
      -  
      -  X
      -  
      -  
      -  
      -  

    * -  Train Driver
      -  
      -  Net
      -  Native
      -  App
      -  
      -  
      -  
      -  X
      -  
      -  
      -  
      -  

    * -  Train Throttle
      -  
      -  Net
      -  WiT
      -  App
      -  
      -  
      -  
      -  
      -  X
      -  
      -  
      -  

    * -  miniThrottle
      -  
      -  Net / USB
      -  Native
      -  Device
      -  
      -  X
      -  
      -  
      -  
      -  
      -  
      -  

    * -  WiTController
      -  Free
      -  Net
      -  WiT
      -  Device
      -  
      -  X
      -  
      -  
      -  
      -  
      -  
      -  

    * -  DccExController
      -  Free
      -  Net
      -  Native
      -  Device
      -  
      -  X
      -  
      -  
      -  
      -  
      -  
      -  

    * -  TCS UWT Throttle
      -  Paid
      -  Net
      -  WiT
      -  Device
      -  
      -  X
      -  
      -  
      -  
      -  
      -  
      -  

    * -  Elgato Stream Deck
      -  Paid
      -  Net
      -  native
      -  Device
      -  PC or Rpi
      -  X
      -  
      -  
      -  
      -  
      -  
      -  

    * -  LocoNet-Compatible Throttles
      -  Free / Paid
      -  Net
      -  LocoNet
      -  Device
      -  IoTT Red hat
      -  X
      -  
      -  
      -  
      -  
      -  
      -  


**Legend**

  Net = Wifi or LAN networks

  Free / paid = Both Free and Paid versions are available. The free version may be limited in features. |BR| |BR|
  Native = Uses the Native DCC-EX command / command protocols |BR| |BR|
  WiT = Uses the WiThrottle command protocol |BR| |BR|
  Web = Requires the use of a Web Browser |BR| |BR|
  Win = Windows 7 and above

----

Reference
=========

- :doc:`Technical Reference for Throttle Developers <tech-reference>`
- :doc:`DCC-EX Native command library - DCCEXProtocol </throttles/native-protocol-library>`

.. toctree::
    :maxdepth: 3
    :hidden:
    
    protocols
    software/index
    hardware/index
    connect_wifi_throttle_via_usb
    tech-reference
    DCC-EX Native command library </throttles/native-protocol-library>

