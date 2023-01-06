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
- Square brackets ``[]`` - Parameters within square brackets ``[]`` are optional and may be ommitted, and if specifying these parameters, do not include the square brackets themselves
- \| - Use of the \| character means you need to provide one of the provided options only, for example ``<0|1 MAIN|PROG|JOIN>`` becomes either ``<0 MAIN>`` or ``<1 MAIN>``
- ``0|1`` DIRECTION: 1=forward, 0=reverse.

*Commonly used Parameters (Arguments)*

- ``cab`` - DCC Address. i.e. a Loco. (eg. 3-9999)
- ``speed`` - 0-127
- ``dir`` ``direction`` - 1=forward 0=reverse
- ``speedByte`` - 0=stopped 1-127=reverse 128-256=forward
- ``funct`` ``function`` - function number related to a specific DCC decoder/ loco (e.g. 0-27)
- ``functMap`` ``functionMap`` - individual bits of the returned number represent the state of the specific functions
- ``slot`` - redundant parameter.  This needs to be included but is ignored by the EX-CommandStation
- ``reg`` ``register`` - redundant parameter.  This needs to be included but is ignored by the EX-CommandStation
- ``desc`` ``description`` - 
- ``byte`` - 
- ``track`` -

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
  * - ``<onOff [track]>`` |BR| |BR| ``<0|1 [MAIN|PROG|JOIN] >`` 
    - **Track Power** |BR|
      Turns power on and off to the MAIN and PROG tracks together or independently. Also allows joining the MAIN and PROG tracks together. |BR|
      **onOff**: 1=on 0=off |BR|
      **track**: <blank>= Both Main and Programming Tracks 'MAIN'= Main track  'PROG'=Programming Track 'JOIN'=Join the Main and Programming tracks temporarily |BR| |_| |BR|
      Response: ``<pX [MAIN|PROG|JOIN]>`` |BR|
      Where "X" is 1=on \| 0=off. MAIN, PROG and JOIN are returned when you invoke commands on just one track. |BR|
  * - ``<D RESET>``
    - **Re-boot the command Station** |BR| |_| |BR|
      Response: *n/a* 

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
    - **Set the speed and direction of a Cab (Loco)** |BR| |_| |BR|
      Response: ``<l cab reg speedByte functMap>`` |BR|
      **speed** - 0-127 |BR| 
      **dir** - 1=forward 0=reverse |BR| 
      Note: this starts a reminder process for any external updates to the cab's (loco's) status. |BR| |_| |BR|
      Legacy response: **Deprecated** |BR|
      ``<T reg speed dir>`` - do not rely on this response
  * - ``<t cab>``
    - Requests a deliberate update on the cab speed/functions in the same format as the cab (loco) broadcast. |BR| |_| |BR|
      Response: ``<l cab reg speedByte functMap>`` |BR|
      Note: |BR|
      If the cab (loco) is not in the reminders table. The Command Station will not return a valid response until a speed is applied to the cab. In this case ``<l -1>`` will be returned.
  * -  ``<- [cab]>`` 
    - **Remove one or all locos from reminders** |BR|
      **cab** - <blank>= all locos  No.= Cab (loco) to forget |BR| |_| |BR|
      Response: *n/a* 
  * - ``<!>`` 
    - **Emergency Stop** |BR| |BR|
      Response: ``<l cab reg speedByte functMap>`` (For each loco in the reminders list.)
  * - ``<F cab funct 1|0>`` 
    - **Turns loco decoder functions ON and OFF** |BR| 
      **funct** - 0-28 (F29-F68 (Support for the RCN-212 Functions) |BR| 
      NOTES: |BR| 
      - Setting requests are transmitted directly to mobile engine decoder. |BR|
      - Current state of engine functions (as known by commands issued since power on) is stored by the CommandStation
      - All functions within a group get set all at once per NMRA DCC standards. |BR| |_| |BR|
      Response ``<l cab reg speedByte functMap>``
  * - ``<JR>`` 
    - **Request the list defined Roster Entry IDs** |BR| |_| |BR|
      Response (roster exists): ``<jR id1 id2 id3 ...>`` |BR|
      Response (no roster exists): ``<jR>`` |BR|
      Returns the list of defined roster entry IDs
  * - ``<JR id>`` 
    - **Request details of a specific Roster Entry** |BR| |_| |BR|
      Response (id is in Roster): ``<jR id "desc" "funct1/funct2/funct3/...">`` |BR|
      Response (id is not in Roster): ``<jR id "" "">`` |BR|
      Returns the ID, description, and function map of the specified roster entry ID
  * - ``<JT>`` 
    - **Request the list of Turnout/Point IDs** |BR| |_| |BR|
      Response (has defined Turnouts/Points): ``<jT id1 id2 id3 ...>`` |BR|
      Response (no defined Turnouts/Points): ``<jT>`` |BR|
      Returns the list of defined turnout/Point IDs
  * - ``<JT id>`` 
    - **Request details of a specific Turnout/Point** |BR| |_| |BR|
      Response (id is defined): ``<jT id state "[desc]">`` |BR|
      Response (id not defined): ``<jT id X>`` |BR|
      Returns the ID, state, and description of the specified Turnout/Point ID
  * - ``<JA>`` 
    - **Request the list of Automation and Route IDs** |BR| |_| |BR|
      Response (has defined Automation/Routes): ``<jA id1 id2 id3 ...>`` |BR|
      Response (no defined Automation/Routes): ``<jA>`` |BR|
      Returns the defined automation and route IDs
  * - ``<JA id>`` 
    - **Request details of a specific Automation or Route** |BR| |_| |BR|
      Response  (id is defined): ``<jA id type "[desc]">`` |BR|
      Response  (id not defined): ``<jA id X>`` |BR|
      Returns the ID, type, and description of the specified automation/route ID |BR|
      **type**: 'A'=automation 'R'=route
  * - ``<t cabid>`` 
    - **Request a deliberate update of cab** |BR| |_| |BR|
      Response: ``<l cab reg speedByte functMap>`` |BR|
      Returns an update of cab speed, directions and functions in the same format as the cab broadcast
  * - ``<f cab byte1 [byte2]]>`` 
    - legacy function. |BR| 
      **Deprecated, please use <W cv value> instead**


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
    - **Request CommandStation Status** |BR| |_| |BR|
      Response (single): ``<iDCCEX version / microprocessorType / MotorControllerType / buildNumber>`` |BR|
      Response (for each defined Turnout/Point): ``<H id state>``
  * - ``<c>`` 
    - **Request Current on the MAIN Track** |BR| |_| |BR|
      Response: ``<c "CurrentMAIN" current C "Milli" "0" max_ma "1" trip_ma>`` |BR|
      **c** - the current response indicator |BR| 
      **CurrentMAIN** - Static text for software like JMRI |BR| 
      **current** - Current in MilliAmps |BR| 
      **C** - Designator to signify this is a current meter (V would be for voltage) |BR| 
      **Milli** - Unit of measure for external software with a meter like JMRI (Milli, Kilo, etc.) |BR| 
      **0** - numbered parameter for external software (1,2,3, etc.) |BR| 
      **max_ma** - The maximum current handling of the motor controller in MilliAmps |BR| 
      **1** - number parameter for external software (we use 2 parameters here, 0 and 1) |BR| 
      **trip_ma** - The overcurrent limit that will trip the software circuit breaker in mA 
  * - ``<#>`` 
    - **Show number of supported cabs** |BR| |_| |BR|
      Response: Will return either ``<# 20>``, ``<# 30>``, or ``<# 50>``


