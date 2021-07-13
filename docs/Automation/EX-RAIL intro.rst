***********************
EX-RAIL Automation
***********************

|

Introduction
***********************

EX-RAIL is an **EX**\panded **R**\ailroad **A**\utomation **I**\nstruction **L**\anguage
that can be easily used to describe sequential actions to automatically take place on your model layout.

|

Some of the things you can do with it:
========================

- Create "Routes" which set multiple turnouts and signals at the press of a button in Engine Driver (other Withrottle-compatible throttles are available)
- Intercept turnout changes to automatically adjust signals or other turnouts
- Animate accessories such as lights, crossings or cranes
- Automatically drive multiple trains simultaneously and manage complex interactions such as single line working and crossovers
- Drive trains manually and hand a train over to an automation

What you don't need:
====================

- You DON'T need JMRI or any additional utilities other than the Arduino IDE.
- You DON'T need Knowlege of C++ or Python/Jython programming

.. sidebar:: A note from the Author

   My original aim was to see if I could create an automated layout with lots going
   on that didn’t just run around in circles. Having looked at JMRI
   (briefly I must say) and DCC++ I began to wonder whether I could
   actually make a simpler automation system and run it entirely on the
   Arduino used for DCC++.

   Some of the automation techniques I read about using jython scripts in
   JRMI seem to require extensive programming skills and complex table configurations 
   which appeared awkward to me despite my years of programming in dozens of languages.

   It seemed to me that basing an automation on block occupancy detection leaves a 
   lot of complex technical problems to be solved… and wanting to be cheap,
   I didn’t want to invest in a range of block occupation detectors 
   or ABC braking modules which are all very well on
   circular layouts but not good at complex crossings 
   or single line operations with passing places. 
   Also I didn’t want the automation to be an obvious cycle of movements… 
   some random timings and decisions need to be introduced so
   that two trains don’t always arrive at the same place in the same order, 
   nor go on the same journey in a predictable cycle.

   By reversing the usual assumptions, I think I have a workable, extendable and cheap solution.
   
   Because the original DCC++ used a software design inappropriate for internal automation, I had to start by 
   rewriting the entire command station and this became DCC-EX, so 
   automation has been in the plan from the start.

How it works
=============

A small amount of code (The EX-RAIL executor) , sits between
the layout owner and DCC so that the layout owner can write automation
scripts in a form that is much more user friendly. In fact the
automation is written in the Arduino IDE (or PlatformIO) as per a normal
Arduino script but all the C++ boilerplate code is stripped away where
you don’t need to see or understand it. This means that you already have
all the tools you will need and there is nothing else to download or
install.

For memory/performance worriers… The EX-RAIL code is surprisingly
small and requires very little PROGMEM or RAM to execute although a UNO and Nano are
simply too small to include EX-RAIL with the rest of the Command Station code.
The EX-RAIL code is only
included in the compilation of the CommandStation if the compiler
detects a “myAutomation.h” file. 

During execution, an EX-RAIL automation is much
(perhaps 2 orders of magnitude) more time efficient than the code
required to process incoming requests from an external automation
processor.

The Automation Process
******************************************

All routes, automations etc step through a list of simple keywords until they reach a DONE
keyword. 

The reference list is here @KEBBIN? I also kept ENDTASK as alias of DONE

Automation scripts are added to your Command Station by creating a file called "myAutomation.h"
in the same folder as CommandStation-EX.ino and adding in the scripts 
as follows:

@KEBBIN Why doesnt this code block appear in the preview?????

.. code_block::

   EXRAIL
     ... your scripts
     ENDEXRAIL

Connecting your Arduino and pressing the upload button in the usual way
will save the file and upload your script into the command station.

@KEBBIN need pic of IDE adding a myAutomation.h file with some example content taken from below maybe. 


Here are some very simple examples  
**********************************

Example 1: Creating Routes for Engine Driver
=================================

A typical route might be to set a sequence of turnouts in response to a single button in Engine Driver.
The EX-RAIL instructions to do this might look like

.. code-block::

   ROUTE(1)
     THROW(1)
     CLOSE(7)
     DONE

