.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-reference.rst
|EX-REF-LOGO|

***************************
DCC-EX Native API Reference
***************************

|engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 1
    :local:

This page documents the API syntax and usage for |EX-CS|.

The current API has resulted from a mix of new commands and commands inherited from the original DCC++ code base, and therefore there are some noted exceptions to the syntax, however all new commands and responses must conform to the correct syntax.

.. note:: 

  Legacy commands and responses that do not comply with this documented syntax will be deprecated in future versions.

If you are looking for information on the WiThrottle protocol, you will find that documented on the `JMRI website <https://www.jmri.org/help/en/package/jmri/jmrit/withrottle/Protocol.shtml>`_.

For detailed information on the various commands and responses available with |EX-CS|, refer to the :doc:`/reference/software/command-summary-consolidated` page.

1. API Client definition
=========================

This API reference applies to any API client that makes use of these commands and responses.

API clients may include:

- Throttles (both wired and wireless)
- |JMRI|
- Other integrations (e.g. RedHat)

2. Serial port and WiFi/Ethernet monitoring
============================================

The input collectors must monitor the serial ports on a byte by byte basis, look for a beginning ``<`` with ending ``>``, and ignore anything outside that before passing commands in for parsing.

The WiFI or ethernet collectors work on a per-transmission basis and the first byte of input determines whether the transmitted block gets sent for parsing as an API or WiThrottle command or response.

**Any input received that an API client does not understand must be discarded and ignored.**

3. General API command usage and responses
===========================================

API commands are to be sent using the message format outlined below, with responses conforming to the same format.

Due to the nature of |EX-CS| being able to be operated by multiple API clients concurrently combined with the fact there is no unique client identifier, there is no guarantee that a response received directly after a command is sent is related. Care must be taken to take this into account.

To repeat from above, any input received that an API client does not understand should be discarded and ignored.

3.1. Command responses
----------------------

Command responses should conform to the syntax standard to ensure they are processed correctly by API clients.

3.2. Broadcast responses
------------------------

Broadcast information is sent to all API clients along with WiThrottle responses on the understanding that API clients will discard and ignore any responses they do not understand.

It is mandatory that an API client accepts and ignores a broadcast it doesn't understand.

3.3. Diagnostics and other responses
------------------------------------

If diagnostic commands are enabled, these are sent to the USB serial port.

If you connect an API client to the USB serial port, you will get these correctly wrapped but do not expect to understand them. 

If, however, WiFi debug is enabled, or the ``<+>`` command is used, then the wrapping can no longer be guaranteed as the wifi traffic may contain ``*>``.

4. General Message Format
==========================

A DCC-EX API message consists of a leading ``<`` symbol, a single character OPCODE, zero to n parameters separated by spaces, and a terminating ``>`` symbol:

``<OPCODE Param1 Param2 … ParamX>``

Messages cannot be nested, and a second ``<`` inside a message constitutes a syntax error.

5. Error and empty responses
=============================

A command sent that is invalid has a response of ``<X>``.

Memory limitations prohibit more detailed error messages.

6. Parameter values
====================

There are three types of parameters in use:

6.1. Keyword
------------

These are a consecutive sequence of one or more non-blank characters consisting of ``a-z``, ``A-Z``, ``0-9``, or ``_``, e.g. "JOIN", "WIFI", "ON", "SPEED28".

Keyword parameters are internally hashed to created integers and may start with any of these characters. The |EX-CS| code does not differentiate between keywords and numbers internally.

For example, a keyword of "3RAIL" would be valid if it were to be implemented.

6.2. Numeric
------------

These are a consecutive sequence of one or more digits, with an optional leading ``-`` to indicate a negative value. Unless noted in `a.1. parameter values`_, these numbers are base10.

6.3. String
-----------

These are surrounded by a leading and trailing ``"`` and may contain text including spaces e.g. "This is a turnout description".

Appendix A. Exceptions
=======================

A.1. Parameter values
---------------------

Due to legacy code and backwards compatibility requirements, there are two OPCODES that expect hexadecimal parameter values.

These are the ``<M>`` and ``<P>`` commands documented in the :ref:`reference/software/command-reference:send packet to the track` section of the Command Reference.

Appendix B. Suggested parameter parsing sequence
=================================================

To obtain the parameters:

B.1. Obtain the OPCODE
----------------------

The first level of parsing is to obtain the single character, case sensitive OPCODE which is preceded by a ``<`` character.

B.2. Obtain the parameters
--------------------------

The second level of parsing takes the next non-blank parameter along with each blank separated parameter and turns them into integers. There are no decimal point or float inputs. A prefix ``-`` may be used.

B.3. Example command and response
---------------------------------

A simple example is sending an API command to retrieve the list of defined turnouts.

The command to retrieve the list of defined turnouts is ``<JT>``.

Using our syntax standard, "J" is the OPCODE, and "T" is the parameter.

The response for this command will look something like ``<jT 1 17>``.

Using our parsing sequence, we obtain the OPCODE "j", with the subsequent parameters being "T", "1", and "17".

Appendix C. Further information
================================

C.1. Keyword parameters are not case sensitive
----------------------------------------------

Unlike OPCODES, keyword parameters are not case sensitive.

As noted, parameters containing ``a-z``, ``A-Z``, or ``_`` are hashed to create integers which results in commands such as ``<D WIFI ON>`` being treated identically to ``<D wifi on>``.
