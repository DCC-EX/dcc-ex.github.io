.. meta::
  :keywords: EX-CommandStation Command Station EX-IOExpander

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-IO-LOGO|

*******************
Using other devices
*******************

|EX-IO| is designed to be a very generic I/O expansion option, and any external device that can work with digital reads/writes or send in analogue data should be able to use the same device driver.

If anyone wishes to utilise the |EX-IO| device driver with a different device, then this can be accomplished provided the correct instructions are sent/received along with the data.

The use of this should be reasonably simple to understand from the device driver itself (IO_EXIOExpander.h) but it is outlined here as an addendum to that.

The EX-IOExpander communication protocol
========================================

There is a protocol of sorts in place that enables the device driver in your |EX-CS| to configure |EX-IO|, know when it is ready for operation, discover what version is installed on it, and then to enter normal operation mode to send/receive data.

There are seven registers or instructions used in this procotol:

- EXIOINIT = 0xE0 - Initialise the setup procedure
- EXIORDY = 0xE1 - Setup procedure complete
- EXIODPUP = 0xE2 - Send digital pin pullup configuration
- EXIOVER = 0xE3 - Get version
- EXIORDAN = 0xE4 - Read an analogue input
- EXIOWRD = 0xE5 - Send a digital write
- EXIORDD = 0xE6 - Read a digital input
- EXIOENAN = 0xE7 - Enable an analogue input
- EXIOINITA = 0xE8 - Request/receive analogue pin mappings
- EXIOPINS = 0xE9 - Request/receive buffer counts
- EXIOWRAN = 0xEA - Send an analogue write (PWM)
- EXIOERR = 0xEF - Error sent/received

Device setup
------------

This is the device setup/configuration process:

- Check no overlaps in Vpin allocation
- Create the device object
- Check that the |I2C| device is online
- Device driver sends "EXIOINIT" with digital and analogue pin counts
- |EX-IO| must respond with "EXIORDY" otherwise device marked offline
- Device driver sends "EXIOVER" and expects a three byte response with the major, minor, and patch version

Digital pin configuration
-------------------------

When a digital input is defined via either |EX-R| (eg. ``AT(vpin)``, ``AFTER(vpin)``, ``IF(vpin)``) or the ``<S id vpin pullup>`` DCC-EX command, this triggers the configuration function which sends that information to the |EX-IO| device:

- Validates the digital pin hasn't already been defined as an analogue pin elsewhere
- Device driver sends "EXIODPUP" with the pin number and pullup flag (0 no pullup, 1 pullup)
- There is no return/acknowledgement required

Digital reads
-------------

When a digital read occurs:

- Validates the digital pin hasn't already been defined as an analogue pin elsewhere
- Device driver sends "EXIORDD" with the pin number
- |EX-IO| device must return a single byte containing the read value (0 inactive, 1 active)

Digital writes
--------------

When a digital write occurs:

- Validates the digital pin hasn't already been defined as an analogue pin elsewhere
- Device driver sends "EXIOWRD" with the pin number and write value (0 inactive, 1 active)
- There is no return/acknowledgement required

Analogue reads
--------------

When an analogue read occurs:

- Validates the analogue pin hasn't already been defined as a digital pin elsewhere
- Device driver sends "EXIORDAN" with the pin number
- |EX-IO| must return two bytes containing the most significant and least significant 8 bits of the 16 bit integer value
- These are bit shifted together to return the full 16 bit integer value to whatever called the analogue read