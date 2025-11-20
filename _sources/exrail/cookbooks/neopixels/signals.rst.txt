.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Neopixel signals
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

There are two types possible:

- a mast with separate fixed colour pixels for each aspect
- a mast with one multiple colour pixel for all aspects.

Bear in mind that a single multicolour neopixel used above might be physically a multi-colour LED (as in a searchlight signal), or 3 individual LEDS wired to a single neopixel chip (ws2812) (as in a 2 or 3 lamp signal).  

For separate pixels, the colours should be established at startup and a normal ``SIGNALH`` macro used.

.. code-block:: cpp

    AUTOSTART 
      SIGNALH(1010,1011,1012)
      NEOPIXEL(1010,255,0,0)       
      NEOPIXEL(1011,128,128,0)
      NEOPIXEL(1012,0,255,0)
      RED(1010)  // force signal state otherwise all 3 lights will be on
    DONE

For signals with 1 neopixel, the ``NEOPIXEL_SIGNAL`` macro will create a signal on one vpin with three separate colours

.. code-block:: cpp

    NEOPIXEL_SIGNAL(vpin,redfx,amberfx,greenfx)

``redfx``,``amberfx``,``greenfx`` = colour values

The fx values above can be created by the NeoRGB macro so a bright red would be ``NeoRGB(255,0,0)``  bright green ``NeoRGB(0,255,0)`` and amber something like ``NeoRGB(255,100,0)``.
NeoRGB creates a single int32_t value so it can be used in several ways as convenient (but can't be used in an ALIAS command).

.. code-block:: cpp

    // create 1-lamp signal with NeoRGB colours
    NEOPIXEL_SIGNAL(1000,NeoRGB(255,0,0),NeoRGB(255,100,0),NeoRGB(0,255,0))

    // Create 1-lamp signal with named colours.
    // This is better if you have multiple signals.
    // (Note: ALIAS is not suitable due to word length defaults) 
    #define REDLAMP NeoRGB(255,0,0)
    #define AMBERLAMP NeoRGB(255,100,0)
    #define GREENLAMP NeoRGB(0,255,0)
    NEOPIXEL_SIGNAL(1001,REDLAMP,AMBERLAMP,GREENLAMP)

    // Create 1-lamp signal with web type RGB colours 
    NEOPIXEL_SIGNAL(1002,0xFF0000,0xFF6400,0x00FF00)
