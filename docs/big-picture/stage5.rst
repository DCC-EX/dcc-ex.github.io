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

Adding the turntable
--------------------

*For the purposes of this exercise, we will assume you've acquired everything you need from the :doc:`/ex-turntable/purchasing` page, and have completed all steps up to and including :ref:`ex-turntable/assembly:7. load the ex-turntable software` on the :doc:`/ex-turntable/assembly` page.*

Now that the basics of |EX-TT| have been completed and it is ready to be added to your |EX-CS|, we need to get it connected ready for action.

Firstly, your |EX-CS| needs to be prepared by ensuring the |EX-TT| device driver is loaded. This is covered in :ref:`ex-turntable/assembly:8. add the ex-turntable device driver to ex-commandstation`.

Next, you need to connect |EX-TT| to your |EX-CS| which requires a connection to the I2C interface, and it's a good idea to make sure |EX-TT| is turned on before |EX-CS| to ensure it's detected successfully at startup. This is covered in :ref:`ex-turntable/assembly:9. connect ex-turntable to your ex-commandstation`.

Expand the code below to see what we expect config.h to look like for |EX-TT|:

.. ..collapse:: Expand to see the |EX-TT| config.h, noting we have removed all comments for brevity:

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

Expand the code below to see what we expect myHal.cpp to resemble at this point:

.. ..collapse:: Expand to see the |EX-CS| myHal.cpp:

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

You will note in the paragraph above that we stopped one step earlier in the |EX-TT| assembly process, and that's because we need to ensure our traverser is available at a different I2C address and on a different Vpin to our turntable to ensure they are controlled independently of each other.

Expand the code below to see what we expect config.h to look like for |EX-TT|:

.. ..collapse:: Expand to see the |EX-TT| config.h, noting we have removed all comments for brevity:

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

Expand the code below to see what we expect myHal.cpp to resemble at this point:

.. ..collapse:: Expand to see the |EX-CS| myHal.cpp:

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

Tune your EX-Turntable positions
================================

Tuning the turntable
--------------------

.. .. collapse:: Expand to see the output

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

Tuning the traverser
--------------------



Control and automate your EX-Turntable
======================================
