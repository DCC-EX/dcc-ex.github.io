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

*For the purposes of this exercise, we will assume you've acquired everything you need from the :doc:`/ex-turntable/purchasing` page, and have completed all steps up to and including :ref:`ex-turntable/assembly:7. load the ex-turntable software` on the :doc:`/ex-turntable/assembly` page.*

At this point, based on the assumption above, your |EX-TT| should be configured ready to add to your |EX-CS|.

.. collapse:: Expand to see the |EX-TT| config.h, noting we have removed all comments for brevity:

  .. code-block:: cpp

    /*
    *  © 2022 Peter Cole
    *
    *  This is the configuration file for Turntable-EX.
    */

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

Now that the basics of |EX-TT| have been completed and it is ready to be added to your |EX-CS|, we need to get it connected ready for action.

Firstly, your |EX-CS| needs to be prepared by ensuring the |EX-TT| device driver is loaded. This is covered in :ref:`ex-turntable/assembly:8. add the ex-turntable device driver to ex-commandstation`.

Next, you need to connect |EX-TT| to your |EX-CS| which requires a connection to the I2C interface, and it's a good idea to make sure |EX-TT| is turned on before |EX-CS| to ensure it's detected successfully at startup. This is covered in :ref:`ex-turntable/assembly:9. connect ex-turntable to your ex-commandstation`.

.. collapse:: Expand to see the |EX-CS| myHal.cpp:

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

Once you have prepared your |EX-CS| and connected |EX-TT|, turn them on and feel free to validate it is connected and working as per :ref:`ex-turntable/test-and-tune:testing ex-turntable`.

Once you reach this point, you can move on to adding the traverser or, if you wish to skip that, move on to tuning the positions.

Adding the traverser
--------------------

*For the purposes of this exercise, we will assume you've acquired everything you need from the :doc:`/ex-turntable/purchasing` page with consideration of the changes for traverser mode as outlined in :ref:`ex-turntable/traverser:what you need for traverser mode`, and have completed all steps up to and including :ref:`ex-turntable/assembly:6. connect power and test` on the :doc:`/ex-turntable/assembly` page, as well as taking into account the changes required as outlined on the :doc:`/ex-turntable/traverser` page.*

.. tip:: 

  It is highly recommended to make use of the :ref:`ex-turntable/traverser:sensor testing mode` to validate both the home and limit sensors are working correctly when in traverser mode.

Firstly, you will note in the paragraph above that we stopped one step earlier in the |EX-TT| assembly process at step 6, and that's because we need to ensure our traverser is available at a different I2C address and on a different Vpin to our turntable to ensure they are controlled independently of each other.

To achieve this, we will be using the I2C address `0x61` and will be assigning the Vpin `601`.

So, in order to complete :ref:`ex-turntable/assembly:7. load the ex-turntable software`, the value for `I2C_ADDRESS` in the "config.h" file needs to be changed to `0x61`, and of course the `TURNTABLE_EX_MODE` needs to be set to `TRAVERSER`.

As we are continuing to use the default ULN2003/28BYJ-48 stepper driver and motor combo for our traverser, nothing else needs to change.

Once you have noted these changes, you can proceed with :ref:`ex-turntable/assembly:7. load the ex-turntable software`, using the updated values in the "config.h" file.

.. collapse:: Expand to see the |EX-TT| config.h, noting we have removed all comments for brevity:

  .. code-block:: cpp

    /*
    *  © 2022 Peter Cole
    *
    *  This is the configuration file for Turntable-EX.
    */

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

Once again, as per the turntable above, we need to add the traverser device to our |EX-CS|, and this is where we need to specify both the updated I2C address of `0x61` and the updated Vpin of `601` to ensure we are adding this as a second device that does not conflict with the turntable.

As per our turntable section above, these changes need to be incorporated into the process outlined in :ref:`ex-turntable/assembly:8. add the ex-turntable device driver to ex-commandstation` in order to add the traverser device driver to your |EX-CS|.

.. collapse:: Expand to see the |EX-CS| myHal.cpp:

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

At this point, we're ready to connect the |EX-TT| in traverser to our |EX-CS| as outlined in :ref:`ex-turntable/assembly:9. connect ex-turntable to your ex-commandstation`, and then validate it's working as per :ref:`ex-turntable/test-and-tune:testing ex-turntable`.

Once that's done, we need to tune both our turntable and traverser positions.

Tune your EX-Turntable positions
================================

Tuning the turntable and traverser positions is going to be part mathematics, and part experimentation.

Using mathematics to calculate turntable positions is fairly straight forward as we are working with a full 360 degree circle, and the resulting experimentation will only be required for fine tuning.

For the traverser, however, the step positions are going to be entirely experimental as there is likely a lead screw in use which introduces a gear ratio that needs to be factored in.

For the purposes of this exercise, however, we will keep it simple and simply assume that there are no gear ratios in place, and will continue to work with a single 360 degree rotation of the stepper motor.

.. note:: 

  We will be using the same steps per revolution number throughout this page (4097) for both turntable and traverser, and will keep this consistent with the examples in the |EX-TT| documentation for simplicity.

Obtain the steps per revolution
-------------------------------

Before attempting any tuning, the first thing we need to obtain is the steps per revolution for both our turntable and traverser.

Ideally these should have been noted in :ref:`ex-turntable/assembly:7. load the ex-turntable software`, however this value can also be obtained by monitoring the serial console on startup where the steps per revolution are reported along with the other configuration details.

.. collapse:: Expand to see an example startup screen of |EX-TT|

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

Tuning the turntable
--------------------

:ref:`ex-turntable/test-and-tune:tuning your turntable positions`

Tuning the traverser
--------------------

For our traverser positions, we will simply start with the fact we will have six evenly spaced tracks on the traverser.

With our assumption of a full rotation moving the traverser from the first to last track, this would give us x steps between positions (360 degrees / 6 positions).

Control and automate your EX-Turntable
======================================
