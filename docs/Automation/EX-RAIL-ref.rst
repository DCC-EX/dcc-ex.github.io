*********************
EX-RAIL – Reference
*********************

Notes
========


- ROUTE, AUTOMATION and SEQUENCE use the same ID number space, so a FOLLOW(n) command can be used for any of them.

- Sensors and outputs used by AT/AFTER/SET/RESET/LATCH/UNLATCH refer directly to Arduino pins, and those handled by I2C expansion.

- Signals also refer directly to pins, and the signal ID (for RED/AMBER/GREEN) is always the same as the RED signal pin.

.. @KEBBIN Servo signals?
.. @KEBBIN refer to Hal , ask neil

- Its OK to use sensor IDs that have no physical item in the layout. These can only be LATCHed, tested (IF/IFNOT), or UNLATCHed in the scripts. If a sensor is latched by the script, it can only be unlatched by the script… so ``AT(35) LATCH(35)`` for example, effectively latches the sensor 35 on when detected once.


COMMAND REFERENCE
==================

There are some diagnostic and control commands added to the <tag> language normally used to control the Command Station over USB, WiFi or Ethernet.

.. list-table:: 
    :widths: 25 75
    :header-rows: 1

    * - Command
      - Function
    * - <D EXRAIL ON|OFF>
      -   Turns on/off diagnostic traces for EX-RAIL events
    * - </ PAUSE>
      - Pauses automation, all locos ESTOP.
    * - </ RESUME>
      - Resumes automation, Locos are restarted at speed when paused.
    * - </ >
      - Displays EX-RAIL running thread information
    * - </ START [loco] route>
      - Starts a new thread to send loco onto route or Start a non-loco animation route
    * - </ RESERVE id>
      - Manually reserves a virtual track block.
    * - </ FREE id>
      - Manually frees a virtual track Block
    * -  </ LATCH id>
      - Lock sensor ON                       
    * - </ UNLATCH id>
      - Unlock sensor

.. @KEBBIN I think this table may need splitting or reordering to group together stuff like Turnouts and signals

Routes and animations
======================

.. list-table:: 
  :widths: 25 75
  :header-rows: 1

  * - Command
    - Function
  * - ALIAS(name,value)
    - Gives name to a value for script readability. Must appear BEFORE the EXRAIL command. 
  * - EXRAIL
    - All scripts exist in a single block between EXRAIL and ENDEXRAIL keywords
  * - AUTOMATION(sequence_id, "description") 
    - Start of an automation SEQUENCE which Withrottles can send a train along
  * - ROUTE(sequence_id, "description") 
    - Start of a route SEQUENCE settable in Withrottle 
  * - SEQUENCE(sequence_id) 
    - A general purpose sequence
  * - ENDTASK or DONE
    - Completes a sequence 
  * - ENDEXRAIL
    - Ends entire script
  * - AFTER(sensor_id)
    - Waits for sensor to be detected and then off for 0.5 seconds
  * - AMBER(signal_id)
    - Sets defined signal to amber 
  * - AT(sensor_id)
    - Waits for sensor to be triggered
  * - CALL(sequence_id)
    - branch to separate sequence and allows RETURN
  * - CLOSE(turnout_id)
    - close defined turnout
  * - DELAY(delay)
    - Wait in mS.
  * - DELAYMINS(mindelay)
    - Wait minutes
  * - DELAYRANDOM(mindelay,maxdelay)
    - Delay random time between min and max mS
  * - ENDIF  
    - End of IF type block
  * - ESTOP 
    - Emergency stop cuurrent loco 
  * - FOFF(func)
    - Turn off loco function
  * - FOLLOW(sequence_id)
    - Branch to another sequence
  * - FON(func)
    - Turn on loco function
  * - FREE(blockid)
    - Free previously reserved block
  * - FWD(speed)
    - Drive loco forward at DCC speed (out of 127)
  * - GREEN(signal_id)
    - Set defined signal green
  * - IF(sensor_id)
    - If sensor is activated, continue. Otherwise skip to matching ENDIF.
  * - IFNOT(sensor_id)
    - If sensor is NOT activated, continue. Otherwise skip to matching ENDIF.
  * - IFRANDOM(percent)
    - Randomly choose to continue or skip to matching ENDIF.
  * - IFRESERVE(block)
    - If block is not reserved, RESERVE it and continue. Otherwise skip to matching ENDIF.
  * - INVERT_DIRECTION
    - Further FWD/REV commands to this loco will be reversed
  * - JOIN
    - Join prog track to main
  * - LATCH(sensor_id)
    - Latch sensor ON (Sensors 0-255 only)
  * - LCD(row,"msg")
    - Write message on LCD/OLED 
  * - ONCLOSE(turnout_id)
    - Catch closure of turnout
  * - ONTHROW(turnout_id)
    - Catch throw of Turnout
  * - PAUSE
    - ESTOP all locos and PAUSE all OTHER EXRAIL tasks until RESUMEd
  * - POM(cv,value)
    - Write loco cv on main track
  * - PRINT("msg")
    - Writes a message to the serial monitor
  * - READ_LOCO
    - Read loco ID from prog track
  * - RED(signal_id)
    - Set defined signal to red
  * - RESERVE(blockid)
    - Reserve a block (0-255) If already reserved current loco will STOP and script waits for block to become free.
  * - RESET(output_pin)
    - Zero an output pin. 
  * - RESUME
    - Resume all paused tasks
  * - RETURN
    - Return to CALL statement
  * - REV(speed)
    - Drive loco in reverse (see FWD)
  * - START(route)
    - Start a new task along given route and handover loco
  * - SERVO(id,position,profile)
    - Move an animation servo. Do not use for Turnouts. (profile is one of  Instant, Fast, Medium, Slow or Bounce)
  * - SETLOCO(loco)
    - Set current loco id
  * - SET(output_pin)
    - Set output pin HIGH
  * - SPEED(speed)
    - drive loco in current direction
  * - STOP 
    - Same as SPEED(0)
  * - SIGNAL(red_pin,amber_pin,green_pin) 
    - Define a signal, Red_pin becomes signal_id for RED/AMBER/GREEN 
  * - SERVO_TURNOUT(id,pin,activeAngle,inactiveAngle,profile)
    - Define a servo turnout. (profile is one of  Instant, Fast, Medium, Slow or Bounce)
  * - PIN_TURNOUT(id,pin) 
    - Define a pin turnout
  * - THROW(id)
    - Throw a defined turnout
  * - TURNOUT(id,addr,subaddr)
    - Define a DCC turnout
  * - UNJOIN
    - Disconnect prog track from main
  * - UNLATCH(sensor_id)
    - Remove LATCH on sensor.
  
  
