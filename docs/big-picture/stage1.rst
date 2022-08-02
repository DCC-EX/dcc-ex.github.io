.. include:: /include/include.rst
.. include:: /include/include-l1.rst
*******
Stage 1
*******

.. sidebar:: On this page

   .. contents:: 
      :depth: 1
      :local:

|conductor|

Stage 1 of our RMFT layout is a simple loop including a single siding for a station, which allows for automated running of up to three trains including automated switching for entering and exiting the station siding.

To accomplish this, the layout will be broken up into four virtual blocks with five sensors in use to detect the position of our trains as they enter and exit the blocks, and three signals that will be controlled by automation to indicate when it is safe to proceed.

Below, we'll cover off the various aspects required to get up and running with stage 1 including object definitions, the various hardware options you can use, and how you can apply automation techniques to the layout.

What to expect to learn from stage 1
====================================

At the end of stage 1, we expect you will learn the following:

* How to define the different types of turnout and signal objects.
* How to reference sensors.
* How, why, and when to effectively use aliases.
* How an object ID is different to the pin or configuration used by the physical object it represents.
* How to enable layout automation while still manually controlling the trains.
* How to enable a fully automated layout.
* What hardware can be used, and how to connect the components (Fritzing diagrams for this will be published soon).

.. raw:: html
  :file: ../../_static/images/big-picture/rmft-stage1.drawio.svg

Aliases
=======

As mentioned already, we will be defining aliases throughout these pages to put human-friendly labels on our various objects.

By doing so, it becomes easier to refer to things in various different sequences or contexts when referring to a name than it is to remember a specific pin or turnout ID.

This also means if there is a need to change a pin or object ID, you can simply update the single alias reference, meaning you don't need to dig through all your sequences, routes, and so forth to edit them individually.

Further more, you can make radical changes such as moving from pin turnouts to servo turnouts, and only need to edit the defined objects and alias. Again, all your existing sequences, routes, etc. should remain unchanged.

For more information on aliases, refer to :ref:`ex-rail/ex-rail-reference:aliases`.

Turnouts
========

Two turnouts are used in this first stage of our RMFT layout to allow trains to enter and exit the station siding, or continue along the main track.

For further reading on turnouts, you can refer to the :ref:`ex-rail/ex-rail-reference:turnouts` section of the EX-RAIL reference and :ref:`reference/software/command-reference:defining (setting up) a turnout` in the DCC++ EX Command reference.

Turnout definitions
___________________

We will define turnout 1 with an ID of 100, and turnout 2 with an ID of 101.

DCC accessory turnouts
^^^^^^^^^^^^^^^^^^^^^^

To define these as DCC accessory turnouts, turnout 1 will be at linear address 101, and turnout 2 at 102. These translate to address 26 with sub address 0 for linear address 101, and address 26 with sub address 1 for linear address 102.

Therefore, the DCC++ EX command to define these in the serial console is as follows:

.. code-block:: 

  <T 100 DCC 26 0>
  <T 101 DCC 26 1>

In EX-RAIL, we would add these lines to myAutomation.h, with aliases defined:

.. code-block:: 

  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  
  TURNOUT(TRN1, 26, 0, "Station entry")
  TURNOUT(TRN2, 26, 1, "Station exit")

Pin turnouts
^^^^^^^^^^^^

To define these same turnout IDs as pin turnouts instead, and using I/O pins that are directly on our CommandStation-EX Mega2560, we will use pins 22 and 23.

To define these in the serial console:

.. code-block:: 

  <T 100 VPIN 22>
  <T 101 VPIN 23>

In EX-RAIL, we would add these lines to myAutomation.h:

.. code-block:: 

  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)

  PIN_TURNOUT(TRN1, 22, "Station entry")
  PIN_TURNOUT(TRN2, 23, "Station exit")

If we were instead to use an MCP23017 I/O expander, we would use Vpins instead of direct pins on the Mega2560, and we would start these at the first I/O expander's 164 Vpin ID.

To define these in the serial console:

.. code-block:: 

  <T 100 VPIN 164>
  <T 101 VPIN 165>

And again, in myAutomation.h for EX-RAIL:

.. code-block:: 

  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  
  PIN_TURNOUT(TRN1, 164, "Station entry")
  PIN_TURNOUT(TRN2, 165, "Station exit")

Servo turnouts
^^^^^^^^^^^^^^

Finally, to define these same turnouts as servo based turnouts, these would be connected to a PCA9685 servo module, and our first module starts at Vpin ID 100.

.. tip:: 

  Remember! Servo angles will be unique to your layout, and probably even unique to individual turnouts, so be sure you read the blurb on :ref:`big-picture/big-picture:tuning servo positions` and the :doc:`/reference/hardware/servo-module` page.

  Please don't blindly copy/paste the servo angles listed here and expect them to "just work".

Throughout these pages, we will assume that the thrown servo position is 400, the closed servo position is 100, and we will use the "Slow" profile.

.. note::

  You will note below that our turnout ID 100 matches the first PCA9685 module's first Vpin which happens to also be 100. While these numbers are the same, they do not represent the same item.

  You can see within this section on defining the turnouts that a turnout with an object ID of 100 could represent any variation of turnout object, with any support hardware implementation.

Defining these in the serial console therefore would be:

.. code-block:: 

  <T 100 SERVO 100 400 100 3>
  <T 101 SERVO 101 400 100 3>

Again, in myAutomation.h this becomes:

.. code-block:: 

  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  
  SERVO_TURNOUT(TRN1, 100, 400, 100, Slow, "Station entry")
  SERVO_TURNOUT(TRN2, 101, 400, 100, Slow, "Station exit")

Sensors
=======

Five sensors are used in this first stage, which allows us to have up to three trains controlled by EX-RAIL automation. The sensors are placed within each virtual block to ensure we know when the front of the train enters a block, and when the rear of the train has exited a block.

We don't need to explicitly define any sensor objects to work with EX-RAIL, so we will simply map these by defining EX-RAIL aliases.

To use pins directly on our Mega2560, we would start at pin 24 (we used pins 22/23 for turnouts):

.. code-block:: 

  ALIAS(SNS1_TRN1_APP, 24)       // Sensor 1, approaching turnout 1
  ALIAS(SNS2_MAIN_TRN1_EX, 25)   // Sensor 2, on the main track exiting turnout 1
  ALIAS(SNS3_STN, 26)            // Sensor 3, at our station stop
  ALIAS(SNS4_MAIN_TRN2_APP, 27)  // Sensor 4, on the main track approaching turnout 2
  ALIAS(SNS5_STN_TRN2_APP, 28)   // Sensor 5, on the station siding approaching turnout 2

Moving these to our first MCP23017 I/O expander, these would start at Vpin 166 (we used Vpins 164/165 for turnouts):

.. code-block:: 

  ALIAS(SNS1_TRN1_APP, 166)       // Sensor 1, approaching turnout 1
  ALIAS(SNS2_MAIN_TRN1_EX, 167)   // Sensor 2, on the main track exiting turnout 1
  ALIAS(SNS3_STN, 168)            // Sensor 3, at our station stop
  ALIAS(SNS4_MAIN_TRN2_APP, 169)  // Sensor 4, on the main track approaching turnout 2
  ALIAS(SNS5_STN_TRN2_APP, 170)   // Sensor 5, on the station siding approaching turnout 2

