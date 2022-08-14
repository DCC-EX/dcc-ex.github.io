.. include:: /include/include.rst
.. include:: /include/include-l2.rst
********************************************
Technical Reference for Throttle Developers
********************************************

|engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

This page is intended to capture relevant information to assist those who develop throttles compatible with |EX-CS|.

Additional throttle commands
=============================

Release 4.0.2 provides a number of additional throttle information commands that have been implemented to assist throttle authors to obtain information from the Command Station in order to implement turnout, route/automation, and roster features which are already found in the wiThrottle implementations. 

These commands are new and do not overlap with the existing commands (which are probably due to be obsoleted as they are over complex and unfit for purpose).

Throttle command summary
=========================

All throttle specific commands are summarised here, refer below for elaboration on the details with examples.

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<JT>``
    - ``<jT id1 id2 id3 ...>``
    - Returns the defined turnout IDs.
  * - ``<JT id>``
    - ``<jT id state "[description]">``
    - Returns the ID, state, and description of the specified turnout ID.
  * - ``<JA>``
    - ``<jA id1 id2 id3 ...>``
    - Returns the defined automation and route IDs.
  * - ``<JA id>``
    - ``<jA id type "[description]">``
    - Returns the ID, type (A=automation or R=route), and description of the specified automation/route ID.
  * - ``<JR>``
    - ``<jR id1 id2 id3 ...>``
    - Returns the defined roster entry IDs.
  * - ``<JR id>``
    - ``<jR id "description" "function1/function2/function3/...">``
    - Returns the ID, description, and function map of the specified roster entry ID.
  * - ``<t cabid>``
    - ``<l cabid slot speedbyte functionMap>``
    - Requests a deliberate update of cab speed/functions in the same format as the cab broadcast.

Detailed command reference
===========================

Turnouts
_________

The conventional turnout definition commands and the ``<H>`` responses do not contain information about the turnout description which may have been provided in an EX-RAIL script. A turnout description is much more user friendly than the identifier (eg. T123), and having a list helps the throttle UI build a suitable set of buttons.

``<JT>`` - Returns a list of turnout IDs. The throttle should be uninterested in the turnout technology used but needs to know the IDs it can throw/close and monitor the current state.

Example response:

* ``<jT 1 17 22 19>`` - Turnout IDS 1, 17, 22, and 19 are defined.

``<JT 17>`` - Returns the description for turnout ID 17, and the status of T=thrown or C=closed.

Example responses:

* ``<jT 17 T "Coal yard exit">`` - Description "Coal yard exit" plus state is thrown.
* ``<jT 17 C "Coal yard exit">`` - Description "Coal yard exit" plus state is closed.
* ``<jT 17 C "">`` - Indicates turnout description not defined, and state is closed.
* ``<jT 17 X>`` - Indicates turnout unknown (or possibly hidden.)

.. note:: It is still the throttles responsibility to monitor the status broadcasts. Also note that turnouts marked in EX-RAIL with the HIDDEN keyword instead of a "description" will NOT show up in these commands.

.. note:: *Note from the author:* The existing broadcast is messy and needs cleaning up, however, I'm not keen on dynamically created/deleted turnouts so I have no intention of providing a command that indicates the turnout list has been updated since the throttle started.
  - Chris Harlow

Automations/Routes
___________________

A throttle needs to know which EX-RAIL Automations and Routes it can show the user.

``<JA>`` - Returns a list of Automations/Routes.

Example response:

* ``<jA 13 16 23>`` - Indicates route/automation ids 13, 16, and 23 are defined.

``<JA 13>`` - Returns information for route/automation ID 13 including the description, and if it is a route (R) or automation (A).

Example responses:

* ``<jA 13 R "description">`` - Returns the description for ID 13, and that it is a route.
* ``<jA 13 A "description">`` - Returns the description for ID 13, and that it is an automation.
* ``<jA 13 X>`` - Indicates ID 13 is not found.

What's the difference?
^^^^^^^^^^^^^^^^^^^^^^^

A **ROUTE** is just a call to an EX-RAIL ROUTE, traditionally to set some turnouts or signals but can be used to perform any kind of EX-RAIL function, but is not expecting to know the loco ID.

* A route can be triggered by sending, for example, ``</START 13>``. 

An **AUTOMATION** is a handoff of the last accessed loco ID to an EX-RAIL AUTOMATION which would typically drive the loco away.

* An automation expects a start command with a cab ID, for example ``</START 13 3>``.

Roster Information
___________________

``<JR>`` - Requests a list of cab IDs from the roster.

Example responses:

* ``<jR 3 200 6336>`` - Returns the roster entry IDs 3, 200, and 6336 are defined.
* ``<jR>`` - Indicates no roster entries are defined.

``<JR 200>`` - Returns the roster name function map for roster ID 200.

Example response:

* ``<jR 200 "Thomas" "whistle/*bell/squeal/panic">`` - Returns the defined description "Thomas" with each defined function's name. Refer to the EX-RAIL ROSTER command for function map format.

Obtaining throttle status
__________________________

``<t cabid>`` - Requests a deliberate update on the cab speed/functions in the same format as the cab broadcast.

Example response:

* ``<l cabid slot speedbyte functionMap>`` - Note that a slot of -1 indicates that the cab is not in the reminders table and this command will not reserve a slot until such time as the cab is throttled.

Where:

* cabid = Loco's DCC address
* slot = Position in the reminders table (for the convenience of slot managers later)
* speedbyte = The DCC packet speed bye including the direction bit (NOT the same as the DCC++ speed)
* functionmap = Binary map of which functions are ON ( 1=F0, 2=F1, 3=F0&F1   etc.)

Commands to avoid
==================

* ``<f cab func1 func2>`` - Use ``<F cab function 1/0>`` instead.
* ``<t  slot cab speed dir>`` - Just drop the slot number .
* ``<T commands>`` - other than ``<T id 0/1>``.
* ``<s>`` - This may need to change in the future to support new features.
* ``<c>`` - This may need to change in the future to support new features.
