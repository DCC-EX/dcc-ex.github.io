********
Stage 1
********

.. sidebar:: On this page

   .. contents:: 
      :depth: 1
      :local:

Stage 1 of our RMFT layout is a simple loop including a single siding for a station.

This allows for automated running of up to three trains including automated switching for entering and exiting the station siding.

We'll cover off the various aspects required to get up and running with stage 1 including object definitions, the various hardware options you can use, and how you can apply automation techniques to the layout.

What to expect to learn from stage 1
=====================================

At the end of stage 1, we expect you will learn the following:

* How to define the different types of turnout and signal objects.
* How to reference sensors.
* How, why, and when to effectively use aliases.
* How an object ID is different to the pin or configuration used by the physical object it represents.
* How to enable layout automation while still manually controlling the trains.
* How to enable a fully automated layout.
* What hardware can be used, and how to connect the components.

.. raw:: html
  :file: ../_static/images/big-picture/rmft-stage1.drawio.svg

Turnouts
=========

Two turnouts are used in this first stage of our RMFT layout to allow trains to enter and exit the station siding, or continue along the main track.

Turnout definitions
____________________

We will define turnout 1 with an ID of 100, and turnout 2 with an ID of 101.

DCC accessory turnouts
^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^

Finally, to define these same turnouts as servo based turnouts, these would be connected to a PCA9685 servo module, and our first module starts at Vpin ID 100.

Throughout these pages, we will assume that the thrown servo position is 400, the closed servo position is 100, and we will use the "Slow" profile.

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
========

Five sensors are used in this first stage, which allows us to have up to three trains controlled by EX-RAIL automation. The sensors are placed within each virtual block to ensure we know when the front of the train enters a block, and when the rear of the train has exited a block.

We don't need to explicitly define any sensor objects to work with EX-RAIL, so we will simply map these by defining EX-RAIL aliases.

To use pins directly on our Mega2560, we would start at pin 24:

.. code-block:: 

  ALIAS(SNS1_TRN1_APP, 24)       // Sensor 1, approaching turnout 1
  ALIAS(SNS2_MAIN_TRN1_EX, 25)   // Sensor 2, on the main track exiting turnout 1
  ALIAS(SNS3_STN, 26)            // Sensor 3, at our station stop
  ALIAS(SNS4_MAIN_TRN2_APP, 27)  // Sensor 4, on the main track approaching turnout 2
  ALIAS(SNS5_STN_TRN2_APP, 28)   // Sensor 5, on the station siding approaching turnout 2

Moving these to our first MCP23017 I/O expander, these would start at Vpin 166:

.. code-block:: 

  ALIAS(SNS1_TRN1_APP, 166)       // Sensor 1, approaching turnout 1
  ALIAS(SNS2_MAIN_TRN1_EX, 167)   // Sensor 2, on the main track exiting turnout 1
  ALIAS(SNS3_STN, 168)            // Sensor 3, at our station stop
  ALIAS(SNS4_MAIN_TRN2_APP, 169)  // Sensor 4, on the main track approaching turnout 2
  ALIAS(SNS5_STN_TRN2_APP, 170)   // Sensor 5, on the station siding approaching turnout 2

Signals
========

Three signals have been used in this first stage to indicate whether or not a train can enter either the station siding or proceed beyond turnout 1 on the main track, to indicate whether a train can exit the station siding, or if a train can proceed beyond turnout 2 on the main track.

Pin based signals
__________________

To use pin based signals, we require three pins per signal, and therefore nine pins in total, but we will only define an alias for the red pin given that it is the "control" pin for each signal. 

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
____________________

To define servo based signals, these only require one Vpin per signal along with specifying the servo angle for the red, amber, and green positions.

Allowing for servo based turnouts being used, we will start our signals from the third available Vpin on our PCA9685 servo module. We will make the assumption that red requires a servo angle of 100, amber 250, and green 400:

