.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-TT-LOGO|

*****************************
Testing, Tuning, and Control
*****************************

|tinkerer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

Ex-Turntable commands
=====================

Before proceeding with testing or any configuration, it's important to understand the two commands available for controlling |EX-TT|.

This is a debug or diagnostic command that can be executed via the serial terminal of the CommandStation:

.. code-block:: 

  <D TT vpin steps activity>

This is the EX-RAIL command to be included in myAutomation.h:

.. code-block:: cpp

  MOVETT(vpin, steps, activity)

For both of these commands, "vpin" is as defined in your "myHal.cpp" file, and "steps" is the number of steps from the home position, not the number of steps the turntable has to travel.

For the diagnostic command, "activity" needs to be defined as a number, whereas for the EX-RAIL command, this is defined as text based on the table below. Sound confusing? The reason for using text in the EX-RAIL command is to make your automation sequences more "human-friendly" when reading what they do later. It's much easier for us humans to remember words rather than numbers.

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
      - Turn to the desired step position and invert the phase/polarity (required for manual phase switching only)
    * - 2
      - Home
      - Activate the homing process, ignores the provided step position
    * - 3
      - Calibrate
      - Activate the automatic calibration process, ignores the provided step position
    * - 4
      - LED_On
      - Turns the LED on, ignores the provided step position
    * - 5
      - LED_Slow
      - Sets the LED to a slow blink, ignores the provided step position
    * - 6
      - LED_Fast
      - Sets the LED to a fast blink, ignores the provided step position
    * - 7
      - LED_Off
      - Turns the LED off, ignores the provided step position
    * - 8
      - Acc_On
      - Turns the accessory output on, ignores the provided step position
    * - 9
      - Acc_Off
      - Turns the accessory output off, ignores the provided step position

Here's a quick example to demonstrate the difference between the diagnostic and EX-RAIL commands, with both commands below rotating to step position 100:

.. code-block:: 

  <D TT 600 100 0>
  MOVETT(600, 100, Turn)

Testing EX-Turntable
====================

Firstly, power on |EX-TT|, followed by your CommandStation. By powering these on in that order, you will ensure that |EX-TT| is available prior to the CommandStation trying to load the device driver, otherwise it will consider the device as "OFFLINE", and commands will fail.

Referring again to :ref:`reference/developers/hal-config:adding a new device`, skip ahead to :ref:`reference/developers/hal-config:checking the driver`, and the output you're looking for to validate the |EX-TT| device driver is loaded and connected successfully is below:

.. code-block:: 

  <D HAL SHOW><* Arduino Vpins:2-69 *>
  <* PCA9685 I2C:x40 Configured on Vpins:100-115  *>
  <* PCA9685 I2C:x41 Configured on Vpins:116-131 OFFLINE *>
  <* MCP23017 I2C:x20 Configured on Vpins:164-179 OFFLINE *>
  <* MCP23017 I2C:x21 Configured on Vpins:180-195 OFFLINE *>
  <* TurntableEX I2C:x60 Configured on Vpins:600-600  *>          <<== This is the important line, |EX-TT| is connected!

If there is an "OFFLINE" at the end of the |EX-TT| line, it indicates something is not quite right. Refer to :ref:`ex-turntable/troubleshooting:ex-turntable showing as offline with \<d hal show\>`.

At power on, note that the turntable should have moved itself to the home position, so all commands below assume this is the case.

.. note:: 

  For all testing and tuning below, it is assumed that the default option for automatic phase switching is enabled, and that the default ULN2003/28BYJ-48 stepper driver and motor combination is in use in half step mode, which is ~4096 steps per revolution.

  For automatic phase switching, this should translate to ~512 steps for the 45 degree phase switch trigger point, and ~2560 steps for the 225 degree revert trigger point.

This command should rotate the turntable 100 steps only:

.. code-block:: 

  <D TT 600 100 0>

This command should rotate the turntable a further 500 steps and active the phase inversion relays:

 - 500 is the difference between the existing 100 steps and target 600 steps
 - 600 steps is greater than the ~512 step/45 degree trigger position for phase inversion

.. code-block:: 

  <D TT 600 600 0>

This next command should rotate the turntable in the reverse direction by 300 steps and deactivate the phase inversion relays:

- 300 is the difference between the existing 600 steps and target 300 steps, with the reverse direction being the shortest path there
- 300 steps is less than the ~512 step/45 degree trigger position for phase inversion

.. code-block:: 

  <D TT 600 300 0>

This command should rotate the turntable again in the reverse direction, and should also activate the phase inversion relays:

- 2000 steps is greater than the ~512 step/45 degree trigger position for phase inversion
- It is also less than the ~2560 step/225 degree trigger position to revert the inversion

.. code-block:: 
  
  <D TT 600 2000 1>

Finally, this command will cause the turntable to once again find its home position:

.. code-block:: 
  
  <D TT 600 0 2>

<TO DO: Add a video demonstrating these tests>

Providing these tests have completed successfully, you are now ready to tune the turntable positions for your layout in preparation for defining the EX-RAIL configuration and putting |EX-TT| to good use.

Tuning your turntable positions
================================

.. tip:: 

  To determine your starting positions, you will need the full turn step count as recorded in :ref:`ex-turntable/assembly:automatic calibration`.

To tune your turntable positions, you will need to calculate the number of steps from the home position the turntable needs to rotate in order to reach the desired position. By default, the turntable will turn in a clockwise direction (as demonstrated by the homing activity).

Determine the positions
________________________

At this point, you should either have a layout you're fitting |EX-TT| into, or a layout design that you're working to, with the various turntable connection tracks defined.

The simplest way to devise the approximate number of steps for each turntable position is to calculate these based on the degrees each step will turn.

For the default |EX-TT| configuration with the ULN2003/28BYJ-48 stepper driver/motor combo in half step mode, this should give a step count close to 4096 for a single 360 degree rotation, which means each step is ~0.088 degrees of movement (360/4096 = 0.088).

Therefore, to determine the number of steps required to turn a certain number of degrees, use the formula "steps = degrees/degrees per step". To turn 10 degrees requires ~114 steps (10 / 0.088 = 113.64).

In this example, for simplicity, we will devise the steps required for a six position turntable, with position 1 being 10 degrees from the home position, position 2 a further 10 degrees, position 3 a further 10 degrees again, and positions 4 through 6 being 180 degrees from the first three positions.

.. image:: /_static/images/turntable-ex/six-pos-example-degrees.png
  :alt: Six Postion Example
  :scale: 70%

Therefore, using our formula, the starting point for each position will be:

.. list-table::
    :widths: auto
    :header-rows: 1
    :class: command-table

    * - Position
      - Degrees from home
      - Steps from home
    * - 1
      - 10
      - 114
    * - 2
      - 20
      - 227
    * - 3
      - 30
      - 341
    * - 4
      - 190
      - 2159
    * - 5
      - 200
      - 2273
    * - 6
      - 210
      - 2386

Example tuning commands
________________________

To validate the above calculated positions, the following six diagnostic commands should be executed in the serial terminal of the CommandStation, which will allow you to visually inspect the alignment with your layout tracks and adjust accordingly:

.. code-block:: 

  <D TT 600 114 0>
  <D TT 600 227 0>
  <D TT 600 341 0>
  <D TT 600 2159 0>
  <D TT 600 2273 0>
  <D TT 600 2386 0>

If you find any of these positions are slightly out of alignment, simply adjust the step count as appropriate to compensate.

Note that due to the automatic phase inversion, the last three positions will automatically active the phase inversion relays due to being within the 45 to 225 degree angles that activates phase inversion.

Apply to your layout
_____________________

At this point, you should be able to apply the above calculations to your own layout and come up with the step count required for each position.

Use appropriate diagnostic commands to test and tune each position for that perfect alignment, and providing your layout is functional, you should be able to drive a locomotive on and off your turntable in each position.

Advertising positions to Engine Driver and WiThrottle applications
===================================================================

Now that you have defined all of your turntable positions with appropriate phase/polarity switching, it's time to get these advertised to Engine Driver and WiThrottle applications.

The method to advertise these is to use EX-RAIL's ROUTE function with the MOVETT command, which will ensure all of your defined turntable positions appear in the Engine Driver and WiThrottle Routes sections.

If this is your first experience with EX-RAIL and the "myAutomation.h" file, familiarise yourself with EX-RAIL by reading through :doc:`/ex-rail/index`.

