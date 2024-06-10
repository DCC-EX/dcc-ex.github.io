.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-tm.rst
|TRACKMANAGER-LOGO|

***********************
TrackManager (DCC & DC)
***********************

|tinkerer| |engineer| |support-button| |githublink-ex-commandstation-button2|

|NEW-IN-V5-LOGO-SMALL|

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:

Welcome to DCC-EX TrackManager
===============================

*A first for the DCC & DC model railroading world.*

|EX-CS| is now a dual **Command Station** for both **Digital Command Control (DCC)** and **analogue (DC)** layouts.

With just a single |EX-CS| and a compatible throttle you can simultaneously run both your DCC Locos and analogue DC Locos with road number IDs as throttle addresses from 1 to 10239 to control and drive them on multiple separate insulated tracks/districts.

Any throttle that connect to an |EX-CS| can control analogue (DC) locos just as easily as DCC locos. Throttle Compatibility:

  * WiFi Throttles (e.g. |Engine Driver|, |wiThrottle| and many others)
  * The DCC-EX browser based |EX-WT|
  * Other wired throttles to operate your DCC layout and your DC layout, either separately or a simultaneous combination of the two modes

|EX-CS| with |TM| includes the following features: 

  * DCC track modes of ``MAIN``, ``PROG``, and ``NONE``
  * DC track modes of ``DC``, ``DCX`` (DC Reversed Polarity), and ``NONE``

|EX-CS| **production version 5.0+** (devel v4.2.50+) supports both DCC (PWM) and DC (PWM) Pulse Width Modulation modes as an *embedded standard feature*.
TrackManager allows you to set up and operate up to eight separate dual insulated sections of track/districts in either DCC (PWM) and or DC (PWM) as tracks A - H.

An Arduino Mega (with or without WiFi) and Standard L298P Motor Shield |EX-CS| has two ready to run Tracks (**A** & **B**) which can be configured as:

  * DCC (PWM) modes MAIN for mainline tracks and PROG for a programming track
  * DC (PWM) modes for DC or DCX (opposite polarity)
  * Each track/district can also be disabled by setting to "NONE"

No additional external DCC decoders are required for DC (PWM) track assignments, and a single |EX-CS| is the only hardware needed for full functionality.

One key difference to note in comparing DCC vs. DC is that in DCC mode, forward/reverse is determined by the DCC decoder, not the track, whereas in DC mode the direction is dependent upon the track polarity.

Before you begin
----------------

**This is not your father's DC railway which used DC transformers for Cab control.**

Turn off, unplug the AC power cord, and disconnect your current DC transformer(s) / power supply(s) from the DC layout track to place in a box for safe keeping.

You will instead be using a regulated DC (Laptop) 12-18 Vdc 3-5Amp power supply to your Motor Shield and or Motor Board (booster) to run all your DCC Locos and analogue DC Cabs on all your individual tracks/districts/blocks.

You will be using DC (Pulse Width Modulation PWM) to drive the DC engines, Not DC Direct Current (-0 +16v).

.. figure:: /_static/images/track_manager/DCCpwm_DCCpwm_AC_DC.png
  :alt: Waveform Comparison
  :scale: 50%

  Waveform Comparison

.. note:: 

  These modes, (PWM) vs analogue DC are totally incompatible with one another and if crossed will result in magic smoke and a burned out motor shield and or USB connector. 

 * DCC(PWM) is detected on a multimeter as an AC signal but in a square wave form, not as a sine wave
 * DC(PWM) is detected on a multimeter as a DC signal in a square wave form, not as a direct current wave

The DC(PWM) track is Power supply dependent and needs a varying amount of 0 zero to maximum Vdc passed to the track of 12 or 16 or 18vdc, depending on whether they're N, HO or G scale engines.

Note; The signal is detected as DC on this track, from 0Vdc to max +xxVdc depending on the Motor Shield DC power supply output. The DCC-EX 122.55Hz PWM DC motor signal allows for better functioning and better running than most competing systems.

TrackManager DCC(PWM) vs. DC(PWM) wave forms
=============================================

A simplified representation of what the dual (PWM) signals might look like through the track:

.. figure:: /_static/images/track_manager/dcc-and-dc-on-track.png
  :alt: DCC PWM signal
  :scale: 50%

  DCC PWM signal

