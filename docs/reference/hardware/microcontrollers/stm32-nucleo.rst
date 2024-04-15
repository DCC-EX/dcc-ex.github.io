.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst

|EX-CS-LOGO|

***************************************
STMicroelectronics Nucleo (Recommended)
***************************************

|tinkerer| |engineer| |support-button| |githublink-ex-commandstation-button2|

|NEW-IN-V5|

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:

STMicroelectronics STM32 NUCLEO series
======================================

STMicroelectronics has a range of ARM based microcontrollers that are generally available, sold from reputable global resellers such as Digi-Key and Mouser, and have exceptional build quality for their price (often lower than clone Arduino Mega models, and presently lower than all genuine Arduino Mega prices.)

Further to this, the NUCLEO series of development boards also provide Arduino Uno compatible header sockets, meaning existing motor (and other) shields can just plug straight in, providing they are 3v3 compatible (see note above).

All of the NUCLEO series being considered as a future |DCC-EX| platform have a great deal more RAM (128KB to 256KB vs 8KB for a Mega), double or more FLASH (512KB to 2MB) for program storage, and much faster CPU speed (100 to 180Mhz vs 16Mhz) than the current AVR-based UNO and Mega.

With those attributes comes the potential to support much larger EX-RAIL scripts, more WiThrottle connections, and many new features.

NUCLEO-F411RE and NUCLEO-F446RE
-------------------------------

The majority of the current development work with the Nucleo series has been focused on the NUCLEO-F411RE as it most closely resembles the ubiquitous Arduino Uno form factor, including having Uno compatible header sockets in addition to Morpho pins for a much larger I/O capability than an Uno.

The F411RE has 50 I/O pins compared with the Uno's 20, and only 20 less than the Arduino Mega despite its diminutive size. For most use cases it is therefore a suitable substitute for a Mega.

There are larger NUCLEO footprints available (see below), which have many more pins than an Arduino Mega.

A good summary if the F411RE is available on the `arm MBED Nucleo-F411RE <https://os.mbed.com/platforms/st-nucleo-f411re/>`_ page.

The NUCLEO-F446RE is the same Nucleo-64 size as the F411RE, but with a faster processor and other features. As one of our more advanced early alpha test users has this board, it's now also supported as a build target for |DCC-EX| and being actively tested.

A good summary if the F446RE is available on the `arm MBED Nucleo-F446RE <https://os.mbed.com/platforms/st-nucleo-f446re/>`_ page.

Both the F411RE and F446RE are supported in the Arduino IDE.

NUCLEO-F412ZG, NUCLEO-F446ZE and NUCLEO-F429ZI
----------------------------------------------

These are three of the larger NUCLEO devices being tested in the Nucleo-144 form factor; the NUCLEO-F412ZG, NUCLEO-F446ZE and NUCLEO-F429ZI.

Each of these has a larger footprint than the Nucleo-64 series, while still retaining the Uno compatible header sockets, with 114 I/O pins. That said, they are only slightly larger (20mm wider, 33mm longer) than an Arduino Mega 2560.

The F412ZG is potentially suitable as a larger replacement for a Mega, with more I/O pins available, refer to the `arm MBED F412ZG <https://os.mbed.com/platforms/ST-Nucleo-F412ZG/>`_ page.

The F446ZE has the same large footprint, however it has a significantly faster CPU and a USB OTG port. Refer to the `arm MBED F446ZE <https://os.mbed.com/platforms/ST-Nucleo-F446ZE/>`_ page.

The F429ZI has the same large footprint, however it has the added benefit of onboard Ethernet, which makes it potentially suitable for larger or exhibition layouts where the WiFi limitations of the ESP01 firmware come in to play. Note, however, that the Ethernet support for this board in |EX-CS| is currently not implemented. It too has a USB OTG port. Refer to the `arm MBED F429ZI <https://os.mbed.com/platforms/ST-Nucleo-F429ZI/>`_ page.

.. note:: 

  While the F429ZI is supported by the Arduino IDE, the F412ZG and F446ZE cannot be selected as build targets from within the Arduino IDE at present, and you will need to request the variant files and get some support from the |DCC-EX| dev team via Discord. The plan is to submit the F412ZG and F446ZE variant files to the STM32duino GitHub repo for inclusion once they are validated and debugged.

Install the STLink drivers for Windows
--------------------------------------

When using any of the NUCLEO series microcontrollers with Microsoft Windows, you will need to install their STLink USB drivers in order to be able to upload software to them and use the serial monitor in either PlatformIO or the Arduino IDE.

.. note:: 

  You should install these drivers before plugging your NUCLEO device in for the first time.

