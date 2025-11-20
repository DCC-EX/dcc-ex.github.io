.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Loco Functions
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

Functions can be set on or off. |EX-R| knows nothing about the meaning of each function because this is internal to the loco decoder.


- ``FON(func)``  turns on a loco function
- ``FOFF(func)`` turns off a function

In more advanced cases, an automation driving a loco may need to manage functions on another address, perhaps carriage lights. This can be done with the commands

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