.. note:: Note on PWM frequency

  Different microcontrollers utilise different PWM frequencies, and at present, these default frequencies are in use rather than using software to define them.

  The side effect of these differing frequencies is that you may notice humming or sometimes squealing noises from older DC motors.

  The known PWM frequencies are:

    * Mega2560 - 122.55Hz
    * ESP32         - 131Hz
    * STM32 Nucleo - typically 1000Hz

Replacing or Integrating Into Your Current Layout
=================================================

Existing analogue DC layouts which have standard DC transformers on two or more separate DC tracks/districts/blocks and/or also have a second separate proprietary DCC command station would have in place a section of dead rail, an electric relay, or a DPDT centre-off switch between the two types of controller powered stations. These should not be using a common ground rail, and only use dual insulated tracks.

You will be replacing this kind of legacy analogue DC and proprietary DCC installation described above with a single |EX-CS| which will have a software switching implementation, allowing you to easily and quickly swap between the two DCC (PWM) and DC (PWM) modes on any of the A thru H dual insulated tracks/districts in real time.

This also allows replacing the physical hardware DPDT switch.

This is all done through a single |EX-CS|. 
And no we're not using another Expensive DCC decoder under the table on each Track/District/Block to address that section of track.

.. note:: 
  
  When specifying a DC or DCX cab ID, do not use one of your existing locomotive DCC addresses or road number IDs, otherwise a command sent to control a Cab on that DC or DCX track will also operate your DCC Loco with the same address, unless you intentionally do so.

Hardware Requirements and Technical Notes
=========================================

.. note:: 

  These requirements are only for operating DC locomotives. There is nothing to do in a pure DCC environment where no DC or analogue locomotives are run.

.. warning:: 

  In order for |TM| to operate in DC mode, the motor shield must have a brake pin defined in your “config.h” motor shield definition. There are a very limited number of motor boards that are suitable for use with DC mode, and any other motor boards are unsupported. The current list is available in :ref:`reference/hardware/motor-boards:trackmanager dc compatible boards`.

