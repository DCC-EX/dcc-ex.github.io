*************************
EX-RAIL Command Summary
*************************


Notes
========


- *ROUTE*, *AUTOMATION* and *SEQUENCE* use the same ID number space, so a ``FOLLOW(n)`` command can be used for any of them.

- Sensors and outputs used by AT/AFTER/SET/RESET/LATCH/UNLATCH/SERVO/IF/IFNOT refer directly to Arduino pins, and those handled by I2C expansion.

- Signals also refer directly to pins, and the signal ID (for RED/AMBER/GREEN) is always the same as the RED signal pin.

- It's OK to use sensor IDs that have no physical item in the layout. These can only be LATCHed, tested (IF/IFNOT), or UNLATCHed in the scripts. If a sensor is latched by the script, it can only be unlatched by the script… so ``AT(35) LATCH(35)`` for example, effectively latches sensor 35 on when detected once.

- All IDs used in commands and functions will be numbers, or an ALIAS name if configured.

|

Command Summary
==================


Diagnostics & Control
-----------------------

There are some diagnostic and control commands added to the <tag> language normally used to control the Command Station over USB, WiFi or Ethernet. 

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
      padding-left: 10px;
      padding-top: 8px;
      padding-bottom: 4px;
      padding-right: 20px;
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
    td.center {
        text-align: center;
    }
    </style>
    </head>
    <body>
    <table>
      <tr>
          <th>EX-RAIL Functions</th>
          <th>Description</th>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;D EXRAIL ON|OFF&gt;</td>
        <td>Turns on/off diagnostic traces for EX-RAIL events</td>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;PAUSE&gt;</td>
        <td>Pauses all automation - all locos E-STOP</td>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;RESUME&gt;</td>
        <td>Resumes all automation - all locos are restarted at the speed when paused</td>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;/&gt;</td>
        <td>Displays EX-RAIL running task information</td>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;/ ROUTES&gt;</td>
        <td>Returns the Routes & Automations control list in WiThrottle format. JMRI integration only!</td>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;/ START [loco_addr] route_id&gt;</td>
        <td>Starts a new task to send a loco onto a Route, or activate a non-loco Animation or Sequence</td>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;/ KILL task_id&gt;</td>
        <td>Kills a currently running script task by ID (use </ > to list task IDs)</td>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;/ RESERVE block_id&gt;</td>
        <td>Manually reserves a virtual track Block</td>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;/ FREE block_id&gt;</td>
        <td>Manually frees a virtual track Block</td>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;/ LATCH sensor_id&gt;</td>
        <td>Lock sensor ON, preventing external influence</td>
      </tr>
      <tr>
        <td class="fitwidth"> &lt;/ UNLATCH sensor_id&gt;</td>
        <td>Unlock sensor, returning to current external state</td>
      </tr>
    </table>
    </body>
    </html>

|

Routes, Automations, and Sequences
----------------------------------

