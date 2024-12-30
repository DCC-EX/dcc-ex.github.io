.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************
EXRAIL Command Reference
**************************

|SUITABLE| |tinkerer| |engineer| |support-button|

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

|EX-CS| provides full automation and accessory control through the Extended Railroad Automation Instruction Language (|EX-R|).

This page includes a reference for all available |EX-R| commands.

See Also:

- :doc:`Introduction to EXRAIL <getting-started>` 
- :doc:`/exrail/examples`

----

Introductory Information
========================

Conventions used on this page
-----------------------------

- CAPITALISED words - These are EXRAIL commands and are case sensitive
- lowercase words within brackets/braces ``()`` - These are EXRAIL parameters that must be provided, with multiple parameters separated by a comma ``,``, for example ``SEQUENCE(id)`` or ``DELAYRANDOM(min_delay, max_delay)``
- Quoted ``"text"`` - Text within quote marks ``""`` are used as descriptions, and must include the quote characters, for example ``ROUTE(id, "description")`` becomes ``ROUTE(1, "This is the route description")``
- Square brackets ``[]`` - Parameters within square brackets ``[]`` are optional and may be ommitted. If specifying these parameters, do not include the square brackets themselves, for example ``ALIAS(name[, value])`` becomes ``ALIAS(MY_ALIAS)`` or ``ALIAS(MY_ALIAS, 3)``
- ``|`` - Use of the ``|`` character means you need to provide one of the provided options only, for example ``<D POWER ON|OFF>`` becomes either ``<D POWER ON>`` or ``<D POWER OFF>``

Handy information
-----------------

- COMMANDS are case sensitive. i.e. they must be in uppercase. Text parameters you provide (aliases,  descriptions) are not
- *AUTOMATION*, *ROUTE*, and *SEQUENCE* use the same ID number space, so a ``FOLLOW(n)`` command can be used for any of them
- Sensors and outputs used by AT/AFTER/SET/RESET/LATCH/UNLATCH/SERVO/IF/IFNOT refer directly to Arduino pins, and those handled by |I2C| expansion (as virtual pins or vpins).
- Signals also refer directly to pins, and the signal ID (for RED/AMBER/GREEN) is always the same as the RED signal pin
- It's OK to use sensor IDs that have no physical item in the layout. These can only be LATCHed, tested (IF/IFNOT), or UNLATCHed in the sequences. If a sensor is latched by the sequence, it can only be unlatched by the sequence so ``AT(35) LATCH(35)`` for example, effectively latches sensor 35 on when detected once
- All IDs used in commands and functions will be numbers, or an ALIAS name if configured
- Most IDs simply need to be unique, however RESERVE/FREE and LATCH/UNLATCH must be in the range 0 - 255

.. note:: 

  There are four uses of ID numbers in EXRAIL:

  - AUTOMATION, ROUTE, and SEQUENCE IDs
  - Turnout/Point IDs
  - Vpins - Includes physical pins on the CommandStation, virtual pins (Vpins) on I/O expander modules, and virtual pins that have no physical presence
  - Virtual block IDs as used in RESERVE/FREE

  Therefore, you can have an AUTOMATION, a turnout/point, a Vpin, and a virtual block all defined with the same ID without issue as these will not relate to each other. This is probably a great reason to consider aliases to avoid confusion.

Correct use of DONE, ENDIF, and FOLLOW() statements
---------------------------------------------------

Every |EX-R| automation/route/sequence, event handler, and conditional statement must be terminated by one of these three directives.

On this page, you will see various references to the use of ``DONE``, ``ENDIF``, and ``FOLLOW()`` which can be confusing, so refer to this quick list to help understand the context in which each of these should be used:

- Every conditional statement (all directives starting with the word ``IF``) must be terminated by ``ENDIF``
- Every group of commands within a ROUTE, AUTOMATION, or SEQUENCE must be terminated by either ``DONE`` or ``FOLLOW(id)``
- Every event handler (all directives starting with the word ``ON``) must be terminated by ``DONE``

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    // Valid use of a ROUTE with a nested IF statement
    ROUTE(1)
      IF(46)
        // Things to be done when sensor ID 46 is active
      ELSE
        // Things to be done when sensor ID 46 is inactive
      ENDIF
      DONE

    // Validate use of a sequence that needs to run continuously
    // DONE is not required in this instance
    SEQUENCE(2)
      IF(46)
        // Things to be done when sensor ID 46 is active
      ELSE
        // Things to be done when sensor ID 46 is inactive
      ENDIF
      FOLLOW(2)

    // Validate use of a turnout event handler for turnout ID 200
    ONCLOSE(200)
      // Things to be done when turnout 200 is closed
      DONE

|force-break|

AT(vpin) or AFTER(vpin [,debounceTime]) versus IF(vpin)
-----------------------------------------------------------------------------

When defining conditions, the behaviour of ``AT()`` and ``AFTER()`` is quite different to using conditional ``IF()`` statements.

This applies to all directives starting with ``AT``, ``AFTER``, and ``IF``.

When using ``AT()`` or ``AFTER()``, this is a blocking activity, meaning the sequence of activities will not progress beyond this particular directive unless the condition is met.

When using ``IF`` conditional statements, these will not block if the condition is not met, allowing the sequence of activities to continue.

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    // Use of AT() to prevent doing anything until a sensor is activated
    // This sequence will continue to run until the sensor is activated, in which case those activities will be performed, and it will end
    SEQUENCE(1)
      AT(46)
        // Things to do when sensor 46 is activated
      DONE

    // Use of IF() to continuously monitor a number of sensors
    // This sequence will continually loop to monitor the sensors, meaning the activities related to each sensor are not blocked by the state of other sensors
    SEQUENCE(2)
      IF(46)
        // Things to do if sensor 46 is activated
      ENDIF
      IF(47)
        // Things to do if sensor 47 is activated
      ENDIF
      IF(48)
        // Things to do if sensor 48 is activated
      ENDIF
      FOLLOW(2)

|force-break|

----

Interactive diagnostics and control
-----------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

Various diagnostic and control commands have been added to control and interact with |EX-R|, including the various sequences and objects once they have been defined in myAutomation.h and uploaded to the |EX-CS|.

These commands can be run interactively via the serial console or over Ethernet/WiFi if using a throttle or client that provides a suitable interface for sending native DCC-EX commands.

|hr-dashed|

``<D EXRAIL state>`` - Enable or disable EXRAIL sequence logging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the CommandStation is connected to a |serial monitor|, |EX-R| sequence logging can be turned on or off (Enabled or Disabled).

  .. collapse:: For example: (click to show)

    Example output from :ref:`exrail/examples:Point to Point Shuttle` running SEQUENCE(13) with loco ID 18:

    .. code-block:: cpp

      <D EXRAIL ON>
      <p1 MAIN>
      PPA1
      <1 18 0 178 0>
      <* EXRAIL Sensor 42 hit *>
      <* EXRAIL Sensor 42 hit *>
      <* EXRAIL drive 18 0 1 *>
      <1 18 0 128 0>
      <* EXRAIL drive 18 20 0 *>
      <1 18 0 20 0>
      <* EXRAIL Sensor 41 hit *>
      <* EXRAIL Sensor 41 hit *>
      <* EXRAIL drive 18 0 0 *>
      <1 18 0 0 0>
      <* EXRAIL begin(13) *>
      <* EXRAIL begin(13) *>
      <* EXRAIL drive 18 50 1 *>
      <1 18 0 178 0>

|force-break|

|hr-dashed|

``</PAUSE>`` - Pause ALL EXRAIL automation activities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pauses **ALL** EXRAIL automation activities, including sending an E-STOP to all locos.

|hr-dashed|

``</RESUME>`` - Resume **ALL** EXRAIL automation activities 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resume **ALL** EXRAIL automation activities, and resumes all locos at the same speed at which they were paused.

``</>`` - Display EXRAIL running task information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. collapse:: For example: (click to show)

  Example outputs also using :ref:`exrail/examples:Point to Point Shuttle`:

  * Leaving right side of the shuttle sequence with speed 50F (forward):

  .. code-block:: cpp
    
    </>
    <1 18 0 178 0>
    <* EXRAIL STATUS
    ID=0,PC=12,LOCO=0 ,SPEED=0F
    ID=1,PC=12,LOCO=18 ,SPEED=50F *>

|force-break|

|hr-dashed|

``</ START [loco_addr] route_id>`` - Start route, optionally using specified loco
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starts a new task to send a loco onto a Route, or activate a non-loco Animation or Sequence.

|hr-dashed|

``</ KILL task_id>`` - Kills a currently running sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kills a currently running sequence task by ID

|hr-dashed|

``</ RESERVE block_id>`` - Manually reserves a virtual track Block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Manually reserves a virtual track Block, valid IDs are in the range 0 - 255

|hr-dashed|

``</ FREE block_id>`` - Manually frees a virtual track Block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Manually frees a virtual track Block, valid IDs are in the range 0 - 255.

|hr-dashed|

``</ LATCH vpin>`` - Lock sensor ON, preventing external influence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lock sensor ON, preventing external influence, valid IDs are in the range 0 - 255.

|hr-dashed|

``</ UNLATCH vpin>`` - Unlock sensor, returning to current external state
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlock sensor, returning to current external state, valid IDs are in the range 0 - 255.

Refer to the LATCH/UNLATCH commands in the :ref:`exrail/exrail-command-reference:sensors/inputs - reading and responding` section below for further details.

----

Aliases
-------

``ALIAS( name[, value] )`` - Assigns name to a value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aliases assigns names to values. They can go anywhere in the sequence. If a value is not assigned, a unique ID will be assigned based on the alias "name" text.

This is a simple substitution that lets you have readable names for things in your sequence. For example, instead of having to remember the VPin a turnout/point is connected to, give the pin number an alias and refer to it by that name. You can use this to name routes, values, pin numbers, or anything you need.

If you simply need a unique identifier for an object used internally to the sequence, such as a turnout/point, route, automation, or sequence, you don't even need to provide an ID, |EX-R| will generate one automatically when you omit the value parameter. We recommend using this for all your routes, sequences, and other internal objects so you don't have to try to remember or keep a list of numbers you've used. This also prevents you from assigning the same number to more than one object.

REMEMBER: IDs for RESERVE/FREE, LATCH/UNLATCH, and pins must be explicitly defined.

To put this another way, if you connect an LED to pin 23 and want to turn it on and off, you have to explicitly set its pin number, so `ALIAS(TOWER_LED, 23)` lets you equate "23" to TOWER_LED. But if you created a route to run your train around an oval, you don't really need to set the number or even know it. Just use `ALIAS(OVAL)` and let EX assign a number internally. If you ever wanted to know what number it assigns, you can enter `<? OVAL>` from the serial monitor with the Command Station running and it will tell you next to "Opcode=". Since this "hash", as it is called, is generated by the alias name word, it is always unique and always the same for that word even if you have not created the alias yet. Fun fact, "OVAL" will always equal 27500.

Alias naming rules:

- **Must not** be an existing EXRAIL command name or other reserved word.
- **Should be** reasonably short but descriptive.
- **Must start** with letters A-Z, a-z, or underscore _ (case sensitive!).
- **May then** also contain numbers.
- **Must not** contain spaces or special characters.

*Parameters:* |BR|
|_| > **name** - name for the Alias.  See rules above |BR|
|_| > **value** - value to insert in place of the Alias

  .. collapse:: For example: (click to show)

    Defining a pin turnout/point without an alias:

    .. code-block:: cpp

      PIN_TURNOUT(1, 25, "Coal Yard")

    Defining a pin turnout/point with aliases:

    .. code-block:: cpp
      
      ALIAS(COAL_YARD)
      ALIAS(COAL_YARD_PIN, 25)
      PIN_TURNOUT(COAL_YARD, COAL_YARD_PIN, "Coal Yard")

    Note that you could have used the command `ALIAS(COAL_YARD, 1)` in the example above to explicitly set the number, but unless you have a reason to use specific numbers, let the Command Station do it for you. 

    In this simple example, aliases seem like overkill, however consider the case where you need to have the "Coal Yard" turnout/point closed or thrown in various different automation sequences, and you will soon see why it's easier to understand you're throwing the COAL_YARD turnout/point rather than turnout/point ID 12345.

|force-break|

----

Alphabetic Command List
=======================

