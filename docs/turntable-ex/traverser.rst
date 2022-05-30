*******************************************
Traversers and Limited Rotation Turntables
*******************************************

Turntable-EX has been written to cater for both horizontal and vertical traversers, as well as turntables that do not rotate a full 360 degrees.

The primary difference from the standard full rotation turntable mode is the addition of a limit sensor to indicate when the traverser or limited rotation turntable reaches the end of its range of movement.

The home sensor takes on an addition purpose in this mode, so in addition to flagging the home position, it also operates as a limit sensor.

Sensor testing mode
====================

As part of introducing the traverser feature, an additional option has been enabled that disables all Turntable-EX operations and simply reports the state changes of the HOME and LIMIT sensors in the serial console.

It is highly recommended that this feature is enabled, and both HOME and LIMIT sensors are tested prior to enabling TRAVERSER mode, especially when using mechanical switches that require proper adjustment and alignment to prevent mechanical damage from the stepper motor attempting to drive traversers or turntable bridges beyond physical boundaries.

Refer to :ref:`turntable-ex/configure:sensor_testing` to enable sensor testing mode.

