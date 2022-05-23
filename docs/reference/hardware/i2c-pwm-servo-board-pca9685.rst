****************************
PCA9685 I²C PWM Servo Board
****************************

The PCA9685 chip is a 16-Channel 12-Bit PWM Servo (and LED) Driver and expands 
the PWM output pins. It depends on I²C communication and brings you 16 additional 
PWM pins you can use for LED and SERVO, but also as General Purpose Output.

.. sidebar:: On this page

   .. contents:: 
      :depth: 2
      :local:

PCA PWM modules
================
The PCA9685 is a extender module that has 16 pins capable of Pulse Width 
Modulation. It can drive servos and leds, but also can be used for more generic
purposes like driving a digital output or switching some external hardware.

.. image:: ../../_static/images/i2c/pca9685_1.jpg
    :alt: PCA9685 Module with Gravity connector
    :scale: 50%
    :class: no-scaled-link

.. image:: ../../_static/images/i2c/pca9685_2.jpg
    :alt: PCA9685 Module with Groove connector
    :scale: 50%
    :class: no-scaled-link

.. image:: ../../_static/images/i2c/pca9685_keyestudio.jpg
    :alt: PCA9685 Module 
    :scale: 50%
    :class: no-scaled-link

Each module has an address associated with it, which will be 
in the range from 0x40 to 0x47. By default, the module is 
usually 0x40. If using more then 1 module, the address **must** 
be changed to prevent conflicts , usually by moving jumpers on 
the module or by soldering across pads on the circuit board. 
Refer to the documentation for your own board for details.

.. seealso:: The address settings can be found in the :ref:`PCA9685 address table`.

Expander wiring examples
_________________________

Both diagrams show a , and a LED (2-pin) connected to GPIO 1.
In these examples the PCA9685 is connected to an Arduino Mega.

.. image:: ../../_static/images/i2c/ArduinoMega_PCA9685.png
    :alt: Diagram: Arduino Mega, PCA9685 Expansion Board with SERVO and LED
    :height: 400px

.. image:: ../../_static/images/i2c/ArduinoMega_PCA9685_breadboard.png
    :alt: Diagram: Arduino Mega, PCA9685 IC with Servo and LED
    :height: 400px

When used for inputs (sensors or switches), the sensor/switch is usually
connected between the nominated pin and the GND (ground) signal. When
the sensor/switch activates, it connects the pin to GND, and the device
detects a small current flow. When the sensor/switch deactivates, the
current stops flowing. This behaviour is the same as with the Arduino
digital GPIO pins

PWM use in EXRAIL
___________________
As long as the predefined PCA9685 boards are used, there is no extra setup
needed to use them as sensor/input or output within EXRAIL.

Outputs in EX-RAIL
^^^^^^^^^^^^^^^^^^^^
An output may be connected at vPIN165 (PCA9685 second pin). That can be
utilized in EXRAIL as follows:

.. code-block:: C

   SET(198)   // Set output pin HIGH
   RESET(199) // Zero an output pin

Turnouts in EX-RAIL
^^^^^^^^^^^^^^^^^^^^
If a pin is used as Turnout, it needs to be setup in EXRAIL as follows:

.. code-block:: C
   
   PIN_TURNOUT(26, 199) // ID:26 | vPIN:199 | optional description
   PIN_TURNOUT(202,202, "Coleyard") // ID == vPIN:202 > preferred

This code defines a turnout with ID 26 connected to vPIN 234 and another 
turnout were the ID is equal to the vPin.

.. code-block:: C
   
   THROW(26) // Throw the turnout with ID:26 | vPIN:199
   CLOSE(26) // Close the turnout with ID:26 | vPIN:199
   THROW(202)// Throw the turnout ID:202


.. warning:: Please take in account that the pin stays high, therefor not suitable for all turnout drivers!!

