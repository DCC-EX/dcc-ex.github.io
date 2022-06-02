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

1. General Message Format
==========================

A DCC++EX API message consists of a leading "<" symbol, a single character OPCODE, zero to n parameters separated by spaces, and a terminating ">" symbol:

``<OPCODE Param1  Param2   …   ParamX>``

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

OPCODEs are single characters following immediately the leading "<" symbol or separated from it by one or more spaces. In other words: The first non-blank character after the leading "<" symbol is the OPCODE.

2.1. Reserved OPCODEs
______________________

"*" is reserved OPCODE for comment lines. The entire content of the message up to the closing ">" symbol is a comment and does not have to follow any rules

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

4.2.4. Floating point number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

optional "-" symbol to indicate a negative value, followed by at least one digit before the floating point symbol "." and at least one digit after. Examples: 23.67, -5.392

4.2.5. String Parameter
^^^^^^^^^^^^^^^^^^^^^^^^

A string parameter is sequence of characters starting and ending with a ‘”’ symbol. Between these symbols, any character, including "*" and Space, is acceptable, except for the ‘”’ itself.
