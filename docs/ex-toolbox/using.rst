.. include:: /include/include.rst
.. include:: /include/include-l1.rst

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

|EX-TB| can be installed on you phone or table via the Google Play Store.

Open the Play Store app on your phone or table and search for "EX-Toolbox".

Once installed, open |EX-TB| and it will go through the initial setup wizard where it will ask for one permission, and for which which theme you would like to use.

After you complete the setup wizard, you will be shown the 'Connection' Screen

|force-break|

Connecting
==========

.. image:: /_static/images/ex-toolbox/connect.png
   :alt: Connecting
   :scale: 50%
   :align: right

Other than the very first time you start |EX-TB|, when the app opens you will be shown the 'Connection' screen.

On the 'Connection' screen there are three ways you can select a |EX-CS| to connect to:

  - IP Address and Port
  - Discovered Servers
  - Recent servers

Discovered Servers
------------------

  This is the most common way to connect. If the server you want to connect to is in the list, simply click on it and you will be taken to the 'CV-Programming' screen.

  If the server does not appear in the recent list try one of the other two methods.  Your server not appearing in the recent list is not necessarily a problem and there can be a number of reasons why.

Recent Server List
------------------

  If the server you want to connect to is in the list, simply click on it and you will be taken to the 'CV-Programming' screen.

  A server being in this list *does not* necessarily mean that you will be able to connect it *now*. It just means that you have successfully connected to it in the past.


IP Address and Port
-------------------

  Type in the **IP address** and **Port** of the |EX-CS| and press :guilabel:`Connect`.

  To find your server's IP address and Port:

    * For a JMRI server, see the WiThrottle screen for its address 
    * For other devices, see the instructions for that device

  If you only ever connect to one |EX-CS| you can effectively bypass this screen by setting the 'Auto-Connect to WiThrottle Server?' preference.


CV Programming
==============

.. image:: /_static/images/ex-toolbox/cv_programmer_menu.png
   :alt: Connecting
   :scale: 25%
   :align: right

DCC Decoder CV programming is available:

* on the Programming track (PROG) - Service Mode
* on the main line (MAIN) - Operation mode / Ops Mode

By default |EX-TB| shows the Service Mode options.  To switch to Operation Mode, select "Program on Main (Operation Mode)" on the drop down list at the top of the screen.

CV Programming (Service Mode)
-----------------------------

.. image:: /_static/images/ex-toolbox/cv_programmer.png
   :alt: Connecting
   :scale: 50%
   :align: right

Service Mode CV Programing is available form the 'CV Programming' screen, when 'Programming Track (ServiceMode)' is selected in the drop down list at the top of the screen.

Service Mode CV Programming allows you to both *Read* (if the decoder/loco supports it) and *Write* CVs.

You do not need to know the DCC Address of the decoder being changed, as all decoders/locos currently on the programming track will have the CV changed at the same time.

On this screen you can:

* read the decoder's DCC Address
* write a new DCC Address to the decoder
* read a CV value from the decoder
* write a CV value to the decoder
* select from a list of named, common CVs
* issue <> commands to the |EX-CS|

To read the DCC Address of the decoder click the ``Read`` button on the DCC Address row.

To write a DCC Address to the decoder, enter the address and click the ``Write`` button on the DCC Address row.

To read a CV of the decoder, enter the CV number and click the ``Read`` button on the CV row.

To write a CV value to the decoder, enter the CV number,  enter the value and click the ``Write`` button on the CV row.

If you select a 'common CV value' it will enter the CV number into the field. From there follow the instructions above for reading or writing the CV.

See below for issuing DCC-EX commands.

|force-break|

CV Programming (Operation Mode)
-------------------------------

.. image:: /_static/images/ex-toolbox/cv_programmer_ops_mode.png
   :alt: Connecting
   :scale: 50%
   :align: right

Operation Mode CV Programing is available form the 'CV Programming' screen, when 'Program on Main (Operation Mode)' is selected in the drop down list at the top of the screen.

Operation Mode CV Programming ONLY allows you to *Write* CVs.

To use Operation Mode CV Programming **you must know the DCC Address** of the decoder/loco you want to change.  Note: you should never try to change the DCC Address of the decoder/loco using Operation Mode CV Programming.

On this screen you can:

* write a new DCC Address to the decoder
* write a CV value to the decoder
* select from a list of named, common CVs
* issue <> commands to the |EX-CS|

To write a CV value to the decoder, enter the DCC Address of the decoder, enter the CV number,  enter the value and click the ``Write`` button on the CV row.

If you select a 'common CV value' it will enter the CV number into the field. From there follow the instructions above for writing the CV.

See below for issuing DCC-EX commands.

----

Turning Track Power On
----------------------

.. image:: /_static/images/ex-toolbox/power_menu.png
   :alt: Connecting
   :scale: 50%
   :align: right
   
|force-break|

.. image:: /_static/images/ex-toolbox/power.png
   :alt: Connecting
   :scale: 50%
   :align: right

|force-break|

Issuing <> Commands to the EX-CommandStation
--------------------------------------------


|force-break|

Track Manager
=============

(Only available when connected to EX-CommandStation version 4.2.7 and above.)

.. image:: /_static/images/ex-toolbox/track_manager.png
   :alt: Connecting
   :scale: 50%
   :align: right

|force-break|



Servo motor testing and adjustment
==================================

.. image:: /_static/images/ex-toolbox/servos.png
   :alt: Connecting
   :scale: 50%
   :align: right

|force-break|

Sensor testing
==============

.. image:: /_static/images/ex-toolbox/servos.png
   :alt: Connecting
   :scale: 50%
   :align: right

|force-break|

Current Meter
=============

(Only available when connected to EX-CommandStation version 4.2.20 and above.)

.. image:: /_static/images/ex-toolbox/currents.png
   :alt: Connecting
   :scale: 50%
   :align: right

|force-break|

