.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-R-LOGO|

********************
EX-RAIL Command List
********************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 3
    :local:

Notes
======

- COMMANDS are case sensitive. i.e. they must be in uppercase. Text parameters you provide (aliases,  descriptions) are not
- *AUTOMATION*, *ROUTE*, and *SEQUENCE* use the same ID number space, so a ``FOLLOW(n)`` command can be used for any of them.
- Sensors and outputs used by AT/AFTER/SET/RESET/LATCH/UNLATCH/SERVO/IF/IFNOT refer directly to Arduino pins, and those handled by |I2C| expansion.
- Signals also refer directly to pins, and the signal ID (for RED/AMBER/GREEN) is always the same as the RED signal pin.
- It's OK to use sensor IDs that have no physical item in the layout. These can only be LATCHed, tested (IF/IFNOT), or UNLATCHed in the scripts. If a sensor is latched by the script, it can only be unlatched by the script… so ``AT(35) LATCH(35)`` for example, effectively latches sensor 35 on when detected once. Only sensors with ID's 0 to 255 may be LATCHED/UNLATCHED in your script.
- All IDs used in commands and functions will be numbers, or an ALIAS name if configured.
- Most IDs simply need to be unique, however RESERVE/FREE and LATCH/UNLATCH must be in the range 0 - 255.

.. note:: 

  There are four uses of ID numbers in EX-RAIL:

  - AUTOMATION, ROUTE, and SEQUENCE IDs
  - Turnout IDs
  - Pin IDs - Includes physical pins on the CommandStation, virtual pins (Vpins) on I/O extender modules, and virtual pins that have no physical presence
  - Virtual block IDs as used in RESERVE/FREE

  Therefore, you can have an AUTOMATION, a turnout, a Vpin, and a virtual block all defined with the same ID without issue as these will not relate to each other. This is probably a great reason to consider aliases to avoid confusion.

Conventions used on this page
=============================

- CAPITALISED words - These are EX-RAIL commands and are case sensitive
- lowercase words within () - These are EX-RAIL parameters that must be provided, with multiple parameters separated by a comma ",", for example SEQUENCE(id) or DELAYRANDOM(min_delay, max_delay)
- Quoted "text" - Text within quote marks "" are used as descriptions, and must include the quote characters, for example ROUTE(id, "description") becomes ROUTE(1, "This is the route description")
- Square brackets [] - Parameters within square brackets [] are optional and may be ommitted. If specifying these parameters, do not include the square brackets themselves, for example ALIAS(name[, value]) becomes ALIAS(MY_ALIAS) or ALIAS(MY_ALIAS, 3)
- \| - Use of the \| character means you need to provide one of the provided options only, for example ``<D POWER ON|OFF>`` becomes either ``<D POWER ON>`` or ``<D POWER OFF>``

Command Summary
==================

.. role:: category(strong)
   :class: category

Diagnostics & Control
---------------------

There are some diagnostic and control commands added to the <tag> language normally used to control the Command Station over USB, WiFi or Ethernet. You can enter these Commands < > through both the Arduino IDE Serial Monitor and the |JMRI| Send DCC++ Command pane.

.. list-table::
    :widths: 30 70
    :header-rows: 1
    :class: command-table

    * -  DCC++ Commands
      -  Description
    * -  <D EXRAIL ON|OFF>
      -  Turns on/off diagnostic traces for EX-RAIL events
    * -  </ PAUSE>
      -  Pauses all automation - all locos E-STOP
    * -  </ RESUME>
      -  Resumes all automation - all locos are restarted at the speed when paused
    * -  </ START [loco_addr] route_id>
      -  Starts a new task to send a loco onto a Route, or activate a non-loco Animation or Sequence
    * -  </>
      -  Displays EX-RAIL running task information
    * -  </ KILL task_id>
      -  Kills a currently running script task by ID (use </> to list task IDs)
    * -  </ RESERVE block_id>
      -  Manually reserves a virtual track Block
    * -  </ FREE block_id>
      -  Manually frees a virtual track Block
    * -  </ LATCH sensor_id>
      -  Lock sensor ON, preventing external influence
    * -  </ UNLATCH sensor_id>
      -  Unlock sensor, returning to current external state
    * -  </ ROUTES>
      -  ***Under Construction*** Returns the Routes & Automations control list in WiThrottle format. JMRI integration only!
    * -  </ RED signal_id>
      -  Set the specified signal red
    * -  </ AMBER signal_id>
      -  Set the specified signal amber
    * -  </ GREEN signal_id>
      -  Set the specified signal green

