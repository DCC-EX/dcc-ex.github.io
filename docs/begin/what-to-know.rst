.. meta::
   :keywords: Comfort Levels Conductor Tinkerer Engineer

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-description.rst
|donate-button|

***********************
What do I need to know?
***********************

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

What is DCC and DCC-EX?
=======================

Firstly, The |EX-CS| can still run your older DC locos! But you can really open up a lot of possibilities using DCC.

For those who have come across our website and don't really know or understand what Digital Command Control (DCC) is or does, then in a very short summary, it is in part a way to control multiple trains on the same piece of track independently of one another (it is also much, much more than that).

With DCC, there is no longer a need for multiple electrically isolated blocks to control multiple trains independently.

To get a more in depth introduction to the DCC standard and protocol, you can read the `Wikipedia <https://en.wikipedia.org/wiki/Digital_Command_Control>`_ and `DCC Wiki <https://dccwiki.com/Introduction_to_DCC>`_ introduction pages.

However, if you just want to know how DCC, and in particular |DCC-EX|, can help you run your trains and also add more realism to your layouts, then continue reading here.

DCC-EX does DC as well
----------------------

As mentioned, along with DCC, |DCC-EX| can be used to control Direct Current (DC) locomotives using Pulse Width Modulation (PWM). This is actually an improvement over pure DC since the full voltage is always applied to the track. Rather than controlling a voltage from zero to full to control speed, the average time the full voltage is applied controls the speed. This allows for better stops and starts and smoother operation at low speeds.

More information on using DC PWM can be found :doc:`on the TrackManager page </trackmanager/index>`.

DCC is for more than just controlling trains
--------------------------------------------

DCC, and in particular our flagship product |EX-CS|, can also be used to control accessories (think turnouts/points, signals, sensors to monitor things, and lineside feature animation to name a few). DCC is not just about running trains!

Of course you don't need to use any of these features if you simply want to run trains without any of the bells and whistles (though we control the bells and whistles too!).

Read on to understand which of our products and features will help you achieve your DCC dreams...

DCC-EX free and Open Source products
------------------------------------

Our list of free, open source software products currently include:

.. list-table::
    :widths: 33 33 33
    :header-rows: 0
    :class: table-grid-homepage

    * - |EX-CS-LOGO-SMALL|
      - |EX-I-LOGO-SMALL|
      - |EX-R-LOGO-SMALL|
    * - Our DCC & DC command station software for controlling your model railroad
      - Our user friendly command station software installer
      - The built-in scripting language for automating your model railroad
    * - |EX-WT-LOGO-SMALL|
      - |EX-TT-LOGO-SMALL|
      - |EX-IO-LOGO-SMALL|
    * - A simple web browser based throttle for your command station
      - A separate stepper based turntable controller
      - Use additional microcontrollers to expand I/O port capability
    * - |EX-DCCI-LOGO-SMALL|
      - |EX-FC-LOGO-SMALL|
      - |EX-TB-LOGO-SMALL| 
    * - A separate DCC packet sniffing tool
      - A FastClock to enable time based events
      - An Android app to help configure your EX-CommandStation

.. list-table::
    :widths: 50 50
    :header-rows: 0
    :class: table-list-homepage

    * - |EX-CS-LOGO-SMALL| 
      - Our DCC & DC command station software for controlling your model railroad
    * - |EX-I-LOGO-SMALL| 
      - Our user friendly command station software installer
    * - |EX-R-LOGO-SMALL| 
      - The built-in scripting language for automating your model railroad
    * - |EX-WT-LOGO-SMALL| 
      - A simple web browser based throttle for your command station
    * - |EX-TT-LOGO-SMALL| 
      - A separate stepper based turntable controller
    * - |EX-IO-LOGO-SMALL| 
      - Use additional microcontrollers to expand I/O port capability
    * - |EX-DCCI-LOGO-SMALL| 
      -  A DCC packet sniffing tool
    * - |EX-FC-LOGO-SMALL| 
      -  A FastClock to enable time based events
    * - |EX-TB-LOGO-SMALL| 
      -  An Android app to help configure your EX-CommandStation
  
Our list of open source hardware products currently include:

.. list-table::
    :widths: 33 33 33
    :header-rows: 0
    :class: table-grid-homepage

    * - |EX-CSB1-LOGO-SMALL|
      - |EX-MS-LOGO-SMALL|
      - |EX-WS-LOGO-SMALL|
    * - Our ready-to-run DCC & DC command station / booster for controlling your model railroad
      - Our dual 5A output motor shield for DIY command stations and adding power districts to the EX-CSB1
      - Our WiFi add-on board for DIY command stations

.. list-table::
    :widths: 50 50
    :header-rows: 0
    :class: table-list-homepage

    * - |EX-CSB1-LOGO-SMALL| 
      - Our ready-to-run DCC & DC command station / booster for controlling your model railroad
    * - |EX-MS-LOGO-SMALL| 
      - Our dual 5A output motor shield for DIY command stations and adding power districts to the EX-CSB1
    * - |EX-WS-LOGO-SMALL| 
      - Our WiFi add-on board for DIY command stations


I'm interested in DCC but have a very small budget
==================================================

How does spending only $60 to $120 US (€54 - 110) sound to get the equivalent of over $400 (€365)worth of command station capabilities?

