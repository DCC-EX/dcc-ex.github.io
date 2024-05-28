.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-throttles.rst
**************************
DccEXcontroller (Physical)
**************************

|tinkerer| |engineer| |support-button| 

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:


DccExController uses exactly the same hardware as the WiTcontroller, but uses the DCC-EX Native command protocol instead of the WiThrottle protocol.

From |Engine Driver|'s very own Peter Akers (flash62au on our Discord server), comes a physical hardware throttle using only 4 parts:

* ESP32 with LiPo charger
* rotary encoder
* 3x4 keyboard
* OLED Display

Files for a 3D printed case are also available.

For a video on how to do this, click below:

  .. raw:: html
      
    <iframe width="336" height="189" src="https://www.youtube.com/embed/RKnhfBCP_SQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Features
==========

* provides a list of discovered SSIDs with the ability to choose one. When you select one:
  
  * if it is one in your specified list, it will use that specified password 
  * if it is a |EX-CS| in Access Point mode, it will guess the password
  * otherwise it will only connect if the password is blank

* Optionally provides a list of SSIDs with the specified passwords (in the sketch) to choose from
* Auto-connects to the first found Server if only one found, otherwise:

  * asks which to connect to
  * if none found will ask to enter the IP Address and Port
  * Guesses the IP address and Port for |EX-CS| WiFi Access Point mode Command Stations

* Rudimentary on-the-fly consists
* Assign commands directly to the 1-9 buttons (in the sketch)
* Command menu including:
  
  * Able to select and deselect locos 
    
    * by their DCC address, via the keypad
    * from the first 50 locos in the roster
  
  * Able to throw/close turnouts/points
  * Able to activate routes  
  * set/unset a multiplier for the rotary encoder
  * Power Track On/Off
  * Disconnect / Reconnect
  * Put ESP32 in deep sleep and restart it

* limited dealing with unexpected disconnects.  It will throw you back to the Server selection screen.

NOTE: This is a Project and is therefore a work in progress and open source. New features are being added regularly.

Source code and instructions can be found on GitHub here: https://github.com/flash62au/DccExController

Images
========

Here is a connection diagram drawn in Frizing showing how to wire the parts together:

.. image:: /_static/images/throttles/witcontroller_connect.png
   :alt: WiTcontroller connection diagram
   :scale: 10%
   :align: center

Here are pictures showing parts placement inside the case:

.. image:: /_static/images/throttles/witcontroller1.jpg
   :alt: WiTcontroller assembly
   :scale: 50%
   :align: left

.. image:: /_static/images/throttles/witcontroller2.jpg
   :alt: WitController in case
   :scale: 50%
   :align: left





