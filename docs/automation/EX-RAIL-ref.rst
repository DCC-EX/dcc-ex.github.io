*********************
EX-RAIL Reference
*********************


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
  * - ALIAS(name, value) **\* See note! --->**
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


|

begin raw html... <link rel="stylesheet" href="mystyle.css">

.. raw:: html

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    table {
      border: 1px solid #E0E0E0;
      font-size: 14px;
     }

    th, td {
      border: 1px solid #E0E0E0;
      text-align: left;
      padding-left: 20px;
      padding-top: 10px;
      padding-bottom: 10px;
      padding-right: 0px;
    }

    tr:nth-child(even) {
      background-color: #E0E0E0;
    }
    tr:nth-child(odd) {
      background-color: #F3F6F6;
    }
    td.fitwidth {
        width: 1px;
        white-space: nowrap;
    }
    </style>
    </head>
    <body>
    <table>
      <tr>
          <th>EXRAIL Functions</th>
          <th>Description</th>
      </tr>
      <tr>
        <td class="fitwidth"> ACTIVATE(addr,subaddr)</td>
        <td>Sends a DCC accessory packet with value 1</td>
      </tr>
      <tr>
        <td class="fitwidth"> ACTIVATEL(addr)</td>
        <td>Sends a DCC accessory packet with value 1 to a linear address</td>
      </tr>
      <tr>
        <td class="fitwidth"> ALIAS(name,value)</td>
        <td>Can now be anywhere</td>
      </tr>
      <tr>
        <td class="fitwidth"> AMBER(signal_id)</td>
        <td>Set a signal to Amber</td>
      </tr>
      <tr>
        <td class="fitwidth"> AT(sensor_id)</td>
        <td>Wait until sensor is active</td>
      </tr>
      <tr>
        <td class="fitwidth"> AUTOMATION(id, description)</td>
        <td>Start of an Automation Sequence which WiThrottles can send a train along</td>
      </tr>
      <tr>
        <td class="fitwidth"> AUTOSTART</td>
        <td>A task is automatically started at this point during startup</td>
      </tr>
      <tr>
        <td class="fitwidth"> CALL(route)</td>
        <td>call a sequence expecting RETURN</td>
      </tr>
      <tr>
        <td class="fitwidth"> CLOSE(turnout_id)</td>
        <td>Close turnout</td>
      </tr>
      <tr>
        <td class="fitwidth"> DEACTIVATE(addr,subaddr)</td>
        <td> Sends a DCC accessory packet with value 0</td>
      </tr>
      <tr>
        <td class="fitwidth"> DEACTIVATEL(addr)</td>
        <td> Sends a DCC accessory packet with value 1 to a linear address</td>
      </tr>
      <tr>
        <td class="fitwidth"> DELAY(mindelay)</td>
        <td>Delay a number of milliseconds</td>
      </tr>
      <tr>
        <td class="fitwidth"> DELAYMINS(mindelay)</td>
        <td>DElay a number of minutes</td>
      </tr>
      <tr>
        <td class="fitwidth"> DELAYRANDOM(mindelay,maxdelay)</td>
        <td>Delay a random time between min and max milliseconds</td>
      </tr>
      <tr>
        <td class="fitwidth"> DONE</td>
        <td>Completes a Sequence/Route/Animation/Event handler etc</td>
      </tr>
      <tr>
        <td class="fitwidth"> DRIVE(analogpin)</td>
        <td>Not complete, do not use</td>
      </tr>
      <tr>
        <td class="fitwidth"> ENDEXRAIL</td>
        <td>No longer required (does nothing)</td>
      </tr>
      <tr>
        <td class="fitwidth"> ENDIF</td>
        <td>Ends an IF/IFNOT/etc (applies to all IF.. functions)</td> 
      </tr>
      <tr>
        <td class="fitwidth"> ENDTASK</td>
        <td> Same as DONE</td>
      </tr>
      <tr>
        <td class="fitwidth"> ESTOP</td>
        <td>Emergency stop loco</td>
      </tr>
      <tr>
        <td class="fitwidth"> EXRAIL</td>
        <td>No longer required (does nothing)</td>
      </tr>
      <tr>
        <td class="fitwidth"> FADE(pin,value,ms)</td>
        <td>Fade a LED on a servo driver to given value taking given time</td>
      </tr>
      <tr>
        <td class="fitwidth"> FOFF(func)</td>
        <td>Turn off loco function</td>
      </tr>
      <tr>
        <td class="fitwidth"> FOLLOW(route)</td>
        <td>Follow numbered sequence (think of GOTO)</td>
      </tr>
      <tr>
        <td class="fitwidth"> FON(func)</td>
        <td> Turn on loco function</td>
      </tr>
      <tr>
        <td class="fitwidth"> FREE(blockid)</td>
        <td>Free previously reserved block</td>
      </tr>
      <tr>
        <td class="fitwidth"> FWD(speed)</td>
        <td>Set loco DCC speed 0-127  (1=ESTOP)</td>
      </tr>
      <tr>
        <td class="fitwidth"> GREEN(signal_id)</td>
        <td>Set signal to GREEN (see SIGNAL)</td>
      </tr>
      <tr>
        <td class="fitwidth"> IF(sensor_id)</td>
        <td>Test if sensor activated or latched</td> 
      </tr>
      <tr>
        <td class="fitwidth"> IFCLOSED(turnout_id)</td>
        <td>  check if turnout is closed</td>
      </tr>
      <tr>
        <td class="fitwidth"> IFGTE(sensor_id,value)</td>
        <td> test if analog values id &gt=</td>
      </tr>
      <tr>
        <td class="fitwidth"> IFLT(sensor_id,value)</td>
        <td>  test if analog value is </td>
      </tr>
      <tr>
        <td class="fitwidth"> IFNOT(sensor_id)</td>
        <td>Test if sensor not latched and not activated</td>
      </tr>
      <tr>
        <td class="fitwidth"> IFRANDOM(percent)</td>
        <td>Does IF block a random percentage of the time</td>
      <tr>
        <td class="fitwidth"> IFTHROWN(turnout_id)</td>
        <td>Test if turnout is thrown</td> 
      </tr>
      <tr>
        <td class="fitwidth"> IFRESERVE(block)</td>
        <td>If block is not reserved, reserves it and does IF block</td>
      </tr>
      <tr>
        <td class="fitwidth"> INVERT_DIRECTION</td>
        <td>Switches FWD/REV meaning for this loco</td>
      </tr>
      <tr>
        <td class="fitwidth"> JOIN</td>
        <td>Joins prog track to main</td>
      </tr>
      <tr>
        <td class="fitwidth"> LATCH(sensor_id)</td>
        <td>Latches a sensor on</td>
      </tr>
      <tr>
        <td class="fitwidth"> LCD(row,msg)</td>
        <td>Write message on LCD/OLED if fitted</td>
      </tr>
        <td class="fitwidth"> LCN(msg)</td>
        <td>Send message to </td>
      </tr>
      <tr>
        <td class="fitwidth"> ONACTIVATE(addr,subaddr)</td>
        <td>Event handler for DCC accessory packet value 1</td>
      </tr>
      <tr>
        <td class="fitwidth"> ONACTIVATEL(linear)</td>
        <td>Event handler for DCC accessory packet value 1</td>
      </tr>
      <tr>
        <td class="fitwidth"> ONDEACTIVATE(addr,subaddr)</td>
        <td>Event handler for DCC accessory packet value 0</td>
      </tr>
      <tr>
        <td class="fitwidth"> ONDEACTIVATEL(linear)</td>
        <td>Event handler for DCC accessory packet value 0</td> 
      </tr>
      <tr>
        <td class="fitwidth"> ONCLOSE(turnout_id)</td>
        <td>Event handler for turnout close</td>
      </tr>
      <tr>
        <td class="fitwidth"> ONTHROW(turnout_id)</td>
        <td>Event handler for turnout thrown</td> 
      </tr>
      <tr>
        <td class="fitwidth"> PAUSE</td>
        <td>ESTOP all locos and PAUSE all other EXRAIL tasks until RESUMEd</td>
      </tr>
        <td class="fitwidth"> PIN_TURNOUT(id,pin,description...)</td>
        <td>Define pin operated turnout</td>
      </tr>
      <tr>
        <td class="fitwidth"> PRINT(msg)</td>
        <td>Print diagnostic message on Serial</td>
      </tr>
      <tr>
        <td class="fitwidth"> POM(cv,value)</td>
        <td>Program cv value on main</td>
      </tr>
      <tr>
        <td class="fitwidth"> POWEROFF</td>
        <td>Power off track</td>
      </tr>
        <td class="fitwidth"> READ_LOCO</td>
        <td>Read loco ID from prog track</td>
      </tr>
      <tr>
        <td class="fitwidth"> RED(signal_id)</td>
        <td>Set defined signal to red</td>
      </tr>
      <tr>
        <td class="fitwidth"> RESERVE(blockid)</td>
        <td> Reserve a block (0-255) If already reserved, current loco will STOP and script waits for block to become free</td>
      </tr>
      <tr>
        <td class="fitwidth"> RESET(pin)</td>
        <td>Reset output pin</td>
      </tr>
      <tr>
        <td class="fitwidth"> RESUME</td>
        <td>Resuma all paused tasks</td>
      </tr>
      <tr>
        <td class="fitwidth"> RETURN</td>
        <td>Return to caller (see CALL)</td> 
      </tr>
        <td class="fitwidth"> REV(speed)</td>
        <td>Set DCC speed in reverse</td>
      </tr>
      <tr>
        <td class="fitwidth"> ROUTE(id, description)</td>
        <td>Start of a Route Sequence settable in WiThrottle</td>
      </tr>
        <td class="fitwidth"> ROSTER(cab,name,funcmap...)</td>
        <td> - proivide roster info for Withrottle</td>
      </tr>
      <tr>
        <td class="fitwidth"> SENDLOCO(cab,route)</td>
        <td>STart a new task taking given loco along given route/sequence</td>
      </tr>
      <tr>
        <td class="fitwidth"> SEQUENCE(id)</td>
        <td>A general purpose Sequence for scenic animations, etc.</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERIAL(msg)</td>
        <td>Writes ditrect to Serial</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERIAL1(msg)</td>
        <td>Writes ditrect to Serial</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERIAL2(msg)</td>
        <td>Wri1tes ditrect to Seria2</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERIAL3(msg)</td>
        <td>Writes ditrect to Serial3</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERVO(id,position,profile)</td>
        <td>Move an animation servo. Do not use for Turnouts. (profile is one of Instant, Fast, Medium, Slow or Bounce)</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERVO2(id,position,duration)</td>
        <td>Move an animation servo taking duration ms. Do not use for Turnouts</td> 
      </tr>
      <tr>
        <td class="fitwidth"> SERVO_TURNOUT(id,pin,activeAngle,<br>inactiveAngle,profile,description...)</td>
        <td>Define a servo turnout</td>
      </tr>
      <tr>
        <td class="fitwidth"> SET(pin)</td>
        <td>Set an output pin</td>
      </tr>
      <tr>
        <td class="fitwidth"> SETLOCO(loco)</td>
        <td>set te loco address for this task</td>
      </tr>
      <tr>
        <td class="fitwidth"> SIGNAL(redpin,amberpin,greenpin)</td>
        <td> Define a signal (RED/AMBER/GREEN commands always use the redpin as the signal_id)</td>
      </tr>
      <tr>
        <td class="fitwidth"> SPEED(speed)</td>
        <td>Set loco DCC speed (0-127)</td>
      </tr>
      <tr>
        <td class="fitwidth"> START(sequence_id)</td>
        <td>Start a new task to execute sequence</td> 
      </tr>
      <tr>
        <td class="fitwidth"> STOP</td>
        <td>Set loco speed to 0</td>  
      </tr>
      <tr>
        <td class="fitwidth"> THROW(id)</td>
        <td>Throw turnout</td>
      </tr>
      <tr>
        <td class="fitwidth"> TURNOUT(id,addr,subaddr,description...)</td>
        <td>Define DCC Accessory turnout</td>
      </tr>
        <td class="fitwidth"> UNJOIN</td>
        <td>Disconnect prog track from main</td>
      </tr>
      <tr>
        <td class="fitwidth"> UNLATCH(sensor_id)</td>
        <td>Remove latch on sensor</td>
      </tr>
      <tr>
        <td class="fitwidth"> WAITFOR(pin)</td>
        <td>Wait for servo to complete movement</td>
      </tr>
      <tr>
        <td class="fitwidth"> XFOFF(cab,func)</td>
        <td>Send DCC function OFF to specific cab (eg coach lights)</td>
      </tr>
      <tr>
        <td class="fitwidth"> XFON(cab,func)</td>
        <td>Send DCC function ON to specific cab (eg coach lights)</td>
      </tr>
    </table>
    <body>
    <html>

end raw html
