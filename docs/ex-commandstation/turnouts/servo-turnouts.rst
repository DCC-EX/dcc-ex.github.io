.. include:: /include/include.rst
.. include:: /include/include-l2.rst
****************************
Servo driven turnouts/points
****************************

|conductor| |tinkerer|

There is already a reasonable amount of information available for servo driven turnouts/points within our documentation, so this page will primarily be a central location pointing to the existing documentation, along with any other considerations that need to be taken into account that may not be covered elsewhere.

:doc:`/reference/hardware/servo-module`



Important considerations for servo operation
============================================

**Test, test, test** your servo parameters prior to connecting to an actual turnout/point. If you have defined angles that exceed the physical limits of your turnout, you will likely damage it and/or the servo mechanism.

**Treat each servo and turnout as an individual** as not all servos are created equal. An angle that works with one servo and associated turnout will not necessarily provide the exact same result with another. Differences in servo brands, mounting methods, and even normal manufacturing tolerances will need to be factored in to the servo angles in use.

**Use flexible wire** to connect your servo arm to the turnout/point. Using a flexible connection between the turnout and the servo mechanism means if anything does go wrong such as the turnout getting jammed or an incorrect servo angle being sent, it reduces the chance of damaging the turnout or servo.