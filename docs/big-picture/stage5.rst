.. include:: /include/include.rst
.. include:: /include/include-l1.rst
*********************************
Stage 5 - Turntables & Traversers
*********************************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :local:
    :depth: 1

A turntable can add significant interest to a layout, especially when involved in operations sessions, and when depicting realistic engine yards.

In addition, turntables can be a real space saver compared to reversing loops, and traversers can also be significant space savers for staging tracks, allowing multiple trains to be staged ready for action without taking up spurs or sidings on the main layout when not in use.

When it comes to RMFT, we are adding a turntable that has seven defined positions, six of which are for entering roundhouse stalls, and the seventh is the track connecting to the rest of the layout via the switching/shunting yard.

In addition, we are also adding a horizontal staging traverser that will allow for six complete trains to be staged off the layout ready for action.

.. tip:: 

  In preparation for adding an |EX-TT| to your layout, you'll need to understand the concepts outlined on the :doc:`/ex-turntable/overview` page, paying particular attention to the section on polarity or phase switching (:ref:`ex-turntable/overview:important! phase (or polarity) switching`), as we will be using automatic phase switching for the turntable.

  Further to this, you'll also need to understand the differences required for traverser mode as outlined on the :doc:`/ex-turntable/traverser` page. We will not require phase switching for the traverser, as any locos on the traverser will not be rotating 180 degrees.

  If you won't be using a traverser on your layout or want to tackle this separately, you can skip the traverser info on this page as it is essentially an extension of the turntable info.

  Having both a turntable and traverser will require two separate instances of |EX-TT|, meaning two Arduinos, two stepper drivers/motors, and so forth.

What to expect to learn from stage 5
====================================

At the end of this stage, we expect you will have learnt the following:

* How to add an |EX-TT| to your |EX-CS| in both turntable and traverser modes
* How to tune your |EX-TT| positions
* How to control and automate your |EX-TT|

Add an EX-Turntable to your EX-CommandStation
=============================================

To add our turntable and traverser to the |EX-CS|, we need to ensure |EX-TT| is configured correctly for both items, and then add the device drivers with the correct configuration to our |EX-CS|.

Adding the turntable
--------------------

*For the purposes of this exercise, we will assume:*

* Everything needed from the :doc:`/ex-turntable/purchasing` page is available
* All steps up to and including :ref:`ex-turntable/assembly:7. load the ex-turntable software` on the :doc:`/ex-turntable/assembly` page have been completed

At this point, based on the assumptions above, our |EX-TT| should be configured ready to add to our |EX-CS|.

Expand "config.h" to see the |EX-TT| configuration file for the turntable, noting we have removed all comments for brevity.

.. collapse:: "config.h" for the turntable

  .. code-block:: cpp

    #define I2C_ADDRESS 0x60
    #define TURNTABLE_EX_MODE TURNTABLE
    #define HOME_SENSOR_ACTIVE_STATE LOW
    #define LIMIT_SENSOR_ACTIVE_STATE LOW
    #define RELAY_ACTIVE_STATE HIGH
    #define PHASE_SWITCHING AUTO
    #define PHASE_SWITCH_ANGLE 45
    #define STEPPER_DRIVER ULN2003_HALF_CW
    #define DISABLE_OUTPUTS_IDLE
    #define STEPPER_MAX_SPEED 200     // Maximum possible speed the stepper will reach
    #define STEPPER_ACCELERATION 25   // Acceleration and deceleration rate
    #define LED_FAST 100
    #define LED_SLOW 500

|

Now that the basics of |EX-TT| have been completed and it is ready to be added to our |EX-CS|, we need to get it connected ready for action.

Firstly, our |EX-CS| needs to be prepared by ensuring the |EX-TT| device driver is loaded. This is covered in :ref:`ex-turntable/assembly:8. add the ex-turntable device driver to ex-commandstation`.

