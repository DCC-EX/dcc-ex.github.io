IB_2 BTS7960 Motor Board
======================================

What You Will Need (for IBT_2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
An Arduino Mega or clone (or an Uno if you don't need WiFi or Ethernet)
An Arduino Motor Shield
An IBT_2 Motor Board
Version 3.0.1 of the DCC++ EX Command Station Software
A 1 Ohm 1/4 Watt resistor
Some Jumper Wires

We can assume that many of you may have started off with the Arduino Mega with Arduino Motor Shield (or clones) and are here because you are making the step up to something that can handle more current, and therefore more locos. We will cover how to "upgrade" with just one IBT_2 board to run your MAIN track and relegate your Arduino Motor Shield to the PROG track as well as explain other options.

.. Note:: We can't say it enough, this board can pump out some Amps. Be careful! Put fuses on the connection to each rail and limit the current to a safe level in your config.h file. We have a saying at DCC-EX, if you need more than 5 Amps to run locos, then you need to add power districts, not more Amps.

Upgrading and Using the Arduino Motor Shield
---------------------------------------------

For this installation we are going to assume you already have a working CS or at least have a the parts you need as listed above.

If you need instructions on how to install the Arduino Motor Shield, see ` Arduino Motor Shield Assembly <../assembly.html>`_

What We Are Going To Do
^^^^^^^^^^^^^^^^^^^^^^^^

* Use just 1 output of your existing Arduino Motor Shield for your program track with no hardware changes
* Add an IBT_2 (BTS7960) Motor Board to replace the "A" output to power your MAIN track
* Move a few wires and connect a few jumpers to your IBT_2
* Add a current sense resistor to the IBT_2
* Change your motor board type in your config.h file

Steps 
^^^^^^^

Make sure all power supplies are disconnected from your Arduino, The Motor Shield, and the IBT_2

Disconect the wires coming out of output A of the Arduino Motor Board that connect to your MAIN track.

Connect those two wires coming from the MAIN track to the B+ and B- Screw terminals. If using power districts or wanting to connect the main and prog tracks together when prog is not in use, keep the polarity of the rails the same with reference to each other. In other words, if you connect + to the left rail, then always keep + on the rail to the left as a train would sit on the track. We need to keep the phase of the DCC signal in sync between power districts and reversing sections.

Connect or solder a resistor (see alternate method using a current sense board below) to XXX

Use the following table to connect pins from the Arduino Mega to the IBT_2

**insert table here**

Connect pin X on Mega to pin Y on IBT_2
Connect pin A on Mega to pin B on IBT_2
Connect current sense resistor to pin A5 on the Arduino Motor Shield

It shoud look like this:

**insert friting diagram here**

.. Note:: We are going to edit your config.h file. If this is your first time using the Command Station software and do not have a config.h file, rename your config.example.h file to config.hardware

Launch the Arduino IDE (or whatever editor you use) and open the CommandStation-EX project. Find the config.h file. look for the following lines of code:

``// DEFINE MOTOR_SHIELD_TYPE BELOW ACCORDING TO THE FOLLOWING TABLE:
//
//  STANDARD_MOTOR_SHIELD : Arduino Motor shield Rev3 based on the L298 with 18V 2A per channel
//  POLOLU_MOTOR_SHIELD   : Pololu MC33926 Motor Driver (not recommended for prog track)
//  FUNDUMOTO_SHIELD      : Fundumoto Shield, no current sensing (not recommended, no short protection)
//  IBT_2_WITH_ARDUINO    : IBT_2 Motor Board on MAIN and Arduino Motor Shield on PROG
//  FIREBOX_MK1           : The Firebox MK1                    
//  FIREBOX_MK1S          : The Firebox MK1S   
//   |
//   +-----------------------v
//
#define MOTOR_SHIELD_TYPE STANDARD_MOTOR_SHIELD``

Change the last line to look like this. To be sure of your spelling, you can copy and past IBT_2_WITH_ARDUINO and replace STANDARD_MOTOR_SHIELD

``#define MOTOR_SHIELD_TYPE IBT_2_WITH_ARDUINO``

Upload the sketch to your arduino. If you need help on how to upload a sketch, see 


**tech notes**
add notes here showing what pins are in the motordrivers section and what the pins are on the motor boards. Also show the motor board section. Show how they can chage the pins if there is a problem by creating a new motor board type.







