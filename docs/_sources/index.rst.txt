DCC++ EX User Guide
===================

Welcome to this website and documentation for the DCC++ EX suite of open source model 
railroading software, firmware, and hardware. DCC++ EX is an extension of the 
original DCC++ program written by Gregg E Bermann. 

==================   ==================   ====================
|Get Started|_       |Download|_          |Reference|_
------------------   ------------------   --------------------
`Get Started`_       `Download`_          `Reference`_
------------------   ------------------   --------------------
|Advanced Setup|_       |Support|_        |Contribute|_
------------------   ------------------   --------------------
`Advanced Setup`_       `Support`_        `Contribute`_
==================   ==================   ====================

.. |Get Started| image:: ./_static/images/timer_bl.png
.. _Get Started: get-started/index.html

.. |Download| image:: ./_static/images/download_bl.png
.. _Download: download/index.html

.. |Reference| image:: ./_static/images/api_bl.png
.. _Reference: reference/index.html

.. |Advanced Setup| image:: ./_static/images/advanced_bl.png
.. _Advanced Setup: advanced-setup/index.html

.. |Support| image:: ./_static/images/question_bl.png
.. _Support: support/index.html

.. |Contribute| image:: ./_static/images/puzzle_bl.png
.. _Contribute: contribute/index.html

Mission
#######

Our mission is to make the world of model railroading universally accessible.

To achieve that, DCC++ EX provides the model railroad community with a complete, open source DCC (Digital Command Control) system - one that is simple, affordable, and expandable, to control model trains and accessories. Further, it is our goal that this project be organized, documented, and maintained so that it can continue far into the future.

What is DCC++ EX?
#################

DCC++ EX is the organization developing and maintaining several products that together represent a fully open source DCC system. Currently, this includes the following:

* **CommandStation-EX** - the latest take on the DCC++ command station for controlling your model railroad. DCC-EX runs on an Arduino board, and includes advanced features such as a WiThrottle server implementation, turnout operation, general purpose inputs and outputs (I/O), and JMRI integration.
* **WebThrottle-EX** - a simple web based controller for your DCC++ and DCC-EX command station.
* **Installer-EX** - an installer that takes care of downloading and installing DCC++ or DCC-EX firmware onto your hardware setup.
* **BaseStation-Classic** - the original DCC++ software, packaged in a stable release. No active development, bug fixes only.

A basic DCC++ EX hardware setup can use easy to find, widely avalable Arduino boards that you can assemble yourself. Both CommandStation-EX and BaseStation-Classic support much of the NMRA Digital Command Control (DCC) standards, including:

* simultaneous control of multiple locomotives
* 1 and 2 byte byte locomotive addressing
* 128-step speed throttling
* Activate/de-activate all accessory function addresses 0-2048
* Control of all cab functions F0-F28
* Main Track: Write configuration variable bytes and set/clear specific configuration variable (CV) bits (aka Programming on Main or POM)
* Programming Track: Same as the main track with the addition of reading configuration variable bytes

**What's new in CommandStation-EX?**

* WiThrottle server built in. Connect Engine Driver or WiThrottle clients directly to your Command Station
* WiFi and Ethernet shield support
* No more jumpers or soldering!
* Direct support for all the most popular motor control boards
* I2C Display support
* Improved short circuit detection and automatic reset from an overload
* Current reading, sensing and ACK detection settings in milliAmps instead of just pin readings
* Improved adherence to the NMRA DCC specification
* Complete support for all the old commands and front ends like JMRI
* Simpler, modular, faster code with an API Library for developers for easy expansion
* New features and functions in JMRI
* Automation (coming soon) 

.. note:: DCC-EX is a major rewrite to the code. We started over and rebuilt it from the ground up! For what that means to you, click `here <about/rewrite.html>`_.

Levels
######

**Choose Your Path**

We've found that our users tend to identify with one of the following three categories. So we've created different paths to help navigate our DCC-EX system and this website. Don't worry, the paths are integrated and you can "switch a turnout" at any point and take another path. See below if you most identify with being a, "Conductor", a "Tinkerer" or an "Engineer".



Conductor
---------

.. image:: _static/images/conductor_hat1.png
   :alt: Conductor Hat
   :width: 100px
   :height: 72px
   :align: left

A Conductor, for the most part, just wants to enjoy operating trains. You could be someone new to trains or picking it up after a long absence, or you could be someone coming from running DC and looking to switch over to DCC. This is also the perfect place for someone who just wants something that works without much tinkering. We'll show you how to put together a Command Station with a Controller and have you up and running in just a few minutes. In short, a Conductor wants to drive trains and doesn't want to have to deal with the details of the hardware or software involved. This path will keep things simple.

Tinkerer
--------

.. image:: _static/images/propeller_beanie.png
   :alt: Propeller Beanie
   :width: 110px
   :height: 110px
   :align: left

A Tinkerer likes the joy of building things themselves. They may not have an Engineering Degree, but they know how to connect a jumper wire and possibly use a soldering iron. They don't have a problem opening something like the Arduino IDE to change settings in a configuration file and upload it back to their Command Station. A Tinkerer wants to do more with model trains like using different motor controllers or getting into more detailed control of turnouts, sensors and other accessories. This path will provide more options over the Conductor path and cover things like expanding your system and using the JMRI software (Java Model Railroad Interface) for more advanced control of your locomotives and your track.

Engineer
--------

.. image:: _static/images/engineer_hat2.png
   :alt: Engineer Hat
   :width: 120px
   :height: 98px
   :align: left

An Engineer is a little more versed in computers and/or electronics. They have a desire to dig a little deeper into how things work. They can understand the basics of computer code and can look at the DCC++ EX software and perhaps make simple changes. They may want to help with offering their talents to the project. They are not averse to experimenting with things to make something work. These are the people whose layout looks like a telephone switching station when you look under their benchwork. This path will offer more technical information and cover more in depth topics like accessory control, sensors, and customizing the DCC++ EX System.

Keep these definitions in mind as you proceed through this website.


I'm Ready!
###########

To learn more about how to build your own DCC++ EX station, go to the `Get Started <get-started/index.html>`_ page!

.. toctree::
   :hidden:
   :maxdepth: 4

   get-started/index
   advanced-setup/index
   throttles/index
   reference/index
   download/index
   contributing/index
   support/index
   about/index