or you can write it like this

.. code-block::

   ROUTE(1)  THROW(1)  CLOSE(7)  DONE

or add comments

.. code-block::

 // This is my coal yard to engine shed route
   ROUTE(1)     // appears as "Route 1" in Engine Driver
     THROW(1)   // Throw turnout onto coal yard siding
     CLOSE(7)   // close turnout for engine shed
     DONE    // thats all folks!

of course, you may want to add signals, and time delays

.. code-block::
   SIGNAL(77,78,79)  // see later for details
   SIGNAL(92,0,93)   // of signal definitions
   
   ROUTE(1)
      RED(77)
      THROW(1)
      CLOSE(7)
      DELAY(50)  // this is a 5 second wait
      GREEN(92)
      DONE


Example 2: Automating Signals with turnouts
===========================================
By intercepting a turnout change its easy to automatically adjust signals or 
automatically switch a facing turnout. Use an ONTHROW or ONCLOSE keyword to detect a particular turnout change:

.. code-block::

   ONTHROW(8)  // When turnout 8 is thrown
      THROW(9)  // must also throw the facing turnout
      RED(24)
      DELAY(20)
      GREEN(27)
      DONE

   ONCLOSE(8)  // When turnout 8 is closed
     CLOSE(9)
     RED(27)
     DELAY(20)
     GREEN(24)
     DONE

@KEBBIN, I'm not sure whether to include the defining turnouts and signals pars here before
the examples that use them or merely forward fererence them from the simple examples.

Defining Turnouts
*****************

DCC-EX++ supports a number of different 
turnout hardware configurations but your automation treats them all
as simple id numbers. Turnouts may be defined using <T> commands from JMRI
or in SETUP("<T ...>") commands or c++ code in mySetup.h as in earlier versions.

You may however find it more convenient to define turnouts using EX-RAIL
commands which may appear anywhere in the myAutomation.h file, even after they are
referenced in an ONTHROW, ONCLOSE, THROW or CLOSE command. 
Turnouts defined in myAutomation.h will still be visible to WiThrottle and JMRI in the normal way.
(@KEBBIN.. feature TODO  However it is possible with EX-RAIL to hide a turnout from Withrottle which is useful if
it is a facing turnout that will be automatically adjusted by your script to
match its partner.)
See reference section for TURNOUT definitions. 


Signals
========

Signals are now simply a decoration to be switched by the route process…
they don’t control anything.

``GREEN(55)`` would turn signal 55 green and ``RED(55)`` would turn it red.
Somewhere in the script there must be a SIGNAL command like this:
SIGNAL(55,56,57)  This defines a singal with ID 55 where the red/stop lamp is connected to 
pin 55, the amber/caution lamp to pin 56 and the green.proceed lamp to pin 57.
The pins do not need to be contiguous and the red pin is also used as the signal id. Thus  
you can change the signal by RED(55), AMBER(55) and GREEN(55).
This means you don't have to manually turn off the other lamps. 
A RED/GREEN only signal may be created with a zero amber pin.


Example 3: Automating various non-track items 
==============================================
This normally takes place in a timed loop, for example alternate flashing a 
fire engine's lights. To do this use a SEQUENCE.

.. code-block::

   SEQUENCE(66)  
     SET(101)   // sets output 101 HIGH
     RESET(102) // sets output 102 LOW
     DELAY(5)   // wait 0.5 seconds
     SET(102)   // swap the lights   
     RESET(101) 
     DELAY(5)   // wait 0.5 seconds
     FOLLOW(66)  // follow sequence 66 continuously
     
Note however that this sequence will not start automatically, it must be SCHEDULE'd
during the startup process (see later) using START(66)

Example 4: Automating a train (simple loop)
===========================================
     
Start with something as simple as a single loop of track with a station and a 
sensor (connected to pin 40 for this example) at the 
point where you want the train to stop.
Using an AUTOMATION keyword means that this automation will appear in Engine Driver so
you can drive the train manually, and then had it over to the automation at the press of a button.

[technically an automation can independently run multiple locos along the same path 
through the layout but this is discussed later]