|

Automations, Routes and Sequences
---------------------------------

Script Definition Items 
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 30 70
    :header-rows: 1
    :class: command-table

    * -  EX-RAIL Functions
      -  Description
    * -  AUTOMATION( id, "description" )
      -  Start a Automation Sequence and creates a WiThrottles {Handoff} button to automatically send a train along.
    * -  ROUTE( id, "description" )
      -  Start of a Route Sequence and creates a WiThrottles {Set} button to manual drive the train along
    * -  SEQUENCE( id )
      -  A general purpose Sequence for scenic animations, etc.
    * -  ENDTASK or DONE
      -  Completes a Animation/Routes/Sequence Event handler, etc.

|

Object definitions
^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 30 70
    :header-rows: 1
    :class: command-table

    * -  EX-RAIL Functions
      -  Description
    * -  ALIAS( name[, value ])
      -  Assign names to values. Can go anywhere in the script
    * -  SIGNAL( red_pin, amber_pin, green_pin )
      -  Define a signal (RED/AMBER/GREEN commands always use the first red_pin as the signal_id for All signal colors)
    * -  SIGNALH(redpin, amberpin, greenpin)
      -  Same as signal but for active-HIGH LEDs
    * -  TURNOUT( id, addr, sub_addr [, "description"] )
      -  Define DCC Accessory turnout/point
    * -  PIN_TURNOUT( id, pin [, "description"] )
      -  Define pin operated turnout
    * -  SERVO_TURNOUT( id, pin, active_angle, inactive_angle, profile [, "description"] )
      -  Define a servo turnout (profile is one of Instant, Fast, Medium, Slow, or Bounce - bounce is probably not ideal for turnouts/points!)
    * -  VIRTUAL_TURNOUT( id [, "description"] )
      -  Define a virtual turnout that will be visible to throttles, but refer to an automation sequence rather than a physical turnout/point.
    * -  SERVO_SIGNAL(vpin, redpos, amberpos, greenpos)
      -  Define a servo signal

|

Flow control functions
^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 30 70
    :header-rows: 1
    :class: command-table

    * -  EX-RAIL Functions
      -  Description
    * -  CALL( route )
      -  Branch to a separate sequence expecting a RETURN
    * -  FOLLOW( route )
      -  Branch or Follow a numbered sequence (think of "GOTO")
    * -  RETURN
      -  Return to caller (see CALL)
    * -  DELAY( delay )
      -  Delay a number of milliseconds
    * -  DELAYMINS( delay )
      -  Delay a number of minutes
    * -  DELAYRANDOM( min_delay, max_delay )
      -  Delay a random time between min and max milliseconds
    * -  IF( sensor_id )
      -  If sensor activated or latched, continue, otherwise skip to ELSE/ENDIF, use negative values for active HIGH sensors
    * -  IFNOT( sensor_id )
      -  If sensor NOT activated and NOT latched, continue, otherwise skip to ELSE/ENDIF, use negative values for active HIGH sensors
    * -  IFCLOSED( turnout_id )
      -  Check if turnout/point is closed
    * -  IFGTE( sensor_id, value )
      -  Test if analog pin reading is greater than or equal to value (>=)
    * -  IFLT( sensor_id, value )
      -  Test if analog pin reading is less than value (<)
    * -  IFRANDOM( percent )
      -  Runs commands in IF block a random percentage of the time
    * -  IFTHROWN( turnout_id )
      -  Test if turnout/point is thrown
    * -  IFRESERVE( block )
      -  If block is NOT reserved, reserves it and run commands in IF block. Otherwise, skip to matching ENDIF
    * -  IFTIMEOUT
      -  Tests if "timed out" flag has been set by an ATTIMEOUT sensor reading attempt
    * -  IFRED( signal_id )
      -  Tests if signal is red
    * -  IFAMBER( signal_id )
      -  Tests if signal is amber
    * -  IFGREEN( signal_id )
      -  Tests if signal is green
    * -  IFRE( id, value )
      -  Tests if a rotary encoder is at the specified position |BR| |NOT-IN-PROD-VERSION|
    * -  ELSE
      -  Provides alternative logic to any IF related command returning False
    * -  ENDIF
      -  Required to end an IF/IFNOT/etc (Used in all IF.. functions)

