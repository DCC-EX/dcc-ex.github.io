.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-reference.rst
|EX-REF-LOGO|

***********************************************
DCC-EX Native Commands - Consolidated Reference
***********************************************

|engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

This page describes all the |DCC-EX Native commands| that the |EX-CS| supports.

Conventions used on this page
=============================

- ``<`` and ``>`` - All DCC-EX commands are surrounded by these characters to indicate the beginning and end, these must always be included
- First letter or number - These are called OPCODES, are case sensitive, and must be specified as directed, e.g. ``1``, ``c``, or ``-``
- CAPITALISED words - These are parameters referred to as keywords, and should be specified as directed, e.g. ``MAIN`` (note these are not case sensitive, however capitalising makes them easier to distinguish from other parameters)
- lowercase words - These are parameters that must be provided or are returned, with multiple parameters separated by a space " ", e.g. ``cab``
- Square brackets ``[]`` - Parameters within square brackets ``[]`` are optional and may be omitted, and if specifying these parameters, do not include the square brackets themselves
- \| - Use of the \| character means you need to provide one of the provided options only, for example ``<0|1 MAIN|PROG|JOIN>`` becomes either ``<0 MAIN>`` or ``<1 MAIN>``
- ``0|1`` DIRECTION: 1=forward, 0=reverse.

----

Controlling the EX-CommandStation
=================================


Power Management
----------------

.. contents:: In this Section
    :depth: 4
    :local:
    :class: in-this-section

Also see `System Information`_ for retrieve command station power information.

|hr-dashed|

``<onOff [track]>`` - Turn power on or off to the MAIN and PROG tracks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Also allows joining the MAIN and PROG tracks together.

  *Parameters:* |BR|
  |_| > **onOff:** one of |BR|
  |_| |_| |_| |_| - 1 = on |BR|
  |_| |_| |_| |_| - 0 = off |BR|
  |_| > **track:** one of |BR|
  |_| |_| |_| |_| - blank = Both Main and Programming Tracks  |BR|
  |_| |_| |_| |_| - MAIN = Main track  |BR|
  |_| |_| |_| |_| - PROG = Programming Track  |BR|
  |_| |_| |_| |_| - JOIN = Join the Main and Programming tracks temporarily |BR|

  *Response:*  N/A

  *Notes:*

    The use of the JOIN function ensures that the DCC signal for the MAIN track is also sent to the PROG track. This allows the prog track to act as a siding (or similar) in the main layout even though it is isolated electrically and connected to the programming track output. However, it is important that the prog track wiring be in the same phase as the main track i.e. when the left rail is high on MAIN, it is also high on PROG. You may have to swap the wires to your prog track to make this work. If you drive onto a programming track that is "joined" and enter a programming command, the track will automatically switch to a programming track. If you use a compatible Throttle, you can then send the join command again and drive off the track onto the rest of your layout!

    In some split motor shield hardware configurations JOIN will not be able to work.

  *Examples:* |BR|
  |_| all tracks off: ``<0>`` |BR|
  |_| all tracks on ``<1>`` |BR|
  |_| join: ``<1 JOIN>``

|hr-dashed|

``<D RESET>`` - Re-boot the command Station
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* N/A

``<J I>`` ``<JI>`` - Request current status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* Repeated for each Channel/Track: ``<j I track current>`` |BR|
  |_| > **track:**  channel/track |BR|
  |_| > **current:** current in milliamps
    
    *Version Introduced: 4.2.19* 

|hr-dashed|

``<J G>`` ``<JG>`` - Request max current
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| repeated for each Channel/Track: ``<j G track currentmax>`` |BR|
  |_| > **track:**  channel/track |BR|
  |_| > **currentmax:** current in milliamps
    
    *Version Introduced: 4.2.19*

----

Track Manager
-------------

Note:  Previously referred to as 'DC-District'.

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<= trackletter mode [cab]>`` - Configure Track Manager 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **trackletter:** 'A' through 'H' represent one of the outputs of the/a motor shield. |BR|
  |_| > **mode:** one of  |BR|
  |_| |_| |_| |_| - MAIN |BR|
  |_| |_| |_| |_| - PROG |BR|
  |_| |_| |_| |_| - DC |BR|
  |_| |_| |_| |_| - DCX = DC reversed polarity |BR|
  |_| |_| |_| |_| - OFF (DCX is DC with reversed polarity) |BR|
  |_| > **id:** the cab ID. *Required when specifying DC or DCX*
  
  *Response:* |BR|
  |_| (for each track/channel that has changed) ``<= trackletter state cab>`` |BR|
  |_|  |BR|
  |_| > **trackletter:** A-H |BR|
  |_| > **state:**  PROG, MAIN DC, DCX |BR|
  |_| > **cab:** cab(loco) equivalent to a fake DCC Address

  *Notes:*

    since only one channel can be PROG, changing a second channel to PROG, will force the other to OFF**

|hr-dashed|

``<=>`` - Request the current Track Manager configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| for each track/channel supported by the motor shield ``<= trackletter state cab>`` |BR|
  |_|  |BR|
  |_| > **trackletter:** A-H |BR|
  |_| > **state:** PROG, MAIN DC, DCX |BR|
  |_| > **cab:** cab(loco) equivalent to a fake DCC Address

----

Cab (Loco) Commands
-------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<t cab>`` - Request a deliberate update on the cab (loco) speed/functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cab:** DCC Address of the decoder/loco
  
  *Response:* |BR|
  |_| The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question. |BR|
  |_|  |BR|
  |_| ``<l cab reg speedByte functMap>`` |BR|
  |_| > **cab:** DCC Address of the decoder/loco. The short (1-127) or long (128-10293) address of the engine decoder (this has to be already programmed in the decoder) |BR|
  |_| > **reg:** not used. We no longer use this but need something here for compatibility with legacy systems. Enter any single digit.
  |_| > **speedbyte:** Speed in DCC speedstep format . |BR|
  |_| |_| |_| |_| - reverse - 2-127 = speed 1-126, 0 = stop  |BR|
  |_| |_| |_| |_| - forward - 130-255 = speed 1-126,  128 = stop |BR|
  |_| > **FunctiMap:** individual function states represented by the bits in a byte
  
  *Notes:*

    The *speedbyte* value is different to the *speed* sent, as it is an encoded (1,7 bits)  byte. |BR|
    This starts a reminder process for any external updates to the cab's (loco's) status.


|hr-dashed|

``<t cab speed dir>`` - Set Cab (Loco) Speed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cab:** DCC Address of the decoder/loco |BR|
  |_| > **speed:** 0-127 |BR|
  |_| > **dir:** one of |BR|
  |_| |_| |_| |_| - 1=forward  |BR|
  |_| |_| |_| |_| - 0=reverse
  
  *Response:* |BR|
  |_| The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question. |BR|
  |_|  |BR|
  |_| ``<l cab reg speedByte functMap>`` |BR|
  |_| > **cab:** DCC Address of the decoder/loco |BR|
  |_| > **speedbyte:** Speed in DCC speedstep format . |BR|
  |_| |_| |_| |_| - reverse - 2-127 = speed 1-126, 0 = stop  |BR|
  |_| |_| |_| |_| - forward - 130-255 = speed 1-126,  128 = stop |BR|
  |_| > **FunctiMap:** individual function states represented by the the bits in a byte

  *Version Introduced: 4.1.1* 
  
  *Notes:*
   
    The *speedbyte* value is different to the *speed* sent, as it is an encoded (1,7 bits)  byte. |BR|
    This starts a reminder process for any external updates to the cab's (loco's) status.

|hr-dashed|

``<!>`` - Emergency Stop
^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| Repeated for each loco in the reminders list ``<l cab reg speedByte functMap>`` |BR|
  |_| Refer to the ``<t ..>`` command for details on this response.

|hr-dashed|

``<F cab funct state>`` - Turn loco decoder functions ON or OFF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cab:** DCC Address of the decoder/loco (short (1-127) or long (128-10293)) |BR|
  |_| > **funct:** 0-68 (Support for the RCN-212 Functions)) |BR|
  |_| > **state:**  |BR|
  |_| |_| |_| |_| - 1=on  |BR|
  |_| |_| |_| |_| - 0=off
  
  *Response:* |BR|
  |_| The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question.
  |_|  |BR|
  |_| ``<l cab reg speedByte functMap>`` |BR|
  |_| refer to the <t > command above for details
  
  *Notes:*

    Setting requests are transmitted directly to mobile loco decoder. |BR|
    Current state of loco functions (as known by commands issued since power on) is stored by the CommandStation - All functions within a group get set all at once per NMRA DCC standards. |BR|
    The command station knows about the previous settings in the same group and will not, for example, unset F2 because you change F1. If, however, you have never set F2, then changing F1 WILL unset F2. |BR|

  .. collapse:: Examples: (click to show)

    * ``<F 3 0 1>`` Turns the headlight ON for CAB (loco address) 3
    * ``<F 126 0 0>`` Turns the headlight OFF for CAB 126
    * ``<F 1330 1 1>`` Turns the horn ON for CAB 1330

