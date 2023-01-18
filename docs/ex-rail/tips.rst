.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-R-LOGO|

*******************
Tips and Techniques
*******************

|tinkerer| |conductor|

.. sidebar:: 

   .. contents:: On this page
      :depth: 2
      :local:

Below are some tips and techniques you can implement to get the most out of |EX-R|.


Comments
========

Comments can be very helpful if you need to go back at a later time to make changes to your sequences, to help you remember what you did or why you did it.

You can add comments to myAutomation.h in two ways:

* If ``//`` occurs in the line, everything after that (including the slashes) is ignored.  i.e. a 'Comment'
* If a line starts with ``/*`` then everything, including all subsequent lines an including the '/*') is ignored until a ``*/`` is found.  i.e. a 'Comment'


Aliases - User Friendly Names for any Ids
=========================================

Use the ``ALIAS()`` command in your script to make IDs a bit more human friendly, and easier to refer to later. 

``ALIAS( name[, value] )`` Aliases assigns names to values. They can go anywhere in the script. If a value is not assigned, a unique ID will be assigned based on the alias "name" text.

This is a simple substitution that lets you have readable names for things in your script. For example, instead of having to remember the VPin a turnout/point is connected to, give the pin number an alias and refer to it by that name. You can use this to name routes, values, pin numbers, or anything you need.

.. code-block:: cpp
   :class: code-block-float-right

   //example
   ALIAS(COAL_YARD_TURNOUT,19)
   ALIAS(COAL_YARD_SIGNAL_3,27)

   ROUTE(1,"Coal yard exit")
      THROW(COAL_YARD_TURNOUT)
      GREEN(COAL_YARD_SIGNAL_3)
   
   // As above with auto generated IDs
   ALIAS(COAL_YARD_TURNOUT)
   ALIAS(COAL_YARD_SIGNAL_3)

   ROUTE(1,"Coal yard exit")
      THROW(COAL_YARD_TURNOUT)
      GREEN(COAL_YARD_SIGNAL_3)

Refer to :ref:`ex-rail/ex-rail-reference:aliases` for more information.

Alias names:

- **Must not** be an existing EX-RAIL command name or other reserved word.
- **Should be** reasonably short but descriptive.
- **Must start** with letters A-Z/a-z, 0-9 or underscore _ .
- **May then** also contain numbers.
- **Must not** contain spaces or special characters.
   

Including sub-files
===================

If you find your myAutomation.h file becoming quite lengthy and cumbersome to scroll through and keep track of, you can break your items up into multiple smaller files, and include those in your myAutomation.h file instead.

There are some rules that apply in this scenario:

* Anything that needs to be done when the CommandStation starts must be defined first.
* Any custom macros/commands must be defined before they are used (see `make your own ex-rail macro or command`_) below.
* The files are included in the order defined, so if an item in one file depends on another file's item, make sure they included in the correct order.

Some suggestions to get the most out of this:

* Define everything that needs to happen on startup directly in myAutomation.h, before any other includes.
* Have a specific file for your custom macros or commands (eg. myMacros.h) and include this before other includes.
* Have a specific file for all your aliases (eg. myAliases.h).
* Group other items logically according to their purpose, eg. myTurnouts.h to define all your turnouts, and myShuttle.h to define an automated shuttle sequence.
* Remember the rules and ensure files are included in the correct order to prevent dependency issues, which will lead to errors when compiling and uploading.

For example:

.. code-block:: cpp

   ROUTE(1,"Coal yard exit")
      THROW(19)
      GREEN(27)
      DONE
   #include "myFireEngineLights.h"
   #include "myShuttle.h"

Realistic turnout sequences 
===========================

Let's say you want to create a turnout that is connected to some signals and you want a more realistic sequence with time delays as if the signalman has to move from lever to lever. This can be readily achieved in EX-RAIL but you really want the turnout to appear normal in your throttle. To do this you can create two complimentary turnout definitions:

1. An invisible turnout definition which actually controls the turnout hardware. This can be a pin, servo, DCC, or whatever technology, but is created using the HIDDEN keyword (see example below) instead of a description. This will not show up in throttles or be shown to |JMRI|. 
2. A virtual turnout. This turnout will have an ID and description, will show up in throttles and |JMRI|, but has no hardware or electronics associated with it. 

Once these are defined, you can then use EX-RAIL's ONTHROW/ONCLOSE commands to intercept the throttle/JMRI/EX-RAIL sequence changing the virtual turnout which then runs the sequence of your choice. This will normally involve throwing or closing the invisible (but real) turnout.

For example:

