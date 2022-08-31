.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-R-LOGO|

**************
Adding Objects
**************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

First we need the 'objects' that we will use for our automation sequences.

There are a number key objects that are important for creating sequences:

* `Roster Entries - Your locos <Adding a Roster>`_
* `Turnouts/Points <Adding Turnouts/Points>`_
* `Servos for Semophores/Signals and Animations <Servos for Signals and Animations>`_
* `Sensors <Sensors>`_
* `Signals (Lights) <Signals>`_

The process for creating these objects consists of:

* Adding the hardware (not strictly applicable to the roster)
* Configuring |EX-CS| by modifying 'myAutomation.h' so that it knows about the object
* Re-uploading the software to the |EX-CS|

----

Adding a Roster
===============

EX-RAIL has a ``ROSTER()`` function to allow you to define all of your locomotives with a list of their defined functions which is advertised to WiThrottle applications, just like turnouts/points and routes.

The functions can simply be listed as "F" numbers, or you can provide a text description of the function. Prefacing the function with a "*" indicates it is momentary, meaning it is only activated while holding that function button down.

In a text editor (e.g. notepad) create a new text file named 'myAutomation.h'. (Note the capital 'A' in the name.  The case of all the characters is important.)

If you are already using |EX-R| and have a myAutomation.h, then just the add ``ROSTER(...)`` lines near the top of the file.

Add a line that looks like:

.. code-block:: cpp
   
   ROSTER(999,"Loco Name","F0/F1/*F2/F3/F4/F5/F6/F7/F8")

Where:

* **999** - is the DCC address of your loco
* **My Loco Name** - is anything you want to see as the name of this loco in the throttle apps
* **F0 F1 F3 ... F27**. - are the names that you want to see for the functions specific to this loco
* **\*F2** - note that if the function is 'momentary' rather than 'latching' (On/Off) then start the function label with a asterisk (\*).  The most common example of this is the Horn/Whistle which is commonly on F2.

Some more realistic examples might look like:

.. code-block:: cpp
   
   ROSTER (  3,"Eng 3", "F0/F1/*F2/*F3/F4/F5/F6/F7/Mute/F9//") // Address 3, Eng 3, Function keys F0-F10
   ROSTER(1224,"PE 1224","") // Motor Only Decoder, But use Engine Driver 'Preferences >In Phone Loco 'Sound'
   ROSTER(1225,"PE 1225","Lights/Bell/*Whistle/*Short Whistle/Steam/On-Time/FX6 Bell Whistle/Dim Light/Mute")
   ROSTER(4468,"LNER 4468","//Snd On/*Whistle/*Whistle2/Brake/F5 Drain/Coal Shvl/Guard-Squeal/Loaded/Coastng/Injector/Shunt-Door ~Opn-Cls/Couplng/BrakeVlv/Sfty Vlv/Shunting/BrkSql Off/No Momentm/Aux3/Fade Out/F22 Res/F23/Res//Aux 5/Aux6/Aux7/Aux 8")

Note: Add additional 'ROSTER(...)' lines for all your locos

.. code-block:: cpp
   
   ROSTER(1506, "HUSA", "Light/Bell/*Horn")

A more complex example with generic functions for the same loco (note the momentary F2 for horn):

.. code-block:: cpp

   ROSTER(1506, "HUSA", "F0/F1/*F2/F3/F4/F5/F6/F7/F8/F9/F10/F11/F12/F13/F14/F15/F16/F17/F18/F19/F20/F21/F22/F23/F24/F25/F26/F27/F28")

The same again, with more text functions defined to represent a number of different sounds:

.. code-block:: cpp

   ROSTER(1506, "HUSA", "Lights/Bell/*Horn/Air/Brake/Coupling/Compressor/Sand/Mute/F9/F10/F11/F12/F13/F14/F15/F16/F17/F18/F19/F20/F21/F22/F23/F24/F25/F26/F27/F28")

