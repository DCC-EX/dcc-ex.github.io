.. include:: /include/include.rst
.. include:: /include/include-l1.rst
  
|EX-FC-LOGO|

*********
Overview
*********

|tinkerer| |githublink-ex-turntable-button2|

.. sidebar:: 
  
  .. contents:: On this page
    :depth: 2
    :local:

What is EX-FastClock?
=====================


|EX-FC| is a standalone microprocessor based fast adjustable speed clock, using an additional Arduino Uno in conjuction with a sheild based TFT touchscreen. Features have been added to |EX-CS| to allow the clock to integrate to the |EX-CS| and control |EX-RAIL| based on time events.

Each time the time changes the |EX-CommandStation| looks for a time change event and if it find a match it executes the commands recorded for that event as defined inmthe |EX-RAIL| myAutomation.h file.  Additionally the |EX-CommandStation| will issue a time broadcast so that other devices such as clock repeaters can capture the time.  Also where WiThrottle devices are connected a WiThrottle broadcast is made witch means that connected devices such as Engine Driver can dislay the time.
|
|EX-FC| allows the FastClock device to connect to the |EX-CS| via either Serial Communications or I2C.  Even though |EX-FC| provides the code for an Uno based Clock it should be possible for |tinkerer-text| level users to add the relevent code if they already have a working clock that thye wish to integrate to |EX-CommandStation|.

To make full use of |EX-FC|, you will need a basic understanding of :doc:`EX-RAIL </ex-rail/index>` automation, but we'll share the details and some examples to help with this.

.. note::

  |EX-FC| is in public Beta testing, and as such, we encourage regular feedback on the success or otherwise of both the software and documentation. Please reach out via any of our :doc:`/support/contact-us` methods and help us get |EX-FC| as easy to use and reliable as possible.



The |EX-FC| integration includes:

* A ready made Arduino program for an Arduino Uno based Fast Clock
* Support for Serial connection
* |I2C| device driver
* EX-RAIL automation support
* Time Broadcast for time display on WiThrottle controllers such as |Engine Driver|
* Debug output to Serial Monitor
* Out-of-the-box support for several common stepper drivers and motors
* 

.. note:: 

  Credit where credit is due!
  
  The |EX-FC| is based on a project originally written by Jim Gifford (Hallet Cove Southern) in June 2017. That project used a 32 x 8 LED matrix to display the time and was controlled by a number of pushbuttons. You can see Jim's Original Project `here <https://www.hallettcovesouthern.com/track-plan-design-info/arduino-projects/fast-clock/>`.



  **MCUFRIEND.kbv credit:** This library was written by David Prentice and has become the De-Facto standard for the shIEld based TFT screens used in this project. This library inherits frommthe Adafruit GFX library.

  **Adafruit** for the Adafruit GFX Library.


Next Steps
==========

Now that you have a general overview of EX-FastClock's features and capabilities, click the "next" button see what is needed to create an |EX-FC|.
