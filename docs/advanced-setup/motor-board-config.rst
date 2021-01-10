Motor Board Selection
======================

This section is for Tinkerer's and Engineers.

DCC++ EX supports many different motor boards, you can select any of the pre-configured boards simply by choosing them from the motor board dropdown list in the installer, or by adding them with one line in your config.h file. If your board is not supported, these instructions will show you how to add it.

.. note:: DCC-EX does NOT require the transistor mixer/inverter circuit seen in many tutorials for boards like the L298N and IBT_2 that have separate PWM inputs, use another GPIO pin on the Arduino and connect directly to these boards

**Links in This Page**

* :ref:`Configure Using the Installer`
* :ref:`Configure By Editing the config.h File`
* :ref:`Your Board is in the Supported List`
* :ref:`Your Board is NOT in the Supported List`
* :ref:`Current Sense and Sense Factor`
* :ref:`Just Buy a Current Sense Board Instead`

Configure Using the Installer
-------------------------------

Tinkerers and even Conductors should be comfortable with this option. If you are using the installer, just select your board from the motor board drop down list. Make sure your other selections are correct, and then simply upload the changes to your Command Station. 

Configure By Editing the config.h File
----------------------------------------

Using the Arduino IDE, PlatformIO, or any other method for editing a file and uploading a sketch, you can add your motor board by editing the config.h file. Click here for a list of `Currently supported boards <../reference/hardware/motor-boards.html>`_

Open the config.h file in your editor. If this is the first time configuring your system, you may need to copy the "config.example.h" file and name the copy "config.h".

Find this section in the file:

.. code-block:: cpp

  // DEFINE MOTOR_SHIELD_TYPE BELOW ACCORDING TO THE FOLLOWING TABLE:
  //
  //  STANDARD_MOTOR_SHIELD : Arduino Motor shield Rev3 based on the L298 with max 18V 2A per channel
  //  POLOLU_MOTOR_SHIELD   : Pololu MC33926 Motor Driver (not recommended for prog track)
  //  FUNDUMOTO_SHIELD      : Fundumoto Shield, no current sensing (not recommended, no short protection)
  //  FIREBOX_MK1           : The Firebox MK1                    
  //  FIREBOX_MK1S          : The Firebox MK1S    
  //   |
  //   +-----------------------
  //
  #define MOTOR_SHIELD_TYPE STANDARD_MOTOR_SHIELD

You will see a list of supported boards with their type and the "STANDARD_MOTOR_SHIELD" defined as the default. Continue below.

Your Board is in the Supported List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This option is possibly Conductor friendly for those just choosing a supported board that requires no wiring.

.. note:: The Arduino Motor Shield, Deek-Robot Motor Shield, DIY More Motor Shield and any other shield or board that is 100% compatible with the Arduino Motor Shield is defined as a "STANDARD_MOTOR_SHIELD"

To select your board, just change the #define line to the type for your board. The following line configures a Pololu Motor Shield. We just copy and paste its name over the STANDARD_MOTOR_SHIELD::

 #define MOTOR_SHIELD_TYPE POLOLU_MOTOR_SHIELD

That's all you need to do. Make your change and then upload the sketch to your Arduino.

.. Note:: If your board is not a shield that plugs onto your Arduino, then you are going to have to run jumper wires. An IBT_2 High Current Motor Board is an example of such a board. See the section on your board for installation help.

Your board is NOT in the Supported List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tinkerer or Engineer level may be required with this option.

If your board is not in the list (remember many boards are considered a "STANDARD_MOTOR_SHIELD"), you can easily add it. In your config.h file, find the line that looks like this::

  #define MOTOR_SHIELD_TYPE STANDARD_MOTOR_SHIELD

We are going to replace this with a new motor board definition and select it. Comment out the above line and replace it with something that looks like this:

.. code-block:: cpp

  #define MY_MOTOR_SHIELD F("MY_MOTOR_SHIELD"),\
     new MotorDriver(11, 13, UNUSED_PIN, UNUSED_PIN, A1, 2.99, 2000, UNUSED_PIN), \
     new MotorDriver(3, 12, UNUSED_PIN, UNUSED_PIN, A0, 2.99, 2000, UNUSED_PIN)
  #define MOTOR_SHIELD_TYPE MY_MOTOR_SHIELD

1. Replace "MY_MOTOR_SHIELD" in both instances with whatever name you like or just leave it as MY_MOTOR_SHIELD.

2. The first "new MotorDriver()" line defines your programming track, the second one is for your main track

3. The format of the MotorDriver code is:

   .. code-block:: cpp

     MotorDriver(power_pin, signal_pin, signal_pin2, brake_pin, current_pin, senseFactor, tripMilliamps, faultPin)

4. Enter the appropriate pin numbers on the Arduino you will connect to your motor board.

Let's look at the details of how this works, first here are all the configuration options:

* **power_pin** - This goes to the EN (enable pin) of the motor board, it turns power on and off
* **signal_pin** - This is the pin that outputs the DCC signal and goes to the PWM input of the motor board. For boards that combine the signal into one pin, like the Arduino Motor Shield, you just need to enter the pin here and connect it to the single PWM pin on the motor board.
* **signal_pin2** - If your motor board has a "left" and "right" or "CW" and "CCW" input, then this is the pin on the Arduino you want to use to output this half of the signal. The other half comes from the signal_pin mentioned above. If not used, it must be left set to "UNUSED_PIN".
* **brake_pin** - If you were going to use the braking feature (for example to use a Railcom cutout), and have NOT cut the trace for this if one exists for your motor board, then you would enter this pin here. If not used, leave it set to "UNUSED_PIN".
* **sense_pin** - This is the analog input pin on the Arduino that will get current sense information from the motor board. The programming track CS usually connects to A1 and main to A0. Important information about current sense is below.
* **tripMilliamps** - This is the value for what current in mA will trip the overcurrent protection.
* **senseFactor** - This is the multiplier specific to your board or current sense circuit that converts the raw reading into track current in milliAmps. Important information about current sense is below.
* **faultPin** - Some boards can report a fault condition, for example under-voltage or over-heating. If you want this feature, you can the Arduino digital pin here and connect it to the fault output of the motor board.

