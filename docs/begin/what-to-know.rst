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

For those who have come across our website and don't really know or understand what Digital Command Control (DCC) is or does, then in a very short summary, it is essentially a way to control multiple trains on the same piece of track independently of one another (it is also much, much more than that).

With DCC, there is no need for multiple electrically isolated blocks to control multiple trains independently any more.

To get a more in depth introduction to the DCC standard and protocol, you can read the `Wikipedia <https://en.wikipedia.org/wiki/Digital_Command_Control>`_ and `DCC Wiki <https://dccwiki.com/Introduction_to_DCC>`_ introduction pages.

However, if you just want to know how DCC, and in particular |DCC-EX|, can help you run your trains and also add more realism to your layouts, then continue reading here.

DCC-EX does DC as well
----------------------

Along with DCC, |DCC-EX| can be used to control Direct Current (DC) locomotives using Pulse Width Modulation (PWM).

More information on using DC PWM can be found :doc:< on the TrackManager page `/trackmanager/index`>.

DCC is for more than just controlling trains
--------------------------------------------

DCC, and in particular our flagship product |EX-CS|, can also be used to control accessories (think turnouts/points, signals, sensors to monitor things, and lineside feature animation to name a few). DCC is not just about running trains!

Of course you don't need to use any of these features if you simply want to run trains.

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
    * - Our DCC command station for controlling your model railroad
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
      - Our DCC command station for controlling your model railroad
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

I'm interested in DCC but have a very small budget
==================================================

The |DCC-EX| project is free and open source software, using consumer grade, inexpensive microcontrollers and components to provide full feature DCC train control, and more.

You will get more features from our software than you will from many commercial DCC controllers, with the hardware components able to be purchased at a fraction of the price of these commercial systems.

At the moment, we don't offer our own ready-to-run solutions, but may do so in partnership with more resellers down the track, so for the moment a willingness to do some DIY is required. There is currently one option we know of in the UK who may be able to help you with this. See :doc:`/projects/railsnail-bluetooth` for details.

The only things we can't help you with are the layout and the DCC equiped locos!

You can start by reading through the :doc:`/ex-commandstation/accessories/index` section of our documentation to understand how to get a basic DCC CommandStation up and running, and also look through :doc:`/throttles/index` to see what throttle/controller options are available to control your trains and/or accessories.

I just want to run my trains
============================

If you simply want a system to run your DCC trains, then you only need to concern yourself with |EX-CS|, as this is our core digital controller product. While it can also do a lot more, you don't need to know about any other features or capabilities in order to use it to control trains only.

Note that you will need some sort of throttle or controller to connect to it also.

You will need to read through the :doc:`/ex-commandstation/index` documentation, and it will be helpful also to read through the :doc:`/throttles/index` section to become familiar with what throttle options are available (including our very own open source |EX-WT|).

This provides a very cost effective introduction to DCC train control using inexpensive consumer grade hardware and our (free) open source |EX-CS| software.

I want to operate my turnouts/points and run DCC trains
=======================================================

If you want your turnouts/points to also be controlled by |DCC-EX|, then this same |EX-CS| product has the capability to enable this also.

In addition to what you need to be familiar with for just running trains above, there is further information available on how to add and control turnouts/points in the :doc:`/ex-commandstation/accessories/turnouts/index` section.

I want to control all my accessories and run DCC trains
=======================================================

Further to just operating turnouts/points, |EX-CS| has the capability to control all your other various accessories including signals, turntables (including our own |EX-TT|), loco and rolling stock lighting, scenic accessories, and pretty much anything else that can be controlled digitally.

This is simply an extension of operating trains and controlling turnouts/points covered above, with further information available in our :doc:`/ex-commandstation/accessories/index` section.

I want some extra automated/animated realism
============================================

To start adding extra realism to your layout, such as controlling signal aspects when turnouts/points are closed or thrown, activating level crossing boom gates and lights as trains approach, or turning street lights off or on according to the time of day, this can be accomplished using the automation/animation capabilities of |EX-CS| which we call |EX-R|.

|EX-R| is an acronym for "**EX**\tended **R**\ailroad **A**\utomation **I**\nstruction **L**\anguage", and is an easy and powerful way to create simple to complex animation/automation sequences to control locos, sensors, signals, turnouts/points, and other layout or scenic accessories. |EX-R|'s English based commands and functions are designed for all levels of experience, from novice or non-programmers to experienced users, to have fun in making their layouts come to life.

Anyone can use |EX-R|, and over time we are building out practical examples to demonstrate how you can use this to automate or animate various aspects of your layout. We will also be publishing a series of "recipes" on this website as a sort of building block approach.

In addition to having your |EX-CS| up and running, with some sort of throttle or controller (see :doc:`/throttles/index`) to control your trains, you'll also need to add some accessories to use with your automation/animation sequences as outlined in :doc:`/ex-commandstation/accessories/index`.

To make the most of |EX-R| you should read through the :doc:`/ex-rail/index` section as well as see the practical examples in :doc:`/big-picture/index`.

I want a fully automated exhibition layout for my club
======================================================

Are your club members sick and tired of having to perform repetitive, manual operations during club open days or exhibitions?

To take your demonstration layouts to the next level, spend more time talking to your visitors and potential club members by using |EX-R| to automate your layout.

This can be anywhere from a simple loop to stop and start trains at stations with automated arrival and departure announcements all the way through to multiple trains running throughout the layout, closing/throwing turnouts/points as required, setting signals, and crossing paths without collisions.

To achieve this level of automation, you'll need to understand more than just how to get your |EX-CS| up and running, and will also need to have a good understanding of the accessories that can be added as outlined in :doc:`/ex-commandstation/accessories/index`.

As per our automated/animated realism information above, be sure to familiarise yourself with :doc:`/ex-rail/index` and :doc:`/big-picture/index`.