.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Defining Servo turnouts/points
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On this page
      :depth: 1
      :local:

(This does not include servos driven from track connected DCC decoders. See :doc:`/exrail/cookbooks/turnouts/defining-dcc-turnouts`)

Important considerations for servo operation
=======================================================

Servo turnouts/points are driven through a **PCA9685** servo control board or an |EX-IO|.

Test, test, test your servo parameters prior to connecting to an actual turnout/point. If you have defined angles that exceed the physical limits of your turnout, you will likely damage it and/or the servo mechanism.

Treat each servo and turnout as an individual as not all servos (or turnouts/points for that matter) are created equal. An angle that works with one servo and associated turnout will not necessarily provide the exact same result with another. Differences in servo brands, mounting methods, and even normal manufacturing tolerances will need to be factored in to the servo angles in use.

The EX-Toolbox Android application provides a servo movement testing tool to help you discover the necessary values for the angles below.

Use flexible wire to connect your servo arm to the turnout/point. Using a flexible connection between the turnout and the servo mechanism means if anything does go wrong such as the turnout getting jammed or an incorrect servo angle being sent, it reduces the chance of damaging the turnout or servo.

Defining servo based turnout objects
=======================================

Define servo based turnouts using |EX-R|.

.. code-block:: cpp
    
    SERVO_TURNOUT(id, vpin, active_angle, inactive_angle, profile, "description")

- ``id`` = Unique turnout ID within the CommandStation. All other turnout commands will refer to this turnout by this id.
- ``pin`` = The ID of the pin the servo is connected to, which would typically be the VPin ID of the PCA9685 controller board.
- ``active_angle`` = The angle to which the servo will move when the turnout is thrown (This is a value passed to the servo drtiver, it is not in degrees).
- ``inactive_angle`` = The angle to which the servo will move when the turnout is closed.
- ``profile`` = The speed at which a turnout will move: ``Instant``, ``Fast``, ``Medium``, ``Slow``.
- ``description`` = A human-friendly description of the turnout that will appear in WiThrottle apps and Engine Driver. Note that this must be enclosed in quotes ``""``. In some cases the HIDDEN keyword can be used here to prevent the turnout being visible to the throttles.

An example definition for a servo connected to the second control pins of the first PCA9685 connected to the CommandStation, using the slow profile for prototypical operation:

.. code-block:: cpp

    SERVO_TURNOUT(200, 101, 450, 110, Slow, "Coal yard exit")