Signals
=======

Three signals have been used in this first stage to indicate whether or not a train can enter either the station siding or proceed beyond turnout 1 on the main track, to indicate whether a train can exit the station siding, or if a train can proceed beyond turnout 2 on the main track.

Pin based signals
_________________

To use pin based signals, we require three pins per signal, and therefore nine pins in total, but we will only define an alias for the red pin given that it is the "control" pin for each signal. The other pins are used in the background by DCC++ EX and are not referenced anywhere else outside the object definition.

To define pin based signals directly on the Mega2560 with aliases for the control pins:

.. code-block:: 

  ALIAS(SIG1_TRN1_APP, 30)       // Signal 1, approaching turnout 1
  ALIAS(SIG2_TRN2_GO, 33)        // Signal 2, proceed beyond turnout 2
  ALIAS(SIG3_STN_EX, 36)         // Signal 3, exit the station siding

  SIGNAL(SIG1_TRN1_APP, 31, 32)
  SIGNAL(SIG2_TRN2_GO, 34, 35)
  SIGNAL(SIG3_STN_EX, 37, 38)

Moving these again to an MCP23017 I/O expander, these would start at Vpin 172, however this also overlaps to a second I/O expander by one pin:

.. code-block:: 

  ALIAS(SIG1_TRN1_APP, 172)      // Signal 1, approaching turnout 1
  ALIAS(SIG2_TRN2_GO, 175)       // Signal 2, proceed beyond turnout 2
  ALIAS(SIG3_STN_EX, 178)        // Signal 3, exit the station siding

  SIGNAL(SIG1_TRN1_APP, 173, 174)
  SIGNAL(SIG2_TRN2_GO, 176, 177)
  SIGNAL(SIG3_STN_EX, 179, 180)

Servo based signals
___________________

To define servo based signals, these only require one Vpin per signal along with specifying the servo angle for the red, amber, and green positions.

.. tip:: 

  Remember! Servo angles will be unique to your layout, and probably even unique to individual signals, so be sure you read the blurb on :ref:`big-picture/big-picture:tuning servo positions` and the :doc:`/reference/hardware/servo-module` page.

  Please don't blindly copy/paste the servo angles listed here and expect them to "just work".

Allowing for servo based turnouts being used, we will start our signals from the third available Vpin on our PCA9685 servo module (we used the first two for servo turnouts). We will make the assumption that red requires a servo angle of 100, amber 250, and green 400:

.. code-block:: 

  ALIAS(SIG1_TRN1_APP, 102)       // Signal 1, approaching turnout 1
  ALIAS(SIG2_TRN2_GO, 103)        // Signal 2, proceed beyond turnout 2
  ALIAS(SIG3_STN_EX, 104)         // Signal 3, exit the station siding

  SERVO_SIGNAL(SIG1_TRN1_APP, 400, 250, 100)
  SERVO_SIGNAL(SIG2_TRN2_GO, 400, 250, 100)
  SERVO_SIGNAL(SIG3_STN_EX, 400, 250, 100)

Virtual blocks
==============

We've divided the layout into four virtual blocks, allowing for up to three trains to coexist safely on the layout. You will need at least one more block than you have trains in order to fully automate a layout, otherwise  there will be nowhere for a train to move to in order to start the automation sequences. This is outlined in further detail in the :ref:`big-picture/stage1:fully automated layout` section.

Block 1
_______

Block 1 is the approach to turnout 1, and can be used to prevent a train from entering either the station siding or the main track between turnouts 1 and 2 if they are occupied.

We will use ID 1 for this, with an alias:

.. code-block:: 

  ALIAS(BLK1_TRN1_APP, 1)

Block 2
_______

Block 2 consists of the section of the main track between turnouts 1 and 2, providing for a section to hold one train, allow a train on the station siding to exit safely, and also prevent a train running around the main track from entering this block.

We will use ID 2 for this, with an alias:

.. code-block:: 

  ALIAS(BLK2_MAIN_HOLD, 2)

Block 3
_______

Block 3 is for our station siding, ensuring no other trains can enter this block while it is occupied.

We will use ID 3 for this, with an alias:

.. code-block:: 

  ALIAS(BLK3_STN, 3)

Block 4
_______

Block 4 is the exit beyond turnout 2, and can hold a train while block 1 is occupied. Once block 1 is free, a train can run uninterrupted from block 4 back to block 1.

Note that block 4 on the diagram continues all the way to the beginning of block 1

We will use ID 4 for this, with an alias:

.. code-block:: 

  ALIAS(BLK4_TRN2_EX, 4)

Station
=======

In this particular stage, there's nothing specific for the station, however some advanced concepts might be to trigger an automated sound recording of arrivals and departures based on triggering sensor 3 or even sensor 2 if turnout 1 is in the thrown position.

This would likely make use of the EX-RAIL ``AT()`` or ``AFTER()`` commands.

Manual train control with automated routes
==========================================

If you still wish to be the driver of the trains but have some automation related to the turnouts and signals, then we can make use of EX-RAIL's ``ROUTE()`` directive. In this scenario, we don't need to implement our virtual blocks, as it will be up to you as the driver to ensure your trains don't collide. We also don't need to use the sensors, and will set our signals based on the choice of routes.

The two routes below will be advertised to WiThrottle applications and Engine Driver, so you can simply select them from the ROUTE menu.

Note that you can mix and match all the above I/O methods together, so you can use direct I/O pins on the Mega2560 while using MCP23017 I/O expanders, PCA9685 servo modules, and any other supported I/O options, which provides a myriad of possibilities to expand the I/O capabilities of your CommandStation.

For simplicity, we will outline the stage 1 options using consistent hardware types otherwise we'll wear out the scroll button on your mouse.

Once you understand the logic of our routes below and the various turnout, sensor, signal, and virtual block concepts above, you can view some :ref:`big-picture/stage1:complete myautomation.h examples` at the end of this page.

Startup sequence
________________

When the CommandStation and EX-RAIL starts, everything defined before the first ``DONE`` command executes automatically.

For safe running and a known starting state, we ensure both our turnouts are closed and set all our signals to red, followed by the first ``DONE`` to stop EX-RAIL executing any further automatically.

If we omit that first ``DONE``, EX-RAIL would automatically execute ``ROUTE(1, "Main Track")`` at every startup. Note, of course, that if you want that first route executed at every startup, then you can simply omit that same ``DONE``, which will have the same effect as manually selecting the "Main track" route.

.. code-block:: 

  // Start up with turnouts closed and signals red
  CLOSE(TRN1)
  CLOSE(TRN2)
  RED(SIG1_TRN1_APP)
  RED(SIG2_TRN2_GO)
  RED(SIG3_STN_EX)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

Route 1 - main track running
____________________________

The first route we publish for use is ``ROUTE(1, "Main track")`` which will appear in WiThrottle apps and Engine Driver with the description "Main track".

Given we have closed our turnouts and set all our signals red in the startup sequence above, when selecting this route the first time, it will simply set signals 1 and 2 green, as the ``IFTHROWN()`` statements will evaluate as false and not execute the associated commands.

On subsequent selections of this route, after selecting route 2 below, the turnouts will be thrown, resulting in these ``IFTHROWN()`` statements evaluating as true, and therefore executing the associated commands.

