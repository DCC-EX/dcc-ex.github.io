.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Passing locos between sequences
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

Each of the methods below involves creating a new |EX-R| task that will run in parallel with the current task. The difference is in how the locoid information is passed to the new sequence.


.. code-block:: cpp

    START(sequence_id)

Start a new task with no loco attached.


.. code-block:: cpp

    SENDLOCO(loco_id,sequence_id)

Start a new task with the given loco id


.. code-block:: cpp

    START_SEND(sequence_id)

Hands over the current loco to the new task. The current task is no longer connected to this loco.


.. code-block:: cpp

    START_SHARED(sequence_id)

Shares the loco with the new task. For example the new task may flash the loco lights to a disco beat while the original task continues to drive the loco.
