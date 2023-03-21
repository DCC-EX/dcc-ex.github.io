.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-REF-LOGO|

***********************************
DCC-EX Consolidated Command Summary
***********************************

|engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

**This is a summary, for a detailed command, see...**
  :doc:`Command Reference <command-reference>`

This page describes all the DCC-EX commands that the |EX-CS| supports.

Conventions used on this page
=============================

- ``<`` and ``>`` - All DCC-EX commands are surrounded by these characters to indicate the beginning and end, these must always be included
- First letter or number - These are called OPCODES, are case sensitive, and must be specified as directed, eg. ``1``, ``c``, or ``-``
- CAPITALISED words - These are parameters referred to as keywords, and should be specified as directed, eg. ``MAIN`` (note these are not case sensitive, however capitalising makes them easier to distinguish from other parameters)
- lowercase words - These are parameters that must be provided or are returned, with multiple parameters separated by a space " ", eg. ``cab``
- Square brackets ``[]`` - Parameters within square brackets ``[]`` are optional and may be omitted, and if specifying these parameters, do not include the square brackets themselves
- \| - Use of the \| character means you need to provide one of the provided options only, for example ``<0|1 MAIN|PROG|JOIN>`` becomes either ``<0 MAIN>`` or ``<1 MAIN>``
- ``0|1`` DIRECTION: 1=forward, 0=reverse.

Controlling the EX-CommandStation
=================================

Power management
----------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<onOff [track]>``
    - **Turns power on and off to the MAIN and PROG tracks together or independently. Also allows joining the MAIN and PROG tracks together.** |BR|
      *Parameters:* |BR|
      onOff: |BR|
      |_| |_| 1 = on |BR|
      |_| |_| 0 = off |BR|
      track: |BR|
      |_| |_| blank = Both Main and Programming Tracks  |BR|
      |_| |_| MAIN = Main track  |BR|
      |_| |_| PROG = Programming Track  |BR|
      |_| |_| JOIN = Join the Main and Programming tracks temporarily |BR|
      |BR|
      e.g. |BR|
      all tracks off: **<0>** |BR|
      all tracks on **<1>** |BR|
      join: **<1 JOIN>** |BR| |BR|
      *Response:* |BR|
      N/A
      |BR|
      *Notes:* |BR|
      The use of the JOIN function ensures that the DCC signal for the MAIN track is also sent to the PROG track. This allows the prog track to act as a siding (or similar) in the main layout even though it is isolated electrically and connected to the programming track output. However, it is important that the prog track wiring be in the same phase as the main track i.e. when the left rail is high on MAIN, it is also high on PROG. You may have to swap the wires to your prog track to make this work. If you drive onto a programming track that is “joined” and enter a programming command, the track will automatically switch to a programming track. If you use a compatible Throttle, you can then send the join command again and drive off the track onto the rest of your layout! |BR|
      |BR|
      In some split motor shield hardware configurations JOIN will not be able to work.
  * - ``<D RESET>``
    - **Re-boot the command Station** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      N/A
  * - ``<J I>``
    - **Request current status** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      repeated for each Channel/Track: **<j I track current>** |BR|
      |BR|
      track:  channel/track |BR|
      current: current in milliamps |BR|
      *Version Introduced: 4.2.19*
  * - ``<J G>``
    - **Request max current** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      repeated for each Channel/Track: **<j IG track currentmax>** |BR|
      |BR|
      track:  channel/track |BR|
      currentmax: current in milliamps |BR|
      *Version Introduced: 4.2.19*
      
