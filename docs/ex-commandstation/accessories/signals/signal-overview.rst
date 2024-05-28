.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-description.rst
|EX-CS-LOGO|

***************************************
Signalling overview - types and options
***************************************

|conductor| |tinkerer| |engineer| |support-button|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

What are signals?
=================

To go back to basics, a signal is used to provide clear indication to engineers on what action to take as they approach the signal.

When moving in to the land of digital control for model railways, there needs to be a way to control signals electronically and, where desired, via automation.

When referring to signals, the colour of the light or position of a semaphore arm is referred to as the aspect of the signal.

This section will focus on the types of signals supported by |EX-CS| with the common hardware configurations required to support them, along with the available methods to control them.

Signal types
============

In the physical sense, and in their most simplest form, signals are either a series of lights with different aspects (colours) or a semaphore with an arm rotating to different positions.

The application of these signals differs by country, region, track purpose, and railroad operator, so we won't attempt to cover that level of detail here, and you will need to do your own research if you wish to prototype a specific situation on your layout.

In terms of our software, |EX-R| can control the aspects of signals by defining them as a signal object, which allows for the correct signal aspect to be set when operating turnouts/points, by push buttons on a mimic panel, by triggering a sensor as a train approaches, or by many other activities on your layout.

Note that while the control of signals within |EX-CS| uses "RED", "AMBER", and "GREEN", there is no reason you can't adapt these to suit your requirements, whereby sending "RED" could in fact activate white lights indicating a train will be deviating to a spur or siding.

Further to this, signals supporting only three aspects is not a limiting factor, as there are ways you can automatically set other signals' aspects based on various activities, allowing for complex signalling scenarios.

Light signals
-------------

Light signals support up to three aspects (colours) to indicate whether an approaching train can continue (green), prepare to stop (amber), or stop (red).

Light signals are controlled by activating or deactivating digital pins either directly on your |EX-CS| or attached to I/O expanders.

All control of light signals is performed by the pin defined as the "Red" aspect.

Continue to :doc:`/ex-commandstation/accessories/signals/light-signals` for details on how to define and connect light signals.

Semaphore (or servo) signals
----------------------------

Semaphore (or servo) signals support up to three aspects (positions) to indicate whether an approaching train can continue, prepare to stop, or stop.

Semaphore signals are controlled by the position of servos attached to a PCA9685 servo module, hence why they are commonly referred to in our documentation as servo signals.

All control of semaphore signals is performed by the defined control pin, moving the servo to the specified angle according to the chosen aspect.

Continue to :doc:`/ex-commandstation/accessories/signals/servo-signals` for details on how to define and connect semaphore/servo signals.

DCC accessory signals
---------------------

In the current implementation, there is no specific signal object that defines and controls signals as DCC accessory items, and these can be operated the same as any other DCC accessory.

Continue to :doc:`/ex-commandstation/accessories/signals/dcc-signals` for considerations and options for DCC accessory signals.