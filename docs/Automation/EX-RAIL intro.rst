***********************
EX-RAIL – Introduction
***********************

@KEBBIN  I have added some notes/questions marked as @KEBBIN 

What you can do with it:
- Create "Routes" which set multiple turnouts and signals at the press of a button in Engine Driver
- Intercept turnout changes to automatically adjust signals
- Animate accessories such as lights, crossings or cranes
- Automatically drive multiple trains simultaneously and manage complex interactions such as single line working and crossovers
- Drive trains manually and hand a train over to an automation

What you don't need:
- JMRI or any additional utilities other than the Arduino IDE.
- Knowlege of C++ or Python/Jython programming


A note from the author:
@KEBBIN  can we put this in a kind of box so its clear its just a note and where it ends?

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
Sensors
========

-  DCC++EX allows for sensors that are LOW-on or HIGH-on, this is
   particularly important for IR sensors that have been converted to
   detect by broken beam, rather than reflection.

-  Magnetic/Hall sensors work for some layouts but beware of how you detect the
back end of a train approching the buffers in a siding, or knowing when the last car has
cleared a crossing.

-  Handling sensors in the automation is made easy because EX-RAIL throws
   away the concept of interrupts (“oh… sensor 5 has been detected…
   which loco was that and what the hell do I do now?”) and instead has
   the route scripts work on the basis of “do nothing, maintain speed
   until sensor 5 triggers and then carry on in the script”

-  EX-RAIL supports the PROG track drive-away feature of CommandStation-EX. This allows a
   script to automatically detect the address of a loco on the programming
   track, then drive it onto the main track to join in the fun.

Introduction to the Automation process
======================================

All routes, automations etc step through a list of simple keywords until they reach an ENDTASK
keyword. The reference list is here @KEBBIN?

@KEBBIN  -- mabe we should call ENDTASK  "DONE" 

Routes for Engine Driver
************************
A typical route might be to set a sequence of turnouts in response to a single button in Engine Driver.
The EX-RAIL instructions to do this might look like 
.. code-block::
   ROUTE(1)
     THROW(1)
     CLOSE(7)
     ENDTASK

or you can write it like this
.. code-block::
   ROUTE(1)  THROW(1)  CLOSE(7) ENDTASK

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

Automating Signals with turnouts
********************************
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
**********************************
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
******************
     
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
***************************************
So what about routes that cross or shere single lines (passing places etc)
… lets add a passing place between A and B. S= sensors, T=Turnout
number. So now our route looks like this:


- **TODO: Add image reference.**

Assuming we have already defined our turnouts with <T> or TURNOUT commands.
.. code-block::
 
 SETLOCO(3)
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

 @KEBBIN got to here
 
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

 BEGINROUTES
 … see later for startup

 ROUTE(12) // From block 1 to block 2
 DELAYRANDOM(100,200) // random wait between 10 and 20 seconds
 RESERVE(2) // we wish to enter block 2… so wait for it
 TR(1) // Now we “own” the block, set the turnout
 FWD(30) // and proceed forward
 AFTER(11) // Once we have reached AND passed sensor 11
 FREE(1) // we no longer occupy block 1
 AT(12) // When we get to sensor 12
 FOLLOW(23) // follow route from block 2 to block 3

 ROUTE(23) // Travel from block 2 to block 3
 RESERVE(3) // will STOP if block 3 occupied
 TL(2) // Now we have the block, we can set turnouts
 FWD(20) // we may or may not have stopped at the RESERVE
 AT(2) // sensor 2 is at the far end of platform B
 STOP
 FREE(2)
 DELAY(150)
 FOLLOW(34)

 ROUTE(34) // you get the idea
 RESERVE(4)
 TR(2)
 REV(20)
 AFTER(13)
 FREE(3)
 AT(14)
 FOLLOW(41)

 ROUTE(41)
 RESERVE(1)
 TL(1)
 REV(20)
 AT(1)
 STOP
 FREE(4)
 FOLLOW(12) // follows Route 1 again… forever
 ENDROUTES

