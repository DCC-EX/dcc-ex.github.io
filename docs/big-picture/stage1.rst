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

There are a lot of different throttle otions available to control your trains and layout, including software applications available for your smart phone or computer and physical hardware options, both wired and wireless.

Going in to any detail on the myriad of options available is well outside the scope of this exercise, so on this page we will be focusing on the four options most commonly used with |EX-CS|: |EX-WT|, |Engine Driver|, |wiThrottle|, and |JMRi|.

For other throttle options, refer to the :doc:`/ex-commandstation/advanced-setup/controllers` page for further information on choosing a throttle, and you can also refer to the  :doc:`/throttles/index` section for more information on the various throttle options available.

What to expect to learn from stage 1
====================================

At the end of this stage, we expect you will have learnt the following:

* How to run a train on your direct connected |EX-CS| with |EX-WT|
* How to run a train on your WiFi enabled |EX-CS|
* How to run a train on your |JMRI| connected |EX-CS|
* How to run more than one train (Individual or Consist/Multiple Units)
* How to program a decoder using |JMRI|

----

Run a train using EX-WebThrottle
================================

If you're just starting out with |EX-CS|, or have a minimal system with no WiFi or Ethernet connection options, then a great way to start simply is by using |EX-WT| via your direct USB connection.

This is by far the simplest option to verify your |EX-CS| is set up and working correctly, as you don't need to install any software or worry about any network connections to get your first train running on your layout.

While there is a lot more detail on the :doc:`/ex-webthrottle/index` page, we will give you a very quick start guide here to get a single train running with your |EX-CS|.

Firstly, launch :guilabel:`EX-WebThrottle` in your Chromium based web browser (Google Chrome, Microsoft Edge, or Opera).

.. rst-class:: dcclink

   `Try It Now <https://DCC-EX.github.io/WebThrottle-EX>`_

Once you have |EX-WT| opened in your browser, follow these steps to get your train running:

* Ensure your |EX-CS| is connected to your computer via the USB cable
* In the top right corner, ensure "Serial" is selected from the pull down menu, then click the :guilabel:`Connect DCC++ EX` button
* A pop up window should appear, prompting you to choose your COM port
* Select the COM port then click the :guilabel:`Connect` button, and the button in the top right corner should change to :guilabel:`Disconnect DCC++ EX` with a green circle to the left
* Turn track power on with the :guilabel:`Power` button
* Type the DCC address of your loco into the "Locomotive ID" text box, then click the :guilabel:`>` button to set it
* You can now use the throttle slider or :guilabel:`+` and :guilabel:`-` buttons to set the speed, and the slider in the centre of the screen to set forward, reverse, stop, or EStop
* The function buttons to the right can also be used to set the various functions supported by your decoder

Enjoy running your train!

----

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
   
   * (The three dots or bars) then 'Power'.  Then click the :guilabel:`power` button till it goes green. (May require more than one click)
   * The two red LEDs, for the main track, on the Motor board will turn on
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

.. note::
  :class: note-float-right

  The free version of wiThrottle ('wiThrottle Lite') only controls one loco at a time and does not offer turnout control or DCC track power control. (Note: EX-CommandStation can be configured to automatically turn the track power on. See the :ref:`EX-RAIL examples <ex-rail/examples:Turn Track Power On at Startup>`.)
  
  The paid version WiThrottle can control multiple locos, can create and control consists, can control turnouts and routes, and can control DCC track power.

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

  * It will not find the |wiThrottle Server| automatically
  * Enter:

    * The IP Address: 192.168.4.1
    * The Port: 2560

  * |wiThrottle| should then connect 

* If you are using |Station Mode| 
  
  * It should find the |wiThrottle Server| and automatically connect to it

* You should then see the 'Address Screen'
* Turn the track power on by selecting the 'settings' tab and clicking on the ``Track Power``

   * The two red LEDs, for the main track, on the Motor board will turn on

* Go back to the 'Address' tab
* Enter the DCC Address of the loco you put on the track in the ``Keypad`` field
* Select ``Long`` or ``Short`` (normally if the address is less than 127, it should be a 'Short' address.)
* Click the :guilabel:`Set` button
* The address should appear in the green box at the top left.
* Select the 'Throttle' tab
* You can now use the sliders to move your train 

See :doc:`WiThrottle Page </throttles/software/withrottle>` for details on how to install and run |wiThrottle|.

----

Run a train on your JMRI connected EX-CommandStation
====================================================

If when you assembled your |EX-CS| configurated to Connect to JMRI, then you will have the ability to connect to your Command Station directly (using JMRI) to run your trains, or you can use smart phone. We are only going to cover three common options here:

* JMRI - PC (Windows, Apple OSX, Linux) 
* Engine Driver - For Android phones
* wiThrottle - for Apple iOS phones

JMRI (PC)
---------

