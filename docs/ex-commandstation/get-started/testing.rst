.. include:: /include/include.rst
.. include:: /include/include-l2.rst
***************
Test your setup
***************

|conductor|

Testing control of a loco
=========================

.. sidebar:: 

    |tinkerer| |engineer|

    A more advanced option for testing and diagnosing issues is available and is described here ???? if needed 

There are two simple options for testing your setup described below:

* Using our |EX-WT| (recommended)
* using the **Engine Driver** app installed on an Android device, |BR| or the **wiThrottle** app installed on an iOS device


Using WebThrottle-EX
____________________

Connect Everything:

* Disconnect the |EX-CS| from the computer (that you used to load the software)
* Connect the wires from the motor shield to your main track
* Plug in the power supply for the Moto shield **only**
* Reconnect the |EX-CS| to the computer
* wait for about 30 seconds

.. NOTE:: 
   :class: note-float-right

   The programming track is for programming only. Make sure you are on the main track if you expect your loco to move or respond to light or sound commands.

.. figure:: /_static/images/installer/exwebthrottle.jpg
   :alt: WebThrottle-EX
   :scale: 100%

   WebThrottle-EX

Click this link: :doc:`WebThrottle-EX </throttles/ex-webthrottle>` to run WebThrottle-EX hosted on our site, or visit `GitHub <https://github.com/DCC-EX/WebThrottle-EX>`_ to get the latest version to run on your computer.

... TODO - This text needs to be expanded

Using Engine Driver (or other WiThrottle Cab) - Requires WiFi
_____________________________________________________________

.. NOTE:: 
   :class: note-float-right

   The programming track is for programming only. Make sure you are on the main track if you expect your loco to move or respond to light or sound commands.

Connect Everything

* Disconnect the |EX-CS| from the computer (that you used to load the software)
* Connect the wires from the motor shield to your main track
* Plug in the two power supplies (The one for the Arduino and the the one for the motor shield)
* wait for about 30 seconds

.. figure:: /_static/images/installer/engine_driver.png
   :alt: Engine Driver
   :scale: 100%

   Engine Driver

You will need to install Engine Driver on your mobile device and then connect to the CS, either directly with AP mode or through your router with Station Mode. You can then use your phone to control your trains.

... TODO - This text needs to be expanded

.. note:: 

   If you have any difficulties check the :doc:`diagnosing-issues` page for assistance.

Next Steps - Choosing a throttle
================================

Click :doc:`here <testing>` or click the "next" button see your options for a controller (throttle).
