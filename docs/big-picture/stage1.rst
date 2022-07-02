********
Stage 1
********

Stage 1 of our RMFT layout is a simple loop including a single siding for a station.

This allows for continuous running for up to three trains with automated switching for entering and exiting the station siding.

.. raw:: html
  :file: ../_static/images/big-picture/rmft-stage1.drawio.svg

Station
========

In this particular stage, there's nothing specific for the station here, however some advanced concepts might be to trigger an automated sound recording of arrivals and departures based on triggering sensor 3.

This would likely make use of the EX-RAIL ``AT()`` command.

Turnouts
=========

Two turnouts are used in this first stage of our RMFT layout.

Sensors
========

Six sensors are used in this first stage, which allows us to have up to three trains controlled by EX-RAIL automation. The sensors are placed at the beginning and end of each virtual block to ensure we know when the front of the train enters a block, and when the rear of the train has exited a block.

Signals
========

This is a section for signal details.

Virtual blocks
===============

This is a section for virtual block details.
