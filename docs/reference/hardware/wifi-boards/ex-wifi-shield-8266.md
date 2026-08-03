\|donate-button\|

# DCC-EX EX-WiFiShield 8266

\|SUITABLEx\| \|conductorx\| \|tinkererx\| \|engineerx\|
\|support-buttonx\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="1" local=""}
On this page
:::
::::

Designed in conjunction with the \|DCC-EXx\| development team\...

![EX-WiFiShield-8266 front](/_static/images/wifi/exwifi5.png){.align-left}

## Overview

The new v1.1 WiFi shield is a joint DCC-EX and Makerfabs project. It
comes already flashed with DCC-EX EX-CommandStation compatible firmware
and can now be easily updated with an Arduino or USB to TTL Adapter.

The EX-WiFiShield 8266 is a cost-effective and highly integrated
UART-WiFi module for DCC-EX and general IoT applications. It comes in a
standard Arduino Uno shield format and uses ULP technology (Ultra Low
Power).

This WiFi Shield is based on ESP-12F, which is a newer version of the
proven ESP8266 chip. With this Shield, you can connect your Command
Station to your network, or have it operate as a stand alone Access
Point to connect directly from your phone, tablet, laptop, or WiFi
hardware throttle.

## Features

supports wireless 2.4GHz 802.11 b/g/n supports the STA/AP/STA + AP
operation modes Built-in TCP/IP protocol stack, and support for multiple
TCP Client connections supports simple AT commands supports UART/GPIO
data communication interface supports Smart Link intelligent networking
Dimensions: 2.1\"(53mm) \* 1.9\"(47mm) \* .9\"(23mm)

## How can I get one?

Units may be purchased from the sources you can find here:
`/purchasing/dealers`{.interpreted-text role="doc"}

## Assembly with EX-MotorShield8874

Assembly instructions to come! But the short version is to just connect
the shield on top of your Motor Shield and connect the included jumpers
from any one of the Tx row of pins to Rx1 on the Mega and a jumper from
any of the Rx row pins to the Tx1 header on the Mega.

\|HR-HEAVYx\|

## Next steps

See the `/ex-commandstation/diy/wifi-setup`{.interpreted-text
role="doc"} page to learn how to connect the WiFi shield to your
\|EX-CSx\|, or *alternatively* connect a controller like \|JMRIx\| or
our \|EX-WTx\| by using the serial cable to connect between your
computer and the \|EX-CSx\| as outlined in the
`ex-installer/installing:getting ready`{.interpreted-text role="ref"}
section of the \|EX-Ix\| page. Note that when configuring the
EX-CommandStation you will want to select [EX8874_SHIELD]{.title-ref} as
the motor board during configuration.
