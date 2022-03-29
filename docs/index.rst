DCC++ EX Model Railroading
===========================

.. image:: ./_static/images/icons/v40banner.jpg
   :alt: v4_0 Release Banner
   :class: float-left
   :scale: 50%
   :target: download/commandstation.html

.. image:: ./_static/images/icons/donate_button_blue.png
   :alt: Donate Button
   :class: float-right
   :scale: 50%
   :target: donate/index.html

The DCC-EX team is pleased to announce the next version of the DCC++EX Command Station. There are tons of new features and enhancements. So many in fact, it takes a separate page to list them all! Be sure to find us on our :doc:`Discord channel </support/index>`. Here are just a few features to whet your appetite.

* EX-RAIL Automation and accessory control
* JMRI and Engine Driver enhancements
* HAL (Hardware Abstraction Layer) to easily add new types of input and output devices
* Synchronize multiple throttles

For a complete list, see the :doc:`Release Notes </reference/software/release-notes>` and the :doc:`Press release <press/v40-announce>`.

Welcome! DCC++ EX is an easy to use, do-it-yourself and affordable, open source DCC CommandStation and suite of supporting products for running your complete model railroad layout. Based on Arduino technology, DCC++ EX is supported by many controllers and applications like JMRI, Engine Driver, WiThrottle, Rocrail and more.

.. table::
   :align: left
   :class: intro-table

   ==================   ==================   ====================
   |Timer|_             |Arrow|_             |Binder|_
   ------------------   ------------------   --------------------
   |Get Started|        |Download|           |Reference|
   ------------------   ------------------   --------------------
   |Lightning|_         |Question|_          |Puzzle|_
   ------------------   ------------------   --------------------
   |Advanced Setup|     |Support|            |Contribute|
   ==================   ==================   ====================

.. |Timer| image:: ./_static/images/timer_bl.png
.. _Timer: get-started/index.html
.. |Get Started| replace:: :doc:`/get-started/index`

.. |Arrow| image:: ./_static/images/download_bl.png
.. _Arrow: download/index.html
.. |Download| replace:: :doc:`Download </download/index>`

.. |Binder| image:: ./_static/images/api_bl.png
.. _Binder: reference/index.html
.. |Reference| replace:: :doc:`/reference/index`

.. |Lightning| image:: ./_static/images/advanced_bl.png
.. _Lightning: advanced-setup/index.html
.. |Advanced Setup| replace:: :doc:`/advanced-setup/index`

.. |Question| image:: ./_static/images/question_bl.png
.. _Question: support/index.html
.. |Support| replace:: :doc:`/support/index`

.. |Puzzle| image:: ./_static/images/puzzle_bl.png
.. _Puzzle: contributing/index.html
.. |Contribute| replace:: :doc:`Contribute </contributing/index>`

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
* Non-blocking ACK processing - Main track signal is not interrupted when programming on the service track
* Advanced CV programming diagnostics and tuning
* Improved adherence to the NMRA DCC specification
* Complete support for all the old commands and controllers/front-ends like JMRI
* New DCC-EX features and integrations built into JMRI, EngineDriver, DCCppCAB and more
* Simpler, modular, faster code with an API Library for developers for easy expansion
* New direct throttle support from apps like EngineDriver, DCCppCAB
* Ability to JOIN operations and service track as one "main" track with 2 power districts when not programming
* DriveAway(tm) feature to place a loco on an isolated siding, read its ID, and drive onto the layout
* New features and functions in JMRI, like a new current meter
* Simple address read and set without understanding long/short CVs
* Function reminders - Function commands are repeated to ensure changes are read by your decoder
* Ability to run many more locos
* Emergency Stop commands
* Forget locos command - Stops reminders for locos no longer on the track
* Built-in Automation and accessory control with EX-RAIL!
* Lively community online, and active feature development

.. note:: DCC-EX is a major rewrite to the code. We started over and rebuilt it from the ground up! For what that means to you, click on our :doc:`Rewrite Article <about/rewrite>`.


Next see the :doc:`Get Started section <get-started/index>` or click next below.

.. toctree::
   :hidden:
   :maxdepth: 4

   get-started/index
   advanced-setup/index
   throttles/index
   automation/index
   reference/index
   download/index
   projects/index
   contributing/index
   roadmap/index
   support/index
   site-map/index
   donate/index
   press/index
   about/index
