.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst
|EX-CS-LOGO|

************
Teensy
************

|tinkerer| |engineer|

**As of version 5.4.0, this is now deprecated, see :doc:`/news/posts/20240328`**

The Teensy 3.x/4.x Series by PJRC are next generation ARM-based microcontrollers. They have loads of RAM, a faster clock speed and a host of add-ons. 

It's teensy because it is even smaller than a Nano, but it is even more powerful than a Nano Every. This is not an Arduino, it is from a company called PJRC. Since they use different processors, there are a lot of changes in the software that load onto the teensy when you select that as your processor.

There are several versions 3.2, 3.5, 3.6, 4.0, 4.1. with the biggest difference being the size/number of pins. You can also purchase the boards with or without the headers soldered on.

.. image:: /_static/images/microcontrollers/teensy_3_2.jpg
   :alt: Teensy 3.2
   :scale: 40%
   :align: center

The above is a Teensy 3.2 compared to a quarter. Below is a Teensy 3.6 if you need more GPIO pins

.. image:: /_static/images/microcontrollers/teensy_3_6.png
   :alt: Teensy 3.6
   :scale: 40%
   :align: center

There are even expansion boards to add WiFi and Ethernet. There is a Mega form factor board available to allow you to use 3.3V shields.

.. image:: /_static/images/microcontrollers/teensy41_ethernet2.jpg
   :alt: Teensy Ethernet
   :scale: 40%
   :align: left

.. image:: /_static/images/microcontrollers/teensy_4_expansion_brd.jpg
   :alt: Teensy WiFi Expansion Board
   :scale: 60%
   :align: left

.. rst-class:: clearer

Teensy 3.6 Specifications
=========================

* 180 MHz ARM Cortex-M4 with Floating Point Unit
* 1M Flash, 256K RAM, 4K EEPROM
* Microcontroller Chip MK66FX1M0VMD18
* MK66FX1M0VMD18
* USB High Speed (480 Mbit/sec) Port 
* 2 CAN Bus Ports 
* 32 General Purpose DMA Channels 
* 22 PWM Outputs 
* 4 |I2C| Ports 
* 11 Touch Sensing Inputs 
* 62 I/O Pins (42 breadboard friendly) 
* 25 Analog Inputs to 2 ADCs with 13 bits resolution 
* 2 Analog Outputs (DACs) with 12 bit resolution 
* 22 PWM Outputs
* USB Full Speed (12 Mbit/sec) 
* Port Ethernet mac, capable of full 100 Mbit/sec speed 
* Native (4 bit SDIO) 
* micro SD card port 
* I2S Audio Port 
* 4 Channel Digital Audio Input & Output 
* 19 Hardware Timers 
* Cryptographic Acceleration Unit 
* Random Number Generator 
* CRC Computation Unit 
* 6 Serial Ports (2 with FIFO & Fast Baud Rates) 
* 3 SPI Ports (1 with FIFO)
* Real Time Clock

|EX-CS| will run on all these boards, however the following caveats apply:

- Teensys are strictly 3.3V, so you have to be careful that anything connected to the GPIO ports is also 3.3V (see also :doc:`other 3.3v microcontrollers </reference/hardware/microcontrollers/microcontrollers>`)
- Teensy 3.x models are all now considered "legacy" products by PCJR and marked "Not recommended for new designs or projects", with only Teensy 4.0/4.1 recommended by PCJR
- Version 3.1, development versions 4.2.4 and beyond, and upcoming 5.x releases of |EX-CS| can compile for the Teensy models listed above, but have not been extensively tested
- Teensy |I2C| peripheral uses the blocking Arduino Wire library, as there is no |DCC-EX| native non-blocking |I2C| driver for any of the Teensy range presently available, or planned. This will limit performance somewhat when using |I2C| peripherals attached to your Teensy.
- Note that no further development and testing efforts by the core development team will be directed to Teensy models under the current :doc:`roadmap </about/roadmap>`

The major downside to all Teensy models is that PJRC is a very small company so as such it simply doesn't have the resources or the staff of major manufacturers like Arduino, Espressif or ST Microelectronics.
