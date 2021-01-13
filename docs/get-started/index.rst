Get Started
===========

This page is intended to get you started with DCC++ EX by helping you in building your hardware setup, installing software, flashing firmware, and running your first train. After that, we will provide examples for how the base system can be extended and upgraded.

The Components of a Full System
-------------------------------

- **Command Station** - An Arduino with a motorboard and the DCC-EX uploadable firmware
- **Controller** - A Throttle/CAB such as WebThrottle-EX, JMRI, Engine Driver, etc.
- **Power** - A DC power supply for the motor board to the track and optionally one for the Arduino
- **A "main" track** aka "operations" track - most people already have this, it's your layout
- **A "programming" track** aka "service" track - a short section of track that you will use to program locomotives (see section on layout)
- **A Train** Specifically, a locomotive equipped with a DCC decoder (either a standard or sound decoder)


What you need
-------------

**Hardware**:

- Supported `Arduino board <../reference/hardware/microcontroller-boards.html>`_
- Supported `motor shield <../reference/hardware/motor-boards.html>`_
- Compatible `power supply <../reference/hardware/power-supplies.html>`_
- Computer running Windows, Linux, or macOS (or a Raspberry Pi)
- USB Cable from the computer to the Arduino
- Piece of track to run trains or program on
- Known-working DCC-equipped locomotive

**Optional hardware**:

- Supported `ESP8266 WiFi shield <../reference/hardware/wifi-boards.html>`_
- Supported `Ethernet shield <../reference/hardware/ethernet-boards.html>`_

**Software**:

- See the `Command Station download page <../download/commandstation.html>`_

The DCC++ EX installer is recommended for most users and automatically downloads and installs the required software. 

You'll also need something to control your trains. Because there are several options, we will discuss this following setup of the system.

See this `Shopping list <../reference/hardware/shopping-list.html>`_ for everything you need organized for you in one place.

I'm Ready!
-----------

Click the "next" button below to choose your path and then move ahead to how to assemble your Command Station.

.. toctree::
    :hidden:

    levels
    assembly
    wifi-setup
    installer
    arduino-ide
    controllers
