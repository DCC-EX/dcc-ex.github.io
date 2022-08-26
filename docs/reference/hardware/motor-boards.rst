.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-REF-LOGO|

***********************
Supported Motor Drivers
***********************

|conductor| |tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:


|EX-CS| is compatible with a wide variety of motor boards, also known as "dual H-bridges" and "motor shields". We've sorted them from least difficult to most difficult to use to help you decide what to use. When it comes to selecting a board, some considerations are size, whether it is a shield or needs to be connected with jumper wires, the amount of current you need, and whether it has current sensing capability built-in or if you have to supply it yourself.

If you have trouble finding a particular board from the list, try searching based on it's name or the type of chip on the board and the terms "H-Bridge" or "Motor Shield". There are often many places that sell these, especially the Chinese sites like AliExpress and Banggood.

**TL;DR** (aka short version): We currently recommend the Arduino Motor Shield R3 or a supported clone board like the Deek-Robot.

.. image:: /_static/images/deek_robot1_sm.jpg
   :alt: Deek Robot Motor Shield
   :scale: 100%

.. note:: Where appropriate, we have used the terms "single" and "dual" to indicate on the non-shield type boards, which ones have just a single H-Bridge for one track and which ones have two. A single H-Bridge board will power your main track, but you will then need another board of some kind to connect to your programming track

What is a Motor Controller?
============================

A motor controller (aka shield, aka board) is just a high voltage, high current switch. While initially designed to power electric motors, we use it to create the DCC signal to the track in a clever misapplication of technology. Normally, a pulse width modulated (PWM) signal would be applied to a motor with the PWM pin to control speed and the direction pin would switch the voltage from positive to negative to control the motor spin direction. Instead, we send full DC track voltage to the PWM pin and switch the direction pin at the DCC frequency (around 8000 times a second) to generate the bi-polar square wave. In this way, we use the 5V DC (or 3.3V) microcontroller output to switch the voltage from separate 12-18V DC power supply connected to the motor controller, and create a pulse train signal of 1's and 0's that a mobile decoder can interpret as commands.

Current list of boards
=======================

Below we outline the various details that we know of related to each of the different boards that we've either tested, or know to work based on user feedback.

Easy to use boards
------------------

|conductor|

.. toctree::
    :maxdepth: 1

    Arduino Motor Shield - 1.5A [RECOMMENDED] </reference/hardware/motorboards/arduino-motor-shield>
    Deek-Robot - 1.5A [RECOMMENDED] </reference/hardware/motorboards/deek-robot-motor-shield>
    Flashtree - 1.5A </reference/hardware/motorboards/flashtree-motor-shield>
    DIY More L298NH - 2A </reference/hardware/motorboards/diy-more-l298nh-motor-shield>
    YFRobot L298P - 2A </reference/hardware/motorboards/yfrobot-l298p>

Intermediate boards
-------------------

|tinkerer|

These boards require wiring.

.. toctree::
    :maxdepth: 1

    L298N (dual) - 2A </reference/hardware/motorboards/L298N-motor-board-setup>
    Dual Module H-bridge MOSFET IRF3205 - 15A </reference/hardware/motorboards/IRF3205-motor-board-setup>
    Pololu MC33926 - 3A </reference/hardware/motorboards/pololu-mc33926>
    MiniIBT L6201P (single) - 5A </reference/hardware/motorboards/miniibt-motor-driver-l6201p>
    BTS7960 IBT_2 (single) - 43A </reference/hardware/motorboards/IBT_2-motor-board-setup>

Expert Level Boards
-------------------

|engineer|

These boards require you to add your own config to the config.h file, and may not have good current sensing. That said, if you buy a separate current sense board, we particularly like the IBT_2 board (though you will need 2 of them or some other board for the programming track)

.. toctree::
    :maxdepth: 1

    Keyes/Fundumoto ("Beeper Board") - 2A </reference/hardware/motorboards/keyes-fundumoto>
    Makerfabs H-Bridge - 8A </reference/hardware/motorboards/makerfabs-h-bridge-motor-shield>
    Velleman KA03/VMA03 - 2A </reference/hardware/motorboards/velleman-ka03-kit-vma03>
    DFRobot 2x2A DC Motor Shield (DRI0009) - 2A </reference/hardware/motorboards/dfrobot-2x2a-dc-motor-shield>

Incompatible boards
-------------------

* VNH2SP30 - SparkFun Monster Moto and others. It can't switch fast enough to generate a reliable DCC signal
* IFX9202ED - Infineon Dual H-Bridge. Can't switch fast enough.
* :doc:`/reference/hardware/motorboards/dfrobot-romeo-v2` - Well, an Engineer could perhaps get this one to work.
* Kuman Board (and any L293D based boards) - not enough current.
* Pololu TB9051FTG based motor shield. It can't switch fast enough to generate a reliable DCC signal. `Product page <https://www.pololu.com/product/2520>`_.
   
Other boards
------------

|engineer|

While not fully supported and tested, other boards can potentially be used. Look for the following criteria:

* We recommend a dual h-bridge board or two discrete h-bridge boards. They can be different sizes, one bigger for main track and one smaller for programming track operations.
* It must handle enough current for the layout. 2 amps will drive 3-5 HO scale locomotives.
* It must have working and accurate current sensing (many do not)
* It must be able to switch at least 10000 times per second (some do not)
* Look for an Arduino shield form factor to eliminate wiring (not required but preferred)

.. Note:: Current capabilities of these boards, especially the boards based on the L298 with no heat sink fins like the Arduino Motor Shield can really not deliver 2 Amps. A realistic number would be 1.5 Amps IF you added a heat sink and a cooling fan. If you need 2 Amps or more, you will need to go with a higher current board.

Configuring Motor Drivers
=========================

|tinkerer| |engineer|

If your board is not in the list of supported motor board types, or if you need to make changes or have more information about how motor boards are configured in |EX-CS|, see:

.. toctree:: 
  :maxdepth: 1

  Motor Driver Configuration Guide </reference/hardware/motorboards/motor-board-config>

High Accuracy Waveform
======================

|engineer|

If you're experiencing issues with specific decoders and all attempts to get them working are failing, you may need to enable the high accuracy waveform functionality (providing your motor driver supports it).

.. toctree:: 
  :maxdepth: 1

  High Accuracy Waveform Guide </reference/hardware/motorboards/high-accuracy>