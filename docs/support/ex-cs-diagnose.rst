.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: EX-CommandStation Command Station diagnosing Issues Troubleshooting

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

********************************
Steps to Diagnose basic Problems
********************************

|conductor| 

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

Depending on how you have your |EX-CS| configure, the steps to diagnose problems are different:

* `When Connected to a PC via USB`_
* `When Configured as an Access Point`_
* `When Configured in Station mode`_

|

When Connected to a PC via USB
==============================

**If you have connected your EX-CommandStation to a PC via USB (including using JMRI)**

.. list-table:: 
  :widths: 50 25 25
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No
  * - 1. Is the light on the Arduino board on?
    - Go to Question 2.
    - xx
  * - 2. xx
    - xx
    - xx

|

When Configured as an Access Point
==================================

**If you have configured your EX-CommandStation as an Access Point (separate network)**


.. list-table:: 
  :widths: 50 25 25
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No
  * - 1. Is the LED on the Arduino board on?
    - Go to Question 2.
    - You have not connected a 7-9v DC power supply to Arduino Board |BR| OR |BR| You have not connected a USB cable connected to a power supply, to Arduino Board
  * - 2. Can your phone see the WiFi network of the EX-CommandStation in the phone's available network list?
    - Go to Question 3
    - xx
  * - 3. Can your phone connect the WiFi network of the EX-CommandStation
    - Go to Question 4
    - xx
  * - 4. Can your throttle app connect the wiThrottle server of the EX-CommandStation |BR| |Engine Driver| should show you the wiThrottle server in the discovered servers list |BR| For |wiThrottle| you will need to type in the IP address and Port
    - Go to Question 5
    - xx
  * - 4. Can you turn the track power on?  |BR| Do the LEDs on the moto shield turn on?
    - xx
    - xx

|

When Configured in Station mode
===============================

**If you have configured your EX-CommandStation in Station mode (connected to your home WiFi network)**


.. list-table:: 
  :widths: 50 25 25
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No
  * - 1. Is the light on the Arduino board on?
    - Go to Question 2.
    - xx
  * - 2. xx
    - xx
    - xx
