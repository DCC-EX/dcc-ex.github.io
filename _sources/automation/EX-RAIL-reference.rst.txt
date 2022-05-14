**************************
EX-RAIL Command Reference
**************************

This is a detailed reference. For a summary version, please see :doc:`EX-RAIL Command Summary <EX-RAIL-summary>`.

`CommandStation-EX <https://github.com/DCC-EX/CommandStation-EX>`_ Provides full automation and accessory control through the Extended Railroad Automation Instruction Language (EX-RAIL). First, make sure you have the latest release of the `CommandStation-EX Firmware <https://github.com/DCC-EX/CommandStation-EX>`_.

See Also:

- :doc:`Introduction to EX-RAIL <EX-RAIL-intro>` 
- :doc:`EX-RAIL Command Summary <EX-RAIL-summary>`

Notes
======


- *AUTOMATION*, *ROUTE*, and *SEQUENCE* use the same ID number space, so a ``FOLLOW(n)`` command can be used for any of them.
- Sensors and outputs used by AT/AFTER/SET/RESET/LATCH/UNLATCH/SERVO/IF/IFNOT refer directly to Arduino pins, and those handled by I2C expansion (as virtual pins or vpins).
- Signals also refer directly to pins, and the signal ID (for RED/AMBER/GREEN) is always the same as the RED signal pin.
- It's OK to use sensor IDs that have no physical item in the layout. These can only be LATCHed, tested (IF/IFNOT), or UNLATCHed in the scripts. If a sensor is latched by the script, it can only be unlatched by the script… so ``AT(35) LATCH(35)`` for example, effectively latches sensor 35 on when detected once.
- All IDs used in commands and functions will be numbers, or an ALIAS name if configured.
- Most IDs simply need to be unique, however RESERVE/FREE and LATCH/UNLATCH must be in the range 0 - 255.

.. note:: 

  There are four uses of ID numbers in EX-RAIL:

  - AUTOMATION, ROUTE, and SEQUENCE IDs
  - Turnout IDs
  - Pin IDs - Includes physical pins on the CommandStation, virtual pins (Vpins) on I/O extender modules, and virtual pins that have no physical presence
  - Virtual block IDs as used in RESERVE/FREE

  Therefore, you can have an AUTOMATION, a turnout, a Vpin, and a virtual block all defined with the same ID without issue as these will not relate to each other. This is probably a great reason to consider aliases to avoid confusion.

DIAGNOSTICS AND CONTROL
========================

There are some diagnostic and control commands added to the <tag> language normally used to control the Command Station over USB, WiFi or Ethernet.

EXRAIL
_______

``<D EXRAIL ON|OFF>`` When the CommandStation is connected to a serial monitor, EX-RAIL script logging can be turned on or off (Enabled or Disabled).

Example output from :ref:`automation/ex-rail-intro:example 6: single line shuttle` running SEQUENCE(13) with loco ID 18:

.. code-block:: 

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
  
PAUSE/RESUME
_____________

``</PAUSE>`` Pauses **ALL** EX-RAIL automation activities, including sending an E-STOP to all locos.

``</RESUME>`` Resumes **ALL** EX-RAIL automation activities, and resumes all locos at the same speed at which they were paused.

Task info
__________

``</>`` Displays EX-RAIL running task information

Example outputs also using :ref:`automation/ex-rail-intro:example 6: single line shuttle`:

* Leaving right side of the shuttle sequence with speed 50F (forward):

.. code-block:: 
  
  </>
  <1 18 0 178 0>
  <* EXRAIL STATUS
  ID=0,PC=12,LOCO=0 ,SPEED=0F
  ID=1,PC=12,LOCO=18 ,SPEED=50F *>

ROUTES
_______

``</ ROUTES>``	Returns the Routes & Automations control list in WiThrottle format.

Example output:

