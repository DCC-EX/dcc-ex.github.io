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

- :doc:`EX-Web-Throttle (Web Browser) <software/ex-webthrottle>`

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
- :doc:` DCC-EX Native command library - DCCEXProtocol <throttles/native-protocol-library>`

Personal Computers
------------------

- :doc:`EX-WebThrottle <software/ex-webthrottle>`
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

- :doc:`EX-WebThrottle <software/ex-webthrottle>`
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

- :doc:`EX-WebThrottle <software/ex-webthrottle>`
- Also see: :doc:`connect_wifi_throttle_via_usb`

JMRI Web Server Based Throttles
-------------------------------

- :doc:`Locontrol (iOS) <software/locontrol>`
- :doc:`DigiTrainsPro (Android) <software/digitrainspro>`

----

Reference
=========

- :doc:`Technical Reference for Throttle Developers <tech-reference>`


.. toctree::
    :maxdepth: 1
    :hidden:
    
    protocols
    software/index
    hardware/index
    connect_wifi_throttle_via_usb
    tech-reference