When this happens, signal 3 to exit the station siding is set to red ``RED(SIG3_STN_EX)`` as it is no longer safe to exit.

Next, in order to safely be able to close turnout 1, signal 1 is set to amber for 2 seconds to warn of the impending change ``AMBER(SIG1_TRN1_APP)``, and then red for a further 2 seconds ``RED(SIG1_TRN1_APP)`` to allow time for the turnout to close fully ``CLOSE(TRN1)``.

This same logic is applied for turnout 2, setting signal 2 to amber ``AMBER(SIG2_TRN2_GO)``, then red ``RED(SIG2_TRN2_GO)`` to allow turnout 2 to close fully ``CLOSE(TRN2)``.

Once both turnouts are closed, both signals 1 and 2 are set to green to indicate trains are safe to run through both turnouts with ``GREEN(SIG1_TRN1_APP)`` and ``GREEN(SIG2_TRN2_GO)``.

The route is completed with a ``DONE`` to tell EX-RAIL not to proceed any further.

.. code-block:: 

  ROUTE(1, "Main track")        // Select this route to just use the main track
    RED(SIG3_STN_EX)            // Set signal 3 red as it is not safe to exit the station siding
    IFTHROWN(TRN1)              // If turnout 1 is thrown, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we close turnout 1
      CLOSE(TRN1)               // Close turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to close
    ENDIF
    IFTHROWN(TRN2)              // If turnout 2 is thrown, do these:
      AMBER(SIG2_TRN2_GO)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG2_TRN2_GO)         // Set signal 2 red while we close turnout 2
      CLOSE(TRN2)               // Close turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to close
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG2_TRN2_GO)         // Set signal 2 green because we're safe to proceed
  DONE

Route 2 - enter and exit the station siding
___________________________________________

The second route we publish for use is ``ROUTE(2, "Stating siding")`` which will appear in WiThrottle apps and Engine Driver with the description "Station siding".

Counter to the main track route above, we use ``IFCLOSED()`` statements to evaluate if turnouts need to change or not from their current position. Therefore, if the first route we choose after startup is this one, both statements will evaluate true. The same will occur if we select our main track route.

When this happens, signal 2 to proceed beyond turnout 2 on the main track is set to red ``RED(SIG2_TRN2_GO)`` as it is no longer safe to exit that section of track.

Next, in order to safely be able to throw turnout 1, signal 1 is set to amber for 2 seconds to warn of the impending change ``AMBER(SIG1_TRN1_APP)``, and then red for a further 2 seconds ``RED(SIG1_TRN1_APP)`` to allow time for the turnout to throw fully ``THROW(TRN1)``.

This same logic is applied for turnout 2, setting signal 3 to amber ``AMBER(SIG3_STN_EX)``, then red ``RED(SIG3_STN_EX)`` to allow turnout 2 to be thrown ``THROW(TRN2)``.

Once both turnouts are thrown, both signals 1 and 3 are set to green to indicate trains are safe to enter and exit the station siding with ``GREEN(SIG1_TRN1_APP)`` and ``GREEN(SIG3_STN_EX)``.

The route is completed with a ``DONE`` to tell EX-RAIL not to proceed any further.

.. code-block:: 

  ROUTE(2, "Station siding")    // Select this route to use the station siding
    RED(SIG2_TRN2_GO)           // Set signal 2 red as it is not safe to proceed beyond turnout 2 on the main track
    IFCLOSED(TRN1)              // If turnout 1 is closed, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we throw turnout 1
      THROW(TRN1)               // Throw turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    IFCLOSED(TRN2)              // If turnout 2 is closed, do these:
      AMBER(SIG3_STN_EX)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG3_STN_EX)         // Set signal 2 red while we throw turnout 2
      THROW(TRN2)               // Throw turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG3_STN_EX)          // Set signal 2 green because we're safe to proceed
  DONE

Fully automated layout
======================

Now it's time to display the full automation capabilities by setting our layout up for fully automated control of your trains.

You will note that these are somewhat similar to :ref:`ex-rail/getting-started:example 7: running multiple inter-connected trains`, updated to suit the specifics of the RMFT layout.

To setup for these fully automated sequences, we need to ensure our trains are placed in the below positions, noting that EX-RAIL has no way of knowing where a train is on the layout when first starting.

* Train 1 in block 1, between sensor 1 and turnout 1.
* Train 2 in block 2, between sensors 2 and 4.
* Train 3 in block 4, after turnout 2.

Once you understand the logic below and the various turnout, sensor, signal, and virtual block concepts above, you can view some :ref:`big-picture/stage1:complete myautomation.h examples` at the end of this page.

Virtual block logic
___________________

As mentioned in the introduction, we can enable fully automated running of up to three trains on this layout by breaking it into four virtual blocks.

.. note:: 

  Remember, these are virtual blocks, and do not necessarily need to be electrically isolated from each other. Don't confuse isolated blocks of track or block occupancy detection with these virtual blocks. For further background, refer to :ref:`ex-rail/ex-rail-reference:blocks`.

When reading through the sections below on the logic, it helps to keep in mind the perspective of the engineer driving the train, rather than thinking of the complete layout. As the engineer, you need to ask yourself the question "what needs to be in place for me to safely drive this train to the desired destination?"

The automation is accomplished by defining six separate sequences that map out how trains can move safely from one block to the next, and we also use ``LATCH()`` as a technique to alternate between trains stopping at the station or continuing on the main track.

Full automation startup sequence
________________________________

As outlined above in the :ref:`big-picture/stage1:startup sequence` section, everything before the first ``DONE`` in myAutomation.h is executed on start up.

Given we are starting with three trains on the layout occupying virtual blocks 1, 2, and 4, we need to ensure our layout starts up in a manner that is safe for the automation to commence running these trains correctly.

Therefore, once again we ensure both our turnouts are closed and our signals are set to red so these objects are all in a known state to start with.

Next, we place a RESERVE() on each block a train occupies, which will prevent any sequence from driving another train into that block.

Once these activities have been done, we can tell our trains to start following the appropriate sequence, which will let them start on their fully automated journey safely.

.. code-block:: 

  // Start up with turnouts closed and signals red
  CLOSE(TRN1)
  CLOSE(TRN2)
  RED(SIG1_TRN1_APP)
  RED(SIG2_TRN2_GO)
  RED(SIG3_STN_EX)

  // Send three locos around our layout:
  RESERVE(BLK1_TRN1_APP)
  RESERVE(BLK2_MAIN_HOLD)
  RESERVE(BLK4_TRN2_EX)
  SENDLOCO(1, BLK1_EXIT)
  SENDLOCO(2, BLK2_BLK4)
  SENDLOCO(3, BLK4_BLK1)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

Exiting block 1 - station entry or main track?
______________________________________________

In order to safely exit block 1, the first decision to be made is if the train will go straight through to continue on the main track, or if it will switch on to the station siding.

Using the ``LATCH()`` command gives us a way to automatically alternate between the main track and the station siding. ``LATCH()`` simply sets the state of a pin (either real or virtual) which can then be tested by an ``IF()`` statement. In this particular case, we have defined pin 60 (alias "CHOOSE_BLK2") to be latched and unlatched, as this pin does not exist on the Mega2560, nor does it exist on any of our I/O expander boards. Further reading on ``LATCH()`` and ``UNLATCH()`` can be found in the :ref:`ex-rail/ex-rail-reference:sensors` section of the EX-RAIL reference.