|

Command Station functions
^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 30 70
    :header-rows: 1
    :class: command-table

    * -  EX-RAIL Functions
      -  Description
    * -  POWERON
      -  Power on track, will UNJOIN programming from main |BR| |NOT-IN-PROD-VERSION|
    * -  POWEROFF
      -  Power off track |BR| |NOT-IN-PROD-VERSION|
    * -  JOIN
      -  Joins PROG and MAIN track outputs to send the same MAIN DCC signal on both tracks
    * -  UNJOIN
      -  Disconnect Prog track from Main DCC signal
    * -  READ_LOCO
      -  Read loco ID from Prog track
    * -  POM( cv, value )
      -  Program CV value on main
    * -  LCD( row, msg )
      -  Write message on a LCD/OLED screen if one is declared and used
    * -  BROADCAST ( msg )
      -  Broadcasts the specified text to all connected throttles/JMRI, over both serial and WiFi
    * -  PRINT( msg )
      -  Print diagnostic message to the IDE Serial Monitor and JMRI DCC++ Traffic Monitor
    * -  SERIAL( msg )
      -  Writes direct to Serial (Serial0/USB)
    * -  SERIAL1( msg )
      -  Writes direct to Serial1
    * -  SERIAL2( msg )
      -  Writes direct to Serial2
    * -  SERIAL3( msg )
      -  Writes direct to Serial3

|

EX-RAIL functions
^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 30 70
    :header-rows: 1
    :class: command-table

    * -  EX-RAIL Functions
      -  Description
    * -  PAUSE
      -  E-STOP all locos and PAUSE all other EX-RAIL tasks until RESUMEd
    * -  RESUME
      -  Resume all paused tasks, including loco movement
    * -  RESERVE( block_id )
      -  Reserve a block (0-255). If already reserved, current loco will STOP and script waits for block to become free
    * -  FREE( block_id )
      -  Free previously reserved block
    * -  START( sequence_id )
      -  Start a new task to execute a route or sequence
    * -  SETLOCO( loco )
      -  Set the loco address for this task
    * -  SENDLOCO( loco, route )
      -  Start a new task send a given loco along given route/sequence
    * -  AUTOSTART
      -  A task is automatically started at this point during startup
    * -  PARSE ( command_string)
      -  Processes the command_string as if it had been sent in by a throttle or typed into the USB serial e.g. PARSE("<1 JOIN>")
         
         This is much less efficient than using an equivalent EXRAIL command. So don't use it for anything that EX-RAIL can do directly.
         
         |NOT-IN-PROD-VERSION|
    * -  DRIVE( analog_pin )
      -  ***Under Construction*** Not complete, DO NOT USE 
         
         |NOT-IN-PROD-VERSION|

|

Loco DCC functions
^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 30 70
    :header-rows: 1
    :class: command-table

    * -  EX-RAIL Functions
      -  Description
    * -  ROSTER( loco, name, func_map )
      -  Provide Engine Roster and F-Key info from the Command Station directly to WiThrottle Apps, see :ref:`ex-rail/creating-elements:adding a roster` for examples
    * -  ESTOP
      -  Emergency stop loco
    * -  FWD( speed )
      -  Drive loco forward at DCC speed 0-127 (1=ESTOP)
    * -  REV( speed )
      -  Drive logo in reverse at DCC speed 0-127 (1=ESTOP)
    * -  SPEED( speed )
      -  Drive loco in current direction at DCC speed (0-127)
    * -  STOP
      -  Set loco speed to 0 (same as SPEED(0) )
    * -  FON( func )
      -  Turn on loco function
    * -  FOFF( func )
      -  Turn off loco function
    * -  INVERT_DIRECTION
      -  Switches FWD/REV meaning for this loco

