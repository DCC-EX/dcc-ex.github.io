.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-description.rst
********************************
Solenoid or coil turnouts/points
********************************

|conductor| |tinkerer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 3
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

Refer to :ref:`reference/software/command-reference:defining (setting up) a turnout/point` for details on these commands.

To define solenoid/coil based turnouts using |EX-R| (whether or not they are to be automated) via the "myAutomation.h" file, use the appropriate one of these commands:

- ``PIN_TURNOUT(id, vpin [, "description"])`` - use this command when using a turnout/point controller that uses a single pin, whether connected directly to your |EX-CS| or via an I/O expander device
- ``VIRTUAL_TURNOUT(id [, "description"])`` - use this command when you need to define a custom macro that controls the various pins and duration required to switch a turnout
- ``TURNOUT(id, addr, sub_addr [, "description"])`` - use this command when using DCC accessory decoders to control the servos

Refer to :ref:`ex-rail/ex-rail-command-reference:turnout/point objects - definition and control` for details on these commands, along with :ref:`ex-rail/creating-elements:adding turnouts/points` for some further information and examples.

Connecting and controlling the hardware
=======================================

Using an L293D motor driver - single solenoid/coil turnouts
-----------------------------------------------------------

.. image:: /_static/images/turnouts/bare-l293d-single-coil-turnouts.png
  :alt: Bare L293D with single coil turnouts
  :scale: 30%

A single L293D motor driver IC can be used to control two turnouts/points and will require six digital output pins either directly from your |EX-CS| (as per the diagram above), or these can also be connected via an I/O expander such as an MCP23017 or |EX-IO|.

To operate the turnouts/points in this manner, the direction of the turnout (close/throw) is configured by setting the input pins (2 and 7, 10 and 15) high or low, and briefly setting the appropriate enable pin high (1 or 9).

Note that the 10K pull down resistors connected from ground to the enable pins are there as a safety feature to ensure that any unknown states during start up don't cause the enable pins to be set to a high state, causing the coils to overheat and burn out.

The voltage provided to "External Power" is the voltage required to operate the turnouts/points, and will depend on the brand/model. Absolute maximum for the L293D is 36V DC.

Here is an example |EX-R| macro that will configure a virtual turnout, setting the correct pins for the two turnouts to operate correctly:

.. code-block:: 

  #define PULSE 10    // Set the duration of the pulse to 10ms

  #define SINGLE_COIL_TURNOUT(t, p1, p2, p3, desc) \
  VIRTUAL_TURNOUT(t, desc) \
  DONE \
  ONCLOSE(t) \
  SET(p2) RESET(p3) \
  SET(p1) DELAY(PULSE) RESET(p1) \
  DONE
  ONTHROW(t) \
  RESET(p2) SET(p3) \
  SET(p1) DELAY(PULSE) RESET(p1) \
  DONE

  SINGLE_COIL_TURNOUT(101, 22, 24, 26, "Turnout 101")
  SINGLE_COIL_TURNOUT(102, 23, 25, 27, "Turnout 102")

Before implementing this macro (or any similar macro controlling solenoid/coil turnouts/points), it is imperative that the correct voltage for the brand and model of turnouts/points is known, and that the defined pulse or delay time is kept to the minimum value possible for reliable switching of the turnouts/points.

Using an L293D motor driver - dual solenoid/coil turnouts
---------------------------------------------------------

.. image:: /_static/images/turnouts/bare-l293d-dual-coil-turnouts.png
  :alt: Bare L293D with dual coil turnouts
  :scale: 30%

Like the single solenoid/coil turnouts, a single L293D motor driver IC can be used to control two turnouts/points. This will still require six digital output pins either directly from your |EX-CS| (as per the diagram above), or these can also be connected via an I/O expander such as an MCP23017 or |EX-IO|.

To operate the turnouts/points in this manner, the direction of the turnout (close/throw) is still configured by setting the input pins (2 and 7, 10 and 15) high or low, and briefly setting the appropriate enable pin high (1 or 9). The key difference for dual solenoid/coil turnouts is the common (thrid) wire of the turnout being connected to ground as per the diagram above.

