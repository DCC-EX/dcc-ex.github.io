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

.. warning:: 
  :class: warning-float-right

  This is not zero (0) stretching. We deliberately do not support the zero stretching address function found on Digitrax and Lenz command Stations. The constant dual DCC electrical signal may damage certain types of older DC motors if left on for a long time. |BR| **So never put a DC locomotive on a DCC-EX DCC track.**

*A first for the DCC & DC model railroading world.*

|EX-CS| is now a dual **Command Station** for both **Digital Command Control (DCC)** and **analogue (DC)** layouts.

With just a single |EX-CS| and a compatible throttle you can simultaneously run both your DCC Locos and analogue DC Locos on multiple separate insulated tracks/districts.

Any throttle that connect to an |EX-CS| can control analogue (DC) locos just as easily as DCC locos. Throttle Compatibility:

  * WiFi Throttles (e.g. |Engine Driver|, |wiThrottle| and many others)
  * The DCC-EX browser based |EX-WT|
  * Other wired throttles to operate your DCC layout and your DC layout, either separately or a simultaneous combination of the two modes

|EX-CS| with |TM| includes the following features: 

  * DCC (PWM) modes ``MAIN`` for mainline tracks and ``PROG`` for a programming track
  * DC (PWM) modes for ``DC`` or ``DCX`` (reversed polarity)
  * Each track/district can also be disabled by setting to ``NONE``
  
|EX-CS| **production version 5.0+** (devel v4.2.50+) supports both DCC (PWM) and DC (PWM) Pulse Width Modulation modes as an *embedded standard feature*.
TrackManager allows you to set up and operate up to eight separate dual insulated sections of track/districts in either DCC (PWM) and or DC (PWM) as tracks A - H. No additional external DCC decoders are required for DC (PWM), and a single |EX-CS| is the only hardware needed for full functionality.

Technical Details
-----------------

If you are interested in the technical details of how this works refer to :doc:`technical-details`

----

Replacing or Integrating Into Your Current Layout
=================================================

A single |EX-CS| is capable of replacing the DC transformers of an existing DC layout and will also allow you to easily swap between DC (PWM) mode and DCC (PWM) mode on any of the A thru H dual insulated tracks/districts.

This is all done through a single |EX-CS|, and no we're not using another Expensive DCC decoder under the table on each Track/District/Block to address that section of track.

.. warning::
  
  Existing analogue DC layouts which have DC transformers on two or more separate DC tracks/districts/blocks and/or also have a separate DCC command station with a section of dead rail, an electric relay, or a DPDT centre-off switch between the two types of controller powered stations must not be using a common ground rail, and should only use dual insulated tracks.

  The features described here also allows replacing the physical DPDT switch for switching from DC to DCC.

----

Hardware Requirements and Technical Notes
=========================================

.. note:: 
  :class: note-float-right

  These requirements are only for operating DC locomotives. There is nothing to do in a pure DCC environment where no DC or analogue locomotives are run.

Generally speaking the |EX-CS| can directly replace a DC transformer on a single block or two block DC layout.  If you have more than two blocks, each with their own controller, then you need to look at one of the motor contorller options that support more than 2 outputs/blocks.

e.g. An Arduino Mega (with or without WiFi) and Standard L298P Motor Shield |EX-CS| has two available Tracks (**A** & **B**). Either or both of these can be used for DC.

The two connections/leads from each output on the motor shield(s) will simply replace the two connection/leads from your transformer(s) that go to the two rails of the block.

.. warning:: 
  
  1. In order for |TM| to operate in DC mode, the motor shield must have a brake pin defined in your “config.h” motor shield definition. There are a very limited number of motor boards that are suitable for use with DC mode, and any other motor boards are unsupported. The current list is available in :ref:`reference/hardware/motor-boards:trackmanager dc compatible boards`.

  2. Never directly connect DC and DCC tracks/blocks together.  There must always be insulated joiners on both tracks between the tracks/blocks.
  
  3. Never drive a loco from an |EX-CS| controlled track/district to any other track controlled by another brand/type of DCC or DC System.

