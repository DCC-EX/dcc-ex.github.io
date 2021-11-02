*********************
EX-RAIL Reference
*********************

.. attention:: EX-RAIL is in Beta testing. It is very far along, but you may experience unexpected issues. We can use your help in final testing and ideas for new features. Please see us on Discord to participate in the Beta, and get the link to the EX-RAIL version of the software.


Notes
========


- *ROUTE*, *AUTOMATION* and *SEQUENCE* use the same ID number space, so a ``FOLLOW(n)`` command can be used for any of them.

- Sensors and outputs used by AT/AFTER/SET/RESET/LATCH/UNLATCH/SERVO/IF/IFNOT refer directly to Arduino pins, and those handled by I2C expansion.

- Signals also refer directly to pins, and the signal ID (for RED/AMBER/GREEN) is always the same as the RED signal pin.

- It's OK to use sensor IDs that have no physical item in the layout. These can only be LATCHed, tested (IF/IFNOT), or UNLATCHed in the scripts. If a sensor is latched by the script, it can only be unlatched by the script… so ``AT(35) LATCH(35)`` for example, effectively latches sensor 35 on when detected once.

- All IDs used in commands and functions will be numbers, or an ALIAS name if configured.

|

Command Reference
==================

.. hint:: Scroll the tables across to view entire contents of two columns!  <--->

Diagnostics & Control
----------------------

There are some diagnostic and control commands added to the <tag> language normally used to control the Command Station over USB, WiFi or Ethernet. 

.. list-table:: 
    :widths: 30 70
    :header-rows: 1

    * - *Command*
      - *Function*
    * - <D EXRAIL ON|OFF>
      - Turns on/off diagnostic traces for EX-RAIL events
    * - </ PAUSE>
      - Pauses all automation - all locos ESTOP
    * - </ RESUME>
      - Resumes all automation - all locos are restarted at speed when paused
    * - </ >
      - Displays EX-RAIL running task information
    * - </ ROUTES>
      - Returns the Routes & Automations control list in WiThrottle format. **JMRI integration only!**
    * - </START [loco_addr] route_id>
      - Starts a new task to send a loco onto a Route, or activate a non-loco Animation or Sequence
    * - </ KILL task_id>
      - Kills a currently running script task by ID (use ``</ >`` to list task IDs) 
    * - </ RESERVE block_id>
      - Manually reserves a virtual track Block
    * - </ FREE block_id>
      - Manually frees a virtual track Block
    * - </ LATCH sensor_id>
      - Lock sensor ON, preventing external influence
    * - </ UNLATCH sensor_ID>
      - Unlock sensor, returning to current external state


