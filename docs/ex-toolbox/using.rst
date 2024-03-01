.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-tb.rst
|EX-TB-LOGO|

*********************************
EX-Toolbox - Installing and Using
*********************************

|tinkerer|

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:

Installing
==========

|EX-TB| can be installed on your Android phone or tablet via the `Google Play Store <https://play.google.com/store/apps/details?id=dcc_ex.ex_toolbox>`_ .

Open the *Play Store* app on your phone or tablet and search for "EX-Toolbox".

Once installed, open |EX-TB| and it will go through the initial setup wizard where it will ask for one permission, and for which which theme you would like to use.

After you complete the setup wizard, you will be shown the 'Connection' Screen.

|force-break|

----

Connecting
==========

.. figure:: /_static/images/ex-toolbox/connect.png
   :alt: Connecting
   :scale: 50%
   :align: right

   EX-Toolbox Connecting

Other than the very first time you start |EX-TB|, when the app opens you will be shown the 'Connection' screen.

On the 'Connection' screen there are three ways you can select a |EX-CS| to connect to:

  - IP Address and Port
  - Discovered Servers
  - Recent servers

Discovered Servers
------------------

  This is the most common way to connect. If the server you want to connect to is in the list, simply click on it and you will be taken to the 'CV-Programming' screen.

  If the server does not appear in the recent list try one of the other two methods.  Your server not appearing in the recent list is not necessarily a problem and there can be a number of reasons why.

  
.. warning::

   |EX-TB| can only connect *directly* to an |EX-CS|, however |JMRI|, the |EX-CS| and other devices and apps can, or do, advertise as "WiThrottle" mDNS services. EX-Toolbox cannot determine which are actually direct connections to an |EX-CS|.

   So... just because a server is in this list, doesn't mean that |EX-TB| will be able to connect to it.

Recent Server List
------------------

  If the server you want to connect to is in the list, simply click on it and you will be taken to the 'CV-Programming' screen.

  A server being in this list *does not* necessarily mean that you will be able to connect it *now*. It just means that you have successfully connected to it in the past.


IP Address and Port
-------------------

  Type in the **IP address** and **Port** of the |EX-CS| and press :guilabel:`Connect`.

  To find your EX-CommandStation's IP address and Port refer you original setup or, if you have a OLED screen on your command station the details will be displayed on it.

  If you only ever connect to one |EX-CS| you can effectively bypass this screen by setting the 'Auto-Connect to WiThrottle Server?' preference.

----

CV Programming
==============

.. figure:: /_static/images/ex-toolbox/cv_programmer_menu.png
   :alt: Connecting
   :scale: 25%
   :align: right

   EX-Toolbox Connecting

DCC Decoder CV programming is available:

* on the Programming track (PROG) - Service Mode
* on the main line (MAIN) - Operation mode / Ops Mode

By default |EX-TB| shows the Service Mode options.  To switch to Operation Mode, select "Program on Main (Operation Mode)" on the drop down list at the top of the screen.

CV Programming (Service Mode)
-----------------------------

.. figure:: /_static/images/ex-toolbox/cv_programmer.png
   :alt: Connecting
   :scale: 50%
   :align: right

   EX-Toolbox Connecting

Service Mode CV Programming is available form the 'CV Programming' screen, when 'Programming Track (ServiceMode)' is selected in the drop down list at the top of the screen.

Service Mode CV Programming allows you to both *Read* (if the decoder/loco supports it) and *Write* CVs.

You do not need to know the DCC Address of the decoder being changed, as all decoders/locos currently on the programming track will have the CV changed at the same time.

On this screen you can:

* read the decoder's DCC Address
* write a new DCC Address to the decoder
* read a CV value from the decoder
* write a CV value to the decoder
* select from a list of named, common CVs
* issue <> commands to the |EX-CS|

To read the DCC Address of the decoder click the :guilabel:`Read` button on the DCC Address row.

To write a DCC Address to the decoder, enter the address and click the :guilabel:`Write` button on the DCC Address row.

To read a CV of the decoder, enter the CV number and click the :guilabel:`Read` button on the CV row.

