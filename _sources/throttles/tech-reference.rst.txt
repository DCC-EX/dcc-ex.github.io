.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-throttles.rst
|EX-THROTTLES-LOGO|

********************************************
Technical Reference for Throttle Developers
********************************************

|engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 3
    :local:

This page is intended to capture relevant information to assist those who develop throttles compatible with |EX-CS| using the |DCC-EX Native Protocol|, not the WiThrottle protocol.

This page should be read in conjunction with the :doc:`/reference/developers/api` in order to understand how to send and parse |DCC-EX| API commands correctly, and ignore any irrelevant commands.

Considerations for throttle developers
======================================

For anyone developing a throttle or controller application, these considerations should be taken into account:

- Refer to the :doc:`/reference/developers/api`
- Refer to the :doc:`/reference/software/command-summary-consolidated`
- A throttle/controller MUST accept and ignore anything it does not understand
- Track power state has three possible states: On, Off, and Unknown
- There is no concept of a throttle 'acquiring' a loco. |BR| Simply, commands for a loco are sent to the Command Station, and the Command Station 'broadcasts' the status of any/every loco to every throttle any time a change is made to a loco.
- There is no concept of the throttle disconnecting from the Command Station.

DCC-EX Native command library - DCCEXProtocol
=============================================

For throttle developers that want to focus on throttle features and functionality, the |DCC-EX| team have now released an Arduino library that communicates with |EX-CS| via the native |DCC-EX| commands.

This library exposes numerous methods to interact with the |EX-CS| and the various objects including locos, turnouts/points, routes, and turntables.

For further information, refer to the `DCC-EX Native command library - DCCEXProtocol <https://dcc-ex.com/DCCEXProtocol/index.html>`_ documentation.

Responding to appropriate information
=====================================

In addition to understanding the specific throttle commands details on this page, throttles/controllers also must understand and respond appropriately to **broadcasts** sent from the |DCC-EX| API.

These are the *key* broadcast responses that should be understood:

- ``<p X [MAIN|PROG|JOIN]>`` - When a throttle issues a track power command, this response is sent as a broadcast (see :ref:`reference/software/command-summary-consolidated:power management`)
- ``<r address>`` - When a loco address is read on the programming track, the address is sent as a broadcast (see :ref:`reference/software/command-summary-consolidated:reading/writing configuration variables (cvs) - programming track`)
- ``<l cabid slot speed/dir func>`` - When throttles send loco commands, this is sent as a broadcast (see :ref:`reference/software/command-summary-consolidated:cab (loco) commands`)

These broadcast responses should be understood if your controller deals with turnouts/points and sensors.
- ``<H id [DCC|SERVO|VPIN|LCN] ... [0|1]>`` - When turnouts are closed/thrown, this response is broadcast (see :ref:`reference/software/command-summary-consolidated:turnouts/points`)
- ``<[q|Q] id>`` - When sensors are deactivated/activated, this response is broadcast (see :ref:`reference/software/command-summary-consolidated:sensors`)

|NOT-IN-PROD-VERSION|

There are now turntable/traverser ``<i id position moving>`` broadcast responses if the new turntable/traverser objects are implemented (see :ref:`reference/software/command-summary-consolidated:turntables/traversers`).

Working with track power states
-------------------------------

Track power can be On, Off, or Unknown. There is no broadcast of an Unknown power state though, meaning a throttle/controller must start with track power flagged as Unknown.

The throttle should only flag the power state as On or Off when either:

- A power broadcast is received from the |EX-CS| ``<p...>``
- The throttle user selects to turn track power on or off

Key Throttle commands
---------------------

Key throttle specific commands are summarised here, refer below for elaboration on the details with examples.  Refer to the :doc:`/reference/software/command-summary-consolidated` for detailed information.

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Command
    - Response
    - Description
  * - ``<t cabid speed dir>``
    - ``<l cabid slot speedbyte functionMap>`` (Broadcast)
    - Sets a cab (loco) speed and direction. (See below for the response)
  * - ``<t cabid>``
    - ``<l cabid slot speedbyte functionMap>`` (Broadcast)
    - Requests a deliberate update of cab (loco) speed/functions
  * - ``<F cabid funct state>``
    - ``<l cabid slot speedbyte functionMap>`` (Broadcast)
    - Turns cab (loco) decoder functions ON and OFF (See below for the response.)
  * - ``<JT>``
    - ``<jT id1 id2 id3 ...>``
    - Returns the defined turnout IDs
  * - ``<JT id>``
    - ``<jT id state "[description]">``
    - Returns the ID, state, and description of the specified turnout ID
  * - ``<JA>``
    - ``<jA id1 id2 id3 ...>``
    - Returns the defined automation and route IDs
  * - ``<JA id>``
    - ``<jA id type "[description]">``
    - Returns the ID, type (A=automation or R=route), and description of the specified automation/route ID
  * - ``<JR>``
    - ``<jR id1 id2 id3 ...>``
    - Returns the defined roster entry IDs
  * - ``<JR id>``
    - ``<jR id "description" "function1/function2/function3/...">``
    - Returns the ID, description, and function map of the specified roster entry ID
  * - ``<JO>``
    - ``<jO id1 id2 id3 ...>``
    - Returns the defined turntable IDs
  * - ``<JO id>``
    - ``<jO id type position position_count "[description]">``
    - Returns the ID, type (0=DCC or 1=EXTT), current position, position count, and description of the specified turntable ID
  * - ``<JP id>``
    - ``<jP id index angle "[description]">``
    - Returns the turntable ID, position index, angle, and description of each defined position for the specified turntable ID

