:orphan:

.. Remove orphan field when the document is added to a toctree

******************************
Using the "DriveAway" Feature
******************************

DCC++EX and Engine Drivers "Request Loco ID" & “Drive Away" 

A new feature enhancement with a Arduino Mega 2560 +WiFi enabled DCC++EX Command Station directly connected to an Engine Driver Throttle on an Android smartphone. 

Place a DCC Engine on a programming track spur or siding, use Engine Driver WiFi Throttle "Request Loco ID" to automatically acquire & load the loco# into the Engine Driver Throttle, then just throttle-up and "Drive Away" onto the main line tracks.

How to Use It
=============

Place any DCC Engine on an insulated Programming track setup as spur or siding connected with dual plastic joiners to the Main layout track. On Engine Driver WiFi Throttle, touch "Select Loco" as normal, choose "Request Loco ID" radio dial and press "Request Loco" button, it automatically acquires & loads the loco# into the Engine Driver WiFi Throttle, then sets and Joins the Programming track as a Mainline DCC signal, then you just throttle-up and "Drive Away" onto the main line tracks. 

Place a second engine on the programming track and repeat the steps as many times as you would like. This is a New & Unique DCC WiFI Throttle client feature only found in DCC++EX & Engine Driver WiFi Apps. 

Where it's used; 
An Arduino Mega DCC++EX + WiFI enabled Command Station in Standalone Operations mode Directly WiFI connected with Engine Driver WiFi Throttles utilizing the new standalone WiThrottle Server feature imbedded in DCC++EX Command Station. 

Setup a Mega DCC++EX CS + ESP 8266 WiFi MakerFab Shield or a ESP01 WiFi board in either Access Point AP mode or Station STA (client) mode through a shared Router for a Command Station (CS) Standalone Operations configuration. Then the Engine Driver and Command Station both sign on to the common SSID and Password to share the common WiFi signal and channel. 

This Standalone WiFi configuration works Without the use of any additional hardware or third party software controller's like JMRI or Rocrail interfaces.

How it works
=============

DCC++EX 3.1 and above has a new software implementation logic that in a sense replaces a hardwired DPDT switch and combines multiple DCC++ commands in a sequence to perform the magic dubbed "DriveAway(tm)". It triggers a <R> read the CV1 Short or CV 17 & 18 Long address and CV8 Mfr ID, and CV29 Setup and then returns and automatically loads the Loco# into the throttle. The Command Station then automatically sets ``<1 JOIN>`` command to switch the PROG track to MAIN and allows your Engine Driver App to drive it away onto the main line tracks  

Logic Programming Protection;
If you inadvertently touch or send any Programming command while an Engine is sitting on the PROG track when it's active as a [JOIN] Main line track, the DCC++EX software Automatically kicks back to Program Track Mode before accepting any other commands as safety procedure. 


New "Discovered Servers" on WiFi Throttles
===========================================

WiThrottles now detect and display both DCC++EX Command Station name and JMRI WiThrottle Server Profile name in the WiFi Throttle Apps.

Sample Engine Driver App Discovered Servers:
      “DCC++EX”                  {Direct connect to the Command Station}
      “My JMRI Railroad”        {JMRI connected via WiThrottle Server}

Our new multicast Dynamic Network Server (mDNS) enhancement allows us to display the available WiFi server connections to a DCC++EX Command Station. Choosing one allows your WiThrottle App to connect to and load engine rosters and function keys to your throttle.

Function key layout, 

New DCC++EX 4.0 EXRAIL "Roster" Feature 
========================================

When choosing “DCC++EX” from discovered servers an Engine Driver or WiThrottle is Directly connected to the Command Station and the WiFi Throttle function keys can be loaded from either the "Default Mode" which load function names you have previously set up in Engine Driver, or now with the New EXRAIL "ROSTER" command which allows you to enter all your engine numbers, names and function keys into your myAutomation.h file and then automatically upload and pass the Command Stations Roster and Function keys into your Engine Driver and WiThrottle Apps.  

To load the JMRI Roster or Rocrail function keys you must switch your WiFi connection to the SSID the JMRI WiThrottle Server {Windows, Mac iOS or Raspberry Pi} is signed on to and then reconnect the new SSID IP address: port # displayed to the JMRI WiThrottle Server on your Engine Driver & WiThrottle or choose "My JMRI Railroad" from discovered servers.

Precaution Wiring Prog & Main
==============================

Please be sure "Both" Programming Track rails are Insulated with dual plastic joiners from the Main line and that both the wiring for CAB A Main and CAB B Prog positive leads are connected on the right rail and the negative leads are connected on the left rail.  Or else undesirable gremlins may appear, you've been forewarned. The proceeding is a public service announcement and the DCC++EX team makes no expressed or implied guarantees if the user fails his or her due diligence.
