:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
**********************************
Using the "DriveAway(tm)" Feature
**********************************

|conductor| |tinkerer| |engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

|EX-CS| and |Engine Driver|'s "Request Loco ID" & “Drive Away" 

A new feature enhancement with a Arduino Mega 2560 +WiFi enabled |EX-CS| directly connected to an Engine Driver Throttle on an Android smartphone. 

Place a DCC Engine on a programming track spur or siding, use |Engine Driver| WiFi Throttle "Request Loco ID" to automatically acquire & load the loco# into the |Engine Driver| Throttle, then just throttle-up and "Drive Away" onto the main line tracks.

How to Use It
=============

Place any DCC Engine onto a insulated Programming track setup as spur or siding connected with dual plastic joiners to the Main layout track. On |Engine Driver| WiFi Throttle, touch "Select" loco as normal, choose "Request Loco ID" radio dial and press "Request Loco" button, it automatically acquires & loads the loco# into the |Engine Driver| WiFi Throttle, then sets and Joins the Programming track as a Mainline DCC signal, then you just throttle-up and "Drive Away" onto the main line tracks. 

Place a second engine on the programming track and repeat the steps as many times as you would like. 
This is a New DCC WiFi Throttle client feature only found in |EX-CS| & |Engine Driver| WiFi App. 

Where it's used
================

An Arduino Mega |EX-CS| + WiFi enabled Command Station in Standalone Operations mode Directly WiFi connected with Engine Driver WiFi Throttles utilizing the new standalone WiThrottle Server feature embedded in |EX-CS|. 

Setup an Arduino Mega |EX-CS| + ESP 8266 WiFi MakerFab Shield or a ESP01 WiFi board in either Access Point AP mode or Station STA (client) mode through a shared Router for a Command Station (CS) Standalone Operations configuration. Then the |Engine Driver| and Command Station both sign on to the common SSID Name and Password to share the common WiFi signal and channel. 

This Standalone WiFi configuration works Without the use of any additional PC, Mac or PI hardware or third party software controller's like JMRI or Rocrail interfaces.

How it works
=============

|EX-CS| version 3.1 and above has a new software implementation logic that in a sense replaces a hardwired DPDT switch and combines multiple DCC++ commands in a sequence to perform the magic dubbed "DriveAway(tm)". It triggers a <R> read the CV1 Short or CV 17 & 18 Long address and CV8 Mfr ID, and CV29 Setup and then returns and automatically loads the Loco# into the WiFi throttle. 
The Command Station then automatically sets ``<1 JOIN>`` command to switch the PROG track to MAIN DCC signal and allows your |Engine Driver| App to drive it away onto the main line tracks.

Logic Programming Protection;
If you inadvertently touch or send any Programming command while an Engine is sitting on the PROG track when it's active as a [JOIN] Main line track, the |EX-CS| software Automatically kicks back to Program Track Mode before accepting any other commands as safety procedure. 

Caution: Wiring Prog & Main
==============================

Please be sure "Both" Programming Track rails are Insulated with dual plastic joiners from the Main line and that both the wiring for CAB A Main and CAB B Prog positive leads are connected on the right rail and the negative leads are connected on the other rails to synchronize the phase of the DCC signal. 
Or else undesirable gremlins may appear, you've been forewarned.
The proceeding is a public service announcement and the |DCC-EX| team makes no expressed or implied guarantees if the user fails his or her due diligence.

New "Discovered Servers" on WiFi Throttles
===========================================

WiFi Throttles now detect and display both |EX-CS| name and JMRI WiThrottle Server Profile names as 'Discovered Servers' in the WiFi Throttle Apps.

Sample WiFi Throttle App "Discovered Servers"
----------------------------------------------
      “DCC-EX”                 {Direct WiFi connected to the Command Station}

      "My JMRI Railroad”        {JMRI WiFI connected via WiThrottle Server on a PC or Mac}

      "RPi JMRI Railroad”       {JMRI WiFI connected via WiThrottle Server on Raspberry Pi}
      