When our CommandStation starts up, virtual pin 60 will not be set, and therefore evaluating the IF() statement ``IF(CHOOSE_BLK2)`` will return false, with our sequence then latching this virtual pin, meaning the next time this sequence is called, ``IF(CHOOSE_BLK2)`` will return true.

This logic allows us to follow our block 1 to block 3 sequence (if false) to switch onto the station siding, or follow our block 1 to block 2 sequence (if true) to continue on the main track.

On startup, we are sending train 1 on this sequence, which means with our ``IF(CHOOSE_BLK2)`` returning false on startup, train 1 will first attempt to move from block 1 to block 3, which means switching to our station siding. Control at this point is handed over to the :ref:`big-picture/stage1:moving from block 1 to block 3 - entering the station` sequence.

As a result of executing the ``LATCH(CHOOSE_BLK2)``, the next train navigating this block will instead have control handed over to the :ref:`big-picture/stage1:moving from block 1 to block 2 - continue on the main track` sequence.

.. code-block:: 

  // Sequence to exit block 1, and choose whether to go to the station or continue on main
  SEQUENCE(BLK1_EXIT)
    IF(CHOOSE_BLK2)
      UNLATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK2)
    ELSE
      LATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK3)
    ENDIF

Moving from block 1 to block 2 - continue on the main track
___________________________________________________________

To move from block 1 to block 2, the first thing we need to know is if it's safe to do so.

In EX-RAIL, this is accomplished by using the ``RESERVE()`` command which says if the block is free, we can reserve it. If it is not free, the reserve cannot be completed, and the train will stop until the block is freed, in which case the sequence can continue.

So, providing a reserve can be placed on block 2, we can then test to see if turnout 1 is thrown. If so, the turnout needs to be closed, but in order to do so safely we set the approach signal amber for 2 seconds ``AMBER(SIG1_TRN1_APP)``, then set the signal red ``RED(SIG1_TRN1_APP)`` before closing the turnout ``CLOSE(TRN2)``, and waiting a further 2 seconds to ensure the turnout is fully closed.

Once the turnout is closed, or if it already was, we set our signal green ``GREEN(SIG1_TRN1_APP)`` and tell the train to proceed at speed 20 ``FWD(20)``. The speed is relatively slow given the train is likely to need to stop again before being able to move beyond turnout 2.

Then, after the train has not only activated sensor 2, but has passed over it completely and allowed it to deactivate for 0.5 seconds ``AFTER(SNS2_MAIN_TRN1_EX)``, the reservation on block 1 can be released ``FREE(BLK1_TRN1_APP)``, meaning the next train needing to enter block 1 can do so.

At this point, control of the train is handed over to the :ref:`big-picture/stage1:moving from block 2 to block 4 - continue on the main track` sequence.

.. code-block:: 

  // Sequence to go from block 1 to block 2
  SEQUENCE(BLK1_BLK2)
    RESERVE(BLK2_MAIN_HOLD)
    IFTHROWN(TRN1)
      AMBER(SIG1_TRN1_APP)
      DELAY(2000)
      RED(SIG1_TRN1_APP)
      CLOSE(TRN1)
      DELAY(2000)
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(20)
    AFTER(SNS2_MAIN_TRN1_EX)
    FREE(BLK1_TRN1_APP)
    FOLLOW(BLK2_BLK4)

Moving from block 1 to block 3 - entering the station
_____________________________________________________

To move from block 1 to block 3, we again use ``RESERVE()``.

As per our move to block 2 above, we ensure turnout 1 is set correctly, however this time we need it to be thrown rather than closed, and so again set our signals if it needs to change.

Once the turnout is thrown, or if it already was, we set our signal green and tell the train to proceed at a very lesuirely speed of 10 ``FWD(10)`` as we need to be cautious approaching the station.

The train needs to ``STOP`` at the appropriate point on the station ``AT(SNS3_STN)``, at which point the reservation on block 1 can be released as we no longer occupy it ``FREE(BLK1_TRN1_APP)`` and it's safe for another train to enter that block.

There is now a delay of 10 to 15 seconds while our passengers embark or disembark ``DELAYRANDOM(10000, 15000)``, before moving off again at low speed ``FWD(10)`` until sensor 5 is reached ``AT(SNS5_STN_TRN2_APP)``, at which point the control of the train is over to the :ref:`big-picture/stage1:moving from block 3 to block 4 - exiting the station siding` sequence.

.. code-block:: 

  // Sequence to go from block 1 to block 3
  SEQUENCE(BLK1_BLK3)
    RESERVE(BLK3_STN)
    IFCLOSED(TRN1)
      AMBER(SIG1_TRN1_APP)
      DELAY(2000)
      RED(SIG1_TRN1_APP)
      THROW(TRN1)
      DELAY(2000)
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(10)
    AT(SNS3_STN)
    STOP
    FREE(BLK1_TRN1_APP)
    DELAYRANDOM(10000, 15000)
    FWD(10)
    AT(SNS5_STN_TRN2_APP)
    FOLLOW(BLK3_BLK4)

Moving from block 2 to block 4 - continue on the main track
___________________________________________________________

There are no new concepts here compared with our previous virtual block sequences, and we again need to ensure block 4 is free prior to entering it, then ensure our signals and turnout are set correctly, and once again after leaving block 2 ``AFTER(SNS4_MAIN_TRN2_APP)`` we free block 2 in order for the next train to be able to safely enter it.

Once done, train control is over to the :ref:`big-picture/stage1:moving from block 4 to block 1 - the speed run` sequence.

.. note:: 

  Note that we start with train 2 occupying block 2, and train 3 occupying block 4 (both with a ``RESERVE()`` in place as part of our startup sequence) and therefore train 2 cannot proceed until train 3 has exited block 4.

  Also on startup, train 1 is occupying block 1 (with a ``RESERVE()`` in place as part of our startup sequence), and therefore until train 1 exits block 1, train 3 cannot enter block 1.

  This creates a domino effect whereby train 1's exit of block 1 is needed in order for train 3 to enter block 1, and likewise for train 3 to exit block 4 in order for train 2 to enter block 4. The trains will then follow the sequences around the layout accordingly.

.. code-block:: 

  // Sequence to go from block 2 to block 4
  SEQUENCE(BLK2_BLK4)
    RESERVE(BLK4_TRN2_EX)
    IFTHROWN(TRN2)
      AMBER(SIG2_TRN2_GO)
      AMBER(SIG3_STN_EX)
      DELAY(2000)
      RED(SIG2_TRN2_GO)
      RED(SIG3_STN_EX)
      CLOSE(TRN2)
      DELAY(2000)
    ENDIF
    GREEN(SIG2_TRN2_GO)
    FWD(20)
    AFTER(SNS4_MAIN_TRN2_APP)
    FREE(BLK2_MAIN_HOLD)
    FOLLOW(BLK4_BLK1)

Moving from block 3 to block 4 - exiting the station siding
___________________________________________________________