Does that look long? Worried about memory on your Arduino…. Well the
script above takes just 70 BYTES of program memory and no dynamic.

If you follow this carefully, it allows for up to 3 trains at a time
because one of them will always have somewhere to go. Notice that there
is common theme to this…

-  RESERVE where you want to go, if you are moving and the reserve
   fails, your loco will STOP and the reserve waits for the block to
   become available. (these waits and the manual WAITS do not block the
   Arduino process… DCC and the other locos continue to follow their
   routes)

-  Set the points to enter the reserved area.. do this ASAP as you may
   be still moving towards them. (EX-RAIL knows if this is a panic and
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

Startup can also SCHEDULE a “route” that is merely a decorative
automation such as flashing lights or moving doors but has no loco
attached to it. For example, using a signal connection to flash a red
light on the pin for signal 7, green will turn it off!

.. code-block::

 ROUTE(66)
 RED(7)
 DELAY(15)
 GREEN(7)
 DELAY(15)
 FOLLOW(66)
 ENDROUTES

Fancy Startup
==============

EX-RAIL can switch a track section between programming and mainline
automatically.

Here for example is a startup route that has no predefined locos but
allows locos to be added at station 1 while the system is in motion.
Let’s assume that the track section at Station1 is isolated and
connected to the programming track power supply. Also that we have a
“launch” button connected where sensor 17 would be and an optional
signal (ie 2 leds) on the control panel connected where signal 17 would
be (see Signals below).

.. code-block::

 BEGINROUTES
 PROG_TRACK(0) // start as program track connected to mainline

 ROUTE(99)
 AFTER(17) // user presses and releases launch button
 RESERVE(1) // Wait until block free and keep others out
 PROG_TRACK(1) // power on the programming track
 GREEN(17) // Show a green light to user
 // user places loco on track and presses “launch” again
 AFTER(17)
 READ_LOCO // identify the loco
 RED(17) // show red light to user
 PROG_TRACK(0) // connect prog track to main
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

``GREEN(5)`` would turn signal 5 green and ``RED(5)`` would turn it red.

Sounds

You can use ``FON(n)`` and ``FOFF(n``) to switch loco functions… eg sound horn

Numbers
========

All route, sensor, output, turnout or signal ids are limited to 0- 255 (
A UNO does not have enough RAM so the compiler limits this to 0-63 on a
UNO device)

The same id may be used for a route, turnout, sensor, output or signal
without confusing the software (the same may not be true of the user!).

Its OK to use sensor ids that have no physical item in the layout. These
can only be set, tested or reset in the scripts. If a sensor is set on
by the script, it can only be set off by the script… so AT(5) SET(5) for
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

COMMAND REFERENCE
==================

There are some diagnostic and control commands added to the <tag>
language normally used to control the command station over USB, WiFi or
Ethernet:

+-----------------------------------+-----------------------------------+
| <D EX-RAIL ON|OFF>                | Turns on/off diagnostic traces    |
|                                   | for EX-RAIL events                |
+===================================+===================================+
| <S …>                             | These JMRI related commands are   |
|                                   | rejected as they are incompatible |
| <Q …>                             | with EX-RAIL                      |
|                                   |                                   |
| <Z …>                             |                                   |
|                                   |                                   |
| <E>                               |                                   |
|                                   |                                   |
| <e>                               |                                   |
+-----------------------------------+-----------------------------------+
| <t …>                             | Throttle commands are only        |
|                                   | accepted for locos that are not   |
|                                   | currently controlled by EX-RAIL   |
|                                   | (This not yet implemented)        |
+-----------------------------------+-----------------------------------+
| <T id address subaddress>         | Incompatible with predefined      |
| <T id>                            | layout and so rejected.           |
|                                   | <T> and <T id 0|1> are accepted.  |
+-----------------------------------+-----------------------------------+
| </ PAUSE>                         | Pauses automation, all locos      |
|                                   | ESTOP.                            |
+-----------------------------------+-----------------------------------+
| </ RESUME>                        | Resumes automation, Locos are     |
|                                   | restarted at speed when paused.   |
+-----------------------------------+-----------------------------------+
| </ STATUS>                        | Displays EX-RAIL running thread   |
|                                   | information                       |
+-----------------------------------+-----------------------------------+
| </ SCHEDULE [loco] route>         | Starts a new thread to send loco  |
|                                   | onto route.                       |
|                                   | or Start a non-loco animation     |
|                                   | route)                            |
+-----------------------------------+-----------------------------------+
| </ RESERVE id>                    | Manually reserves a virtual track |
|                                   | block.                            |
+-----------------------------------+-----------------------------------+
| </ FREE id>                       | Manually frees a virtual track    |
|                                   | block                             |
+-----------------------------------+-----------------------------------+
| </ TL Id>                         | Set turnout LEFT                  |
+-----------------------------------+-----------------------------------+
| </ TR id >                        | Set turnout RIGHT                 |
+-----------------------------------+-----------------------------------+
| </ SET id>                        | Lock sensor                       |
+-----------------------------------+-----------------------------------+
| </ RESET id>                      | Unlock sensor                     |
+-----------------------------------+-----------------------------------+


