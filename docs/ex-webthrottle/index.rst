.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-wt.rst
|EX-WT-LOGO|

**************
EX-WebThrottle
**************

.. rst-class:: dcclink-right

   `Try It Now <https://DCC-EX.github.io/WebThrottle-EX>`_

|conductor| |tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:
 

|EX-WT| is a throttle (controller) that can connect to the |EX-CS| directly through the USB port of a computer.

For a video on how to install and use |EX-WT| click below.

   .. raw:: html
   
      <iframe width="336" height="189" src="https://www.youtube.com/embed/BkgsEOjxWaU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

What you need to run EX-WebThrottle
===================================

* Chromium-Based Browser version 89 or above (March 2021)
  (Chrome, Opera, Edge)

You don't need anything else to test it out and to run in emulator mode, just run it and play. To use it to run real trains you will need:

* An Arduino Mega or Uno Microcontroller
* An Arduino Motor Control Shield
* The |EX-CS| software loaded on your Arduino

Getting started
===============

.. note:: 
    :class: note-float-right
    
    If you don't have your hardware yet or just want to play with the throttle and see commands being sent to the log window, you can skip the part about connecting your |EX-CS|.

Make sure you are using **Chrome** version 89 or above (check the menu, help, about screen) or a compatible web browser. (See above)

To get started, connect your |EX-CS| to a computer that has a USB port and which has a compatible browser installed. Use a USB serial cable from your computer to the USB connector on the |EX-CS|. Power everything up and put a loco on the MAIN track.

Run or Install EX-WebThrottle
=============================

You have an option for how you would like to run |EX-WT|, from the cloud or installed locally on your machine. We recommend using it from the cloud or as a web app, but the choice is yours.

Try it now (Run from the cloud)
===============================

Just click the 'Try it now' button below and you will load a web page from our server that will run the web throttle on your machine. You can connect it to the |EX-CS| or just run it in emulator mode where you don't have to have any hardware. Please read the requirements above for what you need in order to run |EX-CS| in your browser. If you want to remember the link to run the throttle, it is https://dcc-ex.github.io/WebThrottle-EX.

.. rst-class:: dcclink

   `Try It Now <https://DCC-EX.github.io/WebThrottle-EX>`_

|EX-WT| is also a Progressive Web App (PWA). That means you can install it on your computer and run it right from your start menu! If you go into the |EX-WT| settings panel (click the 3 line, or 3 dot, "hamburger menu" at the top left), you will find a "Settings" menu. Click on "Apps" and then select "Install as an App". You can now work offline and always find |EX-WT| with your other Apps!

Download
========

.. note:: 
    :class: note-float-right
    
    We recommend using the version hosted on our servers as this will auto-update whenever we release a new update!

This will install all the files to run locally on your machine. You won't need an internet connection to run the software. Just download the latest zip file from the link below and extract it to any folder you have run permission on. Then click on the index.html file to launch the throttle in your browser. Create a shortcut to it on your desktop so you can launch it more easily.

.. rst-class:: dcclink

   `Download <https://github.com/DCC-EX/WebThrottle-EX/releases>`_

----

Operation
=========

.. figure:: /_static/images/ex-webthrottle/menu.png
   :alt: EX-WebThrottle - Menu
   :scale: 40%
   :align: right

   EX-WebThrottle - Menu

|EX-WT| has four pages which you can switch between using the hamburger menu button (three horizontal bars) on the top left of the screen.

- Throttle *(the default page)*
- CV Programmer
- Locomotives
- Function Maps
- Settings

|force-break|

----

Throttle
--------

.. figure:: /_static/images/ex-webthrottle/ex-webthrottle.png
   :alt: EX-WebThrottle
   :scale: 30%
   :align: right

   EX-WebThrottle screen

To use the program to connect to your |EX-CS| leave the ``Serial`` dropdown as is.

(See the section below if you wish to use the "emulator mode". )

.. figure:: /_static/images/ex-webthrottle/connect-button.png
   :alt: EX-WebThrottle - Connect button
   :scale: 80%

   EX-WebThrottle - Connect button

Next, click on the :guilabel:`Connect EX-CS` button. 

When using the serial connection, if the program finds any compatible devices, it will open a popup a window showing you a selection. It may show a line at the top such as "Arduino Mega 2560 (COM3)". Your com port may vary. Click on your board to select it and then click the :guilabel:`Connect EX-CS` button.

You should then be connected to the |EX-CS| and should see the response from the Command Station in the log textbox of the debug console at the bottom of the throttle window. Make sure your debug console is open. If it isn't, use the :guilabel:`Debug Console` slider button in the lower lower right to open it. 

When the command station is ready to use you should see ``[i] EX-CommandStation is READY`` appear in the log.

Now you are ready to run trains! Place your loco on the track and click the :guilabel:`Power` slider button to turn on power to your track (if not already on). You should see LEDs on your Arduino Motor Shield and an indication that your loco has power.

.. note:: Make sure you place the loco on the *MAIN* track, **not** the PROG track. Check your wiring. On an Arduino Motor Shield, Motor Output "A" should connect to your MAIN track and "B" to the PROGRAM track.

.. figure:: /_static/images/ex-webthrottle/loco-id.png
   :alt: EX-WebThrottle - Loco ID
   :scale: 80%
   :align: right

   EX-WebThrottle - Loco ID

Next go to the `Loco ID` textbox and enter the DCC Address of your loco and press the :guilabel:`Acquire` (right arrow in a circle) button. 

You should now have full control over your loco.

|force-break|

