.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Basic driving functions
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

|EX-R| contains a number of basic commands to drive locos and control their functions such as lights and sounds.

Its important to understand that |EX-R| has "tasks". A task may be driving loco 3 using sequence(555) while another task is driving loco 7 using a the same or a different sequence. That is why the driving commands below do not refer to the loco address, they take the address from the task executing the sequence. 

The loco associated with a task can be set with a `SETLOCO(locoid)` executed within the task, or it can be automatically assigned from a throttle using a hand-off to an :doc:`AUTOMATION </exrail/getting-started>`.

All driving speeds are in the range 0 to 127 where 0 is a normal stop (where a loco's decoder will usually stop gently as if the driver were applying the brakes) and speed 1 is an emergency stop where the loco will stop immediately without any semblance of momentum. The same speed range applies for DC and when running with 28 speed steps.
i.e. |BR|
|_| **speed** - DCC speed (0-127) |BR|
|_| |_| |_| |_| • ``2-127`` = actual speed 1-126  |BR|
|_| |_| |_| |_| • ``0`` = stop  |BR|
|_| |_| |_| |_| • ``1`` = Estop

The basic driving commands are:

- ``FWD(speed)`` will start the loco moving forward at the given speed.
- ``REV(speed)`` will start the loco moving in reverse at the given speed.
- ``SPEED(speed)`` alters the loc speed without changing the direction.
- ``STOP`` is the same as ``SPEED(0)``
- ``ESTOP`` is the same as ``SPEED(1)``

Bear in mind that ``FWD(0)`` and ``REV(0)`` are not quite the same thing as it will affect the loco lights (if the loco has direction changing lights fitted) and may involve sound effects if the loco simulates the driver changing the reversing gear.

Usually, a sequence being used to drive a loco will include ``AT(vpin)`` commands to continue until a given sensor is detected.
