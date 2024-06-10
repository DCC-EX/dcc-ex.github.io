.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-bp.rst
|EX-BP-LOGO|

*********************************
Stage 2 - Adding a Roster
*********************************

|conductor| |tinkerer| |engineer| |support-button|

.. sidebar:: 

   .. contents:: On this page
      :depth: 1
      :local:

What to expect to learn from stage 2
====================================

At the end of this stage, we expect you will have learnt the following:

* How add a Loco Roster, including function labels, to your |EX-CS|
* How to add images for your locos (|Engine Driver| only)


Add a Loco Roster to your EX-CommandStation
===========================================

|EX-R|, the in-built automation capability in the |EX-CS| software also has the ability to store roster entries that can be served up to the various throttles.

To add a roster you need to:

#. create an 'myAutomation.h' file with roster entries in it
#. re-upload the software to the |EX-CS|


Create myAutomation.h
---------------------

In a text editor (e.g. notepad) create a new text file named 'myAutomation.h'. (Note the capital 'A' in the name.  The case of all the characters is important.)

If you are already using |EX-R| and have a myAutomation.h, then just the add ``ROSTER(...)`` lines near the top of the file.

Add a line that looks like:

.. code-block:: 
   
   ROSTER(999,"Loco Name","F0/F1/*F2/F3/F4/F5/F6/F7/F8")

Where:

* **999** - is the DCC address of your loco
* **Loco Name** - is anything you want to see as the name of this loco in the throttle apps
* **F0 F1 F3 ... F27**. - are the names that you want to see for the functions specific to this loco
* **\*F2** - note that if the function is 'momentary' rather than 'latching' (On/Off) then start the function label with a asterisk (\*).  The most common example of this is the Horn/Whistle which is commonly on F2.

Some more realistic examples might look like:

.. code-block:: 
   
   ROSTER(3,"Eng 3","F0/F1/*F2/*F3/F4/F5/F6/F7/Mute/F9//") // Address = 3, Loco Name = Eng 3, Function keys F0-F10
   ROSTER(1224,"PE 1224","") // Motor Only Decoder, But use Engine Driver 'Preferences >In Phone Loco 'Sound'
   ROSTER(1225,"PE 1225","Lights/Bell/*Whistle/*Short Whistle/Steam/On-Time/FX6 Bell Whistle/Dim Light/Mute")
   ROSTER(4468,"LNER 4468","//Snd On/*Whistle/*Whistle2/Brake/F5 Drain/Coal Shvl/Guard-Squeal/Loaded/Coastng/Injector/Shunt-Door ~Opn-Cls/Couplng/BrakeVlv/Sfty Vlv/Shunting/BrkSql Off/No Momentm/Aux3/Fade Out/F22 Res/F23/Res//Aux 5/Aux6/Aux7/Aux 8")


Note: Add additional 'ROSTER(...)' lines for all your locos

Unavailable Functions
^^^^^^^^^^^^^^^^^^^^^

