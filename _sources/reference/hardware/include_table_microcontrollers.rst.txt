.. include:: /include/include_xa.rst
  
.. flat-table::
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Type / Brand |_xa| |_xa| |_xa| |_xa| |_xa|
    - R |BRxa| e |BRxa| c |BRxa| o |BRxa| m |BRxa| m |BRxa| e |BRxa| n |BRxa| d |BRxa| e |BRxa| d
    - S |BRxa| u |BRxa| p |BRxa| p |BRxa| o |BRxa| r |BRxa| t |BRxa| e |BRxa| d
    - Level
    - Shield |BRxa| Format
    - HAL |BRxa| / |BRxa| |I2Cxa|
    - E |BRxa| E |BRxa| P |BRxa| R |BRxa| O |BRxa| M
    - EX- |BRxa| RAIL |BRxa| Sup- |BRxa| port
    - Track |BRxa| Man- |BRxa| ager |BRxa| Sup- |BRxa| port
    - D C |BRxa| Sup- |BRxa| port
    - W |BRxa| i |BRxa| F |BRxa| i
    - Wifi |BRxa| # |BRxa| Con- |BRxa| nect-  |BRxa| ions |BRxa| [9]_
    - Comments / Notes |_xa| |_xa| |_xa| |_xa| |_xa| |_xa| |_xa| |_xa| |_xa| |_xa| 

  * - EX-CSB1
    - Yes
    - Yes
    - Conductor
    - UNO / Mega
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes
    - ~11
    - This is our stable, well supported platform


  * - Arduino :doc:`Mega2560</reference/hardware/microcontrollers/arduino-mega>`
    - Yes
    - Yes
    - Tinkerer
    - UNO / Mega
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes [2]_
    - yes [1]_
    - 4
    - This is our stable, well supported platform

  * - :doc:`ESP32-WROOM</reference/hardware/microcontrollers/esp32>`
    - Yes
    - Yes
    - Tinkerer
    - \-
    - Yes [5]_
    - No
    - Yes
    - Yes
    - Yes [2]_
    - Yes
    - ~11      
    - Inexpensive and includes both WiFi and Bluetooth connectivity, limited in I/O pins

  * - :doc:`STM32 Nucleo</reference/hardware/microcontrollers/stm32-nucleo>`
    - Yes
    - Yes
    - Tinkerer
    - \-
    - Yes
    - No
    - Yes
    - Yes
    - Yes [2]_ [4]_
    - Yes [1]_ [4]_
    - 4
    - Lots of memory and 32 bit architecture, still in the convenient Uno form factor but with more I/O pins

  * - Arduino :doc:`Uno R3</reference/hardware/microcontrollers/arduino-uno>`
    - No
    - Yes
    - Tinkerer
    - UNO / Mega
    - No
    - Yes
    - Limit- |BRxa| ed [3]_
    - No
    - No [2]_
    - No
    - \-
    - Ok for small layouts with no programming, or a dedicated programmer with JMRI

  * - Arduino Uno R4
    - \-
    - :dcc-ex-red-bold-italic:`No`
    - :cspan:`8` \-
    - :dcc-ex-red-bold-italic:`Different architecture to the R3. Will never be supported.`

  * - Arduino :doc:`Nano</reference/hardware/microcontrollers/nano>`
    - No
    - Yes
    - Tinkerer
    - \-
    - No
    - Yes
    - Limit- |BRxa| ed [3]_
    - No
    - No [2]_
    - No
    - \-
    - Similar to Uno, but without the convenient Uno footprint

  * - Arduino :doc:`Mega+WiFi</reference/hardware/microcontrollers/wifi-mega>`
    - No [6]_
    - Yes
    - Tinkerer
    - UNO / Mega
    - Yes
    - Yes
    - Yes
    - Yes
    - Yes [2]_
    - Yes
    - 4
    - This is our stable, well supported platform, but with WiFi on board, but beware quality issues

  * - SAMD21
    - No
    - Dep- |BRxa| re- |BRxa| cat- |BRxa| ed |BRxa| [7]_ [8]_
    - Engineer
    - \-
    - Yes
    - No
    - Yes
    - Yes
    - No [2]_
    - Yes [1]_
    - 4
    - Limited support only, will be removed in 6.0.0

  * - :doc:`Nano Every</reference/hardware/microcontrollers/nano-every>`
    - No
    - Dep- |BRxa| re- |BRxa| cat- |BRxa| ed |BRxa| [7]_
    - Engineer
    - \-
    - Yes
    - Yes
    - Yes
    - No
    - No [2]_
    - Yes [1]_
    - 4
    - Limited support only, will be removed in 6.0.0

  * - :doc:`Teensy</reference/hardware/microcontrollers/teensy>`
    - No
    - Dep- |BRxa| re- |BRxa| cat- |BRxa| ed |BRxa| [7]_
    - Engineer
    - \-
    - Yes [5]_
    - Yes
    - Yes
    - No
    - No [2]_
    - Yes [1]_
    - 4
    - Limited support only, will be removed in 6.0.0

.. [1] Requires an additional :ref:`Ethernet <reference/hardware/ethernet-boards:ethernet boards>` or :ref:`WiFi <reference/hardware/wifi-boards:wifi boards>` shield
.. [2] Requires a supported motor driver that supports :ref:`TrackManager <trackmanager/index:trackmanager technical details and detailed instructions>`
.. [3] Limited EXRAIL scripts are possible only when disabling EEPROM and programming
.. [4] Features and support in Beta testing can and will change regularly, be sure to keep up to date with developments on our `Discord server <https://discord.gg/y2sB4Fp>`_ 
.. [5] HAL/|I2Cxa| connectivity is only available via the blocking Arduino Wire library at present
.. [6] While the Mega+WiFi boards seem like a good option and are based on our well-known, stable Mega2560 platform, there are many reports of quality issues with these, so buyer beware, and use of these is not recommended
.. [7] The core development team no longer have access to these, and testing is limited to ensuring the software compiles for the board type
.. [8] The core Arduino library has a bug affecting serial console output which can be patched but renders the device unsuited for future development until fixed in the main Arduino core library for SAMD21
.. [9] Direct WiFi connections.  If connected via JMRI, more are are supported
