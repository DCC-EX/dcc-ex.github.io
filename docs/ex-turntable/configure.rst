.. include:: /include/include.rst
.. include:: /include/include-l1.rst
..
.. image:: ../_static/images/product-logo-ex-turntable.png
   :alt: EX-CommandStation
   :scale: 40%
   :align: right

**********************
Configuration options
**********************

|conductor|

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

TURNTABLE_EX_MODE
__________________

`Default: TURNTABLE`

`Valid values: TURNTABLE, TRAVERSER`

This option can be used to enable support for horizontal or vertical traversers, as well as limited rotation turntables that cannot rotate a full 360 degrees.

Be sure to read the documentation carefully and ensure both home and limit sensors are functioning correctly.

SENSOR_TESTING
_______________

`Default: disabled`

To enable sensor testing, uncomment this line by removing the "//" from in front of "#define".

When sensor testing is enabled, all Turntable-EX operations are disabled. The state changes of HOME and LIMIT sensors are printed to the serial console when activated/deactivated, and no other activity is possible.

This is ideal for ensuring sensors are functional prior to enabling TRAVERSER mode.

HOME_SENSOR_ACTIVE_STATE
_________________________

`Default: LOW`

`Valid values: LOW, HIGH`

This is the state that the homing sensor reports to Turntable-EX when activated. Use LOW for sensors that activate by pulling the sensor output to ground, and HIGH for sensors that pull the output to 5V.

LIMIT_SENSOR_ACTIVE_STATE
_________________________

`Default: LOW`

`Valid values: LOW, HIGH`

This is the state that the limit sensor reports to Turntable-EX when activated. Use LOW for sensors that activate by pulling the sensor output to ground, and HIGH for sensors that pull the output to 5V.

The limit sensor is only used when Turntable-EX is set to TRAVERSER mode.

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
__________________

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

While the pre-defined stepper driver/motor combinations above will likely be sufficient for most use cases, it is possible to define your own stepper driver configuration providing it is supported by the AccelStepper() Arduino library. Refer to `defining custom stepper drivers`_.

DISABLE_OUTPUTS_IDLE
_____________________

`Default: enabled`

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
________

`Default: 500`

`Valid values: 0 to long time`

This is the time in milliseconds that the LED is on and off when the set to a slow blink. With the default, it will be on for 500ms, then off for 500ms.

Advanced configuration options
==============================

.. image:: /_static/images/tinkerer-level.png
  :alt: Tinkerer Level
  :scale: 50%

DEBUG
______

`Default: Disabled`

If debug level output is requested as part of a support ticket or when troubleshooting in general, uncomment this line by removing the "//" from in front of "#define".

SANITY_STEPS
____________

`Default: 10000 (Disabled)`

`Valid values: 1 to 65535`

This is the maximum number of steps the stepper motor will move during homing and calibration before flagging a failure.

If you have a stepper driver/motor combination that is configured for a large number of steps, or if you have a gear ratio that results in a high number of steps, you may need to increase this number in order for the calibration process to succeed.

HOME_SENSITIVITY
________________

`Default: 150 (Disabled)`

`Valid values: 1 to 65535`

This is the minimum number of steps required for the turntable to rotate away from the homing sensor before it deactivates, which is used during the calibration sequence.

If you have a stepper driver/motor combination that is configured for a large number of steps, or if you have a gear ratio that results in a high number of steps, you may need to increase this number in order for the calibration process to succeed.

FULL_STEP_COUNT
_______________

`Default: 4096 (Disabled)`

`Valid values: 1 to 65535`

If for some reason the automatic calibration sequence is not recording the correct number of steps required for a full 360 degree rotation, or if there is some other requirement to override this value, then uncomment this line and define the desired number of steps.

If you enable this option, the calibration sequence will never run automatically even if the step count is not recorded in EEPROM, and this setting will always override that on startup.

You can initiate the calibration command manually while this option is enabled, it will perform the calibration sequence and record the calibrated step count in EEPROM, and that setting will take effect whilst Turntable-EX is running. However, the calibrated value in EEPROM will be overridden at the next startup unless this option is disabled.

DEBOUNCE_DELAY
______________

`Default: 10 (Disabled)` - TRAVERSER mode

`Default: 0 (Disabled)` - TURNTABLE mode

`Valid values: 0 to 50` (any higher and you will compromise the response time of the limit sensors)

When using mechanical switches as HOME and LIMIT sensors, it is often necessary to "debounce" these switches to mask out the noise when they activate/deactivate. If using mechanical switches, it is advised to enable SENSOR_TESTING mode to validate the HOME and LIMIT switch operation, and this option may be tuned if necessary.

Note that in turntable mode, a hall effect or similar sensor is typically used which does not require debouncing, and therefore the default in turntable mode is to set this delay to 0.

Defining custom stepper drivers
===============================

.. image:: /_static/images/tinkerer-level.png
  :alt: Tinkerer Level
  :scale: 50%

.. note:: 

  We have chosen a few common stepper driver/motor combinations to be on the supported driver/motor list, and there are a large number of other options on the market, many of which are touted to be "pin compatible" with drivers that are already supported.

  If you're reading this section because your driver/motor combination is not explicitly supported, we encourage you to see if it is compatible with a supported combination prior to defining a custom entry, and to share that information with the team.

  Over time, we expect to build a more complete list of drivers and motors that are compatible with what we have tested.

If you have a need to use a stepper driver and motor combination that isn't on the supported list and isn't "pin-compatible" with an existing supported driver/motor combination, you may need to define a custom entry in "config.h" to allow Turntable-EX to work correctly.

To do this, you will need to add a valid AccelStepper() definition with the appropriate parameters provided, and this entry needs to be  defined as your `STEPPER_DRIVER` option.

The list of parameters required are documented on the `AccelStepper <http://www.airspayce.com/mikem/arduino/AccelStepper/>`_ web page.

**Note:** There has been a slight modification to the AccelStepper library included with Turntable-EX. If you have a need to invert the enable option, then provide this as the last parameter. The modified library sets the enable pin (if defined) when the stepper object is instantiated, and if it needs to be inverted, this happens at the same time. We do not call the setEnablePin() or setPinsInverted() functions at any point. You can see this in use in the "standard_steppers.h" file as defined for the "TWO_WIRE_INV" driver option.

To add this to "config.h", add your new definition **before** the `STEPPER_DRIVER` line, and update `STEPPER_DRIVER` to use your definition, and ensure all standard options are commented out:

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //  Define the stepper controller in use according to those available below, refer to the
  //  documentation for further details on which to select for your application.
  //
  #define MY_STEPPER_DRIVER AccelStepper(Type, Pin1, Pin2, Pin3, Pin4, Enable, Invert)
  #define STEPPER_DRIVER MY_STEPPER_DRIVER
  // #define STEPPER_DRIVER ULN2003_HALF_CW
  // #define STEPPER_DRIVER ULN2003_HALF_CCW
  // #define STEPPER_DRIVER ULN2003_FULL_CW
  // #define STEPPER_DRIVER ULN2003_FULL_CCW
  // #define STEPPER_DRIVER TWO_WIRE
  // #define STEPPER_DRIVER TWO_WIRE_INV