|hr-dashed|

``<f cab byte1 [byte2]]>`` - Decoder Functions - Legacy command |DEPRECATED|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cab:** DCC Address of the decoder/loco |BR|
  |_| > **byte1 byte2:** DCC function bytes as sent to decoders (up to F28)

  *Response:* |BR|
  |_| |_| Success: nothing |BR|
  |_| |_| Fail: ``<X>``

  *Notes:*
  
    Used by the sniffer

  .. collapse::  Additional Information for byte1: (click to show)

      To make "byte1" add the values of what you want ON together, the ones that you want OFF do not get added to the base value of 128.

      * F0 (Light)=16, F1 (Bell)=1, F2 (Horn)=2, F3=4, F4=8
      * All off = 128
      * Light on 128 + 16 = 144
      * Light and bell on 128 + 16 + 1 = 145
      * Light and horn on 128 + 16 + 2 = 146
      * Just horn 128 + 2 = 130

      If light is on (144), Then you turn on bell with light (145), Bell back off but light on (144)

      |hr-dashed|

  .. collapse:: Examples: (click to show)
  
      **Breakdown for this example:** ``<f 3265 144>``

      * **f** = (lower case f) This command is for a CAB,s function i.e.: Lights, horn, bell
      * **3265** = CAB: the short (1-127) or long (128-10293) address of the engine decoder
      * **144** = Turn on headlight

      **To set functions F5-F8 on=(1) or off=(0):** ``<f cab byte1 [byte2]>``

      * **f** = (lower case f) This command is for a CAB,s function.
      * **byte1** = 176 + F5*1 + F6*2 + F7*4 + F8*8
      
        * ADD 176 + the ones you want ON together
        * Add 1 for F5 ON
        * Add 2 for F6 ON
        * Add 4 for F7 ON
        * Add 8 for F8 ON
        * 176 Alone Turns OFF F5-F8

      * **byte2** = omitted

      **To set functions F9-F12 on=(1) or off=(0):** `<f cab byte1 [byte2]>``
      
      * f = (lower case f) This command is for a CAB,s function.

      * **byte1** = 160 + F9*1 +F10*2 + F11*4 + F12*8

        ADD 160 + the ones you want ON together
        Add 1 for F9 ON
        Add 2 for F10 ON
        Add 4 for F11 ON
        Add 8 for F12 ON
        160 Alone Turns OFF F9-F12

      **byte2** = omitted

      **To set functions F13-F20 on=(1) or off=(0):** ``<f cab byte1 [byte2]>``
      
      * **f** = (lower case f) This command is for a CAB,s function.
      * **byte1** = 222
      * **byte2** = F13*1 + F14*2 + F15*4 + F16*8 + F17*16 + F18*32 + F19*64 + F20*128

        * ADD the ones you want ON together
        * Add 1 for F13 ON
        * Add 2 for F14 ON
        * Add 4 for F15 ON
        * Add 8 for F16 ON
        * Add 16 for F17 ON
        * Add 32 for F18 ON
        * Add 64 for F19 ON
        * Add 128 for F20 ON
        * 0 Alone Turns OFF F13-F20

      **To set functions F21-F28 on=(1) or off=(0):** ``<f cab byte1 [byte2]>``

      * **f** = (lower case f) This command is for a CAB function.
      * **byte1** = 223
      * **byte2** = F21*1 + F22*2 + F23*4 + F24*8 + F25*16 + F26*32 + F27*64 + F28*128

        * ADD the ones you want ON together
        * Add 1 for F21 ON
        * Add 2 for F22 ON
        * Add 4 for F23 ON
        * Add 8 for F24 ON
        * Add 16 for F25 ON
        * Add 32 for F26 ON
        * Add 64 for F27 ON
        * Add 128 for F28 ON
        * 0 Alone Turns OFF F21-F28

|hr-dashed|

``<t reg cab speed dir>`` - Set Cab (Loco) Speed - Legacy command |DEPRECATED|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **reg:** not used |BR|
  |_| > **cab:** DCC Address of the decoder/loco |BR|
  |_| > **speed:** 0-127 |BR|
  |_| > **dir:** one of  |BR|
  |_| |_| |_| |_| - 1=forward  |BR|
  |_| |_| |_| |_| - 0=reverse

  *Response:* |BR|
  The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question. |BR|
  |_| ``<l cab reg speedByte functMap>`` |BR|
  |_| refer to the <t > command above for details
  |_|  |BR|
  Legacy response: |Deprecated| |BR|
  |_| ``<T reg speed dir>`` - do not rely on this response
    
  *Version Deprecated: 4.1.1*
  
  *Notes:*
  
    The *speedbyte* value is different to the *speed* sent, as it is an encoded (1,7 bits)  byte. |BR|
    This starts a reminder process for any external updates to the cab's (loco's) status.

|hr-dashed|

``<- [cab]>`` - Remove one or all locos from reminders
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cab:** one of |BR|
  |_| |_| |_| |_| - blank = all locos  |BR|
  |_| |_| |_| |_| - No. = Cab (loco) to forget
  
  *Response:* N/A
  
  *Notes:*
  
    Forgets one or all locos. The "cab" parameter is optional.

    Once you send a throttle command to any loco, throttle commands to that loco will continue to be sent to the track. If you remove the loco, or for testing purposes need to clear the loco from repeating messages to the track, you can use this command. Sending **<- cab>** will forget/clear that loco. Sending **<->** will clear all the locos. This doesn't do anything destructive or erase any loco settings, it just clears the speed reminders from being sent to the track. As soon as a controller sends another throttle command, it will go back to repeating those commands.

  *Examples:*

    ``<- 74>`` - Forgets loco at address 74 |BR|
    ``<->`` - Forgets all locos

|hr-dashed|

``<D speedsteps>`` - Switch between 28 and 128 speed steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **speedsteps:** |BR|
  |_| |_| |_| |_| - SPEED28 = use 28 speed steps |BR|
  |_| |_| |_| |_| - SPEED128 = use 128 speed steps
  
  *Response:* |BR|
  |_| Response sent to the Serial Monitor only (not wifi clients). |BR|
  |_| One of: |BR|
  |_| |_| |_| |_| - *28 Speedsteps* |BR|
  |_| |_| |_| |_| - *128 Speedsteps*


----

Roster Commands
---------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<J R>`` ``<JR>`` - Request the list defined Roster Entry IDs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* N/A |BR| 

  *Response:* |BR|
  |_| ``<jR [id1 id2 id3 ...]>`` |BR|
  |_| > **id?:** unique id of the Cab/s (Loco/s) in the roster
  
  *Example Responses:* |BR|
  |_| Response (roster exists): ``<jR id1 id2 id3 ...>`` |BR|
  |_| Response (no roster exists): ``<jR>``

|hr-dashed|

``<J R id>`` ``<JR id>`` - Request details of a specific Roster Entry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** unique id of the Cab/s (Loco/s) in the roster
  
  *Response:* |BR|
  |_| ``<jR id ""|"desc" ""|"funct1/funct2/funct3/...">`` |BR|
  |_| |_| > **id:**  unique id of the Cab/s (Loco/s) in the roster |BR|
  |_| |_| > **desc:** description of the Loco |BR|
  |_| |_| > **funct?:** Label for each function 0-28
  
  *Example Responses:*  |BR|
  |_| Response (id is in Roster): ``<jR id "desc" "funct1/funct2/funct3/...">`` |BR|
  |_| Response (id is not in Roster): ``<jR id "" "">``

----

Turnouts/Points
---------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

For details on how to configure turnouts/points see: `Turnouts/Points (Configuring the EX-CommandStation)`_

|hr-dashed|

``<T>`` - Request a list all defined turnouts/Points
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| Repeated for each defined Turnout/Point |BR|
  |_| Response (DCC Accessories): ``<H id DCC address subaddress state>`` |BR|
  |_| Response (Servos): ``<H id SERVO vpin thrown_position closed_position profile state>`` |BR|
  |_| Response (VPIN): ``<H id VPIN vpin state>`` |BR|
  |_| Response (LCN): ``<H id LCN state>`` |BR|
  |_| Response (fail): ? |BR|
  |_| Response (no defined turnouts/points): ? |BR|
  |_|  |BR|
  |_| state - 0 = closed 1 = thrown

  .. collapse:: Response - Additional Details: (click to show)

      * ``id`` : The numeric ID (0-32767) of the turnout to control.  

      * (NOTE: You pick the ID. IDs are shared between Turnouts/Points, Sensors and Outputs)

      * ``address`` is the primary address of a DCC accessory decoder controlling a turnout/point (0-511)
      * ``subaddress`` is the subaddress of a DCC accessory decoder controlling a turnout/point (0-3)
      * ``vpin`` is the pin number of the output to be controlled by the turnout/point object.  For Arduino output pins, this is the same as the digital pin number.  For 
        servo outputs and I/O expanders, it is the pin number defined for the HAL device (if present), for example 100-115 for servos attached to the first PCA9685 Servo Controller module,
        116-131 for the second PCA9685 module, 164-179 for pins on the first MCP23017 GPIO expander module, and 180-195 for the second MCP23017 module.
      * ``thrown`` - "0" is closed.  "1" is thrown.
      * ``thrown_position`` : the PWM value corresponding to the servo position for THROWN state, normally in the range 102 to 490.
      * ``closed_position`` : the PWM value corresponding to the servo position for CLOSED state, normally in the range 102 to 490.
      * ``profile`` : the profile for the transition between states.  0=Immediate, 1=Fast (0.5 sec), 2=Medium (1 sec), 3=Slow (2 sec), 3=Bounce (for semaphore signals).

|hr-dashed|

``<J T id>`` ``<JT id>`` - Request details of a specific Turnout/Point
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:**  unique id of the Turnout/Point
  
  *Response:* |BR|
  |_| ``<jT id X|state |"[desc]">`` |BR|
  |_| > **id:** unique id of the Turnout/Point  |BR|
  |_| > **state:** one of |BR|
  |_| |_| |_| |_| - C = Closed |BR|
  |_| |_| |_| |_| - T = Thrown |BR|
  |_| |_| |_| |_| - X = unknown id |BR|
  |_| > **desc:** one of  |BR|
  |_| |_| |_| |_| - "desc" = description of the Turnout(Point) (including surrounding quotes) |BR|
  |_| |_| |_| |_| - blank = unknown id |BR|
  |_|  |BR|
  |_| *Example Responses:* |BR|
  |_| Response (id is defined): ``<jT id state "[desc]">`` |BR|
  |_| Response (id not defined): ``<jT id X>``

|hr-dashed|

``<J T>`` ``<JT>`` - Request the list of defined turnout/Point IDs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:*
  |_| ``<jT [id1 id2 id3 ...]>`` |BR|
  |_| > **id:** unique id of the Turnout/s(Point/s) |BR|
  |_|  |BR|
  |_| *Example Responses:* |BR|
  |_| Response (has defined Turnouts/Points): ``<jT id1 id2 id3 ...>`` |BR|
  |_| Response (no defined Turnouts/Points): ``<jT>``

|hr-dashed|

``<T id state>`` - Throw or Close a defined turnout/point
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the Turnout/Point |BR|
  |_| > **state:** one of |BR|
  |_| |_| |_| |_| - 1=Throw,  |BR|
  |_| |_| |_| |_| - T=Throw,  |BR|
  |_| |_| |_| |_| - 0=Close,  |BR|
  |_| |_| |_| |_| - C=Close
  
  *Response:* |BR|
  |_| ``<H id state>`` |BR|
  |_| > **id:** one of |BR|
  |_| |_| |_| |_| - identifier of the Turnout/Point, or  |BR|
  |_| |_| |_| |_| - X if the command fails |BR|
  |_| > **state:** one of |BR|
  |_| |_| |_| |_| - 1 = Thrown,  |BR|
  |_| |_| |_| |_| - 0 = Closed  |BR|
  |_| |_| |_| |_| - blank = command failed |BR|
  |_|  |BR|
  |_| *Example Responses:* |BR|
  |_| Response (successful): ``<H id 0|1>`` |BR|
  |_| Response (fail): ``<X>``

----

Routes/Automations
------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

For details on how to configure routes/automations see: :doc:`/ex-rail/EX-RAIL-command-reference`

Also see the `EX-RAIL` section below for activating routes.

|hr-dashed|

``<J A>`` - Request a list of Automations/Routes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| ``<jA [id0 id1 id2 ..]>`` |BR|
  |_| > **id?:** identifier of the Route/Automation(s) |BR|
  |_|  |BR|
  |_| *Example Responses:* |BR|
  |_| Response (successful turnouts/point exist): ``<jA id0 id1 id2 ..>`` |BR|
  |_| Response (successful turnouts/point don't exist): ``<jA.>`` |BR|
  |_| Response (fail): ??? |BR|

|hr-dashed|

``<J A id>`` ``<JA id>`` - Request information for a route/automation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the Route/Automation
  
  *Response:* |BR|
  |_| ``<jA id X|type |"desc">`` |BR|
  |_| > **id:** identifier of the Route/Automation |BR|
  |_| > **type:** one of |BR|
  |_| |_| |_| |_| - 'R'= Route  |BR|
  |_| |_| |_| |_| - 'A'=Automation |BR|
  |_| > **"desc":** Textual description of the route/automation always surrounded in quotes (") |BR|
  |_|  |BR|
  |_| *Example Responses:* |BR|
  |_| Response (successful): ``<jA id type "desc">`` |BR|
  |_| Response (fail - is not defined): ``<jA id X>``

----

System Information
------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<c>`` - Request Current on the Track(s)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| ``<c "CurrentMAIN" current C "Milli" "0" max_ma "1" trip_ma>`` |BR|
  |_| > **"CurrentMAIN":** Static text for software like JMRI |BR|
  |_| > **current**: Current in MilliAmps |BR|
  |_| > **C**: Designator to signify this is a current meter (V would be for voltage) |BR|
  |_| > **"Milli"**: Unit of measure for external software with a meter like JMRI (Milli, Kilo, etc.) |BR|
  |_| > **"0":** numbered parameter for external software (1,2,3, etc.) |BR|
  |_| > **max_ma**: The maximum current handling of the motor controller in MilliAmps |BR|
  |_| > **"1"**: number parameter for external software (we use 2 parameters here, 0 and 1) |BR|
  |_| > **trip_ma** - The overcurrent limit that will trip the software circuit breaker in mA

|hr-dashed|

``<s>`` - Request the DCC-EX version and hardware info, along with listing defined turnouts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| ``<iDCCEX version / microprocessorType / MotorControllerType / buildNumber>`` |BR|
  |_| (repeated for each defined Turnout/Point): **<H id state>** |BR|
  |_|  |BR|
  |_| > **version:** Command Station version |BR|
  |_| > **microprocessorType:**  microprocessor type (e.g. MEGA) |BR|
  |_| > **MotorControllerType:**  Motor controller type (e.g. STANDARD_MOTOR_SHIELD) |BR|
  |_| > **buildNumber:**  Command Station build number |BR|
  |_| > **id:** unique identifier for the Turnout/Point |BR|
  |_| > **state:** one of  |BR|
  |_| |_| |_| |_| - 1=thrown  |BR|
  |_| |_| |_| |_| - 0=Closed

|hr-dashed|

``<#>`` - Request the number of supported cabs(locos)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| ``<# noCabs>`` |BR|
  |_| > **noCabs:** maximum number of Cabs(Locos) supported by the command station
  
  *Notes:*
  
    This will display the number of available cab slots. This will typically be **<# 20>**, **<# 30>**, or **<# 50>** depending on how much memory your |EX-CS| has available.
    
    This is a design limit based on the memory limitations of the particular hardware and a compromise with other features that require memory such as WiFI. If you need more slots and are comfortable with code changes you can adjust this by changing MAX_LOCOS in "DCC.h", knowing that each new slot will take approximately 8 bytes of memory. The **<D RAM>** command will display the amount of free memory. If you fill the available slots, the "Forget Locos" command (**<- [CAB]>**) will free up unused locos. Currently there is no automatic purging of unused locos.

----

DCC Accessories
---------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|EX-CS| can keep track of the direction of any turnout that is controlled by a DCC stationary accessory decoder once its Defined (Set Up).

All decoders that are not in an engine are accessory decoders including turnouts.

Any DCC Accessory Decoder based turnouts, as well as any other DCC accessories connected in this fashion, can always be operated using the DCC COMMAND STATION Accessory command:

|hr-dashed|

There are two interchangeable commands for controlling Accessory Decoders, the Address/Subaddress method (aka “Dual-Coil” method) and linear addressing method. You can either specify an address and its subaddress (Addresses 0-511 with Subaddresses from 0-3) or the straight linear address (Addresses from 1-2044).

In the mapping used by EX-CS|, linear addresses range from linear address 1, which is address 1 subaddress 0, up to linear address 2040 which is address 510 subaddress 3. Decoder address 511 (linear addresses 2041-2044) is reserved for use as a broadcast address and should not be used for decoders. Decoder address 0 does not have a corresponding linear address. This seems strange, but it is the mapping used by many, but not all, commercial manufacturers. If your decoder does not respond on the expected linear address, try adding and subtracting 4 to see if it works. Or use the address/subaddress versions of the commands.

Here is a spreadsheet in .XLSX format to help you: :ref:`reference/downloads/documents:stationary decoder address table (xlsx spreadsheet)`.

NOTE: Both the following commands do the same thing. Pick the one that works for your needs.

|hr-dashed|

``<a addr subaddr activate>`` - Control an Accessory Decoder with Address and Subaddress
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **addr:** the primary address of the decoder controlling the turnout (0-511) |BR|
  |_| > **subaddr:** the subaddress of the decoder controlling this turnout (0-3) |BR|
  |_| > **activate:** one of  |BR|
  |_| |_| |_| |_| - 0=off, deactivate, straight or Closed  |BR|
  |_| |_| |_| |_| - 1=on, activate, turn or thrown
  
  *Response:* ???

|hr-dashed|

``<a linear_addr activate>`` - Control an Accessory Decoder with linear address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **linear_addr:** linear address of the decoder controlling this turnout (1-2044) |BR|
  |_| > **activate:** one of  |BR|
  |_| |_| |_| |_| - 0=off, deactivate, straight or Closed  |BR|
  |_| |_| |_| |_| - 1=on, activate, turn or thrown

  *Response:* ???

  *Note*
  
    This general command simply sends the appropriate DCC instruction packet to the main tracks to operate connected accessories. It does not store or retain any information regarding the current status of that accessory.

----

Sensors
-------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section


|hr-dashed|

``<Q>`` - Lists Status of all sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| Repeat for each defined sensor: ``<q id>`` |BR|
  |_|  |BR|
  |_| e.g. |BR|
  |_| Response (successful) Repeat for each defined sensor: ``<q id>`` |BR|
  |_| Response (fail): N/A

|hr-dashed|

``<S>`` - Request a list of all defined sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| Repeated for each defined sensor: ``<Q id vpin pullup>`` |BR|
  |_| > **id:** identifier of the Sensor. (0-32767) |BR|
  |_| > **vpin:** pin number of the input to be controlled by the sensor object |BR|
  |_| > **pullup:** one of |BR|
  |_| |_| |_| |_| - 1=Use pull-up resistor ACTIVE=LOW  |BR|
  |_| |_| |_| |_| - 0=don't use pull-up resistor ACTIVE=HIGH |BR|
  |_|  |BR|
  |_| e.g. |BR|
  |_| Response (successful) Repeated for each defined sensor: ``<Q id vpin pullup>`` |BR|
  |_| Response (fail): ``<X>``

----

WiFi Control
------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<+X>`` - Force the Command Station into "WiFi Connected" mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  A special command to force the "connected" flag (WiFi Connected Mode) to on inside the Command Station so that our loop will start seeing network traffic. If your code creates a connection outside of our normal WiFi code, this provides a way for you to notify the Command Station that it needs to process commands on a connection you created and so you can send your own AT commands.

  *Response:* ???

  *Examples:*

    <+GMR> - Sends the "AT+GMR" command that prints version information from the WiFi device. |BR|
    <+CIFSR> - Gets the local IP Address.

  *Notes:*

    :doc:`DCC-EX WiFi Configuration </ex-commandstation/advanced-setup/supported-wifi/wifi-config>`

    `Espressif AT Command Set PDF File (Exressif makes the ESP8266) <https://www.espressif.com/sites/default/files/documentation/4a-esp8266_at_instruction_set_en.pdf>`_

