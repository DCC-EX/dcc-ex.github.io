.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-R-LOGO|

********************
Creating Sequences
********************

|tinkerer| |conductor|

.. sidebar:: 

   .. contents:: On this page
      :depth: 4
      :local:

This page is a limited introduction to the |EX-R| automation sequences.  For more comprehensive information refer to the :doc:`/ex-rail/EX-RAIL-reference` and :doc:`/ex-rail/EX-RAIL-summary` pages.

----

myAutomation.h - Editing Your Sequences
=======================================

The script containing all your sequences is added to your Command Station by creating a file called "myAutomation.h" in the same folder as CommandStation-EX.ino.

Connecting your Arduino and pressing the :guilabel:`Upload` button in the usual way will save the file and upload your script into the Command Station.

You can create and edit the myAutomation.h using a text editor (like Notepad), but if you are using the Arduino IDE (rather than the |EX-I|) you can create the myAutomation.h file in the Arduino IDE. Use the pulldown button and select New Tab (or simply press Ctrl+Shift+N).

.. image:: /_static/images/ex-rail/setup1.jpg
   :alt:  Setup pulldown button
   :align: center
   :scale: 100%
   :target: #myautomation-h-editing-your-sequences

.. image:: /_static/images/ex-rail/setup2.jpg
   :alt:  Setup pulldown menu
   :align: center
   :scale: 100%
   :target: #myautomation-h-editing-your-sequences

Enter the file name "myAutomation.h" (This is case sensitive)

.. image:: /_static/images/ex-rail/setup3.jpg
   :alt:  Setup myAutomation.h
   :align: center
   :scale: 100%
   :target: #myautomation-h-editing-your-sequences

And type your script in.

.. image:: /_static/images/ex-rail/setup4.jpg
   :alt:  Setup Example file
   :align: center
   :scale: 100%
   :target: #

|

Comments in in myAutomation.h
-----------------------------

You can add comments (text that does nothing) to myAutomation.h in two ways:

* If ``//`` occurs in the line, everything after that (including the slashes) is ignored.  i.e. a 'Comment'
* If a line starts with ``/*`` then everything, including all subsequent lines an including the '/*') is ignored until a ``*/`` is found.  i.e. a 'Comment'

----

The Automation Process
======================

Once started, each 'sequence' will step through a list of simple keyword commands until they reach a ``DONE`` keyword.

Multiple concurrent sequences are supported.

For a full list of keywords, see :doc:`EX-RAIL-summary`, and for further detailed information, see the :doc:`/ex-rail/EX-RAIL-reference`.

----

Before You Start - Adding Objects
==================================

Generally you will need to have created some Key Objects before you start writing sequences.

.. code-block:: cpp
   :class: code-block-float-right

   // Example
   ROSTER(1225,"PE 1225","Lights/Bell/*Whistle/*Short Whistle/Steam/On-Time/FX6 Bell Whistle/Dim Light/Mute")
   SERVO_TURNOUT(200, 101, 450, 110, Slow, "Example slow turnout definition")
   SERVO_SIGNAL(102, 400, 250, 100)

Refer to the :doc:`creating-elements` for creating and adding those Objects:

* Roster Entries
* Turnouts/Points
* Sensors
* Signals

Note that these Objects don't have to be added before the sequence in which you use it.

----

Structure of a Sequence
=======================

In general, sequences follow the basic structure:

.. code-block:: cpp
   :class: code-block-float-right

   // Example
   ROUTE(1,"Coal Yard exit")
      RED(77)      // signal 77 to Red
      THROW(1)     // throw turnout/point 1
      CLOSE(7)     // close turnout/point 7
      DELAY(5000)  // 5 second wait
      GREEN(92)    // signal 92 to Green
      DONE

.. code-block:: cpp

   <sequence-type>( parameter-1, parameter-2, ...)
     <command 1>
     <command 2>
     ...
     <command n>
     DONE     or     RETURN     or     FOLLOW ( id )

|force-break|

Sequence Types
--------------

.. sidebar:: Ids (Sequence Numbers)

   - ROUTE / AUTOMATION / SEQUENCE ids share the same sequence number collection. i.e. an id must be unique across all three types
   - All ROUTE / AUTOMATION / SEQUENCE ids are limited to 1 - 32767
   - 0 is reserved for the startup sequence appearing as the first entry in the EXRAIL script. 

Sequences types fall in the following broad groups:

* Manually triggered
* Triggered by another sequence
* Triggered as a result of an event that has occurred on one of the turnouts/points, sensors, signals.

Sequence Types - Manually Triggered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Manually triggered sequences are advertised to WiThrottles so you can activate them on you Throttles (e.g. |engine driver| or |withrottle|). They are one of:

