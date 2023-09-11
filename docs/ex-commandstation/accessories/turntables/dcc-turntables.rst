.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-description.rst

|conductor| |tinkerer| |engineer|

*************************
DCC Turntables/traversers
*************************

|NOT-IN-PROD-VERSION|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:

Defining DCC turntables/traversers
==================================

DCC turntables have pre-configured positions around the turntable that are selected by activating the associated linear DCC address.

To define a DCC turntable, you must create the turntable object with the ``<I id DCC home>`` command, or the ``DCC_TURNTABLE(id, home [,"description"])`` |EX-R| command.

Once the turntable object is defined, you must add each defined position using the ``<I id ADD position dcc_address angle>`` command, or the ``TT_ADDPOSITION(turntable_id, position_id, dcc_address, angle [, "description"])`` |EX-R| command.

In these commands, the **home** and **angle** parameters are there to enable throttle developers to "draw" turntables in software throttles, and have no impact on the operation of the turntable. These can simply be set to 0 (zero) when not in use.

DCC-EX native command example
-----------------------------

To define a DCC accessory turntable with an ID of 201, starting at linear DCC address 201, and with a total of 10 positions, these DCC-EX native commands must be run (note we are not caring about the **home** or **angle** parameters):

.. code-block:: 

  <I 201 DCC 0>
  <I 201 ADD 1 201 0>
  <I 201 ADD 2 202 0>
  <I 201 ADD 3 203 0>
  <I 201 ADD 4 204 0>
  <I 201 ADD 5 205 0>
  <I 201 ADD 6 206 0>
  <I 201 ADD 7 207 0>
  <I 201 ADD 8 208 0>
  <I 201 ADD 9 209 0>
  <I 201 ADD 10 210 0>

Once these are defined, it can be operated using the ``<I id position>`` command:

.. code-block:: 

  <I 201 1>   - Rotate to the first position at linear address 201
  <I 201 10>  - Rotate to the last position at linear address 210

EXRAIL command example
----------------------

To repeat the above example using |EX-R| instead, these commands need to be added to "myAutomation.h", noting the addition of the **description** parameter not available using the native commands:

.. code-block:: 

  DCC_TURNTABLE(201,0,"My DCC turntable")
  TT_ADDPOSITION(201,1,201,0,"Roundhouse stall 1")
  TT_ADDPOSITION(201,2,202,0,"Roundhouse stall 2")
  TT_ADDPOSITION(201,3,203,0,"Roundhouse stall 3")
  TT_ADDPOSITION(201,4,204,0,"Roundhouse stall 4")
  TT_ADDPOSITION(201,5,205,0,"Roundhouse stall 5")
  TT_ADDPOSITION(201,6,206,0,"Roundhouse stall 6")
  TT_ADDPOSITION(201,7,207,0,"Turntable entry")
  TT_ADDPOSITION(201,8,208,0,"Maintenance bay 1")
  TT_ADDPOSITION(201,9,209,0,"Maintenance bay 2")
  TT_ADDPOSITION(201,10,210,0,"Maintenance bay 3")

Throttle control
----------------

The result of both examples above is that the turntable objects are advertised to throttles that understand turntable objects, meaning they can be controlled in a similar manner to turnouts/points.

Note, however, that as this is brand new functionality, there are likely to be no throttles that understand these commands yet.

Automation options
------------------

Other |EX-R| commands have been added to enable automation related to turntable/traverser activities, including the ``ONROTATE(id)`` event handler and ``IF_TTPOSITION(id,position)`` test command to respond to turntable movements, and the ``ROTATE_DCC(id,position)`` command to control the turntable from sequences.

The limitation of DCC accessory turntables is the lack of feedback as to when a rotation or movement has completed, so a suitable delay would need to be calculated for automation sequences to allow sufficient time for rotations to complete prior to performing other activities.

For example, if you wish a warning light to be lit for the duration of a rotation, you could achieve this with the ``ONROTATE(ID)`` event handler:

.. code-block:: 

  ONROTATE(201)     // This event triggers when turntable ID 201 is rotated
    SET(26)         // Turn the warning light on connected to pin 26
    DELAY(10000)    // Wait 10 seconds for the rotation to complete
    RESET(26)       // Turn the warning light off
  DONE