|hr-dashed|

``<+command>`` - Sends AT+ commands to the WiFi board (ESP8266, ESP32, etc.)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **command:** what you want to append after AT+ and send to the AT processor.
  
  *Response:* ???

  *Example:* ``<+X>`` would send AT+X to the ESP

  *Notes:*

    Users familiar with the AT Command Set of WiFi board may enter commands directly into the serial monitor in real-time or as setup commands in the :doc:`mySetup.h file </ex-commandstation/advanced-setup/startup-config>`. This allows users to override the default WiFi connect sequence or to send any command to change a WiFi device setting.

|hr-dashed|

``<+>`` - Switch to direct communication with WiFi AT processor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| All input and output from this point is the direct communication with the Wifi AT software this mode is ended by typing ! (exclamation mark).

----

EX-RAIL
-------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``</ ROUTES>`` ``</ROUTES>`` - Request the Routes & Automations list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Request the Routes & Automations control list in wiThrottle Protocol format.

  *Response:* |BR|
  |_| ``<X>``

|hr-dashed|

``</ START [locoAddr] routeId>`` - Start a new task to send a loco onto a Route, or activate a non-loco Animation or Sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| locoAddr: DCC address of the loco |BR|
  |_| routeId: id of the rout to start
  
  *Response:* ???

|hr-dashed|