Writing CVs - Program on the main
---------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<M ignored hex1 hex2 [hex3 [hex4 [hex5]]]>`` 
    - **Write a DCC packet the MAIN track** |BR| |_| |BR|
      Response: 
  * - ``<w cab cv value>`` 
    - **Write CV on main track** |BR| |_| |BR|
      Response: 
  * - ``<b cab cv bit value>`` 
    - **Write CV bit on main track** |BR| |_| |BR|
      Response: 
  * - ``<W cv value callbacknum callbacksub>`` 
    - Write CV |BR| **Deprecated, please use <W cv value> instead**
  * - ``<B cv bit value callbacknum callbacksub>`` 
    - Write bit to CV |BR| **Deprecated, please use <W cv value> instead**  

Reading/Writing CVs - Programming track
---------------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<R>`` 
    - **Read DCC decoder address** |BR| |_| |BR|
      Response (successful): ``<r cab>``|BR|
      Response (fail): ``<r -1>`` 
  * - ``<W cab>`` 
    - **Write DCC address to cab (loco)** |BR| |_| |BR|
      Response (successful): ``<w cab>`` |BR|
      Response (fail):  ``<w -1>``
  * - ``<W cv value >`` 
    - **Write CV** |BR| |_| |BR|
      Response (successful): ``<r cv value>`` |BR|
      Response (fail):  ``<r cv -1>``
  * - ``<B cv bit 0|1>`` 
    - **Write bit to CV** |BR| |_| |BR|
      Response (successful): |BR|
      Response (fail):  
  * - ``<R cv>`` 
    - **Read CV** |BR| |_| |BR|
      Response (successful): ``<r cv value>`` |BR|
      Response (fail):  ``<r cv -1>``
  * - ``<V cv guessedValue>`` 
    - **Verify/Read of CV with guessed value** |BR| |_| |BR|
      Response (successful): ``<v cv actualValue>`` |BR|
      Response (fail): ``<v id -1>``  
  * - ``<V cv bit 0|1>`` 
    - **Verify/Read bit of CV with guessed value** |BR| |_| |BR|
      Response (successful): |BR|
      Response (fail):  
  * - ``<P ignored hex1 hex2 [hex3 [hex4 [hex5]]]>`` 
    - **Writes a DCC packet to the PROG track** |BR| |_| |BR|
      Response (successful): |BR|
      Response (fail):  

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
    - **8Override ACK processing mA pulse size** |BR| |BR|
  * - ``<D ACK MIN uS>`` 
    - **Override ACK processing minimum pulse width** |BR| |BR|
  * - ``<D ACK MAX uS>`` 
    - **Override ACK processing max pulse width** |BR| |BR|
  * - ``<D ACK RETRY x>`` 
    - **Adjust ACK retries to number x (default is 2)** |BR| |BR|
  * - ``<D PROGBOOST>``  
    - **Override 250mA prog track limit while idle** |BR| |BR|