.. raw:: html

    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <table>
      <tr>
          <th>EXRAIL Functions</th>
          <th>Description</th>
      </tr>
      <tr>
        <td class="center"><b> — Script Definition Items — </b></td>
        <td> </td>
      </tr>
      <tr>
        <td class="fitwidth"> EXRAIL</td>
        <td>No longer required (does nothing)</td>
      </tr>
      <tr>
        <td class="fitwidth"> AUTOMATION( id, description )</td>
        <td>Start of an Automation Sequence which WiThrottles can send a train along</td>
      </tr>
      <tr>
        <td class="fitwidth"> ROUTE( id, description )</td>
        <td>Start of a Route Sequence settable in WiThrottle</td>
      </tr>
      <tr>
        <td class="fitwidth"> SEQUENCE( id )</td>
        <td>A general purpose Sequence for scenic animations, etc.</td>
      </tr>
      <tr>
        <td class="fitwidth"> ENDTASK or DONE</td>
        <td> Completes a Sequence/Route/Animation/Event handler, etc.</td>
      </tr>
      <tr>
        <td class="fitwidth"> ENDEXRAIL</td>
        <td>No longer required (does nothing)</td>
      </tr>

      <tr>
        <td class="center"><b> — Object definitions —</b></td>
        <td> </td>
      </tr>
      <tr>
        <td class="fitwidth"> ALIAS( name, value )</td>
        <td>Assign names to values. Can go anywhere in the script</td>
      </tr>
      <tr>
        <td class="fitwidth"> SIGNAL( red_pin, amber_pin, green_pin )</td>
        <td> Define a signal (RED/AMBER/GREEN commands always use the red_pin as the signal_id)</td>
      </tr>
      <tr>
        <td class="fitwidth"> TURNOUT( id, addr, sub_addr [, description] )</td>
        <td>Define DCC Accessory turnout</td>
      </tr>
      </tr>
        <td class="fitwidth"> PIN_TURNOUT( id, pin [, description] )</td>
        <td>Define pin operated turnout</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERVO_TURNOUT( id, pin, active_angle,<br>&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp inactive_angle, profile [, description] )</td>
        <td>Define a servo turnout</td>
      </tr>

      <tr>
        <td class="center"> <b>— Flow control functions —</b></td>
        <td> </td>
      </tr>
      <tr>
        <td class="fitwidth"> CALL( route )</td>
        <td>Branch to a separate sequence expecting a RETURN</td>
      </tr>
      <tr>
        <td class="fitwidth"> FOLLOW( route )</td>
        <td>Branch or Follow a numbered sequence (think of "GOTO")</td>
      </tr>
      <tr>
        <td class="fitwidth"> RETURN</td>
        <td>Return to caller (see CALL)</td> 
      </tr> 
      <tr>
        <td class="fitwidth"> DELAY( delay )</td>
        <td>Delay a number of milliseconds</td>
      </tr>
      <tr>
        <td class="fitwidth"> DELAYMINS( delay )</td>
        <td>Delay a number of minutes</td>
      </tr>
      <tr>
        <td class="fitwidth"> DELAYRANDOM( min_delay, max_delay )</td>
        <td>Delay a random time between min and max milliseconds</td>
      </tr>
      <tr>
        <td class="fitwidth"> IF( sensor_id )</td>
        <td> If sensor activated or latched, continue. Otherwise skip to matching ENDIF</td> 
      </tr>
      <tr>
        <td class="fitwidth"> IFNOT( sensor_id )</td>
        <td>If sensor NOT activated and NOT latched, continue. Otherwise skip to matching ENDIF</td>
      </tr>
      <tr>
        <td class="fitwidth"> IFCLOSED( turnout_id )</td>
        <td>  Check if turnout is closed</td>
      </tr>
      <tr>
        <td class="fitwidth"> IFGTE( sensor_id, value )</td>
        <td> Test if analog pin reading is greater than or equal to value (&gt;=)</td>
      </tr>
      <tr>
        <td class="fitwidth"> IFLT( sensor_id, value )</td>
        <td>  Test if analog pin reading is less than value (&lt;)</td>
      </tr>
      <tr>
        <td class="fitwidth"> IFRANDOM( percent )</td>
        <td> Runs commands in IF block a random percentage of the time</td>
      </tr>
      <tr>
        <td class="fitwidth"> IFTHROWN( turnout_id )</td>
        <td> Test if turnout is thrown</td> 
      </tr>
      <tr>
        <td class="fitwidth"> IFRESERVE( block )</td>
        <td>If block is NOT reserved, reserves it and run commands in IF block. Otherwise, skipt to matching ENDIF</td>
      </tr>
      <tr>
        <td class="fitwidth"> ENDIF</td>
        <td>Ends an IF/IFNOT/etc (Used in all IF.. functions)</td> 
      </tr>

      <tr>
        <td class="center"><b> — Command Station functions —</b></td>
        <td> </td>
      </tr>
      <tr>
        <td class="fitwidth"> POWEROFF</td>
        <td>Power off track</td>
      </tr>
      <tr>
        <td class="fitwidth"> JOIN</td>
        <td>Joins PROG and MAIN track outputs to send the same MAIN DCC signal</td>
      </tr>
      <tr>
        <td class="fitwidth"> UNJOIN</td>
        <td>Disconnect prog track from main</td>
      </tr>
      <tr>
        <td class="fitwidth"> READ_LOCO</td>
        <td>Read loco ID from prog track</td>
      </tr>
      <tr>
        <td class="fitwidth"> POM( cv, value )</td>
        <td>Program CV value on main</td>
      </tr>
      <tr>
        <td class="fitwidth"> LCD( row, msg )</td>
        <td>Write message on LCD/OLED if fitted</td>
      </tr>
      <tr>
        <td class="fitwidth"> PRINT( msg )</td>
        <td>Print diagnostic message to Serial Monitor</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERIAL( msg )</td>
        <td>Writes direct to Serial (Serial0/USB)</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERIAL1( msg )</td>
        <td>Writes direct to Serial1</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERIAL2( msg )</td>
        <td>Wri1tes direct to Seria2</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERIAL3( msg )</td>
        <td>Writes direct to Serial3</td>
      </tr>

      <tr>
        <td class="center"><b> — EX-RAIL functions —</b></td>
        <td> </td>
      </tr>
      <tr>
        <td class="fitwidth"> PAUSE</td>
        <td>E-STOP all locos and PAUSE all other EX-RAIL tasks until RESUMEd</td>
      </tr>
      <tr>
        <td class="fitwidth"> RESUME</td>
        <td>Resume all paused tasks, including loco movement</td>
      </tr>
      <tr>
        <td class="fitwidth"> RESERVE( block_id )</td>
        <td> Reserve a block (0-255) If already reserved, current loco will STOP and script waits for block to become free</td>
      </tr>
      <tr>
        <td class="fitwidth"> FREE( block_id )</td>
        <td>Free previously reserved block</td>
      </tr>
      <tr>
        <td class="fitwidth"> START( sequence_id )</td>
        <td>Start a new task to execute a route or sequence</td> 
      </tr>
      <tr>
        <td class="fitwidth"> SETLOCO( loco )</td>
        <td>Set the loco address for this task</td>
      </tr>
      <tr>
        <td class="fitwidth"> SENDLOCO( cab, route )</td>
        <td>Start a new task send a given loco along given route/sequence</td>
      </tr>
      <tr>
        <td class="fitwidth"> AUTOSTART</td>
        <td>A task is automatically started at this point during startup</td>
      </tr>
      <tr>
        <td class="fitwidth"> DRIVE( analog_pin )</td>
        <td><b>Not complete, DO NOT USE</b></td>
      </tr>
      <tr>
        <td class="fitwidth"> ROSTER( cab, name, func_map )</td>
        <td>Provide roster info for WiThrottle</td>
      </tr>

      <tr>
        <td class="center"><b> — Loco DCC functions —</b></td>
        <td> </td>
      </tr>
      <tr>
        <td class="fitwidth"> ESTOP</td>
        <td>Emergency stop loco</td>
      </tr>
      <tr>
        <td class="fitwidth"> FWD( speed )</td>
        <td>Drive loco forward at DCC speed 0-127  (1=ESTOP)</td>
      </tr>
      <tr>
        <td class="fitwidth"> REV( speed )</td>
        <td>Drive logo in reverse at DCC speed 0-127 (1=ESTOP)</td>
      </tr>
      <tr>
        <td class="fitwidth"> SPEED( speed )</td>
        <td>Drive loco in current direction at DCC speed (0-127)</td>
      </tr>
      <tr>
        <td class="fitwidth"> STOP</td>
        <td>Set loco speed to 0 (same as SPEED(0) )</td>  
      </tr>
      <tr>
        <td class="fitwidth"> FON( func )</td>
        <td> Turn on loco function</td>
      </tr>
      <tr>
        <td class="fitwidth"> FOFF( func )</td>
        <td>Turn off loco function</td>
      </tr>
      <tr>
        <td class="fitwidth"> INVERT_DIRECTION</td>
        <td>Switches FWD/REV meaning for this loco</td>
      </tr>

      <tr>
        <td class="center"><b> — Sensor input and event handlers —</b></td>
        <td> </td>
      </tr>
      <tr>
        <td class="fitwidth"> AT( sensor_id )</td>
        <td>Wait until sensor is active/triggered</td>
      </tr>
      <tr>
        <td class="fitwidth"> AFTER( sensor_id )</td>
        <td>Waits for sensor to trigger and then go off for 0.5 seconds</td>
      </tr>
      <tr>
        <td class="fitwidth"> LATCH( sensor_id )</td>
        <td>Latches a sensor on (Sensors 0-255 only)</td>
      </tr>
      <tr>
        <td class="fitwidth"> UNLATCH( sensor_id )</td>
        <td>Remove LATCH on sensor</td>
      </tr>
      <tr>
        <td class="fitwidth"> ONCLOSE( turnout_id )</td>
        <td>Event handler for turnout close</td>
      </tr>
      <tr>
        <td class="fitwidth"> ONTHROW( turnout_id )</td>
        <td>Event handler for turnout thrown</td> 
      </tr>
      <tr>
        <td class="fitwidth"> ONACTIVATE( addr, sub_addr )</td>
        <td>Event handler for 2 part DCC accessory packet value 1</td>
      </tr>
      <tr>
        <td class="fitwidth"> ONACTIVATEL( linear )</td>
        <td>Event handler for linear DCC accessory packet value 1</td>
      </tr>
      <tr>
        <td class="fitwidth"> ONDEACTIVATE( addr, sub_addr )</td>
        <td>Event handler for 2 part DCC accessory packet value 0</td>
      </tr>
      <tr>
        <td class="fitwidth"> ONDEACTIVATEL( linear )</td>
        <td>Event handler for linear DCC accessory packet value 0</td> 
      </tr>
      <tr>
        <td class="fitwidth"> WAITFOR( pin )</td>
        <td>Wait for servo to complete movement</td>
      </tr>
      <tr>
        <td class="center"><b> — Action output functions —</b></td>
        <td> </td>
      </tr>
      <tr>
        <td class="fitwidth"> SET( pin )</td>
        <td>Set an output pin HIGH</td>
      </tr>
      <tr>
        <td class="fitwidth"> RESET( pin )</td>
        <td>Reset output pin (set to LOW)</td>
      </tr>
      <tr>
        <td class="fitwidth"> CLOSE( turnout_id )</td>
        <td>Close a defined turnout</td>
      </tr>
      <tr>
        <td class="fitwidth"> THROW( id )</td>
        <td>Throw a defined turnout</td>
      </tr>
      <tr>
        <td class="fitwidth"> GREEN( signal_id )</td>
        <td>Set a defined signal to GREEN (see SIGNAL)</td>
      </tr>
      <tr>
        <td class="fitwidth"> AMBER( signal_id )</td>
        <td>Set a defined signal to Amber. (See SIGNAL)</td>
      </tr>
      <tr>
        <td class="fitwidth"> RED( signal_id )</td>
        <td>Set defined signal to Red (See SIGNAL)</td>
      </tr>
      <tr>
        <td class="fitwidth"> FADE( pin, value, ms )</td>
        <td>Fade an LED on a servo driver to given value taking given time</td>
      </tr>
      <tr>
        <td class="fitwidth"> LCN( msg )</td>
        <td>Send message to LCN Accessory Network</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERVO( id, position, profile )</td>
        <td>Move an animation servo. Do NOT use for Turnouts. (profile is one of Instant, Fast, Medium, Slow or Bounce)</td>
      </tr>
      <tr>
        <td class="fitwidth"> SERVO2( id, position, duration )</td>
        <td>Move an animation servo taking duration in ms. Do NOT use for Turnouts</td> 
      </tr>
      <tr>
        <td class="fitwidth"> XFON( cab, func )</td>
        <td>Send DCC function ON to specific cab (eg coach lights) <b>Not for Loco use - use FON instead!</b></td>
      </tr>
      <tr>
        <td class="fitwidth"> XFOFF( cab, func )</td>
        <td>Send DCC function OFF to specific cab (eg coach lights) <b>Not for Loco use - use FON instead!</b></td>
      </tr>
      <tr>
        <td class="fitwidth"> ACTIVATE( addr, sub_addr )</td>
        <td>Sends a DCC accessory packet with value 1</td>
      </tr>
      <tr>
        <td class="fitwidth"> ACTIVATEL( linear )</td>
        <td>Sends a DCC accessory packet with value 1 to a linear address</td>
      </tr>
      <tr>
        <td class="fitwidth"> DEACTIVATE( addr, sub_addr )</td>
        <td> Sends a DCC accessory packet with value 0</td>
      </tr>
      <tr>
        <td class="fitwidth"> DEACTIVATEL( addr )</td>
        <td> Sends a DCC accessory packet with value 1 to a linear address</td>
      </tr>
    </table>
    </body>
    </html>

|