.. code-block:: cpp

   SERVO_TURNOUT(101, 121, 133, 456, Slow, HIDDEN)    // Define the real, physical turnout, in this case a servo driven turnout, note it is HIDDEN from throttles/JMRI.
   VIRTUAL_TURNOUT(9101,"Coal yard exit")       // Define the virtual turnout, which will be visible to throttles/JMRI.

   ONTHROW(9101)                                // When throwing the virtual turnout:
   RED(MainlineSignal)                          // Set a red signal.
   DELAY(5000)                                  // Wait for the signalman to move to the turnout lever.
   THROW(101)                                   // Throw the real turnout.
   DELAY(7500)                                  // Wait again for the signalman to move to the other signal lever.
   GREEN(ShuntingSignal)                        // Set a green signal.
   DONE

   ONCLOSE(9101)                                // When closing the virtual turnout:
   GREEN(MainlineSignal)                        // Set a green signal.
   DELAY(5000)                                  // Wait for the signalman to move to the turnout lever.
   CLOSE(101)                                   // Close the real turnout.
   DELAY(7500)                                  // Wait again for the signalman to move to the other signal lever.
   RED(ShuntingSignal)                          // Set a red signal.
   DONE

A virtual turnout may be used in any circumstance where the turnout process is handled in EX-RAIL rather than the normal process, for example a solenoid turnout requiring a pin or relay to be manipulated.

Make your own EX-RAIL macro or command
======================================

One of the cunning features of EX-RAIL is enabling users to define macros, or what is effectively your very own EX-RAIL command.

To do this, you're actually making use of some C++ code in addition to the clever programming in DCC++ EX.

(Yes, we just called ourselves cunning and clever. Our talent is superseded only by our modesty ;) )

The way to implement this is as follows:

.. code-block:: cpp

   #define MYMACRO(parameter1, parameter2, parameter3, ...) \
   COMMAND(parameter1) \
   COMMAND(parameter2) \
   COMMAND(parameter3) \
   DONE

Firstly, note the "#define". This is a directive in C++ that tells the compiler to process all this when you compile and upload the CommandStation software.

The entire macro needs to be on a single line, hence the addition of the backslash "\\" at the end of each line in the macro, except after the final DONE. This backslash simply tells the compiler to treat these as the same line while allowing things to be more readable for us humans.

Here's an example for driving single coil Rokuhan turnouts that require the coil to be activated for a very short time in order to CLOSE or THROW the turnout, which will be explained below.

.. code-block::

  // Define a pulse time of 50ms to activate the coil
  #define PULSE 50

  // Define a macro called ROKUHANTURNOUT which creates various objects and event handlers for turnouts
  // This macro:
  // Defines a pin turnout
  // Defines an alias
  // Sets the direction pin and sends the pulse for the CLOSE command
  // Resets the direction pin and sends the pulse for the THROW command
  #define ROKUHANTURNOUT(t, p1, p2, desc, ali) \
  PIN_TURNOUT(t, 0, desc) \
  ALIAS(ali, t) \
  DONE \
  ONCLOSE(t) \
  SET(p1) \
  SET(p2)DELAY(PULSE)RESET(p2) \
  DONE \
  ONTHROW(t) \
  RESET(p1) \
  SET(p2)DELAY(PULSE)RESET(p2) \
  DONE

  ROKUHANTURNOUT(105, 168, 176, "Yard entrance", YD_E)  // Define the "Yard entrance" turnout with turnout ID 5 using MCP23017 pins 168/176, and create alias YD_E

Typically, you would define a pin turnout with the PIN_TURNOUT command, however in this example we need a CLOSE or THROW sent to these turnouts to do more than just set a pin high or low, hence the need for the macro.

Here's the line by line explanation:

* A pulse time of 50ms reliably switches the turnouts.
* Define the ROKUHANTURNOUT macro, providing parameters for the turnout ID, direction pin, enable or pulse pin, a description, and an alias name.
* Create a PIN_TURNOUT that is advertised to WiThrottles using the provided turnout ID and description, with the pin set to 0 as this is not used.
* Create the provided alias for the turnout ID.
* The first DONE is required because we need to separate the turnout and alias definitions from the ONCLOSE and ONTHROW actions.
* Define what happens when a CLOSE command is sent to that turnout ID.
* Setting the direction pin high will result in closing the turnout.
* Set the enable or pulse pin high, wait for our pulse time, then reset it again, which will actually close the turnout.
* The DONE is required to tell EX-RAIL not to proceed any further.
* Define what happens when a THROW command is sent to that turnout ID.
* Resetting the direction pin will result in throwing the turnout.
* Set the enable or pulse pin high, wait for our pulse time, then reset it again, which will actually throw the turnout.
* The DONE is required to tell EX-RAIL not to proceed any further.
* Finally, use the macro to create the "Yard entrance" turnout with turnout ID 105, pins 168/176 on an MCP23017 I/O expander, and an alias of YD_E that can be referred to in other sequences.

This technique can be used in many different ways limited only by your imagination to have EX-RAIL perform many different actions and automations.

