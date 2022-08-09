.. meta::
   :keywords: EX-CommandStation Command Station Controllers

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

*********************************
Choosing a Controller (Throttle)
*********************************

|conductor| 

.. sidebar::

  .. contents:: On this page
    :depth: 4
    :local:

This page is specifically intended for a |conductor-text| who has installed *just* the recommended hardware. If you are a |tinkerer-text| or |engineer-text| or have installed some of the additional, or different, hardware from that recommended for a |conductor-text| then we suggest that you look at the :doc:`/ex-commandstation/advanced-setup/controllers` page for the full list of controller (Throttle) options.

What You Need and Why You Need It
=================================

You need just two things that work together to operate your model railroad:

* The |EX-CS| (aka the Command Station or 'CS')
* A Controller (aka Front-end, Cab, or Throttle)

The EX-CommandStation
_____________________

The |EX-CS| is covered in the :doc:`Getting Started <index>` section, and is usually an Arduino microcontroller, a motor driver and a WiFi shield. The CS accepts instructions from a controller and generates packets that are transmitted to your track.

The Controller (Throttle)
_________________________

Since the |EX-CS| simply accepts commands to turn into signals for your layout, you need something that sends those commands to run your trains - a controller. It isn't very practical to type something like <t 1 3 75 1> into a serial monitor to tell your train to move each time! 😉  A controller can be a hardware device like a handheld throttle (also called a Cab), an App that runs on your phone, a Web Page, or front-end software like |JMRI| or Rocrail that runs on a computer or Raspberry Pi. 

----

Connection Types
=================

Your controller can connect to the |EX-CS| several different ways, such as:

* **WiFi**
* **Direct connection using a USB cable**
* 2 wires to an Arduino serial port
* Ethernet
* Bluetooth 
* Remote connection (VNC, MQTT, etc.)

On this page we are only going to cover a small number of popular options that will be suitable for use if you have installed *just* the recommended hardware. Namely **WiFi** (using a smart phone) and **Direct Connection**. 

Here is a list of *some* of the controllers you can use with the |EX-CS|.

Connecting via WiFi
___________________

For those who just want to run trains and not use any other control software, the simplest method to get going is to download a compatible phone or tablet app and connect directly from your wireless device to the |EX-CS|. You need a CS with a WiFi Shield. Here is an image that represents a direct connection.

.. image:: /_static/images/throttles/throttle_wifi_direct.png
   :alt:  WiFi Throttle Direct to CS
   :align: center
   :scale: 50%

There are number of excellent :doc:`phone apps and physical hardware devices </throttles/index>` that can be used a wifi controller (throttle) for the |EX-CS|.  On this page we are only going to cover two.  These two are a) free, or have a free version, b) are reasonably easy to get to work, and c) most people will already have a suitable phone to use.

Compatible Wifi Throttles
^^^^^^^^^^^^^^^^^^^^^^^^^

For more information on any of these throttles, you can click on their links below or see our :doc:`Throttles Page Index </throttles/index>`.

Engine Driver (Android \| WiThrottle \| WiFi)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Engine Driver| is a throttle app for your phone that can control multiple locos and your turnouts. It uses an interface called "WiThrottle" (for WiFi Throttle) and any WiThrottle compatible throttle will work with the |EX-CS|. There are two ways to connect it;

* The first method is by connecting directly to the CS via WiFi. You will need a WiFi board connected to the CS (see Wifi Setup :doc:`WiFi Setup <wifi-setup>`).
* The second method is to use |JMRI| and connect |Engine Driver| (ED) to the computer running |JMRI|. (We won't cover that option here.)

See :doc:`Engine Driver Page </throttles/software/engine-driver>`

WiThrottle (iOS \| WiThrottle \| WiFi)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|WiThrottle| is an app for iPhones and iPads. It can connect directly to the |EX-CS| like |Engine Driver| does, or connect to |JMRI| on a computer and then have |JMRI| connect to the CS via a USB cable.

See :doc:`WiThrottle Page </throttles/software/withrottle>`

Connection via USB
__________________

Here are your connections, just a computer running a chromium-based browser, a USB cable, and your |EX-CS|.

.. image:: /_static/images/throttles/webthrottle_setup.jpg
   :alt: EX-WebThrottle
   :align: center
   :scale: 45%

Compatible USB Throttles
^^^^^^^^^^^^^^^^^^^^^^^^^

There is currently only one USB compatible controller (throttle) for the |EX-CS|.

Our EX-WebThrottle (DCC++ | USB/Serial)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The simplest option is to just use a throttle connected directly to the CS. The simplest of all is arguably |EX-WT|, connected via a USB cable from your computer and web browser directly to the Command Station. You have control of multiple locomotives and can operate turnouts. There is a way to replace the USB cable with a wireless connection, but we will cover that later in the Wireless USB Bridge section. Below is a picture of |EX-WT| with the side menu open. You can click on the image to see it full size.

.. image:: /_static/images/throttles/webthrottle1.jpg
   :alt: EX-WebThrottle
   :align: center
   :scale: 40%

For operating instructions see :doc:`how to use EX-WebThrottle </throttles/software/ex-webthrottle>`


----

Next Steps - Testing your setup 
===============================

Click :doc:`here <testing>` or click the "next" button to learn how to test your |EX-CS|.
