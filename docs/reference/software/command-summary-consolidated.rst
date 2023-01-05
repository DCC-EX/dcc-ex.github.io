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
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<onOff [MAIN | PROG | JOIN] >`` 
    - **<pX [MAIN\|PROG\|JOIN]>** |BR| 
      Where "X" is 1=on \| 0=off. MAIN, PROG and JOIN are returned when you invoke commands on just one track.
    - Turns power on and off to the MAIN and PROG tracks independently from each other. Also allows joining the MAIN and PROG tracks together |BR|
      **onOff** = 1=on 0=off
  * - ``<D RESET>``  
    - n/a
    - Re-boot the command Station

Loco (Cab) Commands
-------------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<t register cab speed 1|0>``  
    - ``<l cab register speedByte functionMap>`` |BR| |BR|
      Legacy Return: **Deprecated** |BR|
      ``<T register speed direction>`` |BR| 
      do not rely on this return
    - Set the speed and direction of a loco |BR| 
      **speed** - 0-127 |BR| 
      **direction** - 1=forward 0=reverse |BR| 
      Note: this starts a reminder process for any external updates to the loco's status.
  * - ``<t cab>``
    - ``<l cab register speedByte functionMap>`` |BR| Note: |BR|
      If the cab (loco) is not in the reminders table. The Command Station will not return a valid response until a speed is applied to the cab. In this case ``<l -1>`` will be returned.
    - Requests a deliberate update on the cab speed/functions in the same format as the cab broadcast.
  * -  ``<- [cab]>`` 
    - n/a
    - Remove one or all locos from reminders.
  * - ``<!>`` 
    - ``<l cab register speedByte functionMap>`` For each loco in the reminders list
    - Emergency Stop 
  * - ``<- [cab]>`` 
    - n/a
    - Remove one or all cabs from reminders.
  * - ``<F cab function 1|0>`` 
    - ``<l cab register speedByte functionMap>``
    - Turns loco decoder functions ON and OFF
  * - ``<JR>`` 
    - ``<jR id1 id2 id3 ...>``
    - Returns the defined roster entry IDs
  * - ``<JR id>`` 
    - ``<jR id "description" "function1/function2/function3/...">``
    - Returns the ID, description, and function map of the specified roster entry ID
  * - ``<JT>`` 
    - ``<jT id1 id2 id3 ...>``
    - Returns the defined turnout IDs
  * - ``<JT id>`` 
    - ``<jT id state "[description]">``
    - Returns the ID, state, and description of the specified turnout ID
  * - ``<JA>`` 
    - ``<jA id1 id2 id3 ...>``
    - Returns the defined automation and route IDs
  * - ``<JA id>`` 
    - ``<jA id type "[description]">``
    - Returns the ID, type (A=automation or R=route), and description of the specified automation/route ID
  * - ``<t cabid>`` 
    - ``<l cab register speedByte functionMap>``
    - Requests a deliberate update of cab speed/functions in the same format as the cab broadcast
  * - ``<f cab byte1 [byte2]]>`` 
    - **Deprecated**
    - legacy function. **Deprecated, please use <W cv value> instead**

System Information
------------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<s>`` 
    - ``<iDCCEX version / microprocessorType / MotorControllerType / buildNumber>`` |BR|
       ``<H id state>``
    - CommandStation Status
  * - ``<c>`` 
    - ``<c "CurrentMAIN" current C "Milli" "0" max_ma "1" trip_ma>``
    - Current on the MAIN Track |BR| 
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
    - 
    - Show number of supported cabs. Will return either ``<# 20>``, ``<# 30>``, or ``<# 50>``

Writing CVs - Program on the main
---------------------------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<M ignored hex1 hex2 [hex3 [hex4 [hex5]]]>`` 
    - 
    - Write a DCC packet the MAIN track
  * - ``<w cab cv value>`` 
    - 
    - Write CV on main track   
  * - ``<b cab cv bit value>`` 
    - 
    - Write CV bit on main track
  * - ``<W cv value callbacknum callbacksub>`` 
    - 
    - Write CV. **Deprecated, please use <W cv value> instead**
  * - ``<B cv bit value callbacknum callbacksub>`` 
    - 
    - Write bit to cv. **Deprecated, please use <W cv value> instead**  

Writing CVs - Programming track
-------------------------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<R>`` 
    - 
    - Read Loco address (programming track only)
  * - ``<W cab>`` 
    -
    - write cab address to loco on prog track 
  * - ``<W cv value >`` 
    -
    - write CV
  * - ``<B cv bit 0|1>`` 
    - 
    - Write bit to cv.
  * - ``<V cv value>`` 
    - 
    - Verify/Read of cv with guessed value
  * - ``<V cv bit 0|1>`` 
    - 
    - Verify/Read bit of cv with guessed value
  * - ``<P ignored hex1 hex2 [hex3 [hex4 [hex5]]]>`` 
    -
    - Writes a DCC packet to the PROG track

