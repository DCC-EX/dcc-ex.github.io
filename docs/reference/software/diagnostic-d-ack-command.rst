
********************************
Diagnostics ``<D ACK>`` Command
********************************

If you encounter problems with ACKs from the Decoder (Reading or Writing CVs) and you want help, the DCC-EX support team will ask you to provide a log. This is a very simple diagnostic test to provide us with the proper information. With your loco on the PROG track, and using a serial monitor like the one in the Arduino IDE, enter each of these two commands folowed by pressing "send":

| ``<D ACK ON>`` 
| ``<R>``

This will turn ACK diagnostics ON and then try to read the appropriate CVs to determine your loco address. If you don't see your loco address at the end of the report, send us the log (see below for an example), and we can help you diagnose the problem.

More Detail
===========

When the ACK processing on the prog track does not work as expected, you may want to use the ``<D ACK ON>`` command in a serial command window. This is an example how to read CV8 with diagnostics on. You enter the first 2 lines, ``<D ACK ON>`` followed by ``send``, then ``<R 8 1 1>`` followed by ``send``. DCC-EX does not echo what you write, but your serial command window may. With diag on you get the extra 11 lines of output compared to if you just entered the command with diagnostics off. The last line is the answer, CV8=145:

.. code-block:: none

   <D ACK ON>
   <R 8 1 1>
   ACK-BASELINE 33/98mA
   V0 cv=8 bit=7 NO-ACK after 143mS max=12/35mA pulse=0uS
   V1 cv=8 bit=7 ACK-OK after 34mS max=646/1931mA pulse=6852uS
   V0 cv=8 bit=6 ACK-OK after 34mS max=583/1743mA pulse=6844uS
   V0 cv=8 bit=5 ACK-OK after 34mS max=646/1931mA pulse=6800uS
   V0 cv=8 bit=4 NO-ACK after 144mS max=12/35mA pulse=0uS
   V0 cv=8 bit=3 ACK-OK after 34mS max=563/1683mA pulse=6792uS
   V0 cv=8 bit=2 ACK-OK after 34mS max=647/1934mA pulse=6800uS
   V0 cv=8 bit=1 ACK-OK after 34mS max=573/1713mA pulse=6844uS
   V0 cv=8 bit=0 NO-ACK after 145mS max=14/41mA pulse=0uS
   VB cv=8 value=145 ACK-OK after 34mS max=639/1910mA pulse=6848uS
   Callback(145)
   <r1|1|8 145>

Your output may show different formatting with respect to linefeeds. Here the decoder reports that bits 7, 4 and 0 are **NOT** Zero. That gives the value of ``10010001 = 145`` which is the manufacturer ID for Zimo. That value is checked in the ``VB`` line. For a successful read, the result of the verify bit and verify byte commands have to match, otherwise the value can not be read. If you have problems reading decoders, you can compare the received values with the expected values. The format is:

.. code-block:: none

   OPERATION cv=n bit=b NO-ACK/OK after WAITTIME mS max=INTERNALVAL / CURRENT mA pulse= PULSELENGTH uS

The CURRENT should be over 60mA for a successful ACK and the length should be 6000uS +-1000uS but because of Decoder variations from the standard, DCC-EX has some extra pulse length margin.

In this example, we are checking CV 8, which is the manufacturer ID for your decoder. We then check each of the 8 "bits" in the "byte" that holds the value in that CV.

The first test, ``ACK-BASELINE`` gets a baseline reading of the current on your programming track with the loco just sitting there.

Since most bits will be 0, we check that first to save time. ``V0`` means ``Verify zero``. If do not get a zero, we then try to verify a 1 - ``V1`` means "Verify one". If we don't get either, we display an error. A bit must be either a 0 or a 1 so the test will fail, but the data returned can help us see why. 

If we succeed on the first bit, we check each of the remaining 7 bits. ``NO-ACK`` means we did not see the bit value we were testing for, ``ACK-OK`` tells us we received an ACK. After each bit test, we show how long it took to receive the ACK (or the timeout value if we detected none), the Arduino raw pin reading being sent by your motor controller's current sense circuit, and what that translates to in milliAmps. Finally, we report the duration of the ACK Pulse, if detected.

We do one final test at the end to ``Verify Byte``, you see that as ``VB``. This does a double-check to see if the byte contains what we found by checking it one bit at a time. The must match for a successful read.

Other than when using the "decoder address test", ``<R>`` with no parameters, you need to enter CV read commands with all 3 parameters. The format is ``<R CV x y>`` where R stands for read and CV is the CV number you want to check. The X and Y values can be anything, but must be entered. They are an advanced feature for programmers whose software can work with DCC-EX (like JMRI). So you would enter ``<R 8 55 55>`` or ``R 8 1 1>`` to try and read CV 8. The response is ``<r CV x y>`` where "x" and "y" are whatever numbers you entered after the CV value.

To turn off the ack diagnoistics use any parameter that is not "ON" or "LIMIT".

.. code-block:: none

   <D ACK NOPE>

Diag messages off.


Ack Limit
==========

The Ack current limit is set according to the DCC standard(s) of 60mA. Most decoders send a quick back and forth current pulse to the motor to generate this ACK. However, some modern motors (N and Z scales) may not be able to draw that amount of current. You can adjust down this limit. Or, if for some reasons your acks seem to be too "trigger happy" you can make it less sensitive by raising this limit.

.. code-block:: none

   <D ACK LIMIT 30>

would set the ack limit to 30mA (more sensitive). 

.. code-block:: none

   <D ACK LIMIT 100>

would set the limit to 100mA (less sensitive). 

The custom ack limit will be effective until you restart the Command Station (it will not "stick" in EEPROM). If you wish to permanenly set the ACK LIMIT, you may enter it as a command in the setup.h file.

***Add help on how to set this in the autoexec file***