Leaving the station siding is another repeat of the same logic, ensuring block 4 is free to enter, our signals and turnout are set correctly, and again freeing block 3 after we leave it ``AFTER(SNS5_STN_TRN2_APP)``.

Control is then handed over to the :ref:`big-picture/stage1:moving from block 4 to block 1 - the speed run` sequence.

.. code-block:: 

  // Sequence to go from block 3 to block 4
  SEQUENCE(BLK3_BLK4)
    RESERVE(BLK4_TRN2_EX)
    IFCLOSED(TRN2)
      AMBER(SIG2_TRN2_GO)
      AMBER(SIG3_STN_EX)
      DELAY(2000)
      RED(SIG2_TRN2_GO)
      RED(SIG3_STN_EX)
      THROW(TRN2)
      DELAY(2000)
    ENDIF
    GREEN(SIG3_STN_EX)
    FWD(20)
    AFTER(SNS5_STN_TRN2_APP)
    FREE(BLK3_STN)
    FOLLOW(BLK4_BLK1)

Moving from block 4 to block 1 - the speed run
______________________________________________

The final sequence is the simplest of all, and allows for a higher speed run through block 4 ``FWD(40)`` (providing block 1 is free to enter), again freeing up block 4 once we've exited it ``AFTER(SNS1_TRN1_APP)``, and then finally handing control back to our original :ref:`big-picture/stage1:exiting block 1 - station entry or main track?` decision sequence.

Again, we start up with train 3 occupying block 4, and once train 1 has exited block 1, the squence below will execute, with train 3 moving to block 1, and train 2 being able to exit block 2.

.. code-block:: 

  // Sequence to move from block 4 back to block 1
  SEQUENCE(BLK4_BLK1)
    RESERVE(BLK1_TRN1_APP)
    FWD(40)
    AFTER(SNS1_TRN1_APP)
    FREE(BLK4_TRN2_EX)
    FOLLOW(BLK1_EXIT)

Learnings from stage 1
======================

No doubt, as you've read through this fairly lengthy stage 1 page, you've already noted a number of commonalities between all variations of myAutomation.h, regardless of the way we have defined the various objects, and hopefully you've picked up a few tips and techniques to help you on your DCC++ EX and EX-RAIL journey.

The main things at this point that we'd like to call to your attenion are:

* Using aliases helps your brain along. Most of us aren't geared to remember that turnout ID 100 is the station siding entrance turnout, so defining aliases makes these numbers easier to digest and work with when referring to them in myAutomation.h.
* You can expand your I/O devices as you need. The Mega2560 provides easily for 42 available I/O pins (A2 to A15, and 22 to 49), but when you exceed this limit, you can very easily expand this using I/O expanders such as the MCP23017. This means you don't need to have all these devices up front and can start with just the Mega2560.
* Use virtual blocks to safely control automation of your layout. With appropriate use of ``RESERVE()`` and ``FREE()`` along with appropriate location of sensors, you can safely have a number of different trains traversing all sorts of layouts without colliding.
* EX-RAIL is an incredibly powerful piece of software that can automate the most basic, simple layout functions as well as provide fully automated, prototypical operation of an entire layout which is limited only by your imagination.

Complete myAutomation.h examples
================================

ROUTEs with DCC accessory turnouts and signals on Mega2560 direct I/O pins
__________________________________________________________________________

.. code-block:: 

  // myAutomation.h for simple ROUTEs with pin turnouts and signals directly connected to the Mega2560.

  // Define our aliases:
  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SIG1_TRN1_APP, 30)
  ALIAS(SIG2_TRN2_GO, 33)
  ALIAS(SIG3_STN_EX, 36)

  // Define our objects:
  TURNOUT(TRN1, 26, 0, "Station entry")
  TURNOUT(TRN2, 26, 1, "Station exit")
  SIGNAL(SIG1_TRN1_APP, 31, 32)
  SIGNAL(SIG2_TRN2_GO, 34, 35)
  SIGNAL(SIG3_STN_EX, 37, 38)

  // Start up with turnouts closed and signals red
  CLOSE(TRN1)
  CLOSE(TRN2)
  RED(SIG1_TRN1_APP)
  RED(SIG2_TRN2_GO)
  RED(SIG3_STN_EX)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

  // Define our ROUTEs:
  ROUTE(1, "Main track")        // Select this route to just use the main track
    RED(SIG3_STN_EX)            // Set signal 3 red as it is not safe to exit the station siding
    IFTHROWN(TRN1)              // If turnout 1 is thrown, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we close turnout 1
      CLOSE(TRN1)               // Close turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to close
    ENDIF
    IFTHROWN(TRN2)              // If turnout 2 is thrown, do these:
      AMBER(SIG2_TRN2_GO)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG2_TRN2_GO)         // Set signal 2 red while we close turnout 2
      CLOSE(TRN2)               // Close turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to close
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG2_TRN2_GO)         // Set signal 2 green because we're safe to proceed
  DONE

  ROUTE(2, "Station siding")    // Select this route to use the station siding
    RED(SIG2_TRN2_GO)           // Set signal 2 red as it is not safe to proceed beyond turnout 2 on the main track
    IFCLOSED(TRN1)              // If turnout 1 is closed, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we throw turnout 1
      THROW(TRN1)               // Throw turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    IFCLOSED(TRN2)              // If turnout 2 is closed, do these:
      AMBER(SIG3_STN_EX)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG3_STN_EX)         // Set signal 2 red while we throw turnout 2
      THROW(TRN2)               // Throw turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG3_STN_EX)          // Set signal 2 green because we're safe to proceed
  DONE

ROUTEs with turnouts/signals on Mega2560 direct I/O pins
________________________________________________________

.. code-block:: 

  // myAutomation.h for simple ROUTEs with pin turnouts and signals directly connected to the Mega2560.

  // Define our aliases:
  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SIG1_TRN1_APP, 30)
  ALIAS(SIG2_TRN2_GO, 33)
  ALIAS(SIG3_STN_EX, 36)

  // Define our objects:
  PIN_TURNOUT(TRN1, 22, "Station entry")
  PIN_TURNOUT(TRN2, 23, "Station exit")
  SIGNAL(SIG1_TRN1_APP, 31, 32)
  SIGNAL(SIG2_TRN2_GO, 34, 35)
  SIGNAL(SIG3_STN_EX, 37, 38)

  // Start up with turnouts closed and signals red
  CLOSE(TRN1)
  CLOSE(TRN2)
  RED(SIG1_TRN1_APP)
  RED(SIG2_TRN2_GO)
  RED(SIG3_STN_EX)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

  // Define our ROUTEs:
  ROUTE(1, "Main track")        // Select this route to just use the main track
    RED(SIG3_STN_EX)            // Set signal 3 red as it is not safe to exit the station siding
    IFTHROWN(TRN1)              // If turnout 1 is thrown, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we close turnout 1
      CLOSE(TRN1)               // Close turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to close
    ENDIF
    IFTHROWN(TRN2)              // If turnout 2 is thrown, do these:
      AMBER(SIG2_TRN2_GO)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG2_TRN2_GO)         // Set signal 2 red while we close turnout 2
      CLOSE(TRN2)               // Close turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to close
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG2_TRN2_GO)         // Set signal 2 green because we're safe to proceed
  DONE

  ROUTE(2, "Station siding")    // Select this route to use the station siding
    RED(SIG2_TRN2_GO)           // Set signal 2 red as it is not safe to proceed beyond turnout 2 on the main track
    IFCLOSED(TRN1)              // If turnout 1 is closed, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we throw turnout 1
      THROW(TRN1)               // Throw turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    IFCLOSED(TRN2)              // If turnout 2 is closed, do these:
      AMBER(SIG3_STN_EX)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG3_STN_EX)         // Set signal 2 red while we throw turnout 2
      THROW(TRN2)               // Throw turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG3_STN_EX)          // Set signal 2 green because we're safe to proceed
  DONE