.. 
   .. code-block:: C
      
      /**********************************************
          HOW TO SETUP TWIN COIL TURNOUTS (PULSED)  
      **********************************************/
      VIRTUAL_TURNOUT(2233,"description")
      
      // THROW 1st COIL for TURNOUT
      ONTHROW(2233) 
         SET(166) 
         DELAY(150) // pulse length 150ms
         UNSET(166) 
      DONE
      // THROW 2nd COIL for STRAIGHT
      ONCLOSE(2233) 
         SET(167) 
         DELAY(150) // pulse length 150ms
         UNSET(167)
      DONE


 .. 
    .. see-also:: EX-RAIL cookbook example 




Signals in EX-RAIL
^^^^^^^^^^^^^^^^^^^
A set of 2 or 3 pins can be used as signal. Setup in EXRAIL as follows:

.. code-block:: C

   SIGNAL(198, 199, 200) // Define a signal(Red, Amber, Green). Red is signal ID
   SIGNAL(202, 0, 203)   // Define a 2 aspect signal(Red and Green)

The first command defines a 3 aspect signal (Red, Amber, Green) with ID 230 connected 
to vPIN 198, 199, 200. The second command defines a 2 aspect signal (Red and Green). 
The first value equals RED and is always the ID of the defined signal.

.. code-block:: C

   GREEN(198) // Set defined signal green
   AMBER(198) // Set defined signal to amber
   RED(198)   // Set defined signal to red


Setup with Serial Monitor or JMRI console
___________________________________________ 
The Serial Monitor in the Arduino IDE can be used to setup, test and configure I/O 
connected to the DCC-EX Command Station. 

This can also be achieved from within JMRI. There is a tool called JMRI console. In 
the next section where it states "serial monitor" you may also read "JMRI console".


Setup inputs in serial monitor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
An input pin may be configured using the DCC++ EX Sensor commands, as
follows:

.. code-block::
   
   <S 1096 196 1> // ID:1096 | vPIN:196 | Pull up:enabled
   <S 197 197 1>  // ID == vPIN:197    | Pull up:enabled

The first command associates sensor ID 1096 with vPIN 196 and enables the pull up 
resistor. The second one does the same, but ID is equal to vPIN (preferred).

When the sensor activates and deactivates, the following messages are
sent by DCC++ EX over the serial output:

.. code-block::

   <Q 1096> // Activation
   <q 1096> // Deactivation

Setup outputs in serial monitor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An output pin may be configured using the DCC++ EX Output commands, as
follows:

.. code-block::

   <Z 1098 198 1> // ID:1098 | vPin:198 | Pull up:enabled
   <Z 199 199 1> // ID == vPin:199 | Pull up:enabled

The first command associates output ID 2030 with vPIN 230 and enables the pull up 
resistor. The second one does the same, but ID is equal to vPIN (preferred).

After setup, the outputs can be tested with following commands:
.. code-block::

   <Z 1098 1> // command to activate output
   <Z 1098 0> // deactivate to deactivate output

When the output activates and deactivates, the following messages are
sent by DCC++ EX over the serial output:

.. code-block::
   
   <Y 1098 1> -- Activated
   <Y 1098 0> -- Deactivated

Setup turnouts in serial monitor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. 
   Output::create(198, 198, 0);
   Output::create(199, 199, 0);
   Output::create(202, 202, 1);
   Output::create(203, 203, 1);

An output pin may be configured using the DCC++ EX Turnout commands, as
follows:
.. code-block::
   
   <T 3198 VPIN 198> // ID:3198 | vPin:198

This command associates turnout ID 26 with VPIN 166 (PCA9685 third pin)
and enables pullup.

.. code-block::
   
   <T 3198 1> // throw
   <T 3198 0> // close

When the output activates and deactivates, the following messages are
sent by DCC++ EX over the serial output:

.. code-block::

   <H 3198 1> -- Activation
   <H 3198 0> -- Deactivation

.. _configuring pca9685 via myHal.cpp:

Configure the modules in **myHAL.cpp**
________________________________________________

Setup and configure extra PCA9685 modules is done in the file *myHal.cpp*.
If the file is not present in the Commandstation-EX folder, create the file 
or rename *myHal.cpp_example.txt*. 

