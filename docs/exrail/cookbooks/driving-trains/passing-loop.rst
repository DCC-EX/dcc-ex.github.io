.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Passing loop shuttle
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On this page
      :depth: 1
      :local:

A passing loop shuttle involving two trains with a passing loop can be controlled quite easily but involves some more advanced concepts.

If we have a layout like this:

.. code-block::

              164           166
              |             |              Turnout2
    Dogbath ||════[1]═════╦═══[4]═══<<═════════╗
                          ╚═══[2]═══>>═════════╩═════════[3]══════════|| Catflap
                        Turnout1            |                      |
                                            167                    165

Block Reservations
===================

In |EX-R| we operate multiple trains at the same time and coordinate them with block reservations which is an entirely virtual concept but similar to early era real train operations where a driver must obtain a token from the signalman before proceeding into a particular block. In this example, we don't care which train enters the loop first or how it affects the other train. We define (in our minds) the block numbers which are shown in ``[x]`` above. There is no need for track breaks or other electronics, just the sensors so a train driver can say "When I get to the buffers.. STOP!"

For example, a train leaving Dogbath is already occupying ``[1]`` but it must reserve ``[2]`` before departing in case the other train has been stopped in ``[2]`` by a cow on the line. Similarly it cant leave ``[2]`` before the other train has cleared ``[3]``.

Basic passing-loop logic
========================

So, the sequence starting from Dogbath, going to Catflap will look like this:

.. code-block:: cpp

    SEQUENCE(100) 
      DELAYRANDOM(5000,10000)
      RESERVE(2) // will wait with loco stopped until block 2 is available.
      THROW(1)   // set the turnout so we will enter the loop correctly
      FWD(40)    // move off
      AT(167)    // we are in the West>East loop
        FREE(1)    // we are no longer in block 1
        RESERVE(3) // This will stop loco if 3 not yet free, and wait.
        CLOSE(2)   // set turnout to exit loop
        FWD(40)    // must resume speed if we were stopped.
      AT(165)    // when we get to Catflap
        STOP
        FREE(2)    // we are not in loop
    FOLLOW(101) // now follow the Catflap -> Dogbath sequence

And the Catflap to Dogbath sequence will be a similar logic but in reverse and with different sensors etc.

.. code-block:: cpp

    SEQUENCE(101)  // Catflap to Dogbath (loco in reverse)
      DELAYRANDOM(5000,10000)
      RESERVE(4) // will wait with loco stopped and until block 4 is available.
      THROW(2)   // set the turnout so we will enter the loop correctly
      REV(40)    // move off backwards 
      AT(166)    // we are in the E->W loop
        FREE(3)    // we are no longer in block 3
        RESERVE(1) // This will stop loco if 3 not yet free, and wait.
        CLOSE(1)   // set turnout to exit loop
        REV(40)    // must resume speed if we were stopped.
      AT(164)    // when we get to Dogbath
        STOP
        FREE(4)    // we are not in loop
    FOLLOW(101) // now follow the Dogbath-Catflap sequence 

Notice that you don't drive into an area of the track without first reserving the corresponding block, and you must remember to free it once you have safely left. Also the script above assumes that a train can cause the turnout to change quickly enough if it reaches a sensor in the loop and doesn't need to stop, this can be alleviated if you throw/close the turnout behind you as you reach your loop sensor so that the other train does not need to worry about any slow turnout movement.

Please bear in mind that your turnout geometry may be different. The diagram is for two right-hand turnouts, you may have used a left/right pair so modify the ``THROW``/``CLOSE`` statements above to suit.

Starting the shuttle
======================

We have the issue that one train is starting from the far end, and we have to establish the train positions, directions, initial reserved status and where in the sequence they must start.

If we assume that:

- Loco id 3 is ready at Dogbath and faces Catflap.
- Loco id 4 is ready at Catflap and faces Catflap (ie BOTH locos face East).

  Then we can create a ROUTE that will appear on your throttle and start the sequences.

.. code-block:: cpp

    ROUTE(1,"Start Dogbath-Catflap")
      FREEALL   // Clear any reserves left over from previous running 
      RESERVE(1) // loco is already at Dogbath
      RESERVE(3) // loco is already at Catflap
      SENDLOCO(3,100) // start loco 3 running the sequence from Dogbath
      SENDLOCO(4,101) // start loco 4 running the sequence from Catflap
    DONE

Handling facing trains
=======================

If your two trains start facing each other from opposite ends of the loop, you must allow for this change otherwise the train starting at Catflap will be told to reverse when leaving, this is embarrassing to say the least.

The INVERT_DIRECTION command tells |EX-R| to invert the ``FWD``/``REV`` commands for the current loco in the current task. Rather than duplicate both sequences with different direction commands, or litter them with ``IFLOCO`` checks, we can alter the startup to apply this invert to the task running loco 4 before starting at Catflap.

Note that |EX-R| is running a separate task for each loco.

.. code-block:: cpp

    ROUTE(1,"Start Dogbath-Catflap")
      FREEALL   // Make sure all reserves are cleared 
      RESERVE(1) 
      RESERVE(3)
      SENDLOCO(3,100) 
      SENDLOCO(4,102) // start loco 4 running the inverted sequence from Catflap
    DONE

    SEQUENCE(102) // run inverted direction commands from Catflap
      INVERT_DIRECTION // tell current task to invert directions 
    FOLLOW(101) // carry on 

Advanced Extras
=================

Once you have this basic shuttle working, you can use the methods described in previous examples to add signals, sound effects or perhaps a level crossing with gates.

You may consider having an intermediate station stop along one end of the line or extend the design to use three locos and two passing loops.
