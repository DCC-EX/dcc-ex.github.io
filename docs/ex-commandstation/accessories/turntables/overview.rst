.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-description.rst
|EX-CS-LOGO|

|conductor| |tinkerer| |engineer|

****************************
Overview - types and options
****************************

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

What is a turntable or traverser?
=================================

To go back to basics, a turntable or tarverser...

When moving in to the land of digital control for model railways, there needs to be a way to control turntables and traversers electronically and, where desired, via automation.

This section will focus on the types of turntables/traversers supported by |EX-CS| with the common hardware configurations required to support them, along with the available methods to control them.

Turntable/traverser types
=========================

A typical model railroad turntable will be driven by a stepper or other motor, with some mechanism available to index where each...

DCC accessory
-------------

.

EX-Turntable
------------

.

Turntable/traverser control options
===================================

Turntables or traversers can be controlled by your |EX-CS| via DCC-EX native commands or |EX-R| automation.

The Turntable object
--------------------

In order for turntables/traversers to be controlled by any of these methods, they need to be defined as a turntable object first.

Once turntable objects are defined in your |EX-CS|, they will be advertised to throttles/controllers that support these.

Defining turntable objects
--------------------------

Turntable objects can be defined via the serial console using the native DCC-EX command ``<I ...>``, or in your "myAutomation.h" file with the |EX-R| ``DCC_TURNTABLE()`` or ``EXTT_TURNTABLE()`` commands.

The recommended way to define turntable objects is to define these using the |EX-R| commands in "myAutomation.h". This has the advantage that they will automatically be created each time you turn your |EX-CS| on, and can have human-friendly descriptions associated with them.

For information on using the ``<I ...>`` commands, refer to the :doc:`/reference/software/command-summary` and :doc:`/reference/software/command-reference`.

For information on using the |EX-R| commands in "myAutomation.h" refer to the :doc:`/ex-rail/EX-RAIL-command-reference`.

Turntable/traverser control, hardware, and configuration
========================================================

Continue to the next pages for more specific information on controlling, connecting hardware, and configuration of the specific turnout/point types outlined above.