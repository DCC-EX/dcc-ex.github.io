*********************************
Testing, Tuning, and Control
*********************************

Turntable-EX commands
=====================

Before proceeding with testing or any configuration, it's important to understand the two commands available for controlling Turntable-EX.

This is a debug or diagnostic command that can be executed via the serial terminal:

.. code-block:: 

  <D TT vpin steps activity>

This is the EX-RAIL command to be included in myAutomation.h:

.. code-block:: cpp

  MOVETT(vpin, steps, activity)

For both of these commands, "vpin" is as defined in your "myHal.cpp" file, and "steps" is the number of steps from the home position, not the number of steps you wish the turntable to travel.

For the diagnostic command, "activity" needs to be defined as a number, whereas for the EX-RAIL command, this is defined as text based on the table below. Sound confusing? The reason for using text in the EX-RAIL command is to make your automation sequences more "human-friendly" when reading what they do later.

.. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * - Diagnostic activity
      - EX-RAIL activity
      - Description
    * - 0
      - Turn
      - Turn to the desired step position
    * - 1
      - Turn_PInvert
      - Turn to the desired step position and invert the phase/polarity
    * - 2
      - Home
      - Activate the homing process, ignore the provided step position

Here's a quick example to demonstrate the difference between the diagnostic and EX-RAIL commands, with both commands below rotating to step position 100, and both inverting the phase/polarity of the bridge track:

.. code-block:: 

  <D TT 600 100 1>
  MOVETT(600, 100, Turn_PInvert)

Note with the phase/polarity inversion, this activity must be defined for every position that requires the phase to be inverted compared with the surrounding tracks. If it is not defined, the relays will be deactivated, resulting in no phase/polarity inversion.

Testing Turntable-EX
====================

Firstly, power on Turntable-EX, followed by your CommandStation. By powering these on in that order, you will ensure that Turntable-EX is available prior to the CommandStation trying to load the device driver, otherwise it will consider the device as "OFFLINE", and commands will fail.

Referring again to :ref:`reference/software/hal-config:adding a new device`, skip ahead to :ref:`reference/software/hal-config:checking the driver`, and the output you're looking for to validate the Turntable-EX device driver is loaded and connected successfully is below:

.. code-block:: 

  <D HAL SHOW><* Arduino Vpins:2-69 *>
  <* PCA9685 I2C:x40 Configured on Vpins:100-115  *>
  <* PCA9685 I2C:x41 Configured on Vpins:116-131 OFFLINE *>
  <* MCP23017 I2C:x20 Configured on Vpins:164-179 OFFLINE *>
  <* MCP23017 I2C:x21 Configured on Vpins:180-195 OFFLINE *>
  <* TurntableEX I2C:x60 Configured on Vpins:600-600  *>          <<== This is the important line, Turntable-EX is connected!

If there is an "OFFLINE" at the end of the Turntable-EX line, it indicates something is not quite right, so start by checking these things first:

* Is Turntable-EX powered on?
* Is Turntable-EX connected correctly to the CommandStation I2C interface? (see :ref:`turntable-ex/get-started:9. connect turntable-ex to your commandstation`)
* Was Turntable-EX turned on before the CommandStation?
* Does the I2C address defined in "myHal.cpp" match the I2C address defined in Turntable-EX's "config.h" file?

At the initial power on, note that the turntable should have moved itself to the home position, so all commands below assume this is the case.

This command should rotate the turntable 100 steps only:

.. code-block:: 

  <D TT 600 100 0>

This command should rotate the turntable a further 500 steps (the difference between the existing 100 steps and target 600 steps) only:

.. code-block:: 

  <D TT 600 600 0>

This next command should rotate the turntable in the reverse direction by 300 steps:

.. code-block:: 

  <D TT 600 300 0>

This command should rotate the turntable again in the reverse direction, however should also activate both phase switching relays:

.. code-block:: 
  
  <D TT 600 2000 1>

This command should rotate the the turntable further in the reverse direction, and deactivate the phase switching relays:

.. code-block::

  <D TT 600 1500 0>

Finally, this command will cause the turntable to once again find its home position:

.. code-block:: 
  
  <D TT 600 0 2>

