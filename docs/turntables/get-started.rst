***************
Getting started
***************

Assembly
--------

For assembly, we will assume the default ULN2003/28BYJ-48 combo is in use with an Arduino Nano V3, a standard 3 pin Arduio compatible hall effect sensor, and a dual relay board.

We will also assume a prototyping shield is available that provides regulated 5V power sufficient for driving the ULN2003/28BYJ-48 stepper combo, and that there is a power supply with a suitable DC power plug to suit the prototyping shield.

1. BEFORE you start
-------------------

Visually check all components for any obvious damage, paying particular attention to pins on the Arduino to make sure they are straight.

2. Insert the Nano into the shield
----------------------------------

Insert the Nano into the prototype shield socket, taking care to ensure the USB socket is located at the same end as the DC power jack, and that all pins are straight and aligned correctly with the female headers.

The various pin numbers may also be printed on the prototyping shield to confirm the correct orientation.

<Insert image here>

3. Connect the stepper controller and motor
-------------------------------------------

Firstly, note that the ULN2003 controller will have four pins marked "IN1" through "IN4", as well as a pair of pins with "+" and "-". There is a likely a jumper installed across two pins beside these that is unmarked, leave this in place.

Now, you will need six of the female to female Dupont wires and connect these from the ULN2003 pins to the Arduino prototype shield as below:

.. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * - ULN2003 Pin
      - Arduino Pin
    * - IN1
      - 8
    * - IN2
      - 9
    * - IN3
      - 10
    * - IN4
      - 11
    * - \+
      - Pin 8 5V
    * - \-
      - Pin 8 GND
  
<Insert image here>

Insert the stepper motor connector into the recepticle on the ULN2003 controller. Note that it will only go in one way, so check the orientation and simply plug it in.

<Insert image here>

4. Connect the hall effect sensor
---------------------------------

The hall effect sensor has three pins, and likely only two of these pins are marked, the left with "-" and right with "S". The middle pin is likely to be unmarked, and will be the 5V pin. There are probably many different varieties of sensors and designs out there, but both that I have (from different suppliers) are marked identically.

Use three of the Dupont wires and connect these from the hall effect sensor to the Arduino prototype shield as below:

.. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * - Hall Effect Pin
      - Arduino Pin
    * - \- (Left)
      - Pin 2 ground
    * - Unmarked (middle)
      - Pin 2 5V
    * - S (Right)
      - Pin 2

<Insert image here>

5. Connect the dual relay board
-------------------------------

Note there should be six pins on the dual relay board marked "VCC", "GND", "IN1", "IN2", "COM", and "GND". The "COM" and "GND" pins should have a jumper installed to connect these together. Leave this in place.

Use four Dupont wires to connect the other four pins as below:

.. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * - Dual Relay Pin
      - Arduino Pin
    * - VCC
      - Pin 3 5V
    * - GND
      - Pin 3 GND
    * - IN1
      - 3
    * - IN2
      - 4

<Insert image here>

6. Connect power and test
-------------------------

At this point, it should be safe to plug in the power supply to the DC power jack on the prototyping shield.

When the power supply is turned on, the power LEDs on the Arduino Nano and dual relay board should be lit. Note there is likely no power LED on the ULN2003 stepper controller, and testing of this will require loading the Turntable-EX software on to the Nano.

To validate the hall effect sensor is connected correctly, put a magnet in close proximity (within a millimetre or so) of the sensor IC, and the onboard LED should light up.

<Insert images here>

7. Load the software
--------------------

At the time of writing, there is no installer for Turntable-EX like there is for the CommandStation, so you will need to install the Arduino IDE and load the software onto the Arduino manually.

The process here is the same as installing CommandStation-EX via the Arduino IDE which you can find on the :doc:`/get-started/arduino-ide` page.

While following that process, you will need to make some ammendments to cater for Turntable-EX:

* The software is available on the `Turntable-EX download page <https://github.com/DCC-EX/Turntable-EX/releases>`
* References to CommandStation-EX are substituted with Turntable-EX (eg. your folder name needs to be called Turntable-EX)
* You will need to set the board type to "Nano" and set the correct Processor type (typically ATMega328P)

<TO DO: Add the ability to test the basic Turntable-EX functions here via serial console>

1. Connect Turntable-EX to your CommandStation
----------------------------------------------

To control Turntable-EX from your CommandStation, you will need a connection to the I2C (SDA, SCL) pins.

Ensure you turn the power off to both your CommandStation and Turntable-EX prior to making any of these connections.

On the CommandStation, assuming this is a Mega2560 or Mega2560 + WiFi, the SDA (pin 20) and SCL (pin 21) pins are typically labelled as such, so should be easy to identify.

On an Arduino Nano (and Uno) however, the SDA and SCL pins are shared with analog pins A4 and A5, and therefore aren't explicitly labelled. The SDA pin is A4, and the SCL pin is A5.

Connect these pins to your CommandStation as shown in the table below, noting that it is important to ensure the ground is also connected to ensure the I2C communication is reliable.

.. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * - CommandStation Pin
      - Arduino Nano Pin
    * - 20 (SDA)
      - A4 (SDA)
    * - 21 (SCL)
      - A5 (SCL)
    * - Any spare ground
      - A4 GND

Now you're ready!
=================

At this point, you should now have a fully assembled Turntable-EX with the software loaded and a default configuration.

In addition, Turntable-EX should be connected to your CommandStation ready to test, tune your turntable positions, and configure EX-RAIL ready for use on your layout.

Click the "next" button to get cracking!
