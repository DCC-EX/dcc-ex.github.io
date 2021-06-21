DCC++ EX Model Railroading
===========================

Welcome! DCC++ EX is an easy to use, do-it-yourself and affordable, open source DCC CommandStation and suite of supporting products for running your complete model railroad layout. Based on Arduino technology, DCC++ EX is supported by many controllers and applications like JMRI, Engine Driver, WiThrottle, Rocrail and more.

.. table::
   :align: left

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
.. _Contribute: contributing/index.html

Mission
#######

Our mission is to make the world of digital model railroading universally accessible.

To achieve that, DCC++ EX provides the model railroad community with a complete, open source DCC (Digital Command Control) system - one that is simple, affordable, and expandable, to control model trains and accessories. Further, it is our goal that this project be organized, documented, and maintained so that it can continue far into the future.

What is DCC++ EX?
#################

DCC++ EX is the organization developing and maintaining several products that together represent a fully open source DCC system. Currently, this includes the following:

* **CommandStation-EX** - the latest take on the DCC++ command station for controlling your model railroad. DCC-EX runs on Arduino boards, and includes advanced features such as a WiThrottle server implementation, turnout operation, general purpose inputs and outputs (I/O), and JMRI integration.
* **WebThrottle-EX** - a simple web based controller for your DCC++ and DCC-EX command station.
* **Installer-EX** - an installer that takes care of downloading and installing DCC++ or DCC-EX firmware onto your hardware setup.
* **BaseStation-Classic** - the original DCC++ software, packaged in a stable release. No active development, bug fixes only.

A basic DCC++ EX hardware setup can use easy to find, widely available Arduino boards that you can assemble yourself. Both CommandStation-EX and BaseStation-Classic support much of the NMRA Digital Command Control (DCC) standards, including:

* simultaneous control of multiple locomotives
* 2 and 4 byte locomotive addressing
* 28 and 128 throttle speed steps
* Activate/de-activate all accessory function addresses 0-2048
* Control of all cab functions F0-F28 and F29-F68
* Main Track: Write configuration variable (CV) bytes and set/clear specific CV bits (aka Programming on Main, or POM)
* Programming Track: Same as the main track with the addition of reading CV bytes

**What's new in CommandStation-EX?**

* WiThrottle server built in. Connect Engine Driver or WiThrottle clients directly to your Command Station
* WiFi and Ethernet shield support
* No more jumpers or soldering!
* Direct support for all the most popular motor control boards
* 28 speed steps in addition to 128
* I2C Display support
* Improved short circuit detection and automatic reset from an overload
* Current reading, sensing and ACK detection settings in milliAmps instead of just pin readings
* Improved adherence to the NMRA DCC specification
* Complete support for all the old commands and controllers/front-ends like JMRI
* Simpler, modular, faster code with an API Library for developers for easy expansion
* New throttle support from apps like DCCpp Cab
* Ability to JOIN operations and service track as one "main" track with 2 power districts when not programming
* New features and functions in JMRI, like a new current meter
* Automation (coming soon!) 

.. note:: DCC-EX is a major rewrite to the code. We started over and rebuilt it from the ground up! For what that means to you, click on our `Rewrite Article <about/rewrite.html>`_.


Next see the `Get Started section <get-started/index.html>`_ or click next below.

.. toctree::
   :hidden:
   :maxdepth: 4

   get-started/index
   advanced-setup/index
   throttles/index
   reference/index
   download/index
   projects/index
   contributing/index
   roadmap/index
   support/index
   about/index
