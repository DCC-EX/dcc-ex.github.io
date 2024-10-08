.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: Assembly

|EX-CS-LOGO|

****************
Initial Assembly
****************

|conductor| |tinkerer| |engineer| |support-button|

.. sidebar::

   .. contents:: On this page
      :local:
      :depth: 1

|image-note|

This page describes the most common, recommended, configuration, but you will see some breakouts on the right of the page the covers some of the many optional configurations. 

**For this install, you'll need the items listed on the** :doc:`/ex-commandstation/diy/purchasing` **page.**

.. rst-class:: clearer

.. sidebar::  Optional configuration

  |tinkerer| |engineer| |BR| For an Uno, Nano, or other microcontroller, please see :doc:`Using a different microcontroller </reference/hardware/microcontroller-boards>`. 
  
  If you wish to use a different motor controller (for example to have more current to operate more trains and accessories), see :doc:`Motor Controllers </reference/hardware/motor-boards>`

.. figure:: /_static/images/assembly/basic_setup_lg.jpg
   :alt: Command Station Setup
   :width: 500px

   basic setup (click to enlarge picture)

For a video on how to do this, click below: `Setting Up Your Command Station <https://www.youtube.com/watch?v=N6TWR7fIl0A&t=5s>`_

   .. raw:: html
      
      <iframe width="336" height="189" src="https://www.youtube.com/embed/N6TWR7fIl0A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

----

1. Disable Power Sharing - Arduino to Motor Driver
==================================================

**Arduino Motor Shield R3** Only!

.. warning:: 
   :class: warning-float-right
   
   By default, the **Arduino Motor Shield R3** shares its power supply via the pins, with the power supply of the Arduino. *This can supply too much voltage to the Arduino.*
   
   *If you do not cut this trace* or bend out the Vin, you could damage or destroy the Arduino if you apply more than 12V to the motor shield. |BR| In the same way, if you don't bypass Vin and use the 2 power supplies as recommended, they would be connected to each other which could also cause damage.

   Note: This is **not required** if you are using the **EX-MotorShield8874**.

We recommend you use two separate power supplies (or one power supply that can deliver two different voltages). One for the Arduino Mega, and the other for the Motor Controller to power your tracks. 

So **BEFORE YOU BEGIN** It is very important that isolate the power between the two devices.

You will need to turn the motor controller board upside down and do ONE of the following:

- Cut the Vin trace on the bottom of the board. **(Recommended - described below)** |BR| *or*
- Bend out or cut off the Vin Pin

.. rst-class:: clearer

Cutting the Trace
-----------------

**Arduino Motor Shield R3** Only!  This is **not required** if you are using the **EX-MotorShield8874**.

c

   |conductor| |BR| In this *alternate* method, you can just bend the Vin pin so that instead of connecting to the header in the Arduino, it rides on the outside of the header. 

   .. figure:: /_static/images/motorboards/bend_pin1.jpg
      :alt: Bend out the Vin pin on the Arduino motor shield
      :scale: 50%

      Bending out the Pin (click to enlarge)
   
   Another *Alternate* method is to just snip off the pin with wire cutters and make sure that there is not enough pin left to still make contact with the hole it normally would go into when seated on the Arduino.

Cut the trace indicated in the picture with a razor blade or x-acto knife. 2 or 3 firm scratches through the trace should do it. Do not cut too deep. Both a magnifier and an ohmmeter would be helpful here. The little vertical line in between the two solder pads is the scratch mark from where we cut through the little solder trace.

.. figure:: /_static/images/assembly/motor_shield_vin2.jpg
   :alt: Cut Vin trace on Arduino motor shield
   :scale: 80%

   Cutting the Vin trace (click to enlarge)

If you have an ohmmeter, touch your probes to each side of the trace pads and make sure the resistance reading is infinite. In other words, make sure the trace is cut and there is no longer continuity between the two pads on the trace.

2. Connect the Motor Driver
===========================

.. warning:: 
   :class: warning-float-right
   
   It is very easy to misalign the pins and then either have trouble diagnosing problems or damage the board!

   Follow the instructions precisely and you should not have difficulties.

Here are some tips before you start:

* There are power connectors on both boards. They must point in the same direction.
* There are outdented "tabs" on the opposite end of the board. They must point in the same direction.
* The pin numbers on both boards must align (pin 1 goes to pin 1, gnd goes to gnd, etc).
* With the power connectors to your right, align the pins facing you first (pins 0-12, aref, gnd, etc).
* Look at the pins on the motor shield and make sure they are all straight and line up in a neat row.

