***********************
EX-RAIL Automation
***********************

|

Introduction
***********************

EX-RAIL is an **EX**\panded **R**\ailroad **A**\utomation **I**\nstruction **L**\anguage
that can be easily used to describe sequential action to automatically take place on your model layout.

|

What you can do with it:
========================

- Create "Routes" which set multiple turnouts and signals at the press of a button in Engine Driver
- Intercept turnout changes to automatically adjust signals
- Animate accessories such as lights, crossings or cranes
- Automatically drive multiple trains simultaneously and manage complex interactions such as single line working and crossovers
- Drive trains manually and hand a train over to an automation

What you don't need:
====================

- JMRI or any additional utilities other than the Arduino IDE.
- Knowlege of C++ or Python/Jython programming

.. sidebar:: A note from the Author

   My original aim was to see if I could create an automated layout with lots going
   on that didn’t just run around in circles. Having looked at JMRI
   (briefly I must say) and DCC++ I began to wonder whether I could
   actually make a simpler automation system and run it entirely on the
   Arduino used for DCC++.

   Some of the automation techniques I read about using python scripts in
   JRMI made my blood run cold… there’s a lot I could say here but won’t
   without a pint or two.

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
   DCC++-EX, which grew out of the early DCC++ system, provides a clean and efficient API for
   the EX-RAIL automation to call.

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
small and requires very little PROGMEM or RAM to execute. It is only
included in the compilation of the CommandStation code if the compiler
detects a “myEX-RAIL.h” file. During execution, an EX-RAIL automation is much
(perhaps 2 orders of magnitude) more time efficient than the code
required to process incoming requests from an external automation
processor.


@KEBBIN ... the bit about command differences isnt really relevant if EX-RAIL 
is just animating a few flashing lights... so I've taken it out of this part.

@KEBBIN I think this sensor stuff needs to go much further down, don't want to confuse people too early.

|

The Automation Process
******************************************

All routes, automations etc step through a list of simple keywords until they reach an ENDTASK
keyword. The reference list is here @KEBBIN?

@KEBBIN  -- mabe we should call ENDTASK  "DONE" 

|

Routes for Engine Driver
==========================
A typical route might be to set a sequence of turnouts in response to a single button in Engine Driver.
The EX-RAIL instructions to do this might look like

.. code-block::

   ROUTE(1)
     THROW(1)
     CLOSE(7)
     ENDTASK

or you can write it like this

.. code-block::

   ROUTE(1)  THROW(1)  CLOSE(7)  ENDTASK

or add comments

.. code-block::

 // This is my coal yard to engine shed route
   ROUTE(1)     // appears as "Route 1" in Engine Driver
     THROW(1)   // Throw turnout onto coal yard siding
     CLOSE(7)   // close turnout for engine shed
     ENDTASK    // thats all folks!

of course, you may want to add signals, and time delays

.. code-block::

   ROUTE(1)
     RED(77)
     THROW(1)
     CLOSE(7)
     DELAY(50)  // this is a 5 second wait
     GREEN(9)
     ENDTASK
|
Automating Signals with turnouts
==================================
By intercepting a turnout change its easy to automatically adjust signals or 
automatically switch a facing turnout.
Use an ONTHROW or ONCLOSE keyword to detect a particular turnout change:
.. code-block::
   ONTHROW(8)  // When turnout 8 is thrown
     THROW(9)  // must also throw the facing turnout
     RED(14)
     DELAY(20)
     GREEN(13)
     ENDTASK

   ONCLOSE(8)  // When turnout 8 is closed
     CLOSE(9)
     RED(13)
     DELAY(20)
     GREEN(14)
     ENDTASK

Automating various non-track items 
====================================
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
during the startup process (see later) using SCHEDULE(66)
@KEBBIN... maybe this would be better named START.

Automating a train
=====================
     
Start with something as simple as a single loop of track with a station and a 
sensor (connected to pin 40 for this example) at the 
point where you want the train to stop.
Using an AUTOMATION keyword means that this automation will appear in Engine Driver so
you can drive the train manually, and then had it over to the automation at the press of a button.

[technically an automation can independently run multiple locos along the same path 
through the layout but this is discussed later]

