.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst

|donate-button|

.. index:: 8874, EX-MotorShield

*************************
DCC-EX EX-WiFiShield 8266
*************************

|conductor|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

Designed in conjunction with the |DCC-EX| development team...

.. image:: /_static/images/wifi/exwifi5.png
   :alt: EX-WiFiShield-8266 front
   :scale: 40%
   :align: left

.. image:: /_static/images/wifi/exwifi6.png
   :alt: EX-WiFiShield-8266 back
   :scale: 40%
   :align: left

Overview
===========

The new v1.1 WiFi shield is a joint DCC-EX and Makerfabs project. It comes already flashed with DCC-EX EX-CommandStation compatible firmware and can now be easily updated with an Arduino or USB to TTL Adapter.

The EX-WiFiShield 8266 is a cost-effective and highly integrated UART-WiFi module for DCC-EX and general IoT applications. It comes in a standard Arduino Uno shield format and uses ULP technology (Ultra Low Power).

This WiFi Shield is based on ESP-12F, which is a newer version of the proven ESP8266 chip. With this Shield, you can connect your Command Station to your network, or have it operate as a stand alone Access Point to connect directly from your phone, tablet, laptop, or WiFi hardware throttle.

Features
====================

supports wireless 2.4GHz 802.11 b/g/n supports the STA/AP/STA + AP operation modes Built-in TCP/IP protocol stack, and support for multiple TCP Client connections supports simple AT commands supports UART/GPIO data communication interface supports Smart Link intelligent networking Dimensions: 2.1"(53mm) * 1.9"(47mm) * .9"(23mm)



How can I get one?
==================

Units may be purchased from the following sources you can find here: 'Authorized Dealers / Resellers <../purchasing/dealers/'


Assembly with EX-MotorShield8874
================================

Assembly instructions to come! But the short version is to just connect the shield on top of your Motor Shield and connect the included jumpers from any one of the Tx row of pins to Rx1 on the Mega and a jumper from any of the Rx row pins to the Tx1 header on the Mega.

Next steps
==========

Click :doc:`here </ex-commandstation/get-started/wifi-setup>` to learn how to connect the WiFi shield to your |EX-CS|, or *alternatively* connect a controller like |JMRI| or our |EX-WT| by using the serial cable to connect between your computer and the |EX-CS| as outlined in the :ref:`ex-installer/installing:getting ready` section of the |EX-I| page. Note that when configuring the EX-CommandStation you will want to select `EX8874_SHIELD` as the motor board during configuration.
