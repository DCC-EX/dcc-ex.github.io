************************
DCC-EX Roadmap for 2021
************************


Software
=========

DCC++ EX Command Station 
--------------------------

* Develop Hardware Abstraction Layer (HAL) to allow for snap-in modules for different hardware and accessories. We will be both processor and input/output agnostic. Switches, lights, servos,etc. will all go through the same interface
* Add support for an ESP-32 or Equivalent to get rid of resource limitations
* Remove need to have any conditional compilation of features. This means the binary can be built and downloaded directly without a compiler or IDE. Customisation can take place through the command language API and mySetup.h
* Program the WiFi solution with our own code that implements a “true” network connection, still has the AT command set, and can handle at least 12 sockets.
* Upgrade the WiFi option with possible ESP32 containing custom AT firmware with possible Ethernet upgrade and Web Interface for configuration and/or control
* OpenMRN on a co-processor?
* Multiple simultaneous Motor Driver support (beyond the 2 we currently support)
* Add EX-RAIL "Extended Railroad Automation Interface for Layouts". Automate your layout with a simple script.

DCCInspector-EX
------------------

* Add other report formatting options

WebThrottle-EX
-----------------

* Add Turnout support
* Add capability to use as an installer/updater/configurer for DCC++ EX


Hardware
===========

New Motor shield
-----------------




New all-in-one DCC-EX Command Station
--------------------------------------
* (perhaps revive FireBox)to provide a self-contained, yet expandable custom developed Command Station
Features
  * Based on a powerful processor to be chosen from ESP32, Teensy, Xtensa, SAMC21, etc.
  * At least 20 GPIO Pins
  * More efficient, higher current capacity Motor Driver chip or independent MOSFETS
  * Dual H-Bridge with sustained current of 5A, peaks to 10.
  * Processor should have at least 2 - 12bit ADCs for current sense
  * High-Side current sense with amplifier for measurements down to 10mA on the service track.
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
  * Work with Smart Hobby to release LCN (layout control nodes)
  * Define footprint or header(s) for options/add-ons/FireBits
  * Accessible reset button
  * Standard interconnect for pluggable expansion options
  * Display?
  * SDCard?
  * Snap on Raspberry Pi to run JMRI?


Firebit Modules
-----------------
Based on standard interconnect created for the CS, examples would be separate co-processors, boosters, motor controllers, etc.

Outreach/Partnering/Evangelizing
=================================

Work with other manufacturers to get their hardware, accessories, motor shields, etc. to market and to gain support for DCC++ EX. Add more throttles to the list that support DCC++ directly or through JMRI.
