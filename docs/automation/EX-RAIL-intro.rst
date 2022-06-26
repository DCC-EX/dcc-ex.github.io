***********************************
Introduction to EX-RAIL Automation
***********************************

.. attention::
   17 Feb 2022: *Now included* in **DCC++EX 4.0!**
   Available to download and use now!

.. sidebar:: On this page

   .. contents:: 
      :depth: 1
      :local:

Introduction
==============

EX-RAIL is an "**EX**\tended **R**\ailroad **A**\utomation **I**\nstruction **L**\anguage"
that can easily be used to describe sequential actions to automatically take place on your model layout. These actions are defined programmatically in a simple command script file, and uploaded to the Command Station once to configure it. EX-RAIL will then run automatically on CS startup.

To begin, let's define a few terms:

**SEQUENCE** - Simply a list of things to be done in order. These things might be to actually drive a train around, or merely to set some turnouts or flash some scene or panel lights. Actions can be made to wait for conditions to be met, like a sensor detecting a train, a button being pushed, or a period of time elapsing.

**ROUTE** - A SEQUENCE that is made visible to a throttle with a readable name so the user can press a button to get the sequence executed. This might be best used to set a series of turnouts and signals to create a route through the layout.

**AUTOMATION** - A SEQUENCE that is made visible to a throttle so that a user can hand over a loco and let EX-RAIL drive the train away, following each step listed in the sequence.

Most people wanting to do animations or run trains through an automated route will use a SEQUENCE, but those with :doc:`throttles </throttles/index>` that support it (:doc:`/throttles/engine-driver`, :doc:`WebThrottle-EX </throttles/ex-webthrottle>`) can add routes and automations. Both of these terms are just tags that let throttles with this feature automatically assign sequences to control buttons. "Routes" go into route buttons and can set turnouts, signals, etc., so you can drive your train along that route. "Automations" can appear on a "handoff" button that will supply or handoff the Loco ID to EX-RAIL where it can take over and run the train autonomously. An automation example would be manually driving a train into a station and pressing the assigned handoff button in the throttle that runs an AUTOMATION to take it on a journey around the layout.

Things You Can Do With EX-RAIL
====================================

- Create "Routes" which set multiple turnouts and signals at the press of a button in WebThrottle-EX or EngineDriver (other WiThrottle-compatible throttles are available)
- Automatically drive multiple trains simultaneously, and manage complex interactions such as single line working and crossovers by setting up "Automations"
- Drive trains manually, and hand a train over to an Automation
- Animate accessories such as lights, crossings, or cranes
- Intercept turnout changes to automatically adjust signals or other turnouts
- Turn on the coffee pot when the train reaches the station

.. sidebar:: A note from the Author

   My original aim was to see if I could create an automated layout with lots going on, that didn’t just run around in circles. Having looked at JMRI (briefly, I must say) and DCC++, I began to wonder whether I could actually make a simpler automation system, and run it entirely on the Arduino used for DCC++.

   Some of the automation techniques I read about, using Jython scripts in JRMI, seem to require extensive programming skills and complex table configurations which appeared awkward to me, despite my years of programming in dozens of languages.

   It seemed to me that basing an automation on block occupancy detection leaves a lot of complex technical problems to be solved… and wanting to be cheap, I didn’t want to invest in a range of block occupancy detectors, or ABC braking modules, which are all very well on circular layouts, but not good at complex crossings or single line operations with passing places. Also, I didn’t want the automation to be an obvious cycle of movements… some random timings and decisions need to be introduced so that two trains don’t always arrive at the same place in the same order, nor go on the same journey in a predictable cycle.

   By reversing the usual assumptions, I think I have a workable, extensible and cheap solution.
   
   Because the original DCC++ used a software design inappropriate for internal automation, I had to start by rewriting the entire Command Station code and this became DCC-EX, so automation has been in the plan from the start.

   - Chris Harlow

What You Don't Need
====================

While extra functionality may be attained by using additional tools and applications, to get the benefit of EX-RAIL you don't need anything more than a *DCC-EX Command Station, and the Arduino IDE* used to configure it.

You DON'T need:

- JMRI, or any additional utilities
- EngineDriver, or any other WiThrottle app
- A separate computer living under your layout
- Knowledge of C++ or Python/Jython programming

How It Works
=============

