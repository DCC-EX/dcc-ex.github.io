************
Get Started
************

This page is intended to get you started with DCC++ EX by helping you in building your hardware setup, installing software, flashing firmware, and running your first train. After that, we will provide examples for how the base system can be extended and upgraded.

The Components of a Full System
================================

- **Command Station** - An Arduino with a motor driver board and the DCC-EX uploadable firmware
- **Controller** - A Throttle/Cab such as WebThrottle-EX, JMRI, Engine Driver, etc
- **Power** - A DC power supply for the motor board to the track, and optionally one for the Arduino
- **A "Main" track,** aka "Operations" track - most people already have this: it's your layout!
- **A "Programming" track,** aka "Service" track - a short section of track that you will use to program locomotives (see section on layout)
- **A Train** - Specifically, a locomotive equipped with a DCC decoder (either a standard or sound decoder)


What you need
==============

**Hardware**:

- Supported :doc:`Arduino board </reference/hardware/microcontroller-boards>`
- Supported :doc:`motor shield </reference/hardware/motor-boards>`
- Compatible :doc:`power supply </reference/hardware/power-supplies>`
- Computer running Windows, macOS, or Linux (even a Raspberry Pi)
- USB Cable from the computer to the Arduino
- Piece of track to run trains or program on
- Known-working DCC-equipped locomotive

**Optional hardware**:

- Supported :doc:`ESP8266 WiFi shield </reference/hardware/wifi-boards>`
- Supported :doc:`Ethernet shield </reference/hardware/ethernet-boards>`

**Software**:

- See the :doc:`Command Station download page <../download/commandstation>`

The DCC++ EX installer is recommended for most users as it automatically downloads and installs the required software. 

You'll also need something to control your trains. Because there are several options, we will discuss this following the system setup.

See this :doc:`Shopping List </reference/hardware/shopping-list>` for everything you need, organized for you in one place.

I'm Ready!
===========

Click the "next" button below to choose your path, and then move ahead to how to assemble your Command Station.

.. toctree::
    :hidden:

    levels
    assembly
    wifi-setup
    installer
    arduino-ide
    controllers
    diagnosing-issues
