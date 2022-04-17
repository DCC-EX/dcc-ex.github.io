*********************
Configure and Control
*********************

Connect a USB cable to your CommandStation, and power on Turntable-EX followed by the CommandStation.

  Once the CommandStation is up and running, open a serial terminal from the Arduino IDE and at the prompt you can use the "<D HAL SHOW>" command to validate that Turntable-EX is available.

Testing and tuning
==================

Like most other devices within DCC++ EX, there is a diagnostic command available to test that Turntable-EX is working correctly and, more importantly, help you fine tune the correct step numbers for that perfect alignment with your layout at each position.

.. code-block:: 

  <D TT vpin steps activity>



Automation with EX-RAIL
=======================

MOVETT(vpin, steps, activity)

DONE before first ROUTE, if a position is preferred on startup, make it explicit.
