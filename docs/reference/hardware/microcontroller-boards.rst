.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-REF-LOGO|

***********************
Microcontroller Boards
***********************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

Current list of Microcontrollers
================================

|EX-CS| currently is designed for Arduino and select microcontrollers. Out of the box, it is compatible with the following boards:

.. toctree::
    :maxdepth: 1

    /reference/hardware/microcontrollers/arduino-mega
    /reference/hardware/microcontrollers/arduino-uno
    /reference/hardware/microcontrollers/nano
    /reference/hardware/microcontrollers/nano-every
    /reference/hardware/microcontrollers/teensy
    /reference/hardware/microcontrollers/wifi-mega

Will you support other microcontrollers in the future?
=======================================================

Yes, that is on our :doc:`roadmap </about/roadmap>`.

Boards that will NOT work
==========================

**WAVGAT Uno clone** - This board is NOT 100% Uno compatible. It uses a LGT8F328P processor from a company in China called "Logic Green". It has no EEPROM and requires a bit of configuration in the Arduino IDE to get it to be seen correctly and compile sketches. It is, however, a good board for developing other applications on because it can be switched to run at 32mHz instead of 16. It also has 12 bit analog pins instead of 10 bit. That means higher resolution readings, 0-4096 instead of 0-1024. It could potentially work as a Command Station with more testing and some code changes, but we will leave that to someone else to attempt. Megas and Mega clones offer more memory, more serial ports and more GPIO pins and are just a better way to go for the future.

**ESP32** - Great little board, however it is a completely different architecture so the same code will not work on it. It is made by Espressif. We currently support only the Atmel family of processors and the PJRC Teensy. It also is a smaller board so shields would have to be connected with jumpers.
