.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-REF-LOGO|

****************
I2C Multiplexers
****************

|tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :depth: 1
      :local:

|NEW-IN-V5-LOGO-SMALL|

What is a multiplexer?
======================

In simple terms in the context of |I2C| communication, a multiplexer allows for different devices to be "switched" to and from using the same |I2C| bus/pins.

This enables:

- Using multiple devices with the same, hard coded |I2C| address
- Being able to use more devices than normal due to limited address ranges
- Split an |I2C| bus electrically to overcome capacitance/resistance issues

Which multiplexers are supported?
=================================

Both TCA9547 and TCA9548A multiplexers have been tested and are supported at the moment. Equivalent and compatible multiplexers should work, but we have not tested others at this time.

How do I use a multiplexer?
===========================

.. image:: /_static/images/i2c/mega2560-multiplexer-example.png
   :alt: Example of Arduino Mega2560 with TCA9584 multiplexer
   :scale: 30%
