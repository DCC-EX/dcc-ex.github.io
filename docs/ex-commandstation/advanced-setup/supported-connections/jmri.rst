.. include:: /include/include.rst
.. include:: /include/include-l3.rst
|EX-CS-LOGO|

**************************
JMRI Connection
**************************

|tinkerer| |engineer|


.. todo:: JMRI Connection.  actually uses one of the of the other connection types so not sure it needs to be here as a separate page

Connection Type: Direct to Command Station or through JMRI
============================================================

Everything on this page seems to come in twos! You have two options for connecting your controller to your Command Station depending on its capabilities and your preferences:

* Connect directly to |EX-CS| using WiFi or Bluetooth (|JMRI| not required but optional)
* Connect to the |EX-CS| through |JMRI| with the USB cable, and connect a |WiThrottle Protocol| compatible throttle to JMRI's |WiThrottle Server| via WiFi

If you don't need |JMRI|, or just want to connect your wireless controller directly to the |EX-CS|, then you connect to the Command Station using a WiFi or Bluetooth device that speaks either the <DCC++> command language, or the |WiThrottle Protocol| command language. 

For example, |Engine Driver| uses the |WiThrottle Protocol|, so it can connect either directly to the |EX-CS| via WiFi, or indirectly through the JMRI computer that has WiFi and its own |WiThrottle Server|. DCCpp CAB can connect directly to the |EX-CS| via WiFi or Bluetooth, and sends native <DCC++> commands.