.. collapse:: Full Alphabetic list of commands: (click to show)

  * :ref:`ACOF`
  * :ref:`ACON`
  * :ref:`AFTER`
  * :ref:`AFTEROVERLOAD`
  * :ref:`AMBER`
  * :ref:`ASPECT`
  * :ref:`AT`
  * :ref:`ATGTE`
  * :ref:`ATLT`
  * :ref:`ATTIMEOUT1`
  * :ref:`ATTIMEOUT2`
  * :ref:`AUTOMATION`
  * :ref:`AUTOSTART`
  * :ref:`BLINK`
  * :ref:`CALL`
  * :ref:`CLEAR_ALL_STASH`
  * :ref:`CLEAR_STASH`
  * :ref:`CLOSE`
  * :ref:`DCCACTIVATE`
  * :ref:`DCC_TURNTABLE`
  * :ref:`DELAY`
  * :ref:`DELAYMINS`
  * :ref:`DELAYMS`
  * :ref:`DRIVE`
  * :ref:`ELSE`
  * :ref:`ENDEXRAIL`
  * :ref:`ENDIF`
  * :ref:`ENDTASK`
  * :ref:`EXTT_TURNTABLE`
  * :ref:`FOFF`
  * :ref:`FOLLOW`
  * :ref:`FON`
  * :ref:`FORGET`
  * :ref:`FREE`
  * :ref:`FTOGGLE`
  * :ref:`FWD`
  * :ref:`GREEN`
  * :ref:`IF`
  * :ref:`IFAMBER`
  * :ref:`IFCLOSED`
  * :ref:`IFGREEN`
  * :ref:`IFGTE`
  * :ref:`IFLOCO`
  * :ref:`IFLT`
  * :ref:`IFNOT`
  * :ref:`IFRANDOM`
  * :ref:`IFRE`
  * :ref:`IFRED`
  * :ref:`IFRESERVE`
  * :ref:`IFTHROWN`
  * :ref:`IFTIMEOUT`
  * :ref:`IFTTPOSITION`
  * :ref:`INVERT_DIRECTION`
  * :ref:`JOIN`
  * :ref:`KILLALL`
  * :ref:`LATCH`
  * :ref:`LCC`
  * :ref:`LCCX`
  * :ref:`NEOPIXEL`
  * :ref:`ONACOF`
  * :ref:`ONACON`
  * :ref:`ONACTIVATE`
  * :ref:`ONAMBER`
  * :ref:`ONBUTTON`
  * :ref:`ONCHANGE`
  * :ref:`ONCLOCKTIME`
  * :ref:`ONCLOSE`
  * :ref:`ONDEACTIVATE`
  * :ref:`ONGREEN`
  * :ref:`ONLCC`
  * :ref:`ONOVERLOAD`
  * :ref:`ONRED`
  * :ref:`ONROTATE`
  * :ref:`ONSENSOR`
  * :ref:`ONTHROW`
  * :ref:`ONTIME`
  * PAD
  * :ref:`PAUSE`
  * :ref:`PICKUP_STASH`
  * :ref:`PIN_TURNOUT`
  * :ref:`POM`
  * :ref:`POWEROFF`
  * :ref:`POWERON`
  * :ref:`PRINT`
  * :ref:`RANDWAIT`
  * READ_LOCO1
  * READ_LOCO2
  * :ref:`RED`
  * :ref:`RESERVE`
  * :ref:`RESET`
  * :ref:`RESUME`
  * :ref:`RETURN`
  * :ref:`REV`
  * :ref:`ROSTER`
  * :ref:`ROTATE`
  * :ref:`ROUTE`
  * :ref:`ROUTE_ACTIVE`
  * :ref:`ROUTE_DISABLED`
  * :ref:`ROUTE_HIDDEN`
  * :ref:`ROUTE_INACTIVE`
  * :ref:`SENDLOCO`
  * :ref:`SEQUENCE`
  * :ref:`SERVO`
  * :ref:`SERVO_TURNOUT`
  * :ref:`SET`
  * :ref:`SET_POWER`
  * :ref:`SET_TRACK`
  * :ref:`SETFREQ`
  * :ref:`SETLOCO`
  * :ref:`SIGNAL`
  * :ref:`SPEED`
  * :ref:`START`
  * :ref:`STASH`
  * :ref:`THROW`
  * :ref:`TOGGLE_TURNOUT`
  * :ref:`TT_ADDPOSITION`
  * :ref:`TURNOUT`
  * :ref:`UNJOIN`
  * :ref:`UNLATCH`
  * :ref:`WAITFOR`
  * :ref:`WAITFORTT`
  * :ref:`XFOFF`
  * :ref:`XFON`
  * :ref:`XFTOGGLE`


|force-break|

----

Flow Control
============

Scripts/Sequences - Types and Control
-------------------------------------

.. contents:: In This Section
  :depth: 4
  :local:
  :class: in-this-section

|hr-dashed|

.. _autostart:

``AUTOSTART`` - Automatically start sequence at this point during Command Station startup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A sequence is automatically started at this point during startup.

If you have previously relied on the implied AUTOSTART to run things immediately,  as of Version 5.0 you must now add this explicitly to the beginning of myAutomation.h

*Parameters:* |BR|
|_| > none

|hr-dashed|

There are three options to define |EX-R| scripts or sequences:

* AUTOMATION
* ROUTE
* SEQUENCE

|hr-dashed|

.. _automation:

``AUTOMATION( id, "description" )`` - Define an automation, advertised to throttles/clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define an automation sequence that is advertised to throttles/clients to send a train along. 

See :ref:`exrail/examples:Stopping at a Station (simple loop)` for a simple example.

*Parameters:* |BR|
|_| > **id** - id for the sequence/route/automation |BR|
|_| > **description** - description for the sequence/route/automation

|hr-dashed|

.. _route:

``ROUTE( id, "description" )`` - Define a route, advertised to throttles/clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a route that is advertised to throttles/clients. This can be used to initiate automation sequences such as setting turnouts/points and signals to allow a train to be driven through a specific route on the layout. See :ref:`exrail/examples:creating routes` for various examples.

*Parameters:* |BR|
|_| > **id** - id for the sequence/route/automation |BR|
|_| > **description** - description for the sequence/route/automation

|hr-dashed|

.. _sequence:

``SEQUENCE( id )`` - A general purpose sequence, not advertised to throttles/clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A general purpose automation sequence that is not advertised to throttles/clients. This may be triggered automatically on startup, or be called by other sequences or activities. See :ref:`exrail/examples:automating various non-track items`, :ref:`exrail/examples:Point to Point Shuttle`, and :ref:`exrail/examples:multiple inter-connected trains` for further examples.

*Parameters:* |BR|
|_| > **id** - id for the sequence/route/automation |BR|
|_| > **description** - description for the sequence/route/automation

|hr-dashed|

All of these sequence types must be terminated by either a ``DONE``, ``FOLLOW(id)``, or ``RETURN`` statement. If you use ``FOLLOW(id)`` or ``RETURN``, you do not also need a ``DONE`` statement as any of these terms will tell |EX-R| that the sequence of events has ended.

|hr-dashed|

.. _done:

``DONE`` - Completes a Sequence/Route/Animation/Event, or any other automation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Completes a Sequence/Route/Animation/Event handler, and any other automation definition as shown in the various examples on this page and elsewhere in the |EX-R| documentation.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _endtask:

``ENDTASK`` - Completes a Sequence/Route/Animation/Event, or any other automation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Identical to ``DONE``.

Completes a Sequence/Route/Animation/Event handler, and any other automation definition as shown in the various examples on this page and elsewhere in the |EX-R| documentation.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _call:

``CALL( id )`` - Branch to a separate sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Branch to a separate sequence, which will need to RETURN when complete.

*Parameters:* |BR|
|_| > **id** - id for the sequence/route/automation to branch to

|hr-dashed|

.. _return:

``RETURN`` - Return to the calling sequence when completed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return to the calling sequence when completed (no DONE required).

*Parameters:* |BR|
|_| > none

.. collapse:: For example: (click to show)

  For example, you have an AUTOMATION which you initiate that sends a train through your layout with multiple station stops, and you want to do the same things at each station.

  You could write a very long AUTOMATION sequence to do this, or you could write the sound SEQUENCE once, then call it at each station:

  .. code-block:: cpp

    AUTOMATION(21, "Station loop")    // Our station loop sequence
      FWD(30)
      AT(101)                         // At station 1 entrance sensor, call our sequence
      CALL(22)
      AT(102)                         // At station 2 entrance sensor, call our sequence
      CALL(22)
      AT(103)                         // At station 3 entrance sensor, call our sequence
      CALL(22)
      AT(104)                         // At station 4 entrance sensor, call our sequence
      CALL(22)
      FOLLOW(21)                      // Keep looping through the stations (see FOLLOW command reference below)

    SEQUENCE(22, "Station sequence")  // Our station sequence
      FON(2)                         // Blow the horn
      FON(3)                         // Break squeal
      STOP                            // Stop at the station
      FON(4)                         // Let out a hiss from the air breaks for a second
      DELAY(1000)
      FOFF(4)
      DELAYRANDOM(2000, 10000)        // Wait between 2 and 10 seconds for passengers
      FON(2)                         // Blow the horn again
      FWD(30)                         // On our way to the next station
      RETURN                          // Return to the calling sequence

|force-break|

|hr-dashed|

.. _follow:

``FOLLOW( sequence_id )`` - Branch or Follow a specified sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Branch or Follow a specified sequence. This lets us do clever things like performing a different sequence depending on whether a turnout/point is CLOSED or THROWN, as well as simple things such as the example above where we keep looping through the same sequence.

*Parameters:* |BR|
|_| > **sequence_id** - id for the sequence/route/automation to branch to

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    AUTOMATION(23, "Choose your own adventure") // This let's someone control the sequence by throwing a turnout/point (or not)
      FWD(30)
      AFTER(105)
      IFTHROWN(106)
        FOLLOW(24)
      ELSE
        FOLLOW(25)
      ENDIF
      DONE

    SEQUENCE(24, "Adventure 1")                 // Quite a boring adventure to stop in a siding after sensor 106 has activated/deactivated
      AFTER(106)
      FON(2)
      FON(3)
      STOP
      DONE

    SEQUENCE(25, "Adventure 2")                 // If we don't throw the turnout/point, let's do our station loop from the example above
      FOLLOW(21)

|force-break|

|hr-dashed|

.. _pause:

``PAUSE`` - E-STOP all locos and PAUSE all other EXRAIL tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

E-STOP all locos and PAUSE all other |EX-R| tasks until RESUMEd.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _resume:

``RESUME`` - Resume all paused tasks, including loco movement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Resume all paused tasks, including loco movement.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _start:

``START( id )`` - Execute a route or sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start a new task to execute a route or sequence.

*Parameters:* |BR|
|_| > **id** - id for the sequence/route/automation to branch to

|hr-dashed|

.. _delay:

``DELAY( delay )`` - Delay the sequence a number of milliseconds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delay the current sequence a number of milliseconds.

*Parameters:* |BR|
|_| > **delay** - period to delay in milliseconds

|hr-dashed|

.. _delayms:

``DELAYMS( delay )`` - Delay the sequence a number of milliseconds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Same as ``DELAY()``

Delay the current sequence a number of milliseconds.

*Parameters:* |BR|
|_| > **delay** - period to delay in milliseconds

|hr-dashed|

.. _delaymins:

``DELAYMINS( delay )`` - Delay the sequence a number of minutes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delay the current sequence a number of minutes.

*Parameters:* |BR|
|_| > **delay** - period to delay in minutes

|hr-dashed|

.. _delayrandom:

``DELAYRANDOM( min_delay, max_delay )`` - Delay a random period of time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delay the current sequence a random time between min and max milliseconds.

See :ref:`exrail/examples:Multiple inter-connected trains` for good examples.

*Parameters:* |BR|
|_| > **min_delay** - minimum period to delay in milliseconds |BR|
|_| > **max_delay** - maximum period to delay in milliseconds

.. collapse:: Delay examples: (click to show)

  .. code-block:: cpp

    ONCLOSE(102)      // When turnout 102 closed, wait 2 seconds, then set signal 101 green.
      DELAY(2000)
      GREEN(101)
      DONE

    AT(123)           // When sensor 123 is activated, set signal 102 red, wait 1 minute, then set signal 102 green.
      RED(102)
      DELAYMINS(1)
      GREEN(102)
      DONE

|force-break|

|hr-dashed|

.. _randwait:

