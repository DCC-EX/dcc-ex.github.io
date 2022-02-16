:orphan:

.. Remove orphan field when the document is added to a toctree

****************************
DCC++ EX Command Reference
****************************

This is a detailed reference. For a summary version, please see :doc:`EX-RAIL Command Summary <EX-RAIL-summary>`

`CommandStation-EX <https://github.com/DCC-EX/CommandStation-EX>`_ Provides full automation and accessory control through the Extended Railroad Automation Instruction Language (EX-RAIL). First, make sure you have the latest release of the `CommandStation-EX Firmware <https://github.com/DCC-EX/CommandStation-EX>`_.

See Also:

  :doc:`Introduction to EX-RAIL <EX-RAIL-intro>` 

  :doc:`EX-RAIL Command Summary <EX-RAIL-summary>`

Notes
========


- *ROUTE*, *AUTOMATION* and *SEQUENCE* use the same ID number space, so a ``FOLLOW(n)`` command can be used for any of them.

- Sensors and outputs used by AT/AFTER/SET/RESET/LATCH/UNLATCH/SERVO/IF/IFNOT refer directly to Arduino pins, and those handled by I2C expansion.

- Signals also refer directly to pins, and the signal ID (for RED/AMBER/GREEN) is always the same as the RED signal pin.

- It's OK to use sensor IDs that have no physical item in the layout. These can only be LATCHed, tested (IF/IFNOT), or UNLATCHed in the scripts. If a sensor is latched by the script, it can only be unlatched by the script… so ``AT(35) LATCH(35)`` for example, effectively latches sensor 35 on when detected once.

- All IDs used in commands and functions will be numbers, or an ALIAS name if configured.

|

DIAGNOSTICS AND CONTROL
=======================

There are some diagnostic and control commands added to the <tag> language normally used to control the Command Station over USB, WiFi or Ethernet.

``<D EXRAIL ON|OFF>`` Turns diagnostic traces for EX-RAIL events

  .. code-block:: none

    When the CS is connected to a serial monitor, EX-RAIL script logging can be turned on or off (Enabled or Disabled)

    Example output:

  
``</PAUSE>`` Pause an EX-RAIL Script 

``</RESUME>`` Resume an EX-RAIL Script

``</>`` Displays EX-RAIL running task information

   Example output:

``</ ROUTES>``	Returns the Routes & Automations control list in WiThrottle format. JMRI integration only!

``</ START [loco_addr] route_id>``	Starts a new task to send a loco onto a Route, or activate a non-loco Animation or Sequence

``</ KILL task_id>``	Kills a currently running script task by ID (use to list task IDs)

``</ RESERVE block_id>``	Manually reserves a virtual track Block

``</ FREE block_id>``	Manually frees a virtual track Block

``</ LATCH sensor_id>``	Lock sensor ON, preventing external influence

``</ UNLATCH sensor_id>``	Unlock sensor, returning to current external state



ROUTES, AUTOMATIONS, & SEQUENCES
==================================

EX-RAIL provides many commands to allow you to create routes that locomotives to follow that may involve turnouts, signals, etc. that can be automatically set to react whent the loco trips a sensor.

Script Definition Terms
------------------------

``AUTOMATION( id, "description" )>``	Start of an Automation Sequence which WiThrottles can send a train along

``ROUTE( id, "description" )``	Start of a Route Sequence settable in WiThrottle

``SEQUENCE( id )``	A general purpose Sequence for scenic animations, etc.

``ENDTASK`` or ``DONE``	Completes a Sequence/Route/Animation/Event handler, etc.

Object Definitions
-------------------

``ALIAS( name, value )``	Assign names to values. Can go anywhere in the script

This is a simple substitution that lets you have readable names for things in your script. For example, instead of having to remember the VPin a turnout is connected to, give the pin number an alias and refer to it by that name. You can use this to name routes, values, pin numbers, or anything you need. If you want spaces in an alias, you must enclose it in quotes.

Examples:

