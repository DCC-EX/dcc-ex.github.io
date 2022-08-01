.. include:: /include/include.rst
*********************
EX-Rail (Automation)
*********************

Welcome to the home for DCC-EX Automation, **EX-RAIL** is the "**EX**\tended **R**\ailroad **A**\utomation **I**\nstruction **L**\anguage"

|EX-R| is an "**EX**\tended **R**\ailroad **A**\utomation **I**\nstruction **L**\anguage"
that can easily be used to describe sequential actions to automatically take place on your model layout. These actions are defined programmatically in a simple command script file, and uploaded to the Command Station once to configure it. EX-RAIL will then run automatically on CS startup.

To begin, let's define a few terms:

**SEQUENCE** - Simply a list of things to be done in order. These things might be to actually drive a train around, or merely to set some turnouts or flash some scene or panel lights. Actions can be made to wait for conditions to be met, like a sensor detecting a train, a button being pushed, or a period of time elapsing.

**ROUTE** - A SEQUENCE that is made visible to a throttle with a readable name so the user can press a button to get the sequence executed. This might be best used to set a series of turnouts and signals to create a route through the layout.

**AUTOMATION** - A SEQUENCE that is made visible to a throttle so that a user can hand over a loco and let EX-RAIL drive the train away, following each step listed in the sequence.

Most people wanting to do animations or run trains through an automated route will use a SEQUENCE, but those with :doc:`throttles </throttles/index>` that support it (:doc:`/throttles/software/engine-driver`, :doc:`WebThrottle-EX </throttles/software/ex-webthrottle>`) can add routes and automations. Both of these terms are just tags that let throttles with this feature automatically assign sequences to control buttons. "Routes" go into route buttons and can set turnouts, signals, etc., so you can drive your train along that route. "Automations" can appear on a "handoff" button that will supply or handoff the Loco ID to EX-RAIL where it can take over and run the train autonomously. An automation example would be manually driving a train into a station and pressing the assigned handoff button in the throttle that runs an AUTOMATION to take it on a journey around the layout.


.. attention::
   17 Feb 2022: *Now included* in **DCC++EX 4.0!**
   Available to download and use now!



.. toctree::
    :maxdepth: 1

    getting-started
    EX-RAIL-summary
    EX-RAIL-reference
    advanced