``RANDWAIT( ??? )`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo: LOW - EXRAIL doco - RANDWAIT

*Parameters:* |BR|
|_| > **???** - ??? |BR|
|_| > **???** - ???

|hr-dashed|

.. _ifrandom:

``IFRANDOM( percent )`` - Run commands a random percentage of the time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Runs commands in IF block a random percentage of the time. This is handy for more realism by enabling automations that don't have to run on a schedule.

*Parameters:* |BR|
|_| > **percent** - percentage to test against (0-100) |BR|

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    AT(165)           // When sensor 165 is activated, set a lineside merry-go-round in action for 1 minute 50% of the time.
      IFRANDOM(50)
        SET(166)
        DELAYMINS(1)
        RESET(166)
      ENDIF
      DONE

|force-break|

|hr-dashed|

.. _route_caption:

``ROUTE_CAPTION( route_id, "caption" )`` - Change the label of the Route button
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Dynamically change the label of the Route button.

*Parameters:* |BR|
|_| > **route_id** - id of the route to change |BR|
|_| > **caption** - text to replace on the route 'button' label

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    // setup 4 'routes'to switch between tracks/districts between PROG, MAIN and DC
    ROUTE(500,"1.Trk: A main, B prog")
        SET_TRACK(A,MAIN)
        SET_TRACK(B,PROG)
        ROUTE_CAPTION(500,"Active")
        ROUTE_CAPTION(501,"Inactive")
        ROUTE_CAPTION(502,"Inactive")
        ROUTE_CAPTION(503,"Inactive")
        ROUTE_ACTIVE(500)
        ROUTE_INACTIVE(501)
        ROUTE_INACTIVE(502)
        ROUTE_INACTIVE(503)
    DONE
    ROUTE(501,"2.Trk: A dc10, B dc11") 
        SETLOCO(10) SET_TRACK(A,DC)
        SETLOCO(11) SET_TRACK(B,DC)
        ROUTE_CAPTION(500,"Inactive")
        ROUTE_CAPTION(501,"Active")
        ROUTE_CAPTION(502,"Inactive")
        ROUTE_CAPTION(503,"Inactive")
        ROUTE_INACTIVE(500)
        ROUTE_ACTIVE(501)
        ROUTE_INACTIVE(502)
        ROUTE_INACTIVE(503)
    DONE
    ROUTE(502,"3.Trk: A dc10, B DCC main") 
        SETLOCO(10) SET_TRACK(A,DC)
        SETLOCO(11) SET_TRACK(B,MAIN)
        ROUTE_CAPTION(500,"Inactive")
        ROUTE_CAPTION(501,"Inactive")
        ROUTE_CAPTION(502,"Active")
        ROUTE_CAPTION(503,"Inactive")
        ROUTE_INACTIVE(500)
        ROUTE_INACTIVE(501)
        ROUTE_ACTIVE(502)
        ROUTE_INACTIVE(503)
    DONE
    ROUTE(503,"4.Trk: A DCC main, B dc10") 
        SETLOCO(10) SET_TRACK(A,DC)
        SETLOCO(11) SET_TRACK(B,MAIN)
        ROUTE_CAPTION(500,"Inactive")
        ROUTE_CAPTION(501,"Inactive")
        ROUTE_CAPTION(502,"Inactive")
        ROUTE_CAPTION(503,"Active")
        ROUTE_INACTIVE(500)
        ROUTE_INACTIVE(501)
        ROUTE_INACTIVE(502)
        ROUTE_ACTIVE(503)
    DONE

|force-break|

|hr-dashed|

.. _route_active:

``ROUTE_ACTIVE( route_id )`` - Activate a Route
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Dynamically flag a Route as active.

See example in ROUTE_CAPTION.

*Parameters:* |BR|
|_| > **route_id** - id of the route to activate |BR|

|hr-dashed|

.. _route_inactive:

``ROUTE_INACTIVE( route_id, caption )`` - Deactivate a Route
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Dynamically flag a Route as inactive.

See example in ROUTE_CAPTION.

*Parameters:* |BR|
|_| > **route_id** - id of the route to deactivate |BR|

|hr-dashed|

.. _route_hidden:

``ROUTE_HIDDEN( route_id )`` - Hide a Route from display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Dynamically hide a Route.

*Parameters:* |BR|
|_| > **route_id** - id of the route to hide |BR|

|hr-dashed|

.. _route_disabled:

``ROUTE_DISABLED( route_id )`` - disable a Route
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Dynamically disable a Route.

*Parameters:* |BR|
|_| > **route_id** - id of the route to disable |BR|

|hr-dashed|

.. _stash:

``STASH( stash_id )`` - Stashes the current loco/invert
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

*Parameters:* |BR|
|_| > **stash_id** - id of the stash location to store the value (0-???) |BR|

Stashes/Stores the current loco/invert in the specified stash location.

.. note:: 

  |EX-R| has the ability to switch the DCC direction meaning of FWD and REV so that it can, for example, use the same sequence to drive a normal train or one where the loco is pulling in reverse. If invert=1 in the stash then the loco needs to be moved in reverse in order for the train to move forward.

|hr-dashed|

.. _clear_stash:

``CLEAR_STASH( stash_id )`` - Zeroes the specified stash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Zeroes/Empties the specified stash location.

*Parameters:* |BR|
|_| > **stash_id** - id of the stash location to store the value (0-???) |BR|

|hr-dashed|

.. _clear_all_stash:

``CLEAR_ALL_STASH`` - Zeroes all stashes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Zeroes/Empties all stash locations.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _pickup_stash:

``PICKUP_STASH( stash_id )`` - Retrieves and sets the loco/invert from the specified stash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Retrieves and sets the loco/invert from the specified stash location.

*Parameters:* |BR|
|_| > **stash_id** - id of the stash location to store the value (0-???) |BR|

|hr-dashed|

----

.. _exrail_conditional_statements:

Conditional Statements
----------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

There are numerous conditional statements available to influence activities based on the states of sensors, signals, turnouts/points, and other items.

Any directive on this page starting with ``IF`` must have an associated ``ENDIF`` statement, and optionally an ``ELSE`` statement if an alternative activity is to be performed.

If a conditional statement is part of an automation sequence, the sequence still needs to be terminated with a ``DONE``, ``FOLLOW()``, or ``RETURN`` statement.

This include ``IFNOT()``, ``IFRED()``, ``IFAMBER()``, ``IFGREEN()``, 

Refer also to :ref:`exrail/exrail-command-reference:correct use of done, endif, and follow() statements`.

|hr-dashed|

.. _if:

``IF ( vpin )`` ... ELSE ... ENDIF  - Execute commands if the conditions are met
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the following block of commands if the specified sensor is active.

Optionally be followed by an ``ELSE`` somewhere in the following commands. 
Must be followed by an ``ENDIF`` somewhere in the following commands. 

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to check |BR|

Also see ``IFNOT()``, ``IFRED()``, ``IFAMBER()``, ``IFGREEN()``, ``IFCLOSED()``, ``IFTHROWN()``, ``IFRANDOM()``, ``IFTTPOSITION()``, ``IFRE()``, ``IFTIMEOUT()``, ``IFGTE()``, ``IFLT()``, ``IFLOCO()``, ``IFRESERVE()``

|hr-dashed|

.. _ifnot:

``IFNOT ( vpin )`` ... ELSE ... ENDIF  - Execute commands if the conditions are NOT met
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform the following block of commands if the specified sensor is not active.

Optionally be followed by an ``ELSE`` somewhere in the following commands. 
Must be followed by an ``ENDIF`` somewhere in the following commands. 

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to check |BR|

|hr-dashed|

.. _else:

``ELSE`` - Alternate logic to any IF related command returning False
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Provides alternative logic to any IF related command returning False.

Must be proceeded by an ``IF()`` somewhere in the preceding commands. 
Must be followed by an ``ENDIF`` somewhere in the following commands. 

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _endif:

``ENDIF`` - Required to end an IF/IFNOT/etc.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Required to end an IF/IFNOT/etc. (Used in all IF.. functions).

Optionally be proceeded by an ``ELSE`` somewhere in the preceding commands. 
Must be proceeded by an ``IF()`` somewhere in the preceding commands. 

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _at:

``AT( vpin )`` - Halt command execution until the sensor is set
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Halt the execution of the current block of commands until the sensor is set.

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to check |BR|

|hr-dashed|

.. _after:

``AFTER( vpin [,debounce_time] )`` - Halt command execution until the sensor is cleared 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Halt the execution of the current block of commands until the sensor is cleared.

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to check |BR|
|_| > **debounce_time** -  optional debounce time (default 500mS) |BR|

----

Objects - Definition and Control
================================

Create and manage HAL device objects
------------------------------------

|hr-dashed|

.. _hal:

``HAL( device, parameters )`` - Create a HAL device in myAutomation.h
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a HAL device in myAutomation.h rather than needing to use myHal.cpp

*Parameters:* |BR|
|_| > **device** - device |BR|
|_| > **parameters** -  as needed |BR|

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    // Define a third PCA9685 device following the first two default devices at Vpin 132 and I2C address 0x42
    HAL(PCA9685, 132, 16, 0x42)
    
    // Define a third MCP23017 device following the first two default devices at Vpin 196 and I2C address 0x22
    HAL(MCP23017, 196, 16, 0x22)
    
    // Define a Mega2560 based EX-IOExpander device starting at Vpin 800 at the default I2C address of 0x65
    HAL(EXIOExpander, 800, 62, 0x65)
    
    // Define an EX-Turntable device at the default Vpin 600 and I2C address of 0x60
    HAL(EXTurntable, 600, 1, 0x60)

|hr-dashed|

.. _hal_ignore_defaults:

``HAL_IGNORE_DEFAULTS`` - Disable default MCP23017 and PCA9685 HAL devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Disable default MCP23017 and PCA9685 HAL devices

*Parameters:* |BR|
|_| > none

----

Signal Objects - Definition and Control
---------------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

.. _signal:

``SIGNAL( red_pin, amber_pin, green_pin )`` - Define a pin based signal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a pin based signal, which requires three active low pins to be defined to correspond with red, amber, and green lights. Active low means they are activated when the associated pins are set to 0V or ground.

*Parameters:* |BR|
|_| > **red_pin** - vpin of the red LED. Also defines the signal_id. |BR|
|_| > **amber_pin** - vpin of the amber LED |BR|
|_| > **green_pin** - vpin of the green LED |BR|

|hr-dashed|

.. _signalh:

``SIGNALH( red_pin, amber_pin, green_pin )`` - Define a pin based signal with active high pins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As above to define a pin based signal, but with active high pins instead. Active high means they are activated when the associated pins are set to 5V (or 3.3V if using a 3.3V device).

For both the SIGNAL/SIGNALH commands, signal colour is set using the pin defined for the red pin. If the signal only has two colours (e.g. RED/GREEN), set the unused colour's pin to 0.

*Parameters:* |BR|
|_| > **red_pin** - vpin of the red LED. Also defines the signal_id. |BR|
|_| > **amber_pin** - vpin of the amber LED |BR|
|_| > **green_pin** - vpin of the green LED |BR|

|hr-dashed|

.. _servo_signal:

``SERVO_SIGNAL( vpin, red_pos, amber_pos, green_pos )`` - Define a servo based signal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a servo based signal, such as semaphore signals. Each position is an angle to turn the servo to, similar to the SERVO/SERVO2 commands, and SERVO_TURNOUT

*Parameters:* |BR|
|_| > **vpin** - vpin of the servo |BR|
|_| > **red_pos** - position to move the servo to for a red signal |BR|
|_| > **amber_pos** - position to move the servo to for a amber signal |BR|
|_| > **green_pos** - position to move the servo to for a green signal |BR|

|hr-dashed|

.. _dcc_signal:

``DCC_SIGNAL( id, addr, sub_addr )`` - Define a DCC accessory signal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a DCC accessory signal. Control the colour or aspect of these via the defined ``id``

.. _dccex_signal:

``DCCX_SIGNAL( Address, redAspect, amberAspect, greenAspect )`` - Defines a signal (with id as dcc address)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL| 

This defines a signal (with id same as dcc address) that can be operated
by the RED/AMBER/GREEN commands.   In each case the command uses the signal address to refer to the signal and the aspect chosen depends on the use of the RED AMBER or GREEN command sent. Other aspects may be sent but will require the direct use of the ASPECT command.

The IFRED/IFAMBER/IFGREEN  and ONRED/ONAMBER/ONGREEN commands continue to operate as for any other signal type. It is important to be aware that use of the ASPECT (see below) or <A> commands will correctly set the IF flags and call the ON handlers if ASPECT is used to set one of the three aspects defined in the DCCX_SIGNAL command. 

Direct use of other aspects does not affect the signal flags. ASPECT and <A> can be used without defining any signal if the flag management or ON event handlers are not required.    


|hr-dashed|

.. _virtual_signal:

``VIRTUAL_SIGNAL( id )`` - Define a virtual signal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a virtual signal, which is backed by another automation sequence

*Parameters:* |BR|
|_| > **id** - id (or alias) of the virtual signal |BR|

|hr-dashed|

.. _ifred:

``IFRED( signal_id )`` - Test if signal is red
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test if signal is red.

*Parameters:* |BR|
|_| > **signal_id** - id (or alias) of the virtual signal to test |BR|

|hr-dashed|

.. _ifamber:

``IFAMBER( signal_id )`` - Test if signal is amber
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test if signal is amber

*Parameters:* |BR|
|_| > **signal_id** - id (or alias) of the virtual signal to test |BR|

|hr-dashed|

.. _ifgreen:

``IFGREEN( signal_id )`` - Test if signal is green
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test if signal is green

*Parameters:* |BR|
|_| > **signal_id** - id (or alias) of the virtual signal to test |BR|

|hr-dashed|

.. _green:

``GREEN( signal_id )`` - Set a defined signal to GREEN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set a defined signal to GREEN (see SIGNAL).

*Parameters:* |BR|
|_| > **signal_id** - id (or alias) of the virtual signal to set |BR|

|hr-dashed|

.. _amber:

``AMBER( signal_id )`` - Set a defined signal to Amber
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set a defined signal to Amber (See SIGNAL).

*Parameters:* |BR|
|_| > **signal_id** - id (or alias) of the virtual signal to set |BR|

|hr-dashed|

.. _red:

``RED( signal_id )`` - Set defined signal to Red
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set defined signal to Red (See SIGNAL).

*Parameters:* |BR|
|_| > **signal_id** - id of the virtual signal to set|BR|

|hr-dashed|

.. _aspect:

``ASPECT( address, aspect )`` - Command for DCC Extended Accessories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

This command sends an extended accessory packet to the track, normally used to set
a signal aspect. Aspect numbers are undefined as standards except for 0 which is
always considered a stop.  The exact aspect codes to be used must be determined from the documentation for the accessory decoder in use.

|hr-dashed|

.. _ongreen:

``ONGREEN( signal_id)`` - Define event handler for when a signal is set to the green
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define an event handler for when a signal is set to the green aspect.

*Parameters:* |BR|
|_| > **signal_id** - id (or alias) of the virtual signal to set |BR|

|hr-dashed|

.. _onamber:

``ONAMBER( signal_id)`` - Define event handler for when a signal is set to the amber
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define an event handler for when a signal is set to the amber aspect.

*Parameters:* |BR|
|_| > **signal_id** - id (or alias) of the virtual signal to set |BR|

|hr-dashed|

.. _onred:

``ONRED( signal_id)`` - Define event handler for when a signal is set to the red aspect
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define an event handler for when a signal is set to the red aspect.

*Parameters:* |BR|
|_| > **signal_id** - id (or alias) of the virtual signal to set |BR|

|hr-dashed|

.. collapse:: Signal example: (click to show)

  .. code-block:: cpp

    SIGNAL(25, 26, 27)                // Active low red/amber/green signal using pins 25/26/27 directly on the CommandStation.
    SIGNALH(164 ,0, 165)              // Active high red/green signal using the first two pins of an MCP23017 I/O expander module.
    SERVO_SIGNAL(101, 100, 250, 400)  // Servo based signal using the first PCA9685 servo module.

    GREEN(25)                         // Sets our active low signal to green.
    GREEN(164)                         // Sets our active high signal to green.
    GREEN(101)                        // Sets our servo based signal to green.

|force-break|

----

Turnout/Point Objects - Definition and Control
----------------------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

All the below turnout/point definitions will define turnouts/points that are advertised to |WiThrottle Protocol| apps, |Engine Driver|, and |JMRI|, unless the HIDDEN keyword is used.

"description" is an optional parameter, and must be enclosed in quotes "". If you don't wish this turnout/point to be advertised to throttles, then substitute the word HIDDEN (with no "") instead of the description.

|hr-dashed|

.. _turnout:

``TURNOUT( id, addr, sub_addr [, "description"] )`` - Define a DCC accessory turnout/point
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a DCC accessory turnout/point. Note that DCC linear addresses are not supported, and must be converted to address/subaddress in order to be defined. Refer to the :ref:`reference/downloads/documents:stationary decoder address table (xlsx spreadsheet)` for help on these conversions. (or see TURNOUTL below).

*Parameters:* |BR|
|_| > **id** - identifier of the Turnout/Point |BR|
|_| > **addr** - ranges from 0 to 511 |BR|
|_| > **subaddr** - ranges from 0 to 3 |BR|
|_| > **description** - The description that will be assigned to the turnout/point |BR|


|hr-dashed|

.. _turnoutl:

``TURNOUTL( id, addr [, "description"] )`` - Define a DCC accessory turnout/point
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a DCC accessory turnout/point.  This command will convert a linear address to the address/subaddress format using the TURNOUT command above.

Note when providing the name of the profile that the profile names are case sensitive, and must be written exactly as they appear (e.g. Bounce, not bounce or BOUNCE).

|hr-dashed|

.. _pin_turnout:

``PIN_TURNOUT( id, pin [, "description"] )`` - Define a pin operated turnout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a pin operated turnout. When sending a CLOSE command, the pin will be HIGH, and a THROW command will set the pin LOW.

*Parameters:* |BR|
|_| > **id** - unique Id for the servo |BR|
|_| > **pin** - vpin to which the servo is attached |BR|
|_| > **description** - The description that will be assigned to the turnout/point |BR|

|hr-dashed|

.. _servo_turnout:

``SERVO_TURNOUT( id, pin, active_angle, inactive_angle, profile [, "description"] )`` - Define a servo turnout/point 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a servo turnout/point. "active_angle" is for THROW, "inactive_angle" is for CLOSE, and profile is one of Instant, Fast, Medium, Slow or Bounce (although clearly we don't recommend Bounce for turnouts/points!). 

*Parameters:* |BR|
|_| > **id** - unique Id for the servo |BR|
|_| > **pin** - vpin to which the servo is attached |BR|
|_| > **active_angle** - the PWM value corresponding to the servo position for THROWN state, normally in the range 102 to 490 |BR|
|_| > **inactive_angle** - the PWM value corresponding to the servo position for CLOSED state, normally in the range 102 to 490 |BR|
|_| > **profile** - one of |BR|
|_| |_| |_| |_| • 0=Instant,  |BR|
|_| |_| |_| |_| • 1=Fast (0.5 sec),  |BR|
|_| |_| |_| |_| • 2=Medium (1 sec),  |BR|
|_| |_| |_| |_| • 3=Slow (2 sec) and  |BR|
|_| |_| |_| |_| • 4=Bounce (subject to revision) |BR|
|_| > **description** - The description that will be assigned to the turnout/point |BR|
  
Refer to :doc:`/reference/hardware/servo-module` for more information.

|hr-dashed|

.. _virtual_turnout:

``VIRTUAL_TURNOUT( id [, "description"] )`` - Define a virtual turnout, which is backed by another automation sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a virtual turnout, which is backed by another automation sequence. 
  
For a good example of this refer to :ref:`exrail/tips:realistic turnout sequences`.

*Parameters:* |BR|
|_| > **turnout_id** - The id of the turnout/point |BR|
|_| > **description** - The description that will be assigned to the turnout/point |BR|

|hr-dashed|

.. _ifclosed:

``IFCLOSED( turnout_id )`` - Test if a turnout/point is closed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Parameters:* |BR|
|_| > **turnout_id** - The id of the turnout/point to test |BR|

|hr-dashed|

.. _ifthrown:

``IFTHROWN( turnout_id )`` - Test if a turnout/point is thrown
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test if a turnout is thrown

*Parameters:* |BR|
|_| > **turnout_id** - The id of the turnout/point to test |BR|

|hr-dashed|

.. _onclose:

``ONCLOSE( turnout_id )`` - Event handler for when a turnout/point is closed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Event handler for when a turnout/point is sent a close command. Note that there can be only one defined ONCLOSE event for a specific turnout/point.

*Parameters:* |BR|
|_| > **turnout_id** - The id of the turnout/point |BR|

|hr-dashed|

.. _onthrow:

``ONTHROW( turnout_id )`` - Event handler for when a turnout/point is thrown
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Event handler for when a turnout/point is sent a throw command. Note that there can be only one defined ONTHROW event for a specific turnout/point.

*Parameters:* |BR|
|_| > **turnout_id** - The id of the turnout/point |BR|

|hr-dashed|

.. _close:

``CLOSE( turnout_id )`` - Close a turnout/point
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Closes a defined turnout/point.

*Parameters:* |BR|
|_| > **turnout_id** - The id of the turnout/point to close |BR|

|hr-dashed|

.. _throw:

``THROW( turnout_id )`` - Throw a turnout/point
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Throws a defined turnout/point.

*Parameters:* |BR|
|_| > **turnout_id** - The id of the turnout/point to throw |BR|

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    TURNOUT(100, 26, 0, "Coal Yard")                  // DCC accessory turnout at linear address 101.
    PIN_TURNOUT(101, 164, "Switching Yard")           // Pin turnout on an MCP23017 I/O expander module.
    SERVO_TURNOUT(102, 102, 400, 100, Slow, HIDDEN)   // A servo turnout on a PCA9685 servo module that is hidden from throttles.
    VIRTUAL_TURNOUT(103, "Lumber Yard")               // A virtual turnout which will trigger an automation sequence when CLOSE or THROW is sent.

|hr-dashed|

.. _toggle_turnout:

``TOGGLE_TURNOUT( turnout_id )`` - Toggle a defined turnout/point between CLOSE/THROW
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Toggles the state of the specified turnout/point between closed and thrown.

*Parameters:* |BR|
|_| > **turnout_id** - The id of the turnout/point to throw |BR|

|force-break|

----

Turntable/Traverser Objects - Definition and Control
----------------------------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

Also refer to :ref:`ex-turntable/test-and-tune:exrail automation`.

|hr-dashed|

.. _movett:

``MOVETT( id, steps, activity )`` - Move a |EX-TT| to a step position and perform an activity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Move the specified |EX-TT| to the provided step position and perform the specified activity.

*Parameters:* |BR|
|_| > **id** - The id of the turntable |BR|
|_| > **steps** - The step position to move to |BR|
|_| > **activity** - The activity to perform |BR|

.. note:: 

  From version 5.4.0, we highly recommend using our new turntable/traverser commands which allow turntables/traversers to be advertised to throttles similarly to how turnout/point objects are advertised and operated. Refer to :ref:`exrail/exrail-command-reference:turntable features`.

|hr-dashed|

.. _ifre:

``IFRE ( vpin, value )`` - Test if a rotary encoder has been set to a value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test if a rotary encoder has been set to the specified value

*Parameters:* |BR|
|_| > **vpin** - The VPin the encoder is connected to |BR|
|_| > **value** - value to test |BR|

|hr-dashed|

.. _onchange:

``ONCHANGE( vpin )`` - Detects a rotary encoder has changed position
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Detects a rotary encoder has changed position

*Parameters:* |BR|
|_| > **vpin** - The VPin the encoder is connected to |BR|

.. collapse:: For example: (click to show)

  .. code-block:: 

    ONCHANGE(700)     // If rotary encoder ID 700 change state do this sequence
      IFRE(700, 1)    // If rotary encoder ID 700 is at position 1, start ROUTE ID 123
        START(123)
      ENDIF
      IFRE(700, 2)    // If rotary encoder ID 700 is at position 2, start ROUTE ID 124
        START(124)
      ENDIF
      DONE

|hr-dashed|

Turntable features
^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

All the below turntable/traverser definitions will define turntables/traversers that are advertised to throttles that understand them, unless the HIDDEN keyword is used.

To fully define a turntable/traverser object, you need to define the object first, and then one or more positions.

"description" is an optional parameter, and must be enclosed in quotes "". If you don't wish this turntable/traverser to be advertised to throttles, then substitute the word HIDDEN (with no "") instead of the description.

|hr-dashed|

.. _dcc_turntable:

``DCC_TURNTABLE( id, home_angle, [, "description"] )`` - Define a DCC accessory turntable/traverser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define a DCC accessory turntable/traverser at the specified **id** and the **home_angle** angle.

*Parameters:* |BR|
|_| > **id** - id of the turntable/traverser, valid IDs are 1 - 32767 |BR|
|_| > **home_angle** - the angle of the home position, valid angles are 0 - 3600

|hr-dashed|

.. _extt_turntable:

``EXTT_TURNTABLE( id, vpin, home_angle, [, "description"] )`` - Define an EX-Turntable turntable/traverser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define an EX-Turntable turntable/traverser at the specified **id** and **vpin** with a **home_angle** angle.

This statement will create the |EX-TT| turntable/traverser object only, so you will need a separate ``HAL()`` statement for an |EX-TT| device to create the HAL device. It is not recommended to create it via "myHal.cpp".

The HAL creation will require the **vpin** and **i2c_address** parameters.

*Parameters:* |BR|
|_| > **id** - id of the turntable/traverser, valid IDs are 1 - 32767 |BR|
|_| > **vpin** - id of the vpin where the |EX-TT| device is located |BR|
|_| > **i2c_address** - the |I2C| address of the |EX-TT| device |BR|
|_| > **home_angle** - the angle of the home position, valid angles are 0 - 3600

Example creation and definition:

.. code-block:: 

  HAL(EXTurntable,600,1,0x60)            // Create your EX-Turntable device driver
  EXTT_TURNTABLE(1,600,45,"My EX-Turntable")  // Create your EX-Turntable object to enable control

|hr-dashed|

.. _tt_addposition:

``TT_ADDPOSITION( id, position_id, value, angle [, "description"] )`` - Add a turntable position
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a position to a turntable/traverser object **turntable_id** with position index **position_id**, step or DCC address **value**, **angle** degrees from home.

*Parameters:* |BR|
|_| > **id** - id of the turntable/traverser, which must be created prior to adding positions |BR|
|_| > **position_id** - index of the position to add, valid positions are (1 - 48) |BR|
|_| > **value** - either steps from home for EX-Turntable, or the linear DCC address for a DCC accessory turntable, valid values are (1 - 32767) |BR|
|_| > **angle** - angle of the position from the home position, valid angles are (0 - 3600)

|hr-dashed|

.. _ifttposition:

``IFTTPOSITION( id, position )`` - Test if turntable/traverser is at a position
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tests if the turntable/traverser at the specified **id** is at the specified **position**.

*Parameters:* |BR|
|_| > **id** - id of the turntable/traverser to test. (1 - 32767) |BR|
|_| > **position** - position to rotate to. (1 - 48) 

|hr-dashed|

.. _onrotate:

``ONROTATE( id )`` - Event handler for when a turntable/traverser is rotated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Triggers the event handling mechanism for turntable/traverser **id** if configured. Note that there can be only one defined ONROTATE event for a specific turntable/traverser.

*Parameters:* |BR|
|_| > **id** - id of the turntable/traverser to test (1 - 32767)

|hr-dashed|

.. _rotate:

``ROTATE( id, position, activity )`` - Rotate an EX-Turntable turntable/traverser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rotate an EX-Turntable turntable/traverser at the specified **id** to the specified **position**, and perform **activity**.

*Parameters:* |BR|
|_| > **id** - id of the turntable/traverser, valid IDs are (1 - 32767) |BR|
|_| > **position** - position to rotate to, valid positions are (1 - 48) |BR|
|_| > **activity** - refer to :ref:`ex-turntable/test-and-tune:ex-turntable commands`, using the "EXRAIL activity" column

|hr-dashed|

.. _rotate_dcc:

``ROTATE_DCC( id, position )`` - Rotate a DCC accessory turntable/traverser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rotate a DCC accessory turntable/traverser at the specified **id** to the specified **position**.

*Parameters:* |BR|
|_| > **id** - id of the turntable/traverser, valid IDs are (1 - 32767) |BR|
|_| > **position** - position to rotate to, valid positions are (1 - 48)

|hr-dashed|

.. _waitfortt:

``WAITFORTT( id )`` - Wait for EX-Turntable turntable/traverser to complete a rotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Wait for the EX-Turntable turntable/traverser at **id** to complete a rotation. As no feedback can be received from DCC accessory turntables, this is only valid for EX-Turntable.

*Parameters:* |BR|
|_| > **id** - id of the turntable to test

|force-break|

----

Sensors/Inputs - Reading and Responding
---------------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

.. _jmri_sensor:

``JMRI_SENSOR(vpin [,count])`` - Creates <S> type sensors visible to JMRI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

This command causes the creation of |JMRI| <S> type sensors in a way that is simpler than repeating lines of <S> commands in mySetup.h.

- JMRI_SENSOR(100)   is equivalent to <S 100 100 1>
- JMRI_SENSOR(100,16) will create <S> type sensors for vpins 100-115.

*Parameters:* |BR|
|_| > **vpin** - vpin to create |BR|
|_| > **count** - optional. Number of sensors to create. Inclusive on vpin. Default is one (1) 

|hr-dashed|

``AT( vpin )`` - Causes a sequence to wait until a sensor is active/triggered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A sequence will not progress until a sensor has been triggered.

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to test

|hr-dashed|

``AFTER( vpin )`` - Causes a sequence to wait until after a sensor has been triggered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A sequence will not progress until after a sensor has been triggered and then is off for 0.5 seconds.

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to test

|hr-dashed|

.. _attimeout:

``ATTIMEOUT( vpin, timeout_ms )`` - Causes a sequence to wait until either a sensor is active/triggered, or if the timer runs out
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A sequence will not progress until either a sensor is active/triggered, or if the timer runs out. It then continues and sets a testable "timed out" flag (see ``IFTIMEOUT``).

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to test |BR|
|_| > **timeout_ms** - time/duration to wait for in milliseconds

|hr-dashed|

``IF( vpin )`` - If sensor activated or latched, continue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If sensor activated or latched, continue. Otherwise skip to ELSE or matching ENDIF.

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to test

See the :ref:`Condititional Statments section <exrail_conditional_statements>` for more information on IF ... ELSE ... ENDIF commands.

|hr-dashed|

``IFNOT( vpin )`` - If sensor NOT activated and NOT latched, continue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If sensor NOT activated and NOT latched, continue. Otherwise skip to ELSE or matching ENDIF.

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to test

See the :ref:`Condititional Statments section <exrail_conditional_statements>` for more information on IF ... ELSE ... ENDIF commands.

|hr-dashed|

.. _iftimeout:

``IFTIMEOUT`` - Tests if "timed out" flag has been set by an ATTIMEOUT() sensor reading attempt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tests if "timed out" flag has been set by an ATTIMEOUT() sensor reading attempt.

*Parameters:* |BR|
|_| > none

Note that with the sensor commands `IF()`, `IFNOT()`, `IFTIMEOUT()`, `AT()`, `ATTIMEOUT()`, and `AFTER()`, you can use negative values to enable the use of active HIGH sensors.

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    AT(40)        // Wait for pin 40 to go low.
    AT(-40)       // Wait for pin 40 to go high.

|force-break|

|hr-dashed|

.. _atgte:

``ATGTE( vpin, value )`` - Waits for an analog pin to reach a value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Waits for an analog pin to reach the specified value.

*Parameters:* |BR|
|_| > **vpin** - analogue pin. vpin (or alias) of the sensor to test |BR|
|_| > **value** - value to test against

|hr-dashed|

.. _atlt:

``ATLT ( vpin, value )`` - Waits for an analog pin to go below a value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Waits for an analog pin to go below the specified value.

*Parameters:* |BR|
|_| > **vpin** - analogue pin. vpin (or alias) of the sensor to test |BR|
|_| > **value** - value to test against

|hr-dashed|

.. _ifgte:

``IFGTE( vpin, value )`` - Test if analog pin reading is greater than or equal to value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test if analog pin reading is greater than or equal to value (>=).

*Parameters:* |BR|
|_| > **vpin** - analogue pin. vpin (or alias) of the sensor to test |BR|
|_| > **value** - value to test against

|hr-dashed|

.. _iflt:

``IFLT( vpin, value )`` - Test if analog pin reading is less than value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Test if analog pin reading is less than value (<).

*Parameters:* |BR|
|_| > **vpin** - Analogue pin. vpin (or alias) of the sensor to test |BR|
|_| > **value** - value to test against

  All the `IFGTE()`, `IFLT()`, `ATGTE()`and `ATLT()` commands read the analog value from an analog input pin (A0 - A5 on an Arduino Mega) or an analog input from an I/O expander module. Valid values are defined by the capability of the analog to digital converter in use.


.. collapse:: Sensor examples: (click to show)

  .. code-block:: cpp

    IF(25)          // If sensor on the Command Station pin 25 is activated, set a signal red, wait 10 seconds, then close a turnout/point.
      RED(101)
      DELAY(10)
      CLOSE(200)
    ENDIF

    IFNOT(26)       // If sensor on the Command Station pin 26 is not activated, keep our pedestrian crossing light at 102 green, else set it red.
      GREEN(102)
    ELSE
      RED(102)
    ENDIF

    IFGTE(A2, 512)  // If reading the analog input from a photoelectric light sensor exceeds 512, it's bright enough to turn the street lights off.
      RESET(164)
    ENDIF

    IFLT(A3, 10)   // If current sensing from an analog occupancy detector had dropped below the threshold, turn off our mimic panel light, otherwise turn it on.
      RESET(165)
    ELSE
      SET(165)
    ENDIF

|force-break|

LATCH/UNLATCH can be used to maintain the state of a sensor, or can also be used to trigger a virtual sensor to act as a state flag for EXRAIL. As this effects the state of a sensor, it can be tested via IF/IFNOT and will also work with AT/AFTER.

|hr-dashed|

.. _attimeout1:

``ATTIMOUT1 ( vpin, value )`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo: LOW - EXRAIL doco - ATTIMEOUT1

