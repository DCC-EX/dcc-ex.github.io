**************************
Connecting a Servo Module
**************************

To connect a servo module to DCC++EX, you first need to get a module, based on the PCA9685 chip.

.. image:: ../../_static/images/i2c/pca9685.jpg
   :alt: PCA9685 Servo Module
   :scale: 40%

These are widely available from ebay, Amazon, etc. for a few dollars.

Note the pin connectors along the left side of the module - these are where you connect to the
Arduino.  

The 16 columns of three pins along the bottom of the module are where you connect the servos.
The pins are arranged so that you can just plug a servo connector directly onto them, but be
sure that the wire colours match the colours of the pins, i.e. yellow to yellow, red to red and black to black.

The servo module itself is powered from the Arduino, but the servos themselves contain motors that
consume more current than the Arduino is able to supply, and so a separate 5V supply is required for the servos.  This is connected to the green terminal block at the top of the module, with terminals labelled V+ and GND. The V+ terminal is connected to 5V and the GND to the 0V (ground) wire of the supply.

Connections to the Arduino are made with four jumper wires (+5V power and GND, and SCL and SDA), as shown on the following diagram:

.. image:: ../../_static/images/i2c/ArduinoMegaServo.png
   :alt: PCA9685 Servo Module
   :scale: 30%

In DCC++EX, the drivers for the PCA9685 module is already installed, and made available to for use as pin numbers 100-115. A servo is shown in the diagram, connected to the first set of pins on the module.  This will be accessed using pin number 100.

Once you've made all of the connections, apply power to the Arduino.

Then, in the Serial Monitor, enter the command `<D SERVO 100 450>`.  The servo should move, as long as it isn't (by some fluke) already in that position.

Enter `<D SERVO 100 110>` and this time it should definitely move.  For the last parameter (servo position) you can use any value between about 105 and 490.

Try `<D SERVO 100 450 3>` and the servo should move slowly back.

You can use the servo to control turnouts, semaphore signals, engine shed doors, and other layout components, to make your layout more dynamic and exciting.  In the picture below, you can see a servo mounted below the baseboard with a piece of wire passing through a slot cut in the baseboard, to operate a turnout.

.. image:: ../../_static/images/i2c/TurnoutServoMount.jpg
   :alt: Servo mount to operate a turnout
   :scale: 60%

And in the next picture you can see a servo that operates a semaphore signal.  The signal, and its
servo mounting bracket, were 3d-printed on a Creality Ender-3 printer.

.. image:: ../../_static/images/i2c/SemaphoreSignal.jpg
   :alt: Servo mount to operate a Semaphore Signal
   :scale: 60%

Using Servos with EX-RAIL
==========================

Defining Turnouts?

Controlling Servos for Turnouts
---------------------------------

SERVO_TURNOUT Command

Controlling Servos for Animations
----------------------------------

SERVO Command


Technical Discussion for Engineers
====================================

There are three types of servos, standard or "Positional Rotation", "Continuous Rotation" and "Linear"

**A Standard, positional rotation servo** allows a shaft to spin around a central axis to position something like an arm or disk at specific angles. A standard servo can be positioned between 0 and 180 degrees. An example is the SG90 9g Micro Servo


**A Continuous Rotation Servo** can spin around a full circle continuously like a motor. Instead of providing an angular position that the servo should rotate to, the continuous rotation servo simply has a speed and direction, clockwise or counterclockwise.

**Linear Servos** use a rack and pinion gear that converts rotary motion to linear motion. A linear servo works just like a Standard Servo and you can control its postion along a straight line, forward and back in a similar way by giving it a postion.

Pulse width modulation (PWM) sends an electric pulse of variable width to the motor. With PWM there is a minimum pulse, maximum pulse, and a repetition rate. The rotor will turn to the desired position based on the duration of the pulse. When servos are commanded to move, they move to the position and hold the position. A feedback mechansim (usually a potentiometer that rotates with the shaft) adjusts the speed and direction of the motor to be able to hold the correct position.

For our analog servos, the signal or repetition rate is 50Hz, that is once every 20 milliseconds. The duration of the pulses are between 544 and 2400 milliseconds representing 0 and 180 degrees. To derive our 12-bit PWM value, we divide the pulse durations by 20ms and multipy by 4096. That gives us a range of 111 to 491.

Another way to look at this is that with our 12bit ADC, which can measure from 0 to 4095, 4096 (100%) is 20ms pulse length and 0 (0%) is 0ms pulse length. We convert 4095 to 100% since you can't represent the value 4096 in 12 bits.

.. note:: It is a bit difficult finding datasheets for different servos. For the SG90, we have seen a range listed of 1000-2000ms, which maps to 205-410, and 500 to 2400ms, which is 102 to 490. You define these in JMRI, or in the command station in mySetup.h or via command with "<T id SERVO vpin thrownPos closedPos profile>".

.. tip:: Keep a spare slot (we recommend 100) open on your first PCA9685 board so that you can test servo positions with the `<D SERVO ...>` command to connect your servos to and get the exact positions you need.

Servo motors have three wires: power, ground, and signal. The power wire is typically red, and should be connected to the an external 5V power supply. Do NOT connect this to the 5V power of the Arduino! The ground wire is usually black or brown and connects to a ground pin. The signal pin is typically yellow, orange or white and should be connected to a digital pin of the PCA9685.
