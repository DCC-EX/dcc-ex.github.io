:orphan:

.. Remove orphan field when the document is added to a toctree

*********************************
Using the "DriveAway(tm)" Feature
*********************************

DCC++EX and Engine Drivers "Request Loco ID" & “Drive Away" 

A new feature enhancement with a Arduino Mega 2560 +WiFi enabled DCC++EX Command Station directly connected to an Engine Driver Throttle on an Android smartphone. 

Place a DCC Engine on a programming track spur or siding, use Engine Driver WiFi Throttle "Request Loco ID" to automatically acquire & load the loco# into the Engine Driver Throttle, then just throttle-up and "Drive Away" onto the main line tracks.

How to Use It
=============

Place any DCC Engine onto a insulated Programming track setup as spur or siding connected with dual plastic joiners to the Main layout track. On Engine Driver WiFi Throttle, touch "Select" loco as normal, choose "Request Loco ID" radio dial and press "Request Loco" button, it automatically acquires & loads the loco# into the Engine Driver WiFi Throttle, then sets and Joins the Programming track as a Mainline DCC signal, then you just throttle-up and "Drive Away" onto the main line tracks. 

Place a second engine on the programming track and repeat the steps as many times as you would like. 
This is a New DCC WiFi Throttle client feature only found in DCC++EX & Engine Driver WiFi App. 

Where it's used
================

An Arduino Mega DCC++EX + WiFi enabled Command Station in Standalone Operations mode Directly WiFi connected with Engine Driver WiFi Throttles utilizing the new standalone WiThrottle Server feature embedded in DCC++EX Command Station. 

Setup an Arduino Mega DCC++EX CS + ESP 8266 WiFi MakerFab Shield or a ESP01 WiFi board in either Access Point AP mode or Station STA (client) mode through a shared Router for a Command Station (CS) Standalone Operations configuration. Then the Engine Driver and Command Station both sign on to the common SSID Name and Password to share the common WiFi signal and channel. 

This Standalone WiFi configuration works Without the use of any additional PC, Mac or PI hardware or third party software controller's like JMRI or Rocrail interfaces.

How it works
=============

DCC++EX 3.1 and above has a new software implementation logic that in a sense replaces a hardwired DPDT switch and combines multiple DCC++ commands in a sequence to perform the magic dubbed "DriveAway(tm)". It triggers a <R> read the CV1 Short or CV 17 & 18 Long address and CV8 Mfr ID, and CV29 Setup and then returns and automatically loads the Loco# into the WiFi throttle. 
The Command Station then automatically sets ``<1 JOIN>`` command to switch the PROG track to MAIN DCC signal and allows your Engine Driver App to drive it away onto the main line tracks.

Logic Programming Protection;
If you inadvertently touch or send any Programming command while an Engine is sitting on the PROG track when it's active as a [JOIN] Main line track, the DCC++EX software Automatically kicks back to Program Track Mode before accepting any other commands as safety procedure. 


Caution: Wiring Prog & Main
==============================

Please be sure "Both" Programming Track rails are Insulated with dual plastic joiners from the Main line and that both the wiring for CAB A Main and CAB B Prog positive leads are connected on the right rail and the negative leads are connected on the other rails to synchronize the phase of the DCC signal. 
Or else undesirable gremlins may appear, you've been forewarned.
The proceeding is a public service announcement and the DCC++EX team makes no expressed or implied guarantees if the user fails his or her due diligence.


New "Discovered Servers" on WiFi Throttles
===========================================

WiFi Throttles now detect and display both DCC++EX Command Station name and JMRI WiThrottle Server Profile names as 'Discovered Servers' in the WiFi Throttle Apps.

Sample WiFi Throttle App "Discovered Servers"
----------------------------------------------
      “DCC++EX”                 {Direct WiFi connected to the Command Station}

      "My JMRI Railroad”        {JMRI WiFI connected via WiThrottle Server on a PC or Mac}

      "RPi JMRI Railroad”       {JMRI WiFI connected via WiThrottle Server on Raspberry Pi}
      
Our new multicast Dynamic Network Server (mDNS) enhancement allows us to display the available WiFi Server connections to a DCC++EX Command Station. 
Choosing one allows your WiFi Throttle App to connect to and load Server Rosters and function keys to your throttle from Either the DCC++EX Command Station, Or from JMRI Engine Roster.


New DCC++EX 4.0 EXRAIL "Roster" Feature 
========================================

You can now manually enter your ROSTER engine address, names and function keys into your myAutomation.h file and directly pass this Command Stations Engine Roster into your Engine Driver and WiThrottle Apps.  
By choosing “DCC++EX” from discovered servers an Engine Driver or WiThrottle becomes Directly connected to the Command Station and the "Server Roster" radial dial now lists the New DCC++EX EXRAIL "ROSTER" Engines and Function key layout on the Engine Driver or WiThrottles in addition to the standard preset Engine Driver "default mode" function key names.

Current JMRI Engine Rosters
===========================
  
By choosing “My JMRI Railroad” or ”RPi JMRI Railroad” from discovered servers an Engine Driver or WiThrottle is then connected via a {PC, Mac or Pi} JMRI WiThrottle Server to the DCC++EX Command Station and the JMRI Engine Roster & function keys are loaded to your WiFi Throttle App.

Please be sure your JMRI device {Windows, Mac iOS or Raspberry Pi} for JMRI WiThrottle Server is signed on and connected to the same WiFi SSID Name and Password as your WiFi Throttles and then you can choose the JMRI Railroad name or directly enter the JMRI WiThrottle Server IP address: port# displayed into your Engine Driver & WiThrottle Apps.
