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
  * - ``<D RESET>``
    - **Re-boot the command Station** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|

  * - ``<J I>`` |BR| ``<JI>``
    - **Request current status** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| repeated for each Channel/Track: **<j I track current>** |BR|
      |_|  |BR|
      |_| **track:**  channel/track |BR|
      |_| **current:** current in milliamps |BR| |BR|
      |_| *Version Introduced: 4.2.19* |BR|

  * - ``<J G>``  |BR| ``<JG>``
    - **Request max current** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| repeated for each Channel/Track: **<j IG track currentmax>** |BR|
      |_|  |BR|
      |_| **track:**  channel/track |BR|
      |_| **currentmax:** current in milliamps |BR| |BR|
      |_| *Version Introduced: 4.2.19* |BR|

  * - ``<onOff [track]>``
    - **Turns power on and off to the MAIN and PROG tracks together or independently. Also allows joining the MAIN and PROG tracks together.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **onOff:** one of |BR|
      |_|  |_| 1 = on |BR|
      |_|  |_| 0 = off |BR|
      |_| **track:** one of |BR|
      |_|  |_| blank = Both Main and Programming Tracks  |BR|
      |_|  |_| MAIN = Main track  |BR|
      |_|  |_| PROG = Programming Track  |BR|
      |_|  |_| JOIN = Join the Main and Programming tracks temporarily |BR|
      |_|  |BR|
      |_| e.g. |BR|
      |_| all tracks off: **<0>** |BR|
      |_| all tracks on **<1>** |BR|
      |_| join: **<1 JOIN>** |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| The use of the JOIN function ensures that the DCC signal for the MAIN track is also sent to the PROG track. This allows the prog track to act as a siding (or similar) in the main layout even though it is isolated electrically and connected to the programming track output. However, it is important that the prog track wiring be in the same phase as the main track i.e. when the left rail is high on MAIN, it is also high on PROG. You may have to swap the wires to your prog track to make this work. If you drive onto a programming track that is “joined” and enter a programming command, the track will automatically switch to a programming track. If you use a compatible Throttle, you can then send the join command again and drive off the track onto the rest of your layout! |BR|
      |_|  |BR|
      |_| In some split motor shield hardware configurations JOIN will not be able to work. |BR| |BR|

