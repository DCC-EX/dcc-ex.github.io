.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-R-LOGO|

********
Overview
********

|tinkerer| |engineer|

.. sidebar:: 

   .. contents:: On this page
      :depth: 2
      :local:

Welcome to the home for |DCC-EX| Automation.

|EX-R| is an "**EX**\tended **R**\ailroad **A**\utomation **I**\nstruction **L**\anguage"
that can easily be used to describe sequential command 'sequences' to automatically take place on your model layout. These sequences are defined programmatically in a simple command script file, and uploaded to the Command Station once to configure it. **EX-Rail** will then run automatically on **EX-CommandStation** startup or if trigger manually or on occurance of the specified events.

To begin, let's define a few terms:

**SEQUENCE** - Simply a list of things to be done in order. These things might be to actually drive a train around, or merely to set some turnouts or flash some scene or panel lights. Actions can be made to wait for conditions to be met, like a sensor detecting a train, a button being pushed, or a period of time elapsing.

**ROUTE** - A special type of SEQUENCE that is made visible to a throttle with a readable name so the user can press a button to get the sequence executed. This might be best used to set a series of turnouts and signals to create a route through the layout.

**AUTOMATION** - A special type of SEQUENCE that is made visible to a throttle so that a user can hand over a loco and let |EX-R| drive the train away, following each step listed in the sequence.

Most people wanting to do animations or run trains through an automated route will use a SEQUENCE, but those with :doc:`throttles </throttles/index>` that support it (:doc:`/throttles/software/engine-driver`, :doc:`WebThrottle-EX </throttles/software/ex-webthrottle>`) can add routes and automations. Both of these terms are just tags that let throttles with this feature automatically assign sequences to control buttons. "Routes" go into route buttons and can set turnouts, signals, etc., so you can drive your train along that route. "Automations" can appear on a "handoff" button that will supply or handoff the Loco ID to |EX-R| where it can take over and run the train autonomously. An automation example would be manually driving a train into a station and pressing the assigned handoff button in the throttle that runs an AUTOMATION to take it on a journey around the layout.


Things You Can Do With EX-RAIL
==============================

- Create "Routes" which set multiple turnouts and signals at the press of a button in |EX-WT| or EngineDriver (other WiThrottle-compatible throttles are available)
- Automatically drive multiple trains simultaneously, and manage complex interactions such as single line working and crossovers by setting up "Automations"
- Drive trains manually, and hand a train over to an Automation
- Animate accessories such as lights, crossings, or cranes
- Intercept turnout changes to automatically adjust signals or other turnouts
- Turn on the coffee pot when the train reaches the station

.. rst-class:: clearer

What You Don't Need
===================

While extra functionality may be attained by using additional tools and applications, to get the benefit of |EX-R| you don't need anything more than a |EX-CS|, *and the Arduino IDE* used to configure it.

You DON'T need:

- |JMRI|, or any additional utilities
- EngineDriver, or any other WiThrottle app
- A separate computer living under your layout
- Knowledge of C++ or Python/Jython programming

