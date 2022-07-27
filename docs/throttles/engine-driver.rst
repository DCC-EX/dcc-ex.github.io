.. include:: /include/include.rst
.. include:: /include/include-l1.rst
******************
Engine Driver
******************

|conductor|

.. image:: /_static/images/throttles/engine_driver_logo.png
   :alt: Android Logo
   :scale: 60%
   :align: left

**Engine Driver** (ED) is an Android App that uses the WiThrottle\ :sup:`TM` Protocol to either connect directly to the DCC++ EX Command Station or connect to the JMRI WiThrottle Server via WiFi. 

If you wish to connect Engine Driver to JMRI, you need to start the wiThrottle Server and (optionally [#]_) the Web Server in JMRI on the computer running JMRI. The JMRI computer must be connected to the DCC++ EX Command Station using a USB cable. 

If you wish to connect Engine Driver directly to DCC++ EX, you need to add a WiFi option to your DCC++ EX Command Station as explained here: :doc:`WiFi Setup </ex-commandstation/get-started/wifi-setup>`.

.. _ed-platforms:

Platforms
===========

.. image:: /_static/images/throttles/icon_android.png
   :alt: Android Logo
   :scale: 30%
   :align: left


Please visit the Engine Driver Website: https://enginedriver.mstevetodd.com/

`Get 'Engine Driver Throttle' from the Google Play Store <https://play.google.com/store/apps/details?id=jmri.enginedriver>`_

   .. raw:: html
      
      <iframe width="336" height="189" src="https://www.youtube.com/embed/N6TWR7fIl0A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

.. _ed-features:

Standard Features (all wiThrottle servers)
==========================================
* Control one to six locomotives or consists
* Speed and direction control
* Up to 29 DCC functions
* Create and edit consists (software-defined)
* Control layout power, turnouts, routes, and access JMRI web panels and windows
* 'Discover Server' Detect, Select & Connect to WiFi enabled Command Stations
* 'Roster Server' download Engine ID's & function keys from the Command Station
* 'Virtual Engine Sounds' {Bell, Horn, Short Horn, Mute} for motor only decoders, on first two throttles
* Able to use inexpensive bluetooth gamepads for tactile control
* Multiple theme, colours and throttle layout options 

DCC++ Specific or advantageous Features
=======================================
* DCC++EX EXRAIL Automation {Handoff}, Route {Set} and EX-RAIL Command function buttons
* Able to select local images for roster locos
* New 'Request Loco ID' & 'Drive Away' feature from a Program track onto Mainline track with DCC++EX


:doc:`/throttles/driveaway`

.. _ed-screenshots:

Screenshots
============

.. image:: /_static/images/throttles/ed1.png
   :alt: Engine Driver Main Screen
   :scale: 30%
   :align: left

.. image:: /_static/images/throttles/ed2.png
   :alt: Engine Driver 2
   :scale: 30%
   :align: left

.. image:: /_static/images/throttles/ed3.png
   :alt: Engine Driver 3
   :scale: 30%
   :align: left

.. image:: /_static/images/throttles/ed4.png
   :alt: Engine Driver 4
   :scale: 30%
   :align: left

.. rst-class:: clearer

.. _ed-operation:

Operation
===========

https://enginedriver.mstevetodd.com/operation

https://enginedriver.mstevetodd.com/videos

.. TODO:: Give some setup tutorial here. Need a video to match since ED is the top used software

Using a Bluetooth Controller
=============================
This is the one Steve Todd uses himself on a lanyard. It leaves both hands free for paperwork and uncoupling and is light enough to simply let go of when you need both hands. Here are his optimized settings. His prefered settings are listed in the note below. You can use these as a start and customize them for your own use:

.. image:: /_static/images/throttles/bt_controller1.jpg
   :alt: Bluetooth Lanyard Controller
   :scale: 50%
   :align: center

`Wireless Bluetooth Gamepad/Joystick Controller <https://www.ebay.com.au/itm/Wireless-Controller-Rechargeable-Selfie-Remote-Shutter-Gamepad-Joystick-/174852677119>`_

|

And here is another Bluetooth controller that provides extra function buttons and you can hold by placing your finger in the ring.

.. image:: /_static/images/throttles/bt_controller2.jpg
   :alt: Ring Shape Hand Controller
   :scale: 50%
   :align: center
   
`Walmart <https://www.walmart.com/ip/Gamepad-Ring-Shape-Wireless-VR-Joystick-Rechargeable-Bluetooth-compatible-V4-0-Game-Controller/443871148?wmlspartner=wlpa&selectedSellerId=101036302>`_

`AliExpress <https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20220515220821&isPremium=y&SearchText=%22r1%22+bluetooth+game+controller&spm=a2g0o.productlist.1000002.0>`_

.. Note:: From Steve: I set speedsteps to 10, change amount to 1, repeat delay to 9999, horizontal switching layout, throttle web view. I acquire loco/consist using my phone, then dim & lock and put phone in my holster. Then I can "bump" the joystick up and down 3,2,1,0,-1,-2,-3, easily keeping track of the current "notch". 1 is coupling speed, 2 is switching/yard speed, 3 is mainline. If I'm at home, I put the Conductor view in the web and I have my work for each location.

.. image:: /_static/images/throttles/ed_conductor_view1.png
   :alt: Engine Driver Conductor View
   :scale: 15%
   :align: center

====

Footnotes
---------
.. [#] the Web server is required if you want to show the Loco images in Engine Deiver.

* The WiThrottle Protocol is the proprietary protocol developed by Matt Hoffman at https://www.WiThrottle.com
