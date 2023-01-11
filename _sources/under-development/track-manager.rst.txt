.. include:: /include/include.rst
.. include:: /include/include-l1.rst
  
**********************************
*Under Development:* Track Manager
**********************************

|tinkerer| |engineer| |githublink-ex-commandstation-button2|

|NOT-IN-PROD-VERSION|

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:

Formerly referred to as "DC Districts", Track Manager is a new feature under active development to allow an |EX-CS| with the correct hardware and software to control up to 8 separate tracks in different modes including DCC main, DCC programming, and DC.

One key item to note with DC vs. DCC is that in DCC mode, forward/reverse is determined by the DCC decoder, not the track, whereas in DC mode the direction is dependent upon the track polarity.

.. warning:: 

  This feature is under active development, meaning commands, features, and behaviour may change without notice. While we endeavour to keep these features functional, our development releases are updated regularly and we cannot guarantee there are no bugs that will have unexpected results.

  If using our development release and, especially, the Track Manager feature, we highly recommend keeping in touch with conversations and developments via our `Discord server <https://discord.gg/PuPnNMp8Qf>`_.

  You can also use our new GitHub issue templates to report a bug: |githublink-ex-commandstation-button2|

Hardware requirements
=====================

In order to utilise Track Manager's DC mode, your motor shield must have a brake pin, and this must be defined in your "config.h" motor shield definition.

If you are using a non-standard motor shield, you will need to validate if it is capable of this configuration. We will populate the list of compatible motor shields over time.

If your intention is only to have multiple DCC main or programming tracks, this is not required.

Track Manager commands
======================

To configure Track Manager, a new command ``<= trackletter mode [id]>`` has been added, where:

* ``trackletter`` is A through H
* ``mode`` is one of MAIN, PROG, DC, DCX, or OFF (DCX is DC with reversed polarity)
* ``id`` is the cab ID required when specifying DC or DCX

To display the current Track Manager configuration use the command ``<=>``.

For example, to configure a DCC main track, a DCC programming track, a DC track (using cab ID 100), and a reversed polarity DC track (using cab ID 101), these commands are required:

.. code-block:: 

  <= A MAIN>
  <= B PROG>
  <= C DC 100>
  <= D DCX 101>

.. note:: 

  When specifying a DC or DCX cab ID, be sure not to use one of your existing DCC locomotive IDs, otherwise and command sent to control a loco on that DC or DCX track will also operate your DCC loco with the same address.

Note on PWM frequency
=====================

Different microcontrollers utilise different PWM frequencies, and at present, these default frequencies are in use rather than using software to define them.

The side effect of these differing frequencies is that you may notice humming or sometimes squealing noises from older DC motors.

The known PWM frequencies are:

* Mega2560 - 122.55Hz
* ESP32 - variable
* Others (eg. STM32 Nucleo) - typically 1000Hz