.. code-block::

   AUTOMATION(4)
      FWD(50)   // move forward at DCC speed 50 (out of 127)
      AT(40)     // when you get to sensor on pin (40)
      STOP      // Stop the train 
      DELAYRANDOM(50,200) // delay somewhere between 5 and 20 seconds
      FWD(30)   // start a bit slower
      AFTER(40)  // until sensor on pin 40 has been passed
      FOLLOW(4) // and continue to follow the automation

The instructions are followed in sequence by the loco given to it,
the AT command just leaves the loco running until that sensor is
detected.

Notice that this automation does not specify the loco address. If you drive a loco with Engine Driver 
and then hand it over to this automation, then the automation will run with the loco you last drove.

Example 5: Signals in a train script
====================================

Adding a station signal to the loop script is extreemly simple but it does require a mind-shift
for some modellers who like to think in terms of signals being in 
control of trains. 
EX-RAIL takes a different approach, by animating the signals as part of
the driving script. Thus set a signal GREEN before setting off (and allow a little delay for the driver to react)
and RED after you have passed it.

.. code-block::

   SIGNAL(77,78,79)  // see later for details
   AUTOMATION(4)
      FWD(50)   // move forward at DCC speed 50 (out of 127)
      AT(40)     // when you get to sensor on pin (40)
      STOP      // Stop the train 
      DELAYRANDOM(50,200) // delay somewhere between 5 and 20 seconds
      GREEN(77)
      DEALY(25)  // This is not Formula1!
      FWD(30)   // start a bit slower
      AFTER(40)  // until sensor on pin 40 has been passed
      RED(77)
      FOLLOW(4) // and continue to follow the automation

Example 6: Single line shuttle
======================================
Consider a single line shuttling between stations A and B.

Starting from Station A, the steps may be something like:

-  Wait between 10 and 20 seconds for the guard to stop chatting up the
   girl in the ticket office.
-  Move forward at speed 30
-  When I get to B stop.
-  Wait 15 seconds for the tea trolley to be restocked
-  Move backwards at speed 20
-  When I get to A stop.


Notice that the sensors at A and B are near the ends of the track (allowing for braking
distance but don’t care about train length or whether the engine is at the front or back.)
We have wired sensor A on pin 41 and B on pin 42 for this example.

.. code-block::

    SEQUENCE(13)
      DELAYRANDOM(100,200) // random wait between 10 and 20 seconds
      FWD(50)
      AT(42) // sensor 42 is at the far end of platform B
      STOP
      DELAY(150)
      REV(20) // Reverse at DCC speed 20 (out of 127)
      AT(41) // far end of platform A
      STOP
      FOLLOW(13) // follows sequence 13 again… forever


Note a SEQUENCE is exactly the same as an ANIMATION except that it does NOT appear
in Engine Driver.

When the CommandStation is powered up or reset, EX-RAIL starts operating at
the beginning of the file.  For this sequence we need to set a loco address
and start the sequence:

.. code-block::

   SETLOCO(3)
   START(13) 
   DONE        // This marks the end of the startup process

The sequence can also be started from a serial monitor with the command </ START 3 13>


If you have multiple separate sections of track which do not require inter-train
cooperation you may add many more separate sequences and they will operate independently.

Although the above is trivial, the routes are designed to be
independent of the loco address so that we can have several locos
following the same route at the same time (not in the end to end example
above!) perhaps passing each other or crossing over with trains on other
routes.

The example above assumes that loco 3 is sitting on the track and pointing in
the right direction. A bit later I will show how to script an automatic
process to take whatever loco is placed on the programming track and
send it on it’s way to join in the fun.

Example 7: Running multiple inter-connected trains
==================================================
So what about routes that cross or shere single lines (passing places etc)
… lets add a passing place between A and B. S= sensors, T=Turnout
number. So now our route looks like this:


- @KEBBIN **TODO: Add image reference.**

