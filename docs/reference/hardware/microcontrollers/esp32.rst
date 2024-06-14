.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst

|EX-CS-LOGO|

*******************
ESP32 (Recommended)
*******************

|tinkerer| |engineer| |support-button| |githublink-ex-commandstation-button2|

|NEW-IN-V5|

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:

Espressif ESP32 series
======================

Espressif have for some years now made impressive WiFi and Bluetooth capable microcontroller modules. DCC-EX has made use of their original ESP8266 offering as the means to provide WiFi capability to the EX-CS.

Espressif's newer ESP32 range has either WiFi alone or WiFi and Bluetooth capability built in. Espressif's product naming is not the easiest to follow, but DCC-EX has been ported to the original ESP32-WROOM-D0WD module, which has the following capabilities:

- Dual Xtensa 32-bit LX6 CPU cores
- 448KB of ROM for boot and core functions
- 520KB of RAM
- WiFi: 802.11b/g/n up to 150Mbps
- Bluetooth v4.2 BR/EDR and BLE
- WiFi STA mode and AP mode
- WiFi WPA/WPA2/WPA2-Enterprise/WPS support
- Encryption AES/RSA/ECC/SHA
- IPv4, IPv6, SSL, TCP/UDP/HTTP/FTP/MQTT
- Hardware interfaces: SD-card, UART, SPI, SDIO, |I2C|, LED PWM, Motor  PWM, I2S , IR, GPIO, capacitive touch sensor, ADC, DAC, Hall sensor, temperature sensor

The appeal of the ESP32 series is that they are very compact and come with WiFi capability built in. However, during porting to the ESP32-WROOM-32 we discovered they have some limitations, namely:

- WiFi is implemented in a blob of code from Espressif, which takes over interrupts, making DCC signal generation difficult
- To generate a clean DCC signal you need to program the special RMT hardware, normally used for IR remote controls
- Once we had done this, the DCC signal was very good

The port is currently in very active beta testing, and is for the most part very reliable. At present, the hardware modifications needed for the ESPduino32 and connectivity challenges with the various Devkit modules makes the hardware for tinkerers and engineers only.

.. note:: 
  DCC-EX can only run on the ESP32-WROOM-32 module, and none of the other ESP32 modules (S2, S3, C3 etc.) are supported at present. This is because other ESP32 modules do not have the necessary RMT hardware, or do not have enough such hardware to run DCC-EX.

ESP32-WROOM-32 boards tested
----------------------------

The ESP32 development boards that have been tested include the WeMos D1 R32/ESPDUINO-32, the GRobotronics ESP32 DEVKIT V1, the OLIMEX ESP32 DEVKIT LIPO, and the LILYGO® TTGO T-Energy T18 V3.0 ESP32-WROVER-E development board. Note that although the last one is an ESP32-WROVER-E board, not the WROOM, it does appear to work for one user, but more testing is required.

.. image:: /_static/images/esp32/espduino-32.jpg
  :alt: WeMos D1 R32/ESPDUINO-32 UNO form factor
  :scale: 25%

.. image:: /_static/images/esp32/grobotronics-esp32-devkit-v1.jpeg
  :alt: GRobotronics ESP32 DEVKIT V1
  :scale: 15%

.. image:: /_static/images/esp32/olimex-esp32-devkit-lipo.jpeg
  :alt: Olimex ESP32 Devkit LiPo
  :scale: 25%

.. image:: /_static/images/esp32/liligo-t18-v3-esp32-wrover.jpg
  :alt: LILYGO® TTGO T-Energy T18 V3.0 ESP32-WROVER-E
  :scale: 15%

WeMos D1 R32/ESPDUINO-32 board
------------------------------

The recommended hardware for now is the WeMos D1 R32, also referred to as the ESPDUINO-32.
This consists of an `ESP32-WROOM-32 <https://www.espressif.com/en/products/modules/esp32>`_ module mounted on a UNO form factor board with UNO R3 style connectors. Pictured here:

.. image:: /_static/images/esp32/espduino-32.jpg
  :alt: ESPDUINO-32 UNO form factor
  :scale: 50%

Sharing the same form factor as the Arduino UNO it can make use of the :doc:`Arduino Motor Shield R3 </reference/hardware/motorboards/arduino-motor-shield>` or the :doc:`Deek-Robot Motor Shield </reference/hardware/motorboards/deek-robot-motor-shield>`.
Note however that there are some hardware issues to be aware of, and to remedy before using this board.

