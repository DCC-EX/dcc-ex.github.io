.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-R-LOGO|

********************
Creating Automations
********************

|tinkerer| |conductor|

.. sidebar:: 

   .. contents:: On this page
      :depth: 2
      :local:

The Automation Process
======================

Once started, each 'sequence' will step through a list of simple keyword instructions until they reach a ``DONE`` keyword.

There can be a startup sequence (keywords at the beginning of the script), which if present is automatically executed, as are any sequences that contain an ``AUTOSTART``.

Multiple concurrent sequences are supported.

For a full list of keywords, see :doc:`EX-RAIL-summary`, and for further detailed information, see the :doc:`/ex-rail/EX-RAIL-reference`.

.. note:: 

   There is an implied AUTOSTART whereby everything in myAutomation.h prior to the first ``DONE`` keyword is executed on startup. If you don't wish anything to happen at startup, simply add the keyword ``DONE`` as the first line.

myAutomation.h - Editing Sequences
==================================

The script containing all your sequences is added to your Command Station by creating a file called "myAutomation.h" in the same folder as CommandStation-EX.ino.

Connecting your Arduino and pressing the :guilabel:`Upload` button in the usual way will save the file and upload your script into the Command Station.

If you are using the Arduino IDE (rather than the |EX-I|) you can create the myAutomation.h file in the Arduino IDE. Use the pulldown button and select New Tab (or simply press Ctrl+Shift+N).

.. image:: /_static/images/ex-rail/setup1.jpg
   :alt:  Setup pulldown button
   :align: center
   :scale: 100%

.. image:: /_static/images/ex-rail/setup2.jpg
   :alt:  Setup pulldown menu
   :align: center
   :scale: 100%

Enter the file name "myAutomation.h" (This is case sensitive)

.. image:: /_static/images/ex-rail/setup3.jpg
   :alt:  Setup myAutomation.h
   :align: center
   :scale: 100%

And type your script in.

.. image:: /_static/images/ex-rail/setup4.jpg
   :alt:  Setup Example file
   :align: center
   :scale: 100%

|

Comments in in myAutomation.h
-----------------------------

Note that if ``//`` occurs in the line, everything after that (including the slashes) is ignored.  i.e. a 'Comment'

If a line starts with ``/*`` then everything, including all subsequent lines an including the '/*') is ignored until a ``*/`` is found.  i.e. a 'Comment'

----

Structure of a Sequence
=======================

Sequence types
--------------

Sequences are either:

* Manually triggered
* Triggered by another sequence
* Triggered as a result of an event that has occured on one of the turnouts/points, sensors, signals.

Manually triggered sequences take one of the following forms:

.. sidebar:: Ids (Sequence Numbers)

   - ROUTE / AUTOMATION / SEQUENCE ids share the same sequence number collection. i.e. an id must be unique across all three types
   - All ROUTE / AUTOMATION / SEQUENCE ids are limited to 1 - 32767
   - 0 is reserved for the startup sequence appearing as the first entry in the EXRAIL script. 

.. code-block:: 

   AUTOMATION( id, “description” )
     ...
     DONE     or     FOLLOW ( id )

.. code-block:: 

   ROUTE( id, “description” )
      ...   
      DONE     or     FOLLOW ( id )

Sequences that can only be triggered by other sequences have the following form:

.. code-block:: 

   SEQUENCE( id )
      ...
      DONE     or     RETURN     or     FOLLOW ( id )


Sequences that trigger on 'events' have the following forms:

.. code-block:: 

   ONCLOSE( turnout_id )
      ...
      DONE     or     RETURN     or     FOLLOW ( id )

.. code-block:: 

   ONTHROW( turnout_id )
      ...
      DONE     or     RETURN     or     FOLLOW ( id )

.. code-block:: 

   ONACTIVATE( addr, sub_addr )
      ...
      DONE     or     RETURN     or     FOLLOW ( id )

.. code-block:: 

   ONACTIVATEL( linear )
      ...
      DONE     or     RETURN     or     FOLLOW ( id )

.. code-block:: 

   ONDEACTIVATE( addr, sub_addr )
      ...
      DONE     or     RETURN     or     FOLLOW ( id )

.. code-block:: 

   ONDEACTIVATEL( linear )
      ...
      DONE     or     RETURN     or     FOLLOW ( id )

Inside a Sequence
-----------------

A sequence is made up of instructions, one per line.  Those instructions relate to the elements of the system you have created and defined, like turnouts/points, sensors, signals, blocks and locos.  

For a simple sequence, once triggered the system steps though each and every instruction as quickly as possible until it hits ``DONE`` at the end of the sequence.

However there are a number of ways that the processing of a sequence can be changed:

* Conditionals
* CALL - Branch to a separate sequence expecting a RETURN
* FOLLOW - Branch or Follow a numbered sequence (think of “GOTO”)
* RETURN - Return to caller (see CALL)

The timing of the execution of the instructions can be altered as well with 'Delays',

Conditionals
^^^^^^^^^^^^

If a condtional is encountered, the following (enclosed) instructions are only executed if the specified conditions are met.

Conditional have the structure:

.. code-block:: 

  ...
  IFxxx( id_or_condition, ... )  // where xxx is the type of 'IF' instruction (see below)
    <instructions to execute if the conditions are met>
    ...
  ENDIF
  ...

or

.. code-block:: 

  ...
  IFxxx( id, ...)  // where xxx is the type of 'IF' instruction (see below)
    <instructions to execute if the conditions are met>
    ...
  ELSE
    <instructions to execute if the conditions are NOT met>
    ...
  ENDIF
  ...

Types of conditionals
^^^^^^^^^^^^^^^^^^^^^

Sensor Related Conditional

