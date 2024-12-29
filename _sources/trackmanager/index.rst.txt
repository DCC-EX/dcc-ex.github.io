.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-tm.rst
|TRACKMANAGER-LOGO|

***********************
TrackManager (DCC & DC)
***********************

|SUITABLE| |tinkerer| |engineer| |support-button| |githublink-ex-commandstation-button-small|

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:

Welcome to DCC-EX TrackManager
===============================

*A first for the DCC & DC model railroading world.*

|EX-CS| is now a dual **Command Station** for both **Digital Command Control (DCC)** and **analogue (DC)** layouts.

With just a single |EX-CS| and a compatible throttle you can simultaneously run both your DCC Locos and analogue DC Locos with road number IDs as throttle addresses from 1 to 10239 to control and drive them on multiple separate insulated tracks/districts.

----

Track Manager Modes
===================

By default the outputs of a Motor Driver are set to DCC. For Motor Drivers with two outputs one will be MAIN and one will be PROG.  These, and any additional outputs, can be set to a number of different modes, not just DCC.

Valid Modes are:

  * :ref:`DCC modes <trackmanager/index:changing a motor driver output to a different dcc mode>`
  
    * MAIN
    * MAIN_INV
    * MAIN_AUTO
    * PROG
    * NONE
    
  * :ref:`DC modes <trackmanager/index:changing a motor driver output to dc>`
  
    * DC
    * DC_INV [#tm1]_
    * DCX [#tm1]_
    * NONE

.. [#tm1] DC_INV / DCX is DC with an opposite polarity. Like NMRA modular layout track B which is wired left rail positive (+) and right rail negative (-)


.. flat-table::
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - :cspan:`1` Option
    - _INV
    - _AUTO
    - Notes

  * - ``MAIN``
    - ✓
    - ✓
    - ✓
    -

  * - ``PROG``
    - ✓
    - 
    -
    - 

  * - ``DC``
    - ✓
    - ✓ [#tm2]_
    - ✓
    - Motor drivers with brake pin only

  * - ``BOOST``
    - ✓
    - ✓
    - ✓
    - ESP32 microcontrollers only

  * - ``EXT``
    - ✓
    - 
    - Reserved for future use

  * - ``NONE``
    - ✓
    - 
    - 

.. [#tm2] With special alias of ``DCX`` for ``DC_INV``

----

Requirements (DCC and DC)
=========================

DCC Requirements
----------------

Nothing special or extra is required for any of the DCC modes.

----

DC Requirements
---------------

To run DC locos with your |EX-CS| you will need:

* An |EX-CS|.
* A motor shield with a brake pin. |BR| (See the list of compatible boards at :ref:`reference/hardware/motor-boards:trackmanager dc compatible boards`.) |BR| (The |EX-CSB1-SHORT| and |EX-MS| have a brake pin.)
* A controller that can be used with the |EX-CS|.

*No additional external DCC decoders are required for DC (PWM) track assignments, and a single* |EX-CS| *is the only hardware needed for full functionality.*

Note: An additional suggested precaution is to add 4 fuses on wires (-b +b, -a +a) to the |EX-CS| connections. Use 2A fuses for the standard L298P motor shield or 5A fuses for the |EX-MS| and other the larger motor boards.

|HR-DASHED|

Additional Technical Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are interested in the technical details of DC Pulse Width Modulation (PWM) visit our :doc:`/reference/hardware/dcc-vs-dc` page.

----

Changing a Motor Driver Output to a different DCC mode
======================================================

You can change any output of the Motor Driver either temporarily or permanently (every time the |EX-CS| starts).

.. contents:: In this Section
    :depth: 1
    :local:
    :class: in-this-section

|HR-DASHED|

Temporarily Changing to a Different DCC Mode
--------------------------------------------

There are several ways to temporarily change a Motor Driver Output to a different DCC Mode:

* By issuing a command to the the |EX-CS|
* By using the |TM| feature in |Engine Driver| or |EX-TB|
* By creating |EX-R| Routes that can the activated in your throttle app.

Using Engine Driver or EX-Toolbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Issuing a command (DCC)
~~~~~~~~~~~~~~~~~~~~~~~

You can issue |DCC-EX Native Commands| to the |EX-CS| to change the output modes with |Engine Driver|, |EX-TB|, |Device Monitor|, |EX-WT| or the |IDE Serial Monitor|.

1. Open the |Serial Monitor| (or TrackManager page in |Engine Driver| or |Ex-TB|)

2. Issue the following command. |BR| Note that in this example I am setting output B to be DCC MAIN.

.. code-block:: c++

  <= B MAIN>

Note the track power is immediately turn off anytime you change the track mode.

|HR-DASHED|

Creating a Route (DCC)
~~~~~~~~~~~~~~~~~~~~~~

Using a Route will set a specific loco number to be associated with DC output. This is a permanent relationship, in that it will be associated every time you start the |EX-CS|.

We will be adding some instructions the ``myAutomation.h`` file a re-uploading the Command Station software your |EX-CS|.

1. Re-run the |EX-I| selecting the options you would normally choose, but of the last page before loading you also select ``Advanced Config``, before clicking the :guilabel:`Advanced Config` button.
2. This will take you to the ``Advanced Configuration`` page, where you will have two (or possibly more) edit regions. One will be labelled ``myAutomation.h``.
3. in the ``myAutomation.h`` edit region you will need to type or copy the something like the following. |BR| Note that in this example I am setting output B to be DCC MAIN.

.. code-block:: c++

 ROUTE(3, "Set Output B to DCC MAIN") // 3 is the sequence identifier  it must be unique
   SET_TRACK(B,MAIN)  // Set Track B to DCC MAIN
   DONE

4. Then Load the Command Station software as normal (on the next page)

Note the track power is immediately turn off anytime you change the track mode. you may wish to add ``SET_POWER( track, ON/OFF )`` after the ``SET_TRACK()`` command. e.g. ``SET_POWER(B ON)``.

|HR-DASHED|

Permanently Changing the DCC Mode
---------------------------------

By default the outputs of a Motor Driver are set to DCC. For Motor Drivers with two outputs one will be ``MAIN`` and one will be ``PROG``.  These, and any additional outputs, can be set to a number of different modes, not just DCC.

You can set any Motor Driver output to be a specific DCC mode every time the |EX-CS| starts up. (If you wish, at any time you can subsequently temporarily change it any other DC or DCC mode.)

This process is similar to a the 'Route' process in the previous section but will happen automatically at start-up rather than when you select the route.

We will be adding some instructions the ``myAutomation.h`` file a re-uploading the Command Station software your |EX-CS|.

1. Re-run the |EX-I| selecting the options you would normally choose, but of the last page before loading you also select ``Advanced Config``, before clicking the :guilabel:`Advanced Config` button.
2. This will take you to the ``Advanced Configuration`` page, where you will have two (or possibly more) edit regions. One will be labelled ``myAutomation.h``.
3. in the ``myAutomation.h`` edit region you will need to type or copy the something like the following. |BR| Note that in this example I am setting output B to be DCC MAIN.

.. code-block:: c++

 AUTOSTART
   SET_TRACK(B,MAIN)  // Set Track B to DCC MAIN
   DONE

4. Then Load the Command Station software as normal (on the next page)


Note the track power is immediately turn off anytime you change the track mode. you may wish to add ``SET_POWER( track, ON/OFF )`` after the ``SET_TRACK()`` command. e.g. ``SET_POWER(B ON)``.

----

Changing a Motor Driver Output to DC
====================================

You can change any output of the Motor Driver either temporarily or permanently (every time the |EX-CS| starts).

.. contents:: In this Section
    :depth: 1
    :local:
    :class: in-this-section

|HR-DASHED|

Controlling the output not the loco
------------------------------------

It is important to note a key difference between controlling a DCC loco on a DCC output/track, and controlling a DC loco on a DC output/track.

In the case on DCC, you select the individual DCC address of the loco and you control just that loco regardless of how many other DCC locos are on the track.

.. note:: 
  :class: note-float-right
  
  If you plan to also use DCC, when specifying a DC address, avoid using one of your existing loco DCC addresses. 
  
  Otherwise a command sent to control a DC output/track will also operate your DCC loco with the same address.

In the case of DC it is very different. You control the whole output/track and all the locos on it simultaneously.  *To do so we must assign that output/track an address.*  It is not a real DCC Address, but from the perspective of your controller, it will think it is a DCC Address.

When you read further just remember that the address assigned DC output/track is not really the loco.  *It is an address for the output/track.*

|HR-DASHED|

Temporarily Changing to DC
--------------------------

There are several ways to temporarily change a Motor Driver Output to DC:

* By issuing a command to the the |EX-CS|
* By using the |TM| feature in |Engine Driver| or |EX-TB|
* By creating |EX-R| Routes or Automations that can the activated in your throttle app.

Using Engine Driver or EX-Toolbox (DC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Engine Driver| has specific TrackManager features that allow you to alter the output modes.  See the :ref:`throttles/software/engine-driver-native-protocol:trackmanager control` Engine Driver page for details.

|EX-TB| has specific TrackManager features that allow you to alter the output modes. See the :ref:`ex-toolbox/using:track manager` page for details.

|HR-DASHED|

Issuing a Command (DC)
~~~~~~~~~~~~~~~~~~~~~~

You can issue |DCC-EX Native Commands| to the |EX-CS| to change the output modes with |Engine Driver|, |EX-TB|, |Device Monitor|, |EX-WT| or the |IDE Serial Monitor|.

1. Open the |Serial Monitor| (or TrackManager page in |Engine Driver| or |Ex-TB|)

2. Issue the following command |BR| note that in this example I am setting output B to be DC and to be assigned to the Loco Address 1225.

.. code-block:: c++

  <= B DC 1225>  // Set track B to DC mode with address 1225

Note the track power is immediately turn off anytime you change the track mode.

|HR-DASHED|

Creating a Route (DC)
~~~~~~~~~~~~~~~~~~~~~

Using a Route will set a specific loco number to be associated with DC output. This is a permanent relationship, in that it will be associated every time you start the |EX-CS|.

We will be adding some instructions the ``myAutomation.h`` file a re-uploading the Command Station software your |EX-CS|.

1. Firstly you will need to select an address (1-10239) which will be assigned to the DC output.  If you are also using using DCC on another output, pick a number that will not conflict with any of your own loco's addresses.
2. Next re-run the |EX-I| selecting the options you would normally choose, but of the last page before loading you also select ``Advanced Config``, before clicking the :guilabel:`Advanced Config` button.
3. This will take you to the ``Advanced Configuration`` page, where you will have two (or possibly more) edit regions. One will be labelled ``myAutomation.h``.
4. in the ``myAutomation.h`` edit region you will need to type or copy the something like the following |BR| note that in this example I am setting output B to be DC and to be assigned to the Loco Address 1225.

.. code-block:: c++

 ROUTE(1, "Set Output B to DC 1225") // 1 is the sequence identifier  it must be unique
   SETLOCO(1225)    // Assign Loco 1225
   SET_TRACK(B,DC)  // Set Track B to DC with address 1225
   DONE

5. Then Load the Command Station software as normal (on the next page)

Note that this will make the output DC if you activate the route in you controller.  See :ref:`trackmanager/index:controlling a dc loco` for more information. 

Note the track power is immediately turn off anytime you change the track mode. you may wish to add ``SET_POWER( track, ON/OFF )`` after the ``SET_TRACK()`` command. e.g. ``SET_POWER(B ON)``.

|HR-DASHED|

Creating an Automation (DC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using an Automation rather than a Route creates a temporary association between a loco address and the DC output.  It takes whatever address you currently have selected in the controller and assigns that to the output.

We will be adding some instructions the ``myAutomation.h`` file a re-uploading the Command Station software your |EX-CS|.

1. Firstly you will need to select an address (1-10239) which will be assigned to the DC output.  If you are also using using DCC on another output, pick a number that will not conflict with any of your own loco's addresses.
2. Next re-run the |EX-I| selecting the options you would normally choose, but of the last page before loading you also select ``Advanced Config``, before clicking the :guilabel:`Advanced Config` button.
3. This will take you to the ``Advanced Configuration`` page, where you will have two (or possibly more) edit regions. One will be labelled ``myAutomation.h``.
4. in the ``myAutomation.h`` edit region you will need to type or copy the something like the following |BR| note that in this example I am setting output B to be DC and to be assigned to the Loco Address 1225.

.. code-block:: c++

 AUTOMATION(2, "Set Output B to DC") // 2 is the sequence identifier  it must be unique
   SET_TRACK(B,DC)  // Set Track B to DC
   DONE

5. Then Load the Command Station software as normal (on the next page)

Note that this will make the output DC if you activate the route in you controller.  See :ref:`trackmanager/index:controlling a dc loco` for more information. 


Note the track power is immediately turn off anytime you change the track mode. you may wish to add ``SET_POWER( track, ON/OFF )`` after the ``SET_TRACK()`` command. e.g. ``SET_POWER(B ON)``.

|HR-DASHED|

Permanently Changing To DC
--------------------------

By default the outputs of a Motor Driver are set to DCC. For Motor Drivers with two outputs one will be ``MAIN`` and one will be ``PROG``.  These, and any additional outputs, can be set to a number of different modes, not just DCC.

You can set any Motor Driver output to be DC every time the |EX-CS| starts up. (If you wish, at any time you can subsequently temporarily change it any other DC or DCC mode.)

This process is similar to a the 'Route' process in the previous section but will happen automatically at start-up rather than when you select the route.

We will be adding some instructions the ``myAutomation.h`` file a re-uploading the Command Station software your |EX-CS|.

1. Firstly you will need to select an address (1-10239) which will be assigned to the DC output.  If you are also using using DCC on another output, pick a number that will not conflict with any of your own loco's addresses.
2. Next re-run the |EX-I| selecting the options you would normally choose, but of the last page before loading you also select ``Advanced Config``, before clicking the :guilabel:`Advanced Config` button.
3. This will take you to the ``Advanced Configuration`` page, where you will have two (or possibly more) edit regions. One will be labelled ``myAutomation.h``.
4. in the ``myAutomation.h`` edit region you will need to type or copy the something like the following |BR| note that in this example I am setting output to be DC an to be assigned to the Loco Address 1225.

.. code-block:: c++

 AUTOSTART
   SETLOCO(1225)    // Assign Loco 1225
   SET_TRACK(B,DC)  // Set Track B to DC with address 1225
   DONE

5. Then Load the Command Station software as normal (on the next page)


Note the track power is immediately turn off anytime you change the track mode. you may wish to add ``SET_POWER( track, ON/OFF )`` after the ``SET_TRACK()`` command. e.g. ``SET_POWER(B ON)``.

----

Selecting A DC loco to control
==============================

Remember that the address you assigned DC output/track above is not really the loco.  *It is an address for the output/track.*

While the process to control a loco is exactly the same as a DCC loco, the process to select it will vary depending on *how* you configured the Motor Driver Output to be DC.

.. contents:: In this Section
    :depth: 1
    :local:
    :class: in-this-section

If you set the Output to be permanently DC
------------------------------------------

1. You will need to select the Loco Address you assigned to the output when you setup the permanent assignment.

|HR-DASHED|

If you used a Route (DC)
--------------------------------

1. Go to the list of Routes in your throttle app
2. Activate the Route that you created
3. You will then need to select the Loco Address you assigned to the output when you created the route.

|HR-DASHED|

If you used an Automation (DC)
--------------------------------------

1. You will then need to select any Loco Address that you wish to use
2. Go to the list of Routes and Automations in your throttle app
3. Activate the Automation that you created

|HR-DASHED|

If you used Engine Driver, EX-Toolbox or a Command (DC)
-------------------------------------------------------

1. You will need to select the Loco Address you assigned to the output to DC.

----

Controlling a DC Loco
=====================

Any throttle that connect to an |EX-CS| can control analogue (DC) locos just as easily as DCC locos. Throttle Compatibility:

  * WiFi Throttles (e.g. |Engine Driver|, |wiThrottle| and many others)
  * The DCC-EX browser based |EX-WT|
  * Other wired throttles to operate your DCC layout and your DC layout, either separately or a simultaneous combination of the two modes

.. warning:: 

  Never drive a loco, DC or DCC, from an |EX-CS| controlled track or district to any other DCC or DC *System*.

|HR-DASHED|

Changing the Pulse Width Frequency
----------------------------------

**Frequency of PWM in DC Operation** - PWM can use a variety of frequencies for the pulses it sends, and this can alter motor behaviour and noise etc. 

The default frequency used for the |EX-CSB1-SHORT| is 131H, but this can be varied on-the-fly using the virtual DCC functions 29-31 to allow you to alter the frequency to better suit your loco's motor. This can of course be done during running from the throttle.

Just acquire the loco number you have assigned to your DC Output. Then select one of Functions 29, 30 or 31:

* No Function selected: Default - low frequency 131Hz
* F29: Mid frequency - 490Hz
* F30: High frequency - 3400Hz
* F31: Supersonic - 62500Hz

Trial and error will be needed for specific locos that do not respond well to the defaults (low) frequency setting.

Note that these functions are not cumulative - setting F30 overrides F29 and setting F31 overrides F29 & F30.

----

Replacing or Integrating Into Your Current Layout
=================================================

.. warning:: 
  :class: warning-float-right

  If you plan to use multiple |DC| and/or |DCC| blocks, these should not be using a common ground rail, and only use dual insulated tracks.

Existing analogue DC layouts will have standard DC controllers/transformers on one or more separate DC tracks/districts/blocks.

If you have more than one controller, they may have DPDT centre-off switches between two controller powered blocks. 

You will be replacing this kind of legacy analogue DC described above with a single |EX-CS|. It includes a software switching implementation, allowing you to easily and quickly switch between the two |DCC| and |DC PWM| modes on any of the A thru H dual insulated tracks/districts in real time.

This also means that, if you wish, you can remove any physical hardware DPDT switches that were used to switch between standard DC controllers/transformers.

This is all done through a single |EX-CS|. And no we're not using another Expensive DCC decoder under the table on each Track/District/Block to address that section of track. The capability is built into the |EX-CS|.

Below is an example of a very simple DC layout with two DC controllers/transformers, with one for each track.

.. figure:: /_static/images/layouts/dc-layout-1.png
  :alt: DC Layout - 2 Blocks
  :scale: 50%

  DC Layout - 2 Blocks - DC controllers/transformers

With an |EX-CS| with both outputs set to |DC PWM|, the wiring for the same layout is a very simple swap.

.. figure:: /_static/images/layouts/dc-layout-2.png
  :alt: DC Layout - 2 Blocks
  :scale: 50%

  DC Layout - 2 Blocks - EX-CSB1


.. warning::

  The ready-to-run |EX-CSB1-SHORT| and the do-it-yourself |EX-CS| default to |DCC| on both outputs!  
  
  You must use the instructions above before placing a DC loco on the track, or you may risk damaging the loco.


.. TODO XXX see if there is anything else in these two paragraphs that that should be retained
.. Existing analogue DC layouts which have standard DC transformers on two or more separate DC tracks/districts/blocks and/or also have a second separate proprietary DCC command station would have in place a section of dead rail, an electric relay, or a DPDT centre-off switch between the two types of controller powered stations. These should not be using a common ground rail, and only use dual insulated tracks.
.. You will be replacing this kind of legacy analogue DC and proprietary DCC installation described above with a single |EX-CS| which will have a software switching implementation, allowing you to easily and quickly swap between the two DCC (PWM) and DC (PWM) modes on any of the A thru H dual insulated tracks/districts in real time.


.. TODO:: Add examples and diagrams 

----

|HR-DASHED|

----

TrackManager Technical Details and Detailed Instructions
========================================================

Below is a more detailed and technical discussion of the topics above.

How do you run a EX-CommandStation in DC (PWM) mode?
----------------------------------------------------

Using |TM| with simple easy commands from a throttle or from a |serial monitor| we can change any insulated track A-H from DCC (PWM) to DC (PWM) and back in real time.

  * Valid DCC modes are ``MAIN``, ``MAIN_INV``, ``MAIN_AUTO``, ``PROG``, and ``NONE``
  * Valid DC modes are ``DC``, ``DC_INV`` / ``DCX``, and ``NONE``
  
DC_INV / DCX is DC with an opposite polarity like NMRA modular layout track B which is wired left rail positive (+) and right rail negative (-)

This allows a throttle on track B set to DC_INV / DCX to operate in forward and reverse correctly for west bound engines

So, you can take a standard DC motor only loco's road number on the side of the loco and assign it to one or more of up to 8 tracks/districts/blocks labelled A thru H. Then enter that same number into a throttle and control that Address on each and every one of the assigned tracks.

  * Valid Cab addresses are 1 to 10239.
  * Invalid Cab address is 0 zero.

.. sidebar:: 

  We do not support Zero stretching / zero stretch address function, found on Digitrax and Lenz command Stations. See the ':ref:`reference/hardware/dcc-vs-dc:this is not zero stretching`' section for more information.

Place any analogue DC loco/engine on a TrackManager DC assigned track with our |EX-CS| and it sits there dead quiet with lights off. When the throttle speed is increased in either direction and then lights up and begins to move.

A DCC Loco with a DC enabled sound decoder also sits quietly and when the throttle increases the sound will turn on first then as you throttle up more it will begin moving.  You can throttle back until it stops but leave a little throttle speed on say 5% and the Sound will continue to play while it is stopped.

Throttle speed response for DC locos vary because the DCdistrict track is operating from 0Vdc to 16+Vdc ~PWM waveform signal. Locos operating on a DCdistrict with either WiFi Throttles and |EX-R| Automation scripts with |Engine Driver| Handoff run different DC motors at different speeds.

So a script for FWD(50) speed will run at completely different speeds for two different DC motors depending on their resistance and efficiency.  One crawls at 50 while the other one runs like a bat out of hell.

You can also run a DCC locos with DC Conversion CV enabled On and run on the DCdistrict, without having to change the decoder DCC address.

They will all run on that section of track.

DCC Sound Decoder locos with DC conversion enabled may be silent until the track reaches between 2v to 6Vdc then the Sound will start up, and between 3v to 8Vdc the motor will begin to respond and move depending on the manufacturer's decoder.

Controlling & Managing DCC-EX TrackManager modes
-------------------------------------------------

You can Assign Tracks/Districts to |DCC| and |DC| mode in four ways:

  1. Command Line via PC with |IDE Serial Monitor| or |JMRI| serial Traffic Monitor and it is sent through your USB connected cable.
  2. Create an |EX-R| myAutomation.h file Scripts for Track Manager assigned commands and they automatically appear in |Engine Driver| as GUI Automation [Handoff] and Route [Set] buttons, and in WiThrottle WiFi Throttle iOS as [Route] buttons, and on TCS Universal UWT-50 & 100 WiFi Throttle [Select Accry] lines.

  3. Enhanced |Engine Driver| WiFi Throttle Android app v2.35.169+ features;

    * Track/District Manager set mode screen by touching a track mode entering an address
    * Command Cmd Line |Serial Monitor| and enter them like in example (1) above but via WiFi Native mode

  4. New |EX-TB| WiFi Android app features;
  
    * Track/District Manager set mode screen by touching a track mode, entering an address
    * Command Cmd Line |Serial Monitor| and enter them like in example (1) above but via WiFi Native mode

New |Engine Driver| DCC-EX Native mode features now available today via Google Play Store:

  * `Engine Driver <https://play.google.com/store/apps/details?id=jmri.enginedriver>`_
  * `EX-Toolbox <https://play.google.com/store/apps/details?id=dcc_ex.ex_toolbox>`_

----

TrackManager Commands
---------------------

Sending commands from the |IDE Serial Monitor| or |JMRI| Send Command Line or a |Engine Driver| WiFi Throttle.

To display the current TrackManager configuration, use the command ``<=>`` an equal sign looks like a track.

The |Serial Monitor| will show current status, example; Track A as Main and Track B as PROG

  * <= A MAIN>
  * <= B PROG>

To change or configure the current track modes use the new command ``<= trackletter mode [address]>`` which has been added for Track Manager, where:

  * ``trackletter`` is A through H
  * ``mode`` is one of MAIN, MAIN_INV, MAIN_AUTO, PROG, DC, DC_INV / DCX, or NONE (DCX is DC with opposite polarity)
  * ``address`` is the Cab/Loco ID and is only required when specifying DC or DC_INV / DCX modes

.. code-block:: c++

  <= A MAIN>     // Set track A to MAIN DCC mode
  <= B PROG>     // Set track B to PROG DCC mode
 or
  <= A DC 1234>  // Set track A to DC mode with address 1234
  <= B DCX 4321> // Set track B to DC mode Opposite Polarity address 4321
                 // or any number you assign from 1 to 10239
  <= B NONE>      // Set track B disabled, like a staging yard when it gets too noisy.

.. note:: 

  You would then enter your Engine address on the throttle of 1234 and 4321 and drive them on the layout.

EXRAIL Scripts to Change Track modes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using |EX-R| functions inside myAutomation.h file to run Automation scripts to change track modes from DCC to DC and back.
my.Automation.h file

.. code-block:: c++

  //SET_TRACK(id,mode)
    SET_TRACK(A, MAIN)
    SET_TRACK(B, PROG)
    SET_TRACK(C, DC)
    SET_TRACK(D, DCX)

Note that the Address to be used for a DC or DC_INV / DCX block must be set before the ``SET_TRACK`` command e.g.

.. code-block:: c++

    SETLOCO(1225)
    SET_TRACK(C, DC)
    
|HR-DASHED|

EXRAIL list of Track Manager Functions for Engine Driver Automatic Assign [Handoff] buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a |EX-R| Automation script we could assign a track mode to DC and wait for a |Engine Driver| to Assign the Current Selected Active Engine Address and drive Manually through the district on the layout.

 See the third Engine Driver Throttle image 'Districts A thru B with [Set] buttons at the end.

.. code-block:: c++

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
 AUTOMATION(504, "District A DCX")    // Alternate DC_INV / DCX track A Changed to Opposite Polarity
  SETLOCO(1)
  SET_TRACK(A,DCX) PRINT("District A DC_INV/DCX Opposite Polarity") // Track A Opposite Polarity DC    
  DONE
 AUTOMATION(505, "District A NONE")    // A Track disabled
  SET_TRACK(A, NONE) PRINT ("District A disabled")
  DONE
 Copy and repeat AUTOMATION(506-510, District B  mode)
  and create any additional combinations or tracks C - H as you add more motor boards.

|HR-DASHED|

EXRAIL Track Manager Functions for Engine Driver 'Automation' [Handoff] buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a |EX-R| Automation script we could a Set a Loco Address to a specific track in DC mode and have it run on Automation through the layout.
 See the sixth Engine Driver Throttle image 'EXRAIL 202 Roundhouse to Turntable Back & Forth - Timed' [Handoff] button at the end.

.. code-block:: c++

 AUTOMATION(202,"Roundhouse to Turntable Back & Forth -Timed")
   SETLOCO(1225)
   SET_TRACK(B,DC)
   Run a your Roundhouse script blow whistle, run Forward delay wait and run Reverse delay stop       
   DELAYRANDOM(msec, msec) // randomise the run time between runs
   DONE

|HR-DASHED|

EXRAIL Track Manager Functions for Engine Driver 'Route' [Set] buttons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In an EXRAIL Automation script we could Set a Loco Address to a specific track in DC mode and Manually run a preassigned address on the layout.

.. code-block:: c++

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

|HR-DASHED|

EX-CommandStation with EXRAIL & TrackManager
--------------------------------------------

Cool thing is the new |EX-R| Automation(n) & Routes(n) work the same with DCC engines on MAIN tracks and the DC engines on DC or DC_INV / DCX tracks, along with the Sensors, Servos /Turnouts, Signals & MP3 Sound DFPlayer triggers with little or no script changes other than maybe the FWD(n) & REV (n) Speeds.

With the new DCC-EX direct WiFi Discovered Server you can connect |Engine Driver| & other WiThrottle app based throttles directly and have |EX-R| [Handoff] & [Set] buttons to run |EX-R| scripts from the throttles.

These are DCC-EX Major feature/benefits because with other systems you'll have to use a PC computer or Pi processor & |JMRI| for WiThrottle Server throttle access and you have to write two different |JMRI| Jython.py scripts and then Setup Tools> Tables> Routes for for both DCC and DC automation & routes runs.

|HR-DASHED|

Modular Layouts
---------------

DCC-EX TrackManager 4.2.50+ is perfect for NMRA DCC Standards Modular Layouts which have two MAIN tracks/districts,
Track A and Track B with sidings;

* Track A (east bound) wired rails L-  R+
* Track B (westbound) which also have all the siding and spurs, wired rails L+  R-

You can set each district separately as mode

* DCC for MAIN, MAIN_INV, MAIN_AUTO, PROG or NONE
* analogue for DC, DC_INV / DCX or NONE

DC_INV / DCX is Opposite Polarity and is what you set Block B to when you want it in DC mode because it is wired to NMRA Modular DCC Standards L+, R-.

.. Using the TrackManager Function commands you can run the any layout as
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. 
.. .. code-block:: c++
.. 
..  Track A & Track B
..    MAIN & PROG    (Use JOIN function for a Programming track to make a MagicTrack) 
..    MAIN & MAIN
..    PROG & MAIN
..    MAIN & DC
..    PROG & DC
..      DC & MAIN
..      DC & PROG
..      DC & DC
..      DC & DCX
..  or any combination with up to 8 separate dual insulated tracks/districts from A - H.
.. 
.. All done through the free |DCC-EX| TrackManager commands.

----

EXRAIL examples
===============

Example - EXRAIL Scripts running on Engine Driver App (Android)
----------------------------------------------------------------

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
 - Takes the current selected Active Throttle Engine and assigns that Address to the DC or DC_INV / DCX track

.. figure:: /_static/images/track_manager/trackmanager_engine_driver_3.png
  :alt: Track Manager handoff
  :scale: 50%

  Track Manager - Engine Driver handoff

**Engine Driver DCC-EX Native mode**

 - TrackManager MAIN & PROG
 - With |DCC-EX| Cmd Line & |Serial monitor|
  
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

|HR-DASHED|

EXRAIL Functions on Smartphone Apps & Universal WiFi Throttles
--------------------------------------------------------------

The |Engine Driver| |EX-R| screens shown above are all created through user defined |EX-R| Automation(n) and Route(n) scripts which are automatically passed to both |Engine Driver| & WiThrottle App screens as well as the Train Control Systems TCS Universal WiFi UWT-50 and UWT-100 tactile throttles all via direct connect DCC-EX |WITHROTTLE PROTOCOL| interface.

Please see the specific Smartphone App & Universal WiFi Throttle instructions on how to enable their Preferences and Route screens. 
https://dcc-ex.com/throttles/index.html#withrottle-protocol-based-throttles
