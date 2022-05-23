**********************
Configuration options
**********************

.. image:: ../_static/images/tinkerer-level.png
  :alt: Tinkerer Level
  :scale: 50%

Turntable-EX has a number of different configuration options available to customise the behaviour to suit your needs.

Configuration changes are made by editing the "config.h" file.

The various configuration options are outlined below, and all are declared on their own line using the "#define" directive (eg. #define I2C_ADDRESS 0x60).

Standard configuration options
===============================

I2C_ADDRESS
____________

`Default: 0x60`

This is the address that Turntable-EX will occupy on the I2C bus. The default address has been chosen as it is not expected to conflict with any of the existing know I/O expander modules or other known I2C devices.

If you need to change this for any reason, ensure that the I2C address in "myHal.cpp" in the CommmandStation-EX software is also changed to the same value.

Multiple instances of Turntable-EX can be controlled by the same CommandStation by ensuring each has its own unique I2C address.

HOME_SENSOR_ACTIVE_STATE
_________________________

`Default: LOW`

`Valid values: LOW, HIGH`

This is the state that the homing sensor reports to Turntable-EX when activated. Use LOW for sensors that activate by pulling the sensor output to ground, and HIGH for sensors that pull the output to 5V.

RELAY_ACTIVE_STATE
___________________

`Default: HIGH`

`Valid values: HIGH, LOW`

This is the state that the phase inversion relays need to be set to in order to activate, or invert the phase. Use HIGH for relays that require 5V to activate, and LOW for those that require the input to be grounded to activate.

PHASE_SWITCHING
________________

`Default: AUTO`

`Valid values: AUTO, MANUAL`

When set to AUTO, phase switching happens automatically as the turntable rotates. The point at which phase inversion happens is determined by the PHASE_SWITCH_ANGLE (see below), and it will automatically revert 180 degrees later.

PHASE_SWITCH_ANGLE
___________________

`Default: 45`

`Valid values: 0 - 179`

This is the angle in degrees that the turntable needs to rotate away from the home position in order to trigger DCC phase inversion by activating the phase inversion relays. Once the turntable rotates a further 180 degrees, the phase will revert by deactiving the phase inversion relays.

STEPPER_DRIVER
_______________

`Default: ULN2003_HALF_CW`

`Valid values:`

- ULN2003_HALF_CW - ULN2003 stepper driver with a 28BYJ-48 motor, configured for half step mode defaulting to a clockwise rotation
- ULN2003_HALF_CCW - ULN2003 stepper driver with a 28BYJ-48 motor, configured for half step mode defaulting to a counter-clockwise rotation
- ULN2003_FULL_CW - ULN2003 stepper driver with a 28BYJ-48 motor, configured for full step mode defaulting to a clockwise rotation
- ULN2003_FULL_CCW - ULN2003 stepper driver with a 28BYJ-48 motor, configured for full step mode defaulting to a counter-clockwise rotation
- TWO_WIRE - Two wire stepper driver (eg. A4988, DRV8825) with a NEMA17 motor
- TWO_WIRE_INV - Two wire stepper driver (eg. A4988, DRV8825) with a NEMA17 motor, with the driver's enable pin inverted

While the pre-defined stepper driver/motor combinations above will likely be sufficient for most use cases, it is possible to define your own stepper driver configuration providing it is supported by the AccelStepper() Arduino library. Refer to :ref:`turntable-ex/configure:defining custom stepper drivers`.

DISABLE_OUTPUTS_IDLE
_____________________

When defined, this option will ensure that the stepper driver outputs are disabled when the stepper stops rotating. This can prevent stepper drivers and motors from becoming warm during idle time.

To disable this option, simply comment the line out by adding "//" before the "#define".

STEPPER_MAX_SPEED
__________________

`Default: 200`

`Valid values: 1 - 1000`

This is the maximum speed that the turntable will rotate at, in steps per second.

STEPPER_ACCELERATION
_____________________

`Default: 25`

`Valid values: > 0`

The acceleration rate of the turntable, which is defined as steps per second, per second. This is what gives Turntable-EX a more prototypical acceleration/decceleration rate when rotating.

LED_FAST
_________

`Default: 100`

`Valid values: 0 to long time`

This is the time in milliseconds that the LED is on and off when the set to a fast blink. With the default, it will be on for 100ms, then off for 100ms.

LED_SLOW
_________

`Default: 500`

`Valid values: 0 to long time`

This is the time in milliseconds that the LED is on and off when the set to a slow blink. With the default, it will be on for 500ms, then off for 500ms.

Advanced configuration options
===============================

DEBUG
______

If debug level output is requested as part of a support ticket or when troubleshooting in general, uncomment this line by removing the "//" from in front of "#define".

SANITY_STEPS
_____________

`Default: 10000`

`Valid values: 1 to 65535`

This is the maximum number of steps the stepper motor will move during homing and calibration before flagging a failure.

If you have a stepper driver/motor combination that is configured for a large number of steps, or if you have a gear ratio that results in a high number of steps, you may need to increase this number in order for the calibration process to succeed.

HOME_SENSITIVITY
_________________

`Default: 150`

`Valid values: 1 to 65535`

This is the minimum number of steps required for the turntable to rotate away from the homing sensor before it deactivates, which is used during the calibration sequence.

If you have a stepper driver/motor combination that is configured for a large number of steps, or if you have a gear ratio that results in a high number of steps, you may need to increase this number in order for the calibration process to succeed.

Defining custom stepper drivers
================================

These need to have a valid AccelStepper() entry defined.

Further info to be added here.