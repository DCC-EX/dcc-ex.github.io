.. meta::
   :keywords: Comfort Levels Conductor Tinkerer Engineer

.. include:: /include/include.rst
.. include:: /include/include-l0.rst
|donate-button|

***********************
What is DCC and DCC-EX?
***********************

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

What is DCC?
============

For those who have come across our website and don't really know or understand what Digital Command Control (DCC) is or does, then in a very short summary, it is essentially a way to control multiple trains on the same piece of track independently of one another (it is also much, much more than that).

With DCC, there is no need for multiple electrically isolated blocks to control multiple trains independently any more.

To get a more in depth introduction to the DCC standand and protocol, you can read the `Wikipedia <https://en.wikipedia.org/wiki/Digital_Command_Control>`_ and `DCC Wiki <https://dccwiki.com/Introduction_to_DCC>`_ introduction pages.

However, if you just want to know how DCC, and in particular |DCC-EX|, can help you run your trains and also add more realism to your layouts, then continue reading here.

DCC is for more than just controlling trains
--------------------------------------------

DCC, and in particular our flagship product |EX-CS|, can also be used to control accessories (think turnouts/points, signals, sensors to monitor things, and lineside feature animation to name a few). DCC is not just about running trains!

Of course you don't need to use any of these features if you simply want to run trains.

Read on to understand which of our products and features will help you achieve your DCC dreams...

DCC-EX Products
===============

Our products currently include:

.. list-table::
    :widths: 33 33 33
    :header-rows: 0
    :class: table-grid-homepage

    * - |EX-CS-LOGO-SMALL|
      - |EX-I-LOGO-SMALL|
      - |EX-R-LOGO-SMALL|
    * - Our DCC command station for controlling your model railroad
      - Our user friendly command station software installer
      - The in-built scripting language for automating your model railroad
    * - |EX-WT-LOGO-SMALL|
      - |EX-TT-LOGO-SMALL|
      - |EX-IO-LOGO-SMALL|
    * - A simple web based throttle for your command station
      - A separate stepper based turntable controller
      - Use additional microcontrollers to expand I/O port capability
    * - |EX-DCCI-LOGO-SMALL|
      - 
      - 
    * - A separate DCC packet sniffing tool
      - 
      - 

.. list-table::
    :widths: 50 50
    :header-rows: 0
    :class: table-list-homepage

    * - |EX-CS-LOGO-SMALL| 
      - Our DCC command station for controlling your model railroad
    * - |EX-I-LOGO-SMALL| 
      - Our user friendly command station software installer
    * - |EX-R-LOGO-SMALL| 
      - The in-built scripting language for automating your model railroad
    * - |EX-WT-LOGO-SMALL| 
      - A simple web based throttle for your command station
    * - |EX-TT-LOGO-SMALL| 
      - A separate stepper based turntable controller
    * - |EX-IO-LOGO-SMALL| 
      - Use additional microcontrollers to expand I/O port capability
    * - |EX-DCCI-LOGO-SMALL| 
      -  A DCC packet sniffing tool

Choose Your Comfort Level
=========================

Our products are predominately Do-It-Yourself and range in difficulty from very simple to moderately complex. 

To help you navigate this web site, the pages are all tagged [#tags]_ with one or more of 'Comfort Levels' to help identify the difficulty of the what is described on that page.  (Don't worry, the paths are integrated and you can easily choose a slightly different path at any point.)

To work out your own personal comfort level, look at the descriptions of the levels below and see which one you most identify with. (A |Conductor-text|, a |Tinkerer-text|, or an |Engineer-text|.)


----

.. image:: /_static/images/level_icons/conductor-level.png
   :alt: Conductor Hat
   :scale: 50%
   :align: right

Conductor
---------

|force-break| 

.. list-table::
  :widths: 15 85
  :header-rows: 0
  :class: table-wrap-text

  * - .. image:: /_static/images/level_icons/conductor.png
        :alt: Conductor Hat
        :width: 144px
        :class: image-min-width-72
    - A |Conductor-text|, for the most part, just wants to enjoy operating trains. |BR| You could be someone new to trains or picking it up after a long absence, or you could be someone coming from running DC and looking to switch over to DCC. This is also the perfect place for someone who just wants something that works without much tinkering. In short, a |Conductor-text| wants to drive trains and doesn't want to have to deal with the details of the hardware or software involved. |BR| |BR| We'll show you how to put together a DCC Command Station with a Throttle (Controller), and have you up and running in just a few minutes. This path will keep things simple. |BR| |BR| We recommend that you :doc:`start here to build your EX-CommandStation </ex-commandstation/get-started/index>`.


----

.. image:: /_static/images/level_icons/tinkerer-level.png
   :alt: Propeller Beanie
   :scale: 50%
   :align: right

Tinkerer
--------

|force-break|

.. list-table::
    :widths: 15 85
    :header-rows: 0
    :class: table-wrap-text

    * - .. image:: /_static/images/level_icons/tinkerer.png
           :alt: Propeller Beanie
           :width: 144px
           :class: image-min-width-72
      - A |Tinkerer-text| likes the joy of building things themselves. |BR| They may not have an Engineering Degree, but they know how to connect a jumper wire and possibly use a soldering iron. They don't have a problem opening something like the Arduino IDE to change settings in a configuration file and upload it back to their Command Station. A Tinkerer wants to do more with model trains, like using different motor controllers or getting into more detailed control of turnouts/points, sensors, and other accessories. |BR| |BR| This path will provide more options over the Conductor path, and cover things like expanding your system and using the |JMRI| software (Java Model Railroad Interface) for more advanced control of your locomotives and your track. |BR| |BR| We also recommend that you :doc:`start here to build your EX-CommandStation </ex-commandstation/get-started/index>` if you have not already done so, but look out for the |Tinkerer-text| notes on the pages to see other options.

----

.. image:: /_static/images/level_icons/engineer-level.png
   :alt: Engineer Hat
   :scale: 50%
   :align: right

Engineer
--------

|force-break|

.. list-table::
    :widths: 15 85
    :header-rows: 0
    :class: table-wrap-text

    * - .. image:: /_static/images/level_icons/engineer.png
           :alt: Engineer Hat
           :width: 144px
           :class: image-min-width-72
      - An |Engineer-text| is a little more versed in computers and/or electronics. |BR| They have a desire to dig a little deeper into how things work. They can understand the basics of computer code and can look at the |DCC-EX| software and perhaps make simple changes. They may also want to help with offering their talents to the project! They are not averse to experimenting with things to make something work. These are the people whose layout looks like a telephone switching station when you look under their benchwork. |BR| |BR| This path will offer more technical information and cover more in depth topics like accessory control, sensors, and customizing the |EX-CS|. |BR| |BR| We also recommend that you :doc:`start here to build your EX-CommandStation </ex-commandstation/get-started/index>` if you have not already done so, but look out for the |Tinkerer-text| and |Engineer-text| notes on the pages to see other options.

----

Next Steps
==========

Keep these definitions in mind as you proceed through this website.

To learn more about how to build your own |EX-CS| station, click 'Next' or proceed to the :doc:`Getting Started Page </ex-commandstation/get-started/index>`.

----

.. [#tags] Special Note: We would like to thank Alex Leão of Locontrol who as a personal favour created our modeller levels icons.