Current Sense and Sense factor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: It is VERY imortant to connect some form of current sensing, without it, you cannot program decoders on the programming track and you will not have any short circuit protection on either track!

Current sense is actually a voltage output by the motor board that is proportional to the current being delivered to the track. While you are running trains on your MAIN track, the CS is constantly monitoring the current so that we can shut off power to the track in case of a short circuit. Programs like JMRI have a dashboard that can report how much current you are using in real-time.

The PROG track requires current sense to detect the current pulse back from decoders to ACKnowledge the receipt of your command. The DCC specification says that a decoder must send a short 60mA (60 milliAmps) or more current pulse to the programming track for at least 6ms (6 milliseconds). You may still be able to have the decoder accept a command if current sense is not working, just as you would for POM (programming on main), but you will receive no acknowledgement from the loco and you will have no way to read CVs.

.. note:: The DCC-EX team may be able to help you find the correct settings for your board. However, this may stil require you to be at our "Engineer Level" to feel comfortable going further in this section.

In order to calculate the current, we need to know the "Volts per Amp" reported by the motor board current sense circuit. For example, the Arduino Motor Shield, using the L298 dual H-Bridge, has a special circuit that gives us 1.65V/A (1.65 Volts per Amp) reported. In theory, that means this board would send 1.65V to our Arduino analog sense pin when 1A of current was flowing from the motor board. When 2A was flowing, we should see 3.3V on our sense pin.

The Arduino has an ADC (Analog to digital converter) that reads this analog voltage, samples it, and convers it to a digital reading. Ardunio pins have a 10bit resolution, that means it can hold a maximum value of 1024 with current expressed as a number from 0 to 1023. Therefore, we need a senseFactor constant to help us convert the raw Arduino pin reading to a current in milliAmps. Here is the formula we use to find this constant for a particular motor board:

.. code-block:: cpp

  senseFactor = ((5/1024)/Board Volts/Amp)*1000

The Arduno analog pin can go from 0 to 5V and has 1024 possible levels, so we divide 5 by 1024, then divide by the V/A figure from the motor board current sense output, then multiply it by 1000 to make the number easier to work with. From our example of the Arduino motor shield above and its published 1.65V/A, we can compute the senseFactor as follows:

.. code-block:: cpp

  senseFactor = ((5/1024)/1.65)*1000 = 2.96

You may notice that we actually use 2.99 in our code. You caught us! Through experimentation and measurment, we tweak these values to be more accurate. Nothing is ever 100% as reported in a data sheet.

We use the senseFactor to calculate our current in milliAmps by just taking a raw pin reading and multiplying it by this current senseFactor. Again using the Arduino Motor Shield values, if we got a reading of 300 (out of a possible value between 0 and 1023), that would be 300 * 2.99 or about 897mA.

You will also note that if you have the maximum of 2A flowing for this board (2000mA), that the pin reading will only be around 669. That isn't very close to 1023. That is because the Arduino Motor Shield actually only reports its maximum current of 2 Amps as 3.3V, not 5. That would let you use a 3.3V microcontroller with this motor shield.

Many of the stand-alone (discrete) motor boards like the L298N or IBT_2 require a current sense resitor connected between the CS pin on the motor board and ground. This creates a voltage we can read by then connecting the pin to our CS analog pin (usually A0 or A1). This resistor needs to be very small, usually .15 to .25 ohms. We don't want a large voltage drop taking power away from our track (E = I * R so 2 Amps at 1 Ohm would drop 2 Volts!). We also don't want to have to have a huge resistor (P = I * E, so 2V drop in the resistor times 2 Amps of current is 4 Watts!). But, you say, if the Arduino Motor Shield uses only a .15 Ohm resistor, that's only a voltage reading of 0 to .3 volts (.15 Ohms * 2 Amps). That is a very low reading for the Arduino to read! And that is why the motor shield has an op amp circuit that multiplies this voltage by 11 to bring it up to 3.3 Volts and put it in a range that an Arduino can read.

.. warning:: Choose your current sense resistor or circuit carefully, you need to account for all of the factors mentioned above and you do not want to apply more than 5 Volts to any pin on an Arduino! (Be even more careful if you are using a 3.3V board).

How Do I Find Volts per Amp?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In some cases, the datasheet for your motor shield will list it. If the board or chip only provides a raw output, you are going to have to figure it out using Ohm's law. For a board like the IBT_2 that can handle 30 or more Amps, you are going to have to choose a useful range and design your current sense circuit to handle that range. We recommend using no more than 5 Amps on your main track. If you need more than 5 Amps, you need separate power districts and separate boosters. Be sure to set your motor board tripCurrent value to 5000, and be sure that the voltage from your motor board sense resistor/circuit does not exceed the Arduino pin input of 5V.

Just Buy a Current Sense Board Instead
---------------------------------------

Tinkerers and Conductors who don't mind connecting a few jumper wires may like this option.

This saves a lot of time and hassle (not to mention math), and also brings things into the realm of Tinkerer rather than just an Engineer. You also have the added benefit that the same current sense board can be used with lots of different motor boards. Many of these boards have a very simple current conversion factor because they output 1 Volt for 1 Amp! While discontinued, you can still find MAX471 boards.

*** Connection Instructions coming soon ***



