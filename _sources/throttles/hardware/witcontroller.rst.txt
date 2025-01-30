.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-throttles.rst
************************
WiTcontroller (Physical)
************************

|SUITABLE| |tinkerer| |engineer| |support-button|

.. sidebar:: 
   :class: sidebar-on-this-page

   .. contents:: On this page
      :depth: 2
      :local:

WiTcontroller uses exactly the same hardware as the DccExController, but uses the |WITHROTTLE PROTOCOL| instead of the DCC-EX Native command protocol.

From |Engine Driver|'s very own Peter Akers (flash62au on our Discord server), comes a physical hardware throttle using only 4 parts and a battery:

* ESP32 with LiPo charger
* Rotary encoder
* 3x4 keyboard
* OLED Display

Optionally you can add:

* Up to 8 extra buttons
* A battery monitor

Files for a 3D printed case are also available.

For a video on how to do this, click below:

  .. raw:: html
      
    <iframe width="336" height="189" src="https://www.youtube.com/embed/RKnhfBCP_SQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Features
==========

- Provides a list of discovered SSIDs with the ability to choose one. When you select one:

  - If it is one in your specified list (in the sketch), it will use that specified password 
  - If it is a DCC++EX WiFi Command Station in access Point mode, it will guess the password
  - Otherwise it will ask to enter the password (Use the rotary encoder to choose each character and the encoder button to select it.  * = backspace.  # = enter the password.) 

- Optionally provides a list of SSIDs with the specified passwords (in the sketch) to choose from
- Auto-connects to the first found WiThrottle Protocol Server if only one found, otherwise 

  - Asks which to connect to
  - If none found will ask to enter the IP Address and Port
  - Guesses the WiThrottle IP address and Port for DCC++EX WiFi Access Point mode Command Stations
  - Optionally can add a #define (a preference) to disable this auto connect feature

- Rudimentary on-the-fly consists
- Assign commands directly to the 1-9 buttons (in the sketch) (see list below)

  - This is done in config_button.h
  - Latching / non-latching for the function is provided by the roster entry of WiThrottle server

- Optionally use a potentiometer (pot) instead of the rotary encoder
- Optional ability to assign commands directly to the 1-11 additional buttons (in the sketch) (see list below)

  - These are defined config_button.h

- Command menu (see below for full list) including:

  - Able to select and deselect locos:

    - by their DCC address, via the keypad

      - On NCE systems, a leading zero (0) will force a long address

    - from the first 50 locos in the roster

  - Able to select multiple locos to create a consist

    - Able to change the facing of the additional locos in the consists (via the 'extra' menu after selection)

  - Able to activate any function (0-31)

    - Showing of the roster function labels (from the WiThrottle server if provided)
    - Quick access to the functions by pressing #. Temporarily enabled via the Extras menu (or permanently enabled in config_button.h)
    - Limited ability to configure which functions are sent to the first or all locos in a consist (defined in config_button.h)

  - Able to throw/close turnouts/points:

    - from the address
    - from the first 50 turnouts/points in the server list

  - Able to activate routes:

    - from their address
    - from the first 50 routes in the server list

  - Set/unset a multiplier for the rotary encoder
  - Power Track On/Off
  - Disconnect / Reconnect
  - Put ESP32 in deep sleep and restart it
  - Option to switch between Single Loco and Consist/MU (Drop before Acquire)
  - Option to save the currently select locos (on multiple throttles) and have them automatically re-acquired on next connection.

- Option to have up to 6 command sequences executed on connection
- Option to automatically acquire a loco if there is only one loco in the roster
- Have up to 6 throttles, each with an unlimited number of locos in consist. Default is 2 throttles, which can be increased or decreased temporarily via the Extras menu (or permanently enabled in config_button.h)
- Limited dealing with unexpected disconnects.  It will throw you back to the WiThrottle Server selection screen.
- Boundary between short and long DCC addresses can be configured in config_buttons.h
- The default speed step (per encoder click) can be configured in config_buttons.h
- The controller will automatically shut down if no SSID is selected or entered in 4 minutes (to conserve the battery)


NOTE: This is an open source Project and is therefore always a work in progress. New features are being added regularly.

Source code and instructions can be found on GitHub here: https://github.com/flash62au/WiTcontroller |EXTERNAL-LINK|

Images
========

Here is a connection diagram drawn in Frizing showing how to wire the parts together:

.. figure:: /_static/images/throttles/witcontroller_pinouts.png
   :alt: Basic WiTcontroller connection diagram
   :scale: 30%
   :align: center

   Basic WiTcontroller connection diagram

Here are pictures showing parts placement inside the case:

.. figure:: /_static/images/throttles/witcontroller1.jpg
   :alt: WiTcontroller assembly
   :scale: 50%
   :align: left

   WiTcontroller assembly

.. figure:: /_static/images/throttles/witcontroller2.jpg
   :alt: WitController in case
   :scale: 50%
   :align: left

   WitController in case

|FORCE-BREAK|

Build Variations
----------------

Some of the build variations that are possible...

.. figure:: /_static/images/throttles/witcontroller5.png
   :alt: WiTcontroller Extra Butons
   :scale: 85%
   :align: center

   WiTcontroller Extra Butons

.. figure:: /_static/images/throttles/witcontroller3.jpg
   :alt: WiTcontroller Extra Butons
   :scale: 8%
   :align: center

   WiTcontroller Extra Butons

.. figure:: /_static/images/throttles/witcontroller4.png
   :alt: WiTcontroller Larger Screen
   :scale: 85%
   :align: center

   WiTcontroller Larger Screen