**Locos with Unavailable Functions**

   If a function is not available just leave the spot empty. (Don't even have the space character.)

   For example: 

   .. code-block:: cpp

      ROSTER(2825,"CN ES44AC","Headlight/Bell/*Horn/Coupler/Dynamic Brake///Flange Squeal/Startup & Shutdown")

   Note the two missing text labels for positions F5 and F6. Engine Driver will skip those buttons and not display them at all in the interface since they do nothing for that loco.

   Example of loco without sound:

   .. code-block:: cpp

      ROSTER(2405,"AT&SF 2-8-0 2405","Headlight")

   Note that it only has FO (the Headlight) and not following slashes.

----

Adding Turnouts/Points
======================

Turnouts/Points can included on your layout in one of the

* DCC turnouts/Points
* Servo Turnouts/Points
* Pin turnouts/Points

DCC Turnouts/Points
-------------------

Adding the Hardware -  DCC Turnouts/Points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: DCC Turnouts/points

Configure myAutomation.h - DCC Turnouts/Points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pin Turnouts/Points
-------------------

Adding the Hardware -  Pin Turnouts/Points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: DCC Turnouts/points

Configure myAutomation.h - Pin Turnouts/Points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Servo Turnouts/Points
---------------------

Adding the Hardware -  Servo Turnouts/Points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. sidebar::
  
  You can also refer to :doc:`/reference/hardware/servo-module` for more information.

To connect a servo to |EX-CS|, you first need to get a module, based on the PCA9685 chip.

.. image:: /_static/images/i2c/pca9685.jpg
   :alt: PCA9685 Servo Module
   :scale: 40%

These are widely available from eBay, Amazon, etc. for a few dollars.

Note the pin connectors along the left side of the module - these are where you connect to the Arduino.  

The 16 columns of three pins along the bottom of the module are where you connect the servos. The pins are arranged so that you can just plug a servo connector directly onto them, but be sure that the wire colours match the colours of the pins, i.e. yellow to yellow, red to red and black to black.

The servo module itself is powered from the Arduino, but the servos themselves contain motors that consume more current than the Arduino is able to supply, and so a separate 5V supply is required for the servos.  This is connected to the green terminal block at the top of the module, with terminals labelled V+ and GND. The V+ terminal is connected to 5V and the GND to the 0V (ground) wire of the supply.

Connections to the Arduino are made with four jumper wires (+5V power and GND, and SCL and SDA), as shown on the following diagram:

.. image:: /_static/images/i2c/ArduinoMegaServo.png
   :alt: PCA9685 Servo Module
   :scale: 30%

In |EX-CS|, the drivers for the PCA9685 module is already installed, and made available to for use as pin numbers 100-115. A servo is shown in the diagram, connected to the first set of pins on the module.  This will be accessed using pin number 100.

Once you've made all of the connections, apply power to the Arduino.

Then, in the Serial Monitor, enter the command `<D SERVO 100 450>`.  The servo should move, as long as it isn't (by some fluke) already in that position.

Enter `<D SERVO 100 110>` and this time it should definitely move.  For the last parameter (servo position) you can use any value between about 105 and 490.

Try `<D SERVO 100 450 3>` and the servo should move slowly back.

You can use the servo to control turnouts, semaphore signals, engine shed doors, and other layout components, to make your layout more dynamic and exciting.  In the picture below, you can see a servo mounted below the baseboard with a piece of wire passing through a slot cut in the baseboard, to operate a turnout.

.. image:: /_static/images/i2c/TurnoutServoMount.jpg
   :alt: Servo mount to operate a turnout
   :scale: 60%

And in the next picture you can see a servo that operates a semaphore signal.  The signal, and its servo mounting bracket, were 3d-printed on a Creality Ender-3 printer.

.. image:: /_static/images/i2c/SemaphoreSignal.jpg
   :alt: Servo mount to operate a Semaphore Signal
   :scale: 60%


Configure myAutomation.h - Servo Turnouts/Points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The myAutomation.h file needs to be altered so that the |EX-CS| knows about each Turnout/Point.

EX-RAIL supports three methods of controlling servos:

* Turnouts via the SERVO_TURNOUT directive
* Signals via the SERVO_SIGNAL directive
* Animations via the SERVO or SERVO2 directives

Controlling Servos for Turnouts/Points
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SERVO_TURNOUT directive defines a servo based turnout in EX-RAIL, which will appear in |WiThrottle Protocol| apps, |Engine Driver|, and |JMRI| in addition to being defined as a turnout within the CommandStation.

As per the |EX-R| reference, turnouts are defined with the following syntax:

.. code-block:: cpp

   // Example
   SERVO_TURNOUT(id, pin, active_angle, inactive_angle, profile [, "description"])


.. code-block:: cpp
   :class: code-block-float-right

   // Example
   SERVO_TURNOUT(200, 101, 450, 110, Slow, "Example slow turnout definition")

   /* An example definition for a servo connected to the second control pins of the first PCA9685 connected to the CommandStation, using the slow profile for prototypical operation: */The valid parameters are:

- id = Unique ID within the CommandStation (note these are shared across turnouts, sensors, and outputs).
- pin = The ID of the pin the servo is connected to, which would typically be the VPin ID of the PCA9685 controller board.
- active_angle = The angle to which the servo will move when the turnout is thrown (refer below for further detailed information).
- inactive_angle = The angle to which the servo will move when the turnout is closed (refer below for further detailed information).
- profile = There are five profiles to choose from that determine the speed at which a turnout will move: Instant, Fast, Medium, Slow, and Bounce (note we don't recommend Bounce for a turnout definition).
- description = A human-friendly description of the turnout that will appear in WiThrottle apps and |Engine Driver|. Note that this must be enclosed in quotes "".


----

Servos for Signals and Animations
=================================

See above for information on installing the servo hardware (it is the same as for a turnout/point).

Configure myAutomation.h - Servos for Signals an Animations
-----------------------------------------------------------

The myAutomation.h file needs to be altered so that the |EX-CS| knows about each Turnout/Point.

EX-RAIL supports three methods of controlling servos:

* Turnouts via the SERVO_TURNOUT directive
* Signals via the SERVO_SIGNAL directive
* Animations via the SERVO or SERVO2 directives


Servos for Signals
^^^^^^^^^^^^^^^^^^

The SERVO_SIGNAL directive defines a servo based signal in EX-RAIL to drive semaphore type signals as part of sequences or routes, or simply be set via a signal or similar.

Similar to pin based signals, servo signals are controlled by the ID of the red pin only.

Unlike servo based turnouts, there is no ID or description (they don't appear in throttles), and they use the "Bounce" profile with no other options available at the present time:

.. code-block:: 

   SERVO_SIGNAL(vpin, redpos, amberpos, greenpos)

.. code-block:: cpp
   :class: code-block-float-right

   // Example
   SERVO_SIGNAL(102, 400, 250, 100)

   /* A simple example using the third control pins of the first
   PCA9685 connected to the CommandStation would be: */

- **vpin** = The ID of the pin the servo is connected to, which would typically be the VPin ID of the PCA9685 controller board.
- **redpos** = The angle to which the servo will move to for the red position.
- **amberpos** = The angle to which the servo will move to for the amber position.
- **greenpos** = The angle to which the servo will move to for the green position.


Servos for Animations
^^^^^^^^^^^^^^^^^^^^^

The SERVO and SERVO2 directives allow for servos to be used in various automations within |EX-R|.

Note that unlike a SERVO_TURNOUT these are not definitions that appear within WiThrottle apps, |Engine Driver|, or |JMRI|, but are instead actions designed to be used within |EX-R| automations.

As per the |EX-R| reference, these are defined with the following syntax:

.. code-block:: cpp

   SERVO(vpin, position, profile)
   SERVO2(vpin, position, duration)

The valid parameters are:

- **vpin** = The ID of the pin the servo is connected to, which would typically be the VPin ID of the PCA9685 controller board.
- **position** = The angle to which the servo will move when the turnout is thrown (refer below for further detailed information).
- **profile** = There are five profiles to choose from that determine the speed at which a servo will move: Instant, Fast, Medium, Slow, and Bounce.
- **duration** = The time (in milliseconds (ms)) for the servo to be actively rotating.

.. code-block:: cpp
   :class: code-block-float-right

   // Example
   AT(164)
   SERVO(101, 400, Fast)
   DONE

   AFTER(164)
   SERVO(101, 100, Slow)
   DONE

   /* As an example, consider a lineside worker that needs to be moved away 
   from the track when a train approaches, which is controlled by an infrared 
   sensor.
   The SERVO is attached to VPin 101 (second control pin on first PCA9685), 
   with a sensor attached to VPin 164 (first pin on the first MCP23017):
   This tells EX-RAIL that when the sensor at VPin 164 is activated, the 
   lineside worker moves quickly back from the track for safety, and then 
   after the sensor has been deactivated, he can leisurely move back to his 
   working position (no one wants to rush back to work right?). */

----

Adding Sensors
==============

Adding the Hardware -  Sensors
------------------------------

.. todo:: MEDIUM - Stage 2 - Adding a Sensor - needs to be extended

.. sidebar:: 

  Alternate is to use a :doc:`/reference/hardware/gpio-module`

On the Mega2560 Processor board: 

Place IR Infrared or Optical sensors Output wire on Dpins 22, 23, 24 ... 62. One wire to Gnd and for the IR sensor a third wire to 5v pin.

Configure myAutomation.h - Sensors
----------------------------------

You don't actually require anything special to be added to myAutomation.h in advance of using them in an sequence.

Handling sensors in sequences is made easy because |EX-R| throws away the concept of interrupts (“oh… sensor 5 has been detected… which loco was that and whatever do I do now?”) and instead has the sequences work on the basis of “do nothing, maintain speed until sensor 5 triggers, and then carry on in the script”.

Sensor numbers are direct references to VPINs (virtual pin numbers) in the Hardware Abstraction Layer. For a Mega onboard GPIO pin, this is the same as the digital pin number. Other pin ranges refer to I/O expanders etc. 

.. note:: 
   :class: note-float-right
   
   Hall effect sensors work for some layouts, but beware of how you detect the back end of a train approaching the buffers in a siding, or knowing when the last car has cleared a crossing.

|EX-CS| allows for sensors that are **Active Low or Active High**. This is particularly important for IR sensors that have been converted to detect by broken beam, rather than reflection. By making the sensor number negative, the sensor state is inverted. e.g. ``AT(-5)``.

Sensors with ID's 0 to 255 may be LATCHED/UNLATCHED in your script. If a sensor is latched on by the script, it can only be set off by the script… so ``AT(5) LATCH(5)`` for example effectively latches the sensor 5 on when detected once.

Sensor polling by JMRI is independent of this, and may continue if ``<S>`` commands are used.


----

Adding Signals
==============

Adding the Hardware - Signals
------------------------------

To connect a servo to |EX-CS|, you first need to get a module, based on the PCA9685 chip.

.. image:: /_static/images/i2c/pca9685.jpg
   :alt: PCA9685 Servo Module
   :scale: 40%

These are widely available from eBay, Amazon, etc. for a few dollars.

Note the pin connectors along the left side of the module - these are where you connect to the Arduino.  

The 16 columns of three pins along the bottom of the module are where you connect the LEDs.

In |EX-CS|, the drivers for the PCA9685 module is already installed, and made available to for use as pin numbers 100-115.

On the PCA9685 Servo Signal Board:

* Connect individual LEDs on vpins 101, 102 ... 115 as needed
* Only use the -Gnd and Output+ vpins, NOT the center 5v pin

Configure myAutomation.h - Signals
----------------------------------

The myAutomation.h file needs to be altered so that the |EX-CS| knows about each Signal.

Signals setup on vpins 101, 102 ... 115

For each signal add a line in myAutomation.h in the form:

SIGNAL(red_pin, amber_pin, green_pin) 

.. code-block:: 

    // always use the first red_pin as the signal_id for All signal color changes)
    SIGNAL(106, 0, 107) // Red, Amber, Green For turnout 1

Combine the two commands Servo_Turnout and Signal (New 4.1:)

New 4.1 SERVO_SIGNAL(vpin, redpos, amberpos, greenpos)

.. code-block:: 

    // Use the first Red vpin# as the signal_id for All Signal color changes
    // Use this to Combine the two commands Servo_Turnout and Signal above into One Function 
    SERVO_SIGNAL(106, 400, 0, 205) //  Red vpin 106 for Turnout 1, Thrown=Red, Close = Green


----

Next Steps - Creating Sequences
===============================

   
Click :doc:`here <getting-started>` or click the "next" button to learn how to create automation sequences.