DCC Accessories
---------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<a linear_address 1|0>``
    - **???** |BR| |BR|
  * - ``<a addr subaddr 1|0>``
    - **???** |BR| |BR|

Turnouts/Points
---------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<T>`` 
    - **List defined turnouts** |BR| |BR|
  * - ``<T id 0|1|C|T>`` 
    - **Throw (1 or T) or close(0 or C) a defined turnout** |BR| |BR|

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
  * - ``<S>`` 
    - **Lists definition all defined sensors** |BR| |BR|

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
    - **Sends AT+ commands to the WiFi board (ESP8266, ESP32, etc.)** |BR| |BR|
  * - ``<+X>`` 
    - **Force the Command Station into "WiFi Connected" mode** |BR| |BR|


Configuring the EX-CommandStation
=================================

TBA
---

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<D SPEED28|SPEED128>`` 
    - **Switch between 28 and 128 speed steps** |BR| |BR|

Turnouts/Points - Configuration
-------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<T id DCC addr subaddr>`` 
    - **Define DCC turnout** |BR| |BR|
  * - ``<T id DCC linear_addr>`` 
    - **Define DCC turnout** |BR| |BR|
  * - ``<T id SERVO vpin thrownPos closedPos profile>`` 
    - **Define servo turnout** |BR| |BR|
  * - ``<T id VPIN vpin>`` 
    - **Define VPIN turnout** |BR| |BR|
  * - ``<T id>`` 
    - **Delete turnout** |BR| |BR|

Sensors - Configuration
-----------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<S id pin 0|1>`` 
    - **Creates a new sensor ID, with specified PIN and PULLUP** |BR| |BR|
  * - ``<S id>``
    - **Deletes definition of sensor ID** |BR| |BR|

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
    - **Lists all defined output pins** |BR| |BR|
  * - ``<Z id pin iflag>``
    - **Creates a new output ID, with specified PIN and IFLAG values** |BR| |BR|
      **IFLAG, bit 0**: |BR|
      0 = forward operation (ACTIVE=HIGH / INACTIVE=LOW) |BR|
      1 = inverted operation (ACTIVE=LOW / INACTIVE=HIGH) |BR| |BR|
      **IFLAG, bit 1**: |BR|
      0 = state of pin restored on power-up to either ACTIVE or INACTIVE depending on state before power-down.  |BR|
      1 = state of pin set on power-up, or when first created, to either ACTIVE of INACTIVE depending on IFLAG, bit 2 |BR| |BR|
      **IFLAG, bit 2**: 
      0 = state of pin set to INACTIVE upon power-up or when first created |BR|
      1 = state of pin set to ACTIVE upon power-up or when first created

..

 ``<Z id 0|1>`` : Sets output ID to either INACTIVE or ACTIVE state  

 ``<Z id>`` : Deletes definition of output ID  

EEPROM management
-----------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<E>``
    - **Store definitions to EEPROM** |BR| |BR|
  * - ``<e>``
    - **Erase ALL (turnouts, sensors, and outputs) from EEPROM** |BR| |BR|
  * - ``<D EEPROM>``
    - **Diagnostic dump eeprom contents** |BR| |BR|

Diagnostic traces
-----------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<D CABS>`` 
    - **Shows cab numbers and speed in reminder table** |BR| |BR|
  * - ``<D RAM>``
    - **Shows remaining RAM (Free Memory)** |BR| |BR|
  * - ``<D ACK ON|OFF>``
    - **Enables ACK diagnostics** |BR| |BR|
  * - ``<D CMD ON|OFF>``
    - **Enables Command Parser diagnostics** |BR| |BR|
  * - ``<D ETHERNET ON|OFF>``
    - **Enables Ethernet diagnostics** |BR| |BR|
  * - ``<D LCN ON|OFF>``
    - **Enables LCN interface diagnostics** |BR| |BR|
  * - ``<D WIFI ON|OFF>``
    - **Enables WiFi diagnostics** |BR| |BR|
  * - ``<D WIT ON|OFF>``
    - **Enables WiThrottle diagnostics** |BR| |BR|
  * - ``<D HAL SHOW>``
    - **Shows configured servo board and GPIO extender board config and used pins** |BR| |BR|

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
  * - ``<D SERVO vpin value [profile]>``
    - Set servo position to `value` on pin `vpin`.
  * - ``<D ANOUT vpin value [param2]>``
    - Write `value` to analogue pin `vpin`, supplying `param2` to the driver.
  * - ``<D ANIN vpin>``
    - Read and display pin `vpin`'s analogue value.

Other
-----

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * -  ``<U ...>`` 
    - Is reserved for user commands (through user filter)

More Information
================

 **For a detailed command reference, see...**
  :doc:`Command Reference <command-reference>`
