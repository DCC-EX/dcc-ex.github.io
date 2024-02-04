.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-io.rst
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

There are seven registers or instructions used in this protocol:

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
- Device driver sends "EXIOINIT" with the number of defined pins and the first allocated Vpin
- |EX-IO| validates pin count and must respond with "EXIOPINS" along with the number of digital and analogue pins
- Device will be marked offline if response is not correct
- Device driver sends "EXIOINITA" to obtain the mapping of analogue pins
- |EX-IO| must respond with the map of analogue pins to bytes in the analogue input buffer
- Device driver sends "EXIOVER" and expects a three byte response with the major, minor, and patch version

Digital input configuration
---------------------------

When a digital input is defined via either |EX-R| (e.g. ``AT(vpin)``, ``AFTER(vpin)``, ``IF(vpin)``) or the ``<S id vpin pullup>`` DCC-EX command, this triggers the configuration function which sends that information to the |EX-IO| device and must trigger it to start monitoring the pin and sending the data back to the device driver:

- Validates the digital pin hasn't already been defined as an analogue pin elsewhere
- Device driver sends "EXIODPUP" with the pin number and pullup flag (0 no pullup, 1 pullup)
- |EX-IO| must respond with "EXIORDY"

Analogue input configuration
----------------------------

When an analogue input is defined in |EX-R| using commands such as ``ATGTE(vpin, value)`` or ``IFLT(vpin, value)``, this triggers the analogue input configuration function which sends the pin number to the |EX-IO| device and must trigger it to start monitoring the pin and sending the data back to the device driver:

- Validates the analogue pin hasn't already been defined as a digital pin elsewhere
- Device driver sends "EXIOENAN" with the pin number
- |EX-IO| must respond with "EXIORDY"

Continuous receiving of input data
----------------------------------

The |EX-IO| device must continuously send the digital and analogue input pin values to the device driver, as this is requested continuously by the device driver's loop function. This must be sent by using one buffer for digital pin states, and a separate buffer for analogue input values.

- Device driver sends "EXIORDD"
- |EX-IO| device must send a buffer containing all digital input pin states:

  - Each byte in the buffer represents up to 8 pin states
  - The buffer must contain the correct number of bytes to represent the number of all digital pins
  - The buffer bytes must be sent in ascending order, i.e. the first byte contains the first 8 digital pin states

- Device driver sends "EXIORDAN"
- |EX-IO| must send a buffer containing all analogue input pin values:

  - Each input pin is represented by two bytes in the buffer
  - The least significant byte of the pin's value is received first, followed by the most significant byte
  - The buffer must contain the correct number of bytes to represent the number of all analogue pins
  - The buffer bytes must be sent in ascending order, i.e. the first byte contains the least significant byte of the first pin's value, with the second byte containing the most significant byte of the first pin's value

Digital reads
-------------

When a digital read occurs:

- Validates the digital pin hasn't already been defined as an analogue pin elsewhere
- Device driver sends "EXIORDD" with the pin number
- |EX-IO| device must return a single byte containing the read value (0 inactive, 1 active)

Digital writes
--------------

When a digital write occurs:

- There is no interaction with the |EX-IO| device, the bit is read from the digital pin buffer

Analogue reads
--------------

When an analogue read occurs:

- There is no interaction with the |EX-IO| device, the lease and most significant bytes are read from the analogue pin buffer
- These are bit shifted together to return the full 16 bit integer value

Analogue writes (PWM)
---------------------

Using the ``<D SERVO vpin value profile>`` command, or the various ``SERVO_TURNOUT(...)``, ``SERVO_SIGNAL(..)`` |EX-R| servo commands, or the ``FADE(...)`` |EX-R| LED command will generate an analogue write to send the associated PWM value to the |EX-IO| device:

- Device driver calculates servo/PWM parameters
- Device driver sends "EXIOWRAN" with the pin number and least and most significant bytes of the 16 bit value
- No response is required from the |EX-IO| device