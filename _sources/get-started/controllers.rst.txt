*********************************
Choosing a Controller (Throttle)
*********************************

You need just two things that work together to operate your model railroad:

* The DCC++ EX Command Station
* A Controller

The Command Station
---------------------

The CS is covered in the `getting started <get-started.html>`_ section and is usually an Arduino microcontroller and a motor shield or motor board. The CS accepts instructions from a controller and generates packets that are transmitted to your track.

The Front End (aka Controller)
---------------------------------

Since the CS just accepts <DCC++> commands, you need something that sends those commands to run your trains - a controller. It isn't very practical to type <t 1 3 75 1> into a serial monitor to tell your train to move ;)  A controller can be a hardware device like a handheld throttle (also called a CAB), or front-end software like JMRI or Rocrail. Here are a few of the methods you can use to control your layout.

Our WebThrottle-EX
===================

The simplest option is to just use a throttle connected directly to the CS. The simplest of all is arguably WebThrottle-EX connected via a USB cable from your computer and web browser directly to the Command Station. You have control of multiple locomotives and can operate turnouts. There is a way to replace the USB cable with a wireless connection, but we will cover that later in the Wireless USB Bridge section.

See `how to use WebThrottle-EX <../throttles/ex-webthrottle.html>`_

***insert diagram here of the webthrottle layout***

Engine Driver (WiThrottle devices)
==================================

Engine Driver is a throttle app for your phone that can control multiple locos and your turouts. It uses an interface called "WiThrottle" (for WiFi Throttle) and any WiThrottle compatible throttle will work with DCC++ EX. There are two ways to connect it; the first method is by connecting directly to the CS via WiFi. You will need a WiFI board connected to the CS (see `WiFi Setup <wifi-setup.html>`_).


***insert diagram here***

The second method is to use JMRI and connect Engine Driver (ED) to the computer running JMRI. That computer would then connect to the CS via a USB cable (normally) or via a Wireless USB Bridge. The computer running JMRI can be just about any type of computer, PC, Mac, Raspberry Pi, but most operators like the Pi option because it is inexpensive, small, can mount under the layout, and has a free image file that lets you flash it to a Micro-SD card and have a fill JMRI setup with WiFi with virtually no fuss.

See `How to use Engine Driver (WiThrottle) <../throttles/withrottle.html>`_

***insert diagram here***

JMRI
========

JMRI is sort of the 800lb gorrilla of front ends. In its simplest form, it is a throttle, or a gateway to allow you to use Engine Driver or a mouse or touchscreen as a throttle without a WiFi board connected to the CS. The Wifi is built into the computer you use to run JMRI, and JMRI has a WiThrottle Server built into it. The computer running JMRI, in turn, connects to the CS with a USB cable. JMRI is a complex program. if you are seriously into your model railroading however, JMRI can provide a lot of value. It can handle your turnouts, outputs, and sensors. It lets you create rosters for you locos and a visual layout of your tracks. There isn't much it can't do. And is is free and open source, just like DCC++ EX.

Connecting Via USB cable
^^^^^^^^^^^^^^^^^^^^^^^^^

Probably the way most people use JMRI is to have a Raspberry Pi running JMRI connected via a short USB cable to the DCC++ EX Command Station. They then use Engine Driver on their phone connected to JMRI via Wifi as a throttle for their engines. If you want to actually operate using all the features or JMRI, you can connect a small monitor, keyboard and mouse to your computer or Raspberry Pi. You can replace the USB cable with a USB Wireless bridge which is covered in that section. But let's look at another method next.

****insert diagram here***

Connecting Via VNC
^^^^^^^^^^^^^^^^^^^

VNC stands for "Virtual Network Computing", it is a way to access a device remotely. Variations of this are called "Remote Desktop" in Windows, Teamviewer, Anydesk, etc. It is free and it lets you take another device, like a tablet and have a viewport into the computer your are using to rund JMRI. It literally is a "remote desktop". Everything is running on your computer or Raspberry Pi, yet you can control it from a handheld wireless device with a touchscreen.

***insert diagram here***

USB Wireless Bridge
====================

The USB Wireless Bridge is a pair of small, inexpensive devices that let you replace a USB cable with a wireless connection. You really could connect any two devices that would normally connect with a USB cable.The power of this system is that there is little or no configuration and no changes need to be made to your controller or the CS. In our world, here are some of the ways you can use it:

* Connect WebThrottle-EX running on a laptop or tablet wirelessly to the DCC++ EX Command Station
* Connect a computer or Raspberry Pi running JMRI (or another front end) to the Command Station
* Connect normally tethered handheld CABS (throttles) wirelessly to the Command Station

***insert diagram here***

For more information about all the throttles, see the `Throttles Section <../throttles/index.html>`_>