Routes, Automations & Sequences
--------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1

  * - *Command*
    - *Function*
  * -
    - 
  * - **--- Script definition items ---**
    - 
  * - EXRAIL
    - All scripts exist in a single block between EXRAIL and ENDEXRAIL keywords
  * - AUTOMATION(sequence_id, "description") 
    - Start of an Automation Sequence which WiThrottles can send a train along
  * - ROUTE(sequence_id, "description") 
    - Start of a Route Sequence settable in WiThrottle 
  * - SEQUENCE(sequence_id) 
    - A general purpose Sequence for scenic animations, etc
  * - ENDTASK or DONE
    - Completes a Sequence 
  * - ENDEXRAIL
    - Ends entire script


  * -
    - 
  * - **--- Object definitions ---**
    - 
  * - ALIAS("name", value) **\* See note! --->**
    - Gives a name to a value for script readability. **\* Must appear BEFORE the EXRAIL command!** 
  * - SIGNAL(red_pin,amber_pin,green_pin) 
    - Define a signal, Red_pin becomes signal_id for RED/AMBER/GREEN 
  * - TURNOUT(id,addr,subaddr)
    - Define a DCC turnout
  * - PIN_TURNOUT(id,pin) 
    - Define a pin turnout
  * - SERVO_TURNOUT(id,pin,activeAngle,inactiveAngle,profile)
    - Define a servo turnout. (profile is one of  Instant, Fast, Medium, Slow or Bounce)


  * - 
    -
  * - **--- Flow control functions ---**
    -
  * - FOLLOW(sequence_id)
    - Branch to another sequence
  * - CALL(sequence_id)
    - branch to separate sequence and allows RETURN
  * - RETURN
    - Return to CALL statement
  * - DELAY(delay)
    - Wait in mS.
  * - DELAYMINS(delay)
    - Wait minutes
  * - DELAYRANDOM(mindelay,maxdelay)
    - Delay random time between min and max mS
  * - IF(sensor_id)
    - If sensor is activated, continue. Otherwise skip to matching ENDIF.
  * - IFNOT(sensor_id)
    - If sensor is NOT activated, continue. Otherwise skip to matching ENDIF.
  * - IFRANDOM(percent)
    - Randomly choose to continue or skip to matching ENDIF.
  * - IFRESERVE(block)
    - If block is *not reserved*, RESERVE it and continue. Otherwise skip to matching ENDIF.
  * - ENDIF  
    - End of IF type block


  * -
    - 
  * - **--- Command Station functions ---**
    - 
  * - JOIN
    - Join prog track to main
  * - UNJOIN
    - Disconnect prog track from main
  * - READ_LOCO
    - Read loco ID from prog track
  * - POM(cv,value)
    - Write loco cv on main track
  * - LCD(row,"msg")
    - Write message on LCD/OLED 
  * - PRINT("msg")
    - Writes a message to the serial monitor


  * -
    - 
  * - **--- EX-RAIL Functions ---**
    - 
  * - PAUSE
    - ESTOP all locos and PAUSE all other EXRAIL tasks until RESUMEd
  * - RESUME
    - Resume all paused tasks
  * - RESERVE(blockid)
    - Reserve a block (0-255) If already reserved, current loco will STOP and script waits for block to become free.
  * - FREE(blockid)
    - Free previously reserved block
  * - START(route)
    - Start a new task running route or sequence
  * - SETLOCO(loco)
    - Set current loco id
  * - SENDLOCO(loco,route)
    - Start a new task to send loco along given route  


  * - 
    -
  * - **--- Loco DCC functions ---**
    -
  * - ESTOP 
    - Emergency stop cuurrent loco 
  * - FWD(speed)
    - Drive loco forward at DCC speed (out of 127)
  * - REV(speed)
    - Drive loco in reverse (see FWD)
  * - SPEED(speed)
    - drive loco in current direction
  * - STOP 
    - Same as SPEED(0)
  * - FON(func)
    - Turn on loco function
  * - FOFF(func)
    - Turn off loco function
  * - INVERT_DIRECTION
    - Further FWD/REV commands to this loco will be reversed


  * - 
    -
  * - **--- Sensor input functions ---**
    -
  * - AT(sensor_id)
    - Waits for sensor to be triggered
  * - AFTER(sensor_id)
    - Waits for sensor to be detected and then off for 0.5 seconds
  * - LATCH(sensor_id)
    - Latch sensor ON (Sensors 0-255 only)
  * - UNLATCH(sensor_id)
    - Remove LATCH on sensor.
  * - ONCLOSE(turnout_id)
    - Catch closure of turnout
  * - ONTHROW(turnout_id)
    - Catch throw of Turnout


  * - 
    -
  * - **--- Action output functions ---**
    -
  * - SET(output_pin)
    - Set output pin HIGH
  * - RESET(output_pin)
    - Zero an output pin. 
  * - CLOSE(turnout_id)
    - close defined turnout
  * - THROW(turnout_id)
    - Throw a defined turnout
  * - GREEN(signal_id)
    - Set defined signal green
  * - AMBER(signal_id)
    - Sets defined signal to amber 
  * - RED(signal_id)
    - Set defined signal to red
  * - SERVO(Vpin,position,Profile)
    - Move an animation servo. Do not use for Turnouts. (profile is one of Instant, Fast, Medium, Slow or Bounce)
  * - XFON(cab,func)
    - Turn on accessory function, e.g. lit carriages. **Not for Loco use - use FON instead!**
  * - XFOFF(cab,func)
    - Turn off accessory function, e.g. lit carriages. **Not for Loco use - use FOFF instead!**


