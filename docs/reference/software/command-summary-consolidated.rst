.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-REF-LOGO|

***********************************
DCC-EX Consolidated Command Summary
***********************************

|engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 1
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
- ``direction`` - 1=forward 0=reverse
- ``speedByte`` - 0=stopped 1-127=reverse 128-256=forward
- ``function`` - function number related to a specific DCC decoder/ loco (e.g. 0-27)
- ``functionMap`` - individual bits of the returned number represent the state of the specific functions
- ``slot`` - redundant parameter.  This needs to be included but is ignored by the EX-CommandStation
- ``register`` - redundant parameter.  This needs to be included but is ignored by the EX-CommandStation

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
  * - ``<onOff [MAIN | PROG | JOIN] >`` 
    - **Track Power** |BR| |BR|
      Response: ``<pX [MAIN\|PROG\|JOIN]>`` |BR|
      Where "X" is 1=on \| 0=off. MAIN, PROG and JOIN are returned when you invoke commands on just one track. |BR|
      Turns power on and off to the MAIN and PROG tracks independently from each other. Also allows joining the MAIN and PROG tracks together |BR| |BR|
      **onOff**: 1=on 0=off
  * - ``<D RESET>``
    - **Re-boot the command Station** |BR|
      Response: *n/a* 

Loco (Cab) Commands
-------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<t register cab speed 1|0>``  
    - **Set the speed and direction of a loco** |BR| |BR|
      Response: ``<l cab register speedByte functionMap>`` |BR|
      **speed** - 0-127 |BR| 
      **direction** - 1=forward 0=reverse |BR| 
      Note: this starts a reminder process for any external updates to the loco's status. |BR| |BR|
      Legacy response: **Deprecated** |BR|
      ``<T register speed direction>`` - do not rely on this response
  * - ``<t cab>``
    - Requests a deliberate update on the cab speed/functions in the same format as the cab broadcast.|BR|
      Response: ``<l cab register speedByte functionMap>`` |BR| |BR| 
      Note: |BR|
      If the cab (loco) is not in the reminders table. The Command Station will not return a valid response until a speed is applied to the cab. In this case ``<l -1>`` will be returned.
  * -  ``<- [cab]>`` 
    - **Remove one or all locos from reminders** |BR| |BR|
      Response: *n/a* 
  * - ``<!>`` 
    - **Emergency Stop** |BR| |BR|
      Response: ``<l cab register speedByte functionMap>`` (For each loco in the reminders list.)
  * - ``<F cab function 1|0>`` 
    - **Turns loco decoder functions ON and OFF** |BR| |BR|
      Response ``<l cab register speedByte functionMap>``
  * - ``<JR>`` 
    - **Request the list defined Roster Entry IDs** |BR| |BR|
      Response: ``<jR id1 id2 id3 ...>`` |BR|
      Returns the list of defined roster entry IDs
  * - ``<JR id>`` 
    - **Request details of a specific Roster Entry** |BR| |BR|
      Response: ``<jR id "description" "function1/function2/function3/...">`` |BR|
      Returns the ID, description, and function map of the specified roster entry ID
  * - ``<JT>`` 
    - **Request the list of Turnout/Point IDs** |BR| |BR|
      Response: ``<jT id1 id2 id3 ...>`` |BR|
      Returns the list of defined turnout/Point IDs
  * - ``<JT id>`` 
    - **Request details of a specific Turnout/Point** |BR| |BR|
      Response: ``<jT id state "[description]">`` |BR|
      Returns the ID, state, and description of the specified Turnout/Point ID
  * - ``<JA>`` 
    - **Request the list of Automation and Route IDs** |BR| |BR|
      Response: ``<jA id1 id2 id3 ...>`` |BR|
      Returns the defined automation and route IDs
  * - ``<JA id>`` 
    - **Request details of a specific Automation or Route** |BR| |BR|
      Response: ``<jA id type "[description]">`` |BR|
      Returns the ID, type, and description of the specified automation/route ID |BR|
      **type**: 'A'=automation 'R'=route
  * - ``<t cabid>`` 
    - **Request a deliberate update of cab** |BR| |BR|
      Response: ``<l cab register speedByte functionMap>`` |BR|
      Returns an update of cab speed, directions and functions in the same format as the cab broadcast
  * - ``<f cab byte1 [byte2]]>`` 
    - **Deprecated** |BR|
      legacy function. **Deprecated, please use <W cv value> instead**


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
    - **Request CommandStation Status** |BR| |BR|
      Response: ``<iDCCEX version / microprocessorType / MotorControllerType / buildNumber>`` |BR|
      Response (for each): ``<H id state>``
  * - ``<c>`` 
    - **Request Current on the MAIN Track** |BR| |BR|
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
    - **Show number of supported cabs** |BR| |BR|
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
    - **Write a DCC packet the MAIN track** |BR| |BR|
  * - ``<w cab cv value>`` 
    - Write CV on main track   
  * - ``<b cab cv bit value>`` 
    - Write CV bit on main track
  * - ``<W cv value callbacknum callbacksub>`` 
    - Write CV. **Deprecated, please use <W cv value> instead**
  * - ``<B cv bit value callbacknum callbacksub>`` 
    - Write bit to cv. **Deprecated, please use <W cv value> instead**  

