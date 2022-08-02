.. include:: /include/include.rst
.. include:: /include/include-l2.rst
**********
DCCpp CAB
**********

|conductor| |tinkerer| |engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

.. image:: /_static/images/throttles/icon_android.png
   :alt: Android Logo
   :scale: 30%
   :align: left

This is an Android App (with plans for iOS) from Spain. One of the major benefits of DCCpp CAB is that it speaks the <DCC++> Application Programming language (API) natively (see our :doc:`Command Reference </reference/software/command-reference>`). This means it is fast and can take advantage of some features that exist in the |EX-CS| not implemented in other APIs. Another benefit is that this throttle can use Bluetooth instead of Wifi if you choose! There are several advantages to using Bluetooth, the main one being that Uno and Nano users can use a wireless throttle!

You can find it in the Play Store: `DCCpp CAB App <https://play.google.com/store/apps/details?id=com.infotronikblog.dcc_cab>`_

And the website here: `DCCpp Android Cab Infotrokik Blog <http://lamaquetade.infotronikblog.com/dccpp-android-cab/>`_

.. _dccpp-features:

Features
=========

* Speaks the <DCC++> Command Language natively
* Connect via WiFi *or* Bluetooth
* Read and Write CVs
* Serial Monitor to send manual commands and view the log

Screenshots
============

.. image:: /_static/images/throttles/dccpp2.jpg
   :alt: Dccpp CAB Screenshot 2
   :scale: 70%
   :align: left

.. image:: /_static/images/throttles/dccpp3.jpg
   :alt: Dccpp CAB Screenshot 3
   :scale: 70%
   :align: left

.. rst-class:: clearer

..
   The next line is trying to avoid a duplicate label name since many files may have a requirements section

.. _dccpp-requirements:

Requirements
=============

* A |EX-CS| (Mega based for WiFi or Mega or Uno/Nano based for Bluetooth)
* An Android Cell Phone or Tablet
* A Wifi Shield (or other ESP8622 solution) if you want to connect using WiFi :doc:`Wifi Setup Page </ex-commandstation/get-started/wifi-setup>`
* An HC-06 Board if you want to connect using Bluetooth

.. _dccpp-operation:

Operation
==========

.. Note:: A Mega is required for using the WiFi connection, but an Uno or Nano will work with the Bluetooth connection.


Using Wifi
-----------

To use Wifi, make sure you have a WiFi enabled Command Station as described in the :doc:`Wifi Setup </ex-commandstation/get-started/wifi-setup>` section.

We have not tested the WiFi implementation yet


***insert tutorial here***

Using Bluetooth
----------------

The Bluetooth connection requires an Android device with Bluetooth capability and a Bluetooth board attached to the Command Station. The setup is similar to how we use a WiFi Shield or an ESP-01s board. It is just a different method to create a wireless serial connection to the CS from another device.

You will need one of these inexpensive HC-06 boards.

***insert tutorial here***
