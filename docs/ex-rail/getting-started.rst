.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

***************************
Sequences - an Introduction
***************************

|tinkerer| |engineer| |support-button| 

.. sidebar:: 

  .. contents:: On this page
    :depth: 4
    :local:

This page is a limited introduction to the |EX-R| automation sequences.  For more comprehensive information refer to the :doc:`/ex-rail/EX-RAIL-command-reference`.

Before You start, generally you will need to have created some Key Objects (e.g. Turnouts/Points, Sensors, Signals) before you start writing sequences.  Refer to the previous page (:doc:`creating-elements`) for creating and adding those Objects.  Note that these objects don't have to be listed in the myAutomation.h file before the sequence in which you use it, but it is good practice to do so.

----

The Automation Process
======================

Once started, each 'sequence' will step through a list of simple keyword commands, in order, until they reach a ``DONE`` keyword.

Multiple concurrent sequences are supported.

For a full list of keywords, see :doc:`/ex-rail/EX-RAIL-command-reference`.  Only a subset are described on this page.


.. note:: 

   COMMANDS are case sensitive. i.e. they must be in uppercase. Text parameters you provide (aliases,  descriptions) are not.

----

Structure of a 'Sequence'
=========================

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

Manually Triggered Sequence Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Manually triggered sequences are advertised to WiThrottles so you can activate them on your throttles (e.g. |engine driver| or |WiThrottle|). They are one of:

.. list-table:: 
    :widths: 30 70
    :header-rows: 0
    :class: command-table

    * - AUTOMATION( id, “description” ) 
      - Start a Automation Sequence and creates a WiThrottles {Handoff} button to automatically send a train along.
    * - ROUTE( id, “description” ) 
      - Start of a Route Sequence and creates a WiThrottles {Set} button to manual drive the train along

Note that these can also be invoked by other sequences.

Invoked Sequence Types
^^^^^^^^^^^^^^^^^^^^^^

Sequences that can only be triggered by other sequences have the following form:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - SEQUENCE( id ) 
      - A general purpose Sequence for scenic animations, etc.

Event Triggered Sequence Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

See the :doc:`/ex-rail/EX-RAIL-command-reference` for additional Event Triggered Sequence types, and additional information on these types. 

Automatically Running a Sequence at Power Up
--------------------------------------------

.. note:: 
   :class: note-float-right

   |NEW-IN-V5| There is no longer an implied AUTOSTART whereby everything in myAutomation.h prior to the first ``DONE`` keyword is executed on startup. If you wish to reinstate this behaviour, simply add the keyword ``AUTOSTART`` as the first line.

If you want a sequence to start immediate the system powers up, add the ``AUTOSTART`` command to the content of the sequence.

This is useful for sequences where you want to constantly monitor the state of sensors and switches.

----

Contents of a 'Sequence'
------------------------

A sequence is made up of 'Commands'. Commands are usually written one per line for ease of reading, but you can put multiple commands on a single line.  

The commands fall into some basic categories:

* `Actions <#action-commands-getting-ex-rail-to-do-something>`_ - Commands that 'do' something
* `Flow Control Commands <#sequence-flow-flow-control-commands>`_

  * :ref:`Conditionals <getting-started-conditionals>` & `Branching`_ - Commands that change the flow/order in which the commands are executed
  * `Delays & Waits`_ - Commands that change the timing of the execution of the commands

* `Command Station commands`_

----

Action Commands - Getting EX-RAIL to 'do' something
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This type of command will somehow change Objects of the system you have created and defined, like turnouts/points, signals, servos, turntables, blocks and locos.  

There are a substantial number of commands that you can explore in the :doc:`/ex-rail/EX-RAIL-command-reference`. We will look at just a few here.

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

Turntable related commands include:

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - MOVETT( vpin, steps, activity ) 
      - Move a turntable the number of steps relative to home, and perform the activity (refer EX-Turntable documentation)

See the :doc:`/ex-rail/EX-RAIL-command-reference` for additional commands and additional information on these commands. 

