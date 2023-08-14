.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-description.rst
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

|EX-CS| currently is designed for Atmel AVR based Arduino and compatible microcontrollers, and some ARM based boards such as the Teensy range. Out of the box, it is compatible with the following boards:

.. toctree::
    :maxdepth: 1

    /reference/hardware/microcontrollers/arduino-mega
    /reference/hardware/microcontrollers/arduino-uno
    /reference/hardware/microcontrollers/nano
    /reference/hardware/microcontrollers/microcontrollers
    /reference/hardware/microcontrollers/wifi-mega
    /reference/hardware/microcontrollers/nano-every
    /reference/hardware/microcontrollers/teensy

Choosing a microcontroller
==========================

With so many microcontrollers to choose from, how do you know which is the best for your needs?

We've compiled this simple summary table to help with this:

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Microcontroller
    - Status
    - HAL/|I2C|
    - EEPROM
    - EXRAIL
    - JMRI
    - Network
    - TrackManager
    - Comments
  * - Mega2560
    - Supported
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes [1]_
    - DCC and DC [2]_
    - This is our stable, well supported platform
  * - Uno
    - Supported
    - No
    - Yes
    - Limited [3]_
    - Yes
    - No
    - DCC only [2]_
    - Great for either small layouts with no programming, or a dedicated programmer with |JMRi|
  * - Nano
    - Supported
    - No
    - Yes
    - Limited [3]_
    - Yes
    - No
    - DCC only [2]_
    - Similar to Uno, but without the convenient Uno footprint
  * - Mega+WiFi
    - Supported [6]_
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes
    - DCC and DC [2]_
    - This is our stable, well supported platform, with WiFi on board, but beware quality issues
  * - STM32 Nucleo
    - Beta [4]_
    - Yes [5]_
    - No
    - Yes
    - Yes
    - Yes [1]_
    - DCC and DC [2]_
    - Lots of memory and 32 bit architecture, still in the convenient Uno form factor but with more I/O pins
  * - ESP32 WROOM
    - Beta [4]_
    - Yes [5]_
    - No
    - Yes
    - Yes
    - Yes
    - DCC and DC [2]_
    - Inexpensive and includes both WiFi and Bluetooth connectivity, limited in I/O pins
  * - SAMD21
    - Limited [4]_ [8]_
    - Yes [5]_
    - No
    - Yes
    - Yes
    - Yes [1]_
    - DCC only [2]_
    - Modern, 32 bit architecture but several caveats around voltage and USB connectivity
  * - Nano Every
    - Limited [7]_
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes [1]_
    - DCC only [2]_
    - Limited support only
  * - Teensy
    - Limited [7]_
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes [1]_
    - DCC only [2]_
    - Limited support only

.. [1] Requires an additional :ref:`Ethernet <reference/hardware/ethernet-boards:ethernet boards>` or :ref:`WiFi <reference/hardware/wifi-boards:wifi boards>` shield
.. [2] Requires a supported motor driver that supports :ref:`TrackManager <trackmanager/index:hardware requirements and technical notes>`
.. [3] Limited |EX-R| scripts are possible only when disabling EEPROM and programming
.. [4] Features and support in Beta testing can and will change regularly, be sure to keep up to date with developments on our `Discord server <https://discord.gg/y2sB4Fp>`_
.. [5] HAL/|I2C| connectivity is only available via the blocking Arduino Wire library at present
.. [6] While the Mega+WiFi boards seem like a good option and are based on our well-known, stable Mega2560 platform, there are many reports of quality issues with these, so buyer beware
.. [7] The core development team no longer have access to these, and testing is limited to ensuring the software compiles for the board type
.. [8] The core Arduino library has a bug affecting serial console output which can be patched but renders the device unsuited for future development until fixed in the main Arduino core library for SAMD21

Will you support other microcontrollers in the future?
=======================================================

Yes, that is on our :doc:`roadmap </about/roadmap>`, and the current state of progress can be found in our :doc:`features under development </under-development/index>` area. New microcontrollers being ported to include ESP32, SAMD21, and the STM32F4xx range as can be seen in :doc:`/reference/hardware/microcontrollers/microcontrollers`.

Boards that will NOT work
==========================

**WAVGAT Uno clone** - This board is NOT 100% Uno compatible. It uses a LGT8F328P processor from a company in China called "Logic Green". It has no EEPROM and requires a bit of configuration in the Arduino IDE to get it to be seen correctly and compile sketches. It is, however, a good board for developing other applications on because it can be switched to run at 32mHz instead of 16. It also has 12 bit analog pins instead of 10 bit. That means higher resolution readings, 0-4096 instead of 0-1024. It could potentially work as a Command Station with more testing and some code changes, but we will leave that to someone else to attempt. Various other microcontrollers offer more memory, more serial ports and more GPIO pins and are just a better way to go for the future.