.. list-table:: 
    :widths: 30 70
    :header-rows: 0
    :class: command-table

    * - AUTOMATION( id, “description” ) 
      - Start a Automation Sequence and creates a WiThrottles {Handoff} button to automatically send a train along.
    * - ROUTE( id, “description” ) 
      - Start of a Route Sequence and creates a WiThrottles {Set} button to manual drive the train along

Note that these can also be invoked by other sequences.

Sequence Types - Invoked
^^^^^^^^^^^^^^^^^^^^^^^^

Sequences that can only be triggered by other sequences include:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - SEQUENCE( id ) 
      - A general purpose Sequence for scenic animations, etc.

Sequence Types - Event Triggered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: cpp
   :class: code-block-float-right

   // Example
   ONTHROW(8)     // When turnout 8 is thrown,
      THROW(9)    // throw the facing turnout
      RED(24)     // signal 24 to red
      DELAY(2000) // wait 2 seconds
      GREEN(27)   // signal 27 to green
      DONE

Sequences that are triggered when 'events' occur, include:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - ONCLOSE( turnout_id ) 
      - Event handler for turnout close
    * - ONTHROW( turnout_id ) 
      - Event handler for turnout thrown

See :doc:`EX-RAIL-summary` page for additional Event Triggered Sequence types, and additional information on these types. 

Automatically Running a Sequence at Power Up
--------------------------------------------

.. note:: 
   :class: note-float-right

   There is an implied AUTOSTART whereby everything in myAutomation.h prior to the first ``DONE`` keyword is executed on startup. If you don't wish anything to happen at startup, simply add the keyword ``DONE`` as the first line.

If you want a sequence to start immediate the system powers up, add the ``AUTOSTART`` command to the content of the sequence.

This is useful for sequences where you want to constantly monitor the state of sensors and switches.

Contents of a Sequence
----------------------

A sequence is made up of 'Commands'. Commands are usually written one per line or ease of reading, but you can put multiple commands on a single line.  

The commands fall into some basic categories:

* Commands that 'do' something (Actions)
* Commands that change the flow/order in which the commands are executed (Conditionals)
* Commands that change the timing of the execution of the commands  (Delays)
* Informational commands
* Command Station commands

Action Commands - Getting EX-RAIL to 'do' something
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type of command relates to the Objects of the system you have created and defined, like turnouts/points, signals, servos, turntables, blocks and locos.  

There are a substantial number of commands that you can explore on the :doc:`EX-RAIL-summary` page.  We will look at just a few here.

.. code-block:: cpp
   :class: code-block-float-right

   // Example
   ONTHROW(8)     // When turnout 8 is thrown,
      THROW(9)    // throw the facing turnout
      RED(24)     // signal 24 to red
      DELAY(2000) // wait 2 seconds
      GREEN(27)   // signal 27 to green
      DONE

Turnout/Point commands include:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - THROW( id ) 
      - Throw a defined turnout
    * - CLOSE( id) 
      - Close a defined turnout

Signal related commands include:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * -  RED( signal_id ) 
      - Set defined signal to Red (See SIGNAL)
    * - AMBER( signal_id ) 
      - Set a defined signal to Amber. (See SIGNAL)
    * - GREEN( signal_id ) 
      - Set a defined signal to GREEN (see SIGNAL)

.. code-block:: cpp
   :class: code-block-float-right

   // Example
   AUTOMATION(4,"Back and Forward")
      AUTOSTART   // start this immediately the system powers up
      FWD(50)     // move forward at DCC speed 50
      DELAY(5000) // run for 5 seconds
      STOP        // stop the train 
      REV(30)     // move backwards at DCC speed 50
      DELAY(5000) // run for 5 seconds
      STOP        // stop the train 
      FOLLOW(4)   // repeat forever

Loco related commands include:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - FWD( speed ) 
      - Drive loco forward at DCC speed 0-127 (1=ESTOP)
    * - REV( speed ) 
      - Drive logo in reverse at DCC speed 0-127 (1=ESTOP)
    * - SPEED( speed ) 
      - Drive loco in current direction at DCC speed (0-127)
    * - STOP 
      - Set loco speed to 0 (same as SPEED(0) )

Turnout related commands include:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - MOVETT( vpin, steps, activity ) 
      - Move a turntable the number of steps relative to home, and perform the activity (refer EX-Turntable documentation)

See :doc:`EX-RAIL-summary` page for additional commands. 

Sequence Flow / Flow Control Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a simple sequence, once triggered, the system steps though each and every instruction as quickly as possible until it hits ``DONE`` at the end of the sequence.

However there are a number of ways that the processing of a sequence can be changed:

* Conditionals
* CALL - Branch to a separate sequence expecting a RETURN
* RETURN - Return to caller (see CALL)
* FOLLOW - Branch or Follow a numbered sequence (think of “GOTO”)

The timing of the execution of the commands can be altered as well with 'Delay' type commands.

