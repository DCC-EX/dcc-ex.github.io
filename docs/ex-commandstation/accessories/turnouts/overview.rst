.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-description.rst
|EX-CS-LOGO|

****************************
Overview - types and options
****************************

|conductor| |tinkerer| |engineer| |support-button|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

What is a turnout or point?
===========================

To go back to basics, a turnout or point on either a real or model railway allows a train to move from one track to another.

When moving in to the land of digital control for model railways, there needs to be a way to control turnouts or points electronically and, where desired, via automation.

This section will focus on the types of turnouts/points supported by |EX-CS| with the common hardware configurations required to support them, along with the available methods to control them.

Turnout/point types
===================

Ignoring "hand of God" or "the big finger" operation (manually closing/throwing), there are essentially two mechanisms for remote control and automation of turnouts/points: motor driven and solenoid/coil operated.

Motor driven
------------

Lever operated turnouts/points use a lever type mechanism to move the rails into either the closed or thrown position, and to control these remotely, some form of external motor drive mechanism can connect to the lever to operate them.

To control these remotely from your |EX-CS| and also to enable automation capabilities witH |EX-R|, the common solution is to use servo motors connected to a PCA9685 servo module. There are also commercial DCC accessory decoder based motor driven turnout/point controllers available which can be utilised instead.

For layouts using flex track and some brands of set track, these are the sorts of turnouts or points that are in use such as Peco or Hornby, and are also typically used with hand-laid track.

Solenoid/coil operated
----------------------

Solenoid (or coil) operated turnouts/points also typically have a lever or switch to allow these to be operated manually, however these aren't designed to be motor driven in the same was as lever operated turnouts/points, and rather they have an internal solenoid or coil that needs to be energised in order to close or throw them.

The critical element to consider with these is that the solenoid or coil requires a **very brief pulse** to actuate them, and powering them continuously will **burn them out**. This also means they shouldn't be operated in repeatedly in rapid succession, to allow time to cool down.

There are several different options to control these remotely including capacitive discharge units (CDU) and motor driver ICs such as L293D, L298, or HG7881/L9110. There are also commercial DCC accessory decoder based solenoid or coil turnout/point controllers available which can be utilised instead.

Further to this, and depending on the brand of turnout/point, these will either have a single or double solenoid/coil configuration. The difference is fortunately very obvious, as the single coil versions will have two wires to operate them, whereas the double coil versions will have three wires.

Solenoid/coil operated turnouts/points are commonly found in set track from brands such as Kato, Micro-Trains, and Rokuhan.

DCC accessory turnouts/points
-----------------------------

While the sections on solenoid/coil or servo operated turnouts cover DCC accessory turnouts as well, it's worth calling this out explicitly to ensure people wishing to use these on their layout know exactly where to look.

So, for users of DCC accessory based turnouts, simply look at either the solenoid/coil or servo turnout/point pages depending on the type of physical turnout in use, as those pages will also cover off how to operate those as DCC accessories.

There is, however, one further important aspect to take into consideration with DCC accessory turnouts/points: should a short circuit occur on the track, resulting in the |EX-CS| turning the track power off, any DCC accessories obtaining power and DCC commands from the track will not be able to be operated.

This means if a locomotive has caused a short by entering a turnout/point that is set incorrectly, you may not be able to switch the turnout/point to recover from the short circuit situation, and manual intervention will be required.

Turnout/point control options
=============================

Turnouts or points can be controlled by your |EX-CS| in several different ways, including mimic panels, throttles/controllers, |EX-R| automation, and |JMRi|.

The Turnout object
------------------

In order for turnouts/points to be controlled by any of these methods, they need to be defined as a turnout object first.

Once turnout objects are defined in your |EX-CS|, they will be advertised to throttles/controllers that support these, such as Engine Driver and other WiThrottle apps, as well as |JMRi|.

Defining turnout objects
------------------------

Turnout objects can be defined via the serial console using the ``<T ...>`` command, or in your "myAutomation.h" file with the |EX-R| ``TURNOUT()``, ``PIN_TURNOUT()``, ``SERVO_TURNOUT()``, or ``VIRTUAL_TURNOUT()`` commands.

The recommended way to define turnout objects is to define these using the |EX-R| commands in "myAutomation.h". This has the advantage that they will automatically be created each time you turn your |EX-CS| on.

For information on using the ``<T ...>`` commands, refer to the :doc:`/reference/software/command-summary-consolidated` and :doc:`/reference/software/command-reference`.

For information on using the |EX-R| commands in "myAutomation.h" refer to the :doc:`/ex-rail/EX-RAIL-command-reference`.

Turnout/point control, hardware, and configuration
==================================================

Continue to the next pages for more specific information on controlling, connecting hardware, and configuration of the specific turnout/point types outlined above.