.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-throttles.rst
|EX-THROTTLES-LOGO|

***********************
Throttles (Controllers)
***********************

|SUITABLE| |conductor| |tinkerer| |engineer| |support-button| 

This page contains lists of compatible Throttles (Controllers) that currently support the |EX-CS|.  They are listed two ways:

.. sidebar:: 
   :class: sidebar-on-this-page

   .. contents:: On this page
      :depth: 2
      :local:


* :ref:`By Client Technology <throttles/index:throttles - by client technology>`  (e.g. Android, iOS, Web Browser, PC)
* :ref:`By Communication Technology <throttles/index:throttles - by communication technology>` (e.g. |DCC-EX Native Commands|, |WITHROTTLE PROTOCOL|)

For an more introductory overview of throttles and how to choose one, please read the :doc:`Getting Started - Throttles Page </ex-commandstation/controllers-diy>` 

|SUITABLE| |tinkerer| |engineer| |support-button|

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
- :doc:`DigiTrainsPro (Android, iOS, Windows) <software/digitrainspro>` *- Requires JMRI*
- :doc:`RtDtive DCC++ (Android) <software/rtdrive-dccpp>`

Apple iOS (Phones and Tablets)
------------------------------

- :doc:`Locontrol (iOS) <software/locontrol>`
- :doc:`WiThrottle (iOS) <software/withrottle>`
- :doc:`SRCP Client (iOS) <software/srcpclient>`
- :doc:`Train Driver (iOS) <software/train-driver>`
- :doc:`ThrottleCard (iOS) <software/throttlecard>`
- :doc:`DigiTrainsPro (Android, iOS, Windows) <software/digitrainspro>` *- Requires JMRI*


Dedicated Hardware
------------------

- :doc:`miniThrottle (Physical) <hardware/minithrottle>`
- :doc:`WiTcontroller (Physical) <hardware/witcontroller>`
- `HandCab (Physical) <https://github.com/1fatgmc/HandCab/tree/main>`_
- :doc:`DccExController (Physical) <hardware/dccexcontroller>`
- :doc:`TCS UWT-50 (Physical) <hardware/uwt50>`
- :doc:`Elgato Stream Deck (Physical) <hardware/streamdeck>`
- :doc:`LoDi-Con WiFi Throttle </throttles/hardware/lodi-con-wifi-throttle>`
- :doc:`DCC-EX Native command library - DCCEXProtocol </throttles/native-protocol-library>`
- See also :doc:`DCC-EX Native command library - DCCEXProtocol </throttles/native-protocol-library>`

Personal Computers
------------------

- :doc:`EX-WebThrottle </ex-webthrottle/index>`  *(Web Browser)*
- :doc:`JMRI (Windows, iOS, Linux) <software/jmri>`
- :doc:`DigiTrainsPro (Android, iOS, Windows) <software/digitrainspro>` *- Requires JMRI*
- :doc:`Train Throttle <software/train-throttle>`
- :doc:`Railroad Automation <software/railroad-automation>` *- Requires IoTT Red Hat*

Note: The Android throttle apps listed above can be made to made to run on Windows PCs. See :doc:`Running Android apps on Microsoft Windows <software/android-apps-on-windows>`.


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
- :doc:`DccExController (Physical) <hardware/dccexcontroller>`
- See also :doc:`DCC-EX Native command library - DCCEXProtocol </throttles/native-protocol-library>`

WiThrottle Protocol Based Throttles
-----------------------------------

- :doc:`Engine Driver (Android)<software/engine-driver>`
- :doc:`Locontrol (iOS) <software/locontrol>`
- :doc:`Cab Engineer: DCC Throttle (Andriod) <software/cab-engineer>`
- :doc:`WiThrottle (iOS)<software/withrottle>`
- :doc:`SRCP Client (iOS) <software/srcpclient>`
- :doc:`Train Driver (iOS) <software/train-driver>`
- :doc:`ThrottleCard (iOS) <software/throttlecard>`
- :doc:`miniThrottle (Physical) <hardware/minithrottle>`
- :doc:`WiTcontroller (Physical) <hardware/witcontroller>`
- `HandCab (Physical) <https://github.com/1fatgmc/HandCab/tree/main>`_
- :doc:`TCS UWT-50 (Physical) <hardware/uwt50>`
- :doc:`Elgato Stream Deck (Physical) <hardware/streamdeck>`
- :doc:`LoDi-Con WiFi Throttle </throttles/hardware/lodi-con-wifi-throttle>`

USB Based Throttles
-------------------------------

- :doc:`EX-WebThrottle </ex-webthrottle/index>`
- :doc:`myBluePillThrottle <hardware/mybluepillthrottle>`
- Also see: :doc:`connect_wifi_throttle_via_usb`

JMRI Web Server Based Throttles
-------------------------------

- :doc:`DigiTrainsPro (Android) <software/digitrainspro>`

----

Table - Throttles by Technology 
===============================

.. include:: throttle_table.rst

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

