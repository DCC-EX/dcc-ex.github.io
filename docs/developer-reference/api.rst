*************************
API syntax documentation
*************************

.. image:: ../_static/images/engineer-level.png
  :alt: Engineer Level
  :scale: 50%

.. sidebar:: On this page

  .. contents:: 
    :depth: 1
    :local:

This API syntax page defines the current defined syntax used by API commands. These have resulted from a mix of legacy inheritance from the original DCC++ code, in addition to newer commands.

Port and WiFi/Ethernet monitoring
==================================

The input collectors must monitor the serial ports on a byte by byte basis, look for a beginning "<" with ending ">", and ignore anything outside that before passing commands in for parsing.

The WiFI or ethernet collectors work on a per-transmission basis and the first byte of input determines whether the transmitted block gets sent for parsing as a command or WiThrottle.

Parameter parsing sequence
===========================

To obtain the parameters

The first level of parsing is to obtain the single character, case sensitive OPCODE which may be preceeded by any number of blanks or a "<" character.

The second level of parsing takes the next non-blank parameter along with each blank separated parameter and turns them into integers. There are no decimal point or float inputs. A prefix "-" may be used.

For example, sending the command ``<JT>`` to obtain the list of turnouts responds with something like ``<jT 1 17>``.

The OPCODE is "j", with the subsequent parameters being "T", "1", and "17".

Parameters containing "a-z", "A-Z", or "_" are hashed to create integers. Thus a command like <D WIFI ON> is internally identical to <D wifi on>.

  * Some OPCODES are documented in a way that indicates they may have two characters, eg. <Jt ...>. This does not break the syntax rule, and in this example "J" is the OPCODE, with "t" as the first parameter.

The translation of parameters from text to integer is normally base10 but for two specific opcodes the parser is instructed to operate in hex. That's just history. 
Parameters may be separated by any number of spaces but using more than one is wasting cs comms and cpu power and should be discouraged.
There is no need to put a space between the opcode and the first parameter although it is often more readable tjat way. ( I have described the J command as if it were a two character opcode but  <JT>  <Jt> and < J   T >  are all the same thing to the parser. 
Memory prohibits fancy error messages for all the things that can be wrong.. a reply of <X> is commonly used

I think from the above, its best to only formalise the way it should work rather than rhe myriad of relaxed  ways it might work.. eg one space between parameters.
Responses... are a separate issue.
Responses and broadcasts fall into several categories 
- broadcast information sent to all throttles. There are a couple of issues here where we send the <>   and withrottle responses together to all throttles in the knowledge that each will ignore the irrelevant one. We can choose the define the interface on the basis that throttles should ignore what's not for them or we could split the broadcast at the expense of processing time on the cs.

- direct responses to commands. Yes we should fix any that are not  correctly wrapped.

- diagnostics sent to usb serial. If you connect the throttle to the USB serial... you will get these correctly wrapped but do not expect to understand them. 

If, however, someone turns on wifi debug or uses the <+> command then the wrapping can no longer be guaranteed as the wifi traffic may contain "\*>".


It's also important to specify that the cs is not in  position to maintain a conversation about which throttle supports which broadcasts... so it should be mandatory that a throttle accept and ignore a broadcast it doesn't understand.






















3. General Message Format
==========================

A DCC++EX API message consists of a leading "<" symbol, a single character OPCODE, zero to n parameters separated by spaces, and a terminating ">" symbol:

``<OPCODE Param1 Param2 … ParamX>``

Messages cannot be nested, and a second "<" inside a message constitutes a syntax error.

Spaces between the leading "<" symbol and the OPCODE, between the OPCODE and the start of the first parameter, and between the end of the last parameter and the trailing ">" symbol are optional.

Examples for valid formats for a <p1> return message:

.. code-block:: 

  <p1>
  <p 1>
  < p1>
  < p 1>
  <p1 >

2. OPCODE Format
=================

OPCODEs are single, case sensitive characters immediately following the leading "<" symbol, or separated from it by one or more spaces. In other words: The first non-blank character after the leading "<" symbol is the OPCODE.

2.1. Reserved OPCODEs
______________________

"*" is a reserved OPCODE for comment lines. The entire content of the message up to the closing ">" symbol is a comment and does not have to follow any rules.

3. General Parameter Format
============================

A message parameter is a sequence of characters.  Depending on the content, parameters can be of several data types as outlined below. A message can have any number of parameters separated by space symbols. The first parameter of the message may or may not be separated from the OPCODE by a space symbol.

4. Parameter Data Types
========================

4.1. Keyword Parameters
________________________

A sequence of characters without space symbol. The first character after the space separator must not be a ‘”’ symbol. Example: Keyword JOIN in <p1 JOIN>

4.2. Numerical Parameters
__________________________

Numerical values are a sequence of characters that represent a numerical value. Several formats are possible:

4.2.1. Decimal integer
^^^^^^^^^^^^^^^^^^^^^^^

optional "-" symbol to indicate a negative value, followed by a sequence of decimal digits ("0".."9")

4.2.2. Hexadecimal integer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

"$" marker symbol , followed by a sequence of hex digits ("0".."9", "A".."F") forming a hexadecimal integer. Examples: $2367, $B5C2

4.2.3. Binary integer
^^^^^^^^^^^^^^^^^^^^^^

"%" marker symbol followed by a sequence of binary digits ("0".."1") forming a hexadecimal integer. Examples: %01100011, %1100

4.2.5. String Parameter
^^^^^^^^^^^^^^^^^^^^^^^^

A string parameter is sequence of characters starting and ending with a ‘”’ symbol. Between these symbols, any character, including "*" and Space, is acceptable, except for the ‘”’ itself.
