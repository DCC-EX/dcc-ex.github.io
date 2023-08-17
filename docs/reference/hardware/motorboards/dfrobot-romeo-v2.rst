:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-description.rst
**************************************
DFRobot Romeo V2
**************************************

|engineer|


**THIS BOARD HAS NO CURRENT SENSE!** Refer to the :ref:`reference/hardware/motorboards/motor-board-config:current sense and sense factor` section for further information.

On the surface, this seems like a great idea, an Arduino and motor controller on one board. It is a very thin surface ;) While we don't recommend it, an Engineer who reads these notes, may still find a use for it. The V2 uses the ATmega32u4 chip instead of either of the chips used on an Uno or a Mega. It only has 2 interrupts that are usable and it reverses their pin assignments. It uses serial on the chip, not with a UART as on the other boards. It may need a software change to accommodate the timer. It also has the same amount of memory as an Uno, which will only run the basic version of |EX-CS| without options. In addition, the serial port uses memory to operate, so you have even less memory free to use than on an Uno.

Onboard is the L298 dual H-Bridge, with the same lack of cooling as on the Arduino Motor Shield. It will only deliver 1.2 to 1.3A instead of 2A, if you add a fan. Very importantly it has NO CURRENT SENSE for either track. The sense outputs are tied to ground. You would have to cut traces and add resistors at the least, or buy current sense boards.

.. image:: /_static/images/motorboards/romeo_v2.jpg
   :alt: Romeo V2
   :scale: 40%