Next, we need to connect |EX-TT| to our |EX-CS| which requires a connection to the I2C interface, and it's a good idea to make sure |EX-TT| is turned on before |EX-CS| to ensure it's detected successfully at startup. This is covered in :ref:`ex-turntable/assembly:9. connect ex-turntable to your ex-commandstation`.

Expand "myHal.cpp" to see the |EX-CS| HAL configuration file required to add the turntable.

.. collapse:: "myHal.cpp" for the turntable

  .. code-block:: cpp

    #if !defined(IO_NO_HAL)

    // Include devices you need.
    #include "IODevice.h"
    #include "IO_TurntableEX.h"

    //==========================================================================
    // The function halSetup() is invoked from CS if it exists within the build.
    // The setup calls are included between the open and close braces "{ ... }".
    // Comments (lines preceded by "//") are optional.
    //==========================================================================

    void halSetup() {
      TurntableEX::create(600, 1, 0x60);
    }

    #endif

|

Once we have prepared our |EX-CS| and connected |EX-TT|, they then need to be turned on with the connection validated as per :ref:`ex-turntable/test-and-tune:testing ex-turntable`.

Now, we are ready to move on to adding the traverser, then tuning the positions for both.

Adding the traverser
--------------------

*For the purposes of this exercise, we will assume:*

* Everything needed from the :doc:`/ex-turntable/purchasing` page including the considerations as outlined in :ref:`ex-turntable/traverser:what you need for traverser mode` is available
* All steps up to and including :ref:`ex-turntable/assembly:6. connect power and test` on the :doc:`/ex-turntable/assembly` page have been completed
* All changes required as outlined on the :doc:`/ex-turntable/traverser` page have been taken into account

.. tip:: 

  It is highly recommended to make use of the :ref:`ex-turntable/traverser:sensor testing mode` to validate both the home and limit sensors are working correctly when in traverser mode.

Firstly, you will note in the list of assumptions above that we stopped one step earlier in the |EX-TT| assembly process at step 6, and that's because we need to ensure our traverser is available at a different I2C address and on a different Vpin to our turntable to ensure they are controlled independently of each other.

To achieve this, we will be using the I2C address ``0x61`` and will be assigning the Vpin ``601``.

So, in order to complete :ref:`ex-turntable/assembly:7. load the ex-turntable software`, the value for ``I2C_ADDRESS`` in the "config.h" file needs to be changed to ``0x61``, and of course the ``TURNTABLE_EX_MODE`` needs to be set to ``TRAVERSER``.

As we are continuing to use the default ULN2003/28BYJ-48 stepper driver and motor combo for our traverser, nothing else needs to change.

Once we have noted these changes, we can proceed with :ref:`ex-turntable/assembly:7. load the ex-turntable software`, using the updated values in the "config.h" file.

Expand "config.h" to see the |EX-TT| configuration file for the traverser, noting we have removed all comments for brevity.

.. collapse:: "config.h" for the traverser

  .. code-block:: cpp

    #define I2C_ADDRESS 0x61
    #define TURNTABLE_EX_MODE TRAVERSER
    #define HOME_SENSOR_ACTIVE_STATE LOW
    #define LIMIT_SENSOR_ACTIVE_STATE LOW
    #define RELAY_ACTIVE_STATE HIGH
    #define PHASE_SWITCHING MANUAL
    #define STEPPER_DRIVER ULN2003_HALF_CW
    #define DISABLE_OUTPUTS_IDLE
    #define STEPPER_MAX_SPEED 200     // Maximum possible speed the stepper will reach
    #define STEPPER_ACCELERATION 25   // Acceleration and deceleration rate
    #define LED_FAST 100
    #define LED_SLOW 500

|

Once again, as we did with the turntable, we need to add the traverser device to our |EX-CS|, and this is where we need to specify both the updated I2C address of ``0x61`` and the updated Vpin of ``601`` to ensure we are adding this as a second device that does not conflict with the turntable.

As per the turntable section, these changes need to be incorporated into the process outlined in :ref:`ex-turntable/assembly:8. add the ex-turntable device driver to ex-commandstation` in order to add the traverser device driver to our |EX-CS|.