Place both boards on the table with the power connector end facing in the same direction.

.. figure:: /_static/images/assembly/mega_and_motor_shield.png
   :alt: Align Mega and Motor Shield
   :scale: 100%

   Properly orient the boards

a. Did you remember to cut the trace on the motor shield? |BR| If not, see above. |BR| Otherwise, sight down both rows of pins on the motor board and make sure they are all straight. They should all line up in a row and not be bent in any plane, just like the teeth on a comb. If any look like the photo below, bend them with your fingers and/or needle nose pliers.

.. figure:: /_static/images/assembly/bent_pins.png
   :alt: bent pins
   :scale: 75%

   Bent pins

b. Line up the pins on the side of the board closest to the USB with the header connector on the Mega first. |BR| You want to line up pins 0-7 on the Mega with the same pins on the motor board. |BR| On the other side, IOREF, RESET, 3V3, etc, and A0-A5 need to line up on both boards. |BR| See the picture below and notice the small gap between the two sets of pins to match the two pin header sockets.

.. figure:: /_static/images/assembly/seat1.jpg
   :alt: Line up the pins
   :scale: 75%

   Line up left side first

c. Just align them and start to push them in but don't push them all the way. |BR| Use your fingers to try to push the pins to get them to all go into the holes.

.. figure:: /_static/images/assembly/seat2.jpg
   :alt: Push the pins partway in
   :scale: 75%

   Get all the pins started

d. Do the same on the other side. |BR| Get all the pins aligned and start to press gently to get them into the holes. Notice on this side, you have more holes than you do pins. This is normal.

.. figure:: /_static/images/assembly/seat_reverse1.jpg
   :alt: Line up the other side
   :scale: 75%

   Start the other side

e. Now, being careful to not bend any pins gently press, using a rocking motion if you need to, in order to get the motor board to seat firmly onto the Mega. Press gently until you feel you can't put the pins in any further. Don't force anything.

.. figure:: /_static/images/assembly/seat_press.jpg
   :alt: Press together
   :scale: 75%
   
   Gently press the boards together

.. NOTE:: 
   :class: note-float-right
   
   You may notice that the soldered pins on the underside of the power connector hit the top of the USB connector on the Arduino. 
   
   You can either lift the board slightly, it will still connect properly, or take diagonal cutters and carefully trim the ends of the pins a bit.

f. The boards should be seated. Note the pins are longer than the headers. It is normal for you to see a few millimetres of the pins between the bottom of the motor board and the top of the headers. :ref:`boards-fully-seated` shows the boards as they look properly seated. 

.. figure:: /_static/images/assembly/seated.jpg
   :alt: Fully seated
   :scale: 75%
   :name: boards-fully-seated

   The boards when fully seated

Check your work. Look under and through where the boards connect, make sure no pins missed the holes and got bent so that they run along the outside of the headers.

3. Connect the Motor Driver Power Supply
========================================

**But don't plug it in yet!**

.. warning:: 
   :class: warning-float-right

   Make sure you have cut the trace on the motor control board. If not, see above first. Once you know the trace is cut, connect power to the motor board

Make sure you have a power supply with the correct voltage and current rating. For help on selecting your power supply, please see :doc:`compatible Power Supplies </reference/hardware/power-supplies>`

If you are using a "bench" or metal box type power supply, simply connect the DC output of the power supply to the DC input of the motor shield. Make sure that the positive screw terminal (+) is connected to the positive terminal (Vin) of the motor shield and the negative terminal (- or gnd) is connected to the negative (gnd) terminal of the motor shield.

.. figure:: /_static/images/assembly/motor_power2b.jpg
   :alt: Power in to the Motor Shield
   :scale: 75%

   Power in to the Motor Shield

If you are using a laptop style "brick" power supply or an adapter that plugs into the wall (aka wall wart), use the barrel connector to screw terminal adapter to connect your power supply to the Vin and ground pins on the motor shield. Be careful to use the correct polarity. Make sure the positive terminal on the screw terminal adapter connects to the positive (+) on the motor shield and the negative terminal (- or gnd) connects to the negative terminal.

.. figure:: /_static/images/assembly/motor_power3.jpg
   :alt: Screw Terminal Adapter Power
   :scale: 75%

   Screw Terminal Adapter to Motor Shield

If you don't have a screw terminal adapter, you can cut the end off your power supply and strip the wires. The outer wire braid is usually the negative connection and the centre wire is the positive connection. Check the wiring image on the power supply itself.

4. Connect the Power Wires to the Tracks
========================================

**But don't plug it in yet!**