|

Sensor input
^^^^^^^^^^^^

.. list-table::
    :widths: 30 70
    :header-rows: 1
    :class: command-table

    * -  EX-RAIL Functions
      -  Description
    * -  AT( sensor_id )
      -  Wait until sensor is active/triggered, use negative values for active HIGH sensors
    * -  ATTIMEOUT( sensor_id, timeout_ms )
      -  Wait until sensor is active/triggered, or if the timer runs out, then continue and set a testable "timed out" flag, use negative values for active HIGH sensors
    * -  ATGTE( analogpin, value)
      -  waits for analog pin to reach value
    * -  ATLT (analogpin,value)
      -  waits for analog pin to go below value
    * -  AFTER( sensor_id )
      -  Waits for sensor to trigger and then go off for 0.5 seconds, use negative values for active HIGH sensors
    * -  LATCH( sensor_id )
      -  Latches a sensor on (Sensors 0-255 only)
    * -  UNLATCH( sensor_id )
      -  Remove LATCH on sensor
    * -  WAITFOR( pin )
      -  Wait for servo to complete movement
  
|

Event handlers
^^^^^^^^^^^^^^

.. list-table::
    :widths: 30 70
    :header-rows: 1
    :class: command-table

    * -  EX-RAIL Functions
      -  Description
    * -  ONCLOSE( turnout_id )
      -  Event handler for turnout/point close
    * -  ONTHROW( turnout_id )
      -  Event handler for turnout/point thrown
    * -  ONACTIVATE( addr, sub_addr )
      -  Event handler for 2 part DCC accessory packet value 1
    * -  ONACTIVATEL( linear )
      -  Event handler for linear DCC accessory packet value 1
    * -  ONDEACTIVATE( addr, sub_addr )
      -  Event handler for 2 part DCC accessory packet value 0
    * -  ONDEACTIVATEL( linear )
      -  Event handler for linear DCC accessory packet value 0
    * -  ONCHANGE( id )
      -  Event handler for a sensor changing state |BR| |NOT-IN-PROD-VERSION|

|

Action output functions 
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
    :widths: 30 70
    :header-rows: 1
    :class: command-table

    * -  EX-RAIL Functions
      -  Description
    * -  SET( pin )
      -  Set an output pin (set to HIGH)
    * -  RESET( pin )
      -  Reset output pin (set to LOW)
    * -  CLOSE( turnout_id )
      -  Close a defined turnout/point
    * -  THROW( id )
      -  Throw a defined turnout/point
    * -  GREEN( signal_id )
      -  Set a defined signal to GREEN (see SIGNAL)
    * -  AMBER( signal_id )
      -  Set a defined signal to Amber. (See SIGNAL)
    * -  RED( signal_id )
      -  Set defined signal to Red (See SIGNAL)
    * -  FADE( pin, value, ms )
      -  Fade an LED on a servo driver to given value and taking a given time
    * -  LCN( msg )
      -  Send message to LCN Accessory Network
    * -  MOVETT( vpin, steps, activity )
      -  Move a turntable the number of steps relative to home, and perform the activity (refer EX-Turntable documentation)
    * -  SERVO( id, position, profile )
      -  Move an animation servo. Do NOT use for turnouts/points. (profile is one of Instant, Fast, Medium, Slow or Bounce)
    * -  SERVO2( id, position, duration )
      -  Move an animation servo taking duration in ms. |BR| Do NOT use for turnouts/points
    * -  XFON( cab, func )
      -  Send DCC function ON to specific cab (eg coach lights) **Not for Loco use - use FON instead!**
    * -  XFOFF( cab, func )
      -  Send DCC function OFF to specific cab (eg coach lights) **Not for Loco use - use FON instead!**
    * -  ACTIVATE( addr, sub_addr )
      -  Sends a DCC accessory packet with value 1
    * -  ACTIVATEL( linear )
      -  Sends a DCC accessory packet with value 1 to a linear address
    * -  DEACTIVATE( addr, sub_addr )
      -  Sends a DCC accessory packet with value 0
    * -  DEACTIVATEL( addr )
      -  Sends a DCC accessory packet with value 0 to a linear address
