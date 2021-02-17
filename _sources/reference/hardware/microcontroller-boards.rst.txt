Microcontroller Boards
======================

CommandStation-EX currently is designed exclusively for Arduino microcontollers. Out of the box, it is compatible with the following boards:

* Arduino Mega **[RECOMMENDED]**
* Arduino Uno
* Arduino Nano

Why do you recommend the Mega?
------------------------------

* When compiled, our code just barely squeezes onto an Arduino Uno. **A mega allows you to add more features** like networking and displays because it has more memory.
* The Mega has many more GPIOs (General Purpose Input/Outputs) available to you for constructing control panels and controlling turnouts or signals.
* The mega is only modestly more expensive than an Uno, with clones available for less than $10 USD.

.. image:: ../../_static/images/mega.jpg
   :alt: Arduino Mega Microcontroller
   :scale: 100%

If you already have an Uno, or will use JMRI to control your trains, then by all means use an Uno.

What about the Nano?
--------------------

The Arduino nano shares the same processor with the Arduino Uno, so we support it. The nano has a different form factor than the Uno or Mega, so motor driver shields will usually need to be attached with jumper wires. Other than that difference, it is in every way as capable as an Arduino Uno. 

Will you support other microcontrollers in the future?
------------------------------------------------------

Yes, that is on our roadmap.

Click here for a complete `Shopping List <./shopping-list.html>`_