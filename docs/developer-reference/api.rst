********************************
CommandStation-EX API Reference
********************************

.. image:: ../_static/images/engineer-level.png
  :alt: Engineer Level
  :scale: 50%

.. sidebar:: On this page

  .. contents:: 
    :depth: 1
    :local:

.. list-table:: 
  :widths: auto
  :stub-columns: 1

  * - Document status
    - Draft
  * - Document version
    - 0.1
  * - Last update
    - 5th June 2022

This page documents the API syntax and usage for CommandStation-EX.

The current API has resulted from a mix of new commands and commands inherited from the original DCC++ code base, and therefore there are some noted exceptions to the syntax, however all new commands and responses must conform to the correct syntax.

If you are looking for information on the WiThrottle protocol, you will find that documented on the `JMRI website <https://www.jmri.org/help/en/package/jmri/jmrit/withrottle/Protocol.shtml>`_.

For detailed information on the various commands and responses available with DCC++ EX, refer to the :doc:`/reference/software/command-reference` page.

1. Serial port and WiFi/Ethernet monitoring
============================================

The input collectors must monitor the serial ports on a byte by byte basis, look for a beginning "<" with ending ">", and ignore anything outside that before passing commands in for parsing.

The WiFI or ethernet collectors work on a per-transmission basis and the first byte of input determines whether the transmitted block gets sent for parsing as an API or WiThrottle command or response.

**Any input received that a throttle does not understand must be discarded and ignored.**

2. General API command usage and responses
===========================================

API commands are sent using the message format outlined below, with responses conforming to the same format.

Due to the nature of DCC++ EX being able to be operated by multiple throttles concurrently combined with the fact there is no unique throttle identifier, there is no guarantee that a response received directly after a command is sent is related. Care must be taken to take this into account.

To repeat from above, any input received that a throttle does not understand should be discarded and ignored.

Command responses
__________________

Command responses should conform to the syntax standard to ensure they are processed correctly by throttles.

Broadcast responses
____________________

Broadcast information is sent to all throttles along with WiThrottle responses on the understanding that throttles will discard and ignore any responses they do not understand.

It is mandatory that a throttle accepts and ignores a broadcast it doesn't understand.

Diagnostics and other responses
________________________________

If diagnostic commands are enabled, these are sent to the USB serial port.

If you connect a throttle to the USB serial port, you will get these correctly wrapped but do not expect to understand them. 

If, however, WiFi debug is enabled, or the <+> command is used, then the wrapping can no longer be guaranteed as the wifi traffic may contain "\*>".

General Message Format
=======================

A DCC++EX API message consists of a leading "<" symbol, a single character OPCODE, zero to n parameters separated by spaces, and a terminating ">" symbol:

``<OPCODE Param1 Param2 … ParamX>``

Messages cannot be nested, and a second "<" inside a message constitutes a syntax error.

Error responses
================

A command sent that is invalid or returns an error has a response of ``<X>``.

Memory limitations of prohibit more detailed error messages.

Parameter parsing sequence
===========================

To obtain the parameters:

Obtain the OPCODE
__________________

The first level of parsing is to obtain the single character, case sensitive OPCODE which is preceeded by a "<" character.

Obtain the parameters
______________________

The second level of parsing takes the next non-blank parameter along with each blank separated parameter and turns them into integers. There are no decimal point or float inputs. A prefix "-" may be used.

Example command and response
_____________________________

A simple example is sending an API command to retrieve the list of defined turnouts.

The command to retrieve the list of defined turnouts is ``<JT>``.

Using our syntax standard, "J" is the OPCODE, and "T" is the parameter.

The response for this command will look something like ``<jT 1 17>``.

Using our parsing sequence, we obtain the OPCODE "j", with the subsequent parameters being "T", "1", and "17".

Parameter values
=================

Parameters containing "a-z", "A-Z", or "_" are hashed to create integers. Thus a command like <D WIFI ON> is internally identical to <D wifi on>.

The translation of parameters from text to integer is base10.

Exceptions
___________

Due to legacy code and backwards compatibility requirements, there are two OPCODES that expect hexadecimal parameter values.

These are the ``<M>`` and ``<P>`` commands documented in the :ref:`reference/software/command-reference:send packet to the track` section of the Command Reference.