We offer our own ready-to-run solutions in addition to a DIY path where you snap together a command station yourself. The DCC-EX Team created the |EX-CSB1| (EX-CSB1) which is a full USB or WiFi connected Command Station on one board. Just like the commercial products, you can connect a power supply, connect it to your tracks, and you are ready to run trains in seconds. And the EX-CSB1 is half or less the price of competing systems.

The |DCC-EX| DIY project is our free and open source software you install onto widely available, inexpensive microcontrollers and components to provide full featured DCC and DC train and accessory control. If at the lowest end you are willing to do some learning and assembling, you can get into modelling or upgrade your current setup very inexpensively.

You will get more features from our software than you will from many commercial DCC controllers, with the hardware components able to be purchased at a fraction of the price of these commercial systems.

We also have our own |EX-MS| to provide more power to DIY setups using Arduino or ESPDuino32 boards, and an |EX-WS| to add WiFi capability to them as well if you choose that route. (The EX-CSB1 already includes the features of both of these)

As we grow, we are creating an entire ecosystem of products that plug together and allow you to control every aspect of your layout including lighting, sensors, points, motors, servos, displays, and more.

The only things we can't help you with is coming to your location and assembling your benchwork and laying your track!

You can start by reading through the :doc:`/ex-commandstation/accessories/index` section of our documentation to understand how to get a basic DCC & DC CommandStation up and running, and also look through :doc:`/throttles/index` to see what throttle/controller options are available to control your trains and/or accessories.

I just want to run my trains
============================

If you simply want a system to run your DCC or DC trains, then you only need to concern yourself with |EX-CS| running on our |EX-CSB1| or on a DIY system like an Arduino Mega. |EX-CS| is our core digital controller product. While it can also do a lot more, you don't need to know about any other features or capabilities in order to use it to just run trains.

Note that you will need a throttle or controller to connect to the CS (via serial, WiFi, or Ethernet), but you already have a throttle - your phone. There are several excellent apps, like |Engine Driver| that are free and can have you up and running in minutes. And there are plenty of DIY physical throttles as well as commercial ones like the TCS throttles.

You will need to read through the :doc:`/ex-commandstation/index` documentation, and it will be helpful also to read through the :doc:`/throttles/index` section to become familiar with what throttle options are available (including our very own free and open source |EX-WT| that connects your computer to the CS with a USB cable).

This provides a very cost effective introduction to DCC train control using inexpensive hardware and our (free) open source |EX-CS| software.

I want to operate my turnouts/points and run trains
===================================================

If you want your turnouts/points to also be controlled by |DCC-EX|, then this same |EX-CS| product has already has this capability built-in.

In addition to what you need to be familiar with for just running trains listed above, there is further information available on how to add and control turnouts/points in the :doc:`/ex-commandstation/accessories/turnouts/index` section.

I want to control all my accessories and run trains
===================================================

Further to just operating turnouts/points, |EX-CS| has the capability to control all your other various accessories including signals, turntables (including our own |EX-TT|), loco and rolling stock lighting, scenic accessories, sensors, and pretty much anything else that can be run on electricity.

This is simply an extension of operating trains and controlling turnouts/points covered above, with further information available in our :doc:`/ex-commandstation/accessories/index` section.

I want some extra automated/animated realism
============================================

To start adding extra realism to your layout, such as controlling signal aspects when turnouts/points are closed or thrown, activating level crossing boom gates and lights as trains approach, or turning street lights off or on according to the time of day, you can use the automation/animation capabilities of |EX-CS| which we call |EX-R|.

|EX-R| is an acronym for "**EX**\tended **R**\ailroad **A**\utomation **I**\nstruction **L**\anguage", and is an easy and powerful way to create simple to complex animation/automation sequences to control locos, sensors, signals, turnouts/points, and other layout or scenic accessories. |EX-R|'s English based commands and functions are designed for all levels of experience, from novice or non-programmers to experienced users, to have fun in making their layouts come to life.

Anyone can use |EX-R|, and over time we are building out practical examples to demonstrate how you can use this to automate or animate various aspects of your layout. We will also be publishing a series of "recipes" on this website as a sort of building block approach.

In addition to having your |EX-CS| up and running, with some sort of throttle or controller (see :doc:`/throttles/index`) to control your trains, you'll also need to add some accessories to use with your automation/animation sequences as outlined in :doc:`/ex-commandstation/accessories/index`.

To make the most of |EX-R| you should read through the :doc:`/ex-rail/index` section as well as see the practical examples in :doc:`/big-picture/index`.

I want a fully automated exhibition layout for my club
======================================================

Are your club members tired of having to perform repetitive, manual operations during club open days or exhibitions?

To take your demonstration layouts to the next level, spend more time talking to your visitors and potential club members by using |EX-R| to automate your layout.

This can include anything from a simple loop to stop and start trains at stations with automated arrival and departure announcements all the way through to multiple trains running throughout the layout, closing/throwing turnouts/points as required, setting signals, and crossing paths without collisions.

To achieve this level of automation, you'll need to understand more than just how to get your |EX-CS| up and running, and will also need to have a good understanding of the accessories that can be added as outlined in :doc:`/ex-commandstation/accessories/index`.

As per our automated/animated realism information above, be sure to familiarise yourself with :doc:`/ex-rail/index` and :doc:`/big-picture/index`.

How does EX-CommandStation compare to commercial Command Stations
=================================================================

Comparing the |EX-CS| to commercial Command Stations can require a bit of reading, but hopefully we can condense that knowledge into on web page.

See :doc:`/begin/comparison` for a discussion of the differences between |EX-CS| vs the commercial products.