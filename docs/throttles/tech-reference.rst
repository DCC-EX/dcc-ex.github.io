********************************************
Technical Reference for Throttle Developers
********************************************

This page is intended to capture relevant information to assist those who develop throttles compatible with DCC++ EX.

Additional throttle commands
_____________________________

Release 4.0.2 provides a number of additional throttle information commands that have been implemented to assist throttle authors to obtain information from the Command Station in order to implement turnout, route/automation, and roster features which are already found in the Withrottle implementations. 

These commands are new and do not overlap with the existing commands (which are probably due to be obsoleted as they are over complex and unfit for purpose).

Turnouts
~~~~~~~~~

The conventional turnout definition commands and the ```<H>``` responses do not contain information about the turnout description which may have been provided in an EX-RAIL script. A turnout description is much more user friendly than the identifier (eg. T123), and having a list helps the throttle UI build a suitable set of buttons.

Turnout commands
^^^^^^^^^^^^^^^^^^

**<JT>** - Returns a list of turnout IDs. The throttle should be uninterested in the turnout technology used but needs to know the IDs it can throw/close and monitor the current state.

Example response: ``<jT 1 17 22 19>`` - Turnout IDS 1, 17, 22, and 19 are defined.

**<JT 17>** - Returns the description for turnout ID 17, and the status of T=thrown or C=closed.

Example responses:

* ``<jT 17 T "Coal yard exit">`` - Description "Coal yard exit" plus state is thrown.
* ``<jT 17 C "Coal yard exit">`` - Description "Coal yard exit" plus state is closed.
* ``<jT 17 C "">`` - Indicates turnout description not defined, and state is closed.
* ``<jT 17 X>`` - Indicates turnout unknown (or possibly hidden.)

.. note:: It is still the throttles responsibility to monitor the status broadcasts. Also note that turnouts marked in EX-RAIL with the HIDDEN keyword instead of a "description" will NOT show up in these commands.

.. note:: *Note from the author:* The existing broadcast is messy and needs cleaning up, however, I'm not keen on dynamically created/deleted turnouts so I have no intention of providing a command that indicates the turnout list has been updated since the throttle started.

Automations/Routes
^^^^^^^^^^^^^^^^^^^

A throttle needs to know which EX-RAIL Automations and Routes it can show the user.

**<JA>** - Returns a list of Automations/Routes.

Example response: ``<jA 13 16 23>`` - Indicates route/automation ids 13, 16, and 23 are defined.

**<JA 13>** - Returns information for route/automation ID 13 including the description, and if it is a route (R) or automation (A).

Example responses:

* ``<jA 13 R "description">`` - Returns the description for ID 13, and that it is a route.
* ``<jA 13 A "description">`` - Returns the description for ID 13, and that it is an automation.
* ``<jA 13 X>`` - Indicates ID 13 is not found.

Whats the difference: 
  A Route is just a call to an EXRAIL ROUTE, traditionally to set some turnouts or signals but can be used to perform any kind of EXRAIL function... but its not expecting to know the loco.  
  Thus a route can be triggered by sending in for example ```</START 13>```. 

  An Automation is a handoff of the last accessed loco id to an EXRAIL AUTOMATION which would typically drive the loco away.
  Thus an Automation expects a start command with a cab id
  e.g. ```</START 13 3>```


  Roster Information:
  The ```<JR>``` command requests a list of cab ids from the roster.
  e.g. responding ```<jR 3 200 6336>```
  or <jR> for none. 

  Each Roster entry had a name and function map obtained by:
  ```<JR 200>```  reply like ```<jR 200 "Thomas" "whistle/*bell/squeal/panic">
  
  Refer to EXRAIL ROSTER command for function map format.


Obtaining throttle status.
```<t cabid>```  Requests a deliberate update on the cab speed/functions in the same format as the cab broadcast.
    ```<l cabid slot speedbyte functionMap>```
    Note that a slot of -1 indicates that the cab is not in the reminders table and this comand will not reserve a slot until such time as the cab is throttled.


COMMANDS TO AVOID

```<f cab func1 func2>```     Use ```<F cab function 1/0>```
```<t  slot cab speed dir>``` Just drop the slot number 
```<T commands>``` other than ```<T id 0/1>```
```<s>```
```<c>```
