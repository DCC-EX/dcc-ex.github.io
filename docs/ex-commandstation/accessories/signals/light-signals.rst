.. include:: /include/include.rst
.. include:: /include/include-l3.rst
|EX-CS-LOGO|

|conductor| |tinkerer| |engineer|

*************
Light signals
*************

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

Defining light signal objects
=============================

To define light signal objects, this is accomplished by using the signal commands available in |EX-R|.

Note that unlike turnouts or points, there is no equivalent command available in the serial console to define signals.

The commands available are:

- ``SIGNAL(red_pin, amber_pin, green_pin)`` - set the aspect by setting the appropriate pin low
- ``SIGNALH(red_pin, amber_pin, green_pin)`` - set the aspect by setting the appropriate pin high

What if I don't have three aspect signals?
------------------------------------------

If you only have two aspect signals, then you can simply define the unused aspect as either "0", or use a pin number that does not exist in reality, taking note that signals are always operated by the pin number associated with the "RED" aspect, so this should never be set to "0".

For example, defining a red and amber signal might look like ``SIGNAL(28, 30, 0)``. In this instance, setting the signal to red or amber will activate that light, however setting it to green will do nothing.

If defining a signal that has no red aspect, the signal still needs to be controlled by the pin associated with "RED", so a suitable definition would be ``SIGNAL(5000, 30, 32)``. In this instance, setting the light green or amber will activate the appropriate light, however setting it to red will actually display no signal at all as there is no physical connection to the virtual pin 5000.

Note if you have a single aspect signal (eg. just red), you will have no way of turning that red signal off unless you define a virtual pin for one of the unused aspects. Using ``SIGNAL(28, 0, 0)`` will have red always lit, and setting it to green or amber will not turn it off. In order to turn the red signal off, either simply use it as a digital pin with ``SET(28)`` or ``RESET(28)``, or define a virtual pin for one of the unused aspects, and activate that aspect to turn the red signal off, eg. ``SIGNAL(28, 5000, 0)``.

What if my signals have different colours?
------------------------------------------

If your signalling requires using different colours to the standard red/amber/green, then that has no impact whatsoever on defining and operating the signals, and you will still need to refer to them as red/amber/green in the software, and control them by whichever pin is defined as the red aspect.

Connecting the signals
======================

There are two ways to connect light signals:

- With the anode (positive) side of the lights connected to a common power source, and the cathode (negative) connected to the digital pin via a current limiting resistor - this is referred to as "active low" as the digital pin is set low to turn the light on
- With the cathode (negative) side of the lights connected to a common ground, and the anode (positive) connected to the digital pin via a current limiting resistor - this is referred to as "active high" as the digital pin is set high to turn the light on

Active low or ground activated signals
--------------------------------------

The ``SIGNAL(red_pin, amber_pin, green_pin)`` command is used when the anode or positive leg of the signal light/LED is connected to the common positive voltage source, and the cathode or negative leg of the signal light/LED is connected via a current limiting resistor to the digital pin either directly on your |EX-CS|, or to an I/O expander.

.. image:: /_static/images/signals/signal-3aspect-active-low.png
  :alt: 3 Aspect active low signal
  :scale: 30%

In the diagram above, the red aspect is connected to pin 28, amber to 30, and green to 32.

Sending the |EX-R| command GREEN(28) will set pins 28 (red) and 30 (amber) high, and pin 32 (green) low, ensuring the red/amber signals are off, and green is on.

Active high or positive activated signals
-----------------------------------------

Coversely, use the ``SIGNALH(red_pin, amber_pin, green_pin)`` command when the anode or positive leg is connected to the |EX-CS| or I/O expander via a current limiting resistor, with the cathode or negative connected to a common ground.

.. image:: /_static/images/signals/signal-3aspect-active-high.png
  :alt: 3 Aspect active high signal
  :scale: 20%

In the diagram above, the red aspect is connected to pin 28, amber to 30, and green to 32.

Sending the |EX-R| command GREEN(28) will set pins 28 (red) and 30 (amber) low, and pin 32 (green) high, ensuring the red/amber signals are off, and green is on.

Controlling light signals
=========================

Controlling light signals is exactly the same as semaphore or servo signals, skip to :doc:`/ex-commandstation/accessories/signals/signal-control` for information on controlling signals.