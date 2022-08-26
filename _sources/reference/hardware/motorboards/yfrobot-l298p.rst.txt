.. include:: /include/include.rst
.. include:: /include/include-l3.rst
**************************************
YFRobot L298P Motor Shield
**************************************

|conductor|

This board is electrically the same, though a different layout than the Arduino motor shield. Often cheaper. Supports 2A per channel, but can deliver realistically 1.3 or maybe 1.5 Amps with an added heatsink and cooling fan. **Do NOT confuse this with the DFRobot Motor Shield, which is not plug and play!**

.. image:: /_static/images/motorboards/yfrobot1.png
   :alt: YFRobot L298P Motor Driver Shield
   :scale: 30%

:doc:`Install the YFRobot Motor Shield (same as Deek-Robot) </ex-commandstation/get-started/assembly>`

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

.. Todo:: LOW - Give a link to how to handle the jumper reconfig

|