.. figure:: /_static/images/ex-webthrottle/speed-and-direction-controls.png
   :alt: EX-WebThrottle - Speed and Direction
   :scale: 40%
   :align: right

   EX-WebThrottle - Speed and Direction

In the throttle control area, to the left of the function buttons, are vertical controls to control direction. The up arrow selects forward, the square button is stop and the down arrow is reverse.

All the function buttons should be working, so you can play with the headlight, horn and bell and any other function assigned to a function button. The commands being sent to the Command Station and its responses will display in the log window if it is open

The circular control or vertical slider (chosen by the throttle select slider) can be moved by clicking and holding down the mouse button and dragging, clicking at a spot where you want the throttle to move, or clicking the :guilabel:`+` and :guilabel:`-` buttons.

----

Issuing Direct Commands
~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /_static/images/ex-webthrottle/direct-commands.png
   :alt: EX-WebThrottle - Direct commands
   :scale: 80%
   :align: right

   EX-WebThrottle - Direct commands

Once you are connected, you can also send commands directly to the |EX-CS|. 

e.g. You can send the ``<s>`` command in the "direct command" textbox to get status information from your Command Station. To do this just enter ``s`` (without the quotes) and press the :guilabel:`Send` button. |BR| You should see ``<iDCC-EX...>`` returned in the log window with your version, type of Arduino, type of motor shield, and some other information.

You can send any DCC-EX Native command in this way. 

----

Emulator
~~~~~~~~

To use the program in to emulate an |EX-CS|, without actually connecting to a real one, click on the ``Serial`` dropdown button and select ``Emulator`` to run in emulator mode, then follow to instructions above from ``Connect``.

.. note:: Not all Command Station functions are fully supported in the emulator yet. This means that although the software works, not all the responses will be shown in the debug console. This will be completed in a later release.

----

CV Programmer
-------------

The **CV Programmer** page allows you to read and write CVs (including the DCC address) from/to a decoder on the PROG Track.

.. figure:: /_static/images/ex-webthrottle/cv-programmer.png
   :alt: EX-WebThrottle - CV Programmer
   :scale: 40%
   :align: right

   EX-WebThrottle - CV Programmer

Note you must first connect to the |EX-cS| from the **Throttle** page before you can use these features.

**Decoder Address**

To read a decoder address, place your loco on the PROG track and press :guilabel:`Read Address`.  If Successful, the Address will be loaded in the ``DCC Address`` Field.  If unsuccessful, a message to that effect will appear in the log.

To write a decoder address, place you loco on the PROG track, enter the desired address into the ``DCC Address`` field and press :guilabel:`Write Address`.  If Successful or unsuccessful, a message to that effect will appear in the log.

**CV**

To read a CV, place your loco on the PROG track and press :guilabel:`Read CV`.  If Successful, the Value of the CV will be loaded in the ``CV Value`` field.  If unsuccessful, a message to that effect will appear in the log.

To write a decoder address, place you loco on the PROG track, enter the desired CV into the ``CV Numver`` field, the desired value into the ``CV Value`` field and press :guilabel:`Write CV`.  If Successful or unsuccessful, a message to that effect will appear in the log.

You can use the ``Common CVs`` drop list to select a CV. The approprate value will be put into the `CV Number`` field on selection.

.. note:: Programming on the Main (PoM) is not currently supported directly, though you can manually issue the appropriate commands from the throttle page.

----

Locomotives
-----------

The **Locomotives** page allows you store a roster of locomotives.

:dcc-ex-red-bold-italic:`Use of this is not recommended as it may not be available in the new version of EX-Toolbox currently being developed.`

.. note:: This is different to the roster that can be stored in the |EX-CS| itself.

----

Function Maps
-------------

The **Function Maps** page allows you store collections of Function Maps.

:dcc-ex-red-bold-italic:`Use of this is not recommended as it may not be available in the new version of EX-Toolbox currently being developed.`

.. note:: This is different to the functions stored with roster entries that can be stored in the |EX-CS| itself.

----

Settings
--------

The **Settings page** allows you to manage aspects of the |EX-CS| apps.

- General
- Storage
- App

General
~~~~~~~

- Theme
- Speed controller

.. figure:: /_static/images/ex-webthrottle/settings-speed-controller.png
   :alt: EX-WebThrottle - Settings - Speed Controller
   :scale: 50%

   EX-WebThrottle - Settings - Speed Controller

**Theme** Allows you change the appearance of the |EX-WT| screen to one of these options:

- Simple
- Metallic
- Dark

**Speed Controller** allows you to select one of these options:

- vertical
- Knob
- Circular

Storage
~~~~~~~

:dcc-ex-red-bold-italic:`Use of this is not recommended as it may not be available in the new version currently being developed.``

- Export App data
- Import App data
- Wipe App data

App
~~~

- Install as an App


----

Going Further / Developing
==========================

If you want to really delve into how this works and help us improve it with your comments or your development skills, please contact us. You can also read through our :doc:`/about/contributing/webthrottle` page for info on preparing to view and contribute to the code.

To load the Chrome DevTools to look at logging and be able to manually enter "write" commands for testing, click on the Menu (the 3 vertical dots in the upper right hand corner of the Chrome Window), then select "more tools" and then "Developer Tools". Or you can just hit ``Ctrl + Shift I``

----

Looking for some help with EX-WebThrottle?
==========================================

To raise a bug report, feature request, support request, or submit Beta test results, feel free to use our handy GitHub templates accessible by clicking this button:

|githublink-ex-webthrottle-button|
