.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: EX-CommandStation Command Station diagnosing Issues Troubleshooting

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

***************
Troubleshooting
***************

|conductor| 

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

In this section, you will find some tips on troubleshooting the various issues encountered with |EX-CS|.

If you have just assembled your |EX-CS| and it is not working as expected, we recommend you start with the :doc:`/support/ex-cs-diagnose` page.

----

Troubleshooting tips
====================

Cannot drive a locomotive
-------------------------

.. list-table:: 
  :widths: 30 70
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes

  * - Locomotive doesn't respond to throttle settings
    - (a) Track power has not been turned on - Issue ``<1>`` in the serial console, or use the :guilabel:`Power` button in |Engine Driver| or |JMRI|.
      (b) Locomotive is on the PROGRAMMING track - Issue ``<1 JOIN>`` in the serial console, or use the :guilabel:`Request Loco ID` button in |Engine Driver|.
      (c) Power has not been supplied to the motor board - Check to ensure power supply is connected securely witht the correct polarity, is plugged in at the wall, and turned on.

Cannot connect to the EX-CommandStation over WiFi
-------------------------------------------------

.. list-table:: 
  :widths: 30 70
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes
      
  * - CommandStation does not appear in the available WiThrottle server list in |Engine Driver| or |wiThrottle| apps.
      
      Manually entering the expected IP address and port does not successfully connect
      
    - (a) CommandStation is configured for Access Point mode, but |Engine Driver| or |wiThrottle| device is connected to a different WiFi network - Connect the device directly the CommandStation's WiFi network
      (b) CommandStation is configured for Station Mode and connects to the WiFi network, but |Engine Driver| or |wiThrottle| device is connected to a different WiFi network - Connect the device to the correct WiFi network
      (c) WifI shield is connected incorrectly to the CommandStation - The Rx pin of the WiFi shield must connect to the Tx pin on the CommandStation, and Tx to the Rx pin

Diagnostics
===========

Is it Plugged In, Is it Turned On?
----------------------------------

Yes, we need to start with the basics. If you have 12V DC or less connected to the input power of the Arduino and did not cut the power connect trace underneath the Motor Controller, then the Motor Controller and the Arduino can be powered from the one power supply connected to the barrel jack of the Motor Shield. If you cut the trace (which we highly recommend), then you will need two power supplies, a 7-9V DC power supply to the Arduino and a 12-18V DC (based on the scale of your locomotives) power supply for the Motor Controller.

* If you have one power supply, is it plugged into the wall and is it at least capable of delivering 2 Amps of current?
* If you have two power supplies, see above for the Motor Controller board and add a 7-9V DC power supply for the Arduino of at least 1 Amp. Anything less than 7 Volts will cause unreliable operation
* Do you see a green led marked ```on``` on the Arduino board glowing to indicate the Arduino has power? If not, there is a power issue

Testing
-------

#. Remove the Motor Shield ---we are going to test just the Arduino first.
#. Download and install the most current version of :ref:`EX-CommandStation <download/ex-commandstation:Latest EX-CommandStation Official Release>`
#. Open the Serial Monitor Window in the Arduino IDE and establish communication with the Arduino. You will need to set the serial data rate to ``115200 baud`` and make sure you have set ``Both CR & NL`` from the dropdown so that commands are accepted. If you see gibberish (garbage characters), this is usually an indication that the baud rate is incorrect. You should see "DCC-EX" and the software version as well as other log lines that mention WiFi. If you don't see anything in the log, it could be that the software did not upload correctly, less than 7 Volts DC to the Arduino, or be an issue with the connection between your computer and the Arduino. Check your serial port and try a different USB cable.

Testing the Arduino and EX-CommandStation code
----------------------------------------------

Validating the Arduino and |EX-CS| code is functional is a pretty straight forward exercise.

