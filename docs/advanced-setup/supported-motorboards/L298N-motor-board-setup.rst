************************
L298N Motor Board Setup
************************

.. image:: ../../_static/images/tinkerer.png
   :alt: Tinkerer Icon
   :scale: 50%
   :align: left

Tinkerer Level

|

The L298N Motor board is the same H-Bridge on the Arduino Motor Shield. Here are the key differences:

* It is in a much smaller form factor
* It isn't a shield so you have to jumper wires to connect it to your CS
* It doesn't have current sense, so you are going to have to use one of the solutions below
* It stands vertically on the board with a big heat sink for better controlling

.. figure:: ../../_static/images/motorboards/l298_board2.jpg
  :alt: L298N Motor Board
  :scale: 25%

  L298N Motor Board

When is the L298N a Good Option?
===================================

You may wonder why one would go through the trouble of using this board when the Arduino / Deek-Robot Motor Shield already has what we need and is a recommended option. The answer is you may want to use this board because:

* You already have one in your parts box
* They are dirt cheap
* You are not using an Arduino for your Command Station and a shield is unwieldy
* You want something smaller
* You are going to use the L298N for programming and something with more current for MAIN

The disadvantage of this board:

* It does not come with current sense. You will need to add it.


L298N for MAIN and PROG with Current Sense
=============================================

You will need to have currense sense in order to program locos on the programming (service) track. In addition, current sense is necessary to provide short-circuit detection for each track. There are two methods to add current sensing to this board, the first method requires cutting two leads on the IC and soldering in current sense resistors. The other method is to use an external current sense board to measure the current going into the board.

Method 1: Adding Current Sense Resistors
------------------------------------------

This is easier than it sounds and takes about 15 minutes. To do this yourself, you will need:

* 2 One Ohm, 3 Watt Power Resistors
* small wire cutters
* soldering iron and solder
* 18 Guage hookup wire
* 2 Male to Male Arduino jumper wires (dupont connectors)

.. Note:: If you will only be using this board for the programming track and another board like the IBT_2 for your MAIN track, you only need one resistor and can follow the instructions for just the B side of the procedure.

You will need to unsolder the current sense (CS) pins on the L298N chip that are connected to ground and insert a resistor between the lifted leg and ground on each side. Here is how:

1. Remove all jumpers, there are 3!

2. Unsolder the A and B current sense legs on the L298N chip at the green circles being careful to lift them out without breaking them. Pin 1 to the left is output CS A for MAIN. Pin 15 to the right is CS output B for PROG.

.. figure:: ../../_static/images/motorboards/l298_board4.jpg
  :alt: L298N Motor Driver Pinout
  :scale: 50%

1. Lift each leg and bend them carfully upward to provide space for a resistor.

2. Cut one wire lead of the 1 Ohm resistor short, but long enough that you can solder that end into the hole left by unsoldering the CS leg, about 1/4" (6mm). This connects one end of the resistor to ground. Solder the resistor from the bottom leaving air space for cooling. Repeat on the other side.

3. Solder the CS leg of the chip you unsoldered to the top of the resistor. You should be able to carefully bend the leg to meet the top resistor lead as the resistor stands vertically. You are basically inserting a resistor into the space where you cut the leg of the chip. Solder the wire fairly close to the end of the resistor. Repeat on the other side. Do not trim the top resistor lead yet.

4. Measure a jumper wire long enough to connect to the top of resistor A and reach over push into pin A0 on the Arduino. Solder one end of the jumper to the top of resistor A above where you soldered the chip's CS leg. Trim off any remaining resistor lead to remove any sharp points. Repeat for the resistor on side B making sure the male dupont end of the jumper can reach pin A1 on the Arduino.

5. If you haven't already, plug the male end of the A jumper into pin A0 on the Arduino and the male end of the B jumper to pin A1 on the Arduino.

6. Configure the board in your Command Station in the next step.

Configuring the Board in DCC++EX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You have two choices regarding how to wire and configure the L298N motor driver board to the command station. Unlike the Arduino Motor Shield, this board has separate direction inputs which is where we apply the DCC signal. 

Your first choice, the easy way, is to create a new motor board definition that uses the proper pins. This requires you to edit the config.h file, cut and paste the motor board definition below, upload the sketch with the new settings, and connect wires from the L298N board to the correct pins on the Arduino. The only disadvantage to this method is that is uses an extra pin (though there are plenty of spare pins on a Mega), and it uses the standard accuracy waveform. Standard accuracy is fine for almost all cases, but you can read more on the :doc:`High Accuracy Waveform Mode</advanced-setup/high-accuracy>`

