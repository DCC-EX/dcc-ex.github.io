.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: EX-CommandStation Command Station diagnosing Issues Troubleshooting

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

********************************
Steps to Diagnose Basic Problems
********************************

|conductor| 

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

This page is intended to help you diagnose and fix the most common problems with the |EX-CS|.

Depending on how you have your EX-CommandStation configured, the steps to diagnose problems are different:

* `When Connected to a PC via USB`_
* `When Configured as an Access Point`_
* `When Configured in Station mode`_

----

EX-CommandStation Software fails to load
========================================

.. todo:: EX-CommandStation Software fails to load

----

When Connected to a PC via USB
==============================

**If you have connected your EX-CommandStation to a PC via USB (including using JMRI)**

.. list-table:: 
  :widths: 40 20 40
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No - Possible reasons
  * - 1. Is the light on the Arduino board on?
    - Go to Question 2.
    - (a) Software may not have loaded correctly. 
      (b) Possible dead Arduino board.
      
      In either case, try loading the EX-CommandStation software again.
  * - 2. Can you connect to it using EX-WebThrottle?
    - Go to Question 3.
    - (a)
  * - 3. When you select a loco and move the throttle, do the LEDs on the Motor Board light up?
    - Go to Question 4.
    - (a) Have you plugged in and turned on a 12-15v DC power supply into the motor board
      (b) Have you made sure the polarity of the power supply is correct.

|

When Configured as an Access Point
==================================

**If you have configured your EX-CommandStation as an Access Point (separate network)**


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
  * - 2. Can your phone see the WiFi network of the EX-CommandStation in the phone's available network list?
    - Go to Question 3
    - xx
  * - 3. Can your phone connect the WiFi network of the EX-CommandStation
    - Go to Question 4
    - xx
  * - 4. Can your throttle app connect the wiThrottle server of the EX-CommandStation |BR| |BR| |Engine Driver| should show you the wiThrottle server in the discovered servers list |BR| For |wiThrottle| you will need to type in the IP address and Port
    - Go to Question 5
    - xx
  * - 5. Can you turn the track power on?  |BR| Do the LEDs on the moto shield turn on?
    - Go to Question 6
    - (a) Have you plugged in and turned on a 12-15v DC power supply into the motor board
      (b) Have you made sure the polarity of the power supply is correct. |BR| OR |BR| 

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
    - Go to Question 3
    - You may be on a different network to the EX-CommandStation (e.g. 2.5gHz VS 5gHz connection to you home router.) Try entering the IP address and Port manually.  To 