It is a bit frustrating to find the following obvious hardware errors in popular boards like the ESPDUINO-32:

- Pullup voltage to the IO0 pin is too high (4.2v instead of 3.3-3.8v) which leads to unreliable WiFi!
- IOREF pin does **not** output 3v3, but instead breaches the UNO R3 specification and outputs 5V!
- A0 and A1 analog input pins for current sensing should not be used, as they cannot be used on ESP32-WROOM modules when using WiFi!

All these issues can be fixed with a soldering iron and/or a jumper but that's not what one expects from a released product.

Hardware setup notes for a WeMos D1 R32/ESPDUINO-32 |EX-CS|
-----------------------------------------------------------

To fix the IO0 pin voltage, install a resistor of between 250 to 300 Ohms between 3.3V and IO0 to pull it back down to 3.3V. This is easiest to do on the back side of the board, like so:

.. image:: /_static/images/esp32/espduino-32-resistor.jpg
  :alt: ESPDUINO-32 resister modification, underside of PCB
  :scale: 10%

From top to bottom the pins are: `IO0`, `5V` (incorrectly labelled `IOREF` on this board, so not Arduino UNO R3 compliant), `RESET`, `3.3V`, `5V`, `GND`, `GND`, `VIN` as seen here:

.. image:: /_static/images/esp32/espduino-32-header-closeup.jpg
  :alt: ESPDUINO-32 power header closeup, component side
  :scale: 10%


Using an Arduino Motor Shield R3 or clone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To avoid damaging the ESP32's analog inputs, the `IOREF` pin on must be bent outwards or cut so it will not go into the ESPDUINO-32 socket. Then use a jumper from the `3.3v` pin to `IOREF` on the motor shield itself.

For DCC current sensing bend or cut the `A0` and `A1` pins because by default they are connected to `GPIO2` and `GPIO4` on the ESP32 which are not useable at the same time as WiFi.
Instead, on the top of the Motor Shield connect `A0` to `A2` and `A1` to `A3` via jumpers. This will then automatically work when you select STANDARD_MOTOR_SHIELD as the MotorShield in config.h because the definition is in place when ESP32 is selected as the build target.

.. image:: /_static/images/esp32/espduino-32-motor-shield-fritzing.png
  :alt: MotorShield configuration for ESP32
  :scale: 50%

Using a |DCC-EX| EX-MotorShield8874
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To avoid damaging the ESP32's analog inputs, alter the IOREF jumper on the bottom of the EX-MotorShield8874 to take power from the 3v3 supply instead of IOREF as described in `Power Configuration PCB Jumpers <https://github.com/DCC-EX/EX-Hardware/tree/main/EX-Motorshield8874#power-configuration-pcb-jumpers>`_.

For DCC current sensing with the EX-MotorShield8874, use the alternate pin assignment jumpers for current sense to switch sensing to A2/A3 as described in `Alternate Pin Assignment PCB Jumpers <https://github.com/DCC-EX/EX-Hardware/tree/main/EX-Motorshield8874#aternate-pin-assignment-pcb-jumpers>`_. Once this is done, simply select EX8874 in config.h as your MotorShield.

Finally, the ESP32 needs more testing and development of a |DCC-EX| |I2C| non-blocking native driver implementation in particular. |I2C| peripheral performance will be limited until such time.

WeMos D1 R32/ESPDUINO-32 with Microsoft Windows - CH340 drivers
---------------------------------------------------------------

When using the WeMos D1 R32/ESPDUINO-32 board with Microsoft Windows, you will need to install the CH340 USB drivers in order to be able to upload software to it and use the serial monitor in either PlatformIO or the Arduino IDE.

Building DCC-EX for ESP32
-------------------------

The easiest way of building DCC-EX for the ESP32 is via EX-Installer by selecting the ESP32 option. Click here for :doc:`EX-Installer installation instructions </ex-commandstation/get-started/installer>`.

Adding ESP32 support to the Arduino IDE
----------------------------------------

In order to compile for the Espressif ESP32 platforms, you will need to add the board definitions to the Arduino IDE. To do this, follow the instructions on the `official Espressif guide <https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/installing.html#installing-using-arduino-ide>`_.

Adding ESP32 support to VS Code and PlatformIO
----------------------------------------------

When using VS Code and PlatformIO it will auto-configure from the entry in the platformio.ini file when you select the ESP32 target to be built.

.. note::
    The ESP32 board package version 2.0.0 or greater is required.