Writing CVs - Programming track - Tuning
----------------------------------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<D ACK LIMIT mA>`` 
    -
    - Override ACK processing mA pulse size
  * - ``<D ACK MIN uS>`` 
    - 
    - Override ACK processing minimum pulse width
  * - ``<D ACK MAX uS>`` 
    - 
    - Override ACK processing max pulse width
  * - ``<D ACK RETRY x>`` 
    -
    - Adjust ACK retries to number x (default is 2)
  * - ``<D PROGBOOST>``  
    - 
    - Override 250mA prog track limit while idle.

DCC Accessories
---------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<a linear_address 1|0>``
    -
    -
  * - ``<a addr subaddr 1|0>``
    -
    -

Turnouts/Points
---------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<T>`` 
    - 
    - List defined turnouts
  * - ``<T id 0|1|C|T>`` 
    - 
    - Throw (1 or T) or close(0 or C) a defined turnout 

Sensors
-------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<Q>`` 
    -
    - Lists Status of all sensors.
  * - ``<S>`` 
    - 
    - Lists definition all defined sensors. 

WiFi Control
------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<+command>`` 
    - 
    - Sends AT+ commands to the WiFi board (ESP8266, ESP32, etc.)
  * - ``<+X>`` 
    -
    - Force the Command Station into "WiFi Connected" mode


Configuring the EX-CommandStation
=================================

TBA
---

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<D SPEED28|SPEED128>`` 
    - 
    - Switch between 28 and 128 speed steps

Turnouts/Points - Configuration
-------------------------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<T id DCC address subaddress>`` 
    - 
    - Define DCC turnout
  * - ``<T id DCC linear_address>`` 
    - 
    - Define DCC turnout
  * - ``<T id SERVO vpin thrownPos closedPos profile>`` 
    - 
    - Define servo turnout
  * - ``<T id VPIN vpin>`` 
    - 
    - Define VPIN turnout
  * - ``<T id>`` 
    -
    - Delete turnout

Sensors - Configuration
-----------------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<S id pin 0|1>`` 
    - 
    - Creates a new sensor ID, with specified PIN and PULLUP
  * - ``<S id>``
    - 
    - Deletes definition of sensor ID  

Outputs
-------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<Z>`` 
    - 
    - Lists all defined output pins
  * - ``<Z id pin iflag>``
    - 
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
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<E>``
    - 
    - Store definitions to EEPROM
  * - ``<e>``
    - 
    - Erase ALL (turnouts, sensors, and outputs) from EEPROM 
  * - ``<D EEPROM>``
    - 
    - Diagnostic dump eeprom contents

Diagnostic traces
-----------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<D CABS>`` 
    -
    - Shows cab numbers and speed in reminder table
  * - ``<D RAM>``
    - 
    - Shows remaining RAM (Free Memory)
  * - ``<D ACK ON|OFF>``
    - 
    - Enables ACK diagnostics
  * - ``<D CMD ON|OFF>``
    - 
    - Enables Command Parser diagnostics
  * - ``<D ETHERNET ON|OFF>``
    - 
    - Enables Ethernet diagnostics
  * - ``<D LCN ON|OFF>``
    - 
    - Enables LCN interface diagnostics
  * - ``<D WIFI ON|OFF>``
    - 
    - Enables WiFi diagnostics
  * - ``<D WIT ON|OFF>``
    -
    - Enables WiThrottle diagnostics
  * - ``<D HAL SHOW>``
    -
    - Shows configured servo board and GPIO extender board config and used pins

I/O (HAL) Diagnostics
---------------------

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<D HAL SHOW>``
    -
    - List HAL devices and allocated VPINs
  * - ``<D SERVO vpin value [profile]>``
    -
    - Set servo position to `value` on pin `vpin`.
  * - ``<D ANOUT vpin value [param2]>``
    - 
    - Write `value` to analogue pin `vpin`, supplying `param2` to the driver.
  * - ``<D ANIN vpin>``
    - 
    - Read and display pin `vpin`'s analogue value.

Other
-----

.. list-table:: 
  :widths: 20 30 50
  :header-rows: 1
  :width: 100%
  :class: command-table

  * - Command
    - Response
    - Description
  * -  ``<U ...>`` 
    -
    - Is reserved for user commands (through user filter)

More Information
================

 **For a detailed command reference, see...**
  :doc:`Command Reference <command-reference>`