To write a CV value to the decoder, enter the CV number,  enter the value and click the :guilabel:`Write` button on the CV row.

If you select a 'common CV value' it will enter the CV number into the field. From there follow the instructions above for reading or writing the CV.

Note: Issuing a read or write will automatically turn the track power on.

See below for issuing DCC-EX commands.

|force-break|

CV Programming (Operation Mode)
-------------------------------

.. figure:: /_static/images/ex-toolbox/cv_programmer_ops_mode.png
   :alt: CV Programming (Ops Mode) Screen
   :scale: 50%
   :align: right

   EX-Toolbox CV Programming (Operation Mode) Screen

Operation Mode CV Programming is available form the 'CV Programming' screen, when 'Program on Main (Operation Mode)' is selected in the drop down list at the top of the screen.

Operation Mode CV Programming ONLY allows you to *Write* CVs.

To use Operation Mode CV Programming **you must know the DCC Address** of the decoder/loco you want to change.  Note: you should never try to change the DCC Address of the decoder/loco using Operation Mode CV Programming.

On this screen you can:

* write a new DCC Address to the decoder
* write a CV value to the decoder
* select from a list of named, common CVs
* issue <> commands to the |EX-CS|

To write a CV value to the decoder, enter the DCC Address of the decoder, enter the CV number,  enter the value and click the :guilabel:`Write` button on the CV row.

If you select a 'common CV value' it will enter the CV number into the field. From there follow the instructions above for writing the CV.

.. Note: 

   Issuing a read or write will automatically turn the track power on.

   The CV Programming Page has a feature specific to CV29.  When you read CV29; |BR| a) it explains what you need to change the value to to disable the 'Speed Table', and |BR| b) it explains what you need to change the value to to change default direction of the loco. 

See below for issuing DCC-EX commands.

----


Issuing <> Commands to the EX-CommandStation
--------------------------------------------

On several of the screens in |EX-TB| you can issue native DCC-EX ``<>`` commands to your |EX-CS|.

Enter the command you want to send, and click :guilabel:`Send`.

The command you send, and any responses from the command station will be shown below.

If you select a 'common command value' it will enter the command the field. From there follow the instructions above for issuing the command.

You can use the :guilabel:`Next` and :guilabel:`Prior` buttons to retrieve previously issues commands.

|force-break|

----

Speed matching
==============

Speed Matching assists with making two or more locos run at similar speeds.

.. figure:: /_static/images/ex-toolbox/speed_matching.png
   :alt: Speed Matching Screen
   :scale: 20%
   :align: right

   EX-Toolbox Speed Matching Screen

To access the Speed Matching either:

* Swipe Left from the CV-Programming Screen
* Swipe Right from the Loco Status Screen
* Select 'Speed Matching (PoM)' from the Menu

   .. raw:: html
   
      <iframe width="336" height="189" src="https://www.youtube.com/embed/7WyWR8xYvgY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


EX-Toolbox Speed Matching Instructions
--------------------------------------

Requirements
^^^^^^^^^^^^

