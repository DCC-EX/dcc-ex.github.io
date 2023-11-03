.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: EX-CommandStation Command Station diagnosing Issues Troubleshooting

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

.. todo:: `MEDIUM - Diagnosing <https://github.com/DCC-EX/dcc-ex.github.io/issues/433>`_ - EX-CommandStation Software fails to load

Either using the |EX-I| to the Arduino IDE.

.. list-table:: 
  :widths: 40 20 40
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No - Possible reasons

  * - "Failed to upload because uploading error:"
    - Go to Question 2.
    - (a) Have you selected the correct COM port? |BR| See :ref:`ex-installer/installing:getting ready` for information on finding the correct COM port.
      (b) Have you selected the correct Arduino board type?
  
  * - 2. Have you selected the correct Baud rate?
    - Go to Question 3.
    - ToDo
  
  * - 3. Do you receive a message starts with "Failed to download..."
    - Go to Question 4.
    - (a) Your PC may not have an internet connection. 
      (b) Your PC's firewall software may be stopping the installer from accessing the internet. Temporarily disable the firewall, or create an exception for EX-Installer. |br| |br| An internet connection is required to download some files.      
  
  * - 4. ToDo?
    - ToDo.
    - ToDo

----

When Connected to a PC via USB
==============================

**If you have connected your EX-CommandStation to a PC via USB** (including for using JMRI).

Initial Check
-------------

As an initial check we recommend you should try to connect to your EX-CommandStation using |EX-WT|, even if you plan to use it via |JMRI| or a wifi throttle.

.. list-table:: 
  :widths: 40 20 40
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No - Possible reasons
  * - 1. Is the LED on the Arduino board on?
    - Go to Question 2.
    - (a) EX-CommandStation not connected to PC via USB.
      (b) CommandStation software may not have loaded correctly. 
      (c) Possible dead Arduino board.

      For (b) or (c), try loading the EX-CommandStation software again.

  * - 2. Can you connect to it using EX-WebThrottle?
    - Go to Question 3.
    - (a) EX-CommandStation not connected to your **PC** via USB.
      (b) Software may not have loaded correctly. Try loading the EX-CommandStation software again.

  * - 3. When you click the power on slider, it should say power on. |br| Do the 4 LEDs on the motor board turn on and stay on?
    - Go to Question 4.
    - (a) Have you plugged in and turned on a 12-15v DC power supply into the motor board
      (b) Have you made sure the polarity of the power supply is correct.

      |br| Do the 4 LEDs on the motor board turn on briefly, then turn off?

      (c) there is a short circuit on the track.
      (d) there is a short circuit in the loco.

  * - 5. When you select a loco and move the throttle, does the loco move?
    - Congratulations, your |EX-CS| is essentially working.
    - (a) Wrong loco DCC Address selected.
      (b) loco is not DCC decoder equipped.  (You will likely hear a humming coming from the loco. If you do remove it from the track urgently, the loco is being damaged.)

|

Using JMRI
----------

.. todo:: `MEDIUM - Diagnosing <https://github.com/DCC-EX/dcc-ex.github.io/issues/433>`_ - Using JMRI

.. list-table:: 
  :widths: 40 20 40
  :header-rows: 1
  :class: command-table

  * - Question 
    - If Yes
    - If No - Possible reasons    

  * - 1. Have you selected 'DCC++' as the System Manufacturer and 'DCC++ Serial Port' as the System connection in the preferences?
    - Go to Question 2.
    - (a) Select 'DCC++' as the System Manufacturer and 'DCC++ Serial Port' as the System connection in the preferences.

  * - 2. Have you selected the correct COM port?
    - Go to Question 3.
    - (a) Check which com port the EX-CommandStation is connected to. |BR| See :ref:`ex-commandstation/get-started/installer:1. getting ready` for details on how to determine the correct com port.

  * - 3. Can you turn the track power on?  |BR| Do the LEDs on the motor shield turn on?
    - Go to Question 4.
    - (a) Have you plugged in and turned on a 12-15v DC power supply into the motor board
      (b) Have you made sure the polarity of the power supply is correct. 

  * - 4. When you open a throttle window in JMRI, select a loco and move the throttle, does the loco move?
    - Congratulations, your |EX-CS| is essentially working.
    - (a) Have you connected the track to the 'MAIN' outputs of the Motor Board.  |BR| JMRI cannot directly control trains on the 'PROGRAMMING' outputs without using additional commands. See :ref:`support/ex-cs-troubleshooting:cannot drive a locomotive` for more information.
      (b) Wrong loco DCC Address selected.
      (c) loco is not DCC decoder equipped.  (You will likely hear a humming coming from the loco. If you do remove it from the track urgently, the loco is being damaged.)

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

  * - 3. The Wifi network name appears as "DCCEX-SAYS-BROKEN-FIRMWARE" 
    - See :doc:`/support/wifi-at-version` for details.
    - Go to Question 4

  * - 4. Can your phone connect the WiFi network of the EX-CommandStation
    - Go to Question 5
    - (a) ToDo
      (b) ToDo

  * - 5. Can your throttle app connect the wiThrottle server of the EX-CommandStation |BR| |BR| |Engine Driver| should show you the wiThrottle server in the discovered servers list |BR| For |wiThrottle| you will need to type in the IP address and Port
    - Go to Question 6
    - (a) ToDo
      (b) ToDo

  * - 6. Can you turn the track power on?  |BR| Do the LEDs on the motor shield turn on?
    - Go to Question 7.
    - (a) Have you plugged in and turned on a 12-15v DC power supply into the motor board
      (b) Have you made sure the polarity of the power supply is correct. 

  * - 7. When select a loco in the throttle app and move the throttle, does the loco move?
    - Congratulations, your |EX-CS| is essentially working.
    - (a) Have you connected the track to the 'MAIN' outputs of the Motor Board.  |BR| You cannot directly control trains on the 'PROGRAMMING' outputs without using additional commands which can be done in |Engine Driver| but not other WiFi throttle apps (Use the :guilabel:`Request Loco ID` button in |Engine Driver|.) |BR| recommend that the MAIN outputs be used to run a layout.
      (b) Wrong loco DCC Address selected.
      (c) loco is not DCC decoder equipped.  (You will likely hear a humming coming from the loco. If you do remove it from the track urgently, the loco is being damaged.)

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
    - (a) You may be on a different network to the EX-CommandStation (e.g. 2.5gHz VS 5gHz connection to you home router.) Try entering the IP address and Port manually.  To 
