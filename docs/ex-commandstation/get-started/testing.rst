.. meta::
   :keywords: EX-CommandStation Command Station Testing

.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CS-LOGO|

***************
Test Your Setup
***************

|conductor|

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

This page is specifically written for someone who has installed *just* the recommended hardware (including WiFi). However it will generally be suitable for testing most other configuration options.

Testing control of a loco
=========================

There are two simple options for testing your setup described below:

* Using our |EX-WT| (recommended)
* using the |Engine Driver| app installed on an Android device, |BR| or the |wiThrottle| app installed on an iOS device

.. sidebar:: 

    |tinkerer| |engineer| |BR| Additional options (controllers) for testing and diagnosing issues are available and is described in the :doc:`/ex-commandstation/advanced-setup/controllers` page if needed .

Using EX-WebThrottle
--------------------

Connect Everything:

* Disconnect the |EX-CS| from the computer (that you used to load the software)
* Connect the wires from the motor shield to your main track
* Plug in the power supply for the Moto shield **only**
* Reconnect the |EX-CS| to the computer
* wait for about 30 seconds

.. NOTE:: 
   :class: note-float-right-narrow

   The programming track is for programming only. Make sure you are on the main track if you expect your loco to move or respond to light or sound commands.

.. figure:: /_static/images/installer/exwebthrottle.jpg
   :alt: EX-WebThrottle
   :scale: 80%

   EX-WebThrottle

Click this link: :doc:`EX-WebThrottle </throttles/software/ex-webthrottle>` to run |EX-WT| hosted on our site, or visit `GitHub <https://github.com/DCC-EX/WebThrottle-EX>`_ to get the latest version to run on your computer.

.. TODO:: URGENT This text needs to be expanded - Using EX-WebThrottle

Using Engine Driver or WiThrottle - Requires WiFi
-------------------------------------------------

.. NOTE:: 
   :class: note-float-right

   The programming track is for programming only. Make sure you are on the main track if you expect your loco to move or respond to light or sound commands.

Connect Everything

* Disconnect the |EX-CS| from the computer (that you used to load the software)
* Connect the wires from the 'main' terminals the motor shield to your main track
* Plug in the two power supplies (The one for the Arduino and the the one for the motor shield)
* wait for about 30 seconds

Using Engine Driver (Android)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /_static/images/installer/engine_driver.png
   :align: right
   :alt: Engine Driver
   :scale: 80%

   Engine Driver

You will need to install |Engine Driver| on your mobile device and then connect to the |EX-CS|, either directly with AP mode or through your router with Station Mode. You can then use your phone to control your trains.

.. note:: 
   :class: note-float-right

   If you have any difficulties check the :doc:`diagnosing-issues` page for assistance.

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

Using wiThrottle (Apple iOS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: 
   :class: note-float-right

   If you have any difficulties check the :doc:`diagnosing-issues` page for assistance.

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

.. warning:: 

   **Locos Can't Respond to Throttle Commands on the Programming Track!**

   We have repeated this in several places on the Website because it is such a common issue. The MAIN track is for running trains, the PROG (service track) is for programming your loco. **THE LOCO CANNOT RESPOND TO THROTTLE OR FUNCTION COMMANDS WHILE ON THE PROG TRACK** This is by design and part of the NMRA specification.

----

Next Steps - Run Your Trains
============================

*You now should have everything you need to run your trains.*

We suggest that you look at the :doc:`/big-picture/index` to get some additional guidance on running trains and the additional capabilities of |DCC-EX| that you may prove of interest.

You might also like to look at the other :doc:`Controllers (Throttles) </ex-commandstation/advanced-setup/controllers>` that are available.

If you are still having difficulties click :guilabel:`Next`.