Expand "myHal.cpp" to see the |EX-CS| HAL configuration file required to add both the turntable and traverser.

.. collapse:: "myHal.cpp" for the turntable and traverser

  .. code-block:: cpp

    #if !defined(IO_NO_HAL)

    // Include devices you need.
    #include "IODevice.h"
    #include "IO_TurntableEX.h"

    //==========================================================================
    // The function halSetup() is invoked from CS if it exists within the build.
    // The setup calls are included between the open and close braces "{ ... }".
    // Comments (lines preceded by "//") are optional.
    //==========================================================================

    void halSetup() {
      TurntableEX::create(600, 1, 0x60);  // This is our turntable device
      TurntableEX::create(601, 1, 0x61);  // This is our traverser device
    }

    #endif

|

Once we have prepared our |EX-CS| and connected |EX-TT|, they then need to be turned on with the connection validated as per :ref:`ex-turntable/test-and-tune:testing ex-turntable`.

Now, we are ready to move on to tuning the positions.

Tune your turntable and traverser positions
===========================================

We'll use some basic mathematics to tune our turntable and traverser positions, however in a real layout, some experimentation will be required for fine tuning to ensure proper track alignment.

.. note:: 

  When tuning positions, you can use the ``<D TT vpin steps activity>`` diagnostic command as outlined in :ref:`ex-turntable/test-and-tune:tuning your turntable positions` to test and refine these for perfect track alignment between the turntable bridge track and the surrounding tracks.

  We will be using the same steps per revolution number throughout this page (4097) for both the turntable and traverser, and are keeping this consistent with the examples in the |EX-TT| documentation for simplicity.

Obtain the steps per revolution
-------------------------------

Before attempting any tuning, the first thing we need to obtain is the steps per revolution for both our turntable and traverser.

Ideally these should have been noted in :ref:`ex-turntable/assembly:7. load the ex-turntable software`, however this value can also be obtained by monitoring the |EX-TT| serial console on startup where the steps per revolution are reported along with the other configuration details.

.. collapse:: Expand to see an example startup screen

  .. code-block:: 

    License GPLv3 fsf.org (c) dcc-ex.com
    Turntable-EX version 0.4.0-Beta
    Available at I2C address 0x60
    Turntable-EX in TURNTABLE mode
    Turntable-EX has been calibrated for 4097 steps per revolution
    Automatic phase switching enabled at 45 degrees
    Phase will switch at 512 steps from home, and revert at 2560 steps from home
    Homing...
    Homing started
    Turntable homed successfully

|

Once we have our steps per revolution, we can use that number with our formulas to calculate the steps required to move to each desired position.

Tuning the turntable
--------------------

.. todo:: MEDIUM - add diagram outlining angles/steps for turntable position calculations and phase switching

.. tip:: 

  It's a great idea at this point to understand the importance of DCC phase/polarity and how switching/reversing it works with |EX-TT|. Refer to :ref:`ex-turntable/overview:important! phase (or polarity) switching` and :ref:`ex-turntable/overview:how does this work with ex-turntable?` for details.

There are two aspects to tuning our turntable positions; one being the step counts of each track position around the turntable to ensure correct track alignment, and the other being when to swap our DCC phase/polarity to ensure locos can enter and exit the turntable without causing short circuits.

We will refer to our turntable positions from number 1 through to 7 moving in a clockwise direction from our home position, with 1 through 6 being roundhouse stalls 1 through 6, and 7 being our track connecting to the switching/shunting yard.

The home position has been set just before position 1.

:ref:`ex-turntable/test-and-tune:tuning your turntable positions`

Tuning the traverser
--------------------

.. todo:: LOW - add diagram outlining steps for traverser position calculations

For our traverser positions, we will simply start with the fact we will have six evenly spaced tracks on the traverser.

With our assumption of a full rotation moving the traverser from the first to last track, this would give us x steps between positions (360 degrees / 6 positions).

Control and automate your EX-Turntable
======================================
