.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Maintaining multiple command stations
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

Maybe you have more than one command station and you wish to have slightly different |EX-R| setups, perhaps because you are testing a new release on a separate CPU or need to compile different scripts for different layouts.

The C++ compiler pre-processor is available to select various parts of your ``myAutomation.h`` based on definitions created in your ``config.h`` or those created by ``defines.he`` which automates the detection of the CPU type of your command station.

For example:

.. code-block:: cpp

    #if defined(ARDUINO_ARCH_AVR)
      // on my Mega, I have signal1 on pins (30,31,32)
      ALIAS(mysignal1,30)
    #else 
      // on my CSB1 or similar, I use pins 800,801,802 on an expander
      ALIAS(mysignal1,800)
    #endif
      SIGNALH(mysignal1,mysignal1+1,mysignal1+2)
      ONTHROW(1) RED(mysignal1) DONE
      ONCLOSE(1) GREEN(mysignal1) DONE

In addition, each |EX-R| command is actually a preprocessor definition so it is possible to use an #ifdef to include a section that uses a new feature but only if the code version has that feature available.

.. code-block:: cpp

    #ifdef NEOPIXEL
      NEOPIXEL(2013,255,255,0)
    #endif   

Note ``#ifdef xxx`` and ``#if defined(xxx)`` do the same thing.