Do not attempt to connect two insulated tracks together and drive a DCC engine back and forth until someone bolder than you tries it first (or you've tested it).

.. warning:: 

  Never drive a loco from an |EX-CS| controlled track or district to any other DCC or DC System.

Some suggested precautions are to add 4 fuses on wires (-b +b, -a +a) to the |EX-CS| connections. Use 2A fuses for the standard L298P motor shield or 5A fuses for the larger motor boards.

How do you run a EX-CommandStation in DC (PWM) mode?
====================================================

Using TrackManager with simple easy commands from a throttle or from a serial monitor we can change any insulated track A-H from DCC (PWM) to DC (PWM) and back in real time.

  * Valid DCC modes are MAIN, PROG, and NONE
  * Valid DC modes are DC, DCX, and NONE
  * DCX is DC with an opposite polarity like NMRA modular layout track B which is wired left rail positive (+) and right rail negative (-)

This allows a throttle on track B set to DCX to operate in forward and reverse correctly for west bound engines

So, you can take a standard DC motor only engines Cab road number on the side of the engine and assign it to one or more of up to 8 tracks/districts/blocks labelled A thru H then enter that same number into a throttle and control that Loco Cab # on each and every one of the assigned tracks.

  * Valid Cab addresses are 1 to 10239.
  * Invalid Cab address is 0 zero.

.. warning:: 

  We do not support 0 zero stretch address function, found on Digitrax and Lenz command Stations on purpose. The constant dual DCC electrical signal may damage certain types of older DC motors if left on for a long time.

Unlike Digitrax and Lenz 0 Zero stretch DCC (PWM) signal which leaves the engine lit up and humming loudly with the throttle and engine at 0 speed, because it is receiving a Dual DCC(PWM) aka AC signal, while the |EX-CS| TrackManager is dead quiet and at rest at 0 speed.

Place any analogue DC engine on our EX-CommandStation with a TrackManager DC assigned track and it sits there dead quiet with lights off Until the throttle speed is increased in either direction and then lights up and begins to move.

DCC Loco with DC enabled CV decoder also sits quietly and when the throttle increases the Sound will turn on first then as you throttle up more it will begin moving.  You can throttle back until it stops but leave a little throttle speed on say 5% and the Sound will continue to play while it is stopped.

Throttle speed response for DC Cabs vary because the DCdistrict track is operating from 0Vdc to 16+Vdc ~PWM waveform signal. CAB's operating on a DCdistrict with either WiFi Throttles and EXRAIL Automation scripts with |Engine Driver| Handoff run different DC motors at different speeds.

So a script for FWD(50) speed will run at completely different speeds for two different DC motors depending on their resistance and efficiency.  One crawls at 50 while the other one runs like a bat out of hell.

You can also run a DCC Locos with DC Conversion CV enabled On and run on the DCdistrict, without having to change the decoder DCC address.
They will all run on that section of track.

DCC Sound Decoder locos with DC conversion enabled may be silent until the track reaches between 2v to 6Vdc then the Sound will start up, and between 3v to 8Vdc the motor will begin to respond and move depending on the manufacturer's decoder.

Controlling & Managing DCC-EX TrackManager modes
-------------------------------------------------

You can Assign Tracks/Districts to DCC and DC mode in four ways

  1. Command Line via PC with Arduino IDE Serial Monitor or JMRI serial Traffic Monitor and it is sent through your USB connected cable.
  2. Create an EXRAIL myAutomation.h file Scripts for Track Manager assigned commands and they automatically appear in |Engine Driver| as GUI Automation [Handoff] and Route [Set] buttons, and in WiThrottle WiFi Throttle iOS as [Route] buttons, and on TCS Universal UWT-50 & 100 WiFi Throttle [Select Accry] lines.

  3. Enhanced |Engine Driver| WiFi Throttle Android app v2.35.169+ features;

    * Track/District Manager set mode screen by touching a track mode entering an address
    * Command Cmd Line Serial Monitor and enter them like in example (1) above but via WiFi Native mode

  4. New |EX-TB| WiFi Android app features;
  
    * Track/District Manager set mode screen by touching a track mode, entering an address
    * Command Cmd Line Serial Monitor and enter them like in example (1) above but via WiFi Native mode

New |Engine Driver| DCC-EX Native mode features now available today via Google Play Store:

  * `Engine Driver <https://play.google.com/store/apps/details?id=jmri.enginedriver>`_ |EXTERNAL-LINK|
  * `EX-Toolbox <https://play.google.com/store/apps/details?id=dcc_ex.ex_toolbox>`_ |EXTERNAL-LINK|

TrackManager Commands
======================

Sending commands from the Arduino IDE Serial Monitor or JMRI Send Command Line or a |Engine Driver| WiFi Throttle.

To display the current TrackManager configuration, use the command ``<=>`` an equal sign looks like a track.

The Serial Monitor will show current status, example; Track A as Main and Track B as PROG

  * <= A MAIN>
  * <= B PROG>

To change or configure the current track modes use the new command ``<= trackletter mode [address]>`` which has been added for Track Manager, where:

  * ``trackletter`` is A through H
  * ``mode`` is one of MAIN, PROG, DC, DCX, or NONE (DCX is DC with opposite polarity)
  * ``address`` is the Cab ID and is only required when specifying DC or DCX modes

.. code-block::

  <= A MAIN>     // Set track A to MAIN DCC mode
  <= B PROG>     // Set track B to PROG DCC mode
 or
  <= A DC 1234>  // Set track A to DC mode with address 1234
  <= B DCX 4321> // Set track B to DC mode Opposite Polarity address 4321
                 // or any number you assign from 1 to 10239
  <= B NONE>      // Set track B disabled, like a staging yard when it gets too noisy.

.. note:: 

  You would then enter your Engine address on the throttle of 1234 and 4321 and drive them on the layout.

Create EX-RAIL Scripts to Change Track modes
--------------------------------------------
Using |EX-R| functions inside myAutomation.h file to run Automation scripts to change track modes from DCC to DC and back.
my.Automation.h file

.. code-block:: 

  //SET_TRACK(id,mode)
    SET_TRACK(A, MAIN)
    SET_TRACK(B, PROG)
    SET_TRACK(C, DC)
    SET_TRACK(D, DCX)

Create EX-RAIL list of Track Manager Functions for Engine Driver Automatically Assign [Handoff] buttons
-------------------------------------------------------------------------------------------------------

In a |EX-R| Automation script we could assign a track mode to DC and wait for a |Engine Driver| throttle to Assign the Current Selected Active Engine Address and drive Manually through the district on the layout.
 See the third Engine Driver Throttle image 'Districts A thru B with [Set] buttons at the end.

.. code-block:: 

 AUTOMATION(500, "Districts A MAIN _ B PROG Default")// Reset Default back to DCC Main & PROG
  SET_TRACK(A,MAIN) PRINT("Default Districts Tracks MAIN A & PROG B")
  SET_TRACK(B,PROG)
  DONE
 AUTOMATION(501, "District A MAIN")   // Alternate DCC Main track A
  SET_TRACK(A,MAIN) PRINT("District A MAIN")
  DONE
 AUTOMATION(502, "District A PROG")   // Alternate DCC PROG track A
  SET_TRACK(A,PROG) PRINT("District A PROG")
  DONE
 AUTOMATION(503, "District A DC")     // Alternate DC track A with loco ID 1
  SETLOCO(1)
  SET_TRACK(A,DC) PRINT("District A DC")
  DONE
 AUTOMATION(504, "District A DCX")    // Alternate DCX track A Changed to Opposite Polarity
  SETLOCO(1)
  SET_TRACK(A,DCX) PRINT("District A DCX Opposite Polarity") // Track A Opposite Polarity DC    
  DONE
 AUTOMATION(505, "District A NONE")    // A Track disabled
  SET_TRACK(A, NONE) PRINT ("District A disabled")
  DONE
 Copy and repeat AUTOMATION(506-510, District B  mode)
  and create any additional combinations or tracks C - H as you add more motor boards.

Create EX-RAIL Track Manager Functions for Engine Driver Throttle Automation [Handoff] buttons
----------------------------------------------------------------------------------------------

In a |EX-R| Automation script we could a Set a Loco Address to a specific track in DC mode and have it run on Automation through the layout.
 See the sixth Engine Driver Throttle image 'EXRAIL 202 Roundhouse to Turntable Back & Forth - Timed' [Handoff] button at the end.

.. code-block::

 AUTOMATION(202,"Roundhouse to Turntable Back & Forth -Timed")
   SETLOCO(1225)
   SET_TRACK(B,DC)
   Run a your Roundhouse script blow whistle, run Forward delay wait and run Reverse delay stop       
   DELAYRANDOM(msec, msec) // randomise the run time between runs
   DONE

Create EX-RAIL Track Manager Functions for Engine Driver Throttle Route [Set] buttons
-------------------------------------------------------------------------------------

In an EXRAIL Automation script we could Set a Loco Address to a specific track in DC mode and Manually run a preassigned address on the layout.

.. code-block:: 

 ROUTE(1225,"Set track B to DC 1225")
   SETLOCO(1225)    // Assign Loco 1225
   SET_TRACK(B,DC)  // Set Track B to DC with address 1225
   CLOSE(1)         // Close Turnout 1
   THROW(2)         // Throw Turnout 2
   DONE

Then manually drive the Cab# around the layout

All done through DCC-EX TrackManager with a simple push of a GUI button of Either or Both |Engine Driver| Handoff to Acquire the last Throttle Engine# used and run it on the mode of the track  [i.e. DC engine 1225], Or |Engine Driver| (Set) button to set a block to a specific mode.

TrackMagic uses the road number ID of a DC Engine in a throttle to run it on a assigned track/district/block, mimicking the look of DCC Engines.
No DPDT Switches are required, all waveform mode switching is done by Track Manager Software instructions.


DCC-EX Command Station with EX-RAIL & TrackManager
---------------------------------------------------

Cool thing is the new EXRAIL Automation(n) & Routes(n) work the same with DCC engines on MAIN tracks and the DC engines on DC or DCX tracks, along with the Sensors, Servos /Turnouts, Signals & MP3 Sound DFPlayer triggers with little or no script changes other than maybe the FWD(n) & REV (n) Speeds.

With the new DCC-EX direct WiFi Discovered Server you can connect |Engine Driver| & other WiThrottle app based throttles directly and have EXRAIL [Handoff] & [Set] buttons to run EXRAIL scripts from the throttles.

These are DCC-EX Major feature/benefits because with other systems you'll have to use a PC computer or Pi processor & JMRI for WiThrottle Server throttle access and you have to write two different JMRI Jython.py scripts and then Setup Tools> Tables> Routes for for both DCC and DC automation & routes runs.

Modular Layouts
---------------

DCC-EX TrackManager 4.2.50+ is perfect for NMRA DCC Standards Modular Layouts which have two MAIN tracks/districts,
Track A and Track B with sidings;

* Track A (east bound) wired rails L-  R+
* Track B (westbound) which also have all the siding and spurs, wired rails L+  R-

You can set each district separately as mode

* DCC for MAIN, PROG or NONE
* analogue for DC, DCX or NONE

DCX is Opposite Polarity and is what you set Block B to when you want it in DC mode because it is wired to NMRA Modular DCC Standards L+, R-.

Using the New TrackManager Function commands you can run the any layout as
--------------------------------------------------------------------------

.. code-block::

 Track A & Track B
   MAIN & PROG    (Use JOIN function for a Programming track to make a MagicTrack) 
   MAIN & MAIN
   PROG & MAIN
   MAIN & DC
   PROG & DC
     DC & MAIN
     DC & PROG
     DC & DC
     DC & DCX
 or any combination with up to 8 separate dual insulated tracks/districts from A - H.

All done through the free |DCC-EX| TrackManager commands.

EXRAIL examples
===============

Example of User defined EXRAIL Scripts running on Engine Driver Throttle App (Android):
---------------------------------------------------------------------------------------

**Engine Driver Throttle Controlling Two Locos:**

 - DCC PE 1225 on District A DCC address 1225 Sound Decoder
 -  DC NH  667 on District B DC address  667 with IPLS Virtual Sound Decoder

.. figure:: /_static/images/track_manager/trackmanager_engine_driver_1.png
  :alt: Track Manager ED 1
  :scale: 50%

  Track Manager - Engine Driver 1

**DCC-EX Commands, scroll-able**

.. figure:: /_static/images/track_manager/trackmanager_engine_driver_2.png
  :alt: Track Manager
  :scale: 50%

  Track Manager

**DCC-EX TrackManager "Handoff" & "Set" buttons**

 - Scroll through & select track modes
 - Takes the current selected Active Throttle Engine and assigns that Address to the DC or DCX track

.. figure:: /_static/images/track_manager/trackmanager_engine_driver_3.png
  :alt: Track Manager handoff
  :scale: 50%

  Track Manager - Engine Driver handoff

**Engine Driver DCC-EX Native mode**

 - TrackManager MAIN & PROG
 - With DCC-EX Cmd Line & Serial monitor
  
.. figure:: /_static/images/track_manager/trackmanager_engine_driver_4.png
  :alt: Track Manager DCC-EX native mode
  :scale: 50%

  Track Manager - Engine Driver DCC-EX native mode
  
**Engine Driver DCC-EX Native mode**

 - TrackManager District A DCC MAIN
 - TrackManager District B  DC  667

.. figure:: /_static/images/track_manager/trackmanager_engine_driver_5.png
  :alt: Track Manager A/B
  :scale: 50%

  Engine Driver - Track Manager A/B

**Engine Driver EXRAIL Automation [Handoff] and FX special effects buttons**

.. figure:: /_static/images/track_manager/trackmanager_engine_driver_6.png
  :alt: Track Manager handoff
  :scale: 50%

  Track Manager - Engine Driver handoff

**FX Special Effects [Set] continued and Route [Set] buttons**

.. figure:: /_static/images/track_manager/trackmanager_engine_driver_7.png
  :alt: Track Manager handoff/set
  :scale: 50%

  Track Manager - Engine Driver handoff/set

EXRAIL Functions Displaying on Smartphone Apps & Universal WiFi Throttles
-------------------------------------------------------------------------

The |Engine Driver| EXRAIL screens shown above are all created through user defined EXRAIL Automation(n) and Route(n) scripts which are automatically passed to both |Engine Driver| & WiThrottle App screens as well as the Train Control Systems TCS Universal WiFi UWT-50 and UWT-100 tactile throttles all via direct connect DCC-EX WiThrottle Protocol interface.

Please see the specific Smartphone App & Universal WiFi Throttle instructions on how to enable their Preferences and Route screens. 
https://dcc-ex.com/throttles/index.html#withrottle-protocol-based-throttles
