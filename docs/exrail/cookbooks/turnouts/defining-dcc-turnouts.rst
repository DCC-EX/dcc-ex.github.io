.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Defining DCC turnouts/points
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

DCC Turnouts (or points) operate by listening to DCC messages sent along the track by the command station.
Each turnout has a DCC address which may be specified as a pair of values (address,subaddress) or a single value linear address. Its generally easier to think in terms of the linear address but it makes no difference whatever to the kind of DCC message sent, other than the conversion from (address,subaddress) to linear is badly thought out and inconsistent between DCC implementations due to historically/histerically ambiguous standards.

Define DCC based turnouts using |EX-R|.

.. code-block:: cpp

    TURNOUTL(id, address, "description")

    TURNOUT(id, shortAddress, subAddress, "description")

- ``id`` = Unique turnout ID within the CommandStation. All other turnout commands will refer to this turnout by this id.
- ``address`` = the DCC address that the turnout decoder is listening to |BR| or |BR| ``shortAddress,subAddress`` - the alternative form of the same address.
- ``description`` = A human-friendly description of the turnout that will appear in WiThrottle apps and Engine Driver. Note that this must be enclosed in quotes ``""``. In some cases the HIDDEN keyword can be used here to prevent the turnout being visible to the throttles.

For example:

.. code-block:: cpp

    TURNOUTL(123,55,"Up the junction")
    TURNOUT(124,12,3,"Down the mine")
    TURNOUTL(125,56,HIDDEN) // not visible to throttles