Pay particular attention to the various mentions of ROUTE and the associated examples.

There are two highly recommended additions to using just these ROUTEs:

1. Utilise EX-RAIL's virtual RESERVE() and FREE() functions to ensure that while you are operating your turntable, nothing else can interfere with it. This is not so important during manual operation, however if you want to add any other automation (say, turning a warning light on), you will need these to ensure the relevant automation activities are not interrupted should you choose another turntable position prior to the first move completing.
2. Utilise aliases to make things human friendly, and we have also provided 30 pre-defined aliases for the ROUTE IDs to ensure there will be no conflicts, as all IDs must be unique.

To define the required turntable positions in the example six position turntable from above, you will need to have this content added to your "myAutomation.h" file. Note that we recommend adding an additional ROUTE to activate the homing process.

.. tip:: 

  .. image:: /_static/images/conductor.png
    :alt: Conductor Level
    :scale: 40%
    :align: left
  
  To make this as simple as possible, we have included "myTurntable-EX.example.h" with the CommandStation-EX software containing an example automation macro with some pre-defined positions based on the example above as a starting point. Feel free to either copy or rename this to "myAutomation.h" and use it.

That's it! Once you have created "myAutomation.h" and uploaded it to your CommandStation as per the process on the :doc:`/ex-rail/index` page, the routes for each turntable position should automatically be visible in Engine Driver and WiThrottle applications.

My turntable moves on startup!
_______________________________

There is one "catch" with the above "myAutomation.h" example. When your CommandStation starts up and EX-RAIL starts, it will automatically execute everything in "myAutomation.h" up until the first "DONE" statement it encounters.

In this scenario, that means on startup, the turntable will automatically move to position 1.

If you wish to leave the turntable at the home position on startup, you can simply comment out the first MOVETT() command:

.. code-block:: cpp

  MOVETT(600, 114, Turn)        <<== This line here    
  // MOVETT(600, 114 Turn)      <<== Becomes this, add // to comment lines out

In a similar manner, if you prefer the turntable starts at some other position, you can accomplish this by simply changing the steps in that same MOVETT() command:

.. code-block:: cpp

  MOVETT(600, 167, Turn)            // Default moves to position one, edit this line to look like the below
  MOVETT(600, 2386, Turn)           // Move instead to position six

Manual phase switching
=======================

So far, all the examples, testing, and tuning have relied on automatic phase switching.

There may be times where manual phase switching is required, whether due to awkward track wiring, layouts that have tracks at angles that make it hard to determine the correct angles at which to automatically switch the phase, or (in an upcoming release) when traversers are used rather than traditional turntables, that don't actually required phase switching at all.

To enable manual phase switching, you must edit "config.h" and set :ref:`ex-turntable/configure:phase_switching` to "MANUAL".

Once this has been done, you must explicitly define the phase switching to occur as a part of the diagnostic or EX-RAIL command for every step position that requires an inverted phase.

.. note:: 

  The phase switch command (1 for the diagnostic command, Turn_PInvert for EX-RAIL) does not continue to invert the phase each time that command is sent, the command simply tells |EX-TT| whether or not to activate the phase inversion relays.

  Therefore, for every position that requires the phase to be inverted, you must send the invert command (1/Turn_PInvert). For every position that requires the phase to be maintained, you must send just the turn command (0/Turn).

To use our example from above, the commands in :ref:`ex-turntable/test-and-tune:example tuning commands` would need to be modified to replicate the automatic phase switching as such:

.. code-block:: 

  <D TT 600 114 0>
  <D TT 600 227 0>
  <D TT 600 341 0>
  <D TT 600 2159 1>
  <D TT 600 2273 1>
  <D TT 600 2386 1>

The EX-RAIL equivalent to the above would be:

.. code-block:: cpp

  MOVETT(600, 114, Turn)
  MOVETT(600, 227, Turn)
  MOVETT(600, 341, Turn)
  MOVETT(600, 2159, Turn_PInvert)
  MOVETT(600, 2273, Turn_PInvert)
  MOVETT(600, 2386, Turn_PInvert)

.. danger:: 

  If you do not explicitly send the activity command to invert the phase, and the turntable orientation results with the phase out of alignment with the surrounding tracks, this will result in a short circuit when a locomotive attempts to enter or exit the turntable bridge track.