Some suggested precautions are to add 4 fuses on wires (-b +b, -a +a) to the |EX-CS| connections. Use 2A fuses for the standard L298P motor shield or 5A fuses for the larger motor boards.

DC (PWM) modes
==============

Using |TM|, with simple easy commands from a throttle or a serial monitor, you can change any track/block (A-H) from DCC (PWM) to DC (PWM) and back in real time or, alternately you can semi-permanently set them in ``myconfiguration.h``. 

  * Valid DCC modes are ``MAIN``, ``PROG``, and ``NONE``
  * Valid DC modes are ``DC``, ``DCX``, and ``NONE``
 
  ``DCX`` is DC with an opposite polarity. Like NMRA modular layout track B which is wired left rail positive (+) and right rail negative (-). |BR| This allows a throttle on track B set to DCX to operate in forward and reverse correctly for west bound engines.

When specifying ``DC`` or ``DCX`` it is necessary to also specify which locomotive (cab) ID will be used to control that track/block. 

TrackMagic uses that ID (often the road number of a DC locomotive) in a throttle to run it on a assigned track/district/block, mimicking the look of DCC Locomotives. No DPDT Switches are required, all waveform mode switching is done by |TM| software instructions.

So, you can take a standard DC motor only locomotive (Cab) road number on the side of the locomotive and assign it to one, or more (up to 8), tracks/districts/blocks (labelled A thru H). Then enter that same number into a throttle and control that Loco (Cab) ID on each and every one of the assigned tracks.

  * Valid loco (Cab) addresses are 1 to 10239
  * Zero (0) loco (Cab) address is not valid

.. note:: 
  
  When specifying a DC or DCX locomotive (cab) ID, it is advised to avoid using one of your existing locomotive DCC addresses, otherwise a command sent to control a locomotive (cab) on that DC or DCX track will also operate your DCC locomotive with the same address.

----

How to set DC (PWM) mode?
=========================

DC (PWM) mode can be enabled several ways:

* From a throttle, including |EX-WT| (temporary)
* From the serial monitor (temporary)
* In ``myAutomation.h`` (semi-permanent)
* From the |EX-TB| WiFi Android app

|hr-dashed|

From a throttle
---------------

Currently the only throttle that directly supports the track manager features, which include changing to DC mode is |ED|.  See :doc:`/throttles/software/engine-driver-native-protocol` for details.

  |Engine Driver| DCC-EX Native mode features now available today via Google Play Store `Engine Driver <https://play.google.com/store/apps/details?id=jmri.enginedriver>`_ |EXTERNAL-LINK|

However it is possible to create 'Routes' or 'automations' to switch between DC and DCC modes that can be seen and used by many throttles.  (See below for details)

You can use the 'Route' / 'automation' approach in |EX-WT| and also use the same options as for a serial monitor (see below).

|hr-dashed|

From the Serial Monitor
-----------------------

You can use a Command Line via a *PC with Arduino IDE Serial Monitor*, |EX-WT|, or the *JMRI serial Traffic Monitor* to send the following commands through your USB connected cable.  You can also send these commands via |Engine Driver| or |EX-TB|, though both apps povide more user friendly options.

To display the current TrackManager configuration, use the command ``<=>`` an equal sign looks like a track.

The Serial Monitor will show current status, example; Track A as Main and Track B as PROG

  * ``<= A MAIN>``
  * ``<= B PROG>``

To change or configure the current track modes use the new command ``<= trackletter mode [address]>`` which has been added for Track Manager, where:

  * ``trackletter`` is ``A`` through ``H``
  * ``mode`` is one of ``MAIN``, ``PROG``, ``DC``, ``DCX``, or ``NONE`` (DCX is DC with opposite polarity)
  * ``address`` is the Cab ID and is only required when specifying DC or DCX modes