.. code-block::
   AUTOMATION(4)
      FWD(40)   // move forward at DCC speed 40 (out of 127)
      AT(40)     // when you get to sensor on pin (40)
      STOP      // Stop the train 
      DELAYRANDOM(50,200) // delay somewhere between 5 and 20 seconds
      FWD(30)   // start a bit slower
      AFTER(40)  // until sensor on pin 40 has been passed
      FOLLOW(4) // and continue to follow the automation

Notice that this automation does not specify the loco address. If you drive a loco with Engine Driver 
and then hand it over to this automation, then the automation will run with the loco you last drove.


Perhaps you also have a single line shuttling between stations A and B.

These steps may be something like:

-  Wait between 10 and 20 seconds for the guard to stop chatting up the
   girl in the ticket office.
-  Move forward at speed 30
-  When I get to sensor B stop.

Similarly, the route from B to A could be something like this
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
      REV(20)
      AT(41) // far end of platform A
      STOP
      FOLLOW(13) // follows animation 1 again… forever


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

Notice that the route instructions are followed in sequence by the loco given to it,
the AT command just leaves the loco running until that sensor is
detected. 

If you have multiple separate sections of track which do not require inter-train
cooperation you may add many more separate sequences and they will operate independently.

Although the above is trivial, the routes are designed to be
independent of the loco address so that we can have several locos
following the same route at the same time (not in the end to end example
above!) perhaps passing each other or crossing over with trains on other
routes.

The example above assumes that loco 3 is sitting at A and pointing in
the right direction. A bit later I will show how to script an automatic
process to take whatever loco is placed on the programming track and
send it on it’s way to join in the fun.

Running multiple inter-connected trains
========================================
So what about routes that cross or shere single lines (passing places etc)
… lets add a passing place between A and B. S= sensors, T=Turnout
number. So now our route looks like this:


- **TODO: Add image reference.**

Assuming we have already defined our turnouts with <T> or TURNOUT commands.
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

 
All well and good for 1 loco, but with 2 (or even 3) on this track we
need some rules. The principle behind this is

-  To enter a section of track that may be shared, you must RESERVE it.
   If you cant reserve it because another loco already has, then you
   will be stopped and the script will wait until such time as you can
   reserve it. When you leave a shared section you must free it.

-  Each “section” is merely a logical concept, there are no electronic
   section breaks in the track.

So we will need some extra sensors (hardware required) and some logical
blocks (all in the mind!):

- **TODO: Add image reference.**

We can use this map to plan routes, when we do so, it will be easier to
imagine 4 separate routes, each passing from one block to the next. Then
we can chain them together but also start from any block.

So… lets take a look at the routes now. For convenience I have used
route numbers that help remind us what the route is for… any number up
to 255 is Ok. Anyone want more than that and I will fix it.

.. code-block::

 ROUTE(12) // From block 1 to block 2
   DELAYRANDOM(100,200) // random wait between 10 and 20 seconds
   RESERVE(2) // we wish to enter block 2… so wait for it
   THROW(1) // Now we “own” the block, set the turnout
   FWD(30) // and proceed forward
   AFTER(11) // Once we have reached AND passed sensor 11
   FREE(1) // we no longer occupy block 1
   AT(12) // When we get to sensor 12
   FOLLOW(23) // follow route from block 2 to block 3

ROUTE(23) // Travel from block 2 to block 3
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
 
   
@KEBBIN got to here

Does that look long? Worried about memory on your Arduino…. Well the
script above takes just 82 BYTES of program memory and no dynamic.

If you follow this carefully, it allows for up to 3 trains at a time
because one of them will always have somewhere to go. Notice that there
is common theme to this…

-  RESERVE where you want to go, if you are moving and the reserve
   fails, your loco will STOP and the reserve waits for the block to
   become available. (these waits and the manual WAITS do not block the
   Arduino process… DCC and the other locos continue to follow their
   routes)

-  Set the points to enter the reserved area.. do this ASAP as you may
   be still moving towards them. (@KEBBIN... maybe...EX-RAIL knows if this is a panic and
   switches the points at full speed, if you are not moving then the
   switch is a more realistic sweep motion(feature not yet))

