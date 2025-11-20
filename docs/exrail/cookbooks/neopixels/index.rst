.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
NeoPixel Support
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

The IO_NeoPixel.h driver supports the adafruit neopixel seesaw board. It turns each pixel into an individual VPIN which can be given a colour and turned on or off using the the ``NEOPIXEL`` |EX-R| macro. EXRAIL SIGNALS can also drive a single pixel signal or multiple separate pixels.

See also:

.. toctree::
    :maxdepth: 1

    neopixels
    signals

Defining the hardware driver
============================

Add a driver definition in myAutomation.h for each adafruit I2C driver.

.. code-block:: cpp

   HAL(neoPixel, firstVpin, numberOfPixels [, mode [, i2caddress])

Where mode is selected from the various pixel string types which have varying colour order or refresh frequency. For MOST strings this mode will be NEO_GRB but for others refer to the comments in IO_NeoPixel.h

If omitted the node and i2caddress default to NEO_GRB, 0x60.

For example:

.. code-block:: cpp

   HAL(NeoPixel,1000,20)

This is a NeoPixel driver defaulting to I2C aqddress 0x60 for a GRB pixel string. Pixels are given vpin numbers from 1000 to 1019.

.. code-block:: cpp
    
   HAL(NeoPixel,1020,20,NEO_GRB,0x61)

This is a NeoPixel driver on i2c address 0x61.
