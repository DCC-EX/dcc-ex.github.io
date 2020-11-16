
Diagnostics ``<D ACK>`` Command
===================================

When the ACK processing on the prog track does not work as expected, you may want to use the ``<D ACK ON>`` command in a serial command window. This is an example how to read CV8 with diagnostics on. You enter the first 2 lines. DCC-EX does not echo what you write, your serial command window may. With diag on you get the extra 11 lines of output. The last line is the answer, CV8=145:

.. code-block:: none

   <D ACK ON>
   <R 8 1 1>
   ACK-BASELINE 33/98mA
   V0 cv=8 bit=7 ACK-FAIL after 143mS max=12/35mA pulse=0uS
   V1 cv=8 bit=7 ACK-OK after 34mS max=646/1931mA pulse=6852uS
   V0 cv=8 bit=6 ACK-OK after 34mS max=583/1743mA pulse=6844uS
   V0 cv=8 bit=5 ACK-OK after 34mS max=646/1931mA pulse=6800uS
   V0 cv=8 bit=4 ACK-FAIL after 144mS max=12/35mA pulse=0uS
   V0 cv=8 bit=3 ACK-OK after 34mS max=563/1683mA pulse=6792uS
   V0 cv=8 bit=2 ACK-OK after 34mS max=647/1934mA pulse=6800uS
   V0 cv=8 bit=1 ACK-OK after 34mS max=573/1713mA pulse=6844uS
   V0 cv=8 bit=0 ACK-FAIL after 145mS max=14/41mA pulse=0uS
   VB cv=8 value=145 ACK-OK after 34mS max=639/1910mA pulse=6848uS
   Callback(145)
   <r1|1|8 145>

Your output may show different formatting with respect to linefeeds. Here the deocder reports that bits 7, 4 and 0 are **not** Zero. That gives the value of ``10010001 = 145`` which is the manufacturer ID for Zimo. That value is checked in the ``VB`` line. For a successful read, the result of the verify bit and verify byte commands have to match, otherwise the value can nor be read. If you have problems reading decoders, you can compare the received values with the expected values. The format is:

.. code-block:: none

   OPER cv=n bit=b ACK-FAIL/OK after WAITTIME mS max=INTERNALVAL / CURRENT mA pulse= PULSELENGTH uS

The CURRENT should be over 60mA for a successful ACK and the length should be 6000uS +-1000uS but because of Decoder variations from the standard DCC-EX has some extra pulse length margin.

If you encounter problems with ACKs from the Decoder and you want help, the DCC-EX support will probably ask you to provide this kind of diagnostics.

The two values of 1 after each other in the ``<R>`` command and in the ``<r>`` answer you can safely ignore.

Ack Limit
---------

The Ack current limit is according to the DCC standard(s) set to 60mA. But as modern motors (N and Z scales) may have problems to draw that amount of current, you can adjust down that limit. Or if for some reasons your acks seem to be too "trigger happy" you can make it less sensitive.

.. code-block:: none

   <D ACK LIMIT 30>

would set the ack limit to 30mA. The custom ack limit will be effective until you restart the Command Station (it will not "stick" in EEPROM).

To turn off the ack diagnoistics use any parameter that is not "ON" or "LIMIT".

.. code-block:: none

   <D ACK NOPE>

Diag messages off.
