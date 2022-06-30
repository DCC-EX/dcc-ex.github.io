*************************
WiTcontroller (Physical)
*************************

From WiThrottle's very own Peter Akers (flash62au on our Discord server), comes a physical hardware throttle using only 4 parts:

* ESP32 with LiPo charger
* rotary encoder
* 3x4 keyboard
* OLED Display

Files for a 3D printed case are also available.

For a video on how to do this, click below:

  .. raw:: html
      
    <iframe width="336" height="189" src="https://www.youtube.com/embed/S2UfglFeOH8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Features
==========

* Connects to the first available SSID (of three you can specify) with the specified password
* Auto-connects to the first found wiThrottle Protocol Server if only one found, otherwise askes which to connect to
* Rudimentary on-the-fly consists
* Assign commands directly to the 1-9 buttons (see list below)
* Command menu (see below for full list) including:
  - Able to select and deselect locos by their DCC address, via the keypad
  - Able to select from the first 10 locos in the roster
  - Power Track On/Off
  - Disconnect / Reconnect
  - Put ESP32 in deep sleep and restart it

NOTE: This is a Project and is therefore a work in progress and open source. New features are being added regularly and a full tutorial will be available soon in the projects section.

Source code and instructions can be found on GitHub here: https://github.com/flash62au/WiTcontroller