ROUTEs with turnouts/signals on MCP23017 I/O expander Vpins
___________________________________________________________

.. code-block:: 

  // myAutomation.h for simple ROUTEs with pin based turnouts and signals via MCP23017 I/O expander Vpins.

  // Define our aliases:
  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SIG1_TRN1_APP, 172)
  ALIAS(SIG2_TRN2_GO, 175)
  ALIAS(SIG3_STN_EX, 178)

  // Define our objects:
  PIN_TURNOUT(TRN1, 22, "Station entry")
  PIN_TURNOUT(TRN2, 23, "Station exit")
  SIGNAL(SIG1_TRN1_APP, 173, 174)
  SIGNAL(SIG2_TRN2_GO, 176, 177)
  SIGNAL(SIG3_STN_EX, 179, 180)

  // Start up with turnouts closed and signals red
  CLOSE(TRN1)
  CLOSE(TRN2)
  RED(SIG1_TRN1_APP)
  RED(SIG2_TRN2_GO)
  RED(SIG3_STN_EX)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

  // Define our ROUTEs:
  ROUTE(1, "Main track")        // Select this route to just use the main track
    RED(SIG3_STN_EX)            // Set signal 3 red as it is not safe to exit the station siding
    IFTHROWN(TRN1)              // If turnout 1 is thrown, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we close turnout 1
      CLOSE(TRN1)               // Close turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to close
    ENDIF
    IFTHROWN(TRN2)              // If turnout 2 is thrown, do these:
      AMBER(SIG2_TRN2_GO)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG2_TRN2_GO)         // Set signal 2 red while we close turnout 2
      CLOSE(TRN2)               // Close turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to close
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG2_TRN2_GO)         // Set signal 2 green because we're safe to proceed
  DONE

  ROUTE(2, "Station siding")    // Select this route to use the station siding
    RED(SIG2_TRN2_GO)           // Set signal 2 red as it is not safe to proceed beyond turnout 2 on the main track
    IFCLOSED(TRN1)              // If turnout 1 is closed, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we throw turnout 1
      THROW(TRN1)               // Throw turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    IFCLOSED(TRN2)              // If turnout 2 is closed, do these:
      AMBER(SIG3_STN_EX)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG3_STN_EX)         // Set signal 2 red while we throw turnout 2
      THROW(TRN2)               // Throw turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG3_STN_EX)          // Set signal 2 green because we're safe to proceed
  DONE

ROUTEs with servo based turnouts/signals on a PCA9685 servo module
__________________________________________________________________

.. code-block:: 

  // myAutomation.h for simple ROUTEs with servo based turnouts and signals.

  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SIG1_TRN1_APP, 102)
  ALIAS(SIG2_TRN2_GO, 103)
  ALIAS(SIG3_STN_EX, 104)

  // Start up with turnouts closed and signals red
  CLOSE(TRN1)
  CLOSE(TRN2)
  RED(SIG1_TRN1_APP)
  RED(SIG2_TRN2_GO)
  RED(SIG3_STN_EX)
  
  SERVO_TURNOUT(TRN1, 100, 400, 100, Slow, "Station entry")
  SERVO_TURNOUT(TRN2, 101, 400, 100, Slow, "Station exit")
  SERVO_SIGNAL(SIG1_TRN1_APP, 400, 250, 100)
  SERVO_SIGNAL(SIG2_TRN2_GO, 400, 250, 100)
  SERVO_SIGNAL(SIG3_STN_EX, 400, 250, 100)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

  // Define our ROUTEs:
  ROUTE(1, "Main track")        // Select this route to just use the main track
    RED(SIG3_STN_EX)            // Set signal 3 red as it is not safe to exit the station siding
    IFTHROWN(TRN1)              // If turnout 1 is thrown, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we close turnout 1
      CLOSE(TRN1)               // Close turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to close
    ENDIF
    IFTHROWN(TRN2)              // If turnout 2 is thrown, do these:
      AMBER(SIG2_TRN2_GO)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG2_TRN2_GO)         // Set signal 2 red while we close turnout 2
      CLOSE(TRN2)               // Close turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to close
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG2_TRN2_GO)         // Set signal 2 green because we're safe to proceed
  DONE

  ROUTE(2, "Station siding")    // Select this route to use the station siding
    RED(SIG2_TRN2_GO)           // Set signal 2 red as it is not safe to proceed beyond turnout 2 on the main track
    IFCLOSED(TRN1)              // If turnout 1 is closed, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we throw turnout 1
      THROW(TRN1)               // Throw turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    IFCLOSED(TRN2)              // If turnout 2 is closed, do these:
      AMBER(SIG3_STN_EX)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG3_STN_EX)         // Set signal 2 red while we throw turnout 2
      THROW(TRN2)               // Throw turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG3_STN_EX)          // Set signal 2 green because we're safe to proceed
  DONE

Full automation with pin based turnouts and signals on Mega2560 direct I/O pins
_______________________________________________________________________________

