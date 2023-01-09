.. include:: /include/include.rst
.. include:: /include/include-l3.rst
|EX-CS-LOGO|

***************
Turnouts/points
***************

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

What is a turnout or point?
===========================

Turnouts or points are an integral part of almost every layout in operation, and with the variety of turnout/point types and control options available, these require their own special section to help our users understand which is the best option for their layout and level of comfort.

To go back to basics, a turnout or point on either a real or model railway allows a train to move from one track to another.

When moving in to the land of digital control for model railways, to operate turnouts or points without having to manually switch them with our hands, the concept of a turnout object has been introduced.

This section will focus on the types of turnouts/points supported by |EX-CS| with the common hardware configurations required to support them. Where possible, we will outline known and tested brands and combinations of items commonly encountered by our users.

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

The critical element to consider with these is that the solenoid or coil requires a **very brief pluse** to actuate them, and powering them continuously will **burn them out**. This also means they shouldn't be operated in repeatedly in rapid succession, to allow time to cool down.

There are several different options to control these remotely including capacitive discharge units (CDU) and motor driver ICs such as L293D, L298, or HG7881/L9110. There are also commercial DCC accessory decoder based solenoid or coil turnout/point controllers available which can be utilised instead.

Further to this, and depending on the brand of turnout/point, these will either have a single or double solenoid/coil configuration. The difference is fortunately very obvious, as the single coil versions will have two wires to operate them, whereas the double coil versions will have three wires.

Solenoid/coil operated turnouts/points are commonly found in set track from brands such as Kato, Micro-Trains, and Rokuhan.

Turnout/point control from EX-CommandStation and EX-RAIL
========================================================

For turnouts/points to be controlled by |EX-CS| and/or automated by |EX-R|, they need to be defined as a turnout object first.

These can be defined via the serial console using the ``<T ...>`` command, or in your "myAutomation.h" file with the |EX-R| ``TURNOUT()``, ``PIN_TURNOUT()``, ``SERVO_TURNOUT()``, or ``VIRTUAL_TURNOUT()`` commands.

Note that you can define turnout objects using the |EX-R| commands in "myAutomation.h" regardless if you wish to automate them or not, and this has the advantage that they will automatically be created each time you turn your |EX-CS| on.

Once a turnout object is defined (via either method), it will be advertised to throttles and |JMRi|.

For information on using the ``<T ...>`` commands, refer to the :doc:`/reference/software/command-summary` and :doc:`/reference/software/command-reference`.

For information on using the |EX-R| commands in "myAutomation.h" refer to the :doc:`/ex-rail/EX-RAIL-summary`, :doc:`/ex-rail/EX-RAIL-reference`, and :ref:`ex-rail/creating-elements:adding turnouts/points`.

Turnout/point hardware and configuration
========================================

Continue to the next pages for more specific information on controlling, connecting hardware, and configuration of the specific turnout/point types outlined above.

.. toctree::
  :maxdepth: 1
    
  servo-turnouts
  solenoid-turnouts