Sequence Flow / Flow Control Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a simple sequence, once triggered, the system steps though each and every instruction as quickly as possible until it hits ``DONE`` at the end of the sequence.

However there are a number of ways that the processing of a sequence can be changed:

* :ref:`Conditionals <getting-started-conditionals>`
* `Branching`_
   * `CALL <#call-and-return>`_ - Branch to a separate sequence expecting a RETURN
   * `RETURN <#call-and-return>`_ - Return to caller (see `CALL <#call-and-return>`_)
   * `FOLLOW`_ - Branch or Follow a numbered sequence (think of “GOTO”)

The timing of the execution of the commands can be altered as well with 'Delay' and 'Wait' type commands.

.. _getting-started-conditionals:
  
Conditionals
~~~~~~~~~~~~~

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

.. code-block:: cpp

  ...
  IFxxx( id_or_condition, ... )  // where xxx is the type of 'IF' command (see below)
    <commands to execute if the conditions are met>
    ...
  ENDIF
  ...

or

.. code-block:: cpp

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
'''''''''''''''''''''

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

see the :doc:`/ex-rail/EX-RAIL-command-reference` for additional information.

Branching
~~~~~~~~~

Sequences can invoke other sequences.  There are two ways this can be done.

CALL and RETURN
'''''''''''''''

To invoke another sequence, and return and execute the next command in the current sequence you can use the combination of the ``CALL( route_id )`` command in the main sequence, and in the called sequence, use the ``RETURN`` command to return.

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - CALL( route_id )
      - Branch to a separate sequence, which will need to RETURN when complete
    * - RETURN
      - Return to the calling sequence when completed (no DONE required).

FOLLOW
''''''

To invoke another sequence, with no wish to return and execute any further commands in the current sequence you can use the ``FOLLOW( route_id )`` command in the main sequence.

``FOLLOW( route_id )`` Branch or Follow a numbered sequence. (The 'followed' sequence does not return to the sequence that invoked it.)

Delays & Waits
~~~~~~~~~~~~~~

The timing of the execution of the commands in a sequence can be altered with 'Delay' or 'Wait' type commands. i.e. they don't happen immediately on completion of the previous command.

There are a number of delay type commands that you can explore in the :doc:`/ex-rail/EX-RAIL-command-reference`. We will look at just a few here.


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

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * - AFTER( sensor_id ) 
      - Waits for sensor to trigger and then go off for 0.5 seconds, use negative values for active HIGH sensors
    * - WAITFOR( pin ) 
      - Wait for servo to complete movement
    * - AT( sensor_id )
      - Wait until sensor is active/triggered, use negative values for active HIGH sensors
    * - ATTIMEOUT( sensor_id, timeout_ms )
      - Wait until sensor is active/triggered, or if the timer runs out, then continue and set a testable "timed out" flag, use negative values for active HIGH sensors
    * - AFTER( sensor_id )
      - Waits for sensor to trigger and then go off for 0.5 seconds, use negative values for active HIGH sensors

Command Station Commands
^^^^^^^^^^^^^^^^^^^^^^^^

There are a substantial number of commands that you can explore in the :doc:`/ex-rail/EX-RAIL-command-reference`. We will look at just a few here.

.. code-block:: cpp

  // use the drive away feature to recginse the loco on the
  // programming track and drive it onto the main track
  SEQUENCE(99)    
    READ_LOCO // identify the loco on the programming track
    JOIN      // connect programming track to main
    WAIT(30000) // wait 30 seconds
    UNJOIN    // disconnect the programming track form the main
    // see the 'Drive-Away Feature' on this page for more infomation

.. list-table::
    :widths: auto
    :header-rows: 0
    :class: command-table

    * -  JOIN
      -  Joins PROG and MAIN track outputs to send the same MAIN DCC signal on both tracks
    * -  UNJOIN
      -  Disconnect Prog track from Main DCC signal
    * -  READ_LOCO
      -  Read loco ID from Prog track