* open **DecoderPro**
* Menu -> Actions -> New Throttle
* Turn on the power to the track via the button on the toolbar
  
  * Click the :guilabel:`Power` button till it turns green

* Enter the DCC Address of the loco you put on the track in the field in the Address Panel
* Click :guilabel:`Set`
* you can now use the sliders to move your train

Engine Driver (via JMRI)
------------------------

Before |Engine Driver| or |wiThrottle| can be run via |JMRI|, the JMRI WiThrottle server must be started.  It can be started manually by :menuselection:`menu --> actions --> start withrottle server` or be configured to start automatically whenever JMRI is started
:menuselection:`menu --> edit --> preferences --> start up --> add --> perform action --> start withrottle server`` then save, exit, restart JMRI. A wiThrottle server window should open showing wiThrottle server is running.

* Open the network settings on your phone
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

.. note:: 
  :class: note-float-right

  The free version of wiThrottle ('wiThrottle Lite') only controls one loco at a time and does not offer turnout control or DCC track power control. (Note: JMRI can be configured to automatically turn the track power on.)
  
  The paid version WiThrottle can control multiple locos, can create and control consists, can control turnouts and routes, and can control DCC track power.

Before |Engine Driver| or |wiThrottle| can be run via |JMRI|, the JMRI WiThrottle server must be started.  It can be started manually by :menuselection:`menu --> actions --> start withrottle server` or be configured to start automatically whenever JMRI is started
:menuselection:`menu --> edit --> preferences --> start up --> add --> perform action --> start withrottle server`` then save, exit, restart JMRI. A wiThrottle server window should open showing wiThrottle server is running.

* Open the network settings on your phone
* Change to same network of the PC that JMRI is on
* Start the |wiThrottle| App
* |wiThrottle| will try to find the |wiThrottle Server| on the |EX-CS|

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

----

Run more than one train (Individual or Consist/Multiple Units)
==============================================================

Engine Driver (Multiple Trains)
-------------------------------

|Engine Driver| can optionally show throttle screen layouts that can provide for between 1 and 6 separate throttles. Each throttle can control and unlimited number of loco as a Consist / Multiple Unit train.

Multiple Throttles
^^^^^^^^^^^^^^^^^^

To have more than one throttle you need to select a Throttle Screen Layout that has more than one throttle on it.

Use the ``Throttle Screen Layout`` preference to select a layout that supports more than one throttle (:menuselection:`menu --> Preferences --> Throttle Screen Appearance Preferences --> Throttle Screen Layout`).  The numbers in brackets after the Layout name are the number of throttles that the layout supports.

Where a layout supports a range of throttles, select the number that you want to show with the ``Number of Throttles`` preference (:menuselection:`menu --> Preferences --> Throttle Screen Appearance Preferences --> Number of Throttles`).  

See the `Throttle Screen Appearance Preferences <https://flash62au.github.io/EngineDriver_Home/configuration/preferences.html#throttle-screen-appearance-preferences>`_ page on the main |Engine Driver| help sites for detailed information on the options that each Throttle Screen Layout offers.

Consist / Multiple Unit train
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adding additional locos to the Consist / Multiple Unit train is identical to the process of selecting a single loco.  Simply click on the :guilabel:`Select` button, which will be showing the name or address of any locos already selected.

After selecting each additional loco, the Consist Edit screen will be shown. This allows you to:

* Change the facing of each loco (except the front loco)
* Change the order of the locos in the Consist / Multiple Unit
* Remove locos from the Consist / Multiple Unit


wiThrottle (Multiple Trains)
----------------------------

.. note:: 
  :class: note-float-right

  The free version of |WITHROTTLE| (WiThrottle Lite) does not provide any options for running multiple trains or Consisted / Multiple Unit trains.  You need to purchase the paid/full version.

.. todo:: LOW - Stage 1 - wiThrottle - Multiple Trains


----

Program a decoder's DCC address
===============================

|DCC-EX| does not currently provide any apps with a user friendly interface for programming DCC decoders.

At least one Smart Phone App (:doc:`/throttles/software/rtdrive-dccpp`) can program decoders on |EX-CS| but it is not particularly user friendly to do so.

As a result, we recommend using |JMRi| DecoderPro for programming decoders.  It provides plain English descriptions of all the CVs of a huge number of different decoders, is very well supported, runs on the major PC operating systems, and is free and open source.

Programming options
-------------------

There are two basic methods for programming decoders

* Using the Programming Track (Service Mode programming)
* Programming on Main (POM or Ops Mode programming)

Programming on the programming track, or service mode programming, allows for receiving acknowledgement that programming changes have successfully been applied, and also allows |JMRi| DecoderPro to interrogate a decoder to make a best guess at the type of decoder that's installed, what the address is, and so forth.

