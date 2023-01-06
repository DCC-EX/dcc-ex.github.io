.. include:: /include/include.rst
.. include:: /include/include-l2.rst
********************************
Solenoid or coil turnouts/points
********************************

|conductor| |tinkerer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

Important considerations for solenoid/coil turnouts/points
==========================================================

Solenoid/coil based turnouts are switched by very small coils that are typically designed to be energised for very brief periods of time (read milliseconds, not seconds), and **leaving these energised for too long will burn them out**.

If not using the manufacturer's turnout/point control hardware, the safest option is to use a capacitive discharge unit (CDU), as the short duration discharge of the capacitor is what is used to energise the coil.

If switching the points digitally via some other means such as a motor driver IC or relay, use the shortest duration that provides reliable switching.

Defining solenoid/coil based turnout objects
============================================

To define solenoid/coil based turnouts directly in your |EX-CS| via the serial console, use the appropriate one of these commands:

- ``<T id VPIN vpin>`` - use this command when using a turnout/point controller that uses a single pin, whether connected directly to your |EX-CS| or via an I/O expander device
- ``<T id DCC linear_address>`` - use this command when using DCC accessory decoders to control the turnout/point

Refer to :ref:`reference/software/command-reference:defining (setting up) a turnout` for details on these commands.

To define solenoid/coil based turnouts using |EX-R| (whether or not they are to be automated) via the "myAutomation.h" file, use the appropriate one of these commands:

- ``PIN_TURNOUT(id, vpin [, "description"])`` - use this command when using a turnout/point controller that uses a single pin, whether connected directly to your |EX-CS| or via an I/O expander device
- ``VIRTUAL_TURNOUT(id [, "description"])`` - use this command when you need to define a custom macro that controls the various pins and duration required to switch a turnout
- ``TURNTOUT(id, addr, sub_addr [, "description"])`` - use this command when using DCC accessory decoders to control the servos

Refer to :ref:`ex-rail/ex-rail-reference:turnouts/points` for details on these commands, along with :ref:`ex-rail/creating-elements:adding turnouts/points` for some further information and examples.

Connecting the hardware
=======================