.. code-block:: 

  ALIAS(SIG1_TRN1_APP, 102)       // Signal 1, approaching turnout 1
  ALIAS(SIG2_TRN2_GO, 103)        // Signal 2, proceed beyond turnout 2
  ALIAS(SIG3_STN_EX, 104)         // Signal 3, exit the station siding

  SERVO_SIGNAL(SIG1_TRN1_APP, 400, 250, 100)
  SERVO_SIGNAL(SIG2_TRN2_GO, 400, 250, 100)
  SERVO_SIGNAL(SIG3_STN_EX, 400, 250, 100)

Virtual blocks
===============

We've divided the layout into four virtual blocks, allowing for up to three trains to coexist safely on the layout.

Block 1
________

Block 1 is the approach to turnout 1, and prevents a train entering either the station siding or the main track between turnouts 1 and 2 if they are occupied.

We will use ID 1 for this, with an alias:

.. code-block:: 

  ALIAS(BLK1_TRN1_APP, 1)

Block 2
________

Block 2 consists of the section of the main track between turnouts 1 and 2, providing for a section to hold one train, allow a train on the station siding to exit safely, and also prevent a train running around the main track from entering this block.

We will use ID 2 for this, with an alias:

.. code-block:: 

  ALIAS(BLK2_MAIN_HOLD, 2)

Block 3
________

Block 3 is for our station siding, ensuring no other trains can enter this block while it is occupied.

We will use ID 3 for this, with an alias:

.. code-block:: 

  ALIAS(BLK3_STN, 3)

Block 4
________

Block 4 is the exit beyond turnout 2, and can hold a train while block 1 is occupied. Once block 1 is free, a train can run uninterrupted from block 4 back to block 1.

Note that block 4 on the diagram continues all the way to the beginning of block 1

We will use ID 4 for this, with an alias:

.. code-block:: 

  ALIAS(BLK4_TRN2_EX, 4)

Station
========

In this particular stage, there's nothing specific for the station here, however some advanced concepts might be to trigger an automated sound recording of arrivals and departures based on triggering sensor 3.

This would likely make use of the EX-RAIL ``AT()`` or ``AFTER()`` commands.

Manual train control with automated routes
===========================================

If you still wish to be the driver of the trains, but have some automation related to the turnouts and signals, then we make use of EX-RAIL's ``ROUTE()`` directive. In this scenario, we don't need to implement our virtual blocks, as it will be up to you as the driver to ensure your trains don't collide! We also don't need to use the sensors, and will set our signals based on the choice of routes.

Further to this, we can ensure our two turnouts operate concurrently by using the ``ONCLOSE()`` and ``ONTHROW()`` directives.

The two routes below will be advertised to WiThrottle applicaions and Engine Driver, so you can simply select them from the ROUTE menu.

Putting all the variations above together gives us several variations of myAutomation.h.

Note that you can mix and match all the above I/O methods together, so you can use direct I/O pins on the Mega2560 while using MCP23017 I/O expanders, PCA9685 servo modules, and any other supported I/O options, which provides a myriad of possibilities to expand the I/O capabilities of your CommandStation.

For simplicity, we will outline the stage 1 options using the same hardware types otherwise we'll wear out the scroll button out on your mouse.

ROUTEs with turnouts/signals on Mega2560 direct I/O pins
_________________________________________________________

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

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

  // Define our ROUTEs:
  ROUTE(0, "Main track")        // Select this route to just use the main track
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

  ROUTE(1, "Station siding")    // Select this route to use the station siding
    RED(SIG2_TRN2_GO)           // Set signal 2 red as it is not safe to proceed beyond turnout 2 on the main track
    IFCLOSED(TRN1)              // If turnout 1 is closed, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we throw turnout 1
      THROW(TRN1)               // Throw turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    IFCLOSED(TRN2)              // If turnout 2 is closed, do these:
      AMBER(SIG2_TRN2_GO)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG2_TRN2_GO)         // Set signal 2 red while we throw turnout 2
      THROW(TRN2)               // Throw turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG3_STN_EX)          // Set signal 2 green because we're safe to proceed
  DONE