<TO DO: Add a video demonstrating these tests>

Providing these tests have completed successfully, you are now ready to tune the turntable positions for your layout in preparation for defining the EX-RAIL configuration and putting Turntable-EX to good use.

Tuning your turntable positions
===============================

To tune your turntable positions, there are two aspects to consider.

First will be the number of steps from the home position the turntable needs to rotate in order to reach the desired position. By default, the turntable will turn in a clockwise direction (as demonstrated by the homing activity).

Second will be the phase or polarity required for the bridge track to match the connecting layout tracks, as described in the :ref:`turntable-ex/turntable-ex:important! phase (or polarity) switching` section.

Determine the positions
_______________________

At this point, you should either have a layout you're fitting Turntable-EX into, or a layout design that you're working to, with the various turntable connection tracks defined.

The simplest way to devise the approximate number of steps for each turntable position is to calculate these based on the degrees each step will turn.

For the default 28BYJ-48 stepper motor with its 2048 steps in a single 360 degree rotation, this gives each step ~0.18 degrees of movement (360/2048 = 0.1758).

Therefore, to determine the number of steps required to turn a certain degrees, use the formula "steps = degrees/degrees per step". To turn 10 degrees requires ~56 steps (10 / 0.18 = 55.5556).

For this example, for simplicity, we will devise the steps required for a six position turntable, with position 1 being 10 degrees from the home position, position 2 a further 10 degrees, position 3 a further 10 degrees again, and positions 4 through 6 being 180 degrees from the first three positions.

<Insert diagram here>

Therefore, using our formula, the starting point for each position will be:

.. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * - Position
      - Degrees from home
      - Steps
    * - 1
      - 10
      - 56
    * - 2
      - 20
      - 111
    * - 3
      - 30
      - 167
    * - 4
      - 190
      - 1056
    * - 5
      - 200
      - 1111
    * - 6
      - 210
      - 1167

<Insert diagram here>

Determine phase switching
_________________________

Assuming your layout tracks are wired correctly as per :ref:`turntable-ex/turntable-ex:important! phase (or polarity) switching`, each of the positions determined above will need to have the phase set correctly.

In the provided example, positions 1, 2, and 3 would match the surrounding track polarity, with positions 4 through 6 requiring the phase/polarity to be switched.

<Insert diagram here>

Example tuning commands
_______________________

To validate the above calculated positions, the following six diagnostic commands should be executed in the serial terminal of the CommandStation, which will allow you to visually inspect the alignment with your layout tracks and adjust accordingly:

.. code-block:: 

  <D TT 600 56 0>
  <D TT 600 111 0>
  <D TT 600 167 0>
  <D TT 600 1056 1>
  <D TT 600 1111 1>
  <D TT 600 1167 1>

If you find any of these positions are slightly out of alignment, simply adjust the step count as appropriate to compensate.

Apply to your layout
____________________

At this point, you should be able to apply the above calculations to your own layout and come up with the step count and phase/polarity settings required for each position.

Use appropriate diagnostic commands to test and tune each position for that perfect alignment, and providing your layout is functional, you should be able to drive a locomotive on and off your turntable in each position.

Advertising positions to Engine Driver and WiThrottle applications
==================================================================

Now that you have defined all of your turntable positions with appropriate phase/polarity switching, it's time to get these advertised to Engine Driver and WiThrottle applications.

The method to advertise these is to use EX-RAIL's ROUTE function with the MOVETT command, which will ensure all of your defined turntable positions appear in the Engine Driver and WiThrottle Routes sections.

If this is your first experience with EX-RAIL and the "myAutomation.h" file, familiarise yourself with EX-RAIL by reading through :ref:`automation/ex-rail-intro:introduction to ex-rail automation`.

Pay particular attention to the various mentions of ROUTE and the associated examples.

There are two highly recommended additions to using just these ROUTEs:
1. Utilise EX-RAIL's virtual RESERVE() and FREE() functions to ensure that while you are operating your turntable, nothing else can interfere with it. This is not so important during manual operation, however if you want to add any other automation (say, turning a warning light on), you will need these to ensure the relevant automation activities are not interrupted should you choose another turntable position prior to the first move completing.
2. Utilise aliases to make things human friendly, and we have also provided 30 pre-defined aliases for the ROUTE IDs to ensure there will be no conflicts, as all IDs must be unique.