-  Set any signals (see later)

-  Move into the reserved area

-  Reset your signal (see later)

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
 ENDPROG // don’t drop through to the first route

CAUTION: this isn’t ready to handle locos randomly placed on the layout after a power down.

Some interesting points about the startup… You don’t need to set
turnouts because each route is setting them as required. Signals default
to RED on powerup and get turned green when a route decides.


.. code-block::

 ROUTE(66)
 RED(7)
 DELAY(15)
 GREEN(7)
 DELAY(15)
 FOLLOW(66)

Fancy Startup
==============

EX-RAIL can switch a track section between programming and mainline
automatically.

Here for example is a startup route that has no predefined locos but
allows locos to be added at station 1 while the system is in motion.
Let’s assume that the track section at Station1 is isolated and
connected to the programming track power supply. Also that we have a
“launch” button connected where sensor 17 would be and an optional
signal (ie 2 leds) on the control panel connected where signal 18 would
be (see Signals below).

.. code-block::

 
 ROUTE(99)
 AFTER(17) // user presses and releases launch button
 RESERVE(1) // Wait until block free and keep others out
 UNJOIN // separate the programming track from main
 DELAY(20)
 GREEN(18) // Show a green light to user
 // user places loco on track and presses “launch” again
 AFTER(17)
 READ_LOCO // identify the loco
 RED(17) // show red light to user
 JOIN // connect prog track to main
 SCHEDULE(12) // send loco off along route 12
 FOLLOW(99) // keep doing this for another launch

The READ_LOCO reads the loco address and the current route takes on that
loco. By altering the script slightly and adding another sensor, it’s
possible to detect which way the loco sets off and switch the code logic
to send it in the correct direction. (easily done with diesels!)

Signals
========

Signals are now simply a decoration to be switched by the route process…
they don’t control anything.

``GREEN(55)`` would turn signal 55 green and ``RED(55)`` would turn it red.
Somewhere in the script there must be a SIGNAL command like this:
SIGNAL(55,56,57)  This defines a singal with ID 55 where the red/stop lamp is connected to 
pin 55, the amber/caution lamp to pin 56 and the green.proceed lamp to pin 57.
The pins do not need to be contiguous and the red pin is also used as the signal id. Thus  
you can change the signal by RED(55), AMBER(55) and GREEN(55)

Sounds
======
You can use ``FON(n)`` and ``FOFF(n``) to switch loco functions… eg sound horn

Sensors
========

-  DCC++EX allows for sensors that are LOW-on or HIGH-on, this is
   particularly important for IR sensors that have been converted to
   detect by broken beam, rather than reflection.

-  Magnetic/Hall sensors work for some layouts but beware of how you detect
   the back end of a train approching the buffers in a siding,
   or knowing when the last car has cleared a crossing.

-  Handling sensors in the automation is made easy because EX-RAIL throws
   away the concept of interrupts (“oh… sensor 5 has been detected…
   which loco was that and what the hell do I do now?”) and instead has
   the route scripts work on the basis of “do nothing, maintain speed
   until sensor 5 triggers and then carry on in the script”

-  EX-RAIL supports the PROG track drive-away feature of CommandStation-EX. This allows a
   script to automatically detect the address of a loco on the programming
   track, then drive it onto the main track to join in the fun.

Numbers
========

All route/automation/sequence, sensor, output, turnout or signal ids are limited to 0- 255 (

The same id may be used for a route, turnout, but sensor, output or signal ids share the same 
number range as the reference hardware pins. 
without confusing the software (the same may not be true of the user!).

Its OK to use sensor ids that have no physical item in the layout. These
can only be LATCHed, tested or UNLATCHED in the scripts. If a sensor is set on
by the script, it can only be set off by the script… so AT(5) LATCH(5) for
example effectively latches the sensor 5 on when detected once.

You can give names to routes turnouts signals and sensors etc using
``#define`` or ``const byte`` statements.

Future plans
=============

-  Some of the constructs above are not yet in the code, or need
   cleaning up a bit. Its early days but world situation suggests I will
   have plenty of time on my hands.

-  I want to add some more commands for controlling animations, such as
   SERVO, STEPPER and LED

