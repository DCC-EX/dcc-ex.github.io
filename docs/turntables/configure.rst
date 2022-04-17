****************************
Testing, Tuning, and Control
****************************

Testing
=======

The next step is to validate that your CommandStation has successfully connected to Turntable-EX, and to perform some basic functionality tests to ensure it is working as designed.

Configure CommandStation-EX
---------------------------

Before you will be able to use Turntable-EX, you need to configure the CommandStation to load the appropriate device driver.

This requires creating or editing the myHal.cpp file in the CommandStation-EX version 4.0.2 or later code and uploading it to your CommandStation.



Connect a USB cable to your CommandStation, and power on Turntable-EX followed by the CommandStation.

Once the CommandStation is up and running, open a serial terminal from the Arduino IDE and at the prompt you can use the "<D HAL SHOW>" command to validate that Turntable-EX is available.

Like most other devices within DCC++ EX, there is a diagnostic command available to test that Turntable-EX is working correctly and, more importantly, help you fine tune the correct step numbers for that perfect alignment with your layout at each position.

.. code-block:: 

  <D TT vpin steps activity>



Automation with EX-RAIL
=======================

MOVETT(vpin, steps, activity)

DONE before first ROUTE, if a position is preferred on startup, make it explicit.