ROUTEs with turnouts/signals on MCP23017 I/O expander Vpins
____________________________________________________________

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

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

  // Define our ROUTEs:
  ROUTE(0, "Main track")        // Select this route to just use the main track
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

  ROUTE(1, "Station siding")    // Select this route to use the station siding
    RED(SIG2_TRN2_GO)           // Set signal 2 red as it is not safe to proceed beyond turnout 2 on the main track
    IFCLOSED(TRN1)              // If turnout 1 is closed, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we throw turnout 1
      THROW(TRN1)               // Throw turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    IFCLOSED(TRN2)              // If turnout 2 is closed, do these:
      AMBER(SIG2_TRN2_GO)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG2_TRN2_GO)         // Set signal 2 red while we throw turnout 2
      THROW(TRN2)               // Throw turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG3_STN_EX)          // Set signal 2 green because we're safe to proceed
  DONE

ROUTEs with servo based turnouts/signals on a PCA9685 servo module
___________________________________________________________________

.. code-block:: 

  // myAutomation.h for simple ROUTEs with servo based turnouts and signals.

  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SIG1_TRN1_APP, 102)
  ALIAS(SIG2_TRN2_GO, 103)
  ALIAS(SIG3_STN_EX, 104)
  
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
      AMBER(SIG2_TRN2_GO)       // Set signal 2 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG2_TRN2_GO)         // Set signal 2 red while we throw turnout 2
      THROW(TRN2)               // Throw turnout 2
      DELAY(2000)               // Wait 2 seconds for the turnout to throw
    ENDIF
    GREEN(SIG1_TRN1_APP)        // Set signal 1 green because we're safe to proceed
    GREEN(SIG3_STN_EX)          // Set signal 2 green because we're safe to proceed
  DONE

Fully automated layout
=======================

Now it's time to display the full automation capabilities by setting our layout up for fully automated control of your trains.

You will note that these are somewhat similar to :ref:`automation/ex-rail-intro:example 7: running multiple inter-connected trains`, updated to suit the specifics of the RMFT layout.

To setup for these fully automated sequences, we need to ensure our trains are placed in the below positions, noting that EX-RAIL has no way of knowing where a train is on the layout when first starting.

* Train 1 in block 1, between sensor 1 and turnout 1.
* Train 2 in block 2, between sensors 2 and 4.
* Train 3 in block 4, after turnout 2.

Pin based turnouts and signals on Mega2560 direct I/O pins
__________________________________________________________

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
  ALIAS(SNS6_TRN2_EX, 29)
  ALIAS(SIG1_TRN1_APP, 30)
  ALIAS(SIG2_TRN2_GO, 33)
  ALIAS(SIG3_STN_EX, 36)
  ALIAS(BLK1_EXIT, 1)
  ALIAS(BLK1_BLK2, 2)
  ALIAS(BLK2_BLK4, 3)
  ALIAS(BLK3_BLK4, 4)
  ALIAS(BLK4_BLK1, 5)
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

  AUTOMATION(BLK1_EXIT, "Start in block 1")
    IF(CHOOSE_BLK2)
      UNLATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK2)
    ELSE
      LATCH(CHOOSE_BLK2)
      FOLLOW(BLK1_BLK3)
    ENDIF

  SEQUENCE(BLK1_BLK2)
    RESERVE(BLK2_MAIN_HOLD)
    IFTHROWN(TRN1)              // If turnout 1 is thrown, do these:
      AMBER(SIG1_TRN1_APP)      // Set signal 1 amber for 2 seconds to warn of the change
      DELAY(2000)
      RED(SIG1_TRN1_APP)        // Set signal 1 red while we close turnout 1
      CLOSE(TRN1)               // Close turnout 1
      DELAY(2000)               // Wait 2 seconds for the turnout to close fully
    ENDIF
    GREEN(SIG1_TRN1_APP)
    FWD(20)
    AFTER(SNS2_MAIN_TRN1_EX)
    FREE(BLK1_TRN1_APP)
    FOLLOW(BLK2_BLK4)

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
    AT(SNS3_STN_TRN1_EX)
    STOP
    FREE(BLK1_TRN1_APP)
    DELAYRANDOM(10000, 15000)
    FWD(10)
    AT(SNS5_STN_TRN2_APP)
    FOLLOW(BLK3_BLK4)

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
  
  SEQUENCE(BLK4_BLK1)
    RESERVE(BLK1_TRN1_APP)
    FWD(30)
    AFTER(SNS1_TRN1_APP)
    FREE(BLK4_TRN2_EX)
    FOLLOW(BLK1_EXIT)