Cab (Loco) Commands
-------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<f cab byte1 [byte2]]>``
    - **Decoder Functions - Legacy command.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cab:** DCC Address of the decoder/loco |BR|
      |_| **byte1 byte2:** DCC function bytes as sent to decoders (up to F28)  |BR| |BR|
      |_| *Response:* |BR|
      |_| |_| Success: nothing |BR|
      |_| |_| Fail: **<X>** |BR| |BR|
      |_| *Notes:* |BR|
      |_| Used by the sniffer |BR| |BR|

  * - ``<!>``
    - **Emergency Stop** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| Repeated for each loco in the reminders list **<l cab reg speedByte functMap>**  |BR| |BR|

  * - ``<- [cab]>``
    - **Remove one or all locos from reminders** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cab:** one of |BR|
      |_|  |_| blank = all locos  |BR|
      |_|  |_| No. = Cab (loco) to forget |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| Forgets one or all locos. The “cab” parameter is optional.  |BR|
      |_| Once you send a throttle command to any loco, throttle commands to that loco will continue to be sent to the track. If you remove the loco, or for testing purposes need to clear the loco from repeating messages to the track, you can use this command. Sending **<- cab>** will forget/clear that loco. Sending **<->** will clear all the locos. This doesn't do anything destructive or erase any loco settings, it just clears the speed reminders from being sent to the track. As soon as a controller sends another throttle command, it will go back to repeating those commands. |BR| |BR|

  * - ``<J R id>`` |BR| ``<JR id>``
    - **Request details of a specific Roster Entry** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** unique id of the Cab/s (Loco/s) in the roster |BR| |BR|
      |_| *Response:* |BR|
      |_| **<jR id ˮˮ|ˮdescˮ ˮˮ|ˮfunct1/funct2/funct3/...ˮ>** |BR|
      |_| **id:**  unique id of the Cab/s (Loco/s) in the roster |BR|
      |_| **desc:** description of the Loco |BR|
      |_| **funct?:** Label for each function 0-28 |BR|
      |_|  |BR|
      |_| e.g.  |BR|
      |_| Response (id is in Roster): **<jR id ˮdescˮ ˮfunct1/funct2/funct3/...ˮ>** |BR|
      |_| Response (id is not in Roster): **<jR id ˮˮ ˮˮ>** |BR| |BR|

  * - ``<J R>`` |BR| ``<JR>``
    - **Request the list defined Roster Entry IDs** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<jR [id1 id2 id3 ...]>** |BR|
      |_| **id?:** unique id of the Cab/s (Loco/s) in the roster |BR|
      |_|  |BR|
      |_| e.g. |BR|
      |_| Response (roster exists): **<jR id1 id2 id3 ...>** |BR|
      |_| Response (no roster exists): **<jR>** |BR| |BR|

  * - ``<t cab>``
    - **Requests a deliberate update on the cab speed/functions in the same format as the cab (loco) broadcast.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cab:** DCC Address of the decoder/loco |BR| |BR|
      |_| *Response:* |BR|
      |_| The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question. |BR|
      |_|  |BR|
      |_| **<l cab reg speedByte functMap>** |BR|
      |_| **cab:** DCC Address of the decoder/loco |BR|
      |_| **speedbyte:** Speed in DCC speedstep format . |BR|
      |_|  |_| reverse - 2-127 = speed 1-126, 0 = stop  |BR|
      |_|  |_| forward - 130-255 = speed 1-126,  128 = stop |BR|
      |_| **FunctiMap:** individual function states represented by the the bits in a byte |BR| |BR|
      |_| *Notes:* |BR|
      |_| The *speedbyte* value is different to the *speed* sent, as it is an encoded (1,7 bits)  byte. |BR|
      |_| This starts a reminder process for any external updates to the cab's (loco's) status. |BR| |BR|

  * - ``<t cab speed dir>``
    - **Set Cab (Loco) Speed** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cab:** DCC Address of the decoder/loco |BR|
      |_| **speed:** 0-127 |BR|
      |_| **dir:** one of |BR|
      |_|  |_| 1=forward  |BR|
      |_|  |_| 0=reverse |BR| |BR|
      |_| *Response:* |BR|
      |_| The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question. |BR|
      |_|  |BR|
      |_| **<l cab reg speedByte functMap>** |BR|
      |_| **cab:** DCC Address of the decoder/loco |BR|
      |_| **speedbyte:** Speed in DCC speedstep format . |BR|
      |_|  |_| reverse - 2-127 = speed 1-126, 0 = stop  |BR|
      |_|  |_| forward - 130-255 = speed 1-126,  128 = stop |BR|
      |_| **FunctiMap:** individual function states represented by the the bits in a byte |BR| |BR|
      |_| *Version Introduced: 4.1.1* |BR|
      |_| *Notes:* |BR|
      |_| The *speedbyte* value is different to the *speed* sent, as it is an encoded (1,7 bits)  byte. |BR|
      |_| This starts a reminder process for any external updates to the cab's (loco's) status. |BR| |BR|

  * - ``<D speedsteps>``
    - **Switch between 28 and 128 speed steps** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **speedsteps:** |BR|
      |_|  |_| SPEED28 = use 28 speed steps |BR|
      |_|  |_| SPEED128 = use 128 speed steps |BR| |BR|
      |_| *Response:* |BR|
      |_| Response sent to the Serial Monitor only (not wifi clients). |BR|
      |_| One of: |BR|
      |_|  |_| *28 Speedsteps* |BR|
      |_|  |_| *128 Speedsteps* |BR| |BR|

  * - ``<F cab funct state>``
    - **Turns loco decoder functions ON and OFF** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cab:** DCC Address of the decoder/loco |BR|
      |_| **funct:** 0-28 (F29-F68 (Support for the RCN-212 Functions) |BR|
      |_| **state:**  |BR|
      |_|  |_| 1=on  |BR|
      |_|  |_| 0=off |BR| |BR|
      |_| *Response:* |BR|
      |_| The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question. |BR|
      |_|  |BR|
      |_| **<l cab reg speedByte functMap>** |BR|
      |_| **cab:** DCC Address of the decoder/loco |BR|
      |_| **speedbyte:** Speed in DCC speedstep format . |BR|
      |_|  |_| reverse - 2-127 = speed 1-126, 0 = stop  |BR|
      |_|  |_| forward - 130-255 = speed 1-126,  128 = stop |BR|
      |_| **FunctiMap:** individual function states represented by the the bits in a byte |BR| |BR|
      |_| *Notes:* |BR|
      |_| Setting requests are transmitted directly to mobile loco decoder. |BR|
      |_| Current state of loco functions (as known by commands issued since power on) is stored by the CommandStation - All functions within a group get set all at once per NMRA DCC standards. |BR|
      |_| The command station knows about the previous settings in the same group and will not, for example, unset F2 because you change F1. If, however, you have never set F2, then changing F1 WILL unset F2. |BR| |BR|

  * - ``<t reg cab speed dir>``
    - **Set Cab (Loco) Speed - Legacy command** |BR| |BR|
      |_| |DEPRECATED| |BR|
      |_| *Parameters:* |BR|
      |_| **reg:** not used |BR|
      |_| **cab:** DCC Address of the decoder/loco |BR|
      |_| **speed:** 0-127 |BR|
      |_| **dir:** one of  |BR|
      |_|  |_| 1=forward  |BR|
      |_|  |_| 0=reverse |BR| |BR|
      |_| *Response:* |BR|
      |_| The following is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question. |BR|
      |_|  |BR|
      |_| **<l cab reg speedByte functMap>** |BR|
      |_| **cab:** DCC Address of the decoder/loco |BR|
      |_| **reg:** redundant. Not used. |BR|
      |_| **speedbyte:** Speed in DCC speedstep format . |BR|
      |_|  |_| reverse - 2-127 = speed 1-126, 0 = stop  |BR|
      |_|  |_| forward - 130-255 = speed 1-126,  128 = stop |BR|
      |_| FunctMap: individual function states represented by the the bits in a byte |BR|
      |_|  |BR|
      |_| Legacy response: **Deprecated** |BR|
      |_| **<T reg speed dir>** - do not rely on this response |BR| |BR|
      |_| *Version Deprecated: 4.1.1* |BR|
      |_| *Notes:* |BR|
      |_| The *speedbyte* value is different to the *speed* sent, as it is an encoded (1,7 bits)  byte. |BR|
      |_| This starts a reminder process for any external updates to the cab's (loco's) status. |BR| |BR|

