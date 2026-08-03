# DCCpp CAB

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="2" local=""}
On this page
:::
::::

![Android Logo](/_static/images/throttles/icon_android.png){.align-left}

This is an Android App (with plans for iOS) from Spain. One of the major
benefits of DCCpp CAB is that it speaks the \|DCC-EX Native Commands\|
natively. This means it is fast and can take advantage of some features
that exist in the \|EX-CS\| not implemented in other APIs.

Another benefit is that this throttle can use Bluetooth instead of WiFi
if you choose! There are several advantages to using Bluetooth, the main
one being that Uno and Nano users can use a wireless throttle!

And the website here: [DCCpp Android Cab Infotrokik
Blog](http://lamaquetade.infotronikblog.com/dccppcab/dccppcab_index.html)
\|EXTERNAL-LINK\|

## Features {#dccpp-features}

- Speaks the \|DCC-EX Native Commands\| natively
- Connect via WiFi *or* Bluetooth
- Read and Write CVs
- \|Serial Monitor\| to send manual commands and view the log

## Screenshots

![Dccpp CAB Screenshot 2](/_static/images/throttles/dccpp2.jpg){.align-left}

![Dccpp CAB Screenshot 3](/_static/images/throttles/dccpp3.jpg){.align-left}

::: rst-class
clearer
:::

## Requirements {#dccpp-requirements}

- A \|EX-CS\| (Mega based for WiFi or Mega or Uno/Nano based for
  Bluetooth)
- An Android Cell Phone or Tablet
- A WiFi Shield (or other ESP8622 solution) if you want to connect using
  WiFi
  `Wifi Setup Page </ex-commandstation/diy/wifi-setup>`{.interpreted-text
  role="doc"}
- An HC-06 Board if you want to connect using Bluetooth

## Operation {#dccpp-operation}

:::: note
::: title
Note
:::

A Mega is required for using the WiFi connection, but an Uno or Nano
will work with the Bluetooth connection.
::::

### Using WiFi

To use WiFi, make sure you have a WiFi enabled Command Station as
described in the
`Wifi Setup </ex-commandstation/diy/wifi-setup>`{.interpreted-text
role="doc"} section.

We have not tested the WiFi implementation yet

**\*insert tutorial here**\*

### Using Bluetooth

The Bluetooth connection requires an Android device with Bluetooth
capability and a Bluetooth board attached to the Command Station. The
setup is similar to how we use a WiFi Shield or an ESP-01s board. It is
just a different method to create a wireless serial connection to the
Command Station from another device.

You will need one of these inexpensive HC-06 boards.

**\*insert tutorial here**\*
