********************************
High Accuracy Waveform Mode
********************************

**Engineers Only**

Do you need it? Most likely, you don't. But if you run into a problem with a particular decoder and all the usual settings don't help, you may want to try this mode. We have found that some older decoders do not adhere to the NMRA specification tolerances. They can fail to read bits that are within the proper range. While rare, this could occur. The High Accuracy mode makes the waveform, the pulse train of 1's and 0's, even tighter to the nominal values in the specification.

The nominal spec asks for 58us 1 bits and 100us 0 bits with a few microseconds leeway in either direction. We opted to use 116us 0 bits since it is exactly twice a 1 bit and made it easy for us to use one timer to generate both bits. On occasion, with all the other things going on inside the command station, and the way we use timers and interrupts in normal accuracy mode, it is possible for there also to be a little jitter. That's when the bit durations from bit to bit can vary a few microseconds. High Accuracy Mode uses the hardware timers instead of just our software routine, to tighten up any jitter.

For this to work, you need two things:

* The signal pin for the track you want to have high accuracy must be a Timer1 pin
* You must use the single signal pin configuration for your motor board

.. NOTE:: You do not have to do anything to enable High Accuracy Waveform Mode. If your motor board config meets the above two criterion, it will be enabled automatically and report that in the serial monitor boot log.

The Motor Board Config
========================

You will notice that your motor driver type is set in the *config.h* file. This line sets a standard motor shield compatible with the Arduino Motor Shield:

.. code-block:: cpp

#define MOTOR_SHIELD_TYPE STANDARD_MOTOR_SHIELD

Whether called Motor "boards" or "shields" or "drivers", they are defined in the *MotorDrivers.h* file and look like this:

.. code-block:: cpp

#define STANDARD_MOTOR_SHIELD F("STANDARD_MOTOR_SHIELD"), \
  new MotorDriver(3, 12, UNUSED_PIN, UNUSED_PIN, A0, 2.99, 2000, UNUSED_PIN), \
  new MotorDriver(11, 13, UNUSED_PIN, UNUSED_PIN, A1, 2.99, 2000, UNUSED_PIN)

The first line after setting the name and display text is for the Main track and the next line is for the programming track. The parameters are as follows:

.. code-block:: cpp

MotorDriver(power_pin, signal_pin, signal_pin2, brake_pin, current_pin, senseFactor, tripMilliamps, faultPin)

Therefore, the second and third parameters are the signal pins. Some boards have 2 direction pins (ex: IBT_2 Motor Driver Board). These are sometimes labelled CW and CCW for clockwise and counter-clockwise. If you want to use two pins so that you don't need a transister or integrated circuit inverter, then you can't use the high accuracy waveform.

If you have a board with a single DIR input, or wish to make the simple 1 transistor and 2 resistor inverter circuit described ***TODO: Enter link here***, you can use the high accuracy mode.

You must choose signal pins from the following list for your Arduino:

Mega - 11, 12 and 12
Uno - 9 and 10
Nano - 9 and 10

By luck, two of the Mega pins associated with Timer 1 are directly under the DIRA and DIRB pins of an Arduino Motor Shield or pin compatible shield; pins 12 and 13. Therefore, the combination of a Mega and this shield will automatically use high accuracy for both tracks.

However, an Uno's pins do not line up with this shield. In order to use high accuracy mode, you would have to change the signal pin assignements and use a jumper wire.

***TODO: put description here***

***TODO: put description of creating a motor board type here or link to another section if I did it already***