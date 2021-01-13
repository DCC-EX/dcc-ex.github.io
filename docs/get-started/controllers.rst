****************************
Connecting Wirelessly
****************************

You need just two things that work together to operate your model railroad:

* The DCC++ EX Command Station
* A Controller

Command Station
---------------

The CS is covered in the getting started section and is usually an Arduino microcontroller and a motor shield or motor board. The CS accepts instructions from the frontend and generates packets that are transmitted to your track.

Front End
----------

Since the CS just accepts <DCC++> commands, you need something that sends those commands to run your trains. 

WebThrottle-EX
===============

The simplest option is to just use a "Throttle" aka "CAB" aka "Controller" connected directly to the CS. The simplest of all is probable WebThrottle-EX connected via a serial cable directly to the Command Station. You have control of multiple locomotives and can operate turnouts. There is a way to replace the USB cable with a wireless connection, but we will cover that later in the HC-12 section.

Engine Driver
=======================

Engine Driver is a throttle app for your phone that can control multiple locos and your turouts. There are two ways to connect it. The first method is by connecting directly to the CS via WiFi. You will need a WiFI board connected to the CS ***insert link here*** and that's it.

The second method is to use JMRI and connect Engine Driver (ED) to the computer running JMRI. That computer would then connect to the CS via a USB cable (normally) or via a Wireless USB Bridge. The computer running JMRI can be just about any type of computer, PC, Mac, Raspberry Pi, but most operators like the Pi option because it is inexpensive, small, can mount under the layout, and has a free image file that lets you flash it to a Micro-SD card and have a fill JMRI setup with WiFi with virtually no fuss.

JMRI
========

JMRI is sort of the 800lb gorrilla of front ends. In its simplest form, it is a throttle, or a gateway to allow you to use Engine Driver as a throttle without a WiFi board connected to the CS. The Wifi is built into the computer you use to run JMRI, and JMRI has a WiThrottle Server built into it. If you are seriously into your model railroad however, JMRI can provide a lot more value. It can handle your turnouts, outputs, and sensors. It lets you create rosters for you locos and a visual layout of your tracks.

Connecting Via USB cable
^^^^^^^^^^^^^^^^^^^^^^^^^

Probably the way most people use JMRI is to have a Raspberry Pi running JMRI connected via a short USB cable to the DCC++ EX Command Station. They then use Engine Driver on their phone connected to JMRI via Wifi as a throttle for their engines. If you want to actually operate using all the features or JMRI, you can connect a small monitor, keyboard and mouse to your computer or Raspberry Pi. You can replace the USB cable with a USB Wireless bridge which is covered in that section. But let's look at another method next.

Connecting Via VNC
^^^^^^^^^^^^^^^^^^^

VNC stands for "Virtual Network Computing", it is a way to access a device remotely. Variations of this are called "Remote Desktop" in Windows, Teamviewer, Anydesk, etc. It is free and it lets you take another device, like a tablet and have a viewport into the computer your are using to rund JMRI. It literally is a "remote desktop". Everything is running on your computer or Raspberry Pi, yet you can control it from a handheld wireless device with a touchscreen.

USB Wireless Bridge
====================

The USB Wireless Bridge is a pair of small, inexpensive devices that let you replace a USB cable with a wireless connection. You really could connect any two devices that would normally connect with a USB cable.The power of this system is that there is little or no configuration and no changes need to be made to your controller or the CS. In our world, here are some of the ways you can use it:

* Connect WebThrottle-EX running on a laptop or tablet wirelessly to the DCC++ EX Command Station
* Connect a computer or Raspberry Pi running JMRI (or another front end) to the Command Station
* Connect normally tethered handheld CABS (throttles) wirelessly to the Command Station
