.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|donate-button|

************************
DCC-EX Roadmap
************************

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

2022
=====

Software
________

EX-CommandStation 
^^^^^^^^^^^^^^^^^

* Add support for an ESP-32 or equivalent to remove resource limitations.
* Remove need to have any conditional compilation of features. This means the binary can be built and downloaded directly without a compiler or IDE. Customisation can take place through the command language API and mySetup.h file.
* Program the WiFi solution with our own code that implements a “true” network connection, still has the AT command set, and can handle at least 12 sockets.
* Upgrade the WiFi option with possible ESP32 containing custom AT firmware with possible Ethernet upgrade and Web Interface for configuration and/or control.
* OpenMRN on a co-processor?
* Multiple simultaneous Motor Driver support (beyond the 2 we currently support).
* Add EX-RAIL "Extended Railroad Automation Instruction Language". Automate your layout with a simple script. - Now in BETA

EX-DCCInspector
^^^^^^^^^^^^^^^

* Add other report formatting options

EX-WebThrottle
^^^^^^^^^^^^^^

* Add Turnout support
* Add capability to use as an installer/updater/configurer for |DCC-EX|

Hardware
________

New Motor Driver
^^^^^^^^^^^^^^^^

New all-in-one EX-CommandStation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  * Provide a self-contained, yet expandable custom developed Command Station Features (perhaps revive FireBox)
  * Based on a powerful processor to be chosen from ESP32, Teensy, Xtensa, SAMC21, etc
  * At least 20 GPIO Pins
  * More efficient, higher current capacity Motor Driver chip or independent MOSFETS
  * Dual H-Bridge with sustained current of 5A, peaks to 10
  * Processor should have at least 2 x 12bit ADCs for current sense
  * High-Side current sense with amplifier for measurements down to 10mA on the service track
  * Track voltage reading from a resistor voltage divider
  * One USB with 3 or more additional UARTS (hardware serial ports)
  * Computer Interface using the USB port (USB-C or B. Micro too flimsy)
  * 5V Operation through a 5V regulator, 1A output
  * 3.3V Operation through a 3.3V regulator, 800 mA output
  * Manufactured in different countries with partners
  * WiFi, Bluetooth onboard
  * Use ESP32 as WiFi and optional Ethernet bridge using AT commands
  * I2C, CAN and SPI onboard
  * Add RailCom support - Combine main and prog RX signals
  * Add Layout Bus support for LCC
  * Work with Smart Hobby to release LCN (Layout Control Nodes)
  * Define footprint or header(s) for options/add-ons/FireBits
  * Accessible reset button
  * Standard interconnect for pluggable expansion options
  * Display?
  * SDCard?
  * Snap on Raspberry Pi to run |JMRI|?

Firebit Modules
^^^^^^^^^^^^^^^

Based on standard interconnect created for the CS, examples would be separate co-processors, boosters, motor controllers, etc.

Outreach/Partnering/Evangelizing
________________________________

Work with other manufacturers to get their hardware, accessories, motor drives, etc. to market and to gain support for |DCC-EX|. Add more throttles to the list that support the |EX-CS| directly or through |JMRI|.

----

TODO
====

.. todolist:: 
  