A small amount of code in the CS, the EX-RAIL executor, lets you write an automation script in the form of simple, easy to use text commands that it interprets and runs on your layout. You don't have to be a programmer and you don't have to learn code. You simply add your own myAutomation.h file in the same program you use to upload the Command Station Software to your Arduino (the Arduino IDE, PlatformIO, etc). This means that you already have all the tools you will need, and there is nothing else to download or install. The method of creating your script file is described in the next section.

The EX-RAIL code is surprisingly small and requires very little PROGMEM (memory that holds the program code) or SRAM (the runtime workspace that stores variables and things the program needs) to operate. However, you will still need a Mega for your CS; the UNO and Nano memory is simply too small to include EX-RAIL with the rest of the Command Station code.

EX-RAIL automation is *much* (perhaps 2 orders of magnitude) more time efficient than the code required to process incoming requests from an external automation processor, or the continuous polling of every sensor.

.. note:: The EX-RAIL code is only included in the compilation of the Command Station if the compiler detects a “myAutomation.h” file. If you don't create that file, no extra space is wasted for something you don't use.

The Automation Process
=======================

Once started, all sequences step through a list of simple keywords until they reach a ``DONE`` keyword.

There can be a startup sequence (keywords at the beginning of the script), which if present is automatically executed, as are any sequences that contain an ``AUTOSTART``.

.. note:: 

   There is an implied AUTOSTART whereby everything in myAutomation.h prior to the first ``DONE`` keyword is executed on startup. If you don't wish anything to happen at startup, simply add the keyword ``DONE`` as the first line.

Multiple concurrent sequences are supported.

For a full list of keywords, see :doc:`EX-RAIL-summary`, and for further detailed information, see the :doc:`/automation/EX-RAIL-reference`.

The script containing your sequences is added to your Command Station by creating a file called "myAutomation.h" in the same folder as CommandStation-EX.ino.

Connecting your Arduino and pressing the Upload button in the usual way will save the file and upload your script into the Command Station.

To create the myAutomation.h file in the Arduino IDE, use the pulldown button and select New Tab (or simply press Ctrl+Shift+N).

.. image:: ../_static/images/ex-rail/setup1.jpg
   :alt:  Setup pulldown button
   :align: center
   :scale: 100%

.. image:: ../_static/images/ex-rail/setup2.jpg
   :alt:  Setup pulldown menu
   :align: center
   :scale: 100%

Enter the file name "myAutomation.h" (This is case sensitive)

.. image:: ../_static/images/ex-rail/setup3.jpg
   :alt:  Setup myAutomation.h
   :align: center
   :scale: 100%

And type your script in.

.. image:: ../_static/images/ex-rail/setup4.jpg
   :alt:  Setup Example file
   :align: center
   :scale: 100%


Some Simple Examples  
======================

Example 1: Creating Routes for a Throttle
__________________________________________

A typical Route might be used to set a series of turnouts in response to a single button in a throttle.
The EX-RAIL instructions to do this might look like

.. code-block:: cpp

   ROUTE(1,"Coal Yard exit")
     THROW(1)
     CLOSE(7)
     DONE

Or you can write it like this

.. code-block:: cpp

   ROUTE(1,"Coal Yard exit")  THROW(1)  CLOSE(7)  DONE

Or add comments

.. code-block:: cpp

 // This is my coal yard to engine shed route
   ROUTE(1,"Coal Yard exit")     // appears in the throttle
     THROW(1)   // throw turnout onto coal yard siding
     CLOSE(7)   // close turnout for engine shed
     DONE    // that's all folks!

Of course, you may want to add signals, and time delays

.. code-block:: cpp

   SIGNAL(77,78,79)  // see the Defining Signals section
   SIGNAL(92,0,93)   //      below for details
   
   ROUTE(1,"Coal Yard exit")
      RED(77)
      THROW(1)
      CLOSE(7)
      DELAY(5000)  // this is a 5 second wait
      GREEN(92)
      DONE


Example 2: Automating Signals with Turnouts
____________________________________________

By intercepting a turnout change command, it's easy to automatically adjust signals or 
automatically switch an adjacent facing turnout. Use an ``ONTHROW`` or ``ONCLOSE`` keyword to detect a particular turnout change:

.. code-block:: cpp

   ONTHROW(8)  // When turnout 8 is thrown,
      THROW(9)  // must also throw the facing turnout
      RED(24)
      DELAY(2000)
      GREEN(27)
      DONE

   ONCLOSE(8)  // When turnout 8 is closed
     CLOSE(9)
     RED(27)
     DELAY(2000)
     GREEN(24)
     DONE

Defining Turnouts
==================

DCC-EX supports a number of different turnout hardware configurations, but your automation treats them all as simple ID numbers. Turnouts may be defined using ``<T>`` commands from JMRI, or in ``SETUP("<T ...>")`` commands placed in your mySetup.h file, or C++ code in mySetup.h, just like earlier versions.

You may, however, find it more convenient to define turnouts using EX-RAIL commands, which may appear anywhere in the 'myAutomation.h' file, even after they are referenced in an ``ONTHROW``, ``ONCLOSE``, ``THROW`` or ``CLOSE`` command. (EXRAIL extracts the turnout definitions just once from your script at Command Station startup.)

Turnouts defined in 'myAutomation.h' will still be visible to WiThrottle and JMRI in the normal way.

A TURNOUT sends DCC signals to a decoder attached to the track, a PIN_TURNOUT sends a "throw" or "close" (5V or 0V signal) to a pin on the Arduino, and a SERVO_TURNOUT sends an I2C serial command to a servo board connected to your servos.
 
See the :doc:`/automation/EX-RAIL-summary` page for TURNOUT, PIN_TURNOUT and SERVO_TURNOUT definitions.


Defining Signals
=================

Signals can now simply be a decoration to be switched by the route process; they don’t need to control anything.

``GREEN(55)`` would turn signal 55 green, and ``RED(55)`` would turn it red. Somewhere in the script there must be a SIGNAL command like this: ``SIGNAL(55,56,57)``.  This defines a signal with ID 55, where the Red/Stop lamp is connected to pin 55, the Amber/Caution lamp to pin 56, and the Green/Proceed lamp to pin 57. The pin allocations do not need to be contiguous, and the red pin number is also used as the signal ID. Thus you can change the signal by ``RED(55)``, ``AMBER(55)``, or ``GREEN(55)``. This means you don't have to manually turn off the other lamps. A RED/GREEN only signal may be created with a zero amber pin.


Example 3: Automating various non-track items 
______________________________________________

This normally takes place in a timed loop, for example alternate flashing of a fire engine's lights. To do this use a SEQUENCE.

.. code-block:: cpp

   SEQUENCE(66)  
     SET(101)   // sets output 101 HIGH
     RESET(102) // sets output 102 LOW
     DELAY(500)   // wait 0.5 seconds
     SET(102)   // swap the lights   
     RESET(101) 
     DELAY(500)   // wait 0.5 seconds
     FOLLOW(66)  // follow sequence 66 continuously
     
Note, however, that this sequence will not start automatically: it must be started during the startup process (see later) using ``START(66)``.

Example 4: Automating a train (simple loop)
____________________________________________

Start with something as simple as a single loop of track with a station and a sensor (connected to pin 40 for this example) at the point where you want the train to stop.

.. image:: ../_static/images/ex-rail/Example_4_diagram.png
   :alt:  Simple example 4
   :align: center
   :scale: 100%

Using an ``AUTOMATION`` keyword means that this automation will appear in the throttle so you can drive the train manually, and then hand it over to the automation at the press of a button.

\* Technically, an automation can independently run multiple locos along the same path through the layout, but this is discussed later...

.. code-block:: cpp

   AUTOMATION(4,"Round in circles")
      FWD(50)   // move forward at DCC speed 50 (out of 127)
      AT(40)     // when you get to sensor on pin (40)
      STOP      // stop the train 
      DELAYRANDOM(5000,20000) // delay somewhere between 5 and 20 seconds
      FWD(30)   // start a bit slower
      AFTER(40)  // until sensor on pin 40 has been passed
      FOLLOW(4) // and continue to follow the automation

The instructions are followed in sequence by the loco given to it; the ``AT`` command just leaves the loco running until that sensor is detected.

Notice that this automation does not specify the loco address. If you drive a loco with the throttle and then hand it over to this automation, then the automation will run with the loco you last drove.

Example 5: Signals in a train script
_____________________________________

Adding a station signal to the loop script is extremely simple, but it does require a mind-shift for some modellers who like to think in terms of signals being in control of trains! EX-RAIL takes a different approach, by animating the signals as part of the driving script. Thus set a signal GREEN before moving off (and allow a little delay for the driver to react) and RED after you have passed it.