To define the required turntable positions in the example six position turntable from above, you will need to have this content added to your "myAutomation.h" file. Note that we recommend adding an additional ROUTE to activate the homing process:

<TO DO HERE: Set up a sample myTurntable-EX.h to refer to, and identify 30 unique IDs with aliases to include>

.. code-block:: cpp

  // For Conductor level users who wish to just use Turntable-EX, you don't need to understand this
  // and can move to defining the turntable positions below. You must, however, ensure this remains
  // before any position definitions or you will get compile errors when uploading.
  //
  // Definition of the TURNTABLE_EX macro to correctly create the ROUTEs required for each position.
  // This includes RESERVE()/FREE() to protect any automation activities.
  //
  #define TURNTABLE_EX(route_id, reserve_id, vpin, steps, activity, desc) \
    ROUTE(route_id, desc) \
      RESERVE(reserve_id) \
      MOVETT(vpin, steps, activit) \
      WAITFOR(vpin) \
      FREE(reserve_id) \
      DONE
  
  // Define your turntable positions here:
  //
  // TURNTABLE_EX(route_id, reserve_id, vpin, steps, activity, desc)
  //
  // route_id = A unique number for each defined route, the route is what appears in throttles
  // reserve_id = A unique reservation number (0 - 255) to ensure nothing interferes with automation
  // vpin = The Vpin defined for the Turntable-EX device driver, default is 600
  // steps = The target step position
  // activity = The activity performed for this ROUTE (Note do not enclose in quotes "")
  // desc = Description that will appear in throttles (Must use quotes "")
  //
  TURNTABLE_EX(TTRoute1, Turntable, 600, 56, Turn, "Position 1")
  TURNTABLE_EX(TTRoute2, Turntable, 600, 111, Turn, "Position 2")
  TURNTABLE_EX(TTRoute3, Turntable, 600, 167, Turn, "Position 3")
  TURNTABLE_EX(TTRoute4, Turntable, 600, 1056, Turn_PInvert, "Position 4")
  TURNTABLE_EX(TTRoute5, Turntable, 600, 1111, Turn_PInvert, "Position 5")
  TURNTABLE_EX(TTRoute6, Turntable, 600, 1167, Turn_PInvert, "Position 6")
  TURNTABLE_EX(TTRoute7, Turntable, 600, 0, Home, "Home turntable")
  
  // Pre-defined aliases to ensure unique IDs are used.
  ALIAS(Turntable, 255)
  ALIAS(TTRoute1, 5179)
  ALIAS(TTRoute2, 5180)
  ALIAS(TTRoute3, 5181)
  ALIAS(TTRoute4, 5182)
  ALIAS(TTRoute5, 5183)
  ALIAS(TTRoute6, 5184)
  ALIAS(TTRoute7, 5185)

That's it! Once you have created "myAutomation.h" and uploaded it to your CommandStation as per the process on the :ref:`automation/ex-rail-intro:introduction to ex-rail automation` page, the routes for each turntable position should automatically be visible in Engine Driver and WiThrottle applications.

There is one "catch" with the above "myAutomation.h" example. When your CommandStation starts up and EX-RAIL starts, it will automatically execute everything in "myAutomation.h" up until the first "DONE" statement it encounters.

In this scenario, that means on startup, the turntable will automatically move to position 1.

If you wish to leave the turntable at the home position on startup, you can simply add "DONE" on its own line at the beginning of the file prior to the first ROUTE:

.. code-block:: cpp

  // Prevent the turntable moving from home on startup
  DONE

  #define TURNTABLE_EX(route_id, reserve_id, vpin, steps, activity, desc) \
    ...

In a similar manner, if you prefer the turntable starts at some other position, you can accomplish this by simply calling the MOVETT() command at the beginning of the file and specifiying the correct steps and activity to perform:

.. code-block:: cpp

  // This will move the turntable to position 3 on startup:
  MOVETT(600, 167, Turn)
  DONE
