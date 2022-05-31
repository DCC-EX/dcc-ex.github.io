*******************************************
Traversers and Limited Rotation Turntables
*******************************************

.. image:: ../_static/images/tinkerer-level.png
  :alt: Tinkerer Level
  :scale: 50%

Overview
=========

Turntable-EX has the ability to cater for both horizontal and vertical traversers, as well as turntables that do not rotate a full 360 degrees.

The primary difference from the standard full rotation turntable mode is the addition of a limit sensor to indicate when the traverser or limited rotation turntable reaches the end of its range of movement.

The home sensor takes on an additional purpose in this mode, so in addition to flagging the home position, it also operates as a limit sensor.

What you need for traverser mode
_________________________________

The same components outlined in :ref:`turntable-ex/turntable-ex:what you need for turntable-ex` apply in traverser mode, with two likely exceptions:

1. Home and limit sensors: Given the need for positive stops at each of traverser travel, be it vertical, horizontal, or restricting rotation within an arc for limited rotation turntables, micro switches are likely a better choice for these.

  .. image:: ../_static/images/turntable-ex/micro-switch.png
    :alt: Micro switch
    :scale: 20%

2. Dual relay board: With horizontal and vertical traversers, locomotives do not rotate, so it is therefore unlikely any DCC phase switching will be required. Limited rotation turntables are also unlikely to require phase inversion as locomotives will be unable to be rotated 180 degrees.

Assembly
=========



Sensor testing mode
====================

As part of introducing the traverser feature, an additional option has been enabled that disables all Turntable-EX operations and simply reports the state changes of the HOME and LIMIT sensors in the serial console.

It is highly recommended that this feature is enabled, and both HOME and LIMIT sensors are tested prior to enabling TRAVERSER mode, especially when using mechanical switches that require proper adjustment and alignment to prevent mechanical damage from the stepper motor attempting to drive traversers or turntable bridges beyond physical boundaries.

Refer to :ref:`turntable-ex/configure:sensor_testing` to enable sensor testing mode.

Considerations
===============

Home sensor - normal/forward direction triggers home sensor.

Limit sensor - reverse direction triggers limit sensor.


Automatic calibration
______________________

In traverser mode, the calibration sequence has three phases that ensures the calculated step count is reached prior to activating the limit sensor, ensuring this is a safeguard against moving too far.

.. code-block:: 

  Homing started
  Turntable homed successfully
  CALIBRATION: Phase 1, homing...
  Turntable already homed
  CALIBRATION: Phase 2, finding limit switch...
  CALIBRATION: Phase 3, counting limit steps...
  CALIBRATION: Completed, storing full turn step count: 2501                    <<== Step count to record
