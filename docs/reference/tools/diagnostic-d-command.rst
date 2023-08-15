.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-description.rst
|EX-REF-LOGO|

****************************
Diagnostics ``<D>`` Command
****************************

|engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

These commands either enable diagnostics or allow settings to be changed. There are a number of diagnostic facilities under the  ``<D>`` command, most are harmless but caution is advised.

**The** ``<D>`` **commands are intended for diagnostics only which means that their behaviour can change from one release to another without warning**

These commands can be entered directly via the USB serial console or through a Wifi connection to the command station with a tool such as Telnet or Putty. |JMRI| includes the DCC++ traffic monitor which lets you insert serial |DCC-EX Native Commands| as well. (links required)

Speed Step Configuration
========================

``<D SPEED28|SPEED128>`` By default, the Command Station sends speed commands in 128 steps. You can change to 28 speed steps and back again with this command. If speed steps are set to 28, you can still use 128 speed step locos, they will just have a resolution of 28 steps also instead of 128.

``<D CABS>`` Lists the locomotives which the command station is currently managing.

``<D RAM>`` Displays the free RAM on your Arduino. 

The following commands turn ON(1) or OFF(0) various diagnostic traces
======================================================================

``<D ACK ON|OFF>`` trace DCC ACK processing when reading/writing on the prog track. See :doc:`diagnostic-d-ack-command`.

``<D CMD ON|OFF>`` trace received JMRI commands.

``<D WIFI ON|OFF>`` trace Wifi protocol AT command conversation between Arduino and Wifi hardware.

``<D ETHERNET ON|OFF>`` trace Ethernet  conversation between Arduino and Ethernet hardware.

``<D WIT ON|OFF>`` trace WiThrottle protocol conversation of Engine Driver (or other WiThrottle device).
``<D HAL SHOW>`` display information about configured HAL devices (servo controllers, GPIO Extenders) including address and pins used

The following commands might help in exceptional circumstances
===============================================================

``<D PROGBOOST>``  When the programming track is switched on with ``<1>`` or ``<1 PROG>`` it will normally be restricted
to 250mA according to NMRA standards. Some loco decoders require more than this, especially sound versions. ``<D PROGBOOST>``
temporarily removes this limit to allow the decoder more power. The normal limit will be re-imposed when the programming track
is switched off with ``<0>`` or ``<0 PROG>``.

