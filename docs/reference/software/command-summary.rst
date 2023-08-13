:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-REF-LOGO|

*****************************
DCC-EX Native Command Summary
*****************************

|engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 1
    :local:

**This is a summary, for a detailed command, see...**
  :doc:`Command Reference <command-reference>`

Conventions used on this page
=============================

- "<" and ">" - All DCC-EX API commands are surrounded by these characters to indicate the beginning and end, these must always be included
- First letter or number - These are called OPCODES, are case sensitive, and must be specified as directed, eg. 1, c, or -
- CAPITALISED words - These are parameters referred to as keywords, and should be specified as directed, eg. MAIN (note these are not case sensitive, however capitalising makes them easier to distinguish from other parameters)
- lowercase words - These are parameters that must be provided or are returned, with multiple parameters separated by a space " ", eg. cabid
- Square brackets [] - Parameters within square brackets [] are optional and may be ommitted, and if specifying these parameters, do not include the square brackets themselves
- \| - Use of the \| character means you need to provide one of the provided options only, for example ``<0|1 MAIN|PROG|JOIN>`` becomes either ``<0 MAIN>`` or ``<1 MAIN>``

Power management
=================

 ``<0 [MAIN | PROG] >`` Power Off  
 
 ``<1 [MAIN | PROG | JOIN] >`` Power On  
 
 ``<c>`` Current on the MAIN Track

 ``<s>`` CommandStation Status

 ``<D RESET>``  Re-boot the command Station

Cab functions
==============

 ``<!>`` EMERGENCY STOP 
 
 ``<t [ignored] cab speed 1|0>``  Throttle speed<127 direction 1=forward
 
 ``<- [cab]>`` Remove one or all cabs from reminders.
 
 ``<F cab function 1|0>`` command turns engine decoder functions ON and OFF
 
 ``<f cab byte1 [byte2]]>`` legacy functions, see command reference.
 
 ``<#>`` Show number of supported cabs. Will return either ``<# 20>``, ``<# 30>``, or ``<# 50>``
 
 ``<D SPEED28|SPEED128>`` Switch between 28 and 128 speed steps

 ``<M ignored hex1 hex2 [hex3 [hex4 [hex5]]]>`` Write a DCC packet the MAIN track

 ``<w cab cv value>`` Write CV on main track   

 ``<b cab cv bit value>`` Write CV bit on main track

Programming track
==================

 ``<R>`` Read Loco address (programming track only)

 ``<W cab>`` write cab address to loco on prog track 

 ``<W  cv value >``

 ``<W  cv value callbacknum callbacksub>`` **Deprecated, please use <W cv value> instead**

 ``<B cv bit 0|1>`` Write bit to cv.

 ``<B cv bit value callbacknum callbacksub>`` legacy version  

 ``<R cv>`` Read CV BYTE (pending implementation)

 ``<R cv callbacknum callbacksub>`` Read CV BYTE **Deprecated, please use <V cv value> instead**

 ``<V cv value>`` Verify/Read of cv with guessed value

 ``<V cv bit 0|1>`` Verify/Read bit of cv with guessed value

 ``<P ignored hex1 hex2 [hex3 [hex4 [hex5]]]>`` Writes a DCC packet to the PROG track

DCC Accessories
================

 ``<a linear_address 1|0>``

 ``<a addr subaddr 1|0>``

Turnouts
=========

 ``<T id DCC address subaddress>`` Define DCC turnout

 ``<T id DCC linear_address>`` Define DCC turnout

 ``<T id SERVO vpin thrownPos closedPos profile>`` Define servo turnout

 ``<T id VPIN vpin>`` Define VPIN turnout

 ``<T id>`` Delete turnout

 ``<T>`` List defined turnouts

 ``<T id 0|1|C|T>`` Throw (1 or T) or close(0 or C) a defined turnout 
 
Sensors
========
 
 ``<Q>`` Lists Status of all sensors.

 ``<S>`` Lists definition all defined sensors. 

 ``<S id pin 0|1>`` : Creates a new sensor ID, with specified PIN and PULLUP

 ``<S id>`` : Deletes definition of sensor ID  

Outputs
========
 
 ``<Z>`` Lists all defined output pins

 ``<Z id pin iflag>`` : Creates a new output ID, with specified PIN and IFLAG values.  

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
==================
 ``<E>`` Store definitions to EEPROM
 
 ``<e>`` Erase ALL (turnouts, sensors, and outputs) from EEPROM 
 
 ``<D EEPROM>`` Diagnostic dump eeprom contents

WiFi Control
=============
 ``<+command>`` Sends AT+ commands to the WiFi board (ESP8266, ESP32, etc.)

 ``<+X>`` Force the Command Station into "WiFi Connected" mode

Throttle commands for developers
================================

Refer to :doc:`/throttles/tech-reference` for full details on these commands.

``<JT>`` returns the defined turnout IDs

``<JT id>`` returns the ID, state, and description of the specified turnout ID

``<JA>`` Returns the defined automation and route IDs

``<JA id>`` Returns the ID, type (A=automation or R=route), and description of the specified automation/route ID

``<JR>`` Returns the defined roster entry IDs

``<JR id>`` Returns the ID, description, and function map of the specified roster entry ID

``<t cabid>`` Requests a deliberate update of cab speed/functions in the same format as the cab broadcast

Diagnostic traces
==================

 ``<D CABS>`` Shows cab numbers and speed in reminder table

 ``<D RAM>`` Shows remaining RAM (Free Memory)

 ``<D ACK ON|OFF>`` Enables ACK diagnostics

  ``<D CMD ON|OFF>`` Enables Command Parser diagnostics

 ``<D ETHERNET ON|OFF>`` Enables Ethernet diagnostics

 ``<D LCN ON|OFF>`` Enables LCN interface diagnostics

 ``<D WIFI ON|OFF>`` Enables WiFi diagnostics

 ``<D WIT ON|OFF>`` Enables WiThrottle diagnostics

 ``<D HAL SHOW>`` Shows configured servo board and GPIO extender board config and used pins

Tuning
=======

 ``<D ACK LIMIT mA>`` Override ACK processing mA pulse size
 
 ``<D ACK MIN uS>`` Override ACK processing minimum pulse width
 
 ``<D ACK MAX uS>`` Override ACK processing max pulse width

 ``<D ACK RETRY x>`` Adjust ACK retries to number x (default is 2)

 ``<D PROGBOOST>``  Override 250mA prog track limit while idle.

I/O (HAL) Diagnostics
======================

 ``<D HAL SHOW>`` List HAL devices and allocated VPINs

 ``<D SERVO vpin value [profile]>`` Set servo position to `value` on pin `vpin`.

 ``<D ANOUT vpin value [param2]>``  Write `value` to analogue pin `vpin`, supplying `param2` to the driver.

 ``<D ANIN vpin>``  Read and display pin `vpin`'s analogue value.

Other
======

 ``<U ...>`` Is reserved for user commands (through user filter)

 **For a detailed command reference, see...**
  :doc:`Command Reference <command-reference>`
