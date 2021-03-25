
An Introduction to DCC++ EX ‘Extended’ Command Station
======================================================
Digital Command & Control for DCC enabled Model Railroad Layouts
================================================================

Overview
########
DCC++ is an Open Source Arduino Microcontroller based Do-it-Yourself and Affordable suite of DCC Command Stations.
Capable of operating on nearly all sizes of DCC Model Railroads layouts with Z, N, HO and G scales.
It can utilize various Controllers and applications like JMRI, Engine Driver, WiThrottle & Rocrail Apps to name a few.

Both DCC++EX & DCC++ original products are written in C++ and utilizing the Arduino IDE and PlatformIO & MS Visual Studio editors. 

Recent History
##############
First a Special thanks to Gregg E. Berman who had the original vision & idea for a model railroad Command Station using an Arduino Uno or Mega microcontroller with a Arduino Motor Shield, along with Mark Underwood (Twindad) who was instrumental in developing the first JMRI interfaces to the Original DCC++ Base Station.

The first DCC++ Base Station was released in August 2015 and was enhanced through 2017 by various GitHub users.  
In the Spring 2020 Fred Decker (FlightRisk) headed up a group of new and existing DCC++ developers to Enhance the DCC++ project.  Our first attempt to build up and out the Vision on the original code left us with a technological software decision of stay with the Original or build a New design with updated code structures and application interfaces.  

We opted to fix up and keep Gregg’s Original DCC++ 1.2.1+ Base Station code and Rename it to DCC++ ‘Classic’ this version can still can be downloaded from this website and it is now named DCC++ Base Station Classic.  
Note: For a look back at history and where it all began, see Gregg’s DCC++ build videos at [DCC++ 'Classic' Videos](https://www.youtube.com/channel/UCJmvQx-fe0OMAIH-_g-_rZw )


DCC++ EX User Guide
===================

Welcome again to this website and documentation for the DCC++ EX suite of open source model 
railroading software, firmware, and hardware. 
Please click on the Panels below navigate to the area of interest.

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
* Complete support for all the old commands and controllers/front-ends like JMRI
* Simpler, modular, faster code with an API Library for developers for easy expansion
* New features and functions in JMRI
* Automation (coming soon) 

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
   contributing/index
   support/index
   about/index
