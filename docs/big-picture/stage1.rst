.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-BP-LOGO|

*********************************
Stage 1 - Running a Train
*********************************

|conductor|

.. sidebar:: 

   .. contents:: On this page
      :depth: 2
      :local:

Throttle options
================

There are lots of different throttle otions available to control your trains and layout, including software applications available for your smart phone or computer and physical hardware options, both wired and wireless.

Going in to any detail on the myriad of options available is well outside the scope of this exercise, so on this page we will be focusing on the three options most commonly used with |EX-CS|: |EX-WT|, |Engine Driver|, |wiThrottle|, and |JMRi|.

There is more information available in our :doc:`/throttles/index` section on the various throttle options available.

What to expect to learn from stage 1
====================================

At the end of this stage, we expect you will have learnt the following:

* How to run a train using our very own |EX-WT|
* How to run a train on your WiFi enabled |EX-CS|
* How to run a train on your |JMRI| connected |EX-CS|
* How to run more than one train (Individual or Consist/Multiple Units)
* How to program a decoder using |JMRI|

----

Run a train using EX-WebThrottle
================================



Run a train on your WiFi enabled EX-CommandStation
==================================================

If when you assembled your |EX-CS| with one of the common configuration options, then you will have a WiFi enabled Command Station, which will allow to run your trains with a smart phone. We are only going to cover two common options here:

* Engine Driver - For Android phones
* wiThrottle - for Apple iOS phones

Engine Driver (Android)
-----------------------

* If you have set up your |EX-CS| in |Access Point Mode| (The Recommended approach)
  
  * Open the network settings on you phone
  * Change to the network of the |EX-CS|
  
    * SSID (Network name) : 'DCCEX_xxxxxx' |BR| where the x's are the last 6 digits of your device' MAC address (unique to each device)
    * Password: 'PASS_xxxxxx' |BR| where the x's are the last 6 digits of your device' MAC address (same as above)

* If you have set up your |EX-CS| in |Station Mode| (The alternate approach)
  
  * open the network settings on you phone
  * change to your home network
  
    * use your normal home id and password 

* Start the |engine driver| App
* Go through the initial startup pages to set some basic configuration items
* On the 'Connection screen'
  
  * You should see 'DCCEX_xxxxxx' (as above) in the discovered servers list
  * Click on this. |BR| (As long as you did not change the IP address of the |EX-CS| when you ran |EX-I| then this should connect

* You should now be on the the 'Throttle screen'

* Turn on the power to the track via the menu 
   
   * (The three dots or bars) then 'Power'.  Then click the power button till it goes green. 9may require more than one click)
   * The four red LEDs on the Motor board will turn on
   * Click :guilabel:`Back`

* back on the 'Throttle screen'

  * Click one of the :guilabel:`Select` buttons
  
* This will have taken you to the 'Select Loco screen'

  * Enter the DCC Address of the loco you put on the track
  * Select ``Short`` or ``Long`` (normally if the address is less than 127, it will automatically assume it is short) 
  * Click :guilabel:`Aquire`

* Back on the 'Throttle screen' you can now use the sliders to move your train.

See :doc:`Engine Driver Page </throttles/software/engine-driver>` for details on how to install and run |Engine Driver|.

wiThrottle (iOS)
----------------

* If you have set up your |EX-CS| in |Access Point Mode| (The Recommended approach)
  
  * Open the network settings on you phone
  * Change to the network of the |EX-CS|
  
    * SSID (Network name) : 'DCCEX_xxxxxx' |BR| where the x's are the last 6 digits of your device' MAC address (unique to each device)
    * Password: 'PASS_xxxxxx' |BR| where the x's are the last 6 digits of your device' MAC address (same as above)

* If you have set up your |EX-CS| in |Station Mode| (The alternate approach)
  
  * Open the network settings on you phone
  * Change to your home network
  
    * Use your normal home id and password 

* Start the |wiThrottle| App
* |wiThrottle| will try to find the |wiThrottle Server| on the |EX-CS|
* If you are using |Access Point Mode| 

  * It should find the |wiThrottle Server| and automatically connect to it

* If you are using |Station Mode| 
  
  * It will not find the |wiThrottle Server| automatically
  * Enter:

    * The IP Address: 192.168.4.1
    * The Port: 2560

  * |wiThrottle| should then connect 

* You should then see the 'Address Screen'
* Turn the track power on by selecting the 'settings' tab and clicking on the ``Track Power``

   * The four red LEDs on the Motor board will turn on

* Go back to the 'Address' tab
* Enter the DCC Address of the loco you put on the track in the ``Keypad`` field
* Select ``Long`` or ``Short`` (normally if the address is less than 127, it should be a 'Short' address.)
* Click the :guilabel:`Set` button
* The address should appear in the green box at the top left.
* Select the 'Throttle' tab
* You can now use the sliders to move your train 

See :doc:`WiThrottle Page </throttles/software/withrottle>` for details on how to install and run |wiThrottle|.

Other Controllers
-----------------

.. todo:: LOW - Stage 1 - Wifi - Other Controllers

Look at the :doc:`/ex-commandstation/advanced-setup/controllers` page for the full list of controller (Throttle) options.

----

Run a train on your JMRI connected EX-CommandStation
====================================================

If when you assembled your |EX-CS| configurated to Connect to JMRI, then you will have the ability to connect to your Command Station directly (using JMRI) to run your trains, or you can use smart phone. We are only going to cover three common options here:

* JMRI - PC (Windows, Apple OSX, Linux) 
* Engine Driver - For Android phones
* wiThrottle - for Apple iOS phones

JMRI (PC)
---------

* open PanelPro
* Menu -> Actions -> New Throttle
* Turn on the power to the track via the menu 
  
  * Click the :guilabel:`Power` button till it turns green

* Enter the DCC Address of the loco you put on the track in the field in the Address Panel
* Click :guilabel:`Set`
* you can now use the sliders to move your train

Engine Driver (via JMRI)
------------------------

* Open the network settings on you phone
* Change to same network of the PC that JMRI is on
* Start the |engine driver| App
* If needed, Go through the initial startup pages to set some basic configuration items
* On the 'Connection screen'
* You should see 'My JMRI Railroad' (as above) in the discovered servers list. (Unless you have changed the name when you setup JMRI)
* Click on this
* You should now be on the the 'Throttle screen'
* Turn on the power to the track via the Menu 
   
   * (The three dots or bars) then 'Power'.  Then click the :guilabel:`Power` button till it goes green. (may require more than one click.)
   * The four red LEDs on the Motor board will turn on
   * Click :guilabel:`Back`

* back on the 'Throttle screen'

  * Click one of the :guilabel:`Select` buttons
  
* This will have taken you to the 'Select Loco screen'

  * Enter the DCC Address of the loco you put on the track
  * Select ``Short`` or ``Long`` (normally if the address is less than 127, it will automatically assume it is short) 
  * Click :guilabel:`Aquire`

* Back on the 'Throttle screen' you can now use the sliders to move your train.

See :doc:`Engine Driver Page </throttles/software/engine-driver>` for details on how to install and run |Engine Driver|.

wiThrottle (via JMRI)
---------------------

* Open the network settings on your phone
* Change to same network of the PC that JMRI is on
* Start the |wiThrottle| App
* |wiThrottle| will try to find the |wiThrottle Server| on the |EX-CS|
* If you are using |Access Point Mode| 

  * It should find the |wiThrottle Server| in |JMRI| and automatically connect to it

* You should then see the 'Address Screen'
* Turn the track power on by selecting the 'settings' tab and clicking on the ``Track Power``

   * The four red LEDs on the Motor board will turn on

* Go back to the 'Address' tab
* Enter the DCC Address of the loco you put on the track in the ``Keypad`` field
* Select ``Long`` or ``Short`` (normally if the address is less than 127, it should be a 'Short' address.)
* Click the :guilabel:`Set` button
* The address should appear in the green box at the top left.
* Select the 'Throttle' tab
* You can now use the sliders to move your train 

See :doc:`WiThrottle Page </throttles/software/withrottle>` for details on how to install and run |wiThrottle|.

Other apps
----------

There are lots of other options for throttles you can use with your |EX-CS|.

Look at the :doc:`/ex-commandstation/advanced-setup/controllers` page for the full list of controller (Throttle) options.


Run more than one train (Individual or Consist/Multiple Units)
==============================================================

Engine Driver (Multiple Trains)
-------------------------------

.. todo:: LOW - Stage 1 - Engine Driver - Multiple Trains

wiThrottle (Multiple Trains)
----------------------------

.. todo:: LOW - Stage 1 - wiThrottle - Multiple Trains

Other Controllers (Multiple Trains)
-----------------------------------

.. todo:: LOW - Stage 1 - other controllers - Multiple Trains

Program a decoder using JMRI
============================

|DCC-EX| does not currently provide any apps with a user friendly interface for programming DCC decoders.

At least one Smart Phone App (:doc:`/throttles/software/rtdrive-dccpp`) can program decoders on a |EX-CS| but it is not particularly user friendly to do so.

As a result, we recommend using JMRI's Decoder Pro for programming decoders.  It provides plain English descriptions of all the CVs of a huge number of different decoders. It is very well supported, runs on the major PC operating systems, is free and open source.

JMRI (Programming Decoders)
---------------------------

|JMRI| is a PC based app that runs on Windows, Apple OSX, and Linux (including Raspberry Pi's Raspbian (RasPi)).

It relies on the |EX-CS| being connected to the PC running |JMRI|, normally by the USB cable. (It can be done over WiFi, but is not recommended).  This means that, even if you setup your |EX-CS| for Wifi you will need to connect it to the PC.  Don't worry, this will work without having to load the software on the |EX-CS| again.

Installing JMRI
^^^^^^^^^^^^^^^

TODO

see https://www.jmri.org/help/en/manual/DecoderPro3/Installing_JMRI.shtml

Programming Track CS Programming on the Main
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two basic methods for programming decoders

* Using the Programming Track
* Programming on the Main


With "Programming on Main", where you can adjust things like sounds, throttle curves, speed matching, etc., but you can't get acknowledgment back from the loco on the main track. That is usually fine because you will know if a setting like a sound change "took" or not. We will have a section on programming on main.

Programming Track
^^^^^^^^^^^^^^^^^

see https://www.jmri.org/help/en/manual/DecoderPro3/Programmer_ServiceMode.shtml

TODO

Programming on the Main
^^^^^^^^^^^^^^^^^^^^^^^

or OPS Mode programming

https://www.jmri.org/help/en/manual/DecoderPro3/Programmer_OpsMode.shtml