.. code-block:: 

  </ROUTES PRT]\[Routes}|{Route]\[Set}|{2]\[Handoff}|{4
  PRL]\[R1}|{Example 1: Coal Yard exit}|{2]\[A4}|{Example 4: Round in circles}|{4]\[A5}|{Example 5: Round in circles}|{4>

START/KILL
___________

``</ START [loco_addr] route_id>``	Starts a new task to send a loco onto a Route, or activate a non-loco Animation or Sequence

``</ KILL task_id>``	Kills a currently running script task by ID (use to list task IDs)

RESERVE/FREE
_____________

``</ RESERVE block_id>``	Manually reserves a virtual track Block, valid IDs are in the range 0 - 255.

``</ FREE block_id>``	Manually frees a virtual track Block, valid IDs are in the range 0 - 255.

LATCH/UNLATCH
______________

``</ LATCH sensor_id>``	Lock sensor ON, preventing external influence, valid IDs are in the range 0 - 255.

``</ UNLATCH sensor_id>``	Unlock sensor, returning to current external state, valid IDs are in the range 0 - 255.

Refer to the LATCH/UNLATCH commands below for further details.

ROUTES, AUTOMATIONS, & SEQUENCES
=================================

EX-RAIL provides many commands to allow you to create routes that locomotives to follow that may involve turnouts, signals, etc. that can be automatically set to react when the loco trips a sensor.

Script Definition Terms
________________________

``AUTOMATION( id, "description" )``	Define an automation sequence that is advertised to WiThrottles to send a train along. See :ref:`automation/ex-rail-intro:example 4: automating a train (simple loop)` for a simple example.

``ROUTE( id, "description" )``	Define a route that is advertised to WiThrottles. This can be used to initiate automation sequences such as setting turnouts and signals to allow a train to be driven through a specific route on the layout. See :ref:`automation/ex-rail-intro:example 1: creating routes for a throttle` for various examples.

``SEQUENCE( id )``	A general purpose automation sequence that is not advertised to WiThrottles. This may be triggered automatically on startup, or be called by other sequences or activites. See :ref:`automation/ex-rail-intro:example 3: automating various non-track items`, :ref:`automation/ex-rail-intro:example 6: single line shuttle`, and :ref:`automation/ex-rail-intro:example 7: running multiple inter-connected trains` for further examples.

``ENDTASK`` or ``DONE``	Completes a Sequence/Route/Animation/Event handler, and any other automation definition as shown in the previous examples.

Object Definitions
___________________

Aliases
^^^^^^^^

``ALIAS( name[, value] )``	Aliases assigns names to values. They can go anywhere in the script. If a value is not assigned, a unique ID will be assigned based on the alias "name" text.

This is a simple substitution that lets you have readable names for things in your script. For example, instead of having to remember the VPin a turnout is connected to, give the pin number an alias and refer to it by that name. You can use this to name routes, values, pin numbers, or anything you need.

If you simply need a unique identifier for an object used internally to the script, such as a turnout, route, automation, or sequence, you don't even need to provide an ID, EX-RAIL will generate one automatically when you omit the value parameter. We recommend using this for all your routes, sequences, and other internal objects so you don't have to try to remember or keep a list of numbers you've used. This also prevents you from assigning the same number to more than one object.

REMEMBER: IDs for RESERVE/FREE, LATCH/UNLATCH, and pins must be explicitly defined.

To put this another way, if you connect an LED to pin 23 and want to turn it on and off, you have to explicitly set its pin number, so `ALIAS(TOWER_LED, 23)` lets you equate "23" to TOWER_LED. But if you created a route to run your train around an oval, you don't really need to set the number or even know it. Just use `ALIAS(OVAL)` and let EX assign a number internally. If you ever wanted to know what number it assigns, you can enter `<? OVAL>` from the serial monitor with the Command Station running and it will tell you. Since this "hash", as it is called, is generated by the alias name word, it is always unique and always the same for that word even if you have not created the alias yet. Fun fact, "OVAL" will always equal 27500.

Alias naming rules:

- **Must not** be an existing EX-RAIL command name or other reserved word.
- **Should be** reasonably short but descriptive.
- **Must start** with letters A-Z, a-z, or underscore _ (case sensitive!).
- **May then** also contain numbers.
- **Must not** contain spaces or special characters.

Examples:

Defining a pin turnout without an alias:

.. code-block:: cpp

  PIN_TURNOUT(1, 25, "Coal Yard")

Defining a pin turnout with aliases:

.. code-block:: cpp
  
  ALIAS(COAL_YARD)
  ALIAS(COAL_YARD_PIN, 25)
  PIN_TURNOUT(COAL_YARD, COAL_YARD_PIN, "Coal Yard")

Note that you could have used the command `ALIAS(COAL_YARD, 1)` in the example above to explicity set the number, but unless you have a reason to use specific numbers, let the Command Station do it for you. 

In this simple example, aliases seem like overkill, however consider the case where you need to have the "Coal Yard" turnout closed or thrown in various different automation sequences, and you will soon see why it's easier to understand you're throwing the COAL_YARD turnout rather than turnout ID 12345.

Signals
^^^^^^^^

``SIGNAL( red_pin, amber_pin, green_pin )``	Define a pin based signal, which requires three active low pins to be defined to correspond with red, amber, and green lights.

``SIGNALH( red_pin, amber_pin, green_pin )`` As above to define a pin based signal, but with active high pins instead.

For both the SIGNAL/SIGNALH commands, signal colour is set using the pin defined for the red pin. If the signal only has two colours (eg. RED/GREEN), set the unused colour's pin to 0.

``SERVO_SIGNAL( vpin, red_pos, amber_pos, green_pos )`` Define a servo based signal, such as semaphore signals. Each position is an angle to turn the servo to, similar to the SERVO/SERVO2 commands, and SERVO_TURNOUT.

Signal examples:

.. code-block:: cpp

  SIGNAL(25, 26, 27)                // Active low red/amber/green signal using pins 25/26/27 directly on the CommandStation.
  SIGNALH(164 ,0, 165)              // Active high red/green signal using the first two pins of an MCP23017 I/O expander module.
  SERVO_SIGNAL(101, 100, 250, 400)  // Servo based signal using the first PCA9685 servo module.

  GREEN(25)                         // Sets our active low signal to green.
  GREEN(164)                         // Sets our active high signal to green.
  GREEN(101)                        // Sets our servo based signal to green.

Turnouts
^^^^^^^^^

All the below turnout definitions will define turnouts that are advertised to WiThrottle apps, Engine Driver, and JMRI, unless the HIDDEN keyword is used.

"description" is an optional parameter, and must be enclosed in quotes "". If you don't wish this turnout to be advertised to throttles, then substitute the word HIDDEN (with no "") instead of the description.

``TURNOUT( id, addr, sub_addr [, "description"] )``	Define a DCC accessory turnout. Note that DCC linear addresses are not supported, and must be converted to address/subaddress in order to be defined. Refer to the :ref:`reference/downloads/documents:stationary decoder address table (xlsx spreadsheet)` for help on these conversions.

``PIN_TURNOUT( id, pin [, "description"] )``	Define a pin operated turnout. When sending a CLOSE command, the pin will be HIGH, and a THROW command will set the pin LOW.

``SERVO_TURNOUT( id, pin, active_angle, inactive_angle, profile [, "description"] )``	Define a servo turnout. "active_angle" is for THROW, "inactive_angle" is for CLOSE, and profile is one of Instant, Fast, Medium, Slow or Bounce (although clearly we don't recommend Bounce for turnouts!). Refer to :doc:`/reference/hardware/servo-module` for more information.

``VIRTUAL_TURNOUT( id [, "description"] )`` Define a virtual turnout, which is backed by another automation sequence. For a good example of this refer to :ref:`automation/ex-rail-intro:realistic turnout sequeunces`.

Examples:

.. code-block:: cpp

  TURNOUT(100, 26, 0, "Coal Yard")                  // DCC accessory turnout at linear address 101.
  PIN_TURNOUT(101, 164, "Switching Yard")           // Pin turnout on an MCP23017 I/O expander module.
  SERVO_TURNOUT(102, 102, 400, 100, Slow, HIDDEN)   // A servo turnout on a PCA9685 servo module that is hidden from throttles.
  VIRTUAL_TURNOUT(103, "Lumber Yard")               // A virtual turnout which will trigger an automation sequence when CLOSE or THROW is sent.

Flow Control Functions
_______________________

``CALL( route )``	Branch to a separate sequence, which will need to RETURN when complete.

``RETURN``	Return to the calling sequence when completed (no DONE required).

Say, for example, you have an AUTOMATION you initiate the sends a train through your layout with multiple station stops, and you want to do the same things at each station.

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
    FON(F2)                         // Blow the horn
    FON(F3)                         // Break squeal
    STOP                            // Stop at the station
    FON(F4)                         // Let out a hiss from the air breaks for a second
    DELAY(1000)
    FOFF(F4)
    DELAYRANDOM(2000, 10000)        // Wait between 2 and 10 seconds for passengers
    FON(F2)                         // Blow the horn again
    FWD(30)                         // On our way to the next station
    RETURN                          // Return to the calling sequence

``FOLLOW( route )``	Branch or Follow a numbered sequence. This lets us do clever things like performing a different sequence depending on whether a turnout is CLOSED or THROWN, as well as simple things such as the example above where we keep looping through the same sequence.

For example:

.. code-block:: cpp

  AUTOMATION(23, "Choose your own adventure") // This let's someone control the sequence by throwing a turnout (or not)
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
    FON(F2)
    FON(F3)
    STOP
    DONE

  SEQUENCE(25, "Adventure 2")                 // If we don't throw the turnout, let's do our station loop from the example above
    FOLLOW(21)

``DELAY( delay )``	Delay a number of milliseconds

``DELAYMINS( delay )``	Delay a number of minutes

Delay examples:

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

``DELAYRANDOM( min_delay, max_delay )``	Delay a random time between min and max milliseconds, see :ref:`automation/ex-rail-intro:example 7: running multiple inter-connected trains` for good examples.

``IF( sensor_id )``	If sensor activated or latched, continue. Otherwise skip to ELSE or matching ENDIF

``IFNOT( sensor_id )``	If sensor NOT activated and NOT latched, continue. Otherwise skip to ELSE or matching ENDIF

``IFGTE( sensor_id, value )``	Test if analog pin reading is greater than or equal to value (>=)

``IFLT( sensor_id, value )``	Test if analog pin reading is less than value (<)

``IFRANDOM( percent )``	Runs commands in IF block a random percentage of the time

``IFCLOSED( turnout_id )``	Check if turnout is closed

``IFTHROWN( turnout_id )``	Test if turnout is thrown

``IFRESERVE( block )``	If block is NOT reserved, reserves it and run commands in IF block. Otherwise, skip to matching ENDIF

``IFTIMEOUT``	Tests if "timed out" flag has been set by an ATTIMEOUT sensor reading attempt

``IFRED( signal_id )`` Test if signal is red

``IFAMBER( signal_id )`` Test if signal is amber

``IFGREEN( signal_id )`` Test if signal is green

``ELSE``	Provides alternative logic to any IF related command returning False

``ENDIF``	Required to end an IF/IFNOT/etc (Used in all IF.. functions)

Command Station Functions
__________________________

``POWERON`` Power on track and UNJOIN (not yet implemented)

``POWEROFF``	Power off track

``JOIN``	Joins PROG and MAIN track outputs to send the same MAIN DCC signal

``UNJOIN``	Disconnect prog track from main

``READ_LOCO``	Read loco ID from prog track

``POM( cv, value )``	Program CV value on main

``LCD( row, msg )``	Write message on LCD/OLED if fitted

``BROADCAST( msg )`` Broadcast to all throttles/JMRI on serial and WiFi

``PRINT( msg )``	Print diagnostic message to Serial Monitor

``SERIAL( msg )``	Writes direct to Serial (Serial0/USB)

``SERIAL1( msg )``	Writes direct to Serial1

``SERIAL2( msg )``	Wri1tes direct to Seria2

``SERIAL3( msg )``	Writes direct to Serial3

EX-RAIL Functions
__________________

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
___________________

``ESTOP``	Emergency stop loco

``FWD( speed )``	Drive loco forward at DCC speed 0-127 (1=ESTOP)

``REV( speed )``	Drive logo in reverse at DCC speed 0-127 (1=ESTOP)

``SPEED( speed )``	Drive loco in current direction at DCC speed (0-127)

``STOP``	Set loco speed to 0 (same as SPEED(0) )

``FON( func )``	Turn on loco function

``FOFF( func )``	Turn off loco function

``INVERT_DIRECTION``	Switches FWD/REV meaning for this loco

Sensor input and Event Handlers 
________________________________

``AT( sensor_id )``	Wait until sensor is active/triggered

``ATTIMEOUT( sensor_id, timeout_ms )``	Wait until sensor is active/triggered, or if the timer runs out, then continue and set a testable "timed out" flag

``ATGTE( analogpin, value )``  Waits for analog pin to reach value

``ATLT ( analogpin, value )`` Waits for analog pin to go below value

``AFTER( sensor_id )``	Waits for sensor to trigger and then go off for 0.5 seconds

``LATCH( sensor_id )``	Latches a sensor on (Sensors 0-255 only).

``UNLATCH( sensor_id )``	Remove LATCH on sensor.

LATCH/UNLATCH can be used to maintain the state of a sensor, or can also be used to trigger a virtual sensor to act as a state flag for EX-RAIL. As this effects the state of a sensor, it can be tested via IF/IFNOT and will also work with AT/AFTER.

In this example, LATCH/UNLATCH is used to toggle between two different activities each time the ROUTE is selected in a WiThrottle:

.. code-block::

  TURNOUT(17, 30, 1, "Bay to Shed") // DCC turnout with linear address 117

  ALIAS(BayExitStarter, 107)        // Starter Signal with Route board
  ALIAS(ROUTE_TOGGLE, 11)           // State flag to toggle

  ROUTE(11, "Bay to Shed")
    IF(ROUTE_TOGGLE)             // If ROUTE_TOGGLE is not active, do these
      THROW(17)
      DELAY(20)
      DEACTIVATEL(BayExitStarter)
      UNLATCH(ROUTE_TOGGLE)           // LATCH ROUTE_TOGGLE
    ELSE                            // Next time ROUTE activated, this will happen instead
      ACTIVATEL(BayExitStarter)
      DELAY(20)
      CLOSE(17)
      LATCH(ROUTE_TOGGLE)         // UNLATCH ROUTE_TOGGLE to clear the state
    ENDIF
  DONE

``ONCLOSE( turnout_id )``	Event handler for turnout close. Note that there can be only one defined ONCLOSE event for a specific turnout.

``ONTHROW( turnout_id )``	Event handler for turnout thrown. Note that there can be only one defined ONCLOSE event for a specific turnout.

``ONACTIVATE( addr, sub_addr )``	Event handler for 2 part DCC accessory packet value 1

``ONACTIVATEL( linear )``	Event handler for linear DCC accessory packet value 1

``ONDEACTIVATE( addr, sub_addr )``	Event handler for 2 part DCC accessory packet value 0

``ONDEACTIVATEL( linear )``	Event handler for linear DCC accessory packet value 0

All the above "ON" commands are event handlers that trigger a sequence of commands to run when the event occurs. These can vary from the most basic tasks such as setting signals when turnouts are closed or thrown, to triggering complete automation sequences via a DCC accessory decoder.

``WAITFOR( pin )``	The WAITFOR() command instructs EX-RAIL to wait for a servo motion to complete prior to continuing.

A couple of examples:

.. code-block:: cpp

  // First example defines a servo turnout for the coal yard and a signal for the main line.
  TURNOUT(100, 26, 0, "Coal Yard")
  SIGNAL(25, 26, 27)

  // When our turnout is closed, the main line is open, so the signal is green.
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

Action Output Functions
________________________

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