.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

********
Overview
********

|tinkerer| |engineer| |support-button| 

.. sidebar:: 

   .. contents:: On this page
      :depth: 2
      :local:

Welcome to the home for |DCC-EX| Automation.

|EX-R| is an "**EX**\tended **R**\ailroad **A**\utomation **I**\nstruction **L**\anguage"
that can easily be used to describe sequential command 'sequences' to automatically take place on your model layout. 

These sequences are defined programmatically in a simple command script file, and uploaded to the Command Station once to configure it. **EX-Rail** will then run automatically on **EX-CommandStation** startup, trigger manually, or on occurrence of the specified events.

To begin, let's define a few terms:

**OBJECT** - Things / devices on your layout that you want to interact with. these include: :ref:`Your locos <ex-rail/creating-elements:adding a roster>`, :ref:`Turnouts/Points <ex-rail/creating-elements:adding the hardware - servo turnouts/points>`, :ref:`semaphores/Signals <ex-rail/creating-elements:adding the hardware - signals>`, :ref:`Servo based Animations <ex-rail/creating-elements:configure myautomation.h - servos for signals an animations>`, :ref:`Sensors <ex-rail/creating-elements:adding the hardware - sensors>` and :ref:`Signals (Lights) <ex-rail/creating-elements:configure myautomation.h - signals>`.

**COMMANDS** - These can be various things like; drive a loco around, change a turnout/point or signal or LED. Or it could to be to wait for conditions to be met, like a sensor detecting a train, a button being pushed, or a period of time elapsing.  The events in turn may trigger additional commands.

**SEQUENCE** - Simply a list of commnads to be done in order. There a also specific commands allow you to alter the order of the commands. Along with the generic SEQUENCE, there are some special types of sequence; **ROUTE**, **AUTOMATION** and **ONevent** that are discussed in the following pages.

Things You Can Do With EX-RAIL
==============================

- Create 'Routes' which set multiple turnouts/points and signals at the press of a button in |EX-WT| or |Engine Driver|, |WiThrottle|, or other WiThrottle-compatible throttles are available
- Automatically drive multiple trains simultaneously, and manage complex interactions such as single line working and crossovers by setting up Automations 'Sequences'
- Drive trains manually, and hand a train over to an Automation
- Animate accessories such as lights, crossings, or cranes
- Intercept turnout/point changes to automatically adjust signals or other turnouts
- Turn on the coffee pot when the train reaches the station

.. rst-class:: clearer

What You Don't Need
===================

While extra functionality may be attained by using additional tools and applications, to get the benefit of |EX-R| you don't need anything more than a |EX-CS|, *and the Arduino IDE* used to configure it.

You DON'T need:

- |JMRI|, or any additional utilities
- |Engine Driver|, |WiThrottle|, or any other WiThrottle app
- A separate computer living under your layout
- Knowledge of C++ or Python/Jython programming

----

Next Steps - myAutomation.h
===========================
   
Click :doc:`here <editing>` or click the :guilabel:`Next` button to learn how to edit the file which will contain your automation sequences.