ALIAS(coal_yard, 1) or ALIAS("coal yard", 1) then instead of PIN_TURNOUT( id, pin [, "COAL YARD"], write it as PIN_TURNOUT(coal_yard, pin [, "description"]) 

2000 milliseconds is 2 seconds, so with ALIAS(slow, 2000), you could set DELAY(slow).





``SIGNAL( red_pin, amber_pin, green_pin )``	Define a signal (RED/AMBER/GREEN commands always use the red_pin as the signal_id)

``TURNOUT( id, addr, sub_addr [, "description"] )``	Define DCC Accessory turnout

``PIN_TURNOUT( id, pin [, "description"] )``	Define pin operated turnout

``SERVO_TURNOUT( id, pin, active_angle, inactive_angle, profile [, "description"] )``	Define a servo turnout

Flow Control Functions
------------------------

``CALL( route )``	Branch to a separate sequence expecting a RETURN

``FOLLOW( route )``	Branch or Follow a numbered sequence (think of "GOTO")

``RETURN``	Return to caller (see CALL)

``DELAY( delay )``	Delay a number of milliseconds

``DELAYMINS( delay )``	Delay a number of minutes

``DELAYRANDOM( min_delay, max_delay )``	Delay a random time between min and max milliseconds

``IF( sensor_id )``	If sensor activated or latched, continue. Otherwise skip to ELSE or matching ENDIF

``IFNOT( sensor_id )``	If sensor NOT activated and NOT latched, continue. Otherwise skip to ELSE or matching ENDIF

``IFCLOSED( turnout_id )``	Check if turnout is closed

``IFGTE( sensor_id, value )``	Test if analog pin reading is greater than or equal to value (>=)

``IFLT( sensor_id, value )``	Test if analog pin reading is less than value (<)

``IFRANDOM( percent )``	Runs commands in IF block a random percentage of the time

``IFTHROWN( turnout_id )``	Test if turnout is thrown

``IFRESERVE( block )``	If block is NOT reserved, reserves it and run commands in IF block. Otherwise, skip to matching ENDIF

``IFTIMEOUT``	Tests if "timed out" flag has been set by an ATTIMEOUT sensor reading attempt

``ELSE``	Provides alternative logic to any IF related command returning False

``ENDIF``	Required to end an IF/IFNOT/etc (Used in all IF.. functions)

Command Station Functions
--------------------------

``POWEROFF``	Power off track

``JOIN``	Joins PROG and MAIN track outputs to send the same MAIN DCC signal

``UNJOIN``	Disconnect prog track from main

``READ_LOCO``	Read loco ID from prog track

``POM( cv, value )``	Program CV value on main

``LCD( row, msg )``	Write message on LCD/OLED if fitted

``PRINT( msg )``	Print diagnostic message to Serial Monitor

``SERIAL( msg )``	Writes direct to Serial (Serial0/USB)

``SERIAL1( msg )``	Writes direct to Serial1

``SERIAL2( msg )``	Wri1tes direct to Seria2

``SERIAL3( msg )``	Writes direct to Serial3

EX-RAIL Functions
------------------

``PAUSE``	E-STOP all locos and PAUSE all other EX-RAIL tasks until RESUMEd

``RESUME``	Resume all paused tasks, including loco movement

``RESERVE( block_id )``	Reserve a block (0-255). If already reserved, current loco will STOP and script waits for block to become free

``FREE( block_id )``	Free previously reserved block

``START( sequence_id )``	Start a new task to execute a route or sequence

``SETLOCO( loco )``	Set the loco address for this task

``SENDLOCO( cab, route )``	Start a new task send a given loco along given route/sequence

``AUTOSTART``	A task is automatically started at this point during startup

``DRIVE( analog_pin )``	Not complete, DO NOT USE

``ROSTER( cab, name, func_map )``	Provide roster info for WiThrottle

Loco DCC Functions
-------------------

``ESTOP``	Emergency stop loco

``FWD( speed )``	Drive loco forward at DCC speed 0-127 (1=ESTOP)

``REV( speed )``	Drive logo in reverse at DCC speed 0-127 (1=ESTOP)

``SPEED( speed )``	Drive loco in current direction at DCC speed (0-127)

``STOP``	Set loco speed to 0 (same as SPEED(0) )

``FON( func )``	Turn on loco function

``FOFF( func )``	Turn off loco function

``INVERT_DIRECTION``	Switches FWD/REV meaning for this loco

Sensor input and Event Handlers 
--------------------------------

``AT( sensor_id )``	Wait until sensor is active/triggered

``ATTIMEOUT( sensor_id, timeout_ms )``	Wait until sensor is active/triggered, or if the timer runs out, then continue and set a testable "timed out" flag

``AFTER( sensor_id )``	Waits for sensor to trigger and then go off for 0.5 seconds

``LATCH( sensor_id )``	Latches a sensor on (Sensors 0-255 only)

``UNLATCH( sensor_id )``	Remove LATCH on sensor

``ONCLOSE( turnout_id )``	Event handler for turnout close

``ONTHROW( turnout_id )``	Event handler for turnout thrown

``ONACTIVATE( addr, sub_addr )``	Event handler for 2 part DCC accessory packet value 1

``ONACTIVATEL( linear )``	Event handler for linear DCC accessory packet value 1

``ONDEACTIVATE( addr, sub_addr )``	Event handler for 2 part DCC accessory packet value 0

``ONDEACTIVATEL( linear )``	Event handler for linear DCC accessory packet value 0

``WAITFOR( pin )``	Wait for servo to complete movement

Action Output Functions
------------------------

``SET( pin )``	Set an output pin HIGH

``RESET( pin )``	Reset output pin (set to LOW)

``CLOSE( turnout_id )``	Close a defined turnout

``THROW( id )``	Throw a defined turnout

``GREEN( signal_id )``	Set a defined signal to GREEN (see SIGNAL)

``AMBER( signal_id )``	Set a defined signal to Amber. (See SIGNAL)

``RED( signal_id )``	Set defined signal to Red (See SIGNAL)

``FADE( pin, value, ms )``	Fade an LED on a servo driver to given value taking given time

``LCN( msg )``	Send message to LCN Accessory Network

``SERVO( id, position, profile )``	Move an animation servo. Do NOT use for Turnouts. (profile is one of Instant, Fast, Medium, Slow or Bounce)

``SERVO2( id, position, duration )``	Move an animation servo taking duration in ms. Do NOT use for Turnouts

``XFON( cab, func )``	Send DCC function ON to specific cab (eg coach lights) Not for Loco use - use FON instead!

``XFOFF( cab, func )``	Send DCC function OFF to specific cab (eg coach lights) Not for Loco use - use FON instead!

``ACTIVATE( addr, sub_addr )``	Sends a DCC accessory packet with value 1

``ACTIVATEL( linear )``	Sends a DCC accessory packet with value 1 to a linear address

``DEACTIVATE( addr, sub_addr )``	Sends a DCC accessory packet with value 0

``DEACTIVATEL( addr )``	Sends a DCC accessory packet with value 0 to a linear address