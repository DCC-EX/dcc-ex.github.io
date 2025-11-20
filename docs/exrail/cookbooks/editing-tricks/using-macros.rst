.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Using C++ Macros
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

The EXRAIL language is compiled by C++ and this means you can use MACROS of your own design according to the C++ compiler `pre-processor specification <https://gcc.gnu.org/onlinedocs/cpp/Macros.html>`_.

A MACRO is essentially a tiny program that types stuff for you while substituting parameters.

For example: This macro can be used to start two leds flashing alternately at half second intervals:

.. code-block:: cpp

   #define FLIPFLOP(led) \
      BLINK(led,500,500) \
      DELAY(500) \
      BLINK(led+1,500,500)

Notice that a C++ macro must be only one logical line long! So we must use the ``\`` character on the end of the line to indicate that this line is continued on the following.

In the above example, the FLIPFLOP macro takes a LED VPIN and starts flashing it, then half a second later it starts flashing the next pin in line. Since the delay and the on/off period are the same, the LEDs will flash alternately.

So you might use it in a sequence like this:

.. code-block:: cpp

   ONBUTTON(30)
      FLIPFLOP(32)  // start flashing leds 32 and 33
      DELAY(4000)   // wait 4 seconds
      SERVO(123,1033,Slow) // close crossing gates
      DELAY(3000) // give red-light jumpers a chance to consider their life choices
      GREEN(34) // change approach signal to green
   DONE

and

.. code-block:: cpp

   ONBUTTON(31)
      RED(34) // change approach signal to red
      SERVO(123,3200,Slow) // Open crossing gates
      RESET(32,2) // turn off the blinking on pins 32,33
   DONE

The servo positions above are of course dependent on your servos and how they are mounted. You must experiment first.

Macros like these are, obviously, more useful if you use the macro in more than one place.