.. code-block:: cpp

   SIGNAL(77,78,79)  // see the Defining Signals section above for details
   AUTOMATION(4,"Round in circles")
      FWD(50)   // move forward at DCC speed 50 (out of 127)
      AT(40)    // when you get to sensor on pin (40)
      STOP      // Stop the train 
      DELAYRANDOM(5000,20000) // delay somewhere between 5 and 20 seconds
      GREEN(77)    // set signal #77 to Green
      DELAY(2500)  // This is not Formula1!
      FWD(30)    // start a bit slower
      AFTER(40)  // until sensor on pin 40 has been passed
      RED(77)    // set signal #77 to Red
      FOLLOW(4)  // and continue to follow the automation

Example 6: Single line shuttle
_______________________________

Consider a single line, shuttling between stations A and B.

.. image:: ../_static/images/ex-rail/Example_6_diagram.png
   :alt:  Simple example 4
   :align: center
   :scale: 100%

Starting from Station A, the steps may be something like:

-  Wait between 10 and 20 seconds for the guard to stop chatting up the girl in the ticket office.
-  Move forward at speed 30
-  When I get to B, stop.
-  Wait 15 seconds for the tea trolley to be restocked
-  Move backwards at speed 20
-  When I get to A, stop.


Notice that the sensors at A and B are near the ends of the track (allowing for braking distance, but don’t care about train length or whether the engine is at the front or back.) We have wired sensor A on pin 41, and sensor B on pin 42 for this example.

.. code-block:: cpp

    SEQUENCE(13)
      DELAYRANDOM(10000,20000) // random wait between 10 and 20 seconds
      FWD(50)
      AT(42) // sensor 42 is at the far end of platform B
      STOP
      DELAY(15000)
      REV(20) // Reverse at DCC speed 20 (out of 127)
      AT(41) // far end of platform A
      STOP
      FOLLOW(13) // follows sequence 13 again… forever


Note a SEQUENCE is exactly the same as an AUTOMATION except that it does NOT appear in the throttle.

When the Command Station is powered up or reset, EX-RAIL starts operating at the beginning of the file.  For this sequence we need to set a loco address and start the sequence:

.. code-block:: cpp

   SENDLOCO(3,13) // Start sequence 13 using loco 3
   DONE           // This marks the end of the startup process

The sequence can also be started from a serial monitor with the command ``</ START 3 13>``.


If you have multiple separate sections of track which do not require inter-train cooperation, you may add many more separate sequences and they will operate independently.

Although the above is trivial, the routes are designed to be independent of the loco address so that we can have several locos following the same route at the same time (not in the end to end example above!), perhaps passing each other or crossing over with trains on other routes.

The example above assumes that loco 3 is sitting on the track and pointing in the right direction. A bit later you will see how to script an automatic process to take whatever loco is placed on the programming track, and send it on its way to join in the fun!

Example 7: Running multiple inter-connected trains
___________________________________________________

So what about routes that cross or share single lines (passing places etc)?
Let's add a passing place between A and B. S= Sensors, T=Turnout
number. So now our route looks like this:

.. image:: ../_static/images/ex-rail/Example_7a_diagram.png
   :alt:  Simple example 4
   :align: center
   :scale: 100%

Assuming that you have defined your turnouts with :ref:`TURNOUT commands. <automation/EX-RAIL-summary:Automations, Routes and Sequences>`

.. code-block:: cpp

   SEQUENCE(11)
      DELAYRANDOM(10000,20000) // random wait between 10 and 20 seconds
      CLOSE(1)
      CLOSE(2)
      FWD(30)
      AT(42) // sensor 42 is at the far end of platform B
      STOP
      DELAY(15000)
      THROW(2)
      THROW(1)
      REV(20)
      AT(41)
      STOP
      FOLLOW(11) // follows sequence 11 again… forever

 
All well and good for one loco, but with 2 (or even 3) on this track we need some rules. The principle behind this is

-  To enter a section of track that may be shared, you must RESERVE it. If you cant reserve it because another loco already has, then you will be stopped and the script will wait until such time as you can reserve it. When you leave a shared section you must free it.

-  Each “section” is merely a logical concept, there are no electronic section breaks in the track. You may have up to 255 sections (more can be supported by a code mod if required).