Conditionals
~~~~~~~~~~~~

If a conditional is encountered, the following (enclosed) commands are only executed if the specified conditions are met.

Conditionals have the structure:

.. code-block:: cpp
   :class: code-block-float-right

   // Example 
   // - Toggle a turnout/point based on a push button
   SEQUENCE(85)
      DELAY(100)     // check every 0.1 of a second
      AT(35)         // monitor push button 35
      IFCLOSED(105)  // check the state of turnout/point 105
         THROW(105)  // if closed THROW Turnout/Point 105
      ELSE
         CLOSE(105)  // if closed CLOSE Turnout/Point 105
      ENDIF 
      FOLLOW(85)     // repeat forever

.. code-block:: 

  ...
  IFxxx( id_or_condition, ... )  // where xxx is the type of 'IF' command (see below)
    <commands to execute if the conditions are met>
    ...
  ENDIF
  ...

or

.. code-block:: 

  ...
  IFxxx( id_or_condition, ...)  // where xxx is the type of 'IF' command (see below)
    <commands to execute if the conditions are met>
    ...
  ELSE
    <commands to execute if the conditions are NOT met>
    ...
  ENDIF
  ...

Types of Conditionals
_____________________

Sensor Related Conditional:


.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - IF( sensor_id )
      - If sensor activated or latched, continue, otherwise skip to ELSE/ENDIF, use negative values for active HIGH sensors
    * - IFNOT( sensor_id )
      - If sensor NOT activated and NOT latched, continue, otherwise skip to ELSE/ENDIF, use negative values for active HIGH sensors
    * - IFGTE( sensor_id, value )
      - Test if analog pin reading is greater than or equal to value (>=)
    * - IFLT( sensor_id, value )
      - Test if analog pin reading is less than value (<)

Turnout/Point Related Conditionals:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - IFTHROWN( turnout_id )
      - Test if turnout is thrown
    * - IFCLOSED( turnout_id )
      - Check if turnout is closed

Signal Related Conditionals:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - IFRED( signal_id )
      - Tests if signal is red
    * - IFAMBER( signal_id )
      - Tests if signal is amber
    * - IFGREEN( signal_id )
      - Tests if signal is green

Other Conditionals:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - IFRANDOM( percent )
      - Runs commands in IF block a random percentage of the time
    * - IFRESERVE( block )
      - If block is NOT reserved, reserves it and run commands in IF block. Otherwise, skip to matching ENDIF
    * - IFTIMEOUT
      - Tests if “timed out” flag has been set by an ATTIMEOUT sensor reading attempt

see :doc:`EX-RAIL-summary` page for additional information.

CALL and RETURN
_______________

.. todo:: CALL and RETURN

``CALL( route )`` Branch to a separate sequence, which will need to RETURN when complete.

``RETURN`` Return to the calling sequence when completed (no DONE required).

FOLLOW
______

.. todo:: FOLLOW

``FOLLOW( route )`` Branch or Follow a numbered sequence. (The 'followed' sequence does not return to the sequence that invoked it.)

Delay and Wait Commands
~~~~~~~~~~~~~~~~~~~~~~~

The timing of the execution of the commands can be altered with 'Delay' or 'Wait' type commands. i.e. they don't happen immediately on completion of the previous command.

There are a number of delay type commands that you can explore on the :doc:`EX-RAIL-summary` page.  We will look at just a few here.


.. code-block:: cpp
   :class: code-block-float-right

   // Example
   AUTOMATION(5,"Back and Forward - Random")
      FWD(50)     // move forward at DCC speed 50
      DELAY(5000, 20000) // run for between 5 to 20 seconds (random)
      STOP        // stop the train 
      REV(30)     // move backwards at DCC speed 50
      DELAY(5000, 20000) // run for between 5 to 20 seconds (random)
      STOP        // stop the train 
      FOLLOW(5)   // repeat forever

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - DELAY( delay ) 
      - Delay a number of milliseconds
    * - DELAYMINS( delay ) 
      - Delay a number of minutes
    * - DELAYRANDOM( min_delay, max_delay ) 
      - Delay a random time between min and max milliseconds
    * - AFTER( sensor_id ) 
      - Waits for sensor to trigger and then go off for 0.5 seconds, use negative values for active HIGH sensors
    * - WAITFOR( pin ) 
      - Wait for servo to complete movement

Informational Commands
^^^^^^^^^^^^^^^^^^^^^^

.. todo:: Informational Commands

Command Station Commands
^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: Command Station Commands

Referencing Key Objects in Sequences
====================================

Referencing Turnouts/Points
---------------------------

|EX-CS| supports a number of different turnout/point hardware configurations, but your automation treats them all as simple ID numbers. Turnouts may be defined using ``<T>`` commands from JMRI, or in ``SETUP("<T ...>")`` commands placed in your mySetup.h file, or C++ code in mySetup.h, just like earlier versions.

