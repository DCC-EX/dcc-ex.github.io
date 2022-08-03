.. meta::
   :keywords: EX-CommandStation Command Station EX-Installer Testing

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
*************************
Testing your installation
*************************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

Using the Arduino IDE Serial Monitor
-------------------------------------

To test with the Arduino Serial Monitor, download the Arduino IDE from the following link and install it on your computer.

`Download the Arduino IDE <https://www.arduino.cc/en/Main/software>`_

To do a quick test, open the Arduino application:

.. figure:: /_static/images/installer/arduino_ide.jpg
   :alt: Arduino IDE
   :scale: 100%

   The Arduino IDE

* Select "Tools -> Serial Monitor" from the Arduino IDE menu


.. figure:: /_static/images/installer/arduino_ide2.jpg
   :alt: Open the Serial Monitor
   :scale: 100%

   Open the Serial Monitor from the Tools Menu

You will see the following screen:


.. figure:: /_static/images/installer/serial_monitor.jpg
   :alt: Serial Monitor
   :scale: 100%

   Serial Monitor


* Select "115200" as the baud rate in the dropdown in the lower right
* Select "Both NL & CR" from the dropdown next to the baud rate

When you open the serial monitor you will see at least one line sent out as status information. If you have a WiFi board or Ethernet Shield you will see a page full of log information as it configures and connects to your network.

At the top of the serial monitor type ``<s>`` (lowercase "s") into the command textbox and press "Send". You should see:

.. code-block::

   <iDCC-EX V-0.2.1 / MEGA / STANDARD_MOTOR_SHIELD G-9db6d36>

This is the "status" command and reports your version, types of boards you are using, and a build number.

There are a lot of other commands you can enter here. As a matter of fact, you could use the serial monitor to test any of the DCC-EX API (application programming interface) commands. Please see the `DCC-EX Wiki <https://github.com/DCC-EX/CommandStation-EX/wiki>`_ for a list of commands.

Using WebThrottle-EX
--------------------

.. figure:: /_static/images/installer/exwebthrottle.jpg
   :alt: WebThrottle-EX
   :scale: 100%

   WebThrottle-EX

Click this link: :doc:`WebThrottle-EX </throttles/software/ex-webthrottle>` to run WebThrottle-EX hosted on our site, or visit `GitHub <https://github.com/DCC-EX/WebThrottle-EX>`_ to get the latest version to run on your computer.

Using Engine Driver (or other WiThrottle Cab) - Requires WiFi
--------------------------------------------------------------

.. figure:: /_static/images/installer/engine_driver.png
   :alt: Engine Driver
   :scale: 100%

   Engine Driver

You will need to install Engine Driver on your mobile device and then connect to the CS, either directly with AP mode or through your router with Station Mode. You can then use your phone to control your trains.