Waits for ???.

*Parameters:* |BR|
|_| > **vpin** - analogue pin. vpin (or alias) of the sensor to test |BR|
|_| > **value** - value to test against

|hr-dashed|

.. _attimeout2:

``ATTIMOUT2 ( vpin, value )`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo: LOW - EXRAIL doco - ATTIMEOUT2

Waits for ???.

*Parameters:* |BR|
|_| > **vpin** - analogue pin. vpin (or alias) of the sensor to test |BR|
|_| > **value** - value to test against


|hr-dashed|

.. _drive:

``DRIVE ( vpin )`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo: MEDIUM - EXRAIL doco - DRIVE

???

*Parameters:* |BR|
|_| > **vpin** - analogue pin. vpin (or alias) of the sensor to ???

|hr-dashed|

.. _latch:

``LATCH( vpin )`` - Latches a sensor on
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Latches a sensor on (Sensors 0-255 only).

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to unlatch

See UNLATCH() for examples.

|hr-dashed|

.. _unlatch:

``UNLATCH( vpin )`` - Remove LATCH on sensor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remove LATCH on sensor.

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to unlatch

.. collapse:: For example: (click to show)

  In this example, LATCH/UNLATCH is used to toggle between two different activities each time the ROUTE is selected in a WiThrottle:

  .. code-block:: cpp

    TURNOUT(17, 30, 1, "Bay to Shed") // DCC turnout/point with linear address 117

    ALIAS(BayExitStarter, 107)        // Starter Signal with Route board
    ALIAS(ROUTE_TOGGLE, 11)           // State flag to toggle

    ROUTE(11, "Bay to Shed")
      IF(ROUTE_TOGGLE)             // If ROUTE_TOGGLE is active, reset the route
        DEACTIVATEL(BayExitStarter)
        DELAY(20)
        CLOSE(17)
        UNLATCH(ROUTE_TOGGLE)           // UNLATCH (Clear) ROUTE_TOGGLE
      ELSE                            // LATCH is not active, so set route and LATCH
        THROW(17)
        DELAY(20)
        ACTIVATEL(BayExitStarter)
        LATCH(ROUTE_TOGGLE)         // LATCH ROUTE_TOGGLE to indicate route set
      ENDIF
    DONE

