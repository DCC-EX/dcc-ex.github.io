.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst
|EX-CS-LOGO|

**************************
YFRobot L298P Motor Shield
**************************

|conductor|

.. warning:: 

   This board is **not** compatible with |TM| DC mode.

This board is electrically similar, though a different layout than the Arduino motor shield and does not have a brake_pin feature. Often cheaper. Supports 2A per channel, but can deliver realistically 1.3 or maybe 1.5 Amps with an added heatsink and cooling fan. 

The YFROBOT Motor Shield will Only run DCC waveform and will Not be able to run DC waveform with the new TrackManager features as this shield does not have a brake_pin.
 
**Do NOT confuse this with the DFRobot Motor Shield, which is not plug and play!**

.. figure:: /_static/images/motorboards/yfrobot1.png
   :alt: YFRobot L298P Motor Driver Shield
   :scale: 30%

   YFRobot L298P Motor Driver Shield

:doc:`Install the YFRobot Motor Shield (similar to Deek-Robot) </ex-commandstation/get-started/assembly>`

**Remember to select YFROBOT_MOTOR_SHIELD in your config.h file or from the motor board dropdown if using EX-Installer**

Pinout for reference:

| PWM1/MAIN Enable - D5 (normally pin 3)
| PWM2/PROG Enable- D6 (normally pin 11)
| DIR1/MAIN Signal - D4 (normally 12)
| DIR2/PROG Signal - D7 (normally pin 13)
| Current Sense MAIN - A0
| Current Senst PROG - A1

.. Note:: This configuration uses the normal accuracy waveform to avoid having to use jumpers. To use the high-accuracy waveform, you would need to use pins 3 and 11 in your motor board definition in config.h and jumper them to D5 and D6 on the shield. For information about high-accuracy mode, See:

:ref:`High Accuracy Waveform <reference/hardware/motorboards/motor-board-config:Using High Accuracy Waveform Mode>`

.. Todo:: `LOW - Hardware <https://github.com/DCC-EX/dcc-ex.github.io/issues/430>`_ - Give a link to how to handle the jumper reconfig

|
