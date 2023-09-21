.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst
|EX-CS-LOGO|

*******************************
Makerfabs H-Bridge Motor Shield
*******************************

|engineer|

.. warning:: 

   This board is **not** compatible with |TM| DC mode.

**THIS BOARD HAS NO CURRENT SENSE!** Refer to the :ref:`reference/hardware/motorboards/motor-board-config:current sense and sense factor` section for further information.

The higher current capability and efficient power MOSFETs, make this board a good choice if you are running more than 3-5 locos.

Select MAKERFABS_MOTOR_SHIELD in your config.h file.

Pinout

| PWM1 - D9 (normally pin 3)
| PWM2 - D10 (normally pin 11)
| CNTRL1A (DIR1A) - D4 (normally 12)
| CNTRL1B (DIR1B) - D5
| CNTRL2A (DIR2A) - D7 (normally 13)
| CNTRL2B (DIR2B) - D8
| ENABLE/SHUTDOWN - D6