LAYOUT REFERENCE
=================

+-------------------------------+--------------------------------------+
| LAYOUT                        | Identifies start of LAYOUT section.  |
|                               | Only one layout section is           |
|                               | permitted.                           |
+===============================+======================================+
| --- Turnouts ---              | Each turnout must have a unique id   |
|                               | (0-255) which is used in TL and TR   |
|                               | commands.                            |
+-------------------------------+--------------------------------------+
| SER                           | Pin= pin number on I2C xxxx board.   |
| VO_TURNOUT(id,pin,left,right) | (0-64, over 4 chained boards)        |
|                               |                                      |
|                               | Left=servo PWM value for turnout     |
|                               | LEFT                                 |
|                               |                                      |
|                               | Right=servo PWM value for turnout    |
|                               | RIGHT                                |
+-------------------------------+--------------------------------------+
| DCC_TURNOU                    | Addr=DCC accessory address           |
| T(id,addr,subaddr,leftActive) |                                      |
|                               | Subaddr= DCC accessory subaddress    |
|                               |                                      |
|                               | leftIsActive (true/false) set true   |
|                               | if TL command should “activate”      |
|                               | turnout.                             |
+-------------------------------+--------------------------------------+
| PIN_TURNOUT(id,pin,leftValue) | Pin= Arduino CPU pin to drive        |
|                               | turnout                              |
|                               | leftvalue= (HIGH/LOW) TL sets pin to |
|                               | this.                                |
+-------------------------------+--------------------------------------+
| I2C                           | Pin= pin n umber on I2C xxx board    |
| PIN_TURNOUT(id,pin,leftValue) | (0-64, over 4 chained boards)        |
|                               | leftvalue= (HIGH/LOW) TL sets pin to |
|                               | this.                                |
+-------------------------------+--------------------------------------+
| --- Sensors ---               | Each sensor must have a unique id    |
|                               | (0-255) which is used in AT or AFTER |
|                               | commands.                            |
+-------------------------------+--------------------------------------+
| I2C_SENSOR(id,pin,activeWhen) | Pin= pin n umber on I2C xxx board    |
|                               | (0-64, over 4 chained boards)        |
|                               |                                      |
|                               | activeWhen= (HIGH/LOW) value         |
|                               | indicating sensor triggered.         |
+-------------------------------+--------------------------------------+
| PIN_SENSOR(id,pin,activeWhen) | Pin= Arduino CPU pin number          |
|                               |                                      |
|                               | activeWhen= (HIGH/LOW) value         |
|                               | indicating sensor triggered.         |
+-------------------------------+--------------------------------------+
| --- Outputs ---               | Each output must have a unique id    |
|                               | (0-255) which is used in AT or AFTER |
|                               | commands.                            |
+-------------------------------+--------------------------------------+
| I2                            | Pin= pin n umber on I2C xxx board    |
| CO_OUTPUT(id,pin,activeValue) | (0-64, over 4 chained boards)        |
|                               |                                      |
|                               | activeValue = (HIGH.LOW) value used  |
|                               | for SET command                      |
+-------------------------------+--------------------------------------+
| PINOUTPUT(id,pin,activeWhen)  | Pin=Arduino CPU pin n umber          |
|                               |                                      |
|                               | activeValue = (HIGH.LOW) value used  |
|                               | for SET command                      |
+-------------------------------+--------------------------------------+
|    --- Signals ---            | TO BE DEFINED                        |
+-------------------------------+--------------------------------------+
| ENDLAYOUT                     |                                      |
+-------------------------------+--------------------------------------+