Cab (Loco) Commands
-------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<t reg cab speed dir>``
    - **Set Cab (Loco) Speed** |BR|
      **Deprecated** |BR|
      *Parameters:* |BR|
      reg: not used |BR|
      cab: DCC Address of the decoder/loco |BR|
      speed: 0-127 |BR|
      dir:  |BR|
      |_| |_| 1=forward  |BR|
      |_| |_| 0=reverse |BR| |BR|
      *Response:* |BR|
      The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question. |BR|
      |BR|
      **<l cab reg speedByte functMap>** |BR|
      cab: DCC Address of the decoder/loco |BR|
      reg: redundant. Not used. |BR|
      speedbyte: Speed in DCC speedstep format . |BR|
      |_| |_| reverse - 2-127 = speed 1-126, 0 = stop  |BR|
      |_| |_| forward - 130-255 = speed 1-126,  128 = stop |BR|
      FunctMap: individual function states represented by the the bits in a byte |BR|
      *Version Deprecated: 4.1.1*
      |BR|
      *Notes:* |BR|
      The speedbyte value will appear different to the speed sent, as it is an encoded (1,7 bits)  byte
      |BR|
      This starts a reminder process for any external updates to the cab's (loco's) status.
      |BR|
      |BR|
      Legacy response: Deprecated
      |BR|
      **<T reg speed dir>** - do not rely on this response
  * - ``<t cab speed dir>``
    - **Set Cab (Loco) Speed** |BR|
      *Parameters:* |BR|
      cab: DCC Address of the decoder/loco |BR|
      speed: 0-127 |BR|
      dir:  |BR|
      |_| |_| 1=forward  |BR|
      |_| |_| 0=reverse |BR| |BR|
      *Response:* |BR|
      The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question. |BR|
      |BR|
      **<l cab reg speedByte functMap>** |BR|
      cab: DCC Address of the decoder/loco |BR|
      speedbyte: Speed in DCC speedstep format . |BR|
      |_| |_| reverse - 2-127 = speed 1-126, 0 = stop  |BR|
      |_| |_| forward - 130-255 = speed 1-126,  128 = stop |BR|
      FunctiMap: individual function states represented by the the bits in a byte |BR|
      *Version Introduced: 4.1.1*
      |BR|
      *Notes:* |BR|
      The speedbyte value will appear different to the speed sent, as it is an encoded (1,7 bits)  byte
      |BR|
      This starts a reminder process for any external updates to the cab's (loco's) status.
  * - ``<t cab>``
    - **Requests a deliberate update on the cab speed/functions in the same format as the cab (loco) broadcast.** |BR|
      *Parameters:* |BR|
      cab: DCC Address of the decoder/loco |BR| |BR|
      *Response:* |BR|
      The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question. |BR|
      |BR|
      **<l cab reg speedByte functMap>** |BR|
      cab: DCC Address of the decoder/loco |BR|
      speedbyte: Speed in DCC speedstep format . |BR|
      |_| |_| reverse - 2-127 = speed 1-126, 0 = stop  |BR|
      |_| |_| forward - 130-255 = speed 1-126,  128 = stop |BR|
      FunctiMap: individual function states represented by the the bits in a byte
      |BR|
      *Notes:* |BR|
      The speedbyte value will appear different to the speed sent, as it is an encoded (1,7 bits)  byte
      |BR|
      This starts a reminder process for any external updates to the cab's (loco's) status.
  * - ``<- [cab]>``
    - **Remove one or all locos from reminders** |BR|
      *Parameters:* |BR|
      cab: |BR|
      |_| |_| blank = all locos  |BR|
      |_| |_| No. = Cab (loco) to forget |BR| |BR|
      *Response:* |BR|
      N/A
      |BR|
      *Notes:* |BR|
      Forgets one or all locos. The “cab” parameter is optional.  |BR|
      Once you send a throttle command to any loco, throttle commands to that loco will continue to be sent to the track. If you remove the loco, or for testing purposes need to clear the loco from repeating messages to the track, you can use this command. Sending **<- cab>** will forget/clear that loco. Sending **<->** will clear all the locos. This doesn't do anything destructive or erase any loco settings, it just clears the speed reminders from being sent to the track. As soon as a controller sends another throttle command, it will go back to repeating those commands.
  * - ``<!>``
    - **Emergency Stop** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<l cab reg speedByte functMap>** (For each loco in the reminders list.)
  * - ``<F cab funct onOff>``
    - **Turns loco decoder functions ON and OFF** |BR|
      *Parameters:* |BR|
      cab: DCC Address of the decoder/loco |BR|
      funct: 0-28 (F29-F68 (Support for the RCN-212 Functions) |BR|
      onOff:  |BR|
      |_| |_| 1=on  |BR|
      |_| |_| 0=off |BR| |BR|
      *Response:* |BR|
      **<l cab reg speedByte functMap>**
      |BR|
      *Notes:* |BR|
      - Setting requests are transmitted directly to mobile engine decoder. |BR|
      - Current state of engine functions (as known by commands issued since power on) is stored by the CommandStation - All functions within a group get set all at once per NMRA DCC standards. |BR|
      |BR|
      Current state of engine functions (as known by commands issued since power on) is stored by the CommandStation |BR|
      All functions within a group get set all at once per NMRA DCC standards. |BR|
      Using the new F command, the command station knows about the previous settings in the same group and will not, for example, unset F2 because you change F1. If, however, you have never set F2, then changing F1 WILL unset F2.
  * - ``<f cab byte1 [byte2]]>``
    - **Legacy function. Deprecated, please use <W cv value> instead** |BR|
      **Deprecated** |BR|
      *Parameters:* |BR|
      ??? |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<J R>``
    - **Request the list defined Roster Entry IDs** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<jR [id1 id2 id3 ...]>** |BR|
      id?: unique id of the Cab/s (Loco/s) in the roster |BR|
      |BR|
      e.g. |BR|
      Response (roster exists): **<jR id1 id2 id3 ...>** |BR|
      Response (no roster exists): **<jR>**
  * - ``<J R id>``
    - **Request details of a specific Roster Entry** |BR|
      *Parameters:* |BR|
      id: unique id of the Cab/s (Loco/s) in the roster |BR| |BR|
      *Response:* |BR|
      **<jR id ˮˮ|ˮdescˮ ˮˮ|ˮfunct1/funct2/funct3/...ˮ>** |BR|
      id:  unique id of the Cab/s (Loco/s) in the roster |BR|
      desc: description of the Loco |BR|
      funct0-28: Label for each function 0-28 |BR|
      |BR|
      e.g.  |BR|
      Response (id is in Roster): **<jR id ˮdescˮ ˮfunct1/funct2/funct3/...ˮ>** |BR|
      Response (id is not in Roster): **<jR id ˮˮ ˮˮ>** |BR|