.. code-block:: 

  // myAutomation.h for SEQUENCEs with pin turnouts, sensors, and signals directly connected to the Mega2560.

  // Define our aliases:
  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SNS1_TRN1_APP, 24)
  ALIAS(SNS2_MAIN_TRN1_EX, 25)
  ALIAS(SNS3_STN, 26)
  ALIAS(SNS4_MAIN_TRN2_APP, 27)
  ALIAS(SNS5_STN_TRN2_APP, 28)
  ALIAS(SIG1_TRN1_APP, 30)
  ALIAS(SIG2_TRN2_GO, 33)
  ALIAS(SIG3_STN_EX, 36)
  ALIAS(BLK1_TRN1_APP, 1)
  ALIAS(BLK2_MAIN_HOLD, 2)
  ALIAS(BLK3_STN, 3)
  ALIAS(BLK4_TRN2_EX, 4)
  ALIAS(BLK1_EXIT, 1)
  ALIAS(BLK1_BLK2, 2)
  ALIAS(BLK1_BLK3, 3)
  ALIAS(BLK2_BLK4, 4)
  ALIAS(BLK3_BLK4, 5)
  ALIAS(BLK4_BLK1, 6)
  ALIAS(CHOOSE_BLK2, 60)
  
  // Define our objects:
  PIN_TURNOUT(TRN1, 22, "Station entry")
  PIN_TURNOUT(TRN2, 23, "Station exit")
  SIGNAL(SIG1_TRN1_APP, 31, 32)
  SIGNAL(SIG2_TRN2_GO, 34, 35)
  SIGNAL(SIG3_STN_EX, 37, 38)

  // Start up with turnouts closed and signals red
  CLOSE(TRN1)
  CLOSE(TRN2)
  RED(SIG1_TRN1_APP)
  RED(SIG2_TRN2_GO)
  RED(SIG3_STN_EX)

  // Send three locos around our layout:
  RESERVE(BLK1_TRN1_APP)
  RESERVE(BLK2_MAIN_HOLD)
  RESERVE(BLK4_TRN2_EX)
  SENDLOCO(1, BLK1_EXIT)
  SENDLOCO(2, BLK2_BLK4)
  SENDLOCO(3, BLK4_BLK1)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

  // Sequence to exit block 1, and choose whether to go to the station or continue on main
  SEQUENCE(BLK1_EXIT)
    IF(CHOOSE_BLK2)
      UNLATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK2)
    ELSE
      LATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK3)
    ENDIF

  // Sequence to go from block 1 to block 2
  SEQUENCE(BLK1_BLK2)
    RESERVE(BLK2_MAIN_HOLD)
    IFTHROWN(TRN1)
      AMBER(SIG1_TRN1_APP)
      DELAY(2000)
      RED(SIG1_TRN1_APP)
      CLOSE(TRN1)
      DELAY(2000)
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(20)
    AFTER(SNS2_MAIN_TRN1_EX)
    FREE(BLK1_TRN1_APP)
    FOLLOW(BLK2_BLK4)

  // Sequence to go from block 1 to block 3
  SEQUENCE(BLK1_BLK3)
    RESERVE(BLK3_STN)
    IFCLOSED(TRN1)
      AMBER(SIG1_TRN1_APP)
      DELAY(2000)
      RED(SIG1_TRN1_APP)
      THROW(TRN1)
      DELAY(2000)
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(10)
    AT(SNS3_STN)
    STOP
    FREE(BLK1_TRN1_APP)
    DELAYRANDOM(10000, 15000)
    FWD(10)
    AT(SNS5_STN_TRN2_APP)
    FOLLOW(BLK3_BLK4)

  // Sequence to go from block 2 to block 4
  SEQUENCE(BLK2_BLK4)
    RESERVE(BLK4_TRN2_EX)
    IFTHROWN(TRN2)
      AMBER(SIG2_TRN2_GO)
      AMBER(SIG3_STN_EX)
      DELAY(2000)
      RED(SIG2_TRN2_GO)
      RED(SIG3_STN_EX)
      CLOSE(TRN2)
      DELAY(2000)
    ENDIF
    GREEN(SIG2_TRN2_GO)
    FWD(20)
    AFTER(SNS4_MAIN_TRN2_APP)
    FREE(BLK2_MAIN_HOLD)
    FOLLOW(BLK4_BLK1)
  
  // Sequence to go from block 3 to block 4
  SEQUENCE(BLK3_BLK4)
    RESERVE(BLK4_TRN2_EX)
    IFCLOSED(TRN2)
      AMBER(SIG2_TRN2_GO)
      AMBER(SIG3_STN_EX)
      DELAY(2000)
      RED(SIG2_TRN2_GO)
      RED(SIG3_STN_EX)
      THROW(TRN2)
      DELAY(2000)
    ENDIF
    GREEN(SIG3_STN_EX)
    FWD(20)
    AFTER(SNS5_STN_TRN2_APP)
    FREE(BLK3_STN)
    FOLLOW(BLK4_BLK1)
  
  // Sequence to move from block 4 back to block 1
  SEQUENCE(BLK4_BLK1)
    RESERVE(BLK1_TRN1_APP)
    FWD(30)
    AFTER(SNS1_TRN1_APP)
    FREE(BLK4_TRN2_EX)
    FOLLOW(BLK1_EXIT)

Full automation with pin based turnouts and signals on MCP23017 I/O expander Vpins
__________________________________________________________________________________

.. code-block:: 

  // myAutomation.h for SEQUENCEs with pin based turnouts, sensors, and signals via MCP23017 I/O expander Vpins.

  // Define our aliases:
  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SNS1_TRN1_APP, 166)
  ALIAS(SNS2_MAIN_TRN1_EX, 167)
  ALIAS(SNS3_STN, 168)
  ALIAS(SNS4_MAIN_TRN2_APP, 169)
  ALIAS(SNS5_STN_TRN2_APP, 170)
  ALIAS(SNS6_TRN2_EX, 171)
  ALIAS(SIG1_TRN1_APP, 172)
  ALIAS(SIG2_TRN2_GO, 175)
  ALIAS(SIG3_STN_EX, 178)
  ALIAS(BLK1_TRN1_APP, 1)
  ALIAS(BLK2_MAIN_HOLD, 2)
  ALIAS(BLK3_STN, 3)
  ALIAS(BLK4_TRN2_EX, 4)
  ALIAS(BLK1_EXIT, 1)
  ALIAS(BLK1_BLK2, 2)
  ALIAS(BLK1_BLK3, 3)
  ALIAS(BLK2_BLK4, 4)
  ALIAS(BLK3_BLK4, 5)
  ALIAS(BLK4_BLK1, 6)
  ALIAS(CHOOSE_BLK2, 60)

  // Define our objects:
  PIN_TURNOUT(TRN1, 22, "Station entry")
  PIN_TURNOUT(TRN2, 23, "Station exit")
  SIGNAL(SIG1_TRN1_APP, 173, 174)
  SIGNAL(SIG2_TRN2_GO, 176, 177)
  SIGNAL(SIG3_STN_EX, 179, 180)

  // Start up with turnouts closed and signals red
  CLOSE(TRN1)
  CLOSE(TRN2)
  RED(SIG1_TRN1_APP)
  RED(SIG2_TRN2_GO)
  RED(SIG3_STN_EX)

  // Send three locos around our layout:
  RESERVE(BLK1_TRN1_APP)
  RESERVE(BLK2_MAIN_HOLD)
  RESERVE(BLK4_TRN2_EX)
  SENDLOCO(1, BLK1_EXIT)
  SENDLOCO(2, BLK2_BLK4)
  SENDLOCO(3, BLK4_BLK1)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

  // Sequence to exit block 1, and choose whether to go to the station or continue on main
  SEQUENCE(BLK1_EXIT)
    IF(CHOOSE_BLK2)
      UNLATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK2)
    ELSE
      LATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK3)
    ENDIF

  // Sequence to go from block 1 to block 2
  SEQUENCE(BLK1_BLK2)
    RESERVE(BLK2_MAIN_HOLD)
    IFTHROWN(TRN1)
      AMBER(SIG1_TRN1_APP)
      DELAY(2000)
      RED(SIG1_TRN1_APP)
      CLOSE(TRN1)
      DELAY(2000)
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(20)
    AFTER(SNS2_MAIN_TRN1_EX)
    FREE(BLK1_TRN1_APP)
    FOLLOW(BLK2_BLK4)

  // Sequence to go from block 1 to block 3
  SEQUENCE(BLK1_BLK3)
    RESERVE(BLK3_STN)
    IFCLOSED(TRN1)
      AMBER(SIG1_TRN1_APP)
      DELAY(2000)
      RED(SIG1_TRN1_APP)
      THROW(TRN1)
      DELAY(2000)
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(10)
    AT(SNS3_STN)
    STOP
    FREE(BLK1_TRN1_APP)
    DELAYRANDOM(10000, 15000)
    FWD(10)
    AT(SNS5_STN_TRN2_APP)
    FOLLOW(BLK3_BLK4)

  // Sequence to go from block 2 to block 4
  SEQUENCE(BLK2_BLK4)
    RESERVE(BLK4_TRN2_EX)
    IFTHROWN(TRN2)
      AMBER(SIG2_TRN2_GO)
      AMBER(SIG3_STN_EX)
      DELAY(2000)
      RED(SIG2_TRN2_GO)
      RED(SIG3_STN_EX)
      CLOSE(TRN2)
      DELAY(2000)
    ENDIF
    GREEN(SIG2_TRN2_GO)
    FWD(20)
    AFTER(SNS4_MAIN_TRN2_APP)
    FREE(BLK2_MAIN_HOLD)
    FOLLOW(BLK4_BLK1)
  
  // Sequence to go from block 3 to block 4
  SEQUENCE(BLK3_BLK4)
    RESERVE(BLK4_TRN2_EX)
    IFCLOSED(TRN2)
      AMBER(SIG2_TRN2_GO)
      AMBER(SIG3_STN_EX)
      DELAY(2000)
      RED(SIG2_TRN2_GO)
      RED(SIG3_STN_EX)
      THROW(TRN2)
      DELAY(2000)
    ENDIF
    GREEN(SIG3_STN_EX)
    FWD(20)
    AFTER(SNS5_STN_TRN2_APP)
    FREE(BLK3_STN)
    FOLLOW(BLK4_BLK1)
  
  // Sequence to move from block 4 back to block 1
  SEQUENCE(BLK4_BLK1)
    RESERVE(BLK1_TRN1_APP)
    FWD(30)
    AFTER(SNS1_TRN1_APP)
    FREE(BLK4_TRN2_EX)
    FOLLOW(BLK1_EXIT)

