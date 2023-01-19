.. include:: /include/include.rst
.. include:: /include/include-l3.rst
****************************
Servo driven turnouts/points
****************************

|conductor| |tinkerer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

While there is already a reasonable amount of information available for servo driven turnouts/points within our documentation, it is distributed among other pages, so this page will primarily be a central location pointing to the existing documentation, along with any other considerations that need to be taken into account that may not be covered elsewhere.

Important considerations for servo operation
============================================

**Test, test, test** your servo parameters prior to connecting to an actual turnout/point. If you have defined angles that exceed the physical limits of your turnout, you will likely damage it and/or the servo mechanism.

**Treat each servo and turnout as an individual** as not all servos (or turnouts/points for that matter) are created equal. An angle that works with one servo and associated turnout will not necessarily provide the exact same result with another. Differences in servo brands, mounting methods, and even normal manufacturing tolerances will need to be factored in to the servo angles in use.

**Use flexible wire** to connect your servo arm to the turnout/point. Using a flexible connection between the turnout and the servo mechanism means if anything does go wrong such as the turnout getting jammed or an incorrect servo angle being sent, it reduces the chance of damaging the turnout or servo.

Defining servo based turnout objects
====================================

To define servo based turnouts directly in your |EX-CS| via the serial console, use the appropriate one of these commands:

- ``<T id SERVO vpin thrown_position closed_position profile>`` - use this command when using a servo module connected to your |EX-CS|
- ``<T id DCC linear_address>`` - use this command when using DCC accessory decoders to control the servos

Refer to :ref:`reference/software/command-reference:defining (setting up) a turnout` for details on these commands.

To define servo based turnouts using |EX-R| (whether or not they are to be automated) via the "myAutomation.h" file, use the appropriate one of these commands:

- ``SERVO_TURNOUT(id, vpin, active_angle, inactive_angle, profile [, "description"])`` - use this command when using a servo module connected to your |EX-CS|
- ``TURNOUT(id, addr, sub_addr [, "description"])`` - use this command when using DCC accessory decoders to control the servos

Note when providing the name of the profile to the ``SERVO_TURNOUT(...)`` command that the profile names are case sensitive, and must be written exactly as they appear in the reference (eg. Slow, not slow or SLOW).

Refer to :ref:`ex-rail/ex-rail-reference:turnouts/points` for details on these commands, along with :ref:`ex-rail/examples:defining servo turnouts`, :doc:`/big-picture/stage3`, and :ref:`ex-rail/creating-elements:adding turnouts/points` for some further information and examples.

Connecting the hardware
=======================

For turnouts/points controlled by DCC accessory decoders, you will need to refer to the manufacturer documentation on how to connect these to your layout.

For servos controlled by a servo module connected to your |EX-CS|, sufficient information should be available on the :doc:`/reference/hardware/servo-module` page.