Our new multicast Dynamic Network Server (mDNS) enhancement allows us to display the available WiFi Server connections to a |EX-CS|. 
Choosing one allows your WiFi Throttle App to connect to and load Server Rosters and function keys to your throttle from Either the |EX-CS|, Or from JMRI Engine Roster.

.. image:: /_static/images/jmri/engine_driver_discovered_servers.png
  :alt: Engine Driver Discovered Servers
  :scale: 25%
  :align: left


New EX-CommandStation 4.0 EXRAIL "Roster" Feature 
=================================================

You can now manually enter your ROSTER engine address, names and function keys into your myAutomation.h file and directly pass this Command Stations Engine Roster into your |Engine Driver| and |WiThrottle| Apps.  
By choosing “DCC-EX” from discovered servers an |Engine Driver| or |WiThrottle| becomes Directly connected to the Command Station and the "Server Roster" radial dial now lists the New DCC-EX EXRAIL "ROSTER" Engines and Function key layout on the |Engine Driver| or WiThrottles in addition to the standard preset |Engine Driver| "default mode" function key names.

Sample Roster entry in myAutomation.h file

.. code-block:: cpp

  // New EXRAIL 4.0 Engine Server Roster Entries. 
  // The JMRI counter part would be the Roster Screen and the LABLES tab where you define a function key name

  // EXRAIL Defined Engine ROSTER(dcc_address,"name/F1/*F2/etc") // Use asterisk* for function keys that are unlatched i.e. Horn & Whistle
    ROSTER(1204,"RG 1204","Lights/Bell/*Whistle/Coupler/Steam/Dim Lght/Fx6/Sql Brake/Mute/StartUp/ShutDown/////Switching Shunting")
    ROSTER(1224,"PE 1224","") // Motor Only DCC Decoder, Use the Virtual Sound Decoder in Engine Driver Loco Sounds
    ROSTER(1225,"PE 1225","Lights/Bell/*Whistle/*Short Whistle/Steam/On-Time/FX6 Bell Whistle/Dim Light/Mute")
    ROSTER(  70,"3M 70","Lights/Bell/*Horn/Coupler/F4/F5/Fx6/F7/Mute")

  // Legacy Analog DC Engines, Note; Functions F1-F3 & 'Mute' Sounds are available via Engine Driver v2.32+ 'Preferences > Loco Sounds'
    ROSTER(1,"CAB 1","")    // Analog DC Engine with no F-Keys 'See Engine Driver for F-keys'
    ROSTER(2,"CAB 2","")    // Analog DC Engine with no F-Keys
    ROSTER(667, "NH 667","")// Analog DC Engine with no F-Keys

.. image:: /_static/images/jmri/engine_driver_dcc-ex_server_roster.png
  :alt: Engine Driver EX-CommandStation Server Roster
  :scale: 25%
  :align: left

.. image:: /_static/images/jmri/ed_and_dcc-ex_with_dc_and_dcc_throttles.png
  :alt: ED & EX-CommandStation with DC & DCC Throttles
  :scale: 25%
  :align: left

Current JMRI Engine Rosters
===========================
  
By choosing “My JMRI Railroad” or ”RPi JMRI Railroad” from discovered servers an |Engine Driver| or |WiThrottle| is then connected via a {PC, Mac or Pi} JMRI WiThrottle Server to the |EX-CS| and the JMRI Engine Roster & function keys are loaded to your WiFi Throttle App.

Please be sure your JMRI device {Windows, Mac iOS or Raspberry Pi} for JMRI WiThrottle Server is signed on and connected to the same WiFi SSID Name and Password as your WiFi Throttles and then you can choose the JMRI Railroad name or directly enter the JMRI WiThrottle Server IP address: port# displayed into your |Engine Driver| & |WiThrottle| Apps.

.. image:: /_static/images/jmri/engine_driver_jmri_server_roster.png
  :alt: Engine Driver JMRI Server Roster
  :scale: 25%
  :align: left

.. image:: /_static/images/jmri/engine_driver_and_dcc-ex.png
  :alt: Engine Driver & EX-CommandStation
  :scale: 25%
  :align: left