Assuming we have already defined our turnouts with TURNOUT commands.
.. code-block::
 
 
 SEQUENCE(11)
   DELAYRANDOM(100,200) // random wait between 10 and 20 seconds
   THROW(1)
   CLOSE(2)
   FWD(30)
   AT(42) // sensor 42 is at the far end of platform B
   STOP
   DELAY(150)
   THROW(2)
   CLOSE(1)
   REV(20)
   AT(41)
   STOP
   FOLLOW(11) // follows sequence 11 again… forever

 
All well and good for one loco, but with 2 (or even 3) on this track we
need some rules. The principle behind this is

-  To enter a section of track that may be shared, you must RESERVE it.
   If you cant reserve it because another loco already has, then you
   will be stopped and the script will wait until such time as you can
   reserve it. When you leave a shared section you must free it.

-  Each “section” is merely a logical concept, there are no electronic
   section breaks in the track. You may have up to 255 sections (More can be supported by a code mod if required)


So we will need some extra sensors (hardware required) and some logical
blocks (all in the mind!):

- **TODO: Add image reference.**

We can use this map to plan routes, when we do so, it will be easier to
imagine 4 separate routes, each passing from one block to the next. Then
we can chain them together but also start from any block.

So… lets take a look at the routes now. For convenience I have used
route numbers that help remind us what the route is for.

@KEBBIN **the sensor numbers in the code below are all a mess. 
Because the sensor numbers are now direct pin references, we need
to avoid pin numbers that may clash with motor shield, I2C or similar
pins that have special meanings.**


.. code-block::

   SEQUENCE(12) // From block 1 to block 2
      DELAYRANDOM(100,200) // random wait between 10 and 20 seconds
      RESERVE(2) // we wish to enter block 2… so wait for it
      THROW(1) // Now we “own” the block, set the turnout
      FWD(30) // and proceed forward
      AFTER(71) // Once we have reached AND passed sensor 71
      FREE(1) // we no longer occupy block 1
      AT(72) // When we get to sensor 72
      FOLLOW(23) // follow route from block 2 to block 3

   SEQUENCE(23) // Travel from block 2 to block 3
      RESERVE(3) // will STOP if block 3 occupied
      CLOSE(2) // Now we have the block, we can set turnouts
      FWD(20) // we may or may not have stopped at the RESERVE
      AT(2) // sensor 2 is at the far end of platform B
      STOP
      FREE(2)
      DELAY(150)
      FOLLOW(34)

   ROUTE(34) // you get the idea
      RESERVE(4)
      THROW(2)
      REV(20)
      AFTER(13)
      FREE(3)
      AT(14)
      FOLLOW(41)

   ROUTE(41)
      RESERVE(1)
      CLOSE(1)
      REV(20)
      AT(1)
      STOP
      FREE(4)
      FOLLOW(12) // follows Route 12 again… forever
 
   

Does that look long? Worried about memory on your Arduino…. Well the
script above takes about 100 BYTES of program memory and no dynamic.

If you follow this carefully, it allows for up to 3 trains at a time
because one of them will always have somewhere to go. Notice that there
is common theme to this…

-  RESERVE where you want to go, if you are moving and the reserve
   fails, your loco will STOP and the reserve waits for the block to
   become available. (these waits and the manual WAITS do not block the
   Arduino process… DCC and the other locos continue to follow their
   routes)

-  Set the points to enter the reserved area.. do this ASAP as you may
   be still moving towards them. (@KEBBIN... maybe. TODO ..EX-RAIL knows if this is a panic and
   switches the points at full speed, if you are not moving then the
   switch is a more realistic sweep motion if you are using servos rather than slam-solenoid motors.)

-  Set any signals 

-  Move into the reserved area

-  Reset your signals

-  Free off your previous reserve as soon as you have fully left the
   block

Starting the system
===================

Starting the system is tricky because we need to place the trains in a
suitable position and set them off. We need to have a starting position
for each loco and reserve the block(s) it needs to keep other trains
from crashing into it.

For a known set of locos, the easy way is to define the startup process
at the beginning of ROUTES , e.g. for two engines, one at each station

.. code-block::

 // ensure all blocks are reserved as if the locos had arrived there
 RESERVE(1) // start with a loco in block 1
 RESERVE(3) // and another in block 3
 SENDLOCO(3,12) // send Loco DCC addr 3 on to route 12
 SENDLOCO(17,34) // send loco DCC addr 17 to route 34
 DONE // don’t drop through to the first route