----

Additional Details
------------------

Refer to the :doc:`/reference/software/command-summary-consolidated` for detailed information on these commands.

Setting cab (loco) status
^^^^^^^^^^^^^^^^^^^^^^^^^

``<t cabid speed dir>`` - Sets a cab (loco) speed and direction. (See below for the response.)

``<F cab funct state>`` - Turns cab (loco) decoder functions ON and OFF. (See below for the response.)

Obtaining loco (cab) status
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``<t cabid>`` - Requests a deliberate update on the cab speed/functions in the same format as the cab broadcast.

  Example response:

  * ``<l cabid slot speedbyte functionMap>`` - Note that a slot of -1 indicates that the cab is not in the reminders table and this command will not reserve a slot until such time as the cab is throttled.

  Where:

  * cabid = Loco's DCC address
  * slot = Position in the reminders table (for the convenience of slot managers later)
  * speedbyte = The DCC packet speed bye including the direction bit (NOT the same as the DCC-EX speed)

      * reverse - 2-127 = speed 1-126, 0 = stop
      * forward - 130-255 = speed 1-126, 128 = stop

  * functionMap = Binary map of which functions are ON ( 1=F0, 2=F1, 3=F0&F1   etc.)

  The above is not a direct response, but rather as a broadcast that will be triggered as a result of any throttle command being issued by any device for the cab(loc) in question.

Turnouts/Points
^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^

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
~~~~~~~~~~~~~~~~~~~~~~

A **ROUTE** is just a call to an EX-RAIL ROUTE, traditionally to set some turnouts or signals but can be used to perform any kind of EX-RAIL function, but is not expecting to know the loco ID.

* A route can be triggered by sending, for example, ``</START 13>``. 

An **AUTOMATION** is a handoff of the last accessed loco ID to an EX-RAIL AUTOMATION which would typically drive the loco away.

* An automation expects a start command with a cab ID, for example ``</START 13 3>``.

Roster Information
^^^^^^^^^^^^^^^^^^

``<JR>`` - Requests a list of cab IDs from the roster.

  Example responses:

  * ``<jR 3 200 6336>`` - Returns the roster entry IDs 3, 200, and 6336 are defined.
  * ``<jR>`` - Indicates no roster entries are defined.

``<JR 200>`` - Returns the roster name function map for roster ID 200.

  Example response:

  * ``<jR 200 "Thomas" "whistle/*bell/squeal/panic">`` - Returns the defined description "Thomas" with each defined function's name. Refer to the EX-RAIL ROSTER command for function map format.

Turntables/Traversers
^^^^^^^^^^^^^^^^^^^^^

|NOT-IN-PROD-VERSION|

A new feature has been added to support control of turntables/traversers from throttles, including the ability for throttles to "draw" turntable positions as defined to support graphical operation. If |EX-R| commands are used to define turntables and their associated positions, a description for the turntable as well as each position is able to be defined.

Note that to obtain a complete definition for a turntable/traverser, the turntable object needs to be queried first (``<JO id>``) followed by the position query (``<JP id>``) to obtain all defined positions for the object.

``<JO>`` - Returns a list of turntable IDs.

  Example response:

  - ``<jT 1 2>`` - Turnable IDs 1 and 2 are defined.

``<JO 1>`` - Returns details of turntable ID 1.

  Example responses:

  - ``<jO 1 0 1 5 "DCC Turntable">`` - DCC turntable type currently at position 1, with 5 defined positions and a description "DCC Turntable".
  - ``<jO 1 1 0 11 "EX-Turntable">`` - EX-Turntable type currently at the home position (0), with 11 defined positions and a description "EX-Turntable"

``<JP 1>`` - Returns all positions for turntable ID 1.

  Example responses (will return all positions):

  - ``<jP 1 0 0 "">`` - Position 0, unused for DCC turntables, "home" for EX-Turntable
  - ``<jP 1 1 100 "Turntable position 1">`` - Position 1, 10 degrees from home
  - ``<jP 1 2 1800 "Turntable position 2">`` - Position 2, 180 degrees from home

Commands to avoid
=================

* ``<f cab func1 func2>`` - Use ``<F cab function 1/0>`` instead
* ``<t  slot cab speed dir>`` - Just drop the slot number
* ``<T commands>`` - other than ``<T id 0/1>``
* ``<D>`` - If the throttle developer sees the need to obtain info which is <D> only please contact us to get a better way to do it
