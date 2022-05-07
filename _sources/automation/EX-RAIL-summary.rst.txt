*************************
EX-RAIL Command Summary
*************************


Notes
========


- *AUTOMATION*, *ROUTE*, and *SEQUENCE* use the same ID number space, so a ``FOLLOW(n)`` command can be used for any of them.
- Sensors and outputs used by AT/AFTER/SET/RESET/LATCH/UNLATCH/SERVO/IF/IFNOT refer directly to Arduino pins, and those handled by I2C expansion.
- Signals also refer directly to pins, and the signal ID (for RED/AMBER/GREEN) is always the same as the RED signal pin.
- It's OK to use sensor IDs that have no physical item in the layout. These can only be LATCHed, tested (IF/IFNOT), or UNLATCHed in the scripts. If a sensor is latched by the script, it can only be unlatched by the script… so ``AT(35) LATCH(35)`` for example, effectively latches sensor 35 on when detected once. Only sensors with ID's 0 to 255 may be LATCHED/UNLATCHED in your script.
- All IDs used in commands and functions will be numbers, or an ALIAS name if configured.
- Most IDs simply need to be unique, however RESERVE/FREE and LATCH/UNLATCH must be in the range 0 - 255.


Command Summary
==================

.. role:: category(strong)
   :class: category

Diagnostics & Control
______________________

There are some diagnostic and control commands added to the <tag> language normally used to control the Command Station over USB, WiFi or Ethernet. You can enter these Commands < > through both the Arduino IDE Serial Monitor and the JMRI Send DCC++ Command pane.

.. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * -  DCC++ EX Commands
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

Automations, Routes and Sequences
__________________________________

.. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * -  EXRAIL Functions
      -  Description
    * -  :category:`--- Script Definition Items ---`
      -
    * -  AUTOMATION( id, "description" )
      -  Start a Automation Sequence and creates a WiThrottles {Handoff} button to automatically send a train along.
    * -  ROUTE( id, "description" )
      -  Start of a Route Sequence and creates a WiThrottles {Set} button to manual drive the train along
    * -  SEQUENCE( id )
      -  A general purpose Sequence for scenic animations, etc.
    * -  ENDTASK or DONE
      -  Completes a Animation/Routes/Sequence Event handler, etc.
    * -  :category:`--- Object definitions ---`
      -
    * -  ALIAS( name, value )
      -  Assign names to values. Can go anywhere in the script
    * -  SIGNAL( red_pin, amber_pin, green_pin )
      -  Define a signal (RED/AMBER/GREEN commands always use the first red_pin as the signal_id for All signal colors)
    * -  SIGNALH(redpin, amberpin, greenpin)
      -  Same as signal but for active-HIGH LEDs
    * -  TURNOUT( id, addr, sub_addr [, "description"] )
      -  Define DCC Accessory turnout
    * -  PIN_TURNOUT( id, pin [, "description"] )
      -  Define pin operated turnout
    * -  SERVO_TURNOUT( id, pin, active_angle, inactive_angle, profile [, "description"] )
      -  Define a servo turnout (profile is one of Instant, Fast, Medium, Slow, or Bounce - bounce is probably not ideal for turnouts!)
    * -  VIRTUAL_TURNOUT( id [, "description"] )
      -  Define a virtual turnout that will be visible to throttles, but refer to an automation sequence rather than a physical turnout.
    * -  SERVO_SIGNAL(vpin, redpos, amberpos, greenpos)
      -  Define a servo signal
    * -  :category:`--- Flow control functions ---`
      -
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
      -  If sensor activated or latched, continue. Otherwise skip to ELSE or matching ENDIF
    * -  IFNOT( sensor_id )
      -  If sensor NOT activated and NOT latched, continue. Otherwise skip to ELSE or matching ENDIF
    * -  IFCLOSED( turnout_id )
      -  Check if turnout is closed
    * -  IFGTE( sensor_id, value )
      -  Test if analog pin reading is greater than or equal to value (>=)
    * -  IFLT( sensor_id, value )
      -  Test if analog pin reading is less than value (<)
    * -  IFRANDOM( percent )
      -  Runs commands in IF block a random percentage of the time
    * -  IFTHROWN( turnout_id )
      -  Test if turnout is thrown
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
    * -  ELSE
      -  Provides alternative logic to any IF related command returning False
    * -  ENDIF
      -  Required to end an IF/IFNOT/etc (Used in all IF.. functions)
    * -  :category:`--- Command Station functions ---`
      -
    * -  POWERON
      -  Power on track, will UNJOIN programming from main
    * -  POWEROFF
      -  Power off track
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
    * -  :category:`--- EX-RAIL functions ---`
      -
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
    * -  ROSTER( loco, name, func_map )
      -  Provide Engine Roster and F-Key info from the Command Station directly to WiThrottle Apps, see :ref:`automation/ex-rail-intro:roster entries` for examples
    * -  DRIVE( analog_pin )
      -  ***Under Construction*** Not complete, DO NOT USE
    * -  :category:`--- Loco DCC functions ---`
      -
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
    * -  :category:`--- Sensor input & event handlers ---`
      -
    * -  AT( sensor_id )
      -  Wait until sensor is active/triggered
    * -  ATTIMEOUT( sensor_id, timeout_ms )
      -  Wait until sensor is active/triggered, or if the timer runs out, then continue and set a testable "timed out" flag
    * -  ATGTE( analogpin, value)
      -  waits for analog pin to reach value
    * -  ATLT (analogpin,value)
      -  waits for analog pin to go below value
    * -  AFTER( sensor_id )
      -  Waits for sensor to trigger and then go off for 0.5 seconds
    * -  LATCH( sensor_id )
      -  Latches a sensor on (Sensors 0-255 only)
    * -  UNLATCH( sensor_id )
      -  Remove LATCH on sensor
    * -  ONCLOSE( turnout_id )
      -  Event handler for turnout close
    * -  ONTHROW( turnout_id )
      -  Event handler for turnout thrown
    * -  ONACTIVATE( addr, sub_addr )
      -  Event handler for 2 part DCC accessory packet value 1
    * -  ONACTIVATEL( linear )
      -  Event handler for linear DCC accessory packet value 1
    * -  ONDEACTIVATE( addr, sub_addr )
      -  Event handler for 2 part DCC accessory packet value 0
    * -  ONDEACTIVATEL( linear )
      -  Event handler for linear DCC accessory packet value 0
    * -  WAITFOR( pin )
      -  Wait for servo to complete movement
    * -  :category:`--- Action output functions ---`
      -
    * -  SET( pin )
      -  Set an output pin (set to HIGH)
    * -  RESET( pin )
      -  Reset output pin (set to LOW)
    * -  CLOSE( turnout_id )
      -  Close a defined turnout
    * -  THROW( id )
      -  Throw a defined turnout
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
    * -  SERVO( vpin, position, profile )
      -  Move an animation servo. Do NOT use for Turnouts. (profile is one of Instant, Fast, Medium, Slow, or Bounce)
    * -  SERVO2( vpin, position, duration )
      -  Move an animation servo taking duration in ms. Do NOT use for Turnouts
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