1. A loop of track - ``MAIN``
2. A ``PROG`` track - or be prepared to switch the loop to ``PROG`` temporarily. (see Notes)
3. A loco that you wish to be the Master.  i.e. that you want to make to other locos match.
4. One or more 'Second' locos that you wish to match to the Master.
5. That you have run all the locos (the 'Master *and* any 'Second' loco) for 5-10 minutes to warm them up.  Many locos run differently when warm.

Assumptions
^^^^^^^^^^^

1. Assumes that you have already configured the 'Master' to be the way you want it and the other locos to behave.

  The 'Master' should be the naturally slowest loco of the set, not necessarily the one that will be run in the lead position.  |BR| i.e. Test your locos on their default settings first, and find the slowest.

  The low speed test uses a speed setting of `5` (0-126).  If your locos don't start moving at that setting it would be advisable to adjust Low speed setting and/or the Kick Start of the 'Master' first.
  
2. Assumes that, at least, the 'Second' loco is configured to use the High, Mid, Low CVs, not the full 28 step 'Speed Table'.  (Part of CV29) |BR| Not critical, but it is advisable to have the 'Master' also use the High, Mid, Low CVs.

   The CV Programming Page of |EX-TB| has a feature specific to CV29.  When you read CV29, it explains what you need to change the value to to disable the 'Speed Table'.

3. It is highly advisable that **BACK-EMF** is turned off on all locos that will be run in a consist.  If you don't you will likely encounter surging of the locos as they speed up and slow down under individual load.  
   
   **BACK-EMF** is referred to by some manufacturers as 'Dynamic Compensation for Speed Stabilisation', 'Scaleable Speed Stabilisation' or 'Load Compensation'.  Unfortunately there is no standard way to disable BACK-EMF. You will need to refer to the manuals for your decoders. 
   
   `This page <https://tonystrains.com/news/dcc-motor-control-with-back-emf-and-p-i-d/>`_ has a detailed explanation of BACK-EMF and details on how to change it for a number of manufacturers.

Instructions
^^^^^^^^^^^^

1. Open |EX-TB| and go to the Speed Matching screen.
2. Put the/a second (non-master) loco on the ``PROG`` track. (see Notes)
3. Click :guilabel:`Read -PROG trk`.

  This reads 8 CV values, including the loco address and CV29, and loads them in to the fields, with a 3 second delay between each read. |BR| Watch for any -1 responses (failed reads), and redo the read if any have failed.

4. Put the 'Master' on the ``MAIN`` track (the loop of track), along with the 'Second' loco.
5. Enter the `DCC address` of the Master.
6. Click the Low :guilabel:`Set Speed` button.
7. Watch and adjust the speeds of the Second loco in relation the Master, util they run at the same speed:

  If the 'Second' is too slow, either:

	a) Edit and increase the `Low` value and click :guilabel:`Write`.
	b) Click the :guilabel:`+` button.

  If the 'Second' is too fast, either:

	a) Edit and decrease the `Low` value and click :guilabel:`Write`.
	b) Click the :guilabel:`-` button.

8. Repeat for the 'Mid' Speed.
9. Repeat for the 'High' Speed.
10. Adjust the decoder momentum (Acceleration/Deceleration) and `Kick Start` as needed.  Test by starting and stopping the locos from the three different speeds.
11. If you have more locos to match, repeat from step 2.
    
Notes: 
^^^^^^

   1. By default, the :guilabel:`+` and :guilabel:`-` buttons change the CV values by 1. You can change this step amount by editing the 'Step' field. |BR| e.g. When I start on a loco, I normally have the Step at 10.  When it gets closer to a match I change the step to 1.
   
   2. You don't need a separate ``PROG`` track.  You can use the 'Track Manager' screen to temporarily set the loop of track to ``PROG`` for steps 2-3, then change it back to ``MAIN`` for steps 4 on.
   
   3. Some decoders don't support Kick Start.
   
   4. Some decoders don't allow you to turn BACK-EMF off. Check your decoder manual.
   
   5. The low speed test uses a speed setting of ``5`` (0-126).  If your locos don't start moving at that setting it would be advisable to adjust Low speed setting and/or the Kick Start of the 'Master' first.

|force-break|

----

Loco Status
===========

Loco Status allows you to watch changes to all locos being controlled by the command station.

.. figure:: /_static/images/ex-toolbox/loco_status.png
   :alt: Loco Status Screen
   :scale: 20%
   :align: right

   EX-Toolbox Loco Status Screen

To access the Track Manager either:

* Swipe Right from the Speed Matching Screen
* Swipe Left from the Current Status Screen
* Select 'Loco Status' from the Menu

|force-break|

----

Track Manager
=============

(Only available when connected to EX-CommandStation version 5.0.0 and above.)

.. figure:: /_static/images/ex-toolbox/track_manager.png
   :alt: Track Manager
   :scale: 20%
   :align: right

   EX-Toolbox Track Manager Screen

To access the Track Manager either:

* Swipe Right from the CV-Programming Screen
* Swipe Left from the Current Status Screen
* Select 'Track Manager' from the Menu


Track Manager allow you to change up to 8 channels (depending on the Motor Shield you are using)

Each channel can be one of:

* ``DCC PROG`` - Programming Track
* ``DCC MAIN`` - Main Track
* ``DC``
* ``DC reversed polarity (DCX)``
* ``OFF``

Select the value you want for the channels and click :guilabel:`Set`

Note. If you select ``DC`` or ``DCX`` you must select a DCC address for the channel before pressing ``Set``.  What ever address you select, selecting that address on your throttle (e.g. Engine Driver) will result in  the DC locomotive on the track connected to that channel to respond.

Note. Only one channel can be ``PROG``. If you select more that one, one will turned ``OFF``.

|force-break|

----

Servo motor testing and adjustment
==================================

.. figure:: /_static/images/ex-toolbox/servos.png
   :alt: Servos Screen
   :scale: 50%
   :align: right

   EX-Toolbox Servos Screen

The servo motor test screen will allow you to test and fine tune the settings needed for configuring servo motors attached to the |EX-CS|.  This is intended to be temporary.  To permanently configure a servo motor you will need to record the values and include the in the configuration of your |EX-CS|.

To access the Servo configuration screen either:

* Swipe Right from the Sensor Screen
* Swipe Left from the CV Programming Screen
* Select 'Servos' from the Menu

On the Servo motor screen, 

* Enter the VPin of the servo motor you want adjustment
* Enter any known starting values for Close, Mid, Throw
* Test the Close, Mid, Throw positions by pressing the appropriate button. The servo will move to that position.
* Fine adjust any of the three positions by using the :guilabel:`+` or :guilabel:`-` buttons |BR| The servo will gradually move.
* when you are happy, record the three values

|EX-TB| remembers the servos that you have changed (up to 10) in this and previous sessions, and you can select one of the previous servos from the drop down list.  |EX-TB| will restore the last settings you used for the selected servo to the main fields.

|force-break|

----

Sensor testing
==============

.. figure:: /_static/images/ex-toolbox/servos.png
   :alt: Sensors Screen
   :scale: 50%
   :align: right

   EX-Toolbox Sensors Screen

The Sensor test screen will allow you to test any sensors configured in your |EX-CS|.

To access the Sensor Testing configuration screen either:

* Swipe Right from the Current Status Screen
* Swipe Left from the CV Servos Screen
* Select 'Sensors' from the Menu

When the screen opens the first 100 sensors found will be shown. Activity on the sensors will be shown on the screen.  Scroll down to if needed.

The :guilabel:`Watch` button is generally not needed, but will force |EX-TB| to check the available sensors on the |EX-CS| again.

|force-break|

----

Current Meter
=============

(Only available when connected to EX-CommandStation version 5.0.0 and above.)

.. figure:: /_static/images/ex-toolbox/currents.png
   :alt: Current Meter Screen
   :scale: 50%
   :align: right

   EX-Toolbox Current Meter Screen

The Current Status screen will show you the current values for up to eight channels on the motor shield on your |EX-CS|.

To access the Current Meter screen either:

* Swipe Right from the Track Manager Screen
* Swipe Left from the Sensors Screen
* Select 'Current Status' from the Menu

For each channel the following is shown:

* the up-to-date value in Milliamps
* the highest value seen recently in Milliamps
* the maximum value able to be supplied by the moto shield in Milliamps

The readings start as soon as you open the screen and are paused as soon as you exit the screen.  The readings are taken every three seconds.

You can manually stop the readings with the :guilabel:`Stop` button.

You can manually restart the readings with the :guilabel:`Start` button.  This will also clear the 'Highest' values.

|force-break|

----

Secondary Screens
=================

Power
-----

.. figure:: /_static/images/ex-toolbox/power.png
   :alt: Power Screen
   :scale: 10%
   :align: right

   EX-Toolbox Power Screen

.. figure:: /_static/images/ex-toolbox/power_menu.png
   :alt: Power menu
   :scale: 50%
   :align: right

   EX-Toolbox Power menu

**Turning Track Power On**

There are two ways to turn the Track Power on/off:

* Power Screen - accessed from the menu
* Power Action Bar button - needs to be enable in the preferences
 