You may, however, find it more convenient to define turnouts/points using EX-RAIL commands, which may appear anywhere in the 'myAutomation.h' file, even after they are referenced in an ``ONTHROW``, ``ONCLOSE``, ``THROW`` or ``CLOSE`` command. (EXRAIL extracts the turnout definitions just once from your script at Command Station startup.)

Turnouts/Points defined in 'myAutomation.h' will still be visible to WiThrottle and JMRI in the normal way.

A TURNOUT command sends DCC signals to a decoder attached to the track, a PIN_TURNOUT sends a "throw" or "close" (5V or 0V signal) to a pin on the Arduino, and a SERVO_TURNOUT sends an I2C serial command to a servo board connected to your servos.
 
See the :doc:`/ex-rail/EX-RAIL-summary` page for TURNOUT, PIN_TURNOUT and SERVO_TURNOUT definitions.


Referencing Signals
-------------------

Signals can now simply be a decoration to be switched by the route process; they don't need to control anything.

``GREEN(55)`` would turn signal 55 green, and ``RED(55)`` would turn it red. Somewhere in the script there must be a SIGNAL command like this: ``SIGNAL(55,56,57)``.  This defines a signal with ID 55, where the Red/Stop lamp is connected to pin 55, the Amber/Caution lamp to pin 56, and the Green/Proceed lamp to pin 57. The pin allocations do not need to be contiguous, and the red pin number is also used as the signal ID. Thus you can change the signal by ``RED(55)``, ``AMBER(55)``, or ``GREEN(55)``. This means you don't have to manually turn off the other lamps. A RED/GREEN only signal may be created with a zero amber pin.

Referencing Locos
-----------------

.. todo:: Referencing Locos in Sequences

Referencing Loco Functions
--------------------------

.. todo:: Referencing Loco Functions in Sequences

You can use ``FON(n)`` and ``FOFF(n)`` to switch loco functions… eg sound horn.

Referencing Sensors
-------------------

- |EX-CS| allows for sensors that are **Active Low or Active High**. This is particularly important for IR sensors that have been converted to detect by broken beam, rather than reflection. By making the sensor number negative, the sensor state is inverted. e.g. ``AT(-5)``.

- Magnetic/Hall effect sensors work for some layouts, but beware of how you detect the back end of a train approaching the buffers in a siding, or knowing when the last car has cleared a crossing.

- Handling sensors in the automation is made easy because EX-RAIL throws away the concept of interrupts (“oh… sensor 5 has been detected… which loco was that and whatever do I do now?”) and instead has the sequences work on the basis of “do nothing, maintain speed until sensor 5 triggers, and then carry on in the script”.

- Sensor numbers are direct references to VPINs (virtual pin numbers) in the Hardware Abstraction Layer. For a Mega onboard GPIO pin, this is the same as the digital pin number. Other pin ranges refer to I/O expanders etc. 

- Sensors with ID's 0 to 255 may be LATCHED/UNLATCHED in your script. If a sensor is latched on by the script, it can only be set off by the script… so ``AT(5) LATCH(5)`` for example effectively latches the sensor 5 on when detected once.

- Sensor polling by JMRI is independent of this, and may continue if ``<S>`` commands are used.


Outputs
-------

.. todo::  HIGH - Outputs - what is this?

- Generic Outputs are mapped to VPINs on the HAL (as for sensors)
- SIGNAL definitions are just groups of 3 Output pins that can be more easily managed.

Drive-Away feature
==================

EX-RAIL can switch a track section between programming and mainline.

Here for example is a launch sequence that has no predefined locos but allows locos to be added at station 1 while the system is in motion. Let's assume that the track section at Station1 is isolated and connected to the programming track power supply. Also that we have a “launch” button connected where sensor 17 would be and an optional signal (i.e. 3 LEDs) on the control panel connected where signal 27 would be.

.. code-block:: cpp

 SEQUENCE(99)
   SIGNAL(27,28,29)
   RED(27)   // indicate launch not ready
   AFTER(17) // user presses and releases launch button
   UNJOIN    // separate the programming track from main
   DELAY(2000)
   AMBER(27) // Show amber, user may place loco
   AFTER(17) // user places loco on track and presses “launch” again
   READ_LOCO // identify the loco
   GREEN(27) // show green light to user
   JOIN      // connect prog track to main
   START(12) // send loco off along route 12
   FOLLOW(99) // keep doing this for another launch

The READ_LOCO reads the loco address from the PROG track and the current route takes on that loco. By altering the script slightly and adding another sensor, it's possible to detect which way the loco sets off and switch the code logic to send it in the correct direction by using the ``INVERT_DIRECTION`` instruction so that this locos FWD and REV commands are reversed. (easily done with diesels!)