In DCC-EX, two PCA9685 modules are pre-configured: 

   #. Address **0x20** configured with VPINs **164-179** 
   #. Address **0x21** configured with VPINs **180-195**

.. NOTE:: To avoid conflicts with preconfigured I²C modules, both address and pin range must be different.

In the next example, we will add a third PCA9685 module with address 0x22 wih vpins 196-211

.. code-block:: C

   #include "IODevice.h"    // Always required when defining I/O
   #include "Turnouts.h"    // Needed for driving turnouts
   #include "Sensors.h"     // Needed for Input / Sensors
   #include "Outputs.h"     // Needed for Outputs
   #include "IO_PCA9685.h" // PCA9685 specific routines
   // =========================================================
   //  Define a PCA9685 16-port I²C GPIO Extender module.
   // =========================================================
   //              First Vpin=196
   //                │  Number of VPINs=16 (numbered 196-211)
   //                │    │  I²C address of module=0x22
   //                │    │   │
   //                V    V   V
   PCA9685::create(196, 16, 0x22);
   // ======================================================
   //  Define a PCA9685 16-port I²C GPIO Extender module
   //  with an interrupt pin. Pull down to request a scan.
   //        Multiple modules can share same pin.
   //                   First Vpin=212
   //                    │  Number of VPINs=16 (numbered 212-227)
   //                    │    │  I²C address of module=0x23
   //                    │    │   │  Interrupt pin
   //                    │    │   │    │
   //                    V    V   V    V
   // PCA9685::create(212, 16, 0x23, 40);

   void mySetup() {
   // =========================================================
   // Create individual inputs/sensors
   //  NOTE: Does not apply to EXRAIL
   // =========================================================
   //             ID for the input/sensor
   //              │   Vpin
   //              │    │  PullUp 1=on|0=off
   //              │    │   │
   //              V    V   V
   Sensor::create(196, 196, 0);
   Sensor::create(197, 197, 0);
   Sensor::create(200, 200, 1);
   Sensor::create(201, 201, 1);
   // =========================================================
   // Create individual outputs
   //  NOTE: Does not apply to EXRAIL
   // =========================================================
   //             ID for the output
   //              │   Vpin
   //              │    │  PullUp 1=on|0=off
   //              │    │   │
   //              V    V   V
   Output::create(198, 198, 0);
   Output::create(199, 199, 0);
   Output::create(202, 202, 1);
   Output::create(203, 203, 1);
   }

.. _PCA9685 address table:

I²C Address table
___________________

======= === === ===
Address A2  A1  A0
0x40    OFF OFF OFF
0x41    OFF OFF ON
0x42    OFF ON  OFF
0x43    OFF ON  ON
0x44    ON  OFF OFF
0x45    ON  OFF ON
0x46    ON  ON  OFF
0x47    ON  ON  ON
======= === === ===

Specifications & Features
___________________________

- 16-bit remote bidirectional I/O port
   - I/O pins default to input
- Up to 8 devices on the bus (max. 128 additional GOPIO pins)
- Interrupt output pins, configurable as:
      - Active-high,
      - Active-low
      - Open-drain
- High-speed i2c interface:
   - 100kHz / 400kHz / 1.7MHz
- Nominal current per GPIO pin
   - Inputs: ±20mA (max. 25mA)
   - Outputs: ±20mA (max. 25mA)
- Low standby current: 1 μA (max.)
- IntA and IntB can be configured to operate independently or together
- Configurable interrupt source:
   - Interrupt-on-change from configured register defaults or pin changes
- External reset input


IC Packages & Pin Out
_______________________
- 28-pin SOIC, Wide, 7.50mm body
- 28-pin SPDIP, 300 mil body
- 28-pin SSOP, 5.30mm body
- 28-pin QFN, 6mm x 6mm body 


.. image:: ../../_static/images/i2c/pca9685_packages.png
    :alt: PCA9685 Packages information
    :class: no-scaled-link
    

Datasheet 
___________

NXP:
https://www.nxp.com/docs/en/data-sheet/PCA9685.pdf

