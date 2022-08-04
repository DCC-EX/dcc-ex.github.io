.. include:: /include/include.rst
.. include:: /include/include-l1.rst
********************************************************
Stage 3 - Turnouts/Points, Accessories, Sensors & Blocks
********************************************************

|conductor| |tinkerer| |engineer|

What to expect to learn from stage 3
====================================

At the end of this stage, we expect you will have learnt the following:

* How add a Loco Roster to your |EX-CS|
* How add add function labels for you Roster Entries
* How to add images for your locos (Engine Driver only)

Notes
=====

Tuning servo positions
______________________

An important item to note when configuring servo based turnouts/points and signals is that the angles provided are going to be unique to your layout, and possibly even be unique to each particular turnout/point or signal, depending on how they are mounted and physically connected.

We provide some handy documentation on how to evaluate the correct angles on our :doc:`/reference/hardware/servo-module` page.

Turnout/point object IDs
________________________

Throughout this exercise, we will be defining turnout/point objects, and for consistency will be using IDs in the range of 100 to 199 for these.

This way, the various possible variations of each type of object will be defined with the same ID, meaning the same |EX-R| sequences will apply, no matter how the objects are defined.

For further information on IDs used in |EX-R|, refer to the :ref:`ex-rail/ex-rail-reference:notes` section of the |EX-R| reference page.

DCC addresses
_____________

Further to the above, for DCC controlled turnouts/points, these will commence at the linear DCC address 101, which starts at an address of 26, and a sub address of 0.

For help understanding linear vs. address/sub address formatting of DCC accessories, refer to the :ref:`reference/downloads/documents:stationary decoder address table (xlsx spreadsheet)`.

Sensor types
============

For simplicity, we will use infrared obstacle avoidance/proximity sensors throughout these exercises, which produce an active low output when activated.

If you use different sensors that simply provide an active low or high output, then there should be no change required to the various automation sequences provided, except using a negative "-" for the sensor pin ID if the sensors are active high instead of active low.

.. note:: 

  When defining aliases for sensors, you cannot specify a negative number for these, and therefore to use an alias with an active high sensor, you need to add the negative in front of the alias name when referring to it in sequences and routes instead.

  This is invalid:

  .. code-block:: 

    ALIAS(SNS1, -22)

  Instead, these use cases are valid:

  .. code-block:: 

    ALIAS(SNS1, 22)

    AT(-SNS1)         // When activie high sensor 1 is triggered
    IF(-SNS1)         // If activie high sensor 1 is triggered
