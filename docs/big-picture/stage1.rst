********
Stage 1
********

Stage 1 of our RMFT layout is a simple loop including a single siding for a station.

This allows for continuous running of up to three trains with automated switching for entering and exiting the station siding.

.. raw:: html
  :file: ../_static/images/big-picture/rmft-stage1.drawio.svg

Turnouts
=========

Two turnouts are used in this first stage of our RMFT layout to allow trains to enter and exit the station siding, or continue along the main track.

Turnout definitions
____________________

We will define turnout 1 with an ID of 100, and turnout 2 with an ID of 101.

Sensors
========

Six sensors are used in this first stage, which allows us to have up to three trains controlled by EX-RAIL automation. The sensors are placed at the beginning and end of each virtual block to ensure we know when the front of the train enters a block, and when the rear of the train has exited a block.

Signals
========

Three sensors have been used in this first stage to indicate whether or not a train can enter either the station siding or proceed beyond turnout 1 on the main track, to indicate whether a train can exit the station siding, or if a train can proceed beyond turnout 2 on the main track.

Virtual blocks
===============

We've divided the layout into three virtual blocks, allowing for up to three trains to coexist safely on the layout.

Block 1
________

Block 1 consists of the majority of the layout, allowing a train to run from turnout 2 all the way to turnout 1 uninterrupted.

Block 2
________

Block 2 consists of the section of the main track between turnouts 1 and 2, providing for a section to hold one train, allow a train on the station siding to exit safely, and also prevent a train running around the main track from entering this block.

Block 3
________

Block 3 is for our station siding, ensuring no other trains can enter this block while it is occupied.

Station
========

In this particular stage, there's nothing specific for the station here, however some advanced concepts might be to trigger an automated sound recording of arrivals and departures based on triggering sensor 3.

This would likely make use of the EX-RAIL ``AT()`` command.
