*****************
Turntable-EX
*****************

Turntable-EX is a fully integrated turntable controller, using an Arduino microcontroller to drive a stepper controller and motor to spin the turntable bridge.

The integration includes:

* I2C device driver
* Full EX-RAIL automation support
* Specific debug/test command (handy for tuning step positions)
* Out-of-the-box support for several common stepper controllers (see below)
* DCC signal phase switching to align bridge track phase with layout phase

What you need for Turntable-EX
==============================

* An Arduino microcontroller (tested on Nano V3, both old and new bootloader, and Uno R3)
* A stepper motor controller and stepper motor
* A dual relay board (or similar) if you wish to use the phase switching capability
* A hall effect (or similar) sensor for homing

Supported stepper controllers and motors
=========================================

The default configuration of Turntable-EX is for the ubiquitous ULN2003/28BYJ-48 stepper controller and motor combination. These steppers are used in a myriad of applications, are inexpensive, and will be suitable for most smaller scale turntable applications.

However, it is very easy to use one of several other common stepper controllers if you require more torque, or if you prefer to use a NEMA17 or other stepper motor.

The other controllers supported are:

* A4988
* DRV8825
* TMC2208

If you have a need to use a different controller, code updates will be required unless it is "pin compatible" with one of the existing controllers.
