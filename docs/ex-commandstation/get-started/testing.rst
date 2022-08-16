.. meta::
   :keywords: EX-CommandStation Command Station Testing

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

***************
Test your setup
***************

|conductor|

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

This page is specifically written for someone who has installed *just* the recommended hardware (including WiFi). However it will generally be suitable for testing most other configuration options.

Testing control of a loco
=========================

There are two simple options for testing your setup described below:

* Using our |EX-WT| (recommended)
* using the |Engine Driver| app installed on an Android device, |BR| or the |wiThrottle| app installed on an iOS device

.. sidebar:: 

    |tinkerer| |engineer|

    Additional options (controllers) for testing and diagnosing issues are available and is described in the :doc:`/ex-commandstation/advanced-setup/controllers` page if needed .

Using EX-WebThrottle
--------------------

Connect Everything:

* Disconnect the |EX-CS| from the computer (that you used to load the software)
* Connect the wires from the motor shield to your main track
* Plug in the power supply for the Moto shield **only**
* Reconnect the |EX-CS| to the computer
* wait for about 30 seconds

.. NOTE:: 
   :class: note-float-right-narrow

   The programming track is for programming only. Make sure you are on the main track if you expect your loco to move or respond to light or sound commands.

.. figure:: /_static/images/installer/exwebthrottle.jpg
   :alt: EX-WebThrottle
   :scale: 80%

   EX-WebThrottle

Click this link: :doc:`EX-WebThrottle </throttles/software/ex-webthrottle>` to run |EX-WT| hosted on our site, or visit `GitHub <https://github.com/DCC-EX/WebThrottle-EX>`_ to get the latest version to run on your computer.

.. TODO:: URGENT This text needs to be expanded - Using EX-WebThrottle

Using Engine Driver (or other WiThrottle Protocol app) - Requires WiFi
----------------------------------------------------------------------

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

You will need to install |Engine Driver| on your mobile device and then connect to the |EX-CS|, either directly with AP mode or through your router with Station Mode. You can then use your phone to control your trains.

.. TODO:: URGENT This text needs to be expanded - Using Engine Driver (or other WiThrottle Protocol app) - Requires WiFi

.. note:: 

   If you have any difficulties check the :doc:`diagnosing-issues` page for assistance.

   **Locos Can't Respond to Throttle Commands on the Programming Track!**

   We have repeated this in several places on the Website because it is such a common issue. The MAIN track is for running trains, the PROG (service track) is for programming your loco. **THE LOCO CANNOT RESPOND TO THROTTLE OR FUNCTION COMMANDS WHILE ON THE PROG TRACK** This is by design and part of the NMRA specification. There is such a thing as "Programming on Main", where you can adjust things like sounds, throttle curves, speed matching, etc, but you can't get acknowledgment back from the loco on the main track. That is usually fine because you will know if a setting like a sound change "took" or not. We will have a section on programming on main. ***TODO: Write the POM*** help.


Next Steps - Choosing a throttle
================================

Click :doc:`here <testing>` or click the "next" button see your options for a controller (throttle).