Turnout/Points
--------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<J T>``
    - **Returns the list of defined turnout/Point IDs** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<jT [id1 id2 id3 ...]>** |BR|
      id:  unique id of the Turnout/s(Point/s) |BR|
      |BR|
      e.g. |BR|
      Response (has defined Turnouts/Points): **<jT id1 id2 id3 ...>** |BR|
      Response (no defined Turnouts/Points): **<jT>**
  * - ``<J T id>``
    - **Request details of a specific Turnout/Point** |BR|
      *Parameters:* |BR|
      id:  unique id of the Turnout/Point  |BR| |BR|
      *Response:* |BR|
      **<jT id X|state |ˮ[desc]ˮ>** |BR|
      id:  unique id of the Turnout/Point  |BR|
      state: one of |BR|
      |_| |_| C = Closed |BR|
      |_| |_| T = Thrown |BR|
      |_| |_| X = unknown id |BR|
      desc: one of  |BR|
      |_| |_| ˮdescˮ = description of the Turnout(Point) (including surrounding quotes) |BR|
      |_| |_| blank = unknown id |BR|
      |BR|
      e.g. |BR|
      Response (id is defined): **<jT id state ˮ[desc]ˮ>** |BR|
      Response (id not defined): **<jT id X>**
  * - ``<T>``
    - **List all defined turnouts/Points** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      Repeated for each defined Turnout/Point |BR|
      Response (DCC Accessories): **<H id DCC address subaddress state>** |BR|
      Response (Servos): **<H id SERVO vpin thrown_position closed_position profile state>** |BR|
      Response (VPIN): **<H id VPIN vpin state>** |BR|
      Response (LCN): **<H id LCN state>** |BR|
      Response (fail): ? |BR|
      Response (no defined turnouts/points): ? |BR|
      |BR|
      state - 0=closed 1=thrown
  * - ``<T id state>``
    - **Throw (1 or T) or close(0 or C) a defined turnout/point** |BR|
      *Parameters:* |BR|
      id: identifier of the Turnout/Point |BR|
      state: one of |BR|
      |_| |_| 1=Throw,  |BR|
      |_| |_| T=Throw,  |BR|
      |_| |_| 0=Close,  |BR|
      |_| |_| C=Close  |BR| |BR|
      *Response:* |BR|
      **<H id state>** |BR|
      id: one of |BR|
      |_| |_| identifier of the Turnout/Point, or  |BR|
      |_| |_| X if the command fails |BR|
      state: one of |BR|
      |_| |_| 1 = Thrown,  |BR|
      |_| |_| 0 = Closed  |BR|
      |_| |_| blank = command failed |BR|
      |BR|
      e.g. |BR|
      Response (successful): **<H id 0|1>** |BR|
      Response (fail): **<X>**
  * - ``<T id>``
    - **Delete defined turnout/point** |BR|
      *Parameters:* |BR|
      id: identifier of the Turnout/Point |BR| |BR|
      *Response:* |BR|
      ???

