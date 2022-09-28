.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: EX-CommandStation Command Station diagnosing Issues Troubleshooting

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

***************************
Steps to Diagnose a Problem
***************************

|conductor| 

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:


----

If you have connected your EX-CommandStation to a PC via USB (including using JMRI)
=========================================================================================

- Is the light on the Arduino board on?

----

If you have configured your EX-CommandStation as an Access Point (separate network)
=====================================================================================

- Is the light on the Arduino board on?

 - Most common cause

  - You have not connected a 7-9v DC power supply to Arduino Board |BR| OR
  - You have not connected a USB cable connected to a power supply, to Arduino Board

- Can your phone see the WiFi network of the |EX-CS| in the phone's available network list?


- Can your phone connect the WiFi network of the |EX-CS| 


- Can your throttle app connect the wiThrottle server of the |EX-CS| 

 - |Engine Driver| should show you the wiThrottle server in the discovered serve list
 - For |wiThrottle| you will need to type in the IP address and Port

  
- Can you turn the track power on?

 - Do the LEDs on the moto shield turn on

----

If you have configured your EX-CommandStation in Station mode (connected to your home WiFi network)
========================================================================================================

- Is the light on the Arduino board on?