So we will need some extra sensors (hardware required) and some logical blocks (all in the mind!):

.. image:: ../_static/images/ex-rail/Example_7b_diagram.png
   :alt:  Simple example 4
   :align: center
   :scale: 100%

We can use this diagram to plan routes. When we do so, it will be easier to imagine 4 separate mini routes, each passing from one block to the next. Then we can chain them together to form a full route, but also start from any block.

So… lets take a look at the routes now. For convenience I have used route numbers that help remind us what the route is for.

.. code-block:: cpp

   SEQUENCE(12) // From block 1 to block 2
      DELAYRANDOM(10000,20000) // random wait between 10 and 20 seconds
      RESERVE(2) // we wish to enter block 2… so wait for it
      CLOSE(1) // Now we “own” the block, set the turnout
      FWD(30) // and proceed forward
      AFTER(71) // Once we have reached AND passed sensor 71
      FREE(1) // we no longer occupy block 1
      AT(72) // When we get to sensor 72
      FOLLOW(23) // follow route from block 2 to block 3
   
   SEQUENCE(23) // Travel from block 2 to block 3
      RESERVE(3) // will STOP if block 3 occupied
      CLOSE(2) // Now we have the block, we can set turnouts
      FWD(20) // we may or may not have stopped at the RESERVE
      AT(42) // sensor 2 is at the far end of platform B
      STOP
      FREE(2)
      DELAY(15000)
      FOLLOW(34)
   
   SEQUENCE(34) // you get the idea
      RESERVE(4)
      THROW(2)
      REV(20)
      AFTER(73)
      FREE(3)
      AT(74)
      FOLLOW(41)
   
   SEQUENCE(41)
      RESERVE(1)
      THROW(1)
      REV(20)
      AT(41)
      STOP
      FREE(4)
      FOLLOW(12) // follows Route 12 again… forever


Does that look long? Worried about memory on your Arduino…. Well the script above takes about 100 BYTES of program memory and no dynamic SRAM!

If you follow this example carefully, you'll see it allows for up to 3 trains at a time, because one of them will always have somewhere to go. Notice that there is a common theme to this…

-  RESERVE where you want to go. If you are moving and the reserve fails, your loco will STOP and the reserve waits for the block to become available. \*These waits and the manual WAITS do not block the Arduino process… DCC and the other locos continue to follow their routes!

-  Set the points to enter the reserved area. Do this ASAP, as you may be still moving towards them. 
   
-  Set any signals.

-  Move into the reserved area.

-  Reset your signals.

-  Free off your previous reserve as soon as you have fully left the block.

In addition, it is possible to take decisions based on blocks reserved by other trains. The IFRESERVE(block) can be used to reserve a block if it's not already reserved by some other train, or skip to the matching ENDIF. For example, this allows a train to choose which platform to stop at based on prior occupancy. It is features like this that allow for more interesting and unpredictable automations.       

Starting the system
====================

Starting the system is tricky, because we need to place the trains in a suitable position and set them going. We need to have a starting position for each loco, and reserve the block(s) it needs to keep other trains from crashing into it.

.. warning:: This EX-RAIL version isn’t ready to handle locos randomly placed on the layout after a power down!

For a known set of locos, the easiest way is to define the startup process at the beginning of the script. E.g. for two engines, one at each station.

.. code-block:: cpp

 // ensure all blocks are reserved as if the locos had arrived there
 RESERVE(1) // start with a loco in block 1
 RESERVE(3) // and another in block 3
 SENDLOCO(3,12) // send Loco DCC addr 3 on to route 12
 SENDLOCO(17,34) // send loco DCC addr 17 to route 34
 DONE // don’t drop through to the first sequence definition that follows in the script file

.. hint:: Some interesting points about the startup:

 * You don’t need to set turnouts, because each route is setting them as required.
 * Signals default to RED on power up, and get turned GREEN when a route clears them.


Drive-Away feature
===================

EX-RAIL can switch a track section between programming and mainline.

Here for example is a launch sequence that has no predefined locos but allows locos to be added at station 1 while the system is in motion. Let’s assume that the track section at Station1 is isolated and connected to the programming track power supply. Also that we have a “launch” button connected where sensor 17 would be and an optional signal (i.e. 3 LEDs) on the control panel connected where signal 27 would be.