Routes and animations
======================

The EX-RAIL system operates on a number of concurrent “threads”. Each thread
is following a route through the system and usually has an associated
loco that it is driving. Some threads may be driving animations and have
no loco attached. The thread keeps track of the position withing the
route and the loco speed. A thread may be delayed deliberately or when
waiting for a sensor or block section, this does not affect other
threads.

At system startup, a single thread is created to follow the first entry
in the routes table, with no loco. .

+-----------------------------------+-----------------------------------+
| ROUTES                            | Start of routes table.            |
+===================================+===================================+
| ROUTE(routeid)                    | Start if a route                  |
|                                   | routeid=0-255                     |
+-----------------------------------+-----------------------------------+
| AFTER(sensorid)                   | Waits until sensor reached, then  |
|                                   | waits until sensor no longer      |
|                                   | active for 0.5 seconds            |
+-----------------------------------+-----------------------------------+
| AT(sensorid)                      | Waits until sensor reached        |
+-----------------------------------+-----------------------------------+
| DELAY(duration)                   | Waits for duration/10 seconds     |
+-----------------------------------+-----------------------------------+
| DELAYMINS(duration)               | Waits for a number of minutes     |
+-----------------------------------+-----------------------------------+
| DEL                               | Waits a random time between       |
| AYRANDOM(minduration.maxduration) | minDuration/10 and maxDuration/10 |
|                                   | seconds.                          |
+-----------------------------------+-----------------------------------+
| ENDIF                             | Marks end of IF block (see IF     |
|                                   | command)                          |
+-----------------------------------+-----------------------------------+
| FOFF(func)                        | Switches loco function off        |
+-----------------------------------+-----------------------------------+
| FON(func)                         | Switches loco function on         |
+-----------------------------------+-----------------------------------+
| FOLLOW(routeid)                   | Continue at ROUTE(routeid)        |
|                                   | command                           |
+-----------------------------------+-----------------------------------+
| FREE(blockid)                     | Frees a previously reserved       |
|                                   | block. See RESERVE(blockid)       |
+-----------------------------------+-----------------------------------+
| FWD(speed)                        | Drive loco at given speed (0-127) |
|                                   | forwards (0=stop, 1=ESTOP)        |
+-----------------------------------+-----------------------------------+
| GREEN(signalId)                   | Sets signal to green              |
+-----------------------------------+-----------------------------------+
| IF(sensorId)                      | Checks if sensor is activated, if |
|                                   | NOT then processing skips to the  |
|                                   | matching ENDIF command (allowing  |
|                                   | for nested IF/IFNOTs )            |
+-----------------------------------+-----------------------------------+
| IFNOT(sensorId)                   | Checks if sensor is activated, if |
|                                   | it is active then processing      |
|                                   | skips to the matching ENDIF       |
|                                   | command (allowing for nested      |
|                                   | IF/IFNOT/IFRANDOMs )              |
+-----------------------------------+-----------------------------------+
| IFRANDOM(percent)                 | Randomly decides whether to       |
|                                   | continue or skip to the matching  |
|                                   | ENDIF                             |
+-----------------------------------+-----------------------------------+
| INVERT_DIRECTION                  | Causes current loco FWD and REV   |
|                                   | commands to be reversed (e.g.     |
|                                   | used if loco is pointing in wrong |
|                                   | direction)                        |
+-----------------------------------+-----------------------------------+
| PAUSE                             | Sets EX-RAIL into paused mode, all|
|                                   | animations and locos are stopped  |
|                                   | and manual control is possible    |
+-----------------------------------+-----------------------------------+
| PROGTRACK_JOIN                    | See DCCEX cmd <1 JOIN>            |
+-----------------------------------+-----------------------------------+
| PROGTRACK_OFF                     | See DCC cmd <0 PROG> (Disconnects |
|                                   | a JOIN)                           |
+-----------------------------------+-----------------------------------+
| READ_LOCO                         | Reads loco id from prog track and |
|                                   | assigns it to current route       |
+-----------------------------------+-----------------------------------+
| RED(signalId)                     | Sets Signal to RED                |
+-----------------------------------+-----------------------------------+
| RESERVE(blockId)                  | Blockid=(0-255)                   |
|                                   | If block is already reserved by   |
|                                   | another train, this loco will     |
|                                   | STOP and wait for the block to    |
|                                   | become free.                      |
|                                   | block is marked as reserved and   |
|                                   | this train continues..            |
|                                   | When you leave a block that you   |
|                                   | have reserved, you must FREE it.  |
+-----------------------------------+-----------------------------------+
| RESET(sensorId)                   | Clears a sensor flag (see SET)    |
+-----------------------------------+-----------------------------------+
| RESUME                            | Resumes EX-RAIL from PAUSE mode.  |
|                                   | Locos stopped by PAUSE are        |
|                                   | restarted.                        |
+-----------------------------------+-----------------------------------+
| REV(speed)                        | Move loco in reverse (see FWD)    |
+-----------------------------------+-----------------------------------+
| SCHEDULE(routeid)                 | Starts a new thread at            |
|                                   | ROUTE(routeid) and transfers      |
|                                   | current loco to it.               |
+-----------------------------------+-----------------------------------+
| SETLOCO(locoid)                   | Sets the loco id of the current   |
|                                   | thread.                           |
+-----------------------------------+-----------------------------------+
| SET(sensorId)                     | Locks on the software part of a   |
|                                   | sensor.                           |
|                                   | If a sensor is tested by          |
|                                   | AT/AFTER/IF etc and the software  |
|                                   | part is locked on, then the       |
|                                   | sensor is seen as active without  |
|                                   | a hardware check.                 |
|                                   | NOTE: This can be used for        |
|                                   | debounce. It can also be used for |
|                                   | virtual sensors that ONLY exist   |
|                                   | in software and have no hardware  |
|                                   | equivalent. Can be used for       |
|                                   | example to pass information from  |
|                                   | a travelling train thread to a    |
|                                   | lineside animation thread.        |
+-----------------------------------+-----------------------------------+
| SPEED(speed)                      | Changes loco speed in current     |
|                                   | direction.                        |
+-----------------------------------+-----------------------------------+
| STOP                              | =SPEED(0)                         |
+-----------------------------------+-----------------------------------+
| ESTOP                             | =SPEED(1) DCC emergency stop      |
+-----------------------------------+-----------------------------------+
| TL(turnoutId)                     | Sets turnout LEFT                 |
+-----------------------------------+-----------------------------------+
| TR(turnoutId)                     | Sets turnout RIGHT                |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+
| ENDROUTE                          | Terminates a route thread         |
+-----------------------------------+-----------------------------------+
| ENDROUTES                         | End of ROUTES table, must be last |
|                                   | entry.                            |
+-----------------------------------+-----------------------------------+