.. code-block::

  example:

  <= A MAIN>     // Set track A to MAIN DCC mode
  <= B PROG>     // Set track B to PROG DCC mode
 or
  <= A DC 1234>  // Set track A to DC mode with address 1234
  <= B DCX 4321> // Set track B to DC mode Opposite Polarity address 4321
                 // or any number you assign from 1 to 10239
  <= B NONE>      // Set track B disabled, like a staging yard when it gets too noisy.

  You would then enter your Engine address on the throttle of 1234 and 4321 and drive them on the layout.

|hr-dashed|

in myAutomation.H
-----------------

Create an EXRAIL myAutomation.h file Scripts for Track Manager assigned commands and they automatically appear in |Engine Driver| as GUI Automation [Handoff] and Route [Set] buttons, and in WiThrottle WiFi Throttle iOS as [Route] buttons, and on TCS Universal UWT-50 & 100 WiFi Throttle [Select Accry] lines.

Semi-Permanently setting the mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using |EX-R| functions inside myAutomation.h file to run Automation scripts to change track modes from DCC to DC and back.
my.Automation.h file

.. code-block:: 

  example:
  
  //SET_TRACK(id,mode)
  SET_TRACK(A, MAIN)
  SET_TRACK(B, PROG)
  SET_TRACK(C, DC)
  SET_TRACK(D, DCX)

On Demand
^^^^^^^^^

You can create routes to dynamically set the modes.  The following are examples of how you can do this:

All are then controlled through DCC-EX TrackManager with a simple push of a GUI button of Either or Both |Engine Driver| Handoff to Acquire the last Throttle Engine# used and run it on the mode of the track  [i.e. DC engine 1225], Or |Engine Driver| (Set) button to set a block to a specific mode.

Simple changes
~~~~~~~~~~~~~~

In an EXRAIL Automation script we could Set a Loco Address to a specific track in DC mode and Manually run a preassigned address on the layout.

.. code-block:: 

  example:
  
  ROUTE(500,"1.Trk: A main, B prog") 
      SET_TRACK(A,MAIN)            // set output A to DCC MAIN
      SET_TRACK(B,PROG)            // set output B to DCC PROG
  DONE
  ROUTE(501,"2.Trk: A dc10, B dc11") 
      SETLOCO(10) SET_TRACK(A,DC)  // set output A to DC using address 10
      SETLOCO(11) SET_TRACK(B,DC)  // set output B to DC using address 11
  DONE
  ROUTE(502,"3.Trk: A dc10, B main") 
      SETLOCO(10) SET_TRACK(A,DC)  // set output A to DC using address 10
      SET_TRACK(B,MAIN)            // set output B to DCC MAIN
  DONE
  ROUTE(503,"4.Trk: A main, B dc10") 
      SET_TRACK(A,MAIN)            // set output A to DCC MAIN
      SETLOCO(10) SET_TRACK(B,DC)  // set output B to DC using address 10
  DONE

These will appear in the list of routes in the throttle.  They set the various tracks to DCC, or DC using address 10 or 11 (see above).

[Handoff] buttons
~~~~~~~~~~~~~~~~~

In a |EX-R| Automation script we could assign a track mode to DC and wait for a |Engine Driver| throttle to Assign the Current Selected Active Engine Address and drive Manually through the district on the layout.
See the third Engine Driver Throttle image 'Districts A thru B with [Set] buttons at the end.

.. code-block:: 

  example:

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

  Copy and repeat AUTOMATION(506-510, District B mode) and create any additional combinations or tracks C - H as you add more motor boards.

Complex Automations
~~~~~~~~~~~~~~~~~~~

You could also create more complex EX-RAIL Track Manager Functions for Engine Driver Throttle Automation [Handoff] buttons

In a |EX-R| Automation script we could a Set a Loco Address to a specific track in DC mode and have it run on Automation through the layout. See the sixth Engine Driver Throttle image 'EXRAIL 202 Roundhouse to Turntable Back & Forth - Timed' [Handoff] button at the end.