Full automation with servo based turnouts and signals with a PCA9685 servo module
_________________________________________________________________________________

.. code-block:: 

  // myAutomation.h for simple ROUTEs with servo based turnouts and signals, and sensors directly connected to the Mega2560.

  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SNS1_TRN1_APP, 24)
  ALIAS(SNS2_MAIN_TRN1_EX, 25)
  ALIAS(SNS3_STN, 26)
  ALIAS(SNS4_MAIN_TRN2_APP, 27)
  ALIAS(SNS5_STN_TRN2_APP, 28)
  ALIAS(SNS6_TRN2_EX, 29)
  ALIAS(SIG1_TRN1_APP, 102)
  ALIAS(SIG2_TRN2_GO, 103)
  ALIAS(SIG3_STN_EX, 104)
  ALIAS(BLK1_TRN1_APP, 1)
  ALIAS(BLK2_MAIN_HOLD, 2)
  ALIAS(BLK3_STN, 3)
  ALIAS(BLK4_TRN2_EX, 4)
  ALIAS(BLK1_EXIT, 1)
  ALIAS(BLK1_BLK2, 2)
  ALIAS(BLK1_BLK3, 3)
  ALIAS(BLK2_BLK4, 4)
  ALIAS(BLK3_BLK4, 5)
  ALIAS(BLK4_BLK1, 6)
  ALIAS(CHOOSE_BLK2, 60)
  
  SERVO_TURNOUT(TRN1, 100, 400, 100, Slow, "Station entry")
  SERVO_TURNOUT(TRN2, 101, 400, 100, Slow, "Station exit")
  SERVO_SIGNAL(SIG1_TRN1_APP, 400, 250, 100)
  SERVO_SIGNAL(SIG2_TRN2_GO, 400, 250, 100)
  SERVO_SIGNAL(SIG3_STN_EX, 400, 250, 100)

  // Start up with turnouts closed and signals red
  CLOSE(TRN1)
  CLOSE(TRN2)
  RED(SIG1_TRN1_APP)
  RED(SIG2_TRN2_GO)
  RED(SIG3_STN_EX)

  // Send three locos around our layout:
  RESERVE(BLK1_TRN1_APP)
  RESERVE(BLK2_MAIN_HOLD)
  RESERVE(BLK4_TRN2_EX)
  SENDLOCO(1, BLK1_EXIT)
  SENDLOCO(2, BLK2_BLK4)
  SENDLOCO(3, BLK4_BLK1)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

  // Sequence to exit block 1, and choose whether to go to the station or continue on main
  SEQUENCE(BLK1_EXIT)
    IF(CHOOSE_BLK2)
      UNLATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK2)
    ELSE
      LATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK3)
    ENDIF

  // Sequence to go from block 1 to block 2
  SEQUENCE(BLK1_BLK2)
    RESERVE(BLK2_MAIN_HOLD)
    IFTHROWN(TRN1)
      AMBER(SIG1_TRN1_APP)
      DELAY(2000)
      RED(SIG1_TRN1_APP)
      CLOSE(TRN1)
      DELAY(2000)
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(20)
    AFTER(SNS2_MAIN_TRN1_EX)
    FREE(BLK1_TRN1_APP)
    FOLLOW(BLK2_BLK4)

  // Sequence to go from block 1 to block 3
  SEQUENCE(BLK1_BLK3)
    RESERVE(BLK3_STN)
    IFCLOSED(TRN1)
      AMBER(SIG1_TRN1_APP)
      DELAY(2000)
      RED(SIG1_TRN1_APP)
      THROW(TRN1)
      DELAY(2000)
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(10)
    AT(SNS3_STN)
    STOP
    FREE(BLK1_TRN1_APP)
    DELAYRANDOM(10000, 15000)
    FWD(10)
    AT(SNS5_STN_TRN2_APP)
    FOLLOW(BLK3_BLK4)

  // Sequence to go from block 2 to block 4
  SEQUENCE(BLK2_BLK4)
    RESERVE(BLK4_TRN2_EX)
    IFTHROWN(TRN2)
      AMBER(SIG2_TRN2_GO)
      AMBER(SIG3_STN_EX)
      DELAY(2000)
      RED(SIG2_TRN2_GO)
      RED(SIG3_STN_EX)
      CLOSE(TRN2)
      DELAY(2000)
    ENDIF
    GREEN(SIG2_TRN2_GO)
    FWD(20)
    AFTER(SNS4_MAIN_TRN2_APP)
    FREE(BLK2_MAIN_HOLD)
    FOLLOW(BLK4_BLK1)
  
  // Sequence to go from block 3 to block 4
  SEQUENCE(BLK3_BLK4)
    RESERVE(BLK4_TRN2_EX)
    IFCLOSED(TRN2)
      AMBER(SIG2_TRN2_GO)
      AMBER(SIG3_STN_EX)
      DELAY(2000)
      RED(SIG2_TRN2_GO)
      RED(SIG3_STN_EX)
      THROW(TRN2)
      DELAY(2000)
    ENDIF
    GREEN(SIG3_STN_EX)
    FWD(20)
    AFTER(SNS5_STN_TRN2_APP)
    FREE(BLK3_STN)
    FOLLOW(BLK4_BLK1)
  
  // Sequence to move from block 4 back to block 1
  SEQUENCE(BLK4_BLK1)
    RESERVE(BLK1_TRN1_APP)
    FWD(30)
    AFTER(SNS1_TRN1_APP)
    FREE(BLK4_TRN2_EX)
    FOLLOW(BLK1_EXIT)
