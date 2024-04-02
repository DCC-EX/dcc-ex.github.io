.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst

|EX-CS-LOGO|

*****************************************************
Beta microcontrollers - STM32 Nucleo, ESP32, and SAMD
*****************************************************

|tinkerer| |engineer| |support-button| |githublink-ex-commandstation-button2|

|NEW-IN-V5|

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:

Newer, faster, better
=====================

As technology progresses, newer, faster, and better microcontrollers become available, and therefore the dev team works in the background on porting and testing of |DCC-EX| on newer generations of microcontrollers to see if they might better suit the |DCC-EX| project.

This is never done lightly, as the effort to support a new microcontroller might be high and the benefits may be too inconsequential, or indeed may mean loss of functionality.

Considerations for new microcontrollers
---------------------------------------

When considering new microcontrollers to test and experiment with as potential candidates for |EX-CS|, these are the sorts of concerns taken into account (there are more considerations than this of course, these are just the highlights):

- Architecture/code portability - how much work is required to adapt the codebase to support the architecture?
- Form factor - can existing users use their existing motor shields and accessories with them?
- Availability - with continuing microchip shortages impacting supply, is it still generally and easily available in quantity, and globally as we have users all over the world?
- Sustainability - is the manufacturer deprecating the series or likely to?
- Price - is it available at a price point that would encourage users to adopt it readily?
- Quality - is it available with a sufficient build quality to make it reliable?

Notes on 3v3 vs. 5V microcontrollers
------------------------------------

It's important to note that the newer generations of microcontrollers almost always operate at 3.3 volts rather than 5 volts.

For some, like the STM32F4xx range, this is a non-issue as their digital I/O pins are designed to be 5V tolerant, meaning your existing sensors, serial devices, and |I2C| devices running at 5V are expected to be compatible. Outputs may need further consideration though, as while a "high" signal at 3v3 will trigger most 5V input logic devices, in some rare instances it can potentially not provide a high enough voltage. Using level shifters for digital outputs will resolve these issues, and if you want an extra layer of caution, you can use level shifters for the digital inputs as well.

For others that are not 5V tolerant, using 5V accessories will cause damage to the microcontroller, so using digital I/O level shifters is mandatory with these.

ALL 3v3 microcontrollers require analog inputs to be restricted to no more than 3.3V. This means only some Motor Driver boards are compatible unmodified with 3v3 microcontrollers to read output current. For the moment we recommend the genuine Ardiuno Motor Driver R3, and only the R3 version of it. Motor Drivers such as the Deek Robot can be modified readily enough. We will document this, but in the meantime ask on the Discord server.

.. note::  

  Some devices such as the ESP01 WiFi board and HC05/06 Bluetooth boards are already 3v3 devices, so if you have set these up with level shifters, the level shifters will no longer be required when using 3v3 microcontrollers.

Microchip SAMD21 series
=======================

Microchip's SAMD21 series of ARM Cortex-M0+ enabled microcontrollers offer significantly more resources than the Mega. The Arduino Zero uses Microchip's SAMD21G18A in an UNO R3 compatible form factor. A variety of manufacturers have produced clones of this design, usually omitting the Embedded Debugger (EBDG) of the original Arduino Zero design.

- ATSAMD21G18 32-bit/48MHz ARM Cortex-M0+
- 256KB Flash Memory
- 32KB SRAM
- 30 GPIO
- 14-channel 12-bit resolution ADC
- 1 10-bit resolution DAC
- 6 serial ports, any combination of UART, |I2C| and SPI (separate from the USB serial)
- 3 16-bit timer/counters
- 32-bit Real-Time Clock and Calendar
- 20 PWM capable outputs
- Full Speed USB device and embedded host capability

The appeal of the SAMD21 series is their relatively high performance, low cost and low power consumption.

.. note::
  A strong limitation however is that their GPIO are 3v3 compatible **only** and not 5v-tolerant like the STM32F4xx range. Another is an apparent bug in the USB CDC serial driver library code for the console, and lack of intent by Arduino to issue the fix we suggest. For these reasons whilst support is included, we are not pursuing this line as a long term support goal for now.


