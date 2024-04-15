.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-bp.rst
|EX-BP-LOGO|

********************
Stage 4 - Automation
********************

|tinkerer| |engineer| |support-button|

What to expect to learn from stage 4
====================================

At the end of this stage, we expect you will have learnt the following:

* How add automations to your |EX-CS|

Recommended reading
===================

Throughout these pages we will be using |EX-R| functionality extensively, not just for automation, but also to define the various objects in use, and therefore we highly recommend being familiar with at least the basics of EX-RAIL, so it would be best to read through the :doc:`/ex-rail/getting-started` page prior to going any further.

We will also be outlining the equivalent DCC-EX commands for items where relevant, so it can be handy to refer to the :doc:`/reference/software/command-summary-consolidated` where necessary.

Overview of EX-RAIL automations
===============================

The |EX-R| sequences are described in detail in the :doc:`/ex-rail/index` pages, which we recommend that you read. We won't repeat all that information here, but as introduction... 

|EX-R| is an "**EX**\tended **R**\ailroad **A**\utomation **I**\nstruction **L**\anguage"
that can be used to describe sequential command 'sequences' to automatically take place on your model layout. These sequences are defined in a simple command script file, and uploaded to the Command Station once to configure it. 

**EX-Rail** will then run the sequences *automatically* on EX-CommandStation startup, be triggered *manually* or run on occurrence of a *specified events*.

Once started, each 'sequence' will step through a list of simple keyword commands, in order, until they reach a ``DONE`` keyword.  Multiple concurrent sequences are supported.  

By using *Conditional*, *Branching*, *Delay* and *Wait* commands it is possible to design complex sequences with multiple outcomes which can drive your trains, operate your turnouts/points and signals, and react to events on your layout.

See the :doc:`/ex-rail/examples` page and the following pages in this section for examples of what is possible.

Structure of a 'Sequence'
-------------------------

In general, sequences follow the basic structure:

.. code-block:: cpp
   :class: code-block-float-right

   // Example
   ROUTE(1,"Coal Yard exit")
      RED(77)      // signal 77 to Red
      THROW(1)     // throw turnout/point 1
      CLOSE(7)     // close turnout/point 7
      DELAY(5000)  // 5 second wait
      GREEN(92)    // signal 92 to Green
      DONE

.. code-block:: cpp

   <sequence-type>( parameter-1, parameter-2, ...)
     <command 1>
     <command 2>
     ...
     <command n>
     DONE     or     RETURN     or     FOLLOW ( id )


Notes
=====

Locomotive addresses in use
---------------------------

For our various automations and sequences that involve driving trains, we will be using locomotives that represent the various international locations and preferred modelling eras of the |DCC-EX| team. Be warned that this means we will be mixing completely unrealistic combinations of eras on the same layout!

Here are the various locomotives you can find used throughout these examples:

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - DCC Address
    - Name/Number
    - Type
    - Era
    - Location
  * - 1
    - DH72
    - Diesel Hydraulic
    - Early Modern
    - Queensland, Australia
  * - 2
    - RM2031
    - Railcar
    - Early Modern
    - Queensland, Australia
  * - 3
    - 2350
    - Diesel Electric
    - Early Modern
    - Queensland, Australia