``</ PAUSE>`` - Pauses ALL EX-RAIL automation activities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Including sending an E-STOP to all locos.

  *Response:* N/A

|hr-dashed|

``</ RESUME>`` ``</RESUME>`` - Resumes ALL EX-RAIL automation activities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Also resumes all locos at the same speed at which they were paused.

  *Parameters:* N/A |BR|
  *Response:* N/A

|hr-dashed|

``</ KILL taskId>`` - Kills a currently running script task by ID (use to list task IDs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **taskId:** ??

  *Response:* ???

|hr-dashed|

``</ LATCH sensorId>`` - Lock sensor ON, preventing external influence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **sensorId:**  ??  valid ids and in the range 0-255
  
  *Response:* ??? |BR|
  |_|  |BR|
  |_| ``<* Opcode=L params=2 *>`` |BR|
  |_| ``<* p[0]=-7906 (0xE11E) *>`` |BR|
  |_| ``<* p[1]=24 (0x18) *>`` |BR|
  |_| ``<X>``

|hr-dashed|

``</ UNLATCH sensorId>`` - Unlock sensor, returning to current external state
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **sensor_id:** ??  valid ids and in the range 0-255
  
  *Response:* ??? |BR|
  |_|  |BR|
  |_| ``<* Opcode=U params=2 *>`` |BR|
  |_| ``<* p[0]=23772 (0x5CDC) *>`` |BR|
  |_| ``<* p[1]=24 (0x18) *>`` |BR|
  |_| ``<X>``

|hr-dashed|

``</ RESERVE blockId>`` - Manually reserves a virtual track Block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **blockId:** ?? valid ids and in the range 0-255
  
  *Response:* ???

|hr-dashed|

``</ FREE blockId>`` - Manually frees a virtual track Block
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **blockId:** ?? valid ids and in the range 0-255

  *Response:* ???

|hr-dashed|

``</>`` - Request EX-RAIL running task information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| > **<* EXRAIL STATUS |BR|
  |_| ID=0,PC=189,LOCO=0 ,SPEED=0F |BR|
  |_| ID=2,PC=267,LOCO=0 ,SPEED=0F |BR|
  |_| ID=1,PC=228,LOCO=0 ,SPEED=0F |BR|
  |_| RED[110] |BR|
  |_| RED[113] *>**

|hr-dashed|

``<D EXRAIL state>`` - Enable or disable EX-RAIL script logging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  When the CommandStation is connected to a serial monitor, EX-RAIL script logging can be Enabled or Disabled

  *Parameters:* |BR|
  |_| > **state:** one of |BR|
  |_| |_| |_| |_| - ON |BR|
  |_| |_| |_| |_| - OFF
  
  *Response:* N/A

----

EX-FastClock
------------

These commands require the optional |EX-FC| hardware to the installed along with the |EX-CS| to function.

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<JC minutes speed>`` - Start the fast clock with a specified time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| **minutes:** = time in minutes since midnight. i.e. (hours * 60) + mins |BR|
  |_| **speed:** = the perceived speed factor
  
  *Response:* ``<jC minutes>`` |BR|
  |_| where |BR|
  |_| **minutes:** = time in minutes since midnight. i.e. (hours * 60) + mins |BR|

  *Example:*

    ``<JC 375 4>`` Will set the fast clock time as 6:15am with the percieved speed factor of 1 minute every 15 seconds (4 times actual).

|hr-dashed|

``<JC>`` - Request the fast clock current time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* ``<jC minutes>`` |BR|
  |_| where |BR|
  |_| **minutes:** = time in minutes since midnight. i.e. (hours * 60) + mins |BR|

----

Writing Configuration Variable (CVs)
====================================


Writing CVs - Program on the main
---------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<b cab cv bit value>`` - Write Configuration Variable (CV) bit on main track
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cab:** DCC Address of the decoder/loco.  The short (1-127) or long (128-10293) address of the engine decoder |BR|
  |_| > **cv:** The number of the Configuration Variable memory location in the decoder to write to (1-1024) |BR|
  |_| > **bit:** ???  |BR|
  |_| > **value:** The value to be written to the Configuration Variable memory location (0-255)
  
  *Response:* ???

|hr-dashed|

``<w cab cv value>`` - Write Configuration Variable (CV) on main track
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cab:** DCC Address of the decoder/loco.  The short (1-127) or long (128-10293) address of the engine decoder |BR|
  |_| > **cv:** The number of the Configuration Variable memory location in the decoder to write to (1-1024) |BR|
  |_| > **value:** The value to be written to the Configuration Variable memory location (0-255)
  
  *Response:* N/A

----

Reading/Writing Configuration Variables (CVs) - Programming track
-----------------------------------------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

**Note**

By design, for safety reasons, the NMRA specification prevents locos from responding to throttle or function commands while on the service track. A loco WILL NOT MOVE on the service track! Don't let the little 'jumps' you may see when you are programming a CV confuse you. The loco pulses the motor to give a jump in current that we read as an 'ACK' (acknowledgment), that causes some locos to stutter ahead slightly every time you read or write a CV.

|hr-dashed|

``<R cv>`` - Read Configuration Variables (CVs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cv:** CV number

  *Response:* |BR|
  |_| ``<r cv value>`` |BR|
  |_| > **cv:** The number of the Configuration Variable memory location in the decoder to write to (1-1024) |BR|
  |_| > **value:** one of |BR|
  |_| |_| |_| |_| - value of the CV |BR|
  |_| |_| |_| |_| - -1: if the write failed

  *Example:* ``<r 3450>`` shows that Loco with ID **3450** is on the programming track.

|hr-dashed|

``<R>`` - Read DCC decoder (cab) address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| ``<r -cab>`` |BR|
  |_| > **cab:** |BR|
  |_| |_| |_| |_| - DCC Address of the decoder/loco. The short (1-127) or long (128-10293) address of the engine decoder |BR|
  |_| |_| |_| |_| - -1 = failed read |BR|
  |_|  |BR|
  |_| *Example Responses:* |BR|
  |_| Response (successful): **<r cab>** |BR|
  |_| Response (fail): **<r -1>**

  *Notes:*

    **IMPORTANT:** If the loco is on a consist, the address returned will be the consist address

    When combined with the ``<D ACK ON>`` Command, the ``<R>`` Command (with or without parameters) can be used for diagnostics, for example when you get a "-1" response. (See `Diagnosing Issues <https://github.com/DCC-EX/CommandStation-EX/wiki/Diagnosing-Issues>`_\ ** for more help)

|hr-dashed|

``<V cv bit onOff>`` - Verify/Read bit of Configuration Variable (CV) with guessed value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cv:** CV number |BR|
  |_| > **bit:** bit to verify in the CV |BR|
  |_| > **onOff:** one of |BR|
  |_| |_| |_| |_| - 1=on  |BR|
  |_| |_| |_| |_| - 0=off
 
  *Response:* |BR|
  |_| Response (successful): **0 | 1** |BR|
  |_| Response (fail): **<V -1>**

  *Notes:*

    This command is designed to offer faster verification of the value held in a CV and can be used instead of the ``<R>`` commands. Instead of reading a bit value, it compares the bit to an expected value. It will attempt to verify the value first, an if it is successful, will return the value as if it was simply “read”. If the verify fails, it will perform a read bit command (see above) and return the value read.


|hr-dashed|

``<V cv value>`` - Verify/Read of Configuration Variable (CV) with guessed value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cv:** CV number |BR|
  |_| > **value:**  value to verify

  *Response:* |BR|
  |_| ``<v cv value>`` |BR|
  |_| > **cv:** CV number |BR|
  |_| > **value:** one of |BR|
  |_| |_| |_| |_| - actual value of the CV |BR|
  |_| |_| |_| |_| - -1: if the write failed

  *Notes:*

    This command is designed to offer faster verification of the value held in a CV and can be used instead of the ``<R>`` commands. Instead of reading a byte value or looking at each bit, it compares the byte to an expected value. It will attempt to verify the value first, and if it is successful, will return the value as if it was simply “read”. If the verify fails, it will perform a read byte command (see above) and return the value read.

|hr-dashed|

``<B cv bit onOff>`` - Write bit to Configuration Variable (CV)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cv:** CV number |BR|
  |_| > **bit:** bit to change in the CV |BR|
  |_| > **onOff:** one of  |BR|
  |_| |_| |_| |_| - 1=on  |BR|
  |_| |_| |_| |_| - 0=off
  
  *Response:* ???

|hr-dashed|

``<W cv value >`` - Write Configuration Variable (CV)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cv:** CV number |BR|
  |_| > **value:** value to change the CV to

  *Response:* |BR|
  |_| ``<w cv value>`` |BR|
  |_| > **cv:** CV number |BR|
  |_| > **value:** one of |BR|
  |_| |_| |_| |_| - value CV was changed to |BR|
  |_| |_| |_| |_| - -1: if the write failed

|hr-dashed|

``<W address>`` - Write DCC address to cab (loco)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **address:** DCC Address of the decoder/loco
  
  *Response:* |BR|
  |_| ``<w address>`` |BR|
  |_| > **address:** one of |BR|
  |_| |_| |_| |_| - DCC Address of the decoder/loco |BR|
  |_| |_| |_| |_| - -1 = failed read |BR|
  |_|  |BR|
  |_| Response (successful): **<w cab>** |BR|
  |_| Response (fail): **<w -1>**
  
  *Notes:*
  
    Writes, and then verifies, the address to decoder of an engine on the programming track. This involves clearing any consist and automatically setting a long or short address. This is an easy way to put a loco in a known state to test for issues like not responding to throttle commands when it is on the main track. |BR|

|hr-dashed|

``<P register hex1 hex2 [hex3 [hex4 [hex5]]]>`` - Writes a DCC packet to the PROG track
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **register:** an internal register number, from 0 through MAX_MAIN_REGISTERS (inclusive), to write (if REGISTER=0) or write and store (if REGISTER>**0) the packet |BR|
  |_| > **byte1:**  first hexadecimal byte in the packet |BR|
  |_| > **byte2:**  second hexadecimal byte in the packet |BR|
  |_| > **byte3:**  optional third hexadecimal byte in the packet |BR|
  |_| > **byte4:**  optional fourth hexadecimal byte in the packet |BR|
  |_| > **byte5:**  optional fifth hexadecimal byte in the packet
  
  *Response:* ???

|hr-dashed|

``<B cv bit value callbacknum callbacksub>`` - :dcc-ex-red-bold-italic:`Deprecated, please use <W cv value> instead`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cv:** The number of the Configuration Variable memory location in the decoder to write to (1-1024 ). |BR|
  |_| > **bit:** The bit number of the Configuration Variable memory location to write (0-7) |BR|
  |_| > **value:** The value to be written to the Configuration Variable memory location (0-255) |BR|
  |_| > **callbacknum:** An arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs that call this function. |BR|
  |_| > **callbacksub:** a second arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs (e.g. DCC-EX Interface) that call this function.

  *Response:* ``<r callbacknum|callbacksub|cv value>``

|hr-dashed|

``<W cv value callbacknum callbacksub>`` - :dcc-ex-red-bold-italic:`Deprecated, please use <w cv value> instead`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cv:** The number of the Configuration Variable memory location in the decoder to write to (1-1024 ). |BR|
  |_| > **value:** The value to be written to the Configuration Variable memory location (0-255) |BR|
  |_| > **callbacknum:** An arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs that call this function. |BR|
  |_| > **callbacksub:** a second arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs (e.g. DCC-EX Interface) that call this function.

  *Response:* ``<r callbacknum|callbacksub|cv value>``

|hr-dashed|

``<R cv callbacknum callbacksub>`` - Read Configuration variable byte
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cv:** The number of the Configuration Variable memory location in the decoder to write to (1-1024 ). |BR|
  |_| > **callbacknum:** An arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs that call this function. |BR|
  |_| > **callbacksub:** a second arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs (e.g. DCC-EX Interface) that call this function.

  *Response:* ``<r callbacknum|callbacksub|cv value>``

  *Notes:*

    If specified with parameters, reads a Configuration Variable from the decoder of an engine on the programming track. If no parameters are specified, it returns the Address of the loco on the programming track.

----

Write direct DCC packet
-----------------------

.. Warning:: THESE ARE FOR DEBUGGING AND TESTING PURPOSES ONLY.  DO NOT USE UNLESS YOU KNOW HOW TO CONSTRUCT NMRA DCC PACKETS - YOU CAN INADVERTENTLY RE-PROGRAM YOUR ENGINE DECODER

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<M register hex1 hex2 [hex3 [hex4 [hex5]]]>`` - Write a DCC packet the MAIN track
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Writes a DCC packet of two, three, four, or five hexadecimal bytes to a register driving the selected track.

  *Parameters:* |BR|
  |_| > **register:** ignored |BR|
  |_| > **byte1:**  first hexadecimal byte in the packet |BR|
  |_| > **byte2:**  second hexadecimal byte in the packet |BR|
  |_| > **byte3:**  optional third hexadecimal byte in the packet |BR|
  |_| > **byte4:**  optional fourth hexadecimal byte in the packet |BR|
  |_| > **byte5:**  optional fifth hexadecimal byte in the packet

  *Response:* |BR|
  |_| N/A
  
  *Notes:*
  
    register for backwards compat (can not be removed because number of arguments is unknown)
    
|hr-dashed|

``<P register hex1 hex2 [hex3 [hex4 [hex5]]]>`` - Write a DCC packet the MAIN track
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Writes a DCC packet of two, three, four, or five hexadecimal bytes to a register driving the selected track.

  *Parameters:* |BR|
  |_| > **register:** ignored |BR|
  |_| > **byte1:**  first hexadecimal byte in the packet |BR|
  |_| > **byte2:**  second hexadecimal byte in the packet |BR|
  |_| > **byte3:**  optional third hexadecimal byte in the packet |BR|
  |_| > **byte4:**  optional fourth hexadecimal byte in the packet |BR|
  |_| > **byte5:**  optional fifth hexadecimal byte in the packet

  *Response:* |BR|
  |_| N/A

  *Notes:*

    register for backwards compat (can not be removed because number of arguments is unknown)

----

Programming track - Tuning
--------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<D ACK LIMIT mA>`` - Sets the ACK limit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Use this command to override the minimum milliamps (mA) required to detect the ACK pulse, e.g. ``<D ACK LIMIT 30>`` means a minimum 30mA pulse would be accepted.
 
  *Parameters:* |BR|
  |_| > **mA:** currently limit in milliamps

  *Response:* N/A

  *Notes:*
      
    The Ack current limit is set according to the DCC standard(s) of 60mA. Most decoders send a quick back and forth current pulse to the motor to generate this ACK. However, some modern motors (N and Z scales) may not be able to draw that amount of current. You can adjust down this limit. Or, if for some reasons your acks seem to be too "trigger happy" you can make it less sensitive by raising this limit.

|hr-dashed|

``<D ACK MIN µS>`` - Sets the ACK pulse minimum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  As above, however overriding the maximum amount of time for a pulse, e.g. ``<D ACK MAX 20000>`` means a pulse up to 20ms would be accepted.

  *Parameters:* |BR|
  |_| > **µS:** ACK pulsedureation in milliseconds lower bound
  
  *Response:* N/A

  *Notes:*
  
    The NMRA specifies that the ACK pulse duration should be 6 milliseconds, which is 6000 microseconds (µS), give or take 1000 µS. That means the minimum pulse duration is 5000 µS and the maximum is 7000 µS. There are many poorly designed decoders in existence so DCC-EX extends this range from 4000 to 8500 µS. If you have any decoders that still do not function within this range, you can adjust the ACK MIN and ACK MAX parameters.

|hr-dashed|

``<D ACK MAX µS>`` - Sets the ACK pulse maximum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Use this command to override the minimum amount of time in microseconds (uS) the pulse needs to be active for, e.g. ``<D ACK MIN 2000>`` means a pulse of 2ms or more would be accepted.

  *Parameters:* |BR|
  |_| > **µS:** ACK pulse duration in milliseconds upper bound
  
  *Response:* |BR|
  |_| N/A |BR| |BR|
  |_| *Notes:* |BR|
  |_| see MIN

|hr-dashed|

``<D ACK RETRY x>`` - Adjust ACK retries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  When reading/writing CVs, the program will try again upon failure.  The default is ``<D ACK RETRY 2>``, which means 3 attempts before a failure is reported.  Each of the unsuccessful attempts is reported in the serial monitor or JMRI monitor log.  The last unsuccessful attempt remains on the display if in use.  To reset the running total, send the command manually: ``<D ACK RETRY 2>``.

  *Parameters:* |BR|
  |_| > **x:** Number of times to retry
  
  *Response:* N/A


  *Notes:*

    When combined with the ``<D ACK ON>`` Command, the ``<R>`` Command (with or without parameters) can be used for diagnostics, for example when you get a "-1" response. (See `Diagnosing Issues <https://github.com/DCC-EX/CommandStation-EX/wiki/Diagnosing-Issues>`_\ ** for more help)

|hr-dashed|

``<D PROGBOOST>`` - Override prog track limit while idle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  By default, the programming track has a current limit enabled of 250mA, so any programming activities requiring more than this value will cause power to the programming track to be cut for 100ms. Run this command to override this if programming decoders trigger current limiting on the programming track.

  *Response:* N/A
  
  *Notes:*
  
    When the programming track is switched on with **<1>** or **<1 PROG>** it will normally be restricted to 250mA according to NMRA standards. Some loco decoders require more than this, especially sound versions. **<D PROGBOOST>** temporarily removes this limit to allow the decoder to use more power. The normal limit will be re-imposed when the programming track is switched off with **<0>** or **<0 PROG>** or the Command Station is reset.

----

Configuring the EX-CommandStation
=================================

Turnouts/Points (Configuring the EX-CommandStation)
---------------------------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

The Turnout/Point commands provide a more flexible and more functional way of operating turnouts/points. It requires that the turnout/point be pre-defined through the ``<T ...>`` commands, described below.

Turnouts may be in either of two states: Closed or Thrown. The turnout/point commands below use the values ``1`` for ``Throw`` or ``Thrown`` and ``0`` for ``Close`` or ``Closed``.

*General notes:*

  **vpin** is the pin number of the output to be controlled by the turnout/point object. For Arduino output pins, this is the same as the digital pin number. For servo outputs and I/O expanders, it is the pin number defined for the HAL device (if present), for example 100-115 for servos attached to the first PCA9685 Servo Controller module, 116-131 for the second PCA9685 module, 164-179 for pins on the first MCP23017 GPIO expander module, and 180-195 for the second MCP23017 module.

|hr-dashed|

``<T id DCC addr subaddr>`` - Define turnout/point on a DCC Accessory Decoder with the specified address and subaddress
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the Turnout/Point |BR|
  |_| > **addr:** ranges from 0 to 511 |BR|
  |_| > **subaddr:** ranges from 0 to 3
  
  *Response:* ???
  
  .. collapse:: Examples: (click to show)
    
      *Example:* ``<T 23 DCC 5 0>``

      *Example:* You have a turnout on your main line going to warehouse industry. The turnout is controlled by an accessory decoder with a address of 123 and is wired to output 3. You want it to have the ID of 10. You would send the following command to the CommandStation: ``<T 10 DCC 123 3>``

      This Command means:

        * **T** = (Upper case T) Define a Turnout
        * **DCC** = The turnout is DCC Accessory Decoder based
        * **10** = ID number I am setting to use this turnout
        * **123** = The accessory decoders address
        * **3** = The turnout is wired to output 3

      Next you would send the following command to the EX-CS: ``<E>``
      
      This Command means:

      * E : (Upper case E) Store (save) this definition to EEPROM

|hr-dashed|

``<T id DCC linearAddr>`` - Define turnout/point on a DCC Accessory Decoder with the specified linear address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the Turnout/Point |BR|
  |_| > **linearAddr:** ranges from 1 (address 1/subaddress 0) to 2044 (address 511/subaddress 3).

  *Response:* ???

  *Example:* ``<T 23 DCC 44>`` (corresponds to address 11 subaddress 3)

|hr-dashed|

``<T id VPIN vpin>`` - Define turnout/point output on specified vpin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** unique Id for the servo |BR|
  |_| > **vpin:** vpin to which the servo is attached

  *Response:* |BR|
  |_| Successful: ``<O>`` |BR|
  |_| Fail: ``<X>``

  *Example:* ``<T 25 VPIN 30>`` defines a turnout/point that operates Arduino digital output pin D30. |BR|
  *Example:* ``<T 26 VPIN 164>`` defines a turnout/point that operates the first pin on the first MCP23017 GPIO expander (if present).

  *Notes:*
      
    See vpin notes above.
    
    This may be used for controlling Arduino digital output pins or pins on an I/O Extender.

|hr-dashed|

``<T id SERVO vpin thrownPos closedPos profile>`` - Define turnout/point servo (PWM) on specified vpin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** unique Id for the servo |BR|
  |_| > **vpin:** vpin to which the servo is attached |BR|
  |_| > **thrownPos:** the PWM value corresponding to the servo position for THROWN state, normally in the range 102 to 490 |BR|
  |_| > **closedPos:** the PWM value corresponding to the servo position for CLOSED state, normally in the range 102 to 490 |BR|
  |_| > **profile:** one of |BR|
  |_| |_| |_| |_| - 0=Instant,  |BR|
  |_| |_| |_| |_| - 1=Fast (0.5 sec),  |BR|
  |_| |_| |_| |_| - 2=Medium (1 sec),  |BR|
  |_| |_| |_| |_| - 3=Slow (2 sec) and  |BR|
  |_| |_| |_| |_| - 4=Bounce (subject to revision)
  
  *Response:* |BR|
  |_| Successful: ``<O>`` |BR|
  |_| Fail: ``<X>``

  *Example:* <``T 24 SERVO 100 410 205 2>`` defines a servo turnout/point on the first PCA9685 pin, moving at medium speed between positions 205 and 410.

  *Notes:*

    *Servos are not supported on the minimal HAL (Uno or Nano target).*

    See vpin notes above.
    
    The active and inactive positions are defined in terms of the PWM parameter (0-4095 corresponds to 0-100% PWM). The limits for an SG90 servo are about 102 to 490. The standard range of 1ms to 2ms pulses correspond to values 205 to 409. |BR|
    Profile defines the speed and style of movement: 0=Instant, 1=Fast (0.5 sec), 2=Medium (1 sec), 3=Slow (2 sec) and 4=Bounce (subject to revision).

|hr-dashed|

``<T id>`` - Deletes a turnout by Id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** unique Id for the servod
  
  *Response:* |BR|
  |_| Successful: ``<O>`` |BR|
  |_| Fail: ``<X>``  (Id does not exist)

|hr-dashed|

``<D SERVO vpin value [profile]>`` - Set servo position to value on pin vpin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
  *Parameters:* |BR|
  |_| > **vpin:** vpin to which the servo is attached |BR|
  |_| > **value:**  position to mve the servo to |BR|
  |_| > **profile:**  one of |BR|
  |_| |_| |_| |_| - 0 = instant |BR|
  |_| |_| |_| |_| - 1 = fast |BR|
  |_| |_| |_| |_| - 2 = medium |BR|
  |_| |_| |_| |_| - 3 = slow |BR|
  |_| |_| |_| |_| - 4 = bounce
  
  *Response:* N/A

  *Notes:*
  
    See vpin notes above.

|hr-dashed|

``<T id addr subaddr>`` - Define a turnout on a DCC Accessory Decoder with the specified address and subaddress - Legacy command |DEPRECATED|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the Turnout/Point |BR|
  |_| > **addr:** ??? |BR|
  |_| > **subaddr:** ???

  *Response:* ???
  
  *Version Deprecated:* ???

|hr-dashed|

``<T id vpin activePos inactivePos>`` - Define a turnout/point servo on specified vpin - Legacy command |DEPRECATED|
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the Turnout/Point |BR|
  |_| > **vpin:** vpin of the input to be controlled by the sensor object |BR|
  |_| > **activePos:** ??? |BR|
  |_| > **inactivePos:** ???

  *Response:* ???

  *Version Deprecated: ???*

  *Notes:*
  
    See vpin notes above.

    The positions are the same as for the turnout/point servo command above. Note: Servos are not supported on the minimal HAL (Uno or Nano target).

|hr-dashed|
  
Once all turnouts have been properly defined, Use the ``<E>`` command to store their definitions to EEPROM. If you later make edits/additions/deletions to the turnout definitions, you must invoke the ``<E>`` command if you want those new definitions updated in the EEPROM. You can also ERASE everything; (turnouts, sensors, and outputs) stored in the EEPROM by invoking the ``<e>`` (lower case e) command. WARNING: (There is no Un-Delete)

If turnout definitions are stored in EEPROM, the turnout thrown/closed state is also written to EEPROM whenever the turnout is switched. Consequently, when the |EX-CS| is restarted the turnout outputs may be set to their last known state (applicable for Servo and VPIN turnouts). This is intended so that the servos don't perform a sweep on power-on when their physical position does not match initial position in the CommandStation.

----

Sensors (Configuring the EX-CommandStation)
-------------------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|EX-CS| supports Sensor inputs that can be connected to any Arduino Pin not in use by this program, as well as pins on external I/O expanders and other devices. Physical sensors can be of any type (infrared, magnetic, mechanical…). They may be configured to pull-up or not. When configured for pull-up, the input is connected (within the CS) to +5V via a resistor. This sort of input is suited to sensors that have two wires (a switch or relay contacts, or a device with an 'open collector' or 'open drain' output. Some sensors may be sensitive to the pull-up resistor and not operate as expected - in this case you can turn off the pull-up.

The sensor is considered INACTIVE when at +5V potential, and ACTIVE when the pin is pulled down to 0V.

To ensure proper voltage levels, some part of the Sensor circuitry MUST be tied back to the same ground as used by the Arduino.

The Sensor code utilizes debouncing logic to eliminate contact 'bounce' generated by mechanical switches on transitions. This avoids the need to create smoothing circuitry for each sensor. You may need to change the parameters in Sensor.cpp through trial and error for your specific sensors, but the default parameters protect against contact bounces for up to 20 milliseconds, which should be adequate for almost all mechanical switches and all electronic sensors.

To monitor one or more Arduino pins for sensor triggers, first define/edit/delete sensor definitions using the following variation of the ``<S>`` command:

|hr-dashed|

``<S id vpin pullup>`` - Create a new sensor ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the Sensor (0-32767) (You pick the ID & they are shared between Turnouts, Sensors and Outputs) |BR|
  |_| > **vpin:** vpin of the input to be controlled by the sensor object For Arduino input pins, this is the same as the digital pin number. For servo inputs and I/O expanders, it is the pin number defined for the HAL device (if present), for example 164-179 for pins on the first MCP23017 GPIO expander module, and 180-195 for the second MCP23017 module.|BR|
  |_| > **pullup:** one of  |BR|
  |_| |_| |_| |_| - 1=Use pull-up resistor ACTIVE=LOW  |BR|
  |_| |_| |_| |_| - 0=don't use pull-up resistor ACTIVE=HIGH
  
  *Response:* |BR|
  |_| Successful: **<O>** |BR|
  |_| Fail: **<X>** (e.g. out of memory)
  
  *Notes:*
  
    Once defined, the EX-CS will send a ``<Q id>`` response anytime the sensor is activated, and a ``<q id>`` response when deactivated. 

|hr-dashed|

``<S id>`` - Delete defined sensor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the Sensor (0-32767)
  
  *Response:* |BR|
  |_| Successful: ``<O>`` |BR|
  |_| Fail: ``<X>`` (e.g. ID does not exist)

|hr-dashed|

Once all sensors have been properly defined, use the ``<E>`` (upper case E) command to store their definitions to EEPROM. If you later make edits/additions/deletions to the sensor definitions, you must invoke the ``<E>`` (upper case E) command if you want those new definitions updated in the EEPROM. You can also clear everything (turnouts, sensors, and outputs) stored in the EEPROM by invoking the ``<e>`` (lower case e) command. (There is NO UN-Delete)

All sensors defined as per above are repeatedly and sequentially checked within the main loop of this sketch. If a Sensor Pin is found to have transitioned from one state to another, one of the following serial messages are generated:

* ``<Q id>`` - for transition of Sensor ID from INACTIVE state to ACTIVE state (i.e. the sensor is triggered)
* ``<q id>`` - for transition of Sensor ID from ACTIVE state to INACTIVE state (i.e. the sensor is no longer triggered)

Depending on whether the physical sensor is acting as an "event-trigger" or a "detection-sensor", you may decide to ignore the ``<q id>`` return and only react to ``<Q id>`` triggers.

----

Outputs (Configuring the EX-CommandStation)
-------------------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|EX-CS| supports optional OUTPUT control of any unused Arduino Pins for custom purposes. Pins can be activated or de-activated. 
The default is to set ACTIVE pins HIGH and INACTIVE pins LOW. However, this default behavior can be inverted for any pin in which case ACTIVE=LOW and INACTIVE=HIGH.  

Definitions and state (ACTIVE/INACTIVE) for pins are retained in EEPROM and restored on power-up.
The default is to set each defined pin to active or inactive according to its restored state. 
However, the default behaviour can be modified so that any pin can be forced to be either active or inactive upon power-up regardless of its previous state before power-down.  

To have |EX-CS| utilize one or more Arduino pins as custom outputs, first define/edit/delete output definitions using the following variation of the ``<Z>`` command:  

|hr-dashed|

``<Z id vpin iflag>`` - Creates a new output ID, with specified PIN and IFLAG values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the output |BR|
  |_| > **vpin:** the pin number of the output to be controlled by the output object. For Arduino output pins, this is the same as the digital pin number. For servo outputs and I/O expanders, it is the pin number defined for the HAL device (if present), for example 100-115 for servos attached to the first PCA9685 Servo Controller module, 116-131 for the second PCA9685 module, 164-179 for pins on the first MCP23017 GPIO expander module, and 180-195 for the second MCP23017 module. |BR|
  |_| > **iflag:** see below |BR|
  |_|  |BR|
  |_| iflag, bit 0: |BR|
  |_| |_| |_| |_| - 0 = forward operation (ACTIVE=HIGH / INACTIVE=LOW) |BR|
  |_| |_| |_| |_| - 1 = inverted operation (ACTIVE=LOW / INACTIVE=HIGH) |BR|
  |_| iflag, bit 1: |BR|
  |_| |_| |_| |_| - 0 = state of pin restored on power-up to either ACTIVE or INACTIVE depending on state before power-down. |BR|
  |_| |_| |_| |_| - 1 = state of pin set on power-up, or when first created, to either ACTIVE of INACTIVE depending on IFLAG, bit 2 |BR|
  |_| iflag, bit 2:  |BR|
  |_| |_| |_| |_| - 0 = state of pin set to INACTIVE upon power-up or when first created |BR|
  |_| |_| |_| |_| - 1 = state of pin set to ACTIVE upon power-up or when first created

  *Response:* |BR|
  |_| Successful: ``<O>``  |BR|
  |_| Fail: ``<X>`` (e.g. out of memory).

  *Notes:*

    if output ID already exists, it is updated with specified vpin and iflag.

    Output state will be immediately set to ACTIVE/INACTIVE and pin will be set to HIGH/LOW according to iflag value specified (see below).

|hr-dashed|

``<Z id>`` - Deletes definition of output ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the output to delete
  
  *Response:* |BR|
  |_| Successful: ``<O>`` |BR|
  |_| Fail: ``<X>``  (e.g. ID does not exist)

|hr-dashed|

``<Z>`` -Lists all defined output pins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| Successful: ``<Y id vpin iflag state>`` repeated for each defined output pin |BR|
  |_| Fail: ``<X>``  (e.g. ID does not exist)

|hr-dashed|

``<Z id state>`` - Sets output ID to either INACTIVE or ACTIVE state
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **id:** identifier of the output |BR|
  |_| > **state:** one of  |BR|
  |_| |_| |_| |_| - 0= INACTIVE  |BR|
  |_| |_| |_| |_| - 1= INACTIVE

  *Response:* |BR|
  |_| Successful: ``<Y id state>`` |BR|
  |_| Fail: ``<X>`` if output ID does not exist

  *Notes:* 

    When controlled as such, the Arduino updates and stores the direction of each output in EEPROM so that it is retained even without power. A list of the current states of each output in the form ``<Y id state>`` is generated by |EX-CS| whenever the ``<s>`` status command is invoked. This provides an efficient way of initializing the state of any outputs being monitored or controlled by a separate interface or GUI program.

|hr-dashed|

Once all outputs have been properly defined, use the ``<E>`` Upper Case "E" command to store their definitions to EEPROM.
If you later make edits/additions/deletions to the output definitions, you must invoke the ``<E>`` command if you want those new definitions updated in the EEPROM.
You can also **ERASE everything (turnouts, sensors, and outputs)** stored in the EEPROM by invoking the ``<e>`` (lower case e) command.
**(There is no Un-Delete)**  

----

EEPROM Management (Configuring the EX-CommandStation)
-----------------------------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<D EEPROM>`` - Diagnostic dump EEPROM contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* ???

|hr-dashed|

``<e>`` - Erase ALL (turnouts, sensors, and outputs) from EEPROM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| ``<O>``

|hr-dashed|

``<E>`` - Store definitions to EEPROM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| ``<O>``

----

Diagnostic Programming Commands (Configuring the EX-CommandStation)
-------------------------------------------------------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<D ACK state>`` - Enables ACK diagnostics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **state:** one of |BR|
  |_| |_| |_| |_| - ON |BR|
  |_| |_| |_| |_| - OFF

  *Response:* |BR|
  |_| "Ack diag on" or "Ack diag off" |BR|
  |_| Displayed on the serial monitor only.
  
  *Notes:*
  
    This will turn ACK diagnostics ON and then try to read the appropriate CVs to determine your loco address.

|hr-dashed|

``<D CMD state>`` - Enables Command Parser diagnostics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **state:** one of |BR|
  |_| |_| |_| |_| - ON |BR|
  |_| |_| |_| |_| - OFF
  
  *Response:* N/A

  *Notes:*
    
    When enabled, diagnostic messages will be shown on the the serial monitor.

|hr-dashed|

``<D ETHERNET state>`` - Enables Ethernet diagnostics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **state:** one of |BR|
  |_| |_| |_| |_| - ON |BR|
  |_| |_| |_| |_| - OFF

  *Response:* N/A 
  
  *Notes:*

    When enabled, diagnostic messages will be shown on the the serial monitor.

|hr-dashed|

``<D LCN state>`` - Enables LCN interface diagnostics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **state:** one of |BR|
  |_| |_| |_| |_| - ON |BR|
  |_| |_| |_| |_| - OFF

  *Response:* N/A

|hr-dashed|

``<D WIFI state>`` - Enables WiFi diagnostics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **state:** one of |BR|
  |_| |_| |_| |_| - ON |BR|
  |_| |_| |_| |_| - OFF

  *Response:* N/A
  
  *Notes:*
    
    When enabled, diagnostic messages will be shown on the the serial monitor.

|hr-dashed|

``<D WIT state>`` - Enables WiThrottle diagnostics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **state:** one of |BR|
  |_| |_| |_| |_| - ON |BR|
  |_| |_| |_| |_| - OFF

  *Response:* N/A

  *Notes:*
  
    When enabled, diagnostic messages will be shown on the the serial monitor.

|hr-dashed|

``<D CABS>`` - Shows cab numbers and speed in reminder tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| "Used=xxx, max=yyy" |BR|
  |_| Displayed on the serial monitor only.

|hr-dashed|

``<D HAL SHOW>`` - Shows configured servo board and GPIO extender board config and used pins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| List the configured I/O drivers in the Hardware Abstraction Layer (HAL). This command is available from Version 3.2.0.

  *Examples*

    Example output showing a connected PCA9685 Servo controller and an MCP23017 I/O expander: |BR|
    <* PARSING:D HAL SHOW * > |BR|
    <* Arduino Vpins:2-69 * > |BR|
    <* PCA9685 I2C:x40 Configured on Vpins:100-115 * > |BR|
    <* PCA9685 I2C:x41 Configured on Vpins:116-131 OFFLINE * > |BR|
    <* MCP23017 I2C:x20 Configured on Vpins:164-179 * > |BR|
    <* MCP23017 I2C:x21 Configured on Vpins:180-195 * >

|hr-dashed|

``<D RAM>`` - Shows remaining RAM (Free Memory)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* |BR|
  |_| "Free memory=xxxx" |BR|
  |_| Displayed on the serial monitor only.

----

I/O (HAL) Diagnostics
---------------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<D HAL SHOW>`` - List HAL devices and allocated VPINs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Response:* ???

|hr-dashed|

``<D ANIN vpin>`` - Read and display pin vpin's analogue value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **vpin:** ??

  *Response:* ???

|hr-dashed|

``<D ANOUT vpin value [param2]>`` - Write value to analogue vpin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Write value to analogue pin vpin, supplying param2 to the driver.

  *Parameters:* |BR|
  |_| > **vpin:** ?? |BR|
  |_| > **value:**  ?? |BR|
  |_| > **param2:** ??
  
  *Response:* ???

----

Other
=====

Other Commands
--------------

.. contents:: In This Section
    :depth: 4
    :local:
    :class: in-this-section

|hr-dashed|

``<U cmd>`` - Is reserved for user commands (through user filter)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  *Parameters:* |BR|
  |_| > **cmd:** user defined command
  
  *Response:* N/A