.. collapse:: For example: (click to show)

  In this example, LATCH/UNLATCH is used to start/stop a separate running sequence.

  .. code-block:: cpp

      ROUTE(1,"Shuttle")
        SETLOCO(3)
        IF(99) 
          UNLATCH(99) 
          DONE 
        ENDIF
        LATCH(99)
      FOLLOW(2)   // this line is not actully needed

      SEQUENCE(2)
        .... move loco etc
        IF(99) 
          FOLLOW(2) 
        ENDIF
      DONE // will also stop loco

|hr-dashed|

.. _onbutton:

``ONBUTTON( vpin )`` - Event handler for debounced button presses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

This new event handler is handy for mimic panel and other buttons that need to perform an action when a button is pressed, rather than having to create a sequence with a combination of ``AFTER`` and ``IF`` statements to debounce a button which quickly becomes very complicated.

Note that this works for active low buttons only.

*Parameters:* |BR|
|_| > **vpin** - vpin to test

|hr-dashed|

.. _onsensor:

``ONSENSOR( vpin )`` - Event handler for sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

A new event handler to perform actions when a sensor is activated. Like the other sensor triggers such as ``IF``, ``AT``, and ``AFTER``, a negative value can be used for an active high sensor.

*Parameters:* |BR|
|_| > **vpin** - vpin (or alias) of the sensor to test

