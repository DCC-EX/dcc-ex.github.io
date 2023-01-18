.. include:: /include/include.rst
.. include:: /include/include-l3.rst
|EX-CS-LOGO|

|conductor| |tinkerer| |engineer|

*******************
Controlling signals
*******************

Signals are always controlled by the first Vpin/pin associated with the signal.

For light signals, this means the Vpin/pin associated with the red aspect, and for semaphore or servo signals, there is only one Vpin/pin associated with the signal.

There are three |EX-R| commands available for controlling signals:

- ``RED(vpin)`` - Set the signal to the red aspect
- ``AMBER(vpin)`` - Set the signal to the amber aspect
- ``GREEN(vpin)`` - Set the signal to the green aspect

It doesn't matter what type of signal it has been defined as, the control commands are the same.

These commands can be used within automation sequences to automatically set signal aspects as part of other activities such as closing/throwing turnouts/points.

For a simple example, to set a signal at pin 28 red when turnout ID 1 is thrown, this event handler would be added to "myAutomation.h":

.. code-block:: cpp

  SIGNAL(28, 30, 32)

  ONTHROW(101)
    RED(28)
  DONE

For further information on controlling signals refer to :ref:`ex-rail/ex-rail-reference:signals`, and for some examples refer to :doc:`/big-picture/index`.

Controlling DCC signals
=======================

If, instead your signals will be controlled as per any other DCC accessory device, you will need to familiarise yourself with the :ref:`ex-rail/ex-rail-reference:dcc accessory decoder commands` as outlined in the |EX-R| reference.

.. code-block:: cpp

  red 101
  amber 102
  green 103