SAMD21G18 boards tested
-----------------------

So far, the Arduino Zero, SparkFun SAMD21 Dev Breakout, Sparkfun RedBoard Turbo, and SAMD21 M0 Mini (originally RobotDyn, but clones exist too) have been tested. The Arduino Zero, and both Sparkfun boards are more conveniently in the UNO R3 form factor:

.. image:: /_static/images/samd21/arduino_zero.jpeg
  :alt: Arduino Zero
  :scale: 12%

.. image:: /_static/images/samd21/samd21_dev_breakout.jpeg
  :alt: Sparkfun SAMD21 Dev Breakout
  :scale: 25%

.. image:: /_static/images/samd21/redboard_turbo.jpeg
  :alt: Sparkfun RedBoard Turbo
  :scale: 30%

.. image:: /_static/images/samd21/robotdyn_m0_mini.jpeg
  :alt: RobotDyn M0 Mini
  :scale: 25%

.. note::
  Please note that the barrel jack on the Sparkfun SAMD21 Dev Breakout is not fitted by the factory and the board itself **CANNOT handle more than 6VDC**. We strongly suggest you triple-check voltages before using this connector. It may give less scope for error to stick to powering the board via the Micro-USB connector for power. |BR| |BR| Note also that the |DCC-EX| EX-MotorShield8874's onboard regulator is by default set **too high** for the SAMD21 Dev Breakout at 7.2VDC. Adjustments to resistor R206 will be needed to lower the output to a safe 6V instead.

Dropped character on USB CDC fix
---------------------------------

The USB CDC driver code for Arduino SAMD core implementation seems broken as it is both slow and loses characters. This issue had already been reported to the Arduino SAMD GitHub pages as issue #538, and was then backed up with details from the DCC-EX dev team (https://github.com/arduino/ArduinoCore-samd/issues/538).

You will need to edit some code in the Arduino Core library for SAMD to fix this temporarily. Where the file to be fixed resides depends on the particular SAMD21 board you have, the OS and development environment you are using.

When running Arduino IDE: look for the file USBCore.cpp in one of these locations, in this case for the Arduino Zero:

- Windows: C:\\Users\\____\\AppData\\Local\\Arduino15\\packages\\arduino\\hardware\\samd\\1.8.13\\cores\\arduino\\USB\\USBCore.cpp
- MacOS: ~/Library/Arduino15/packages/arduino/hardware/samd/1.8.13/cores/arduino/USB/USBCore.cpp
- Linux: ~/.arduino15/packages/arduino/hardware/samd/1.8.13/cores/arduino/USB/USBCore.cpp

When running VS Code/PlatformIO: look for the file USBCore.cpp in one of these locations:

- Windows: C:\\Users\\____\\.platformio\\packages\\framework-arduino-samd\\cores\\arduino\\USB\\USBCore.cpp
- MacOS: ~/.platformio/packages/framework-arduino-samd/cores/arduino/USB/USBCore.cpp
- Linux: ~/.platformio/packages/framework-arduino-samd/cores/arduino/USB/USBCore.cpp

Look for the code shaded in dark blue, and replace it per the suggestion in light blue at the top (code for which is shown below for easy copy/paste):

.. image:: /_static/images/samd21/samd21_arduino_cdc_fix.jpeg
  :alt: Arduino SAMD21 Core CDC driver fix - replace this code

And replace it with:
::

  while (usbd.epBank1IsReady(ep) && !usbd.epBank1IsTransferComplete(ep)) {
  // optional timeout code here
  };

For boards such as the Sparfun SAMD21 Dev Breakout or Redboard Turbo, you will need to look in the Sparkfun directories for the appropriate USBCore.cpp file to alter, for example:

- For PlatformIO this is: .platformio/packages/framework-arduino-samd/cores/arduino/USB/USBCore.cpp
- For Arduino IDE this is: Arduino15/packages/SparkFun/hardware/samd/1.8.3/cores/arduino/USBCore.cpp

.. note::
  You will need to do this every time the SAMD Arduino core code is updated unless our fix has been incorporated. We will change our documentation to reflect is if/when it happens.