.. code-block::

  example:
  
  AUTOMATION(202,"Roundhouse to Turntable Back & Forth -Timed")
    SETLOCO(1225)
    SET_TRACK(B,DC)
    // Run a your Roundhouse script blow whistle, run Forward delay wait and run Reverse delay stop       
    DELAYRANDOM(msec, msec) // randomise the run time between runs
  DONE

|hr-dashed|

Using EX-Toolbox
----------------

|EX-TB| has the same |TM| features as |ED| plus many additonal capabilities. see :doc:`/ex-toolbox/index` for details.

|EX-TB| features now available today via Google Play Store  `EX-Toolbox <https://play.google.com/store/apps/details?id=dcc_ex.ex_toolbox>`_ |EXTERNAL-LINK|

----

Using DC (PWM) mode
===================

First set the desired track/block to be DC using on of the options above.

Place any analogue (DC locomotive) on a |EX-CS| power layout with a TrackManager DC assigned track/block. It will sit there dead quiet with lights off until the throttle speed is increased in either direction and then lights up and begins to move.

In your throttle (the same one that you would use for a DCC locomotive), select the address assigned to track/block when you enabled it.  Then just control the loco the same as if it was a DCC locomotive.

Throttle speed response for DC Cabs vary because the DC district track is operating from 0Vdc to 16+Vdc ~PWM waveform signal. CAB's operating on a DCdistrict with either WiFi Throttles and EXRAIL Automation scripts with |Engine Driver| Handoff run different DC motors at different speeds.

So a script for FWD(50) speed will run at completely different speeds for two different DC motors depending on their resistance and efficiency.  One crawls at 50 while the other one runs like a bat out of hell.

You can also run a DCC Locos with DC Conversion CV enabled On and run on the DCdistrict, without having to change the decoder DCC address.
They will all run on that section of track with the address specified for that track/block (not the DCC address of the loco). DCC Loco with DC enabled CV decoder will also sit quietly until the throttle increases. The Sound will turn on first then as you throttle up more it will begin moving.  You can throttle back until it stops but leave a little throttle speed on say 5% and the Sound will continue to play while it is stopped. DCC Sound Decoder locos with DC conversion enabled may be silent until the track reaches between 2v to 6Vdc then the Sound will start up, and between 3v to 8Vdc the motor will begin to respond and move depending on the manufacturer's decoder.

----

DCC-EX Command Station with EX-RAIL & TrackManager
---------------------------------------------------

Cool thing is the new EXRAIL Automation(n) & Routes(n) work the same with DCC engines on MAIN tracks and the DC engines on DC or DCX tracks, along with the Sensors, Servos /Turnouts, Signals & MP3 Sound DFPlayer triggers with little or no script changes other than maybe the FWD(n) & REV (n) Speeds.

With the new DCC-EX direct WiFi Discovered Server you can connect |Engine Driver| & other WiThrottle app based throttles directly and have EXRAIL [Handoff] & [Set] buttons to run EXRAIL scripts from the throttles.

These are DCC-EX Major feature/benefits because with other systems you'll have to use a PC computer or Pi processor & JMRI for WiThrottle Server throttle access and you have to write two different JMRI Jython.py scripts and then Setup Tools> Tables> Routes for for both DCC and DC automation & routes runs.

Modular Layouts
---------------

DCC-EX TrackManager 4.2.50+ is perfect for NMRA DCC Standards Modular Layouts which have two MAIN tracks/districts,
Track A and Track B with sidings;

* Track A (east bound) wired rails L- R+
* Track B (westbound) which also have all the siding and spurs, wired rails L+  R-

You can set each district separately as mode

* DCC for MAIN, PROG or NONE
* analogue for DC, DCX or NONE

DCX is Opposite Polarity and is what you set Block B to when you want it in DC mode because it is wired to NMRA Modular DCC Standards L+, R-.

Combinations of Modes
---------------------

Using the New TrackManager Function commands you can run the any layout as:

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

----

EXRAIL additional examples
==========================

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