See the :doc:`/ex-rail/EX-RAIL-command-reference` for additional Command Station Commands and additional information on the commands shown here.

----

Referencing Key Objects in Sequences
====================================

Referencing Turnouts/Points
---------------------------

|EX-CS| supports a number of different turnout/point hardware configurations, but your automation treats them all as simple ID numbers. Turnouts may be defined using ``<T>`` commands from JMRI, or in ``SETUP("<T ...>")`` commands placed in your mySetup.h file, or C++ code in mySetup.h, just like earlier versions.

You may, however, find it more convenient to define turnouts/points using EX-RAIL commands, which may appear anywhere in the 'myAutomation.h' file, even after they are referenced in an ``ONTHROW``, ``ONCLOSE``, ``THROW`` or ``CLOSE`` command. (EXRAIL extracts the turnout definitions just once from your script at Command Station startup.)

Turnouts/Points defined in 'myAutomation.h' will still be visible to WiThrottle and JMRI in the normal way.

A TURNOUT command sends DCC signals to a decoder attached to the track, a PIN_TURNOUT sends a "throw" or "close" (5V or 0V signal) to a pin on the Arduino, and a SERVO_TURNOUT sends an |I2C| serial command to a servo board connected to your servos.
 
See the :doc:`/ex-rail/EX-RAIL-command-reference` for TURNOUT, PIN_TURNOUT and SERVO_TURNOUT definitions.

Referencing Signals
-------------------

Signals can now simply be a decoration to be switched by the route process; they don't need to control anything.

``GREEN(55)`` would turn signal 55 green, and ``RED(55)`` would turn it red. Somewhere in the script there must be a SIGNAL command like this: ``SIGNAL(55,56,57)``.  This defines a signal with ID 55, where the Red/Stop lamp is connected to pin 55, the Amber/Caution lamp to pin 56, and the Green/Proceed lamp to pin 57. The pin allocations do not need to be contiguous, and the red pin number is also used as the signal ID. Thus you can change the signal by ``RED(55)``, ``AMBER(55)``, or ``GREEN(55)``. This means you don't have to manually turn off the other lamps. A RED/GREEN only signal may be created with a zero amber pin.

Referencing Locos
-----------------

.. code-block:: cpp
  :class: code-block-float-right
  
  //Example
  // If this is at the start of myConfiuration.h  
  // this will act like an AUTOSTART sequence
  // and automatically turn the track power on
  SETLOCO(9999)   // select loco 9999
  SPEED(0)        // set the speed to 0.  This will turn the tarck power on
  DONE

To reference a loco in a sequence you only need to know it's DCC Address.  i.e. It does not need to be in the roster.

Use the ``SETLOCO( loco_dcc_address )`` command to set the loco address for the sequence. Use ``SENDLOCO( ( loco_dcc_address, route_id )`` to activate a new route/sequence send a given loco along it.

Following commands (e.g. ``SPEED (50)`` ) will be directed at the loco chosen.

Referencing Loco Functions
--------------------------

You can use ``FON( function_no )`` and ``FOFF( function_no )`` to activate and deactivate loco functions… eg sound horn.  The loco that the command will be directed to will be the one previously chosen using ``SETLOCO( loco_dcc_address )`` or ``SENDLOCO( ( loco_dcc_address, route_id )``.

Referencing Sensors
-------------------

Sensor numbers are direct references to VPINs (virtual pin numbers) in the Hardware Abstraction Layer. For a Mega onboard GPIO pin, this is the same as the digital pin number. Other pin ranges refer to I/O expanders etc. 

Sensors with ID's 0 to 255 may be LATCHED/UNLATCHED in your script. If a sensor is latched on by the script, it can only be set off by the script… so ``AT(5) LATCH(5)`` for example effectively latches the sensor 5 on when detected once.

Sensor polling by JMRI is independent of this, and may continue if ``<S>`` commands are used.

----

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


----

Next Steps - Examples
=====================

Click :doc:`here <examples>` or click the :guilabel:`Next` button to see some concrete examples of automation sequences.