As per STMicroelectronics' software licensing policy, we have been able to host a local copy of these drivers and firmware upgrade software which also includes the license agreement that you are agreeing to when you download the software.

You can obtain the zip file containing these from our website here:

.. rst-class:: dcclink

  `Nucleo USB drivers and diagnostic firmware <../../../_static/files/nucleo/st_micro_nucleo_drivers.zip>`_

Once you download and extract this zip file, you will need to install the STLink drivers located in the "en.stsw-linik009" folder.

.. image:: /_static/images/nucleo/driver-folder.png
  :alt: STLink driver folder
  :scale: 30%

Right click the "stlink_winusb_install.bat" file and select "Run as administrator". You will need to click "Yes" to allow it to make changes to your computer.

.. image:: /_static/images/nucleo/driver-install1.png
  :alt: Run as admin
  :scale: 50%

Click "Next" to install the drivers, and you should see this summary screen to confirm the drivers installed successfully:

.. image:: /_static/images/nucleo/driver-install2.png
  :alt: Drivers installed
  :scale: 50%

You can now plug your NUCLEO device in and proceed with upgrading the debugger firmware (highly recommended).

Upgrade the debugger firmware
-----------------------------

During testing, it was noted with certain USB chipsets on Windows 11 that serial responses via the USB debugger port would stop being received by the serial monitor, even though the device continued to operate normally. The recommendation to resolve this issue is to upgrade the debugger firmware.

We recommend you upgrade the debugger firmware regardless if you experience this issue or not.

You need to ensure your NUCLEO device is plugged in to a USB port prior to commencing the upgrade.

In the same zip file as the drivers, you will need to navigate through the "en.stsw-link007_v3-10-3" folder down to the "Windows" folder, which contains an executable "ST-LinkUpgrade.exe" to upgrade the firmware on the NUCLEO devices.

.. image:: /_static/images/nucleo/extracted-firmware.png
  :alt: Drivers installed
  :scale: 50%

Double click this file to run it, which should present the upgrade window.

.. image:: /_static/images/nucleo/firmware1.png
  :alt: Drivers installed
  :scale: 50%

Clicking the "Device Connect" button will attempt to connect to your NUCLEO device and display the currently installed firmware version, along with the version it will attempt to upgrade to.

.. image:: /_static/images/nucleo/firmware2.png
  :alt: Drivers installed
  :scale: 50%

Providing your NUCLEO device has been detected and is running an older version of the firmware, click "Yes >>>>" to proceed with the upgrade.

.. image:: /_static/images/nucleo/firmware3.png
  :alt: Drivers installed
  :scale: 50%

Hopefully you will see the "Upgrade is successful" pop up appear when complete.

.. image:: /_static/images/nucleo/firmware4.png
  :alt: Drivers installed
  :scale: 50%

At this point, after clicking "OK" the software should display the new version of the firmware that has been applied to your device.

.. image:: /_static/images/nucleo/firmware5.png
  :alt: Drivers installed
  :scale: 50%

Adding NUCLEO support to the Arduino IDE
----------------------------------------

In order to compile for the STM32 NUCLEO platforms, you will need to add the boards to the Arduino IDE.

To do this, navigate to "File" -> "Preferences" and add this URL to the "Additional Boards Manager URLs" list:

`<https://github.com/stm32duino/BoardManagerFiles/raw/main/package_stmicroelectronics_index.json>`_

.. image:: /_static/images/nucleo/arduino-support.png
  :alt: Arduino IDE Preferences
  :scale: 50%

You will then need to navigate to "Tools" -> "Board" -> "Boards Manager", search for "stm32", and install the support for these boards.

.. image:: /_static/images/nucleo/arduino-install-stm32.png
  :alt: Arduino STM32 board install
  :scale: 50%

Once this has been performed, the NUCLEO devices should be available to be selected in the Arduino IDE.

Adding NUCLEO support to VS Code/PlatformIO
-------------------------------------------

In order to compile for the STM32 NUCLEO platforms you need do nothing when using Microsoft VS Code and PlatformIO. PlatformIO will automatically download the required tool chains and frameworks for platform support based on the entries in platformio.ini included in the |EX-CS| source tree.

Just select "Nucleo-F411RE" or "Nucleo-F446RE" as the build target, and hit build. Be sure to do this after installing the drivers (for Windows) and upgrading the debugger firmware per the instructions above.

Hardware setup notes for a NUCLEO |EX-CS|
-----------------------------------------

Here is how the NUCLEO-F411RE looks when new, with a top view, and the pinouts. The NUCLEO-F446RE board looks near identical, pinouts are exactly the same, however some of their I/O functions map slightly differently as the F411RE and F446RE microcontrollers are different internally.