#. From the serial monitor window, type ``<D RESET>`` to restart the |EX-CS| and monitor the startup logs. Once it has started, ensure the version you expect is displayed, and that the motor driver you have configured is also displayed. Look for a line similar to ``<iDCC-EX V-4.2.3 rc1 / STM32 / STANDARD_MOTOR_SHIELD G-PORTX-HAL-20220828>`` which translates to ``<Version / Microcontroller / Motor shield definition>``. If these differ from what you expect, the software hasn't loaded correctly, or your "config.h" file may not have been updated prior to uploading the software.
#. If there are obvious issues noted from these startup logs, review "config.h", make sure you have downloaded the correct version of |EX-CS|, and upload the software again. 

Testing the Motor Shield
------------------------

If first two tests pass, then the Arduino is functioning correctly and it's time to test the Motor Shield.  

#. Power down the Arduino
#. Install the Motor Shield, then connect power to your Arduino and the Motor Shield, though do not connect to the tracks. Verify that you have the correct supply going to the correct board 
#. Verify that all the pins are properly seating in the headers and that they are aligned correctly and not shifted and off by one or more pins. Sight down the inside of the headers between the boards and make sure no pins are bent inward where you could easily miss them
#. Verify that all of the mappings are correct for your motor shield. For an Arduino Motor Shield, you should not have changed any pin settings in the config.h file
#. Open (or re-open) the Arduino Serial window  
#. Send a ``<1>`` command.  
#. All 4 lights next to the outputs of the Motor Shield should be on.

If neither of the LEDs attached to one of the output channels comes on when you send a ``<1>`` command, this indicates you are not correctly mapping either the SIGNAL_ENABLE_PIN_MAIN or SIGNAL_ENABLE_PIN_PROG pins from the Arduino (depending on which output channel does not appear to be working). Make sure you did not change any of the default settings in the config.h file.

If only one of the LEDs attached to the one of the output channels comes on when you send a ``<1>`` command, but the other does not, this suggests that either the DCC signal is not getting through to the Motor Shield, in which case it is a mapping/wiring/jumper problem, OR that the signal is getting through but the H-bridge on the Motor Shield itself is not functioning (and the Motor Shield may need to be replaced). 

If you still need help, please find us on Discord or send an email to support@dcc-ex.com

Testing the DCC signal
----------------------

Now the fun part -- we are going to test the generation of the DCC signal itself.  

The easiest way to do this is using a Multi-meter that can read AC voltage. You can measure that 12V DC is going INTO the Motor Shield, but you have to use the **AC setting** to measure the bipolar square wave signal. With one lead of either probe connected to one track and the other probe connected to the other track, you should read an AC voltage in the range of 15-24V depending on our input voltage and a few other factors. An N-Scale track with 12V DC input to the motor shield is usually around 14VAC. If you read zero volts or a very small AC voltage (1V or less) then either you are still using the DC setting on your meter, or there is something wrong with your wiring, motor shield, or config.h settings.

Loco Programming Issues (-1 or JMRI 308 error)
===============================================

With all of the decoder manufacturers creating hardware and the difficulties in properly interpreting the NMRA standard, we have found that quite a few decoders are wildly outside the specification. That presents a few challenges. If you can't read CVs or program your loco or you see "Error 308" in your JMRI log, it could be one of the following:

#. **Current sense issue** - From the Arduino Serial monitor with ``115200 baud`` set and ``Both CR & NL`` selected in the dropdown, put a loco on the MAIN track. Enter the <1> command to turn on power. Then enter the <C> command and check the response. You should see a valid number for current.
#. Check the analog input pins to make sure there are no bent pins. If you wired your own motor board, make sure you have current sense capability on that board, that you have wires going to the correct analog pin on the Arduino, and that if pin A0, for example, is your current sense for the MAIN track, that your motorboard definition matches that pin.
#. **Out of spec. decoder (most likely)** - You will need to run a test and then modify a setting or two. Please go to the :doc:`<Diagnostic \<D ACK\> </reference/tools/diagnostic-d-ack-command>`. Send us your log.

If you continue to have issues reading decoders on the programming track with multiple different decoders, it's worthwhile reviewing the :doc:`/reference/hardware/motorboards/motor-board-config` page, especially all information relating to current sensing. If current sensing is not configured and functioning correctly, you will not be able to read any decoders via the programming track.