CAUTION: this isn’t ready to handle locos randomly placed on the layout after a power down.

Some interesting points about the startup… You don’t need to set
turnouts because each route is setting them as required. Signals default
to RED on powerup and get turned green when a route decides.


Drive Away feature
==================

EX-RAIL can switch a track section between programming and mainline
automatically.

Here for example is a startup route that has no predefined locos but
allows locos to be added at station 1 while the system is in motion.
Let’s assume that the track section at Station1 is isolated and
connected to the programming track power supply. Also that we have a
“launch” button connected where sensor 17 would be and an optional
signal (ie 3 leds) on the control panel connected where signal 27 would
be .

.. code-block::

 
 ROUTE(99)
   SIGNAL(27,28,29)
   RED(27)   // indicate launch not ready
   AFTER(17) // user presses and releases launch button
   UNJOIN // separate the programming track from main
   DELAY(20)
   AMBER(27) // Show amber, user may place loco
   // user places loco on track and presses “launch” again
   AFTER(17)
   READ_LOCO // identify the loco
   GREEN(27) // show green light to user
   JOIN // connect prog track to main
   SCHEDULE(12) // send loco off along route 12
   FOLLOW(99) // keep doing this for another launch

The READ_LOCO reads the loco address from the PROG track and the current route takes on that
loco. By altering the script slightly and adding another sensor, it’s
possible to detect which way the loco sets off and switch the code logic
to send it in the correct direction by using the INVERT_DIRECTION instruction so that
this locos FWD and REV commands are reversed. (easily done with diesels!)

Sounds
======
You can use ``FON(n)`` and ``FOFF(n``) to switch loco functions… eg sound horn

Sensors
========

-  DCC++EX allows for sensors that are LOW-on or HIGH-on, this is
   particularly important for IR sensors that have been converted to
   detect by broken beam, rather than reflection. @KEBBIN This is TODO!!!

-  Magnetic/Hall sensors work for some layouts but beware of how you detect
   the back end of a train approching the buffers in a siding,
   or knowing when the last car has cleared a crossing.

-  Handling sensors in the automation is made easy because EX-RAIL throws
   away the concept of interrupts (“oh… sensor 5 has been detected…
   which loco was that and what the hell do I do now?”) and instead has
   the route scripts work on the basis of “do nothing, maintain speed
   until sensor 5 triggers and then carry on in the script”

- Sensor numbers are direct references to virtual pin numbers in the Hardware Adapter Layer. 
   For a Mega onboard GPIO pin, this is the same as the digital pin number. Other pin ranges refer to 
   pin expanders etc. 

- Sensors with id's 0 to 255 may be LATCHED/UNLATCHED in your script.
   If a sensor is latched on
   by the script, it can only be set off by the script… so AT(5) LATCH(5) for
   example effectively latches the sensor 5 on when detected once.

- Sensor polling by JMRI is independent of this and may continue if <S> commands are used.


Outputs
========

- Generic Outputs are mapped to VPINs on the HAL (as for sensors)
- SIGNAL definitions are just groups of 3 Outputs that can be more easily managed.

Sequence Numbers
================

- All ROUTE / AUTOMATION / SEQUENCE  ids are limited to 1- 32767 
- 0 is reserved for the startup sequence appearing as the first entry in  the EXRAIL script. 

Various techniques
===================

As the myAutomation.h file is effecticely being C++ compiled, 
it is possible to use some preprocessor tricks to aid your scripts.

- Defining names for some or all of the numbers 
   For example:
   .. code-block::

      #define COAL_YARD_EXIT 32 
      EXRAIL
         ROUTE(COAL_YARD_EXIT) 
            THROW(19)
            GREEN(27)

- Including sub-files
For example:
.. code-block::

   EXRAIL
      ROUTE(COAL_YARD_EXIT) 
         THROW(19)
         GREEN(27)
         DONE
   #include "myFireEngineLights.h"
   #include "myShuttle.h"