.. image:: /_static/images/nucleo/nucleo-f411re-top.png
  :alt: STM Nucleo-F411RE top face
  :scale: 25%

.. image:: /_static/images/nucleo/nucleo-f411re-pinout.png
  :alt: STM Nucleo-F411RE connector pinouts
  :scale: 50%

You will notice that the Ardiuno connectors are slightly inboard of the dual-row headers called the Morpho connectors.

Notes on the Arduino connectors on the NUCLEO range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Whilst the I/O pins are 5v-tolerant for digital IO, for the moment we recommend using 3v3 friendly Arduino R3 spec shields where you can.
- The analog pins are NOT 5v-tolerant and accept a maximum of 3v3. We recommend using the new EX-MotorShield8874, or a genuine Ardiuno Motor Shield R3 revision (and only the R3!) for the moment. Instructions for modifying the earlier R2 version and the Deek Robot Motor Shield will follow in due course.
- By default the Rx/Tx Arduino pins (D0/D1) are NOT connected to any of the NUCLEO's pins. There are jumpers underneath to connect them to Serial2, but this isn't recommended (see steps for serial connections below)
- The Morpho pins extend both above AND below the Nucleo-64 series boards! Please be very wary of shorting any of these pins, especially those that protrude below. We recommend mounting 10mm M3 screw hex standoffs into the 3 mounting holes on the main PCB for your safety. See pic here:

.. image:: /_static/images/nucleo/nucleo-f411re-bottom-spacers.png
  :alt: STM Nucleo-F411RE underneath face with 10mm M3 standoffs
  :scale: 25%


Here is the NUCLEO-F411RE with on the left a genuine Arduino Motor Shield R3 installed, and on the right a |DCC-EX| EX-MotorShield8874 installed:

.. image:: /_static/images/nucleo/nucleo-f411re-with-motor-shield.png
  :alt: STM Nucleo-F411RE with genuine Arduino Motor Shield R3 installed
  :scale: 30%

.. image:: /_static/images/motorboards/ex_motorshield8874_nucleo_f411.jpg
  :alt: STM Nucleo-F411RE with DCC-EX EX-MotorShield8874 installed
  :scale: 17%

Notes on using the EX-MotorShield8874 with Nucleo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to take advantage of the EX-MotorShield8874's single power source capability, you will need to move the Nucleo jumper JP5 from the U5V position (pins 1+2 jumpered, USB 5V source being used) to the E5V position (pins 2+3 jumpered).

This will power your Nucleo-64 unit using the EX-MotorShield8874's onboard switch mode power supply of 7.2V to the VIN pin, and allows some 800mA of 5V power to be available for the Nucleo and peripherals.

NB: once you do this it will mean you need both the EX-MotorShield8874 barrel jack to be powered AND the USB cable to enable programming. Or you can temporarily move JP5 back to U5V whilst uploading |EX-CS|.

Serial for WiFi, for F411RE and F446RE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To connect an ESP8266 via either a WiFi shield or ESP01 module, you may use any of the available serial ports, which appear on different Morpho pins for the F411RE and F446RE.

The |EX-CS| source code currently maps the first additional serial port pins to:

- F411RE: Rx/PA15 on CN7 pin 17, Tx/PB7 on CN7 pin 21 - known as Serial1
- F446RE: Rx/PC11 on CN7 pin 2, Tx/PC10 on CN7 pin 1 - known as Serial3

Also defined in |EX-CS| is an additional serial port which appears on the following pins:

- F411RE Rx CN10 PA12 pin 12, Tx CN10 PA11 pin 13 - known as Serial6
- F446RE Rx CN7 PD2 pin 4, Tx CN7 PC12 pin 3 - known as Serial5

You will need to select a serial port to use, and connect the Rx pin on your NUCLEO to the Tx pin of your WiFi device, and the Tx pin of the NUCLEO to the Rx pin of the WiFi device. We recommend using Serial1 for the F411RE and Serial3 for F446RE. Below are pics of the positions of all available mapped serial ports:

.. image:: /_static/images/nucleo/nucleo-f411re-f446re-wifi-serial1.png
  :alt: NUCLEO F411RE/F446RE Serial1 Rx/Tx Connections
  :scale: 50%

NB: The default serial port used for console communications for the F411RE and F446RE is Serial2, which is not connected to the Arduino Rx/Tx pins of D0/D1. Because the D0/D1 pads on the F411RE and F446RE are completely unconnected, you can happily jumper your chosen WiFi serial port pins above to D0/D1 with dupont connectors or permanently soldered wires.

