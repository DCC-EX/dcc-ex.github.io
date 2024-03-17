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

What is a turntable or traverser?
=================================

A turntable is a device that is used to rotate locomotives, primarily used in the steam era when locomotives could not reverse, and a mechanism was required to turn them around without requiring lengthy reversing loops.

A traverser on the other hand typically moves horizontally or vertically to align with different tracks. In the real world, traversers tend to move horizontally only, however it is not uncommon for vertical traversers in model railroading to transfer locomotives and even full trains between levels on a layout.

While turntables and traversers can be operated manually or electronically independent of your |EX-CS|, it is ideal to be able to control them the same way you can control turnouts/points, hence the introduction of this capability.

This section will focus on the types of turntables/traversers supported by |EX-CS| with the common hardware configurations required to support them, along with the available methods to control them.

|EX-CS| supports two types of turntables/traversers; DCC accessory types (such as the Walthers 90' and 130' motorised turntables) and our very own |EX-TT|.

.. note:: 

  While |EX-TT| is |NEW-IN-V5|, this section focuses on new functionality supporting turntables/traversers in the same manner as turnouts/points, by creating objects that can be advertised to and controlled by throttles in a similar way. |NOT-IN-PROD-VERSION|.

Turntable/traverser control options
===================================

Turntables or traversers can be controlled by your |EX-CS| via DCC-EX native commands or |EX-R| automation.

The Turntable object
--------------------

In order for turntables/traversers to be controlled by any of these methods, they need to be defined as a turntable object first.

Once turntable objects are defined in your |EX-CS|, they will be advertised to throttles/controllers that support these.

Note that as this functionality is brand new, there are unlikely to be throttles that make use of these commands at this point in time, however we encourage throttle developers to take note and consider adding this functionality for the best user experience by incorporating all layout control into the same throttle device if practical.

Defining turntable objects
--------------------------

Turntable objects can be defined via the serial console using the native |DCC-EX| command ``<I ...>``, or in your "myAutomation.h" file with the |EX-R| ``DCC_TURNTABLE()`` or ``EXTT_TURNTABLE()`` commands.

The recommended way to define turntable objects is to define these using the |EX-R| commands in "myAutomation.h". This has the advantage that they will automatically be created each time you turn your |EX-CS| on, and can have human-friendly descriptions associated with them.

For information on using the ``<I ...>`` commands to define objects, refer to :ref:`reference/software/command-summary-consolidated:turntables/traversers (configuring the ex-commandstation)`.

For information on using the |EX-R| commands in "myAutomation.h" refer to the :ref:`ex-rail/ex-rail-command-reference:turntable/traverser objects - definition and control`.

Controlling turntables/traversers
---------------------------------

As per defining the objects, turntables/traversers can also be controlled by both native |DCC-EX| commands and |EX-R|.

Refer to :ref:`reference/software/command-summary-consolidated:turntables/traversers` for information pertaining to controlling these devices, as well as for what throttle developers can use to enable control of these from throttles.

For |EX-R| commands, refer to :ref:`ex-rail/ex-rail-command-reference:turntable/traverser objects - definition and control`.

DCC accessory turntables
========================

.. note:: 

  As the author of these pages and the new turntable functionality has no access to a DCC accessory turntable, operation of DCC accessory turntables is theoretical only and has not been tested. The operation has been defined referring to the instructions found online for operating a Walthers DCC turntable only.

Like any other DCC accessory device, turntables are typically connected to the DCC track signal, and configured according to the manufacturer's instructions.

There is one important aspect to take into consideration with DCC accessory turntables: should a short circuit occur on the track, resulting in the |EX-CS| turning the track power off, any DCC accessories obtaining power and DCC commands from the track will not be able to be operated.

Also, as there is no feedback to the |EX-CS| from a DCC accessory turntable, you will not be able to use the ``WAITFORTT()`` command during |EX-R| automation, nor will a second broadcast be sent to tell throttles when a rotation or move has been completed.

EX-Turntable
============

Given |EX-TT| is fully integrated into your |EX-CS| via its device driver, full control and automation is possible as the status of a turntable or traverser is known at all times, allowing |EX-R| automations to be sequenced along with turntable/traverser rotations and movements.

The existing |EX-TT| documentation has been updated to reflect using both the original control methods, along with how to use the new turntable object to define and control turntables/traversers using it.

While it's recommended to review the entire updated |EX-TT| documentation inline with these changes, the important updates related to the new definition and control methods are on the :doc:`/ex-turntable/test-and-tune` page.

Read on for more...
===================

Continue on to the next pages to understand the methods to define and control these types of turntables/traversers...