|force-break|

----

Output and LED control
----------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

.. _set:

``SET( pin [,count] )`` - Set an output pin HIGH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set output pin (set to HIGH)

*Parameters:* |BR|
|_| > **pin** - The first pin number connected that you which to change |BR|
|_| > **count** - optional number of pins to change, starting from and including **pin**. Default is one

|hr-dashed|

.. _reset:

``RESET( pin [,count] )`` - Reset output pin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reset output pin (set to LOW)

*Parameters:* |BR|
|_| > **pin** - The first pin number connected that you which to change |BR|
|_| > **count** - optional number of pins to change, starting from and including **pin**. Default is one

|hr-dashed|

.. _fade:

``FADE( pin, value, ms )`` - Fade an LED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fade an LED on a servo driver to specified value taking specified time.

*Parameters:* |BR|
|_| > **pin** -  pin/vpin of the LED |BR|
|_| > **value** - value to fade the pin to |BR|
|_| > **ms** - duration taken to get to the value in milliseconds

|hr-dashed|

.. _blink:

``BLINK( pin, onMs, offMs )`` - Blink an output pin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

This will start a pin/Vpin blinking until such time as it is ``SET``, ``RESET``, or set via a signal operation.

*Parameters:* |BR|
|_| > **pin** -  pin/vpin of the LED |BR|
|_| > **onMs** - time/duration for the pin to be on in milliseconds |BR|
|_| > **offMs** - off time/duration in milliseconds

  .. code-block:: 

    BLINK(22, 500, 500) // Blink pin 22 at half second intervals

|hr-dashed|

.. _lcn:

``LCN( "msg" )`` - Send message to LCN Accessory Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send message to LCN Accessory Network.

*Parameters:* |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _config_servo:

``CONFIGURE_SERVO(vpin, pos1, pos2, profile)`` - Define LED's connected to PCA9685 boards
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

This command offers a more convenient way of defining an LED connected to a PCA9685 pin, instead of performing the HAL call in halSetup.h

*Parameters:* |BR|
|_| > **vpin** - The VPin the LED is connected to, e.g. 101 for the second pin on the first PCA9685 servo module |BR|
|_| > **pos1** - The desired intensity (brightness) of the LED when turned on, with 0 being off, and 4095 being 100%) |BR|
|_| > **pos2** - The desired intensity (brightness) of the LED when turned off |BR|
|_| > **profile** - the required profile |BR|

*Examples:* |BR|
|_| previously in mySetup.h you would have used: |BR|
|_| IODevice::configureServo(112,2437,0,PCA9685::NoPowerOff); |BR|
|_| Now in myAutomation.h use: |BR| |BR|
|_| CONFIGURE_SERVO(111, 2437, 0, PCA9685::NoPowerOff)


|hr-dashed|

.. _neopixel:

``NEOPIXEL( vpin, red, green, blue [,count] )`` - Controls the colour of attached Neopixel LEDs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Controls the colour of one or more attached Neopixel LEDs

*Parameters:* |BR|
|_| > **vpin** - The VPin the first Neopixel connected that you which to change|BR|
|_| > **red** - The desired red colour value (0-255) |BR|
|_| > **green** - The desired red colour value (0-255) |BR|
|_| > **blue** - The desired red colour value (0-255) |BR|
|_| > **count** - number of Neopixels to change, starting from and including **vpin**. Default is one |BR|

*Examples:* |BR|
|_| NEOPIXEL(100,255,255,255,10)  // set 10 Neopixels LEDs to white starting at vpin 100


|hr-dashed|

.. _neopixel_signal:

``NEOPIXEL_SIGNAL( signalid, red, green, blue )`` - Controls the colour of attached Neopixel LED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Controls the colour of one attached Neopixel LED

*Parameters:* |BR|
|_| > **signalid** - The VPin the first Neopixel connected that you which to change|BR|
|_| > **red** - The desired red colour value (0-255) |BR|
|_| > **green** - The desired red colour value (0-255) |BR|
|_| > **blue** - The desired red colour value (0-255) |BR|

*Examples:* |BR|
|_| NEOPIXEL_SIGNAL(100,255,255,255)  // set one Neopixel LED to white


|hr-dashed|

.. _anout:

``ANOUT( vpin, value, param1, param2)`` - Analog output ??
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

.. todo: LOW - EXRAIL doco - ANOUT


*Parameters:* |BR|
|_| > **vpin** - first VPIN allocated |BR|
|_| > **value** - ??? |BR|
|_| > **param1** - ??? |BR|
|_| > **param2** - ??? |BR|

*Examples:* |BR|
|_| ANOUT(10000,23,0,0) // will play the 23rd mp3 file. |BR|
|_| ANOUT(10000,23,30,0) // will do the same thing, as well as setting the volume to 30 (maximum value).

.. collapse:: For example: (click to show)

  .. code-block:: cpp

      //=======================================================================
      // Play mp3 files from a Micro-SD card, using a DFPlayer MP3 Module.
      //=======================================================================
      // Parameters: 
      //   10000 = first VPIN allocated.
      //   10 = number of VPINs allocated.
      //   Serial1 = name of serial port (usually Serial1 or Serial2).
      // With these parameters, up to 10 files may be played on pins 10000-10009.
      // Play is started from EXRAIL with SET(10000) for first mp3 file, SET(10001)
      // for second file, etc.  Play may also be initiated by writing an analogue
      // value to the first pin, e.g. ANOUT(10000,23,0,0) will play the 23rd mp3 file.
      // ANOUT(10000,23,30,0) will do the same thing, as well as setting the volume to 
      // 30 (maximum value).
      // Play is stopped by RESET(10000) (or any other allocated VPIN).
      // Volume may also be set by writing an analogue value to the second pin for the player, 
      // e.g. ANOUT(10001,30,0,0) sets volume to maximum (30).
      // The EXRAIL sequence may check for completion of play by calling WAITFOR(pin), which will only proceed to the
      // following line when the player is no longer busy.
      // E.g.
      //    SEQUENCE(1)
      //      AT(164)           // Wait for sensor attached to pin 164 to activate
      //      SET(10003)        // Play fourth MP3 file
      //      LCD(4, "Playing") // Display message on LCD/OLED
      //      WAITFOR(10003)    // Wait for playing to finish
      //      LCD(4, "")       // Clear LCD/OLED line 
      //      FOLLOW(1)         // Go back to start

      // DFPlayer::create(10000, 10, Serial1);

|hr-dashed|

.. _playsound:

``PLAY_SOUND( vpin, fileNumber, volume, ??? )`` - Play mp3 files from a Micro-SD card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Play mp3 files from a Micro-SD card, using a DFPlayer MP3 Module.

Alias of ANOUT.

*Parameters:* |BR|
|_| > **vpin** - first VPIN allocated |BR|
|_| > **fileNumber** - number of VPINs allocated |BR|
|_| > **volume** - volume (0-30) |BR|
|_| > **???** - ??? TBA |BR|

----

Servo Control
-------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

.. _servo:

``SERVO( id, position, profile )`` - Move an animation servo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Move an animation servo. *Do NOT use for Turnouts/points.*

*Parameters:* |BR|
|_| > **id** - id of the servo to move |BR|
|_| > **position** - position to move to |BR|
|_| > **profile** - one of |BR|
|_| |_| |_| |_| • Instant,  |BR|
|_| |_| |_| |_| • Fast (0.5 sec),  |BR|
|_| |_| |_| |_| • Medium (1 sec),  |BR|
|_| |_| |_| |_| • Slow (2 sec) and  |BR|
|_| |_| |_| |_| • Bounce (subject to revision) |BR|

|hr-dashed|

.. _servo2:

``SERVO2( id, position, duration )`` - Move an animation servo taking duration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Move an animation servo taking duration in milliseconds. *Do NOT use for Turnouts/points*

*Parameters:* |BR|
|_| > **id** - id of the servo to move |BR|
|_| > **position** - position to move to |BR|
|_| > **duration** - duration of the move in milliseconds|BR|

|hr-dashed|

.. _waitfor:

``WAITFOR( pin )`` - Wait for a servo motion to complete prior to continuing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The WAITFOR() command instructs EXRAIL to wait for a servo motion to complete prior to continuing.

*Parameters:* |BR|
|_| > **pin** - vpin to test


.. collapse:: A couple of examples: (click to show)

  .. code-block:: cpp

    // First example defines a servo turnout/point for the coal yard and a signal for the main line.
    TURNOUT(100, 26, 0, "Coal Yard")
    SIGNAL(25, 26, 27)

    // When our turnout/point is closed, the main line is open, so the signal is green.
    ONCLOSE(100)
      GREEN(25)
    DONE

    // When our turnout is closed, the main line is interrupted, so the signal is red.
    ONTHROW(100)
      RED(25)
    DONE

    // This example triggers an automation sequence when a DCC accessory decoder is activated, including waiting for SERVO motions to complete.
    ONACTIVATEL(100)            // Activating DCC accessory decoder with linear address 100 commences the sequence.
      SERVO(101, 400, Slow)     // Move the first servo and wait.
      WAITFOR(101)
      SERVO(102, 300, Medium)   // Move the second servo and wait.
      WAITFOR(102)
      SET(165)                  // Activate a Vpin to turn an LED on.
      SET(166)                  // Activate a second Vpin to turn a second LED on.
    DONE

|force-break|

----

DCC Accessory Decoder Control
------------------------------

.. contents:: In This Section
  :depth: 4
  :local:
  :class: in-this-section

|hr-dashed|

.. _onactivate:

``ONACTIVATE( addr, sub_addr )`` - Event handler for 2 part DCC accessory packet value 1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Event handler for 2 part DCC accessory packet value 1

All these "ON" commands are event handlers that trigger a sequence of commands to run when the event occurs. These can vary from the most basic tasks such as setting signals when turnouts are closed or thrown, to triggering complete automation sequences via a DCC accessory decoder.

*Parameters:* |BR|
|_| > **addr** - DCC address ??? |BR|
|_| > **Sub_addr** - sub-address ???

|hr-dashed|

.. _onactivatel:

``ONACTIVATEL( linear )`` - Event handler for linear DCC accessory packet value 1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Event handler for linear DCC accessory packet value 1

All these "ON" commands are event handlers that trigger a sequence of commands to run when the event occurs. These can vary from the most basic tasks such as setting signals when turnouts are closed or thrown, to triggering complete automation sequences via a DCC accessory decoder.

*Parameters:* |BR|
|_| > **linear** - ???

|hr-dashed|

.. _ondeactivate:

``ONDEACTIVATE( addr, sub_addr )`` - Event handler for 2 part DCC accessory packet value 0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Event handler for 2 part DCC accessory packet value 0

All these "ON" commands are event handlers that trigger a sequence of commands to run when the event occurs. These can vary from the most basic tasks such as setting signals when turnouts are closed or thrown, to triggering complete automation sequences via a DCC accessory decoder.

*Parameters:* |BR|
|_| > **addr** - DCC address ??? |BR|
|_| > **Sub_addr** - sub-address ???

|hr-dashed|

.. _ondeactivatel:

``ONDEACTIVATEL( linear )`` - Event handler for linear DCC accessory packet value 0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Event handler for linear DCC accessory packet value 0.

*Parameters:* |BR|
|_| > **linear** - ???

|hr-dashed|

.. _activate:

``ACTIVATE( addr, sub_addr )`` - Sends a DCC accessory packet with value 1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a DCC accessory packet with value 1.

*Parameters:* |BR|
|_| > **addr** - DCC address ??? |BR|
|_| > **Sub_addr** - sub-address ???

|hr-dashed|

.. _activatel:

``ACTIVATEL( linear )`` - Sends a DCC accessory packet with value 1 to a linear address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a DCC accessory packet with value 1 to a linear address.

*Parameters:* |BR|
|_| > **linear** - ???

|hr-dashed|

.. _deactivate:

``DEACTIVATE( addr, sub_addr )`` - Sends a DCC accessory packet with value 0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a DCC accessory packet with value 0.

*Parameters:* |BR|
|_| > **addr** - DCC address ??? |BR|
|_| > **Sub_addr** - sub-address ???

