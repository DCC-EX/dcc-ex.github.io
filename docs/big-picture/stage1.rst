********
Stage 1
********

Stage 1 of our RMFT layout is a simple loop including a single siding for a station.

This allows for automated running of up to three trains including automated switching for entering and exiting the station siding.

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

In EX-RAIL, we would add these lines to myAutomation.h:

.. code-block:: 

  TURNOUT(100, 26, 0, "Station entry")
  TURNOUT(101, 26, 0, "Station exit")

Pin turnouts
^^^^^^^^^^^^^

To define these same turnout IDs as pin turnouts instead, and using I/O pins that are directly on our CommandStation-EX Mega2560, we will use pins 22 and 23.

To define these in the serial console:

.. code-block:: 

  <T 100 VPIN 22>
  <T 101 VPIN 23>

In EX-RAIL, we would add these lines to myAutomation.h:

.. code-block:: 

  PIN_TURNOUT(100, 22, "Station entry")
  PIN_TURNOUT(100, 23, "Station exit")

If we were instead to use an MCP23017 I/O expander, we would use Vpins instead of direct pins on the Mega2560, and we would start these at the first I/O expander's 164 Vpin ID.

To define these in the serial console:

.. code-block:: 

  <T 100 VPIN 164>
  <T 100 VPIN 165>

And again, in myAutomation.h for EX-RAIL:

.. code-block:: 

  PIN_TURNOUT(100, 164, "Station entry")
  PIN_TURNOUT(101, 165, "Station exit")

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

  SERVO_TURNOUT(100, 100, 400, 100, Slow, "Station entry")
  SERVO_TURNOUT(101, 101, 400, 100, Slow, "Station exit")

Sensors
========

Six sensors are used in this first stage, which allows us to have up to three trains controlled by EX-RAIL automation. The sensors are placed at the beginning and end of each virtual block to ensure we know when the front of the train enters a block, and when the rear of the train has exited a block.

We don't need to explicitly define any sensor objects to work with EX-RAIL, so we will simply map these by defining EX-RAIL aliases.

To use pins directly on our Mega2560, we would start at pin 24:

.. code-block:: 

  ALIAS(SNS1_TRN1_APP, 24)       // Sensor 1, approaching turnout 1
  ALIAS(SNS2_MAIN_TRN1_EX, 25)   // Sensor 2, on the main track exiting turnout 1
  ALIAS(SNS3_STN_TRN1_EX, 26)    // Sensor 3, on the station siding exiting turnout 1
  ALIAS(SNS4_MAIN_TRN2_APP, 27)  // Sensor 4, on the main track approaching turnout 2
  ALIAS(SNS5_STN_TRN2_APP, 28)   // Sensor 5, on the station siding approaching turnout 2
  ALIAS(SNS6_TRN2_EX, 29)        // Sensor 6, exiting turnout 2

Moving these to our first MCP23017 I/O expander, these would start at Vpin 166:

.. code-block:: 

  ALIAS(SNS1_TRN1_APP, 166)       // Sensor 1, approaching turnout 1
  ALIAS(SNS2_MAIN_TRN1_EX, 167)   // Sensor 2, on the main track exiting turnout 1
  ALIAS(SNS3_STN_TRN1_EX, 168)    // Sensor 3, on the station siding exiting turnout 1
  ALIAS(SNS4_MAIN_TRN2_APP, 169)  // Sensor 4, on the main track approaching turnout 2
  ALIAS(SNS5_STN_TRN2_APP, 170)   // Sensor 5, on the station siding approaching turnout 2
  ALIAS(SNS6_TRN2_EX, 171)        // Sensor 6, exiting turnout 2

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

We will use ID 0 for this, with an alias:

.. code-block:: 

  ALIAS(BLK1_TRN1_APP, 0)

Block 2
________

Block 2 consists of the section of the main track between turnouts 1 and 2, providing for a section to hold one train, allow a train on the station siding to exit safely, and also prevent a train running around the main track from entering this block.

We will use ID 1 for this, with an alias:

.. code-block:: 

  ALIAS(BLK2_MAIN_HOLD, 1)

Block 3
________

Block 3 is for our station siding, ensuring no other trains can enter this block while it is occupied.

We will use ID 2 for this, with an alias:

.. code-block:: 

  ALIAS(BLK3_STN, 2)

Block 4
________

Block 4 is the exit beyond turnout 2, and can hold a train while block 1 is occupied. Once block 1 is free, a train can run uninterrupted from block 4 back to block 1.

We will use ID 3 for this, with an alias:

.. code-block:: 

  ALIAS(BLK4_TRN2_EX, 3)

Station
========

In this particular stage, there's nothing specific for the station here, however some advanced concepts might be to trigger an automated sound recording of arrivals and departures based on triggering sensor 3.

This would likely make use of the EX-RAIL ``AT()`` command.