Programming on main, also known as POM or ops mode programming, doesn't allow for acknowledgement or reading of CVs, but is handy when simple changes need to be made while a loco is in operation.

We will outline how to use each option below to update a locomotive DCC decoder's address, as well as identify a loco that is currently on the programming track.

Service mode programming is the preferred method for making wholesale changes to decoder settings as you will receive positive feedback that changes have been made and, if you make a mistake with a DCC address, you can quickly read what has been programmed to correct the issue, or reset them to factory default settings and start again.

To program any other features, refer to the `DecoderPro user guide <https://www.jmri.org/help/en/html/apps/DecoderPro/index.shtml>`_.

JMRI (Programming Decoders)
---------------------------

|JMRI| is a PC based app that runs on Windows, Apple OSX, and Linux (including Raspberry Pi's Raspbian (RasPi)).

It relies on the |EX-CS| being connected to the PC running |JMRI|, normally by the USB cable. (It can be done over WiFi, but is not recommended).  This means that, even if you setup your |EX-CS| for Wifi you will need to connect it to the PC.  Don't worry, this will work without having to load the software on the |EX-CS| again.

Installing JMRI
^^^^^^^^^^^^^^^

To install |JMRi|, refer to the installation instructions on the `JMRI <https://www.jmri.org/help/en/manual/DecoderPro3/Installing_JMRI.shtml>`_ website.

Once |JMRi| is installed, launch DecoderPro. If you haven't previously used DecoderPro or any |JMRi| applications, you will need to setup your |EX-CS| connection. Refer to the `JMRi help page <https://www.jmri.org/help/en/html/hardware/dccpp/index.shtml>`_ for instructions on how to accomplish this.

Using the programming track (service mode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this point, DecoderPro will be open at the "Getting Started" screen, assuming you have not used it before, and have no roster entries defined. The loco to be programmed also must be placed on your programming track.

This is the process to create your first roster entry and set the desired DCC decoder address:

* Click the :guilabel:`New Loco` button on the menu bar at the top of the screen
* Click the :guilabel:`Read type from decoder` button at the bottom of the screen
* The most appropriate decoder should automatically be detected and selected automatically (multiple matches may be made, so select the most appropriate)
* Once only one decoder is selected, the "Create Basic Roster Entry" pane should appear to the right of the decoder list
* Enter the desired name in "Roster ID", enter the desired DCC address in the "Active Address" box, then click the :guilabel:`Write` button to write the new address to the decoder
* An "OK" should appear in the bottom left corner to indicate the write was successful
* Click :guilabel:`Save` to save your roster entry, and then either close the window or repeat the process for other locos

Once your roster entries are populated, if you forget which loco was programmed with what, place your loco on the programming track and click the :guilabel:`Identify` button on the top menu. DecoderPro will detect the decoder settings and, if they match an existing roster entry, this will be displayed.

To make further programming changes to your decoders, simply select the roster entry, make sure "Programming Track" is selected in the bottom right corner, then click the :guilabel:`Program` button which will open the full programming dialogue window.

For further information on programming in service mode, see `Service Mode Programmer <https://www.jmri.org/help/en/manual/DecoderPro3/Programmer_ServiceMode.shtml>`_ on the |JMRi| website.

Programming on main (POM or ops mode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you wish to set up a new roster entry for a loco that is already on your main track, or you don't have a programming track available, to a limited extent you can still do this through DecoderPro. You will, however, receive no acknowledgement that the changes have been written successfully.

This is the process to add a roster entry and set the desired DCC address:

Using POM only changes the loco you have selected, not all locos on the track.  Which is why you must select a loco first.  (Unlike the programming track where it changes everything on it)

.. warning:: 
  :class: warning-float-right

  You can theoretically change the DCC address using POM, but *only short addresses* (below 127) and some decoders don't even allow that.

* Use the :guilabel:`Power` button at the top of the window to turn track power on
* Click the :guilabel:`New Loco` button on the menu bar at the top of the screen
* Unlike the service mode process above, you will need to manually select which decoder is installed in the loco
* Once the decoder is selected, the "Create Basic Roster Entry" pane should appear to the right of the decoder list
* Enter the desired name in "Roster ID", enter the current DCC address in the "Active Address" box, then click the :guilabel:`Save` to save your roster entry, then close the "New Loco" window
* To set the desired DCC address, select the correct roster entry  *(See Warning)*
* Select "Programming on Main", then click the :guilabel:`Program` button
* Click the "Basic" tab, set the desired DCC address in the "Active Address" text box, then click the :guilabel:`Write changes on sheet` button  *(See Warning)*
* Close the "Program" window and when prompted, click the :guilabel:`Save and close` button

For further information on programming on the main track, see `Ops Mode Programming <https://www.jmri.org/help/en/manual/DecoderPro3/Programmer_OpsMode.shtml>`_ on the |JMRi| website.