|hr-dashed|

.. _deactivatel:

``DEACTIVATEL( addr )`` - Sends a DCC accessory packet with value 0 to a linear address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a DCC accessory packet with value 0 to a linear address

*Parameters:* |BR|
|_| > **addr** - DCC address ??? 

|hr-dashed|

.. _dccactivate:

``DCCACTIVATE( addr, sub_addr )`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo: LOW - EXRAIL doco - DCCACTIVTE

*Parameters:* |BR|
|_| > **addr** - DCC address ??? |BR|
|_| > **Sub_addr** - sub-address ???


|hr-dashed|

.. _xfon:

``XFON( cab, func )``` - Send DCC function ON to specific cab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send DCC function ON to specific cab (e.g. coach lights) *Not for Loco use - use FON instead!*

All these "ON" commands are event handlers that trigger a sequence of commands to run when the event occurs. These can vary from the most basic tasks such as setting signals when turnouts are closed or thrown, to triggering complete automation sequences via a DCC accessory decoder.

*Parameters:* |BR|
|_| > **cab** - DCC address of your loco |BR|
|_| > **func** - Function number (0-31)

|hr-dashed|

.. _xfoff:

``XFOFF( cab, func )`` - Send DCC function OFF to specific cab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send DCC function OFF to specific cab (e.g. coach lights) Not for Loco use - use FON instead!

All these "ON" commands are event handlers that trigger a sequence of commands to run when the event occurs. These can vary from the most basic tasks such as setting signals when turnouts are closed or thrown, to triggering complete automation sequences via a DCC accessory decoder.

*Parameters:* |BR|
|_| > **cab** - DCC address of your loco |BR|
|_| > **func** - Function number (0-31)

|hr-dashed|

.. _xftoggle:

``XFTOGGLE( loco, func )`` - Toggle DCC function on specific loco
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Toggle DCC function on loco with the specified DCC address.

*Parameters:* |BR|
|_| > **loco** - DCC address of your loco |BR|
|_| > **func** - Function number (0-31)

----

EX-FastClock Event Handlers
---------------------------

.. contents:: In This Section
  :depth: 4
  :local:
  :class: in-this-section

Also refer to :ref:`ex-fastclock/cs-commands:controlling exrail by time`.

|hr-dashed|

.. _ontime:

``ONTIME( value )`` - Event handler for when the specified time is reached
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo: MEDIUM - EXRAIL doco - ONTIME

Event handler for when the specified time is reached

*Parameters:* |BR|
|_| > **value** - value to test against

|hr-dashed|

.. _onclocktime:

``ONCLOCKTIME( hours, mins )`` - Event handler for when the specified clock time is reached
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Event handler for when the specified clock time is reached

*Parameters:* |BR|
|_| > **hour** - hour to test against |BR|
|_| > **minute** - minute to test against

|hr-dashed|

.. _onclockmins:

``ONCLOCKMINS( mins )`` - Event handler to be repeated the same time every hour
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Event handler to be repeated the same time every hour

*Parameters:* |BR|
|_| > **minute** - minute to test against

----

Locos and Tracks
================

Locos - Definition and Control
------------------------------

.. contents:: In This Section
  :depth: 4
  :local:
  :class: in-this-section

|hr-dashed|

.. _estop:

``ESTOP`` - Emergency stops all locomotives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Emergency stops all locomotives.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _setloco:

``SETLOCO( loco )`` - Set the loco address for this task
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the loco address for this sequence.

*Parameters:* |BR|
|_| > **loco** - DCC address of your loco 

|hr-dashed|

.. _sendloco:

``SENDLOCO( loco, route )`` - Start route/sequence with a specified loco 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start a new task send a specified loco along a specified route/sequence

*Parameters:* |BR|
|_| > **loco** - DCC address of your loco |BR|
|_| > **route** - route to execute using the specified loco

|hr-dashed|

.. _read_loco:

``READ_LOCO`` - Read loco ID from prog track
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Read the loco ID from prog track.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _fwd:

``FWD( speed )`` - Drive loco forward at DCC speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Drive loco forward at DCC speed 0-127 (1=ESTOP)

*Parameters:* |BR|
|_| > **speed** - DCC speed (0-127) |BR|
|_| |_| |_| |_| • 2-127 = speed 1-126  |BR|
|_| |_| |_| |_| • 0 = stop  |BR|
|_| |_| |_| |_| • 1 = Estop

|hr-dashed|

.. _rev:

``REV( speed )`` - Drive loco in reverse at DCC speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Drive current loco in reverse at DCC speed 0-127 (1=ESTOP)

*Parameters:* |BR|
|_| > **speed** - DCC speed (0-127) |BR|
|_| |_| |_| |_| • 2-127 = speed 1-126  |BR|
|_| |_| |_| |_| • 0 = stop  |BR|
|_| |_| |_| |_| • 1 = Estop

|hr-dashed|

.. _speed:

``SPEED( speed )`` - Drive loco in current direction at DCC speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Drive loco in current direction at DCC speed

*Parameters:* |BR|
|_| > **speed** - DCC speed (0-127) |BR|
|_| |_| |_| |_| • 2-127 = speed 1-126  |BR|
|_| |_| |_| |_| • 0 = stop  |BR|
|_| |_| |_| |_| • 1 = Estop

|hr-dashed|

.. _stop:

``STOP`` - Set loco speed to 0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the current loco speed to 0 (same as SPEED(0))

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _fon:

``FON( func )`` - Turn on loco function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Turn on the specified function for the current loco.

*Parameters:* |BR|
|_| > **func** - Function number (0-31)

|hr-dashed|

.. _foff:

``FOFF( func )`` - Turn off loco function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Turn off the specified function for the current loco.

*Parameters:* |BR|
|_| > **func** - Function number (0-31)

|hr-dashed|

.. _ftoggle:

``FTOGGLE( func )`` - Toggle the state of a loco's function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Toggle off the specified function for the current loco.  i.e. Turn off if on, or on if off.

*Parameters:* |BR|
|_| > **func** - Function number (0-31)

|hr-dashed|

.. _invert_direction:

``INVERT_DIRECTION`` - Switches FWD/REV meaning for loco
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Switches FWD/REV meaning for the current loco.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _roster:

``ROSTER( loco, "name", "func_map" )`` - Provide roster info for a specified loco
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Parameters:* |BR|
|_| > **loco** - DCC address of your loco
|_| > **name** - the name of this loco that will appear in the throttle apps. Enclosed in quotes (") |BR|
|_| > **funct_map** - the names that you want to see for the functions specific to this loco separated by forward slashes ("/"). All enclosed in quotes (") |BR|
|_| |_| |_| |_| Note that if the function is 'momentary' rather than 'latching' (On/Off) then start the function label with a asterisk (*). The most common example of this is the Horn/Whistle which is commonly on F2. |BR|

*Examples:* |BR|
|_| ROSTER (  3,"Eng 3", "F0/F1/\*F2/\*F3/F4/F5/F6/F7/Mute/F9//") // Address 3, Eng 3, Function keys F0-F10 |BR|
|_| ROSTER(1224,"PE 1224","") // Motor Only Decoder |BR|
|_| ROSTER(1225,"PE 1225","Lights/Bell/\*Whistle/\*Short Whistle/Steam/On-Time/FX6 Bell Whistle/Dim Light/Mute") |BR|
|_| ROSTER(4468,"LNER 4468","//Snd On/\*Whistle/\*Whistle2/Brake/F5 Drain/Coal Shvl/Guard-Squeal/Loaded/Coastng/Injector/Shunt-Door \~Opn-Cls/Couplng/BrakeVlv/Sfty Vlv/Shunting/BrkSql Off/No Momentm/Aux3/Fade Out/F22 Res/F23/Res//Aux 5/Aux6/Aux7/Aux 8")

|hr-dashed|

.. _pom:

``POM( cv, value )`` - Program CV value on main
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Program CV value on main, must be proceeded by setting the loco ID with ``SETLOCO( loco )``

|hr-dashed|

.. _ifloco:

``IFLOCO( loco )`` - perform commands if the specified loco ID is defined for this sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the specified loco ID is defined for this sequence, perform the defined activities

*Parameters:* |BR|
|_| > **loco** - DCC Address of the loco to test against

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    // A defined automation sequence that will do activities only if loco ID 123 is in use
    AUTOSTART AUTOMATION(1, "Do stuff for loco 123")
      IFLOCO(123)
        // Define activities here e.g. blow horn or whistle
      ENDIF
      DONE

|force-break|

|hr-dashed|

.. _forget:

``FORGET`` - Forget the loco in the running automation/sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forget the loco in the running automation/sequence

*Parameters:* |BR|
|_| > none

----

TrackManager Control
--------------------

.. contents:: In This Section
  :depth: 4
  :local:
  :class: in-this-section

|hr-dashed|

.. _set_track:

``SET_TRACK( track, mode )`` - Configures the mode of a track
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configures the mode of the selected track, refer also to :doc:`/trackmanager/index`

*Parameters:* |BR|
|_| > **track** - - The track to configure, valid options are A to H |BR|
|_| > **mode** - - The mode to set the track to, |BR|
|_| |_| |_| |_| valid options for |DCC| are: |BR|
|_| |_| |_| |_| • ``MAIN`` or |BR|
|_| |_| |_| |_| • ``MAIN_INV`` or |BR|
|_| |_| |_| |_| • ``MAIN_AUTO`` or |BR|
|_| |_| |_| |_| • ``PROG``, |BR|
|_| |_| |_| |_| and valid options for |DC| are: |BR|
|_| |_| |_| |_| •  ``DC`` or |BR|
|_| |_| |_| |_| •  ``DC_INV`` or |BR|
|_| |_| |_| |_| •  ``DCX`` (same as DC_INV). |BR|
|_| |_| |_| |_| If a track is unused, it can be set to: |BR| 
|_| |_| |_| |_| • ``NONE``, |BR|
|_| |_| |_| |_| If the |EX-CS| is confgured as a Booster (ESP32 Microcontrollers only), it can be set to: |BR| 
|_| |_| |_| |_| • ``BOOST`` or |BR|
|_| |_| |_| |_| • ``BOOST_INV`` or |BR|
|_| |_| |_| |_| • ``BOOST_AUTO``. |BR|

.. flat-table::
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - :cspan:`1` Option
    - _INV
    - _AUTO
    - Notes

  * - ``MAIN``
    - ✓
    - ✓
    - ✓
    -

  * - ``PROG``
    - ✓
    - 
    -
    - 

  * - ``DC``
    - ✓
    - ✓ [1]_
    - ✓
    - Motor drivers with brake pin only

  * - ``BOOST``
    - ✓
    - ✓
    - ✓
    - ESP32 microcontrollers only

  * - ``EXT``
    - ✓
    - 
    -
    - Reserved for future use

  * - ``NONE``
    - ✓
    -
    - 
    - 

.. [1] With special alias of ``DCX`` for ``DC_INV``


When setting at track mode to either ``DC`` or ``DC_INV`` / ``DCX``, you must use the ``SETLOCO( loco )`` command first to specify the loco ID that will be used for the DC track then SET_TRACK()

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    // Set both tracks A and B to be main DCC tracks
    AUTOSTART
    SET_TRACK(A, MAIN)
    SET_TRACK(B, MAIN)
    DONE

    // Set track A to be a DC track with loco ID 1, and track B to be a DCC programming track
    AUTOSTART
    SETLOCO(1) SET_TRACK(A, DC)
    SET_TRACK(B, PROG)
    DONE


.. _set_power:

``SET_POWER( track, ON/OFF )`` - Enable/Disable power on a track
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configures the power setting of the selected track, refer also to :doc:`/trackmanager/index`

*Parameters:* |BR|
  |_| > **track** - - The track to configure, valid options are A to H |BR|
  |_| > **ON/OFF** - - Turn the power ON or OFF for this track |BR|

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    // Set track A to be a DC track with loco ID 1 and power on, and track B to be a DCC programming track
    AUTOSTART
    SETLOCO(1) SET_TRACK(A, DC)
    SET_TRACK(B, PROG)
    SET_POWER(A, ON)
    DONE

.. _setfreq:

``SETFREQ( track, frequency )`` - Enable a specific frequency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``DC`` or ``DC_INV`` / ``DCX`` track settings only.

Configures the frequency setting of the selected track.

The settings achievable vary slightly depending upon the processor running the Command Station but broadly follow the following:

*Parameters:* |BR|
|_| > **track** - - The track to configure, valid options are A to H |BR|
|_| > **frequency** - - The frequency to set for this track |BR|
|_| |_| |_|>valid options are: |BR|
|_| |_| |_| |_|> **0** - Default - low frequency 131Hz |BR|
|_| |_| |_| |_|> **1** - Mid frequency - 490Hz |BR|
|_| |_| |_| |_|> **2** - High frequency - 3400Hz |BR|
|_| |_| |_| |_|> **3** - Supersonic - 62500Hz |BR|

Trial and error will be needed for specific locos that do not respond well to the defaults (low) frequency setting.

|force-break|

----

Controlling Overload/Shorts
---------------------------

.. contents:: In This Section
  :depth: 4
  :local:
  :class: in-this-section

|hr-dashed|

.. _onoverload:

``ONOVERLOAD( track )`` - Event handler for when an Overload occurs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Creates an event handler for the selected track, to be executed when the MotorDriver routines detect and overload. Refer also to :doc:`/trackmanager/index`

*Parameters:* |BR|
|_| > **track** - - The track to configure, valid options are A to H

|hr-dashed|

.. _afteroverload:

``AFTEROVERLOAD( track )`` - Event handler for when an Overload clears
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a complementary event handler for the selected track, to be executed when the MotorDriver routines indicate the overload is cleared. Refer also to :doc:`/trackmanager/index`

Note:  AFTEROVERLOAD is only relevant when used within and ONOVERLOAD.... DONE structure.

*Parameters:* |BR|
|_| > **track** - - The track to configure, valid options are A to H

|hr-dashed|

The power calculation routines within |DCC-EX| will check for shorts and overloads and will change the state of the power produced by the MotorDriver board to protect both it and locos from damage.  This is usually eveident by the LED's on the MotorDriver board flashing.  However some users may wish to see some physical notifcation of these events.  This can now be achieved with EXRAIL and the ONOVERLOAD event.


.. collapse:: For example: (click to show)

  This first example shows a warning message to an attached screen with an LED being illuminated to warn the user of the overload.  Once the overload is cleared the AFTEROVERLOAD code is run automatically.
  
  .. code-block:: cpp

    ONOVERLOAD(A)       // the EXRAIL statement to control the event.
      SCREEN(2,0, "OVERLOAD ON TRACK A")     // A message to the second screen
      PRINT("Overload Detected on Track A")   // Message to system moniter
      SET(27)                                 // Turn on an LED perhaps
      AFTEROVERLOAD(A)
          SCREEN(2,0, "RESTORE A POWER ON")
          PRINT("Overload Cleared on A - Power Restored")
          RESET(27)                           // Turn off the LED
          DELAY(2000)
          SCREEN(2,0, "                  ")   // Clear the screen message
    DONE

  If the user wishes to turn off power whilst he/she investigates the problem, then this can be achieved using the second example below.  POWEROFF can be used, but this will turn off powere to all tracks.  Power to the track with the problem can be turned off with a TrackManager command.  However in order to execute the AFTEROVERLOAD routine it is necessary to have a reset routine.

  .. code-block:: cpp

    // This is the event triggered by an overload.  AFTEROVERLOAD cannot be triggered whilst power is OFF.
    ONOVERLOAD(A)
      SCREEN(2,0, "OVERLOAD A POWEROFF")
      PRINT("Overload Detected on A - Turn Off Power")
      SET_TRACK(A, NONE)   // Unsets the TrackManager assignment and turns off power.
      SET(27)              // Light the LED
      AFTEROVERLOAD(A)
          SCREEN(2,0, "RESTORE A POWER ON")
          PRINT("Overload Cleared on A - Power Restored")
          RESET(27)
          DELAY(2000)
          SCREEN(2,0, "                  ")
    DONE

    // The following turns the poweron and allows the AFTEROVERLOAD to run
    // This could also be achieved with a physical button and AFTER(pin) in place of ROUTE()
    ROUTE(12,"Reset A")
      SCREEN(2,0,"                  ")
      SET_TRACK(A, MAIN)
      POWERON
    DONE
    

|force-break|

----

Virtual Block Control
---------------------

.. contents:: In This Section
  :depth: 4
  :local:
  :class: in-this-section

|hr-dashed|

.. _reserve:

``RESERVE( block_id )`` - Reserve a block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reserve a block (0-255). If already reserved, current loco will STOP and sequence waits for block to become free

*Parameters:* |BR|
|_| > **block_id** - Block to reserve (0-255)

|hr-dashed|

.. _free:

``FREE( block_id )`` - Free block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Free previously reserved block.

*Parameters:* |BR|
|_| > **block_id** - Block to free (0-255)

|hr-dashed|

.. _ifreserve:

``IFRESERVE( block )`` - Execut commnads if block is NOT reserved
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If block is NOT reserved, reserves it and run commands in IF block. Otherwise, skip to matching ENDIF

*Parameters:* |BR|
|_| > **block_id** - Block to test (0-255)

----

System
======

Communication and Display Functions
-----------------------------------

.. contents:: In This Section
  :depth: 4
  :local:
  :class: in-this-section

|hr-dashed|

.. _lcd:

``LCD( row, "msg" )`` - Write message on LCD/OLED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Write message on LCD/OLED, if fitted.

*Parameters:* |BR|
|_| > **row** - row of the LED/OLD to write the message |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _screen:

``SCREEN( display, row, "msg" )`` - Writes a message to a display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes a message to the specified display on the specified row.

*Parameters:* |BR|
|_| > **display** - which display to write to ??? |BR|
|_| > **row** - row of the LED/OLD to write the message |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _broadcast:

``BROADCAST( "msg" )`` - Broadcast to all throttles/JMRI on serial and WiFi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Broadcast to all throttles/JMRI on serial and WiFi

*Parameters:* |BR|
|_| > **msg** - message to broadcast

|hr-dashed|

.. _print:

``PRINT( "msg" )`` - Print diagnostic message to Serial Monitor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Write a diagnostic message to the |serial monitor|.

*Parameters:* |BR|
|_| > **msg** - message to write


|hr-dashed|

.. _serial:

``SERIAL( "msg" )`` - Writes direct to Serial
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes direct to Serial (Serial0/USB)

*Parameters:* |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _serial1:

``SERIAL1( "msg" )`` - Writes direct to Serial1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes direct to Serial1.

*Parameters:* |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _serial2:

``SERIAL2( "msg" )`` - Writes direct to Serial2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes direct to Serial2.

*Parameters:* |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _serial3:

``SERIAL3( "msg" )`` - Writes direct to Serial3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes direct to Serial3.

*Parameters:* |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _serial4:

``SERIAL4( "msg" )`` - Writes direct to Serial4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes direct to Serial4.

*Parameters:* |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _serial5:

``SERIAL5( "msg" )`` - Writes direct to Serial5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes direct to Serial5.

*Parameters:* |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _serial6:

``SERIAL6( "msg" )`` - Writes direct to Serial6
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes direct to Serial6.

*Parameters:* |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _withrottle:

``WITHROTTLE( "msg" )`` - Writes a message to WiThrottle clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes a message to WiThrottle clients (alias of ``PRINT``)

A a WiThrottle throttle will receive ``Hmtext``.

*Parameters:* |BR|
|_| > **msg** - message to write

|hr-dashed|

.. _exrail_message:

.. _message:

``MESSAGE( "msg" )`` - Writes a message to all clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

Writes a message to all serial throttles and all WiThrottle Clients.

A |DCC-EX| throttle will receive a broadcast ``<m "text">``, and a WiThrottle throttle will receive ``Hmtext``.

*Parameters:* |BR|
|_| > **msg** - message to write

----

CommandStation Functions
------------------------

.. contents:: In This Section
  :depth: 4
  :local:
  :class: in-this-section

|hr-dashed|

.. _poweron:

``POWERON`` - Power on track and UNJOIN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Turn the track power on and UNJOIN if currently joined.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _poweroff:

``POWEROFF`` - Power off track
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Turn the track power off.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _join:

``JOIN`` - Join PROG and MAIN track outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Join PROG and MAIN track outputs to send the same MAIN DCC signal.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _unjoin:

``UNJOIN`` - Disconnect prog track from main
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disconnect PROG output from MAIN output.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _endexrail:

``ENDEXRAIL`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo: LOW - EXRAIL doco - ENDEXRAIL

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _killall:

``KILLALL`` - Kills all running |EX-R| activities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Kills all running |EX-R| activities

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _parse:

``PARSE( "msg" )`` - Allows parsing of a DCC-EX API command via myAutomation.h
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Allows parsing of a DCC-EX API command via myAutomation.h.  This allows you to include Native DCC-EX Cammands in myAutomation.h where there is no equivalent EXRAIL command.

*Parameters:* |BR|
|_| > **msg** - message to parse

|hr-dashed|

.. _disable_prog:

``DISABLE_PROG`` - Disable programming to save RAM/Flash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disable programming to save RAM/Flash.

*Parameters:* |BR|
|_| > none

|hr-dashed|

.. _io_no_hal:

``IO_NO_HAL`` - Reduce FLASH footprint when HAL features not required
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To reduce FLASH footprint when HAL features not required.

Note: The HAL is disabled by default on Nano and Uno platforms, because of limited flash space.

*Parameters:* |BR|
|_| > none

----

Layout Command Control (LCC)
----------------------------

The following commands have been introduced to support Layout Command Control (LCC) / CBUS.

.. contents:: In This Section
  :depth: 4
  :local:
  :class: in-this-section

|hr-dashed|

.. _onlcc:

``ONLCC(sender, eventid)`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: LOW - EXRAIL doco - ONLCC

*Parameters:* |BR|
|_| > **sender** - TBA |BR|
|_| > **eventid** - TBA

|hr-dashed|

.. _lcc:

``LCC(eventid)`` - TBA
^^^^^^^^^^^^^^^^^^^^^^

.. todo:: LOW - EXRAIL doco - LCC

*Parameters:* |BR|
|_| > **eventid** - TBA

|hr-dashed|

.. _lccx:

``LCCX(senderid,eventid)`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: LOW - EXRAIL doco - LCCX

*Parameters:* |BR|
|_| > **senderid** - TBA |BR|
|_| > **eventid** - TBA

|hr-dashed|

.. _acon:

``ACON(eventid)`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: LOW - EXRAIL doco - ACON

*Parameters:* |BR|
|_| > **eventid** - TBA

|hr-dashed|

.. _acof:

``ACOF(eventid)`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: LOW - EXRAIL doco - ACOF

*Parameters:* |BR|
|_| > **eventid** - TBA

|hr-dashed|

.. _onacon:

``ONACON(eventid)`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: LOW - EXRAIL doco - OACON

*Parameters:* |BR|
|_| > **eventid** - TBA

|hr-dashed|

.. _onacof:

``ONACOF(eventid)`` - TBA
^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: LOW - EXRAIL doco - ONACOF

*Parameters:* |BR|
|_| > **eventid** - TBA

----

Advanced (Engineers only)
=========================

Caution required!
-----------------

Any commands in this section are intended for |engineer| level users that have advanced knowledge of how |EX-R| works, and likely some understanding of C++ coding as well.

If you are unsure on the impacts using anything in this section may have, please reach out to the |DCC-EX| team via the methods listed on our :doc:`/support/contact-us` page.

.. _stealth:

``STEALTH( code )`` - include some C++ code in a ROUTE/SEQUENCE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

**SERIOUS ENGINEERS and ADVANCED C++ USERS ONLY**   |engineer| 

Permits a certain level of C++ code to be embedded as a single step in an EXRAIL sequence.

Please use this option with great care.  If in doubt ask for assistance.

Syntax:
  STEALTH( .. C++ code ..)

.. collapse:: For example: (click to show)

  .. code-block:: cpp

    // run a routine to free any LATCHES that are left on.
    SEQUENCE(999)
          STEALTH(  //RESET ANY LATCHES WE TURNED ON
          for (int i = 1; i <= 255; i++) {
            if (getFlag(i,LATCH_FLAG)) {    //IF LATCH ON
            setFlag(i,0,LATCH_FLAG);      //RESET LATCH
              }
            }  
          )
    RETURN

    then
    CALL(999) inside your onthrow/onclose sections.

|hr-dashed|

.. _stealth_global:

``STEALTH_GLOBAL( code )``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|NEW-IN-V5-4-LOGO-SMALL|

**SERIOUS ENGINEERS and ADVANCED C++ USERS ONLY**   |engineer| 

Inserts code such as static variables and functions that may be utilised by multiple ``STEALTH`` operations.

Please use this option with great care, and you will need to be an advanced C++ user to make use of this command.  If in doubt ask for assistance.