If a function is not available leave the spot empty. (Don't even have the space character.)

For example: 

.. code-block:: 

   ROSTER(2825,"CN ES44AC","Headlight/Bell/*Horn/Coupler/Dynamic Brake///Flange Squeal/Startup & Shutdown")

Note the two missing text labels for positions F5 and F6. Engine Driver will skip those buttons and not display them at all in the interface since they do nothing for that loco.

Example of loco without sound:

.. code-block:: 

   ROSTER(2405,"AT&SF 2-8-0 2405","Headlight")

Note that it only has FO (the Headlight) and not following slashes.

..
   Locos With the Same DCC Address

   If you have two or more Loco with identical DCC Addresses, but with with decoder functions you need to make the "name" different or you'll get compile error 'Duplicate Case Value'.

   Examples of naming Different Locos identical DCC Addresses. Notice the different Function values in the following two examples:

   .. code-block:: 

      ROSTER(4468,"LNER 4468","//Snd On/*Whistle/*Whistle2/Brake/F5 Drain/Coal Shvl/Guard-Squeal/Loaded/Coastng/Injector/Shunt-Door ~Opn-Cls/Couplng/BrakeVlv/Sfty Vlv/Shunting/BrkSql Off/No Momentm/Aux3/Fade Out/F22 Res/F23/Res//Aux 5/Aux6/Aux7/Aux 8")

   For example, you can add a "-2" to the Second Loco DCC Address and Name:

   .. code-block:: 

      ROSTER(4468-2,"LNER 4468-2","Lights/Steam/*L~Whistle/*S~Whistle/*Whistle2/DoorSlam/Whl Slip/Coal Shvl/BlwDown/SftyVlv/Injector/CylnCock/Brake/Blower/Grd Whistle/Coupler/Fireman/Chuff-Coast/Aux Lghts")
   

Re-upload the EX-CommandStation software
----------------------------------------

Using EX-Installer
^^^^^^^^^^^^^^^^^^

The |EX-I| can make use of the config files from a 'saved' location.  

*If you have previously saved the config files...*

   At the end of the install process it will ask you if you want to save the config files. If you have said ``Yes`` (and put them in a folder well away from the EX-Installer folder) you can place your 'myAutomation.h' in that folder and rerun the |EX-I|. the |EX-I| will ask if you want to use existing config files. Just point it to where you saved and edited the file.

   The Roster will be automatically loaded with the |EX-CS| software.

*If you have not saved the config files...*

   Re-run the |EX-I|. Select the same options that you originally chose *and* also select the ``create myAutomation.h`` and the ``Advanced config`` options.  This will show a myAutomation.h window on the following page. Copy and paste your roster lines into this window then ``Compile and load`` the software.

   After the load finishes you will be asked to 'backup/save' the config files. Say `Yes` and put them in a folder well away from the EX-Installer folder. You can can then make direct edits to the file there, and when you next run |EX-I|, it asks if you want to use existing config files. Just point it to where you saved and edited the file.

   The Roster will be automatically loaded with the |EX-CS| software.

More information on the config files can be found on the :doc:`/ex-installer/managing-config-files` page.

.. warning:: 

   Never edit any files in the EX-Installer folder. Editing any files in the EX-Installer folder will **always** cause |EX-I| to fail.

Using the Arduino IDE
^^^^^^^^^^^^^^^^^^^^^

#. Place your 'myAutomation.h' file in the ``CommandStation-EX`` subfolder of wherever you extracted the |EX-CS| files from GitHub.
#. Run the Arduino IDE
#. Open the ``CommandStation-EX`` folder
#. Select the Board, COM port etc. as before
#. click :guilabel:`Upload`

The Roster will be automatically loaded with the |EX-CS| software.

Add images for your locos (Engine Driver only)
==============================================

|EX-CS| does not natively support roster images, however several of the throttle (controller) apps allow you to do so.  Only one will be explored here... Engine Driver.

Engine Driver
-------------

There are three ways to load & store your Locomotive Icon Image in Engine Driver 2.32.142 and above.

1. **Automatically from your existing JMRI Roster & Media**
  
  If you have a JMRI Server that does support loco images:

  * Start JMRI and capture and load your images into JMRI Roster & Media panel as normal
  * Start the |WiThrottle server|.
  * Start the Web Server.
  * Connect |Engine Driver| to JMRI |WiThrottle server| Discovered Server 'My JMRI Railroad' or type in the IP address : Port# 
  * Click ``Select`` and load your Locos then ``Release`` and repeat until you've loaded all the locomotives you require with Icons into a throttle. 
 
  These Loco Icons will automatically be saved/cached on the Android device/phone in a new '/Android/data/jmri.enginedriver/files/recent_engine_list/**recent_engine_list**' folder for you.

  Requirements for this to work:

    * Have identical names (from JMRI Roster ID to |DCC-EX| |EX-R| Roster ID)  example ID;    "PE 1225"
    * Have image icons displayed for the locomotives

2. **Manually entered directly into your Android Engine Driver folder**
  
  * Capture then rename the image exactly like the Roster ID name in JMRI & EXRAIL and save as a .PNG file
  * Then place the engine Image into your Android device/phone in the |BR|\ '/Android/data/jmri.enginedriver/files/recent_engine_list' folder |BR|\ example image name;  PE 1225.png

  Note: certain characters are not allowed in file names so need to be substituted with "_" (underscore) if you have used them in your roster name. They are:

  * / (forward slash) 
  * " (double quote)
  * \\ (backslash)
  * \* (asterisk)
  * ? (question mark)
  * < (less than)
  * > (greater than)

3. **Select an image on the phone/device (which can be taken on the phone's camera)**

 * In the **Roster List** on the Select Loco screen

   * Long press on the loco
   * press the :guilabel:`New Image` button, which will launch the Android system's default app for choosing images 
   * find and select an image
   * click :guilabel:`Save` |BR|\ |BR|\ You can replace an image with the :guilabel:`New Image` button or remove it with the :guilabel:`Remove` button

**General Notes on the Local Loco Icons:**

* If the loco already has an image in the JMRI Roster (of the currently connected |WiThrottle server|), you won't be able to choose a local image.
* If you later add an image in the JMRI Roster for the loco (or later connect to a |WiThrottle server| that has an image), it will automatically overwrite the local image with the one on the server.
* In the Recent Locos list you *can not* add images to locos entered by a DCC address. (i.e. not from the roster)  

Also refer to the `Engine Driver Loco Icon Documentation <https://flash62au.github.io/EngineDriver_Home/configuration/loco_icons.html?highlight=images>`_ |EXTERNAL-LINK| for more information.