Note that the 10K pull down resistors connected from ground to the enable pins are there as a safety feature to ensure that any unknown states during start up don't cause the enable pins to be set to a high state, causing the coils to overheat and burn out.

The voltage provided to "External Power" is the voltage required to operate the turnouts/points, and will depend on the brand/model. Absolute maximum for the L293D is 36V DC.

Here is an example |EX-R| macro that will configure a virtual turnout, setting the correct pins for the two turnouts to operate correctly (note it is identical to the single coil version, but renamed):

.. code-block:: 

  #define PULSE 10    // Set the duration of the pulse to 10ms

  #define DUAL_COIL_TURNOUT(t, p1, p2, p3, desc) \
  VIRTUAL_TURNOUT(t, desc) \
  DONE \
  ONCLOSE(t) \
  SET(p2) RESET(p3) \
  SET(p1) DELAY(PULSE) RESET(p1) \
  DONE
  ONTHROW(t) \
  RESET(p2) SET(p3) \
  SET(p1) DELAY(PULSE) RESET(p1) \
  DONE

  DUAL_COIL_TURNOUT(101, 22, 24, 26, "Turnout 101")
  DUAL_COIL_TURNOUT(102, 23, 25, 27, "Turnout 102")

Before implementing this macro (or any similar macro controlling solenoid/coil turnouts/points), it is imperative that the correct voltage for the brand and model of turnouts/points is known, and that the defined pulse or delay time is kept to the minimum value possible for reliable switching of the turnouts/points.

Using a Capacitive Discharge Unit (CDU) - single solenoid/coil turnouts
-----------------------------------------------------------------------

.. todo:: MEDIUM - Add CDU info

Using a Capacitive Discharge Unit (CDU) - dual solenoid/coil turnouts
---------------------------------------------------------------------

Option 1 - DIY CDU by "Rosscoe" (DCC-EX user on Discord)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The infomation here is based on the combined driver and CDU as outlined in this GitHub repository, with a PCB available from `PCBWay <https://www.pcbway.com/>`_

.. rst-class:: dcclink

  `DCC Solenoid Turnout Driver <https://github.com/Rosscoetrain/DCC-Solenoid-Turnout-Driver>`_

.. image:: /_static/images/turnouts/block_diagram_switch_final.png
  :alt: Block Diagram
  :scale: 60%

This board has an MCP23017 which is connected to your |EX-CS| via |I2C|, which is then controlled like any other MCP23017.  This MCP23017 controls two ULN2803 darlington arrays to switch power to the turnout/point solenoids.

The connections will depend on the driver and CDU.

On the turnout/point solenoids, there will be three wires: a common wire, a wire to close the turnout, and a wire to throw the turnout.

With the above driver board, the common is positive and the control wires are connected to ground by the darlington drivers.

The EX-RAIL macro below creates a turnout object that closes/throws the turnout/point via the MCP23017 vpins on the board.

The DUAL_SOLENOID_TURNOUT definition is:

- id - turnout id
- pc - pin for CLOSE command
- pt - pin for THROW command
- desc - description
- ali - alias that can be used for the turnout in EX-RAIL

.. code-block:: 

  #define PULSE 10 //10 mSec
  #define DUAL_SOLENOID_TURNOUT(id,pc,pt,desc,ali)\
  VIRTUAL_TURNOUT(id,desc)\
  ALIAS(ali,id)\
  DONE\
  ONCLOSE(id)\
  SET(pc)\
  DELAY(PULSE)\
  RESET(pc)\
  DONE\
  ONTHROW(id)\
  SET(pt)\
  DELAY(PULSE)\
  RESET(pt)\
  DONE

  // Example use of this macro using first two pins on the first MCP23017 I/O expander
  DUAL_SOLENOID_TURNOUT(1,164,165,"Example CDU turnout",EXAMPLE_TURNOUT)
