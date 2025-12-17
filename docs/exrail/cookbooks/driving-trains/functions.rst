.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Loco Functions
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

Functions of the current loco can be set on or off. 

- ``FON(func)``  turns on a loco function
- ``FOFF(func)`` turns off a function

Note: |EX-R| knows nothing about the meaning/purpose of each function because this is internal to each decoder, and each decoder may have different functions assigned to different function numbers. It is up to the user to know what each function number does for their particular decoder.

In more advanced cases, an automation driving a loco may need to manage functions on *another decoder (differnt DCC address)*, perhaps carriage lights. This can be done with the commands:

- ``XFON(locoid, function)``
- ``XFOFF(locoid, function)``

For example:

.. code-block:: cpp

   ... while driving...
      AT(189)   // passing tunnel
         FON(0)    // loco lights on
         FON(8)    // make like a boy-racer  
         XFON(3001,0) // carriage lights on
      AT(190)   // at far end of tunnel
         FOFF(8)   // pretend we didn't do that
         FOFF(0)   // loco lights off
         XFOFF(3001,0) // carriage lights off
   ... and so on

