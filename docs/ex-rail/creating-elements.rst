.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-R-LOGO|

*********************
Creating Key Elements
*********************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

First we need the elements that we will use for our automations.

This consists of:

* adding the hardware (not applicable to the roster)
* configuring |EX-CS| by modifying 'myAutomation.h' so that it know about the element
* re-uploading the software to the |EX-CS|

Adding a Roster
===============

In a text editor (e.g. notepad) create a new text file named 'myAutomation.h'. (Note the capital 'A' in the name.  The case of all the characters is important.)

If you are already using |EX-R| and have a myAutomation.h, then just the add ``ROSTER(...)`` lines near the top of the file.

Add a line that looks like:

.. code-block:: 
   
   ROSTER(999,"Loco Name","F0/F1/*F2/F3/F4/F5/F6/F7/F8")

Where:

* 999 - is the DCC address of your loco
* My Loco Name - is anything you want to see as the name of this loco in the throttle apps
* F0 F1 F3 ... F27. - are the names that you want to see for the functions specific to this loco
* \*F2 - note that if the function is 'momentary' rather than 'latching' (On/Off) then start the function label with a asterisk (\*).  The most common example of this is the Horn/Whistle which is commonly on F2.

Some more realistic examples might look like:

.. code-block:: 
   
   ROSTER (  3,"Eng 3", "F0/F1/*F2/*F3/F4/F5/F6/F7/Mute/F9//") // Address 3, Eng 3, Function keys F0-F10
   ROSTER(1224,"PE 1224","") // Motor Only Decoder, But use Engine Driver 'Preferences >In Phone Loco 'Sound'
   ROSTER(1225,"PE 1225","Lights/Bell/*Whistle/*Short Whistle/Steam/On-Time/FX6 Bell Whistle/Dim Light/Mute")
   ROSTER(4468,"LNER 4468","//Snd On/*Whistle/*Whistle2/Brake/F5 Drain/Coal Shvl/Guard-Squeal/Loaded/Coastng/Injector/Shunt-Door ~Opn-Cls/Couplng/BrakeVlv/Sfty Vlv/Shunting/BrkSql Off/No Momentm/Aux3/Fade Out/F22 Res/F23/Res//Aux 5/Aux6/Aux7/Aux 8")


Note: Add additional 'ROSTER(...)' lines for all your locos

Unavailable Functions
---------------------

If a function is not available leave the spot empty. (Don't even have the space character.)

For example: 

.. code-block:: 

   ROSTER(2825,"CN ES44AC","Headlight/Bell/*Horn/Coupler/Dynamic Brake///Flange Squeal/Startup & Shutdown")

Note the two missing text labels for positions F5 and F6. Engine Driver will skip those buttons and not display them at all in the interface since they do nothing for that loco.

Example of loco without sound:

.. code-block:: 

   ROSTER(2405,"AT&SF 2-8-0 2405","Headlight")

Note that it only has FO (the Headlight) and not following slashes.


Adding Turnouts/points
======================

.. todo::   URGENT - Need to have the details on how to add the hardware to support a Turnout Point, plus configuring EX-CS

Hardware -  Turnouts/points
---------------------------

For |conductor-text| we are assume you are use a single Mega2560 for Sensors and use a PCA9685 Servo/Signal board for Turnouts and LED Signals.

Mega2560 Processor board 

PCA9685 Servo Signal Board
Servo Turnouts and LED Signals and Special Lighting Effects
Connect servos on vpin 101, 102 and 115.  {Wired Brown Gnd, Orange 5v, Yellow Output}

To connect the Mega to the  PCA9685 Servo board use a four wire Female to Female cable simple connect four wire from the top of the Motor Shields four male pins labeled SCL, SDA, 5v, Gnd to the PCA male pins labeled SCL, SDA, 5v Gnd.

When you boot up the CS it will automatically find the board and assign address 40 to it.

myAutomation.h -  Turnouts/points
---------------------------------

TODO

Adding Sensors
==============

.. todo::   URGENT - Need to have the details on how to add the hardware to support a Sensor, plus configuring EX-CS

Hardware -  Sensors
-------------------

For |conductor-text| we are assume you are use a single Mega2560 for Sensors and use a PCA9685 Servo/Signal board for Turnouts and LED Signals.

Mega2560 Processor board 
Sensors and optional Momentary push buttons.
place IR Infrared or Optical sensors Output wire on Dpins 22, 23 & 24 sensors  one wire to Gnd and for the IR sensor a third wire to 5v pin.

Software -  Sensors
-------------------

TODO

Adding Signals
==============

.. todo::   URGENT - Need to have the details on how to add signals

Hardware -  Signals
-------------------

For |conductor-text| we are assume you are use a single Mega2560 for Sensors and use a PCA9685 Servo/Signal board for Turnouts and LED Signals.

Mega2560 Processor board 

PCA9685 Servo Signal Board
Servo Turnouts  and LED Signals and Special Lighting Effects
Connect 2 Red\Green LED point signals for the two turnouts on vpins 106 Red & 107 Green for turnout T1, and on vpins 108 Red & 109 Green for turnout T2

For LEDs Only use the -Gnd and Output+ vpins, NOT the center 5v pin

Software -  Signals
-------------------

TODO

Re-upload the EX-CommandStation software
----------------------------------------

Using EX-Installer
^^^^^^^^^^^^^^^^^^

#. Place your 'myAutomation.h' file in the ``CommandStation-EX`` subfolder of wherever you extracted the |EX-I| files.
#. Re-Run |EX-I|
#. Select the same options that you originally chose and upload

The Roster will be automatically loaded with the |EX-CS| software.

Using the Arduino IDE
^^^^^^^^^^^^^^^^^^^^^

#. Place your 'myAutomation.h' file in the ``CommandStation-EX`` subfolder of wherever you extracted the |EX-CS| files from GitHub.
#. Run the Arduino IDE
#. Open the ``CommandStation-EX`` folder
#. Select the Board, COM port etc. as before
#. click :guilabel:`Upload`

The Roster will be automatically loaded with the |EX-CS| software.
