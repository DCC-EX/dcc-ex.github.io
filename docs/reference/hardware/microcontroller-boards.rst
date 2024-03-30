.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-hardware.rst
|EX-REF-LOGO|

**********************
Microcontroller Boards
**********************

 |tinkerer| |engineer| |support-button|
 
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
    /reference/hardware/microcontrollers/esp32
    /reference/hardware/microcontrollers/stm32-nucleo
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
  * - ESP32-WROOM
    - Supported
    - Yes [5]_
    - No
    - Yes
    - Yes
    - Yes
    - DCC and DC [2]_
    - Inexpensive and includes both WiFi and Bluetooth connectivity, limited in I/O pins
  * - STM32 Nucleo
    - Supported
    - Yes
    - No
    - Yes
    - Yes
    - Yes [1]_ [4]_
    - DCC and DC [2]_ [4]_
    - Lots of memory and 32 bit architecture, still in the convenient Uno form factor but with more I/O pins
  * - Uno
    - Not recommended
    - No
    - Yes
    - Limited [3]_
    - Yes
    - No
    - DCC only [2]_
    - Ok for small layouts with no programming, or a dedicated programmer with |JMRi|
  * - Nano
    - Not recommended
    - No
    - Yes
    - Limited [3]_
    - Yes
    - No
    - DCC only [2]_
    - Similar to Uno, but without the convenient Uno footprint
  * - Mega+WiFi
    - Not recommended [6]_
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes
    - DCC and DC [2]_
    - This is our stable, well supported platform, with WiFi on board, but beware quality issues
  * - SAMD21
    - Deprecated [7]_ [8]_
    - Yes [5]_
    - No
    - Yes
    - Yes
    - Yes [1]_
    - DCC only [2]_
    - Limited support only, will be removed in 6.0.0
  * - Nano Every
    - Deprecated [7]_
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes [1]_
    - DCC only [2]_
    - Limited support only, will be removed in 6.0.0
  * - Teensy
    - Deprecated [7]_
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes [1]_
    - DCC only [2]_
    - Limited support only, will be removed in 6.0.0

.. [1] Requires an additional :ref:`Ethernet <reference/hardware/ethernet-boards:ethernet boards>` or :ref:`WiFi <reference/hardware/wifi-boards:wifi boards>` shield
.. [2] Requires a supported motor driver that supports :ref:`TrackManager <trackmanager/index:hardware requirements and technical notes>`
.. [3] Limited |EX-R| scripts are possible only when disabling EEPROM and programming
.. [4] Ethernet on F429ZI/F439ZI is still in Beta, as is DC mode on all STM32 Nucleo boards
.. [5] HAL/|I2C| connectivity is only available via the blocking Arduino Wire library at present
.. [6] While the Mega+WiFi boards seem like a good option and are based on our well-known, stable Mega2560 platform, there are many reports of quality issues with these, so buyer beware, and use of these is not recommended
.. [7] The core development team no longer have access to these, and testing is limited to ensuring the software compiles for the board type
.. [8] The core Arduino library has a bug affecting serial console output which can be patched but renders the device unsuited for future development until fixed in the main Arduino core library for SAMD21

Will you support other microcontrollers in the future?
=======================================================

New microcontrollers are constantly being developed and released, and we continue to monitor those to see if they are beneficial for our users.

Right now, however, we have a good selection of microcontrollers with the Mega2560 and the newer generation ESP32 and STMicroelectronics Nucleo, so we're not looking to add more in the immediate future.

Note the Arduino Giga and Arduino Uno R4 are still not on our roadmap as per our :doc:`/news/posts/20230728` News announcement.

Boards that will NOT work
==========================

**WAVGAT Uno clone** - This board is NOT 100% Uno compatible. It uses a LGT8F328P processor from a company in China called "Logic Green". It has no EEPROM and requires a bit of configuration in the Arduino IDE to get it to be seen correctly and compile sketches. It is, however, a good board for developing other applications on because it can be switched to run at 32mHz instead of 16. It also has 12 bit analog pins instead of 10 bit. That means higher resolution readings, 0-4096 instead of 0-1024. It could potentially work as a Command Station with more testing and some code changes, but we will leave that to someone else to attempt. Various other microcontrollers offer more memory, more serial ports and more GPIO pins and are just a better way to go for the future.