Your second choice is to make a small inverter circuit (using 1 FET, IC, or transistor) to connect to the standard signal pin on the Command Station, and split it into two signals connect to the two pins on the L298N board. The advantage of this method is you use just one pin and get the high accuracy DCC waveform. The downside is that you have to solder together a circuit with 2 or 3 parts.


Using 2 signal pins
~~~~~~~~~~~~~~~~~~~~~~~

This method uses 2 pins on the Arduino for signal pins and requires the following custom motor board definition. It uses the standard accuracy DCC waveform.

To wire the board, connect the pins as follows:

.. table:: 2 Signal Pin Wiring diagram

    +---------------+-----------------------------+
    |  Arduino      |           L298N             |
    +===============+=============================+
    | 2 (enable A)  | ENA                         |
    +---------------+-----------------------------+
    | 4 (signal A1) | IN4                         |
    +---------------+-----------------------------+
    | 6 (signal A2) | IN3                         |
    +---------------+-----------------------------+
    | A0 (CS MAIN)  | CS A                        |
    +---------------+-----------------------------+
    | 3 (enable B)  | ENB                         |
    +---------------+-----------------------------+
    | 5 (signal B1) | IN2                         |
    +---------------+-----------------------------+
    | 7 (signal B2) | IN1                         |
    +---------------+-----------------------------+
    | A1 (CS PROG)  | CS B                        |
    +---------------+-----------------------------+
    |     5V        |   Vcc  (+5V from Arduino)   |
    +---------------+-----------------------------+
    |     GND       |    GND                      |
    +---------------+-----------------------------+

.. figure:: ../../_static/images/motorboards/l298n_pinout.png
  :alt: L298N Motor Driver Pinout
  :scale: 25%

  L298N Motor Driver Pinout

Once wired correctly, edit the config.h file and replace the following line:

.. code:: none
   
   #define MOTOR_SHIELD_TYPE STANDARD_MOTOR_SHIELD

with this:

.. code:: none
   
   #define MY_L298N_BOARD F("MY_L298N_BOARD"),\
      new MotorDriver(2, 4, 6, UNUSED_PIN, A0, 4.88, 2000, UNUSED_PIN), \
      new MotorDriver(3, 5, 7, UNUSED_PIN, A1, 4.88, 2000, UNUSED_PIN)

      #define MOTOR_SHIELD_TYPE MY_L298N_BOARD

Save the file and then upload the entire sketch into the Command Station using the Arduino IDE as explained in :doc:`Installing Using the Arduino IDE</get-started/arduino-ide>`


Using One Signal Pin With an Inverter circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This method uses 1 pin on the Arduino and the standard motorboard definition. It uses the high accuracy DCC waveform.

Make the following Inverter circuit

.. todo:: finish

Then wire the L298N to the Arduino with jumper wires according to the following table:

13
12
A0
11
13
A1

To wire the board, connect the pins as follows:

.. table:: 1 Signal Pin Wiring diagram

    +---------------+-----------------------------+
    |  Arduino      |           L298N             |
    +===============+=============================+
    | 3 (enable A)  | ENA                         |
    +---------------+-----------------------------+
    | 12 (signal A1)| IN4                         |
    +---------------+-----------------------------+
    | Inverter A    | IN3                         |
    +---------------+-----------------------------+
    | A0 (CS MAIN)  | CS A                        |
    +---------------+-----------------------------+
    | 11 (enable B) | ENB                         |
    +---------------+-----------------------------+
    | 13 (signal B1)| IN2                         |
    +---------------+-----------------------------+
    | Inverter B    | IN1                         |
    +---------------+-----------------------------+
    | A1 (CS PROG)  | CS B                        |
    +---------------+-----------------------------+
    |     5V        |   Vcc  (+5V from Arduino)   |
    +---------------+-----------------------------+
    |     GND       |    GND                      |
    +---------------+-----------------------------+

Once wired correctly, edit the config.h file and replace the following line:

.. code:: none
   
   #define MOTOR_SHIELD_TYPE STANDARD_MOTOR_SHIELD

with this:

.. code:: none
   
   #define MY_L298N_BOARD F("MY_L298N_BOARD"),\
      new MotorDriver(3, 12, UNUSED_PIN, UNUSED_PIN, A0, 4.88, 2000, UNUSED_PIN), \
      new MotorDriver(11, 13, UNUSED_PIN, UNUSED_PIN, A1, 4.88, 2000, UNUSED_PIN)

      #define MOTOR_SHIELD_TYPE MY_L298N_BOARD

Save the file and then upload the entire sketch into the Command Station using the Arduino IDE as explained in :doc:`Installing Using the Arduino IDE</get-started/arduino-ide>`


Method 2: Using An External Current Sense Board
-------------------------------------------------

Coming Soon

.. todo:: finish this

L298N for PROG and High Current IBT_2 for MAIN
================================================





   