Routes/Automations
------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<J A>``
    - **Returns a list of Automations/Routes** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<jA [id0 id1 id2 ..]>** |BR|
      id?: identifier of the Route/Automation(s) |BR|
      |BR|
      e.g. |BR|
      Response (successful turnouts/point exist): **<jA id0 id1 id2 ..>** |BR|
      Response (successful turnouts/point don't exist): **<jA.>** |BR|
      Response (fail): ???
  * - ``<J A id>``
    - **Returns information for a route/automation** |BR|
      *Parameters:* |BR|
      id: identifier of the Route/Automation |BR| |BR|
      *Response:* |BR|
      **<jA id X|type |ˮdescˮ>** |BR|
      id: identifier of the Route/Automation |BR|
      type: ‘R'= Route ‘A'=Automation |BR|
      “desc”: Textual description of the route/automation always surrounded in quotes (“) |BR|
      |BR|
      e.g. |BR|
      Response (successful): **<jA id type ˮdescˮ>** |BR|
      Response (fail - is not defined): **<jA id X>** |BR|
      
      
System Information
------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<s>``
    - **Returns the DCC-EX version and hardware info, along with listing defined turnouts.** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<iDCCEX version / microprocessorType / MotorControllerType / buildNumber>** |BR|
      (repeated for each defined Turnout/Point): **<H id state>** |BR|
      |BR|
      version: Command Station version |BR|
      microprocessorType:  microprocessor type (e.g. MEGA) |BR|
      MotorControllerType:  Motor controller type (e.g. SATNDARD_MOTOR_SHIELD) |BR|
      buildNumber:  Command Station build number |BR|
      id: unique identifier for the Turnout/Point |BR|
      state:  |BR|
      |_| |_| 1=thrown  |BR|
      |_| |_| 0=Closed
  * - ``<c>``
    - **Request Current on the Track(s)** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<c ˮCurrentMAINˮ current C ˮMilliˮ ˮ0ˮ max_ma ˮ1ˮ trip_ma>** |BR|
      CurrentMAIN: Static text for software like JMRI |BR|
      current - Current in MilliAmps |BR|
      C - Designator to signify this is a current meter (V would be for voltage) |BR|
      Milli - Unit of measure for external software with a meter like JMRI (Milli, Kilo, etc.) |BR|
      0 - numbered parameter for external software (1,2,3, etc.) |BR|
      max_ma - The maximum current handling of the motor controller in MilliAmps |BR|
      1 - number parameter for external software (we use 2 parameters here, 0 and 1) |BR|
      trip_ma - The overcurrent limit that will trip the software circuit breaker in mA |BR|
      *Version Introduced: ??.*
  * - ``<#>``
    - **Show number of supported cabs(locos)** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<# noCabs>** |BR|
      noCabs: maximum number of Cabs(Locos) supported by the command station |BR|
      |BR|
      Will return one of **<# 20>**, **<# 30>**, or **<# 50>**
      |BR|
      *Notes:* |BR|
      This will display the number of available cab slots. This will typically be **<# 20>**, **<# 30>**, or **<# 50>** depending on how much memory your EX‑CommandStation has available.  |BR|
      This is a design limit based on the memory limitations of the particular hardware and a compromise with other features that require memory such as WiFI. If you need more slots and are comfortable with code changes you can adjust this by changing MAX_LOCOS in “DCC.h”, knowing that each new slot will take approximately 8 bytes of memory. The **<D RAM>** command will display the amount of free memory. If you fill the available slots, the “Forget Locos” command (**<- [CAB]>**) will free up unused locos. Currently there is no automatic purging of unused locos.

Writing CVs - Program on the main
---------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<M register hex1 hex2 [hex3 [hex4 [hex5]]]>``
    - **Write a DCC packet the MAIN track** |BR|
      *Parameters:* |BR|
      register: an internal register number, from 0 through MAX_MAIN_REGISTERS (inclusive), to write (if REGISTER=0) or write and store (if REGISTER>**0) the packet |BR|
      byte1:  first hexadecimal byte in the packet |BR|
      byte2:  second hexadecimal byte in the packet |BR|
      byte3:  optional third hexadecimal byte in the packet |BR|
      byte4:  optional fourth hexadecimal byte in the packet |BR|
      byte5:  optional fifth hexadecimal byte in the packet |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<w address cv value>``
    - **Write CV on main track** |BR|
      *Parameters:* |BR|
      address: DCC Address of the decoder/loco |BR|
      cv: CV number |BR|
      value: value to change the CV to |BR| |BR|
      *Response:* |BR|
      N/A
  * - ``<b address cv bit value>``
    - **Write CV bit on main track** |BR|
      *Parameters:* |BR|
      address: DCC Address of the decoder/loco |BR|
      CV: CV number |BR|
      bit: ???  |BR|
      value: value to change the CV to |BR| |BR|
      *Response:* |BR|
      ???

Reading/Writing CVs - Programming track
---------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<W cv value callbacknum callbacksub>``
    - **Deprecated, please use <w cv value> instead** |BR|
      **Deprecated** |BR|
      *Parameters:* |BR|
      cv: CV to write |BR|
      value: value to change the CV to |BR|
      callbacknum: ??? |BR|
      callbacksub: ??? |BR| |BR|
      *Response:* |BR|
      ??? |BR|
      *Version Deprecated: ???*
  * - ``<B cv bit value callbacknum callbacksub>``
    - **Deprecated, please use <W cv value> instead** |BR|
      **Deprecated** |BR|
      *Parameters:* |BR|
      cv: CV to write |BR|
      bit: bit of the CV to change |BR|
      value: value to chnage the bit of CV to |BR|
      callbacknum: ??? |BR|
      callbacksub: ??? |BR| |BR|
      *Response:* |BR|
      ??? |BR|
      *Version Deprecated: ???*
  * - ``<R>``
    - **Read DCC decoder address** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<r -cab>** |BR|
      cab:  |BR|
      |_| |_| DCC Address of the decoder/loco |BR|
      |_| |_| -1 = failed read |BR|
      |BR|
      e.g. |BR|
      Response (successful): **<r cab>** |BR|
      Response (fail): **<r -1>**
  * - ``<W address>``
    - **Write DCC address to cab (loco)** |BR|
      *Parameters:* |BR|
      address: DCC Address of the decoder/loco |BR| |BR|
      *Response:* |BR|
      **<w address>** |BR|
      address: one of |BR|
      |_| |_| DCC Address of the decoder/loco |BR|
      |_| |_| -1 = failed read |BR|
      |BR|
      Response (successful): **<w cab>** |BR|
      Response (fail): **<w -1>**
      |BR|
      *Notes:* |BR|
      Writes, and then verifies, the address to decoder of an engine on the programming track. This involves clearing any consist and automatically setting a long or short address. This is an easy way to put a loco in a known state to test for issues like not responding to throttle commands when it is on the main track.
  * - ``<W cv value >``
    - **Write CV** |BR|
      *Parameters:* |BR|
      cv: CV number |BR|
      value: value to change the CV to |BR| |BR|
      *Response:* |BR|
      **<w cv value>** |BR|
      cv: CV number |BR|
      value: one of |BR|
      |_| |_| value CV was changed to |BR|
      |_| |_| -1: if the write failed
  * - ``<B cv bit onOff>``
    - **Write bit to CV** |BR|
      *Parameters:* |BR|
      cv: CV number |BR|
      bit: bit to change in the CV |BR|
      onOff:  |BR|
      |_| |_| 1=on  |BR|
      |_| |_| 0=off |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<R cv>``
    - **Read CV** |BR|
      *Parameters:* |BR|
      cv: CV number |BR| |BR|
      *Response:* |BR|
      **<r cv value>** |BR|
      cv: CV number |BR|
      value: one of |BR|
      |_| |_| value of the CV |BR|
      |_| |_| -1: if the write failed
  * - ``<V cv value>``
    - **Verify/Read of CV with guessed value** |BR|
      *Parameters:* |BR|
      cv: CV number |BR|
      value:  value to verify |BR| |BR|
      *Response:* |BR|
      **<v cv value>** |BR|
      cv: CV number |BR|
      value: one of |BR|
      |_| |_| actual value of the CV |BR|
      |_| |_| -1: if the write failed
      |BR|
      *Notes:* |BR|
      Additional Notes
  * - ``<V cv bit onOff>``
    - **Verify/Read bit of CV with guessed value** |BR|
      *Parameters:* |BR|
      cv: CV number |BR|
      bit: bit to verify in the CV |BR|
      onOff:  |BR|
      |_| |_| 1=on  |BR|
      |_| |_| 0=off |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<P register hex1 hex2 [hex3 [hex4 [hex5]]]>``
    - **Writes a DCC packet to the PROG track** |BR|
      *Parameters:* |BR|
      register: an internal register number, from 0 through MAX_MAIN_REGISTERS (inclusive), to write (if REGISTER=0) or write and store (if REGISTER>**0) the packet |BR|
      byte1:  first hexadecimal byte in the packet |BR|
      byte2:  second hexadecimal byte in the packet |BR|
      byte3:  optional third hexadecimal byte in the packet |BR|
      byte4:  optional fourth hexadecimal byte in the packet |BR|
      byte5:  optional fifth hexadecimal byte in the packet |BR| |BR|
      *Response:* |BR|
      ???

Writing CVs - Programming track - Tuning
----------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<D ACK LIMIT mA>``
    - **Override ACK processing mA pulse size** |BR|
      *Parameters:* |BR|
      mA: millamps |BR| |BR|
      *Response:* |BR|
      N/A
  * - ``<D ACK MIN uS>``
    - **Override ACK processing minimum pulse width** |BR|
      *Parameters:* |BR|
      uS: microseconds |BR| |BR|
      *Response:* |BR|
      N/A
  * - ``<D ACK MAX uS>``
    - **Override ACK processing max pulse width** |BR|
      *Parameters:* |BR|
      uS: microseconds |BR| |BR|
      *Response:* |BR|
      N/A
  * - ``<D ACK RETRY x>``
    - **Adjust ACK retries to number x (default is 2)** |BR|
      *Parameters:* |BR|
      x: ??? |BR| |BR|
      *Response:* |BR|
      N/A
  * - ``<D PROGBOOST>``
    - **Override 250mA prog track limit while idle** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      N/A

DCC Accessories
---------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<a linear_addr activate>``
    - **Control an Accessory Decoder** |BR|
      *Parameters:* |BR|
      linear_addr: linear address of the decoder controlling this turnout (1-2044) |BR|
      activate:  |BR|
      |_| |_| 0=off, deactivate, straight or Closed  |BR|
      |_| |_| 1=on, activate, turn or thrown |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<a addr subaddr activate>``
    - **Control an Accessory Decoder** |BR|
      *Parameters:* |BR|
      addr: the primary address of the decoder controlling the turnout (0-511) |BR|
      subaddr: the subaddress of the decoder controlling this turnout (0-3) |BR|
      activate:  |BR|
      |_| |_| 0=off, deactivate, straight or Closed  |BR|
      |_| |_| 1=on, activate, turn or thrown |BR| |BR|
      *Response:* |BR|
      ???

Sensors
-------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<Q>``
    - **Lists Status of all sensors** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      Repeat for each defined sensor: **<q id>** |BR|
      |BR|
      e.g. |BR|
      Response (successful) Repeat for each defined sensor: **<q id>** |BR|
      Response (fail): N/A
  * - ``<S>``
    - **Lists definition all defined sensors** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      Repeated for each defined sensor: **<Q id vpin pullup>** |BR|
      id: identifier of the Sensor. (0-32767) |BR|
      vpin pin number of the input to be controlled by the sensor object |BR|
      pullup: one of |BR|
      |_| |_| 1=Use pull-up resistor ACTIVE=LOW  |BR|
      |_| |_| 0=don't use pull-up resistor ACTIVE=HIGH |BR|
      |BR|
      e.g. |BR|
      Response (successful) Repeated for each defined sensor: **<Q id vpin pullup>** |BR|
      Response (fail): **<X>**

WiFi Control
------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<+command>``
    - **Sends AT+ commands to the WiFi board (ESP8266, ESP32, etc.)** |BR|
      *Parameters:* |BR|
      command: ??? |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<+X>``
    - **Force the Command Station into “WiFi Connected” mode** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      ???

Track Manager (Formally DC-District)
------------------------------------

Note: this is not available yet in the Production release of |EX-CS|

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<= trackletter mode [cab]>``
    - **Configure Track Manager  Note: since only one channel can be PROG, changing a second channel to PROG, will force the other to OFF** |BR|
      *Parameters:* |BR|
      trackletter: A through H and represents one of the outputs of the/a motor shield. |BR|
      mode: one of  |BR|
      |_| |_| MAIN |BR|
      |_| |_| PROG |BR|
      |_| |_| DC |BR|
      |_| |_| DCX = DC reversed polarity |BR|
      |_| |_| OFF (DCX is DC with reversed polarity) |BR|
      id: the cab ID required when specifying DC or DCX |BR| |BR|
      *Response:* |BR|
      (for each track/channel that has changed) **<= trackletter state cab>** |BR|
      |BR|
      trackletter: A-H |BR|
      state:  PROG, MAIN DC, DCX |BR|
      cab: cab(loco) equivalent to a fake DCC Address
  * - ``<=>``
    - **Display the current Track Manager configuration** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      for each track/channel supported by the motor shield **<= trackletter state cab>** |BR|
      |BR|
      trackletter: A-H |BR|
      state:  PROG, MAIN DC, DCX |BR|
      cab: cab(loco) equivalent to a fake DCC Address


TBA
---

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<D speedSteps>``
    - **Switch between 28 and 128 speed steps** |BR|
      *Parameters:* |BR|
      speedsteps: |BR|
      |_| |_| SPEED28 = |BR|
      |_| |_| SPEED128 = |BR| |BR|
      *Response:* |BR|
      Response sent to the Serial Monitor only (not wifi clients). |BR|
      One of: |BR|
      |_| |_| 28 Speedsteps |BR|
      |_| |_| 128 Speedsteps

EX-RAIL
-------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<D EXRAIL state>``
    - **When the CommandStation is connected to a serial monitor, EX-RAIL script logging can be Enabled or Disabled** |BR|
      *Parameters:* |BR|
      state: one of |BR|
      |_| |_| ON |BR|
      |_| |_| OFF |BR| |BR|
      *Response:* |BR|
      N/A
  * - ``</ PAUSE>``
    - **Pauses ALL EX-RAIL automation actvites, including sending an E-STOP to all locos.** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      N/A
  * - ``</ RESUME>``
    - **Resumes ALL EX-RAIL automation actvites, and resumes all locos at the same speed at which they were paused.** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      N/A
  * - ``</>``
    - **Displays EX-RAIL running task information.** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<* EXRAIL STATUS |BR|
      ID=0,PC=189,LOCO=0 ,SPEED=0F |BR|
      ID=2,PC=267,LOCO=0 ,SPEED=0F |BR|
      ID=1,PC=228,LOCO=0 ,SPEED=0F |BR|
      RED[110] |BR|
      RED[113] *>** |BR|
      |BR|
      
  * - ``</ ROUTES>``
    - **Returns the Routes & Automations control list in wiThrottle Protocol format.** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<X>**
  * - ``</ START [locoAddr] routeId>``
    - **Starts a new task to send a loco onto a Route, or activate a non-loco Animation or Sequence** |BR|
      *Parameters:* |BR|
      locoAddr: DCC address of the loco |BR|
      routeId: id of the rout to start |BR| |BR|
      *Response:* |BR|
      ???
  * - ``</ KILL taskId>``
    - **Kills a currently running script task by ID (use to list task IDs)** |BR|
      *Parameters:* |BR|
      task_id: ?? |BR| |BR|
      *Response:* |BR|
      ???
  * - ``</ RESERVE blockId>``
    - **Manually reserves a virtual track Block** |BR|
      *Parameters:* |BR|
      block_id: ?? valid ids and in the range 0-255 |BR| |BR|
      *Response:* |BR|
      ???
  * - ``</ FREE blockId>``
    - **Manually frees a virtual track Block** |BR|
      *Parameters:* |BR|
      block_id: ?? valid ids and in the range 0-255 |BR| |BR|
      *Response:* |BR|
      ???
  * - ``</ LATCH sensorId>``
    - **Lock sensor ON, preventing external influence** |BR|
      *Parameters:* |BR|
      sensor_id:  ??  valid ids and in the range 0-255 |BR| |BR|
      *Response:* |BR|
      ??? |BR|
      |BR|
      **<* Opcode=L params=2 *>** |BR|
      **<* p[0]=-7906 (0xE11E) *>** |BR|
      **<* p[1]=24 (0x18) *>** |BR|
      **<X>**
  * - ``</ UNLATCH sensorId>``
    - **Unlock sensor, returning to current external state** |BR|
      *Parameters:* |BR|
      sensor_id: ??  valid ids and in the range 0-255 |BR| |BR|
      *Response:* |BR|
      ??? |BR|
      |BR|
      **<* Opcode=U params=2 *>** |BR|
      **<* p[0]=23772 (0x5CDC) *>** |BR|
      **<* p[1]=24 (0x18) *>** |BR|
      **<X>**

---

Configuring the EX-CommandStation
=================================

Configuring the EX-CommandStation - Turnouts/Points
---------------------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<T id DCC addr subaddr>``
    - **Define turnout on a DCC Accessory Decoder with the specified address and subaddress.** |BR|
      *Parameters:* |BR|
      id: ??? |BR|
      addr:: ??? |BR|
      subaddr: ??? |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<T id DCC linearAddr>``
    - **Define turnout on a DCC Accessory Decoder with the specified linear address** |BR|
      *Parameters:* |BR|
      id: ??? |BR|
      linearAddr: ??? |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<T id SERVO vpin thrownPos closedPos profile>``
    - **Define turnout servo (PWM) on specified vpin.  Note: Servos are not supported on the minimal HAL (Uno or Nano target).** |BR|
      *Parameters:* |BR|
      id: unique Id for the servo |BR|
      vpin: vpin to which the servo is attached |BR|
      thrownPos: position for the servo when thrown |BR|
      closedPos: position for the servo when closed |BR|
      profile: one of |BR|
      |_| |_| 0=Instant,  |BR|
      |_| |_| 1=Fast (0.5 sec),  |BR|
      |_| |_| 2=Medium (1 sec),  |BR|
      |_| |_| 3=Slow (2 sec) and  |BR|
      |_| |_| 4=Bounce (subject to revision). |BR| |BR|
      *Response:* |BR|
      **<X|O>** |BR|
      |BR|
      Response (successful): **<O>** |BR|
      Response (fail): **<X>**
      |BR|
      *Notes:* |BR|
      The active and inactive positions are defined in terms of the PWM parameter (0-4095 corresponds to 0-100% PWM). The limits for an SG90 servo are about 102 to 490. The standard range of 1ms to 2ms pulses correspond to values 205 to 409.
      |BR|
      Profile defines the speed and style of movement: 0=Instant, 1=Fast (0.5 sec), 2=Medium (1 sec), 3=Slow (2 sec) and 4=Bounce (subject to revision).
  * - ``<T id VPIN vpin>``
    - **Define turnout output on specified vpin.** |BR|
      *Parameters:* |BR|
      id: unique Id for the servo |BR|
      vpin: vpin to which the servo is attached |BR| |BR|
      *Response:* |BR|
      ???
      |BR|
      *Notes:* |BR|
      This may be used for controlling Arduino digital output pins or pins on an I/O Extender.
  * - ``<T id>``
    - **Define VPIN turnout** |BR|
      *Parameters:* |BR|
      id: unique Id for the servod |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<T id addr subaddr>``
    - **Legacy command format for defining a turnout on a DCC Accessory Decoder with the specified address and subaddress.** |BR|
      **Deprecated** |BR|
      *Parameters:* |BR|
      id: ??? |BR|
      addr: ??? |BR|
      subaddr: ??? |BR| |BR|
      *Response:* |BR|
      ??? |BR|
      *Version Deprecated: ???*
  * - ``<T id vpin activePos
      inactivePos>``
    - **Legacy command format for defining a turnout servo on specified vpin. The positions are the same as for the turnout servo command above. Note: Servos are not supported on the minimal HAL (Uno or Nano target).** |BR|
      **Deprecated** |BR|
      *Parameters:* |BR|
      id: ??? |BR|
      vpin: ??? |BR|
      activePos: ??? |BR|
      inactivePos: ??? |BR| |BR|
      *Response:* |BR|
      ??? |BR|
      *Version Deprecated: ???*

Once all turnout/points have been properly defined, you can use the ``<E>`` (upper case E) command to store their definitions to EEPROM. 

Configuring the EX-CommandStation - Sensors
-------------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<S id vpin pullup>``
    - **Create a new sensor ID** |BR|
      *Parameters:* |BR|
      id numeric ID 0-32767 of the sensor |BR|
      vpin pin number of the input to be controlled by the sensor object |BR|
      pullup  |BR|
      |_| |_| 1=Use pull-up resistor ACTIVE=LOW  |BR|
      |_| |_| 0=don't use pull-up resistor ACTIVE=HIGH |BR| |BR|
      *Response:* |BR|
      **<O>** |BR|
      |BR|
      Response (successful): **<O>** |BR|
      Response (fail): ???? |BR|
      |BR|
      Note: Once defined, the EX-CS will send a **<Q id>** response anytime the sensor is activated, and a **<q id>** response when deactivated.
  * - ``<S id>``
    - **Delete defined sensor** |BR|
      *Parameters:* |BR|
      id: identifier of the Sensor |BR| |BR|
      *Response:* |BR|
      **<O|X>** |BR|
      |BR|
      Response (successful): **<O>** |BR|
      Response (fail): **<X>**

Once all sensors have been properly defined, you can use the ``<E>`` (upper case E) command to store their definitions to EEPROM. 

Outputs
-------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<Z>``
    - **Lists all defined output pins** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<Z id pin iflag>``
    - **Creates a new output ID, with specified PIN and IFLAG values** |BR|
      *Parameters:* |BR|
      ifflag, bit 0: |BR|
      |_| |_| 0 = forward operation (ACTIVE=HIGH / INACTIVE=LOW) |BR|
      |_| |_| 1 = inverted operation (ACTIVE=LOW / INACTIVE=HIGH) |BR|
      |BR|
      ifflag, bit 1: |BR|
      |_| |_| 0 = state of pin restored on power-up to either ACTIVE or INACTIVE depending on state before power-down. |BR|
      |_| |_| 1 = state of pin set on power-up, or when first created, to either ACTIVE of INACTIVE depending on IFLAG, bit 2 |BR|
      |BR|
      ifflag, bit 2:  |BR|
      |_| |_| 0 = state of pin set to INACTIVE upon power-up or when first created |BR|
      |_| |_| 1 = state of pin set to ACTIVE upon power-up or when first created |BR|
      |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<Z id state>``
    - **Sets output ID to either INACTIVE or ACTIVE state** |BR|
      *Parameters:* |BR|
      id: ??? |BR|
      state:  |BR|
      |_| |_| 0= ???  |BR|
      |_| |_| 1= ??? |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<Z id>``
    - **Deletes definition of output ID** |BR|
      *Parameters:* |BR|
      id: ??? |BR| |BR|
      *Response:* |BR|
      ???

Configuring the EX-CommandStation - EEPROM management
-----------------------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<E>``
    - **Store definitions to EEPROM** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<O>**
  * - ``<e>``
    - **Erase ALL (turnouts, sensors, and outputs) from EEPROM** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      **<O>**
  * - ``<D EEPROM>``
    - **Diagnostic dump eeprom contents** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      ???

Configuring the EX-CommandStation - Diagnostic programming commands
-------------------------------------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<D ACK LIMIT mA>``
    - **Sets the ACK limit** |BR|
      *Parameters:* |BR|
      mA: |BR|
      |BR|
      The Ack current limit is set according to the DCC standard(s) of 60mA. Most decoders send a quick back and forth current pulse to the motor to generate this ACK. However, some modern motors (N and Z scales) may not be able to draw that amount of current. You can adjust down this limit. Or, if for some reasons your acks seem to be too “trigger happy” you can make it less sensitive by raising this limit. |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<D ACK MIN µS>``
    - **Sets the ACK pulse minimum** |BR|
      *Parameters:* |BR|
      µS |BR|
      |BR|
      The NMRA specifies that the ACK pulse duration should be 6 milliseconds, which is 6000 microseconds (µS), give or take 1000 µS. That means the minimum pulse duration is 5000 µS and the maximum is 7000 µS. There are many poorly designed decoders in existence so DCC-EX extends this range from 4000 to 8500 µS. If you have any decoders that still do not function within this range, you can adjust the ACK MIN and ACK MAX parameters. |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<D ACK MAX µS>``
    - **Sets the ACK pulse maximum** |BR|
      *Parameters:* |BR|
      µS |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<D ACK MIN µS>``
    - **Sets the ACK pulse maximum** |BR|
      *Parameters:* |BR|
      µS |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<D PROGBOOST>``
    - **Override 250mA prog track limit while idle** |BR|
      *Parameters:* |BR|
      N/A |BR|
      |BR|
      When the programming track is switched on with **<1>** or **<1 PROG>** it will normally be restricted to 250mA according to NMRA standards. Some loco decoders require more than this, especially sound versions. **<D PROGBOOST>** temporarily removes this limit to allow the decoder to use more power. The normal limit will be re-imposed when the programming track is switched off with **<0>** or **<0 PROG>** or the Command Station is reset. |BR|
      |BR| |BR|
      *Response:* |BR|
      ???

Diagnostic programming commands
-------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<D ACK MAX µS>``
    - **Sets the ACK pulse maximum** |BR|
      *Parameters:* |BR|
      µS |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<D ACK MIN µS>``
    - **Sets the ACK pulse maximum** |BR|
      *Parameters:* |BR|
      µS |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<D PROGBOOST>``
    - **Override 250mA prog track limit while idle** |BR|
      *Parameters:* |BR|
      N/A |BR|
      |BR|
      When the programming track is switched on with **<1>** or **<1 PROG>** it will normally be restricted to 250mA according to NMRA standards. Some loco decoders require more than this, especially sound versions. **<D PROGBOOST>** temporarily removes this limit to allow the decoder to use more power. The normal limit will be re-imposed when the programming track is switched off with **<0>** or **<0 PROG>** or the Command Station is reset. |BR| |BR|
      *Response:* |BR|
      ???

I/O (HAL) Diagnostics
---------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<D HAL SHOW>``
    - **List HAL devices and allocated VPINs** |BR|
      *Parameters:* |BR|
      N/A |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<D SERVO vpin value [profile]>``
    - **Set servo position to value on pin vpin.** |BR|
      *Parameters:* |BR|
      vpin: |BR|
      value: |BR|
      profile: |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<D ANOUT vpin value [param2]>``
    - **Write value to analogue pin vpin, supplying param2 to the driver.** |BR|
      *Parameters:* |BR|
      vpin: |BR|
      value: |BR|
      param2: |BR| |BR|
      *Response:* |BR|
      ???
  * - ``<D ANIN vpin>``
    - **Read and display pin vpin’s analogue value.** |BR|
      *Parameters:* |BR|
      vpin: ?? |BR| |BR|
      *Response:* |BR|
      ???

Other
-----

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<U ...>``
    - **Is reserved for user commands (through user filter)** |BR|
      *Parameters:* |BR|
      |BR| |BR|
      *Response:* |BR|
      ???

More Information
================

 **For a detailed command reference, see...**
  :doc:`Command Reference <command-reference>`