* IF( sensor_id )
* IFNOT( sensor_id )
* IFGTE( sensor_id, value )
* IFLT( sensor_id, value )

Turnout/Point Related Conditonals

* IFTHROWN( turnout_id )
* IFCLOSED( turnout_id )

Signal Related Conditionals

* IFRED( signal_id )
* IFAMBER( signal_id )
* IFGREEN( signal_id )

Other Contitionals

* IFRANDOM( percent )
* IFRESERVE( block )
* IFTIMEOUT

see :doc:`EX-RAIL-summary` page for additional information.

CALL and RETURN
---------------

.. todo:: CALL and RETURN

FOLLOW
------

.. todo:: FOLLOW

Delays
------

.. todo:: Delays

Referencing Turnouts/Points in Automations
==========================================

|EX-CS| supports a number of different turnout/point hardware configurations, but your automation treats them all as simple ID numbers. Turnouts may be defined using ``<T>`` commands from JMRI, or in ``SETUP("<T ...>")`` commands placed in your mySetup.h file, or C++ code in mySetup.h, just like earlier versions.

You may, however, find it more convenient to define turnouts/points using EX-RAIL commands, which may appear anywhere in the 'myAutomation.h' file, even after they are referenced in an ``ONTHROW``, ``ONCLOSE``, ``THROW`` or ``CLOSE`` command. (EXRAIL extracts the turnout definitions just once from your script at Command Station startup.)

Turnouts defined in 'myAutomation.h' will still be visible to WiThrottle and JMRI in the normal way.

A TURNOUT sends DCC signals to a decoder attached to the track, a PIN_TURNOUT sends a "throw" or "close" (5V or 0V signal) to a pin on the Arduino, and a SERVO_TURNOUT sends an I2C serial command to a servo board connected to your servos.
 
See the :doc:`/ex-rail/EX-RAIL-summary` page for TURNOUT, PIN_TURNOUT and SERVO_TURNOUT definitions.


Referencing Signals in Automations
==================================

Signals can now simply be a decoration to be switched by the route process; they don't need to control anything.

``GREEN(55)`` would turn signal 55 green, and ``RED(55)`` would turn it red. Somewhere in the script there must be a SIGNAL command like this: ``SIGNAL(55,56,57)``.  This defines a signal with ID 55, where the Red/Stop lamp is connected to pin 55, the Amber/Caution lamp to pin 56, and the Green/Proceed lamp to pin 57. The pin allocations do not need to be contiguous, and the red pin number is also used as the signal ID. Thus you can change the signal by ``RED(55)``, ``AMBER(55)``, or ``GREEN(55)``. This means you don't have to manually turn off the other lamps. A RED/GREEN only signal may be created with a zero amber pin.


Starting the system
===================

Starting the system is tricky, because we need to place the trains in a suitable position and set them going. We need to have a starting position for each loco, and reserve the block(s) it needs to keep other trains from crashing into it.

.. warning:: This EX-RAIL version isn't ready to handle locos randomly placed on the layout after a power down!

For a known set of locos, the easiest way is to define the startup process at the beginning of the script. E.g. for two engines, one at each station.

.. code-block:: cpp

 // ensure all blocks are reserved as if the locos had arrived there
 RESERVE(1) // start with a loco in block 1
 RESERVE(3) // and another in block 3
 SENDLOCO(3,12) // send Loco DCC addr 3 on to route 12
 SENDLOCO(17,34) // send loco DCC addr 17 to route 34
 DONE // don't drop through to the first sequence definition that follows in the script file

.. hint:: Some interesting points about the startup:

 * You don't need to set turnouts, because each route is setting them as required.
 * Signals default to RED on power up, and get turned GREEN when a route clears them.


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

The READ_LOCO reads the loco address from the PROG track and the current route takes on that loco. By altering the script slightly and adding another sensor, it's possible to detect which way the loco sets off and switch the code logic to send it in the correct direction by using the INVERT_DIRECTION instruction so that this locos FWD and REV commands are reversed. (easily done with diesels!)

Referencing Loco Functions in Automations
=========================================

You can use ``FON(n)`` and ``FOFF(n)`` to switch loco functions… eg sound horn.

Referencing Sensors in Automations
==================================

- |EX-CS| allows for sensors that are **Active Low or Active High**. This is particularly important for IR sensors that have been converted to detect by broken beam, rather than reflection. By making the sensor number negative, the sensor state is inverted. e.g. ``AT(-5)``.

- Magnetic/Hall effect sensors work for some layouts, but beware of how you detect the back end of a train approaching the buffers in a siding, or knowing when the last car has cleared a crossing.

- Handling sensors in the automation is made easy because EX-RAIL throws away the concept of interrupts (“oh… sensor 5 has been detected… which loco was that and whatever do I do now?”) and instead has the sequences work on the basis of “do nothing, maintain speed until sensor 5 triggers, and then carry on in the script”.

- Sensor numbers are direct references to VPINs (virtual pin numbers) in the Hardware Abstraction Layer. For a Mega onboard GPIO pin, this is the same as the digital pin number. Other pin ranges refer to I/O expanders etc. 

- Sensors with ID's 0 to 255 may be LATCHED/UNLATCHED in your script. If a sensor is latched on by the script, it can only be set off by the script… so ``AT(5) LATCH(5)`` for example effectively latches the sensor 5 on when detected once.

- Sensor polling by JMRI is independent of this, and may continue if ``<S>`` commands are used.


Outputs
=======

- Generic Outputs are mapped to VPINs on the HAL (as for sensors)
- SIGNAL definitions are just groups of 3 Output pins that can be more easily managed.

Sequence Numbers
================

- All ROUTE / AUTOMATION / SEQUENCE ids are limited to 1 - 32767
- 0 is reserved for the startup sequence appearing as the first entry in the EXRAIL script. 