.. sidebar:: **EX-MotorShield8874**

   For the **EX-MotorShield8874** the output are reversed.  ``A`` is furthest from the barrel connector. ``B`` is closest to the barrel connector.

There are two sets of output connectors on the motor shield, ``A`` and ``B``. A is the Main or Operations (also called 'Ops') track while ``B`` is the Programming or Service track. Connect twisted pair wire of the proper gauge to each track. 

Polarity (which wire is connected to which side of the track) is not not important here if you are using separate, completely isolated piece of track for PROG. *However* if you will be using a siding track that connects to your main track, make sure that the *connections for both tracks match*. 

In other words, if you view one side of your main track as having a 'left' side and a 'right' side, and connect positive output A to the left side, connect the positive from the B side to the left side of the programming track. In electrical terms, we want both tracks to be "in phase" with each other. Here is the diagram from above repeated again for reference.

.. figure:: /_static/images/assembly/motor_power2b.jpg
   :alt: Main and Prog Out to track
   :scale: 75%

   Out to Main and Program tracks

5. Connect the Arduino Power Supply
===================================

.. sidebar:: Arduino Power supply options

   |conductor| |BR| There are different ways to power your Arduino. You may be able to avoid having a second power supply if you will always have a computer connected to your |EX-CS| (for example to run |EX-WT| or |JMRI|. There is also a way to use a 5V power supply. Please read :doc:`Power Supplies </reference/hardware/power-supplies>` to help you find what will work best for you).

Connect the 2.5mm barrel connector from your separate 7-9V DC power supply to the barrel connector on the Arduino. 

If you have a power supply with bare wires, you can bypass the barrel connector and connect your power supply to the ``Vin`` and ``Gnd`` pins on the Arduino.

.. rst-class:: clearer

Next Steps - Install the WiFi board
===================================

.. sidebar:: 
   :class: sidebar-float-right

   |conductor| |BR| You can *alternately* connect a controller like |JMRI| or our |EX-WT| by using the serial cable to connect between your computer and the |EX-CS|. If so, skip to :doc:`/ex-commandstation/installer`.

Click :doc:`here </ex-commandstation/diy/wifi-setup>` or click the "next" button to learn how to connect the WiFi shield to your |EX-CS|.

..
   1. Load firmware on your Command Station

   Keep your USB cable handy because we are going to need it in this step.

   Go to the :doc:`Command Station downloads </download/ex-commandstation>` page. Most users will want to use the installer.

   ----

   Locos Can't Respond to Throttle Commands on the Programming Track!

   We have repeated this in several places on the Website because it is such a common issue. The MAIN track is for running trains, the PROG (service track) is for programming your loco. **THE LOCO CANNOT RESPOND TO THROTTLE OR FUNCTION COMMANDS WHILE ON THE PROG TRACK** This is by design and part of the NMRA specification. There is such a thing as "Programming on Main", where you can adjust things like sounds, throttle curves, speed matching, etc, but you can't get acknowledgment back from the loco on the main track. That is usually fine because you will know if a setting like a sound change "took" or not. We will have a section on programming on main. ***TODO: Write the POM*** help.

|force-break|

.. note::

   **TECHNICAL NOTES**

   **Wire Gauge** - The Arduino motor controller can only provide about 1.5 Amps of power (despite being rated for 2A), so 18 AWG wire is ample. If you use a different motor controller and deliver more current to your track, you may need thicker wire (lower number gauge).

   See the :doc:`/reference/hardware/wire-gauge` page for more information on wire gauges.

   **Power Supplies** - Why do we recommend a 7-9V power supply for the Mega when the manual says it can handle 12V or even 20V? Can't you just use one 12V power supply to power both of them? Short answer; NO. You want two supplies (or one supply that splits out 2 voltages). The Arduino Mega only needs around 7V to operate. Any voltage over that is wasted as heat and can burn out the regulator on the board. And most people want a minimum of 12V into the Motor Board, while many want 14V (for N and HO Scale). Where your Mega could run hot for a while with 12V, if 14V from the Motorboard was connected to the Mega, it would destroy it. Cut the trace and use 2 power supplies.

   **Using a 5V Supply** - There is one more option for powering the Mega. If you have a 5V DC regulated power supply, you can bypass the barrel connector and the regulator and connect it directly to the 5V and Gnd pins on the Arduino. Do NOT connect anything to the barrel connector if you do this! You would still need to cut the Vin trace on the Motor Shield and use your separate power supply that plugs into the shield. For more information, see :doc:`Power Supplies </reference/hardware/power-supplies>`