.. code-block:: cpp

 SEQUENCE(99)
   SIGNAL(27,28,29)
   RED(27)   // indicate launch not ready
   AFTER(17) // user presses and releases launch button
   UNJOIN    // separate the programming track from main
   DELAY(2000)
   AMBER(27) // Show amber, user may place loco
   AFTER(17) // user places loco on track and presses “launch” again
   READ_LOCO // identify the loco
   GREEN(27) // show green light to user
   JOIN      // connect prog track to main
   START(12) // send loco off along route 12
   FOLLOW(99) // keep doing this for another launch

The READ_LOCO reads the loco address from the PROG track and the current route takes on that loco. By altering the script slightly and adding another sensor, it’s possible to detect which way the loco sets off and switch the code logic to send it in the correct direction by using the INVERT_DIRECTION instruction so that this locos FWD and REV commands are reversed. (easily done with diesels!)

Roster entries
===============

EX-RAIL has a ROSTER() function to allow you to define all of your locomotives with a list of their defined functions which is advertised to WiThrottle applications, just like turnouts and routes.

The functions can simply be listed as "F" numbers, or you can provide a text description of the function. Prefacing the function with a "*" indicates it is momentary, meaning it is only activated while holding that function button down.

A very simple roster entry for a loco with ID 1506 called "HUSA" with three functions of light, bell, and momentary horn would look like this:

.. code-block:: cpp
   
   ROSTER(1506, "HUSA", "Light/Bell/*Horn")

A more complex example with generic functions for the same loco (note the momentary F2 for horn):

.. code-block:: cpp

   ROSTER(1506, "HUSA", "F0/F1/*F2/F3/F4/F5/F6/F7/F8/F9/F10/F11/F12/F13/F14/F15/F16/F17/F18/F19/F20/F21/F22/F23/F24/F25/F26/F27/F28")

The same again, with more text functions defined to represent a number of different sounds:

.. code-block:: cpp

   ROSTER(1506, "HUSA", "Lights/Bell/*Horn/Air/Brake/Coupling/Compressor/Sand/Mute/F9/F10/F11/F12/F13/F14/F15/F16/F17/F18/F19/F20/F21/F22/F23/F24/F25/F26/F27/F28")

Sounds
=======

You can use ``FON(n)`` and ``FOFF(n)`` to switch loco functions… eg sound horn.

Sensors
========

- DCC++EX allows for sensors that are **Active Low or Active High**. This is particularly important for IR sensors that have been converted to detect by broken beam, rather than reflection. By making the sensor number negative, the sensor state is inverted. e.g. ``AT(-5)``.

- Magnetic/Hall effect sensors work for some layouts, but beware of how you detect the back end of a train approaching the buffers in a siding, or knowing when the last car has cleared a crossing.

- Handling sensors in the automation is made easy because EX-RAIL throws away the concept of interrupts (“oh… sensor 5 has been detected… which loco was that and whatever do I do now?”) and instead has the sequences work on the basis of “do nothing, maintain speed until sensor 5 triggers, and then carry on in the script”.

- Sensor numbers are direct references to VPINs (virtual pin numbers) in the Hardware Abstraction Layer. For a Mega onboard GPIO pin, this is the same as the digital pin number. Other pin ranges refer to I/O expanders etc. 

- Sensors with ID's 0 to 255 may be LATCHED/UNLATCHED in your script. If a sensor is latched on by the script, it can only be set off by the script… so ``AT(5) LATCH(5)`` for example effectively latches the sensor 5 on when detected once.

- Sensor polling by JMRI is independent of this, and may continue if ``<S>`` commands are used.


Outputs
========

- Generic Outputs are mapped to VPINs on the HAL (as for sensors)
- SIGNAL definitions are just groups of 3 Output pins that can be more easily managed.

Sequence Numbers
=================

- All ROUTE / AUTOMATION / SEQUENCE ids are limited to 1 - 32767
- 0 is reserved for the startup sequence appearing as the first entry in the EXRAIL script. 

Tips and Techniques
===================

Below are some tips and techniques you can implement to get the most out of EX-RAIL.

Defining names for any ID numbers (aliases)
____________________________________________

Use the ``ALIAS()`` command in your script to make IDs a bit more human friendly, and easier to refer to later. This can be defined before or after it is used.

Refer to :ref:`automation/ex-rail-reference:aliases` for more information.

Alias names:

- **Must not** be an existing EX-RAIL command name or other reserved word.
- **Should be** reasonably short but descriptive.
- **Must start** with letters A-Z/a-z or underscore _ .
- **May then** also contain numbers.
- **Must not** contain spaces or special characters.
   
For example:

.. code-block:: cpp

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

Including sub-files
____________________

If you find your myAutomation.h file becoming quite lengthy and cumbersome to scroll through and keep track of, you can break your items up into multiple smaller files, and include those in your myAutomation.h file instead.

There are some rules that apply in this scenario:

* Anything that needs to be done when the CommandStation starts must be defined first.
* Any custom macros/commands must be defined before they are used (see :ref:`automation/ex-rail-intro:make your own ex-rail macro or command`) below.
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

Realistic turnout sequeunces
_____________________________

Let's say you want to create a turnout that is connected to some signals and you want a more realistic sequence with time delays as if the signalman has to move from lever to lever. This can be readily achieved in EX-RAIL but you really want the turnout to appear normal in your throttle. To do this you can create two complimentary turnout definitions:

1. An invisible turnout definition which actually controls the turnout hardware. This can be a pin, servo, DCC, or whatever technology, but is created using the HIDDEN keyword (see example below) instead of a description. This will not show up in throttles or be shown to JMRI. 
2. A virtual turnout. This turnout will have an ID and description, will show up in throttles and JMRI, but has no hardware or electronics associated with it. 

Once these are defined, you can then use EX-RAIL's ONTHROW/ONCLOSE commands to intercept the throttle/JMRI/EX-RAIL sequence changing the virtual turnout which then runs the sequence of your choice. This will normally involve throwing or closing the invisible (but real) turnout.

For example:

.. code-block:: cpp

   SERVO_TURNOUT(101, 121, 133, 456, HIDDEN)    // Define the real, physical turnout, in this case a servo driven turnout, note it is HIDDEN from throttles/JMRI.
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
_______________________________________

One of the cunning features of EX-RAIL is enabling users to define macros, or what is effectively your very own EX-RAIL command.

To do this, you're actually making use of some C++ code in addition to the clever programming in DCC++ EX.

(Yes, we just called ourselves cunning and clever. Our talent is superceded only by our modesty ;) )

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

  // Define a pulse time of 25ms to activate the coil
  #define PULSE 2

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

* A pulse time of 25ms reliably switches the turnouts.
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

Why Can't I Put a Script on an SDCard?
=======================================

From time to time, we are asked why we can't put automation scripts (the contents of a myAutomation.h file) on an SDCard or load it into EEPROM storage on the Arduino. This is not possible, and as you will see in the last paragraph of this section, would not provide much of a benefit. For you Engineers and advanced Tinkerers:

1) Being able to read an SD card on the arduino platforms requires a significant amount of code because there is no operating system or file system which we would take for granted on a PC. We simply don't have enough free memory on an Arduino to hold that code. The same problems exist for using EEPROM.   


2) myAutomation.h is actually generating compiled code as an integral part of the CS. To have this file loaded separately at run time would require that the CS contained all the code necessary to read the file and interpret the contents. This would be a significant additional code burden on the CS (>1000 lines of code) and also require huge amounts of precious RAM to store the interpreted version of the file because it cannot be written into flash memory at run time.   


3) By compiling the code on your pc, you have the advantage of the vast majority of syntax errors being detected by the compiler (albeit somewhat opaquely) rather than having to move the SDCard to the CS before discovering an issue.   


4) The current implementation requires no additional PC code/tool download or installation. If you are able to setup your CS, you already have everything you need to add your myAutomation.


5) To implement an SD card solution requires a user to have access to the CS, which could involve climbing under their layout, opening the CS case if you have one, dismounting the motor shield to get access to the SDCard slot, potentially damaging the CS, the layout, or your body, etc. The card would have to be placed into a computer, an editor opened, the file edited and saved, and then the process reversed to get the SDCard back into the CS.

In contrast... with the current system: One takes the end of the USB cable that has been thoughtfully left connected to the CS and plugs it into ones laptop. The Arduino IDE (or suitable alternative) is opened and the myAutomation.h files is edited. A SINGLE CLICK on the upload button is sufficient to save the file, check it for errors, upload to the CS and restart the CS. 

As more powerful processors become available and affordable, we may find other ways to handle saving settings and adding automations, but the current method, as you can see, is efficient, easy to use, and fast.