Pin based turnouts and signals on MCP23017 I/O expander Vpins
_____________________________________________________________

.. code-block:: 

  // myAutomation.h for SEQUENCEs with pin based turnouts, sensors, and signals via MCP23017 I/O expander Vpins.

  // Define our aliases:
  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SNS1_TRN1_APP, 166)
  ALIAS(SNS2_MAIN_TRN1_EX, 167)
  ALIAS(SNS3_STN_TRN1_EX, 168)
  ALIAS(SNS4_MAIN_TRN2_APP, 169)
  ALIAS(SNS5_STN_TRN2_APP, 170)
  ALIAS(SNS6_TRN2_EX, 171)
  ALIAS(SIG1_TRN1_APP, 172)
  ALIAS(SIG2_TRN2_GO, 175)
  ALIAS(SIG3_STN_EX, 178)

  // Define our objects:
  PIN_TURNOUT(TRN1, 22, "Station entry")
  PIN_TURNOUT(TRN2, 23, "Station exit")
  SIGNAL(SIG1_TRN1_APP, 173, 174)
  SIGNAL(SIG2_TRN2_GO, 176, 177)
  SIGNAL(SIG3_STN_EX, 179, 180)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

Servo based turnouts and signals with a PCA9685 servo module
_____________________________________________________________

.. code-block:: 

  // myAutomation.h for simple ROUTEs with servo based turnouts and signals, and sensors directly connected to the Mega2560.

  ALIAS(TRN1, 100)
  ALIAS(TRN2, 101)
  ALIAS(SNS1_TRN1_APP, 24)
  ALIAS(SNS2_MAIN_TRN1_EX, 25)
  ALIAS(SNS3_STN_TRN1_EX, 26)
  ALIAS(SNS4_MAIN_TRN2_APP, 27)
  ALIAS(SNS5_STN_TRN2_APP, 28)
  ALIAS(SNS6_TRN2_EX, 29)
  ALIAS(SIG1_TRN1_APP, 102)
  ALIAS(SIG2_TRN2_GO, 103)
  ALIAS(SIG3_STN_EX, 104)
  
  SERVO_TURNOUT(TRN1, 100, 400, 100, Slow, "Station entry")
  SERVO_TURNOUT(TRN2, 101, 400, 100, Slow, "Station exit")
  SERVO_SIGNAL(SIG1_TRN1_APP, 400, 250, 100)
  SERVO_SIGNAL(SIG2_TRN2_GO, 400, 250, 100)
  SERVO_SIGNAL(SIG3_STN_EX, 400, 250, 100)

  // We need DONE to tell EX-RAIL not to automatically proceed beyond definitions above
  DONE

Learnings from stage 1
=======================

No doubt, as you've ready through this fairly lengthy stage 1 page, you've already noted a number of commonalities between all variations of myAutomation.h, regardless of the way we have defined the various objects, and hopefully you've picked up a few tips and techniques to help you on your DCC++ EX and EX-RAIL journing.

The main things at this point that we'd like to call to your attenion are:

* Using aliases helps your brain along. Most of us aren't geared to remember that turnout ID 100 is the station siding entrance turnout, so defining aliases makes these numbers easier to digest and work with when referring to them in myAutomation.h.
* You can expand your I/O devices as you need. The Mega2560 provides easily for 42 available I/O pins (A2 to A15, and 22 to 49), but when you exceed this limit, you can very easily expand this using I/O expanders such as the MCP23017. This means you don't need to have all these devices up front and can start with just the Mega2560.