The *Power Screen* can be accessed from the :menuselection:`Menu --> Power`.  This will open the Power Screen where there is a simple button that to turn the power on or off. Use the :guilabel:`Close` button or Android's :guilabel:`Back` button to return to the CV-Programming Screen.

If the *Power Action Bar button* is enabled, simply click on it to turn track power on or off.

.. note:: 

  You can also optionally enable the Power Button on the Action bar in the preferences.

|force-break|

Preferences
-----------

Most configuration options are found in the *Preferences* which is accessed via the overflow menu which is normally three dots (⁞) or three bars (≡).


View log
--------


Accessed from any of the main screens via :menuselection:`Menu --> View Log`.

This screen allows you to view the internal Engine Driver log of events.
This is sometimes useful for analysing problems.

The option to `Start recording to file` creates a user-accessible file that can be sent to the |EX-TB| app developers to assist you in resolving a problem.
The file will be located on your mobile phone at:
Internal storage ``/Android/data/dcc_ex.toolbox/files`` |br|\ and will be named something like: ``logcat9999999999999.txt``

Enable the preference to include the timestamp on each line of the log.


About
-----

This screen displays 

* Information about |EX-TB| 
* Information about the |EX-CS| it is currently connected to (if any)
* A page of basic information about |EX-CS|

|force-break|

----

Connecting via USB
==================

|EX-TB| can't normally connect to an |EX-CS| via USB, however it is possible to temporarily create a USB to IP connection on your PC using tools like *socat* or *SerialToIPGUI* (for windows).

Using *socat* in Linux:

   ``socat TCP4-LISTEN:2560 /dev/ttyUSB0,b115200,raw,echo=0``

   or (to provide more information)

   ``socat -d -d -d TCP4-LISTEN:2560 /dev/ttyUSB0,b115200,raw,echo=0``

   Note: Change 'dev/ttyUSB0' to the appropriate USB port that the command station is connected to.

Using *socat* in Microsoft Windows:

   ``socat TCP-LISTEN:2560 /dev/ttyS11,b115200,raw,echo=0``

   or (to provide more information)

   ``socat -d -d -d TCP-LISTEN:2560 /dev/ttyS11,b115200,raw,echo=0``


   Note: Change S11 to the appropriate USB port.  Whatever 'COM' number appears in the Device Manager, subtract 1.  |BR|
   i.e. 'COM12' in the Windows Device Manager becomes '/dev/ttyS11'


Using *SerialToIPGUI* (For Microsoft Windows) (Recommended):

   .. figure:: /_static/images/SerialToIPGUI/SerialToIPGUI.png
      :alt: SerialToIPGUI
      :scale: 50%
      :class: responsive-image

      SerialToIPGUI

   * start SerialToIPGUI
   * Select the correct COM port for the command station
   * Enter the port of '2560' 
   * Click :guilabel:`Start`

   Once started...
   
   * Open |EX-TB| on your Android device
   * Enter the IP address of your PC (The one running socat or SerialToIPGUI)
   * Enter the port of '2560' 
   * Click :guilabel:`connect`

.. warning::

   This 'trick' only supports a single connection at a time.  So it is important that JMRI (if you are using it), or the Arduino IDE serial monitor, or anything else that might be using the COM (USB) port are shut down first.

Downloads
---------

 * *SerialToIPGUI*  - https://sourceforge.net/projects/serialtoip/
 * *socat* for windows requires downloading the 'cgywin' and installing the optional 'socat' package when you install - https://www.cygwin.com/ 


----

Troubleshooting (Windows socat)
-------------------------------

In Microsoft Windows and using the command line socat, if you see a "command not found" error, Here is what you need to do to fix it:

* Right click on "My Computer" -> Properties -> Advanced -> Environment Variables
* Add a new environment variable, called ``CYGWIN_HOME`` and set its value to ``C:\cygwin``
* Edit the PATH environment variable and add ``C:\cygwin\bin`` to it (usually separated by a ';').
* Just click okay, exit any command prompts or bash shells (over cygwin) you may have open, and open it again - it'll work!

Note that if you installed cgywin to a folder *other than "C:\\cgywin"* (e.g. c:\\cgywin64), use that folder name instead in the change above.