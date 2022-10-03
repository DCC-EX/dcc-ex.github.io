.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: EX-CommandStation Command Station diagnosing Issues Troubleshooting

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

*************************
Diagnosing Basic Problems
*************************

|conductor| 

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

This page is intended to help you diagnose and fix some of the most common problems with the |EX-CS|.  If you have a more specific issue see the :doc:`ex-cs-troubleshooting` page.

Depending on how you have your EX-CommandStation configured, the steps to diagnose problems are different:

* `When Connected to a PC via USB`_
* `When Configured as an Access Point`_
* `When Configured in Station mode`_

----

EX-CommandStation Software fails to load
========================================

.. todo:: Diagnosing - EX-CommandStation Software fails to load

Either using the |EX-I| to the Arduino IDE.

.. list-table:: 
  :widths: 40 20 40
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No - Possible reasons
  * - 1. Have you selected the correct COM port?
    - Go to Question 2.
    - ToDo
  * - 2. Have you selected the correct Arduino board type?
    - Go to Question 3.
    - ToDo
  * - 3. ToDo?
    - ToDo.
    - ToDo

----

When Connected to a PC via USB
==============================

**If you have connected your EX-CommandStation to a PC via USB** (including for using JMRI).

Initial Check
-------------

.. list-table:: 
  :widths: 40 20 40
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No - Possible reasons
  * - 1. Is the LED on the Arduino board on?
    - Go to Question 2.
    - (a) Software may not have loaded correctly. 
      (b) Possible dead Arduino board.
      
      In either case, try loading the EX-CommandStation software again.
  * - 2. Can you connect to it using EX-WebThrottle?
    - Go to Question 3.
    - (a) EX-CommandStation not connected to PC via USB.
      (b) Software may not have loaded correctly. 
  * - 3. When you select a loco and move the throttle, do the LEDs on the Motor Board light up?
    - TBA
    - (a) Have you plugged in and turned on a 12-15v DC power supply into the motor board
      (b) Have you made sure the polarity of the power supply is correct.

|

Using JMRI
----------

.. todo:: Diagnosing - Using JMRI

.. list-table:: 
  :widths: 40 20 40
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No - Possible reasons
  * - 1. Have you selected 'DCC++' as the System Manufacturer and 'DCC++ Serial Port' as the System connection in the preferences?
    - Go to Question 2.
    - ToDo
  * - 2. Have you selected the correct COM port?
    - Go to Question 3.
    - ToDo
  * - 3. Can you turn the track power on?  |BR| Do the LEDs on the motor shield turn on?
    - Go to Question 4.
    - (a) Have you plugged in and turned on a 12-15v DC power supply into the motor board
      (b) Have you made sure the polarity of the power supply is correct. 
  * - 4. ToDo
    - ToDo
    - (a) ToDo

|

When Configured as an Access Point
==================================

**If you have configured your EX-CommandStation as an Access Point** (separate network)


.. list-table:: 
  :widths: 40 20 40
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No - Possible reasons
  * - 1. Is the LED on the Arduino board on?
    - Go to Question 2.
    - (a) You have not connected a 7-9v DC power supply to Arduino Board. |BR| *or* |BR| 
      (b) You have not connected a USB cable connected to a power supply, to Arduino Board. 
      (c) Software may not have loaded correctly.
      (d) Possible dead Arduino board. 

      For c & d, try loading the EX-CommandStation software again.
  * - 2. Can your phone see the WiFi network of the EX-CommandStation in the phone's available network list?
    - Go to Question 3
    - (a) WifI shield is connected incorrectly to the CommandStation - The Rx pin of the WiFi shield must connect to the Tx pin on the CommandStation, and Tx to the Rx pin
      (b) ToDo
  * - 3. Can your phone connect the WiFi network of the EX-CommandStation
    - Go to Question 4
    - (a) ToDo
      (b) ToDo
  * - 4. Can your throttle app connect the wiThrottle server of the EX-CommandStation |BR| |BR| |Engine Driver| should show you the wiThrottle server in the discovered servers list |BR| For |wiThrottle| you will need to type in the IP address and Port
    - Go to Question 5
    - (a) ToDo
      (b) ToDo
  * - 5. Can you turn the track power on?  |BR| Do the LEDs on the motor shield turn on?
    - ToDo
    - (a) Have you plugged in and turned on a 12-15v DC power supply into the motor board
      (b) Have you made sure the polarity of the power supply is correct. 

|

When Configured in Station mode
===============================

**If you have configured your EX-CommandStation in Station mode (connected to your home WiFi network)**


.. list-table:: 
  :widths: 40 20 40
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No - Possible reasons
  * - 1. Is the LED on the Arduino board on?
    - Go to Question 2.
    - (a) You have not connected a 7-9v DC power supply to Arduino Board
      (b) You have not connected a USB cable connected to a power supply, to Arduino Board
      (c) Software may not have loaded correctly.
      (d) Possible dead Arduino board.
      
      For c & d, try loading the EX-CommandStation software again.
  * - 2. Can your throttle app connect to the wiThrottle server of the EX-CommandStation |BR| |BR| |Engine Driver| should show you the wiThrottle server in the discovered servers list |BR| For |wiThrottle| It should connect automatically.
    - ToDo
    - You may be on a different network to the EX-CommandStation (e.g. 2.5gHz VS 5gHz connection to you home router.) Try entering the IP address and Port manually.  To 