Writing CVs - Programming track
-------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<R>`` 
    - Read Loco address (programming track only)
  * - ``<W cab>`` 
    - write cab address to loco on prog track 
  * - ``<W cv value >`` 
    - write CV
  * - ``<B cv bit 0|1>`` 
    - Write bit to cv.
  * - ``<V cv value>`` 
    - Verify/Read of cv with guessed value
  * - ``<V cv bit 0|1>`` 
    - Verify/Read bit of cv with guessed value
  * - ``<P ignored hex1 hex2 [hex3 [hex4 [hex5]]]>`` 
    - Writes a DCC packet to the PROG track

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
    - Override ACK processing mA pulse size
  * - ``<D ACK MIN uS>`` 
    - Override ACK processing minimum pulse width
  * - ``<D ACK MAX uS>`` 
    - Override ACK processing max pulse width
  * - ``<D ACK RETRY x>`` 
    - Adjust ACK retries to number x (default is 2)
  * - ``<D PROGBOOST>``  
    - Override 250mA prog track limit while idle.

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
    -
  * - ``<a addr subaddr 1|0>``
    -

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
    - List defined turnouts
  * - ``<T id 0|1|C|T>`` 
    - Throw (1 or T) or close(0 or C) a defined turnout 

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
    - Lists Status of all sensors.
  * - ``<S>`` 
    - Lists definition all defined sensors. 

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
    - Sends AT+ commands to the WiFi board (ESP8266, ESP32, etc.)
  * - ``<+X>`` 
    - Force the Command Station into "WiFi Connected" mode


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
    - Switch between 28 and 128 speed steps

Turnouts/Points - Configuration
-------------------------------

.. list-table:: 
  :widths: 25 75
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Description / Response 
  * - ``<T id DCC address subaddress>`` 
    - Define DCC turnout
  * - ``<T id DCC linear_address>`` 
    - Define DCC turnout
  * - ``<T id SERVO vpin thrownPos closedPos profile>`` 
    - Define servo turnout
  * - ``<T id VPIN vpin>`` 
    - Define VPIN turnout
  * - ``<T id>`` 
    - Delete turnout

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
    - Creates a new sensor ID, with specified PIN and PULLUP
  * - ``<S id>``
    - Deletes definition of sensor ID  

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
    - Lists all defined output pins
  * - ``<Z id pin iflag>``
    - Creates a new output ID, with specified PIN and IFLAG values.  


.. code-block::

  IFLAG, bit 0: 0 = forward operation (ACTIVE=HIGH / INACTIVE=LOW)
                1 = inverted operation (ACTIVE=LOW / INACTIVE=HIGH)

  IFLAG, bit 1: 0 = state of pin restored on power-up to either ACTIVE or INACTIVE 
                    depending on state before power-down. 
                1 = state of pin set on power-up, or when first created,
                    to either ACTIVE of INACTIVE depending on IFLAG, bit 2

  IFLAG, bit 2: 0 = state of pin set to INACTIVE upon power-up or when first created
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
    - Store definitions to EEPROM
  * - ``<e>``
    - Erase ALL (turnouts, sensors, and outputs) from EEPROM 
  * - ``<D EEPROM>``
    - Diagnostic dump eeprom contents

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
    - Shows cab numbers and speed in reminder table
  * - ``<D RAM>``
    - Shows remaining RAM (Free Memory)
  * - ``<D ACK ON|OFF>``
    - Enables ACK diagnostics
  * - ``<D CMD ON|OFF>``
    - Enables Command Parser diagnostics
  * - ``<D ETHERNET ON|OFF>``
    - Enables Ethernet diagnostics
  * - ``<D LCN ON|OFF>``
    - Enables LCN interface diagnostics
  * - ``<D WIFI ON|OFF>``
    - Enables WiFi diagnostics
  * - ``<D WIT ON|OFF>``
    - Enables WiThrottle diagnostics
  * - ``<D HAL SHOW>``
    - Shows configured servo board and GPIO extender board config and used pins

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
    - List HAL devices and allocated VPINs
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