Turnout/Points
--------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<T id>``
    - **Delete defined turnout/point** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Turnout/Point |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<T>``
    - **Request a list all defined turnouts/Points** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| Repeated for each defined Turnout/Point |BR|
      |_| Response (DCC Accessories): **<H id DCC address subaddress state>** |BR|
      |_| Response (Servos): **<H id SERVO vpin thrown_position closed_position profile state>** |BR|
      |_| Response (VPIN): **<H id VPIN vpin state>** |BR|
      |_| Response (LCN): **<H id LCN state>** |BR|
      |_| Response (fail): ? |BR|
      |_| Response (no defined turnouts/points): ? |BR|
      |_|  |BR|
      |_| state - 0=closed 1=thrown |BR| |BR|

  * - ``<J T id>`` |BR| ``<JT id>``
    - **Request details of a specific Turnout/Point** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:**  unique id of the Turnout/Point  |BR| |BR|
      |_| *Response:* |BR|
      |_| **<jT id X|state |ˮ[desc]ˮ>** |BR|
      |_| **id:** unique id of the Turnout/Point  |BR|
      |_| **state:** one of |BR|
      |_|  |_| C = Closed |BR|
      |_|  |_| T = Thrown |BR|
      |_|  |_| X = unknown id |BR|
      |_| **desc:** one of  |BR|
      |_|  |_| ˮdescˮ = description of the Turnout(Point) (including surrounding quotes) |BR|
      |_|  |_| blank = unknown id |BR|
      |_|  |BR|
      |_| e.g. |BR|
      |_| Response (id is defined): **<jT id state ˮ[desc]ˮ>** |BR|
      |_| Response (id not defined): **<jT id X>** |BR| |BR|

  * - ``<J T>`` |BR| ``<JT>``
    - **Request the list of defined turnout/Point IDs** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<jT [id1 id2 id3 ...]>** |BR|
      |_| **id:** unique id of the Turnout/s(Point/s) |BR|
      |_|  |BR|
      |_| e.g. |BR|
      |_| Response (has defined Turnouts/Points): **<jT id1 id2 id3 ...>** |BR|
      |_| Response (no defined Turnouts/Points): **<jT>** |BR| |BR|

  * - ``<T id state>``
    - **Throw (1 or T) or close(0 or C) a defined turnout/point** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Turnout/Point |BR|
      |_| **state:** one of |BR|
      |_|  |_| 1=Throw,  |BR|
      |_|  |_| T=Throw,  |BR|
      |_|  |_| 0=Close,  |BR|
      |_|  |_| C=Close  |BR| |BR|
      |_| *Response:* |BR|
      |_| **<H id state>** |BR|
      |_| **id:** one of |BR|
      |_|  |_| identifier of the Turnout/Point, or  |BR|
      |_|  |_| X if the command fails |BR|
      |_| **state:** one of |BR|
      |_|  |_| 1 = Thrown,  |BR|
      |_|  |_| 0 = Closed  |BR|
      |_|  |_| blank = command failed |BR|
      |_|  |BR|
      |_| e.g. |BR|
      |_| Response (successful): **<H id 0|1>** |BR|
      |_| Response (fail): **<X>** |BR| |BR|

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
    - **Request a list of Automations/Routes** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<jA [id0 id1 id2 ..]>** |BR|
      |_| **id?:** identifier of the Route/Automation(s) |BR|
      |_|  |BR|
      |_| e.g. |BR|
      |_| Response (successful turnouts/point exist): **<jA id0 id1 id2 ..>** |BR|
      |_| Response (successful turnouts/point don't exist): **<jA.>** |BR|
      |_| Response (fail): ??? |BR| |BR|

  * - ``<J A id>`` |BR| ``<JA id>``
    - **Requests information for a route/automation** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Route/Automation |BR| |BR|
      |_| *Response:* |BR|
      |_| **<jA id X|type |ˮdescˮ>** |BR|
      |_| **id:** identifier of the Route/Automation |BR|
      |_| **type:** one of |BR|
      |_|  |_| ‘R'= Route  |BR|
      |_|  |_|  ‘A'=Automation |BR|
      |_| **“desc”:** Textual description of the route/automation always surrounded in quotes (“) |BR|
      |_|  |BR|
      |_| e.g. |BR|
      |_| Response (successful): **<jA id type ˮdescˮ>** |BR|
      |_| Response (fail - is not defined): **<jA id X>** |BR|
      |_|  |BR| |BR|

System Information
------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<c>``
    - **Request Current on the Track(s)** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<c ˮCurrentMAINˮ current C ˮMilliˮ ˮ0ˮ max_ma ˮ1ˮ trip_ma>** |BR|
      |_| **ˮCurrentMAINˮ:** Static text for software like JMRI |BR|
      |_| **current**: Current in MilliAmps |BR|
      |_| **C**: Designator to signify this is a current meter (V would be for voltage) |BR|
      |_| **ˮMilliˮ**: Unit of measure for external software with a meter like JMRI (Milli, Kilo, etc.) |BR|
      |_| **ˮ0ˮ:** numbered parameter for external software (1,2,3, etc.) |BR|
      |_| **max_ma**: The maximum current handling of the motor controller in MilliAmps |BR|
      |_| **ˮ1ˮ**: number parameter for external software (we use 2 parameters here, 0 and 1) |BR|
      |_| **trip_ma** - The overcurrent limit that will trip the software circuit breaker in mA |BR| |BR|
      |_| *Version Introduced: ??.* |BR|

  * - ``<s>``
    - **Requests the DCC-EX version and hardware info, along with listing defined turnouts.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<iDCCEX version / microprocessorType / MotorControllerType / buildNumber>** |BR|
      |_| (repeated for each defined Turnout/Point): **<H id state>** |BR|
      |_|  |BR|
      |_| **version:** Command Station version |BR|
      |_| **microprocessorType:**  microprocessor type (e.g. MEGA) |BR|
      |_| **MotorControllerType:**  Motor controller type (e.g. SATNDARD_MOTOR_SHIELD) |BR|
      |_| **buildNumber:**  Command Station build number |BR|
      |_| **id:** unique identifier for the Turnout/Point |BR|
      |_| **state:** one of  |BR|
      |_|  |_| 1=thrown  |BR|
      |_|  |_| 0=Closed |BR| |BR|

  * - ``<#>``
    - **Requests the number of supported cabs(locos)** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<# noCabs>** |BR|
      |_| **noCabs:** maximum number of Cabs(Locos) supported by the command station |BR|
      |_|  |BR| |BR|
      |_| *Notes:* |BR|
      |_| This will display the number of available cab slots. This will typically be **<# 20>**, **<# 30>**, or **<# 50>** depending on how much memory your EX‑CommandStation has available.  |BR|
      |_| This is a design limit based on the memory limitations of the particular hardware and a compromise with other features that require memory such as WiFI. If you need more slots and are comfortable with code changes you can adjust this by changing MAX_LOCOS in “DCC.h”, knowing that each new slot will take approximately 8 bytes of memory. The **<D RAM>** command will display the amount of free memory. If you fill the available slots, the “Forget Locos” command (**<- [CAB]>**) will free up unused locos. Currently there is no automatic purging of unused locos. |BR| |BR|

Writing CVs - Program on the main
---------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<b address cv bit value>``
    - **Write CV bit on main track** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **address:** DCC Address of the decoder/loco |BR|
      |_| **cv:** CV number |BR|
      |_| **bit:** ???  |BR|
      |_| **value:** value to change the CV to |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<w address cv value>``
    - **Write CV on main track** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **address:** DCC Address of the decoder/loco |BR|
      |_| **cv:** CV number |BR|
      |_| **value:** value to change the CV to |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|

Reading/Writing CVs - Programming track
---------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<R cv>``
    - **Read CV** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cv:** CV number |BR| |BR|
      |_| *Response:* |BR|
      |_| **<r cv value>** |BR|
      |_| **cv:** CV number |BR|
      |_| **value:** one of |BR|
      |_|  |_| value of the CV |BR|
      |_|  |_| -1: if the write failed |BR| |BR|

  * - ``<R>``
    - **Read DCC decoder address** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<r -cab>** |BR|
      |_| **cab:** |BR|
      |_|  |_| DCC Address of the decoder/loco |BR|
      |_|  |_| -1 = failed read |BR|
      |_|  |BR|
      |_| e.g. |BR|
      |_| Response (successful): **<r cab>** |BR|
      |_| Response (fail): **<r -1>** |BR| |BR|

  * - ``<V cv bit onOff>``
    - **Verify/Read bit of CV with guessed value** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cv:** CV number |BR|
      |_| **bit:** bit to verify in the CV |BR|
      |_| **onOff:** one of |BR|
      |_|  |_| 1=on  |BR|
      |_|  |_| 0=off |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<V cv value>``
    - **Verify/Read of CV with guessed value** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cv:** CV number |BR|
      |_| **value:**  value to verify |BR| |BR|
      |_| *Response:* |BR|
      |_| **<v cv value>** |BR|
      |_| **cv:** CV number |BR|
      |_| **value:** one of |BR|
      |_|  |_| actual value of the CV |BR|
      |_|  |_| -1: if the write failed |BR| |BR|
      |_| *Notes:* |BR|
      |_| Additional Notes |BR| |BR|

  * - ``<B cv bit onOff>``
    - **Write bit to CV** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cv:** CV number |BR|
      |_| **bit:** bit to change in the CV |BR|
      |_| **onOff:** one of  |BR|
      |_|  |_| 1=on  |BR|
      |_|  |_| 0=off |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<W cv value >``
    - **Write CV** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cv:** CV number |BR|
      |_| **value:** value to change the CV to |BR| |BR|
      |_| *Response:* |BR|
      |_| **<w cv value>** |BR|
      |_| **cv:** CV number |BR|
      |_| **value:** one of |BR|
      |_|  |_| value CV was changed to |BR|
      |_|  |_| -1: if the write failed |BR| |BR|

  * - ``<W address>``
    - **Write DCC address to cab (loco)** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **address:** DCC Address of the decoder/loco |BR| |BR|
      |_| *Response:* |BR|
      |_| **<w address>** |BR|
      |_| **address:** one of |BR|
      |_|  |_| DCC Address of the decoder/loco |BR|
      |_|  |_| -1 = failed read |BR|
      |_|  |BR|
      |_| Response (successful): **<w cab>** |BR|
      |_| Response (fail): **<w -1>** |BR| |BR|
      |_| *Notes:* |BR|
      |_| Writes, and then verifies, the address to decoder of an engine on the programming track. This involves clearing any consist and automatically setting a long or short address. This is an easy way to put a loco in a known state to test for issues like not responding to throttle commands when it is on the main track. |BR| |BR|

  * - ``<P register hex1 hex2 [hex3 [hex4 [hex5]]]>``
    - **Writes a DCC packet to the PROG track** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **register:** an internal register number, from 0 through MAX_MAIN_REGISTERS (inclusive), to write (if REGISTER=0) or write and store (if REGISTER>**0) the packet |BR|
      |_| **byte1:**  first hexadecimal byte in the packet |BR|
      |_| **byte2:**  second hexadecimal byte in the packet |BR|
      |_| **byte3:**  optional third hexadecimal byte in the packet |BR|
      |_| **byte4:**  optional fourth hexadecimal byte in the packet |BR|
      |_| **byte5:**  optional fifth hexadecimal byte in the packet |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<B cv bit value callbacknum callbacksub>``
    - **Deprecated, please use <W cv value> instead** |BR| |BR|
      |_| |DEPRECATED| |BR|
      |_| *Parameters:* |BR|
      |_| **cv:** CV to write |BR|
      |_| **bit:** bit of the CV to change |BR|
      |_| **value:** value to chnage the bit of CV to |BR|
      |_| **callbacknum:** ??? |BR|
      |_| **callbacksub:** ??? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|
      |_| *Version Deprecated: ???* |BR|

  * - ``<W cv value callbacknum callbacksub>``
    - **Deprecated, please use <w cv value> instead** |BR| |BR|
      |_| |DEPRECATED| |BR|
      |_| *Parameters:* |BR|
      |_| **cv:** CV to write |BR|
      |_| **value:** value to change the CV to |BR|
      |_| **callbacknum:** ??? |BR|
      |_| **callbacksub:** ??? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|
      |_| *Version Deprecated: ???* |BR|

Writing CVs - Programming track - Tuning
----------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<D ACK RETRY x>``
    - **Adjust ACK retries to number x (default is 2)** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **x:** ??? |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|

  * - ``<D PROGBOOST>``
    - **Override 250mA prog track limit while idle** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|

DCC Accessories
---------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<a addr subaddr activate>``
    - **Control an Accessory Decoder** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **addr:** the primary address of the decoder controlling the turnout (0-511) |BR|
      |_| **subaddr:** the subaddress of the decoder controlling this turnout (0-3) |BR|
      |_| **activate:** one of  |BR|
      |_|  |_| 0=off, deactivate, straight or Closed  |BR|
      |_|  |_| 1=on, activate, turn or thrown |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<a linear_addr activate>``
    - **Control an Accessory Decoder** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **linear_addr:** linear address of the decoder controlling this turnout (1-2044) |BR|
      |_| **activate:** one of  |BR|
      |_|  |_| 0=off, deactivate, straight or Closed  |BR|
      |_|  |_| 1=on, activate, turn or thrown |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

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
    - **Lists Status of all sensors** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| Repeat for each defined sensor: **<q id>** |BR|
      |_|  |BR|
      |_| e.g. |BR|
      |_| Response (successful) Repeat for each defined sensor: **<q id>** |BR|
      |_| Response (fail): N/A |BR| |BR|

  * - ``<S>``
    - **Requests a definition list of all defined sensors** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| Repeated for each defined sensor: **<Q id vpin pullup>** |BR|
      |_| **id:** identifier of the Sensor. (0-32767) |BR|
      |_| **vpin:** pin number of the input to be controlled by the sensor object |BR|
      |_| **pullup:** one of |BR|
      |_|  |_| 1=Use pull-up resistor ACTIVE=LOW  |BR|
      |_|  |_| 0=don't use pull-up resistor ACTIVE=HIGH |BR|
      |_|  |BR|
      |_| e.g. |BR|
      |_| Response (successful) Repeated for each defined sensor: **<Q id vpin pullup>** |BR|
      |_| Response (fail): **<X>** |BR| |BR|

WiFi Control
------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<+X>``
    - **Force the Command Station into “WiFi Connected” mode** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<+command>``
    - **Sends AT+ commands to the WiFi board (ESP8266, ESP32, etc.)** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **command:** what you want to append after AT+ and send to the AT processor. |BR| |BR|
      |_| *Response:* |BR|
      |_|  |BR| |BR|
      |_| *Notes:* |BR|
      |_| **<+X>** would send AT+X to the ESP |BR| |BR|

  * - ``<+>``
    - **Switch to direct communication with WiFi AT processor** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| None |BR| |BR|
      |_| *Response:* |BR|
      |_| All input and output from this point is the direct communication with the Wifi AT software this mode is ended by typing ! (exclamation mark). |BR| |BR|

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
    - **Configure Track Manager Note: since only one channel can be PROG, changing a second channel to PROG, will force the other to OFF** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **trackletter:** 'A' through 'H' represent one of the outputs of the/a motor shield. |BR|
      |_| **mode:** one of  |BR|
      |_|  |_| MAIN |BR|
      |_|  |_| PROG |BR|
      |_|  |_| DC |BR|
      |_|  |_| DCX = DC reversed polarity |BR|
      |_|  |_| OFF (DCX is DC with reversed polarity) |BR|
      |_| **id:** the cab ID. *Required when specifying DC or DCX* |BR| |BR|
      |_| *Response:* |BR|
      |_| (for each track/channel that has changed) **<= trackletter state cab>** |BR|
      |_|  |BR|
      |_| **trackletter:** A-H |BR|
      |_| **state:**  PROG, MAIN DC, DCX |BR|
      |_| **cab:** cab(loco) equivalent to a fake DCC Address |BR| |BR|

  * - ``<=>``
    - **Request the current Track Manager configuration** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| for each track/channel supported by the motor shield **<= trackletter state cab>** |BR|
      |_|  |BR|
      |_| **trackletter:** A-H |BR|
      |_| **state:** PROG, MAIN DC, DCX |BR|
      |_| **cab:** cab(loco) equivalent to a fake DCC Address |BR| |BR|

EX-RAIL
-------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``</ KILL taskId>``
    - **Kills a currently running script task by ID (use to list task IDs)** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **taskId:** ?? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``</ LATCH sensorId>``
    - **Lock sensor ON, preventing external influence** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **sensorId:**  ??  valid ids and in the range 0-255 |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR|
      |_|  |BR|
      |_| **<* Opcode=L params=2 *>** |BR|
      |_| **<* p[0]=-7906 (0xE11E) *>** |BR|
      |_| **<* p[1]=24 (0x18) *>** |BR|
      |_| **<X>** |BR| |BR|

  * - ``</ FREE blockId>``
    - **Manually frees a virtual track Block** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **blockId:** ?? valid ids and in the range 0-255 |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``</ RESERVE blockId>``
    - **Manually reserves a virtual track Block** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **blockId:** ?? valid ids and in the range 0-255 |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``</ PAUSE>``
    - **Pauses ALL EX-RAIL automation actvites, including sending an E-STOP to all locos.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|

  * - ``</>``
    - **Request EX-RAIL running task information.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<* EXRAIL STATUS |BR|
      |_| ID=0,PC=189,LOCO=0 ,SPEED=0F |BR|
      |_| ID=2,PC=267,LOCO=0 ,SPEED=0F |BR|
      |_| ID=1,PC=228,LOCO=0 ,SPEED=0F |BR|
      |_| RED[110] |BR|
      |_| RED[113] *>** |BR|
      |_|  |BR|
      |_|  |BR| |BR|

  * - ``</ ROUTES>``
    - **Request the Routes & Automations control list in wiThrottle Protocol format.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<X>** |BR| |BR|

  * - ``</ RESUME>``
    - **Resumes ALL EX-RAIL automation actvites, and resumes all locos at the same speed at which they were paused.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|

  * - ``</ START [locoAddr] routeId>``
    - **Starts a new task to send a loco onto a Route, or activate a non-loco Animation or Sequence** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| locoAddr: DCC address of the loco |BR|
      |_| routeId: id of the rout to start |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``</ UNLATCH sensorId>``
    - **Unlock sensor, returning to current external state** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **sensor_id:** ??  valid ids and in the range 0-255 |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR|
      |_|  |BR|
      |_| **<* Opcode=U params=2 *>** |BR|
      |_| **<* p[0]=23772 (0x5CDC) *>** |BR|
      |_| **<* p[1]=24 (0x18) *>** |BR|
      |_| **<X>** |BR| |BR|

  * - ``<D EXRAIL state>``
    - **When the CommandStation is connected to a serial monitor, EX-RAIL script logging can be Enabled or Disabled** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **state:** one of |BR|
      |_|  |_| ON |BR|
      |_|  |_| OFF |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|

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
    - **Define turnout on a DCC Accessory Decoder with the specified address and subaddress** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Turnout/Point |BR|
      |_| **addr:** ??? |BR|
      |_| **subaddr:** ??? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<T id DCC linearAddr>``
    - **Define turnout on a DCC Accessory Decoder with the specified linear address** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Turnout/Point |BR|
      |_| **linearAddr:** ??? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<T id VPIN vpin>``
    - **Define turnout output on specified vpin.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** unique Id for the servo |BR|
      |_| **vpin:** vpin to which the servo is attached |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|
      |_| *Notes:* |BR|
      |_|  This may be used for controlling Arduino digital output pins or pins on an I/O Extender. |BR| |BR|

  * - ``<T id SERVO vpin thrownPos closedPos profile>``
    - **Define turnout servo (PWM) on specified vpin Note: Servos are not supported on the minimal HAL (Uno or Nano target).** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** unique Id for the servo |BR|
      |_| **vpin:** vpin to which the servo is attached |BR|
      |_| **thrownPos:** position for the servo when thrown |BR|
      |_| **closedPos:** position for the servo when closed |BR|
      |_| **profile:** one of |BR|
      |_|  |_| 0=Instant,  |BR|
      |_|  |_| 1=Fast (0.5 sec),  |BR|
      |_|  |_| 2=Medium (1 sec),  |BR|
      |_|  |_| 3=Slow (2 sec) and  |BR|
      |_|  |_| 4=Bounce (subject to revision). |BR| |BR|
      |_| *Response:* |BR|
      |_| Successful: **<O>** |BR|
      |_| Fail: **<X>** |BR| |BR|
      |_| *Notes:* |BR|
      |_| The active and inactive positions are defined in terms of the PWM parameter (0-4095 corresponds to 0-100% PWM). The limits for an SG90 servo are about 102 to 490. The standard range of 1ms to 2ms pulses correspond to values 205 to 409. |BR|
      |_| Profile defines the speed and style of movement: 0=Instant, 1=Fast (0.5 sec), 2=Medium (1 sec), 3=Slow (2 sec) and 4=Bounce (subject to revision). |BR|
      |_|  |BR| |BR|

  * - ``<T id>``
    - **Deletes a turnout by Id.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** unique Id for the servod |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<D SERVO vpin value [profile]>``
    - **Set servo position to value on pin vpin.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **vpin:** vpin to which the servo is attached |BR|
      |_| **value:**  position to mve the servo to |BR|
      |_| **profile:**  one of |BR|
      |_|  |_| 0 = instant |BR|
      |_|  |_| 1 = fast |BR|
      |_|  |_| 2 = medium |BR|
      |_|  |_| 3 = slow |BR|
      |_|  |_| 4 = bounce |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|

  * - ``<T id addr subaddr>``
    - **Define a turnout on a DCC Accessory Decoder with the specified address and subaddress - Legacy command** |BR| |BR|
      |_| |DEPRECATED| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Turnout/Point |BR|
      |_| **addr:** ??? |BR|
      |_| **subaddr:** ??? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|
      |_| *Version Deprecated: ???* |BR|

  * - ``<T id vpin activePos
      inactivePos>``
    - **Define a turnout servo on specified vpin - Legacy command** |BR| |BR|
      |_| |DEPRECATED| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Turnout/Point |BR|
      |_| **vpin:** vpin of the input to be controlled by the sensor object |BR|
      |_| **activePos:** ??? |BR|
      |_| **inactivePos:** ??? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|
      |_| *Version Deprecated: ???* |BR|
      |_| *Notes:* |BR|
      |_| The positions are the same as for the turnout servo command above. Note: Servos are not supported on the minimal HAL (Uno or Nano target). |BR| |BR|

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
    - **Create a new sensor ID** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Sensor (0-32767) |BR|
      |_| **vpin:** vpin of the input to be controlled by the sensor object |BR|
      |_| **pullup:** one of  |BR|
      |_|  |_| 1=Use pull-up resistor ACTIVE=LOW  |BR|
      |_|  |_| 0=don't use pull-up resistor ACTIVE=HIGH |BR| |BR|
      |_| *Response:* |BR|
      |_| Successful: **<O>** |BR|
      |_| Fail: ???? |BR| |BR|
      |_| *Notes:* |BR|
      |_| Once defined, the EX-CS will send a **<Q id>** response anytime the sensor is activated, and a **<q id>** response when deactivated. |BR| |BR|

  * - ``<S id>``
    - **Delete defined sensor** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Sensor (0-32767) |BR| |BR|
      |_| *Response:* |BR|
      |_| Successful: **<O>** |BR|
      |_| Fail: **<X>** |BR| |BR|

Once all sensors have been properly defined, you can use the ``<E>`` (upper case E) command to store their definitions to EEPROM. 

Configuring the EX-CommandStation - Servos
------------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<S id pin state>``
    - **Creates a new sensor ID, with specified PIN and PULLUP** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Sensor (0-32767) |BR|
      |_| **pin:** pin the sensor is connected to |BR|
      |_| **state:** one of |BR|
      |_|  |_| 0= ???   |BR|
      |_|  |_| 1=??? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<S id>``
    - **Deletes definition of sensor** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the Sensor (0-32767) |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

Configuring the EX-CommandStation - Outputs
-------------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<Z id pin iflag>``
    - **Creates a new output ID, with specified PIN and IFLAG values** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the output |BR|
      |_| **pin:** pin to which the output will be connected |BR|
      |_| **iflag:** see below |BR|
      |_|  |BR|
      |_| iflag, bit 0: |BR|
      |_|  |_| 0 = forward operation (ACTIVE=HIGH / INACTIVE=LOW) |BR|
      |_|  |_| 1 = inverted operation (ACTIVE=LOW / INACTIVE=HIGH) |BR|
      |_| iflag, bit 1: |BR|
      |_|  |_| 0 = state of pin restored on power-up to either ACTIVE or INACTIVE depending on state before power-down. |BR|
      |_|  |_| 1 = state of pin set on power-up, or when first created, to either ACTIVE of INACTIVE depending on IFLAG, bit 2 |BR|
      |_| iflag, bit 2:  |BR|
      |_|  |_| 0 = state of pin set to INACTIVE upon power-up or when first created |BR|
      |_|  |_| 1 = state of pin set to ACTIVE upon power-up or when first created |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<Z id>``
    - **Deletes definition of output ID** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the output to delete |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<Z>``
    - **Lists all defined output pins** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<Z id state>``
    - **Sets output ID to either INACTIVE or ACTIVE state** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **id:** identifier of the output |BR|
      |_| **state:** one of  |BR|
      |_|  |_| 0= ???  |BR|
      |_|  |_| 1= ??? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

Configuring the EX-CommandStation - EEPROM management
-----------------------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<D EEPROM>``
    - **Diagnostic dump eeprom contents** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<e>``
    - **Erase ALL (turnouts, sensors, and outputs) from EEPROM** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<O>** |BR| |BR|

  * - ``<E>``
    - **Store definitions to EEPROM** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| **<O>** |BR| |BR|

Configuring the EX-CommandStation - Diagnostic programming commands
-------------------------------------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<D PROGBOOST>``
    - **Override 250mA prog track limit while idle** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| When the programming track is switched on with **<1>** or **<1 PROG>** it will normally be restricted to 250mA according to NMRA standards. Some loco decoders require more than this, especially sound versions. **<D PROGBOOST>** temporarily removes this limit to allow the decoder to use more power. The normal limit will be re-imposed when the programming track is switched off with **<0>** or **<0 PROG>** or the Command Station is reset. |BR| |BR|

  * - ``<D ACK LIMIT mA>``
    - **Sets the ACK limit** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **mA:** currently limit in milliamps |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| The Ack current limit is set according to the DCC standard(s) of 60mA. Most decoders send a quick back and forth current pulse to the motor to generate this ACK. However, some modern motors (N and Z scales) may not be able to draw that amount of current. You can adjust down this limit. Or, if for some reasons your acks seem to be too “trigger happy” you can make it less sensitive by raising this limit. |BR| |BR|

  * - ``<D ACK MAX µS>``
    - **Sets the ACK pulse maximum** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **µS:** ACK pulsedureation in milliseconds upper bound |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| see MIN |BR| |BR|

  * - ``<D ACK MIN µS>``
    - **Sets the ACK pulse minimum** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **µS:** ACK pulsedureation in milliseconds lower bound |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| The NMRA specifies that the ACK pulse duration should be 6 milliseconds, which is 6000 microseconds (µS), give or take 1000 µS. That means the minimum pulse duration is 5000 µS and the maximum is 7000 µS. There are many poorly designed decoders in existence so DCC-EX extends this range from 4000 to 8500 µS. If you have any decoders that still do not function within this range, you can adjust the ACK MIN and ACK MAX parameters. |BR| |BR|

Diagnostic traces
-----------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<D ACK state>``
    - **Enables ACK diagnostics** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **state:** one of |BR|
      |_|  |_| ON |BR|
      |_|  |_| OFF |BR| |BR|
      |_| *Response:* |BR|
      |_| ˮAck diag onˮ or ˮAck diag offˮ |BR|
      |_| Displayed on the serial monitor only. |BR| |BR|
      |_| *Notes:* |BR|
      |_| This will turn ACK diagnostics ON and then try to read the appropriate CVs to determine your loco address. |BR| |BR|

  * - ``<D CMD state>``
    - **Enables Command Parser diagnostics** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **state:** one of |BR|
      |_|  |_| ON |BR|
      |_|  |_| OFF |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| When enabled, diagnostic messages will be shown on the the serial monitor. |BR| |BR|

  * - ``<D ETHERNET state>``
    - **Enables Ethernet diagnostics** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **state:** one of |BR|
      |_|  |_| ON |BR|
      |_|  |_| OFF |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| When enabled, diagnostic messages will be shown on the the serial monitor. |BR| |BR|

  * - ``<D LCN state>``
    - **Enables LCN interface diagnostics** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **state:** one of |BR|
      |_|  |_| ON |BR|
      |_|  |_| OFF |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|

  * - ``<D WIFI state>``
    - **Enables WiFi diagnostics** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **state:** one of |BR|
      |_|  |_| ON |BR|
      |_|  |_| OFF |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| When enabled, diagnostic messages will be shown on the the serial monitor. |BR| |BR|

  * - ``<D WIT state>``
    - **Enables WiThrottle diagnostics** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **state:** one of |BR|
      |_|  |_| ON |BR|
      |_|  |_| OFF |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| When enabled, diagnostic messages will be shown on the the serial monitor. |BR| |BR|

  * - ``<D CABS>``
    - **Shows cab numbers and speed in reminder tables** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| ˮUsed=xxx, max=yyyˮ |BR|
      |_| Displayed on the serial monitor only. |BR| |BR|

  * - ``<D HAL SHOW>``
    - **Shows configured servo board and GPIO extender board config and used pins** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<D RAM>``
    - **Shows remaining RAM (Free Memory)** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| ˮFree memory=xxxxˮ |BR|
      |_| Displayed on the serial monitor only. |BR| |BR|

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
    - **List HAL devices and allocated VPINs** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| N/A |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<D ANIN vpin>``
    - **Read and display pin vpin’s analogue value.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **vpin:** ?? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

  * - ``<D ANOUT vpin value [param2]>``
    - **Write value to analogue pin vpin, supplying param2 to the driver.** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **vpin:** ?? |BR|
      |_| **value:**  ?? |BR|
      |_| **param2:** ?? |BR| |BR|
      |_| *Response:* |BR|
      |_| ??? |BR| |BR|

Write direct DCC packet
-----------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response
  * - ``<M register hex1 hex2 [hex3 [hex4 [hex5]]]>``
    - **Write a DCC packet the MAIN track** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **register:** ignored |BR|
      |_| **byte1:**  first hexadecimal byte in the packet |BR|
      |_| **byte2:**  second hexadecimal byte in the packet |BR|
      |_| **byte3:**  optional third hexadecimal byte in the packet |BR|
      |_| **byte4:**  optional fourth hexadecimal byte in the packet |BR|
      |_| **byte5:**  optional fifth hexadecimal byte in the packet |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| register for backwards compat (can not be removed because number of arguments is unknown) |BR| |BR|

  * - ``<P register hex1 hex2 [hex3 [hex4 [hex5]]]>``
    - **Write a DCC packet the MAIN track** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **register:** ignored |BR|
      |_| **byte1:**  first hexadecimal byte in the packet |BR|
      |_| **byte2:**  second hexadecimal byte in the packet |BR|
      |_| **byte3:**  optional third hexadecimal byte in the packet |BR|
      |_| **byte4:**  optional fourth hexadecimal byte in the packet |BR|
      |_| **byte5:**  optional fifth hexadecimal byte in the packet |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|
      |_| *Notes:* |BR|
      |_| register for backwards compat (can not be removed because number of arguments is unknown) |BR| |BR|


Other
=====

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<U cmd>``
    - **Is reserved for user commands (through user filter)** |BR| |BR|
      |_| *Parameters:* |BR|
      |_| **cmd:** user defined command |BR| |BR|
      |_| *Response:* |BR|
      |_| N/A |BR| |BR|

More Information
================

 **For a detailed command reference, see...**
  :doc:`Command Reference <command-reference>`
