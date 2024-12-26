.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-csb1.rst
  
|EX-CS-LOGO| |donate-button|

.. index:: EXCSB1, EX-CSB1

**********************************
EX-CSB1 Quick Setup Guide
**********************************

|SUITABLE| |conductor| |tinkerer| |engineer| |support-button|

.. sidebar::

   .. contents:: On this page
      :depth: 4
      :local:

|EX-CSB1|

This quick startup guide is designed to have you configured and setup to run trains in 5 minutes. After all, the point is to enjoy running trains, not sifting through more information than you need until you are ready. 

These instructions are for DCC locomotives. For more detailed information, to configure for running DC trains, or to use different throttles like |EX-WT| or |JMRI|, see the :doc:`EX-CSB1 Operating Manual <rtr-manual>`

What You Will Need
==================

* An |EX-CSB1| [#c1]_
* A **Power supply** (12V - 16V DC see :ref:`Power Supplies <reference/hardware/power-supplies:power supplies>`)
* A **DCC loco** (If you are here to run DC locos, please go to the :doc:`/trackmanager/index` page.)
* Some **Track**
* **16 to 28AWG/1.5mm^2 Wire**, preferably in 2 colours with 1/8"/6mm insulation stripped (and wire tinned if stranded)
* Jeweller's **flat bladed screwdriver** (1.5 - 2mm blade)
* A **WiFi capable smart device** like a phone or tablet to control your trains (aka a "Throttle")

 .. [#c1] While not required for normal use, a PC is required a) to initially install the software on a DIY system, b) is optional for making a USB connection and using programs like |EX-WT| or |JMRI|, and c) to update/add |EX-R| Scripts to the |EX-CS| or make other changes to its configuration. |BR| A USB connection also provides a connection to a "serial monitor" to generate logs and diagnose issues. But more on that later.

----

Board Layout
============

.. figure:: /_static/images/ex-csb1/csb1_render_layout_top.png
   :alt: DCC-EX EX-CSB1 Express
   :scale: 42%

   EX-CSB1 top (click image to enlarge it)

A full explanation of the board is available in the :doc:`manual </ex-commandstation/rtr-manual>`.

.. warning::

   **Start with all power disconnected!!**
   
   Before connecting any wires to your command station or tracks, make sure you have unplugged the power supply from the wall or removed the barrel connector from the command station. 
   
   It is crucial to ensure that the command station has no power while you are working on your connections.

----

Summary or Super-Quick Start
============================

In summary, you need just two basic wiring connections to the |EX-CSB1| to be up and running trains:

.. XXX Add link above to point to the full manual

1. Track connected to Track A Output
2. Power supply input connected to Power IN DC barrel jack

.. sidebar:: Engine Driver & EX-Toolbox

   There are quite a few custom features in |Engine Driver| and |EX-TB|. It may be worth getting a cheap Android phone or tablet just to be able to use those apps

And to connect via WiFi to the |EX-CSB1-SHORT| to control trains your smart device will need either:

* |Engine Driver| or |EX-TB| for Android
* |WiThrottle| for Apple iOS

|HR-DASHED|

These are the most basic steps to get you up and running.  If you need more help, then remainder of this page explains these steps in much greater detail.

**Steps**

   **1. Connect your EX-CSB1 to your track**

      Connect your main track to the ``A`` **MAIN** output to your Command Station. 

   **2. Connect power to your EX-CSB1**

      The |EX-CSB1-SHORT| has a 2.1mm x 5.5mm power jack. Connect this to an appropriate DC power supply.

      For N and HO scale you would normally use a 12V to 15V DC power supply, but be sure to check the manual for your loco/decoder combination for the correct voltage. 

   **3. Connect Your Smart Device(Phone) to the 'DCCEX_xxxxx' WiFi Network**

      An Android Phone or Tablet or Apple iOS Phone or Tablet can be used.

      * Open the Wifi Settings in your smart device.
      * Select the WiFi network in your smart device WiFi settings named ``DCCEX_xxxxxx``, and use the corresponding password ``PASS_xxxxxx`` (where **xxxxxx** is identical in each case) which is shown on your EX-CSB1's OLED display.
      * Tell your smart device not to worry about there being no Internet connection. [2]_

      .. [2] You also may need to tell your smart device to not automatically connect to your default WiFi network or it might keep trying to reconnect to that instead

   **4. Connect Your Controller (Throttle) App to the 'dccex' Server**

      * Launch your throttle app.
      * In your throttle app, connect to the ``dccex`` server.

   **5. Acquire a Loco in Your Controller (Throttle) App**

      * Place a working DCC equiped loco, with a known DCC Address, on the track 
      * Acquire that loco using its DCC Address

   **6. Run Trains**

      * Run/control the loco

These quick tips may have been be enough to get your running, but step by step instructions follow below.

----

Connecting your Command Station 
===============================

Track Connection
-----------------

There are 2 track output power connectors marked ``A`` and ``B``. In the standard DCC-EX configuration of a |EX-CSB1-SHORT|, ``A`` is configured for DCC **MAIN** operation, and ``B`` is configured for **PROG** or programming track output. 

We recommend connecting your track to the ``A`` **MAIN** output initially to test your Command Station. 

To alter this default configuration of |DCC| outputs, or for |DC| Mode, you would need to configure outputs with a |TM| command in the ``mySetup.h`` file or by creatine a 'Route'. See the :doc:`TrackManager page </trackmanager/index>` for details.

.. figure:: /_static/images/ex-csb1/ab_outputs.png
   :alt: Track A and B Outputs
   :scale: 90%
   :align: center

   Track A and B Outputs

The pluggable male screw terminals accept to 16 to 28 AWG/1.5mm^2 gauge solid or stranded wire. 

If you use stranded wire, we recommend "tinning" the ends of the wire to make a good connection and ensure that stray wire whiskers don't stray outside the screw terminals and cause a short circuit. 

.. sidebar:: Wire gauge
   
   See :doc:`/reference/hardware/wire-gauge` for more information or wire gauge.

Larger wire can handle more current and provide less resistance.  18-22 AWG usually good. Keep your wires short by mounting the Command Station close to the track. 

Using a small flat-bladed screwdriver, loosen both screws on the MAIN (A) Track Output being careful not to screw them all the way out. The screws just need to be loosened enough to fit your wires into the holes. Tighten down both screws once you have inserted the wires making sure to not overtighten. 

You can pull the connector out of its socket to remove it from the |EX-CSB1-SHORT| to make this easier. Remember push the connector all the way into the connector on the board to snap it back in place.

.. figure:: /_static/images/ex-csb1/csb1_insert_wire3.png
   :alt: Inserting Track Wires
   :scale: 40%
   :align: center

   Inserting wires

.. figure:: /_static/images/ex-csb1/csb1_insert_wire4.png
   :alt: Tightening Screws
   :scale: 40%
   :align: center
   
   Tightening Screws

.. figure:: /_static/images/ex-csb1/csb1_insert_wire.png
   :alt: Unplugging connector to insert wires
   :scale: 40%
   :align: center

   Optionally unplugging connector to insert wires

.. figure:: /_static/images/ex-csb1/csb1_insert_wire2.png
   :alt: Wires properly inserted
   :scale: 40%
   :align: center
   
   Wires properly inserted and plug inserted

.. NOTE:: The power connection to your track will be either wires you solder yourself to the rails or via a power connector that plugs into track (such as Kato Unitrack). We will leave it up to you to determine the proper connection to your track. 

Connect the other ends of the track output wires to your track. While not critical at this stage when using DCC. It is best to keep to a standard where the RED wire (or striped wire) is connected to the outside rail of the track to make things easier when using feeders to track sections or adding reversing loops. 

.. todo XXX need to mention DC here with a link?

.. figure:: /_static/images/ex-csb1/track_power_conn_1.jpg
   :alt: Connecting Wires to Track
   :scale: 80%
   :align: center
   
   Connecting Wires to Track

.. todo Add more on WiFi here XXX and More on this below XXX

Power Connection
------------------

The |EX-CSB1-SHORT| has a 2.1mm x 5.5mm power jack. If you already have a power supply with bare wires, you can use an optional 2.1mm x 5.5mm screw terminal block adapter. 

For N and HO scale you would normally use a 12V to 15V DC power supply, but be sure to check the manual for your loco/decoder combination for the correct voltage. 

For more information about power supplies, including how to use one power supply to supply all the different voltages on your layout, see :ref:`Power Supplies <reference/hardware/power-supplies:power supplies>`. 

.. figure:: /_static/images/power/2_1mm_screw_terminal_adapter.png
   :scale: 40%
   :align: left
   :alt: 2.1mm screw terminal adapter

   2.1mm Screw Terminal Adapter

.. figure:: /_static/images/power/12v-3A-brick.png
   :alt: 12V 3A brick power supply
   :scale: 100%
   :align: center

   12V/3A Power Supply

|force-break|

Testing Your Command Station
============================

Connect Track Input Power
-------------------------

To fully power the |EX-CSB1|, just plug your power supply into the mains power (aka wall outlet) and connect the barrel end to the Command Station. 

Make sure your power supply matches the needs of your setup: the voltage should be between 12V and 25V DC, depending on the scale of your locomotives, and it should provide at least 2A of current with good over-current performance and voltage stability. 

To get the most out of your |EX-CSB1-SHORT| we suggest using a modern switching power supply with 4A or more. For Z scale, 12V is usually enough, but for N, HO, and OO scales, we recommend using between 14V and 16V DC. 

It's important that your DC power is well-regulated which is why we suggest a modern switch-mode power supply with double insulation and strong overload protection.

.. figure:: /_static/images/ex-csb1/csb1_barrel_insert.png
   :alt: Inserting barrel plug
   :scale: 40%
   :align: center

   Inserting Power Supply Barrel Plug

When you connect power to the |EX-CSB1-SHORT| via the barrel connector, you should see both bright green power LEDs light up (5V and 3.3V power), confirming that the electronics are working. 

However, for safety, track output power will be off by default when you first plug in the |EX-CSB1-SHORT|. This is to prevent power from accidentally being applied to your layout before everything is ready. If you prefer, you can change this default setting in the :doc:`Startup Configuration </ex-commandstation/advanced-setup/startup-config>`. 

.. figure:: /_static/images/ex-csb1/csb1_power_barrel.png
   :alt: Barrel Power LEDs
   :scale: 40%
   :align: center

   Barrel Plug Power LEDs

You should see status information on the display including the |EX-CSB1-SHORT| firmware version, track power status, free memory, and WiFi connection information. 

If you do not have a display, you will need to connect a |serial monitor| to see the status, but this is not essential for ongoing use of the system. (See: :doc:`Using a Serial Monitor </reference/tools/serial-monitor>`).

.. todo XXX insert link to serial monitor

.. figure:: /_static/images/ex-csb1/csb1_oled.png
   :alt: OLED Status Display
   :scale: 40%
   :align: center

   OLED Status Display

Connecting Your Throttle (controller)
-------------------------------------

Connect the Smart Device to the EX-CSB1 AP Network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /_static/images/ex-csb1/oled_startup.png
   :alt: EX-CSB1 Startup - OLED screen
   :scale: 25%
   :align: right

   EX-CSB1 Startup - OLED screen

The |EX-CSB1| will power up in WiFi **Access Point mode** as configured out of the box, with its own unique WiFi network SSID of ``DCCEX_xxxxxx`` and password of ``PASS_xxxxxx`` (where **xxxxxx** is the last 6 digits of the MAC address of the |EX-CSB1-SHORT|), both of which will be visible on the OLED display (or |serial monitor| log). After it boots you can connect with a WiFi throttle like |Engine Driver| or |WiThrottle|. 

This quick start covers initial testing with the |Engine Driver| app, though it is a broadly similar process when using any other throttle app on a Smart device. 

For a USB Connection with |EX-WT| or |JMRI| and a computer, please see the full :doc:`CSB1 operating manual <rtr-manual>`.

**Access Point (AP) mode** creates a separate WiFi network on the Command Station itself, whereas **Station (STA) mode** allows the Command Station to join as a WiFi device on your home or layout WiFi network. We have the |EX-CSB1-SHORT| set to default to **Access Point (AP) mode** for the convenience of being able to get up and running quickly. 

To configure your |EX-CSB1-SHORT| to connect to your home network, see :doc:`WiFi Configuration </ex-commandstation/advanced-setup/supported-wifi/wifi-config>`.

The WiFi LED will illuminate once WiFi is configured and ready as an Access Point (or Station if reconfigured for STA mode.)

In your smart device's system WiFi settings, select the network settings and find an available network that begins with "DCCEX\_".

.. figure:: /_static/images/engine_driver/ed_wifi_select1.png
   :alt: Smart Device Available Network Screen
   :scale: 40%
   :align: center

   Smart Device Available Networks Screen

Click on that network to see the next screen to enter your password. Notice the password is just "PASS\_" followed by the same 6 digits in the network name (called a "SSID").

.. figure:: /_static/images/engine_driver/ed_wifi_pass.png
   :alt: Smart Device AP Password Entry
   :scale: 40%
   :align: center

   Smart Device AP Password Entry

.. todo XXX We need to probably link to the manual or another EX-CSB1 doc and cover using installer as preferred to the IDE


.. todo [insert link] XXX figure link showing WiFi LED

Run the Engine Driver Setup Wizard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the |Engine Driver| app on your Android smart device: 

.. figure:: /_static/images/engine_driver/ed_ed_icon.png
   :alt: Engine App Icon
   :scale: 45%
   :align: center

   Engine Driver App Icon

The very first time the app is launched the "Welcome to Engine Driver" **Intro/Setup Wizard** is shown. The wizard will ask to grant the app the required permissions and allow you to select some basic preferences for the theme and throttle layout. 

If you have already used |Engine Driver|, you can run the wizard again at any time from the app menu (from the 'Connection' screen only). Any settings from previous runs of the wizard will be maintained.

.. figure:: /_static/images/engine_driver/ed_preferences1.png
   :alt: Engine Driver App Menu
   :scale: 45%
   :align: left

   Engine Driver App Menu

.. figure:: /_static/images/engine_driver/ed_wizard_menu.png
   :alt: Engine Driver Intro/Setup Wizard
   :scale: 45%
   :align: center

   Engine Driver Intro/Setup Wizard

The Wizard allows you to set or change appearance options and, most importantly, choose to use |DCC-EX native commands| instead of |WiThrottle Protocol|:

.. figure:: /_static/images/engine_driver/ed_wizard1.png
   :alt: Engine Driver Wizard Opening Screen
   :scale: 45%
   :align: center

   Engine Driver Wizard Opening Screen

Scroll through the other screens setting your preferences until you get the the DCC-EX screen and make sure to select the option to use an EX-CommandStation. 

This setting will automatically add useful buttons and switch to using the |DCC-EX native commands| instead of |WiThrottle Protocol| (you can always switch back and forth if you need to connect to a WiThrottle specific device):

.. figure:: /_static/images/engine_driver/ed_wizard6.png
   :alt: Engine Driver Wizard DCC-EX Select
   :scale: 45%
   :align: center

   Engine Driver Wizard DCC-EX Select

After choosing the DCC-EX option above and pressing the checkmark to finish the Wizard, the opening |Engine Driver| screen will change to look like *Figure: DCC-EX Protocol Bottom Selector* below with an added option at the bottom of the screen for 'Connection Protocol'. 

'Auto' for Automatic is now the default. 

You can manually switch between |DCC-EX Native Protocol| and |WITHROTTLE PROTOCOL| if you go to a club or use another type of Command Station that requires the |WITHROTTLE PROTOCOL|, but generally the 'Auto' setting will do so automatically.

The |DCC-EX Native protocol| allows for more powerful, expanded capabilities when connected to an |EX-CS|:

.. figure:: /_static/images/engine_driver/ed_dcc_ex_protocol1.png
   :alt: DCC-EX Protocol Bottom Selector
   :scale: 45%
   :align: left

   DCC-EX Protocol Bottom Selector

.. figure:: /_static/images/engine_driver/ed_dcc_ex_protocol2.png
   :alt: DCC-EX Protocol Menu
   :scale: 45%
   :align: center

   DCC-EX Protocol Menu

|BR|

Connect Engine Driver to EX-CommandStation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|Engine Driver| should find the Command Station automatically and show it's SSID in the 'Discovered Servers' List. Simply select yours by clicking on it. The last 6 characters of the SSID will be unique to your Command Station. 

If the list is empty, try entering it manually by putting ``192.168.4.1`` in the 'Server Address' and ``2560`` for the 'Port'. If that still does not work, see the Section on WiFi here todo XXX.

.. figure:: /_static/images/engine_driver/ed_detect_2.png
   :alt: Command Station Connect
   :scale: 45%
   :align: center

   Command Station Connect

Acquire Your Loco
^^^^^^^^^^^^^^^^^

Once you have connected to your command station, the next screen will display the throttle controls. They will be greyed out until you select a loco to control. 

Press the :guilabel:`select` button and enter the address for your loco. Here you can see we are acquiring loco `3` (the default address for almost all locos as they come from the box). 

   (Once you are happy that your |EX-CS| is fully functioning you can change the DCC address of your locos using :ref:`these instructions<throttles/software/engine-driver-native-protocol:read and write dcc addresses on the programming track>`.)

.. figure:: /_static/images/engine_driver/ed_select_addr.png
   :alt: Press Loco Select Button
   :scale: 45%
   :align: left

   Press Loco Select Button

.. figure:: /_static/images/engine_driver/ed_select_addr2.png
   :alt: Acquire Loco by its Address
   :scale: 45%
   :align: center

   Acquire Loco by its address

|BR|

The throttle screen reappears and the controls are active. You will also see 3 icons at the top of the display, a special DCC-EX button, an 'emergency stop' button, and a 'track power' button. 

Press the red 'power' button to turn on the track power, the button should turn green and your track power should be on (the track output LEDs on your motor driver should light).

.. figure:: /_static/images/engine_driver/ed_powr_btn_shadow.png
   :alt: Turn On Track Power
   :scale: 60%
   :align: center

   Turn On Track Power

Run Trains
^^^^^^^^^^

Move the slider control up slowly, operate the horn and light buttons, and you should be running trains! 

.. figure:: /_static/images/engine_driver/ed_run.png
   :alt: Operate Controls to Run Trains
   :scale: 45%
   :align: center

   Operate Controls to Run trains

----

Additional information
======================

Confirm startup
----------------

.. figure:: /_static/images/ex-csb1/oled_startup.png
   :alt: EX-CSB1 Startup - oLED screen
   :scale: 25%
   :align: center

   EX-CSB1 Startup - OLED screen

... todo XXX [insert link] Show and explain the startup screen. What goes here?

At startup of the |EX-CSB1| the OLED screen shows useful information.

.. list-table::
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Line 
    - key
    - Meaning

  * - 1
    - DCC-EX
    - EX-CommandStation version number

  * - 2
    - Lic
    - The licence under which the EX-CommandStation code is published

  * - 3
    - Power
    - Power State.  ON / OFF / JOIN / etc.

  * - 4
    - Free RAM
    - Available RAM

  * - 5
    - Wifi:
    - The SSID / Network name

  * - 6
    - PASS:
    - The password for the Network

  * - 7
    - IP:
    - The IP Address of the WiThrottle / Native server

|HR-DASHED|

DCC Operation
---------------

The |EX-CSB1| is set to operate in |DCC| mode by default. If you want to switch to any of the outputs to |DC| mode, you can find instructions on how to do that on the :doc:`TrackManager page </trackmanager/index>`.

|HR-DASHED|

Booster Mode
--------------

The |EX-CSB1| as the name implies can operate as a Command Station or a Booster. See [insert link] for instructions on how to use the EX-CSB1 as a booster.

|HR-DASHED|

Full EX-CSB1 Operating Manual
------------------------------

:doc:`rtr-manual`
`design files <https://github.com/DCC-EX/EX-CSB1>`_ |EXTERNAL-LINK|

----

Next Steps
==========

If you are happy with the default configuration of your |EX-CSB1| there is nothing more you need to do.

If you want to change the way the WiFi is configured, just click next or go the :doc:`rtr-wifi-setup` page.

If you want to look at some other options to use as a controller (throttle) then have a look at the :doc:`/ex-commandstation/controllers-rtr` page.

If you want to add a roster, turnout/points, routes or automations look at the :doc:`/exrail/index` page.
