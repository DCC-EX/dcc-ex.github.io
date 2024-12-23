.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-csb1.rst
  
|EX-CS-LOGO| |donate-button|

.. index:: EXCSB1, EX-CSB1

*****************************************
|EX-CSB1|
*****************************************

|SUITABLE| |conductor| |tinkerer| |engineer| |support-button|

.. sidebar::

  .. contents:: On this page
    :depth: 3
    :local:

Designed by the |DCC-EX| development team, the EX-CSB1 replaces up to 3 different stacked Arduino boards to provide a complete, expandible DCC and DC PWM command station or booster with dual 5A track outputs, integrated programming track capability, and built-in fast WiFi for throttle control connections.

.. figure:: /_static/images/ex-csb1/csb1_render_drop_shadow.png
   :alt: DCC-EX EX-CSB1
   :scale: 40%

   EX-CSB1 CommandStation / Booster

|HR-DASHED|

What is the EX-CSB1?
====================

The |EX-CSB1| is the first fully integrated DCC Command Station with DC PWM and Booster mode capabilities developed by the DCC-EX Team. This versatile board can function as a complete Command Station with USB or WiFi connectivity or serve as a stand-alone booster, making it an ideal addition to any layout, including those using non-DCC-EX systems.

Key Features:
  * All-in-one DCC Command Station/Booster: Compatible with DCC and capable of PWM DC output
  * Built-in Fast WiFi: Supports up to 10 simultaneous throttle connections, expandable with JMRI
  * Advanced Hardware: Utilizes an ESP32 microcontroller with dual DCC or PWM DC 5A outputs, including variable current limit control
  * Expandable Outputs: Can accept a DCC-EX EX-MotorShield8874 for two additional DCC/DC PWM outputs, providing power to four total districts. Multiple EX-CSB1s can be added as boosters around the layout.
  * Protection & Safety: Software programmable over-current protection, and hardware over-current, over-temperature and reverse voltage protection
  * Versatile Power Supply: Operates with a single 12V to 25V power supply that powers the entire system
  * USB-C Interface: For easy software updates, connection to EX-WebThrottle or JMRI, and logging/debugging
  * Accessory Support: Qwiic/STEMMA QT 3.3V, compatible I2C connector and extra I2C pin headers for all your accessories
  * Pre-Installed with DCC-EX Command Station Software from most suppliers
  * Auto-Reverser capability assignable to each DCC output independently
  * RailSync DCC input for automatic booster mode engagement under software control (|EX-R|)
  * OLED Display: Bundled graphical display for status and diagnostics, with support for additional displays

Benefits include: 
  * Ready-To-Run: Pre-assembled, with no need for additional assembly or configuration
  * Enhanced Performance: Faster WiFi than an ESP8266 with support for double the number of connections, faster processor, and a great deal more memory than an Arduino Mega for complex EXRAIL automation/animation scripts
  * Efficient Power Usage: Less voltage drop, ensuring more power reaches the track
  * Flexible Output Management (TrackManager :sup:`tm` support): Dynamically assign outputs to different modes (DC/DCC/PROG/Auto-Reverse), with proper NMRA current limits

.. image:: /_static/images/ex-csb1/ti_8874.jpeg
   :alt: DCC-EX EX-CSB1
   :scale: 80%
   :align: right

The EX-CSB1's robust, single-PCB design includes integrated MOSFET motor drivers from Texas Instruments, providing up to 5A peak power per track output. This allows for simultaneous operation of multiple trains with reduced power consumption and heat generation compared to traditional systems.

With its dual role as a command station or booster, the EX-CSB1 can be strategically placed around a layout, seamlessly switching to booster mode upon detecting a RailSync input signal. This feature is particularly useful for modular layouts, ensuring smooth operation across different sections once joined together and slaved to a master DCC signal. Distributing power around the layout also reduces the cost of heavy copper lines to carry the DCC signal that would otherwise be needed with centralised power.

An additional DCC-EX EX-MotorShield 8874 can be inserted onto the command station board to provide two more DCC or PWM DC outputs with the same performance characteristics and output mode flexibility.

.. figure:: /_static/images/ex-csb1/csb1_stacked.png
   :alt: EX-CSB1 Stacked with EX-MotorShield8874
   :scale: 60%
   :align: center

   EX-CSB1 Stacked with EX-MotorShield8874

The system includes comprehensive protection features such as reverse polarity protection, hardware and software overcurrent protection, overvoltage protection, and thermal protection. It also provides clear status indications via LEDs for microcontroller power, track input supply, track output power per output channel, DCC/DC mode indication and direction for DC mode, and WiFi connection status.

The |EX-CSB1|'s built-in EXRAIL layout Animation and Automation capabilities enable advanced control of layout operations, including crossing controls, signal management, automated train routing, layout lighting control, and much more whilst being much simpler to learn than Arduino C++ programming.

|HR-DASHED|

Why did we make it?
====================

After the success of our EX-CommandStation software and then the |EX-MS|, which allowed modellers to build their own setups, we realised there was a need for something even simpler. The DCC-EX Team wanted to create a solution that would appeal to a wider range of modellers, especially those who might not feel as confident with the electronics and software or those who just prefer to spend time enjoying their layouts instead of tinkering with tech.

We wanted to keep the sense of accomplishment that comes with a DIY project, but make it much easier, smaller, and more "plug-and-play". After all, most of us would rather focus on running our trains than on troubleshooting wiring or connections. 

Whether you consider yourself a |Conductor-text|, |Tinkerer-text|, or |Engineer-text|, you might appreciate an all-in-one solution that saves time and space, and reduces complexity. So we asked ourselves, "What features would the ideal entry-level yet expandible command station have?". And that's how the |EX-CSB1| was born.

|HR-DASHED|

How can I get one?
==================

Units may be purchased from the following sources:

.. include:: /purchasing/include__dealers.rst

|HR-DASHED|

.. include:: /purchasing/include__ex-csb1-pricing.rst

----

Next Steps
==========

* :doc:`Getting started with the EX-CSB1 </ex-commandstation/ready-to-run/connecting>`
* :doc:`EX-CSB1 Operating Manual </ex-commandstation/ready-to-run/manual>`
