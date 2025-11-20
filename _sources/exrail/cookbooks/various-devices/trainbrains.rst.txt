.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Trainbrains Devices
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On this page
      :depth: 1
      :local:

These devices are available from `trainbrains.eu <https://trainbrains.eu>`_ and operate over I2C.

They auto-detect the device type so it is only necessary to provide HAL statements in myAutomation.h to identify that the device on the given address is a Trainbrains device and the number of VPINs that will be reserved for it by DCC-EX. 

Turnout drivers (solenoid and servo)
=====================================

Use the HAL statement to identify the device I2C address and create PIN_TURNOUT definitions so that DCC-EX sees the vpins as turnouts.

.. code-block:: cpp

    HAL(Trainbrains,700,2,0x14)
    PIN_TURNOUT(1,700,"Coal yard exit")
    PIN_TURNOUT(1,701,"Oil yard exit")

This creates VPINS 700 and 701 as turnouts. All other turnout operations in DCC-EX operate as normal.
This isn't going to work if the devivce at I2C address 0x15 is not a Trainbrains turnout controller.

## Signal controller

The signal controller only has one VPIN but may have hundreds of different combinations of lamps, blinking and state. This can be handled by pretending it is a NEOPIXEL signal and setting the Red channel to the lamp combination, the Blue channel to the blinking combination and the Green channel to the signal state. (Refer to Trainbrains documentation for details)

For example: (This is taken from the NEOPIXEL definitions, TODO we can replace this with a suitable alias. Just replace the colour values with the lamps,blink,state values. )

.. code-block:: cpp

    HAL(Trainbrains,720,1,0x15)

    // create 1-lamp signal with NeoRGB colours
    NEOPIXEL_SIGNAL(720,NeoRGB(255,0,0),NeoRGB(255,100,0),NeoRGB(0,255,0))

    // Create 1-lamp signal with named colours.
    // This is better if you have multiple signals.
    // (Note: ALIAS is not suitable due to word length defaults) 
    #define REDLAMP NeoRGB(255,0,0)
    #define AMBERLAMP NeoRGB(255,100,0)
    #define GREENLAMP NeoRGB(0,255,0)
    NEOPIXEL_SIGNAL(702,REDLAMP,AMBERLAMP,GREENLAMP)

    // Create 1-lamp signal with web type RGB colours 
    NEOPIXEL_SIGNAL(702,0xFF0000,0xFF6400,0x00FF00)

Signal values can be manually tested using the <o> command like this

.. code-block:: cpp

    <o vpin lamps flashes state>

To have a disco party, try 

.. code-block:: cpp

    <o 702 255 255 1>

For more than 3 signal aspects (other than RED/AMBER/GREEN) it is suggested that you create macros that will set the signal to the nearest equivalent RED/AMBER/GREEN and then overwrite the aspect with a NEOPIXEL command. In this way the IFRED/ONRED etc features will still work but the actual lamp display could be anything.

.. code-block:: cpp

    #define SHUNT(x) \
    AMBER(x)  \
    NEOPIXEL(x,10,2,2)

Sensors
============

The block occupancy sensor has 3 blocks.

.. code-block:: cpp

    HAL(Trainbrains,730,3,0x13)

makes virtual pins 730..732 usable as sensors like any other in |DCC-EX|
