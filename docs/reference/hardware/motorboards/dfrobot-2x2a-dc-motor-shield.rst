.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-description.rst
**************************************
DFRobot 2x2A DC Motor Shield (DRI0009)
**************************************

|engineer|

**THIS BOARD HAS NO CURRENT SENSE!** Refer to the :ref:`reference/hardware/motorboards/motor-board-config:current sense and sense factor` section for further information.

This is another L298 based board with inadequate cooling. Fan and/or heat sink recommended. Max current realistically 1.3A. This board has NO CURRENT SENSE. As with many boards like this, both L298 current sense pins are tied to ground. Cutting traces and adding sense resistors or the use of an eternal current sense board is required for short circuit protection and loco programming. If you don't use current sense, you must ground pins A0 and A1 on the Arduino or you will get an overcurrent condition.

Speed Control Jumpers need to all be on the PWM side of the shield (all 4 jumpers on the right 4 pins)
Power Source Selection Jumpers need to both be on PWRIN (to the left) and NOT VIN

| ENABLE1 (EN1) - D5 (normally pin 3)
| ENABLE2 (EN2) - D6 (normally pin 11)
| DIR1 (M1)     - D4 (normally pin 12)
| DIR2 (M2)     - D7 (normally pin 13)

On the schematic, pin 1 of the jumper bank is the right side as you read the labels, the PWM side.

NOTE: There is a "Twin" version of this board that uses pins 10, 11 and 12, 13 instead

.. image:: /_static/images/motorboards/dfrobot_shield_2x2_main.jpg
   :alt: DFRobot 2x2
   :scale: 60%
