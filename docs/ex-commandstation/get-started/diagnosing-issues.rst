.. meta::
   :keywords: EX-CommandStation Command Station diagnosing Issues Troubleshooting

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

**************************************
Diagnosing Issues (Troubleshooting)
**************************************

|conductor| 

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:


This is the "Help, it's not working!" page.

NOTE: This section is a very rough draft. More coming soon.

There are a lot of optional settings and choices a user can make and sometimes things don't work as you expect them to. If you upload software to the Command Station, connect power to your motor controller and the CS and then connect the output to your track and don't see power or your train responding, here are the steps to follow.

Is it Plugged In, Is it Turned On?
===================================

Yes, we need to start with the basics. If you have 12V DC or less connected to the input power of the Arduino and did not cut the power connect trace underneath the Motor Controller, then the Motor Controller and the Arduino can be powered from the one power supply connected to the barrel jack of the Motor Shield. If you cut the trace (which we highly recommend), then you will need two power supplies, a 7-9V DC power supply to the Arduino and a 12-18V DC (based on the scale of your locomotives) power supply for the Motor Controller.

* If you have one power supply, is it plugged into the wall and is it at least capable of delivering 2 Amps of current?
* If you have two power supplies, see above for the Motor Controller board and add a 7-9V DC power supply for the Arduino of at least 1 Amp. Anything less than 7 Volts will cause unreliable operation
* Do you see a green led marked ```on``` on the Arduino board glowing to indicate the Arduino has power? If not, there is a power issue

Diagnosing and Testing
=============================

#. Remove the Motor Shield ---we are going to test just the Arduino first.
#. Download and install the most current version of :ref:`EX-CommandStation <download/ex-commandstation:Latest EX-CommandStation Official Release>`
#. Open the Serial Monitor Window in the Arduino IDE and establish communication with the Arduino. You will need to set the serial data rate to ``115200 baud`` and make sure you have set ``Both CR & NL`` from the dropdown so that commands are accepted. If you see gibberish (garbage characters), this is usually an indication that the baud rate is incorrect. You should see "DCC-EX" and the software version as well as other log lines that mention WiFi. If you don't see anything in the log, it could be that the software did not upload correctly, less than 7 Volts DC to the Arduino, or be an issue with the connection between your computer and the Arduino. Check your serial port and try a different USB cable.

Testing the Arduino and Base Station code
==============================================

TODO: Coming soon... 


Testing the DCC signal
=========================

Now the fun part -- we are going to test the generation of the DCC signal itself.  

The easiest way to do this is using a Multi-meter that can read AC voltage. You can measure that 12V DC is going INTO the Motor Shield, but you have to use the **AC setting** to measure the bipolar square wave signal. With one lead of either probe connected to one track and the other probe connected to the other track, you should read an AC voltage in the range of 15-24V depending on our input voltage and a few other factors. An N-Scale track with 12V DC input to the motor shield is usually around 14VAC. If you read zero volts or a very small AC voltage (1V or less) then either you are still using the DC setting on your meter, or there is something wrong with your wiring, motor shield, or config.h settings.


Testing the Motor Shield
==============================

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

Loco Programming Issues (-1 or JMRI 308 error)
===============================================

With all of the decoder manufacturers creating hardware and the difficulties in properly interpreting the NMRA standard, we have found that quite a few decoders are wildly outside the specification. That presents a few challenges. If you can't read CVs or program your loco or you see "Error 308" in your JMRI log, it could be one of the following:

#. **Current sense issue** - From the Arduino Serial monitor with ``115200 baud`` set and ``Both CR & NL`` selected in the dropdown, put a loco on the MAIN track. Enter the <1> command to turn on power. Then enter the <C> command and check the response. You should see a valid number for current.
#. Check the analog input pins to make sure there are no bent pins. If you wired your own motor board, make sure you have current sense capability on that board, that you have wires going to the correct analog pin on the Arduino, and that if pin A0, for example, is your current sense for the MAIN track, that your motorboard definition matches that pin.
#. **Out of spec. decoder (most likely)** - You will need to run a test and then modify a setting or two. Please go to the :doc:`<Diagnostic \<D ACK\> </reference/tools/diagnostic-d-ack-command>`. Send us your log.

..

   TODO: finish this section. Link to notes about current sensing.

Updated June 30, 2021