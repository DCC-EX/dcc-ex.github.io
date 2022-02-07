****************************
DCC++ EX Command Reference
****************************

This is a detailed reference. For a summary version, please see :doc:`Command Summary <command-summary>`

`CommandStation-EX <https://github.com/DCC-EX/CommandStation-EX>`_ Provides an Application Programming Interface (API) that other applications use to send simple text commands that can operate your Command Station. Several "front end" controllers are available or you can easily create your own. Here are some examples:

* :doc:`exWebThrottle </throttles/ex-webthrottle>` - Our DCC++ EX browser based throttle using your USB cable. See it and run from the web. You can also install it by clicking a button from within WebThrottle-EX itself!

* `Engine Driver <https://enginedriver.mstevetodd.com/>`_ - Cellphone App WiFi Throttle  

* `JMRI (Java Model Railroad Interface) <http://www.jmri.org/>`_

* A serial console, like the Arduino Serial Monitor or PuTTY

* `Gregg Bermann's DCC++ Controller Software <https://github.com/DccPlusPlus/Controller>`_

This reference explains the available command structure, and for commands that provide them, their responses. If you are testing your Command Station or writing your own control program, make sure you have the latest release of the `CommandStation-EX Firmware <https://github.com/DCC-EX/CommandStation-EX>`_.

You can view and edit this code in the `Arduino IDE <https://www.arduino.cc/en/Main/Software>`_ or in `PlatformIO <https://github.com/DCC-EX/CommandStation-EX/blob/master/CONTRIBUTING.md>`_ Software from `GitHub <https://github.com/DCC-EX>`_. If you are new to we suggest you start with the `DCC++ EX Webpage <https://dcc-ex.com>`_.  

SINGLE LETTER COMMANDS
=======================

 ``<0>`` Number Zero: Turn Power **OFF** to tracks (Both Main & Programming)
  
  .. code-block:: none

      RETURNS: <p0> : Power to tracks OFF. (See extended power command below)

 ``<1>`` Number One: Turn Power **ON** to tracks (Both Main & Programming). 

  .. code-block:: none

      RETURNS: <p1> : Power to tracks ON. (See extended power command below)

 ``<c>`` Lower case c: Displays the instantaneous current on the MAIN Track

  .. code-block:: none

      RETURNS: <c "CurrentMAIN" CURRENT C "Milli" "0" MAX_MA "1" TRIP_MA >
      

  Example <c CurrentMAIN 120 C Milli 0 1996 1 1800>

  The above shows a MAIN track current of 120mA, 1.996A max, 1.8A trip current

  * ``c`` - the current response indicator
  * ``CurrentMAIN`` - Static text for software like JMRI
  *  ``CURRENT`` - Current in MilliAmps
  *  ``C`` - Designator to signify this is a current meter (V would be for voltage)
  *  ``Milli`` - Unit of measure for external sofware with a meter like JMRI (Milli, Kilo, etc.)
  *  ``0`` - numbered parameter for external sofware (1,2,3, etc.)
  *  ``MAX_MA`` - The maximum current handling of the motor controller in MilliAmps
  *  ``1`` - number parameter for external software (we use 2 parameters here, 0 and 1)
  *  ``TRIP_MA`` - The overcurrent limit that will trip the software circuit breaker in mA
  

 ``<E>`` Upper case E : Command to **Store** definitions to EEPROM

  .. code-block:: none

      RETURNS: <e nTurnouts nSensors>

 ``<e>`` Lower Case e: Command to **Erase ALL (turnouts, sensors, and outputs)** definitions from EEPROM 

  .. code-block:: none

      RETURNS: <0> EEPROM Empty


  *NOTE:There is NO Un-Delete*


 ``<Q>`` Upper Case Q : Lists Status of all sensors.

  .. code-block:: none

      RETURNS: <Q ID> (active) or <q ID> (not active)

 ``<R>`` Upper Case R : Read Loco address (programming track only)

  .. code-block:: none

      RETURNS: <r ADDRESS> where it finds the address of our loco or <r -1> for a read failure.


 ``<S>`` Upper Case S : Lists all defined sensors. 

  .. code-block:: none

      RETURNS: <Q ID PIN PULLUP> for each defined sensor or <X> if no sensors defined. 

 ``<s>`` Lowercase "s": DCC++ EX CommandStation Status

  .. code-block:: none

       RETURNS: Track power status, Version, Microcontroller type, Motor Shield type, build number, and then any defined turnouts, outputs, or sensors.
       Example: <iDCC-EX V-3.0.4 / MEGA / STANDARD_MOTOR_SHIELD G-75ab2ab><H 1 0><H 2 0><H 3 0><H 4 0><Y 52 0><q 53><q 50>

 ``<T>`` Upper Case T : Lists all defined turnouts. 

  .. code-block:: none

      RETURNS: One of the following for each defined turnout or <X> if no turnouts defined.
      <H ID DCC ADDRESS SUBADDRESS THROWN>     -- DCC Accessory Turnouts
      <H ID SERVO PIN THROWNPOSITION CLOSEDPOSITION PROFILE THROWN>  -- Servo Turnouts
      <H ID VPIN PIN THROWN>  -- VPIN Turnouts
      <H ID LCN THROWN>  -- LCN Turnouts
      **ID** - ID assigned to the turnout
      **THROWN** - "0" is closed.  "1" is thrown.
      The rest of the parameters are as defined for the turnout definition commands.

 ``<+X>`` Plus sign and upper case X : A special case WiFi command for Engineers to force the CS into "WiFi Connected" mode so that it processes commands from a WiFi board. This is for when users override our network startup and enter their own <+COMMAND> AT commands.

 ``<Z>`` Upper Case Z : Lists all defined output pins

  .. code-block:: none

      RETURNS: <Y ID PIN IFLAG STATE> for each defined output pin or <X> if no output pins defined

 ``<!>`` Exclamation Point : EMERGENCY STOP - Stops all locos on the track but leaves power on.

  .. code-block:: none

      RETURNS: NONE

* 
  There are a few other Debugging commands that should only be used by advanced users (Potentially Harmful if not used correctly).

Track Power Commands
====================

``<0|1 MAIN|PROG|JOIN>`` - Turns power on and off to the MAIN and PROG tracks independently from each other and allows joining the MAIN and PROG tracks together

  .. code-block:: none

      RETURNS: <pX [MAIN|PROG|JOIN]> where "X" is 0 for off and 1 for on. MAIN, PROG and JOIN are returned when you invoke commands on just one track.

Examples:

``<1>`` - Turn power to all tracks on. RETURNS: <p1>

``<0>`` - Turn power to all tracks off. RETURNS: <p0>

``<1 MAIN>`` - Turns on power just to the MAIN track. RETURNS: <p1 MAIN>

``<0 PROG>`` - Turns off power just to the PROG track. RETURNS: <p0 PROG>

``<1 JOIN>`` - Joins both tracks together to be both MAIN (ops) tracks. Any other power command turns it off. RETURNS: <p1 JOIN>


.. note:: The use of the JOIN function ensures that the DCC signal for the MAIN track is also sent to the PROG track. This allows the prog track to act as a siding (or similar) in the main layout even though it is isolated electrically and connected to the programming track output. However, it is important that the prog track wiring be in the same phase as the main track i.e. when the left rail is high on MAIN, it is also high on PROG. You may have to swap the wires to your prog track to make this work. If you drive onto a programming track that is "joined" and enter a programming command, the track will automatically switch to a programming track. If you use a compatible Throttle, you can then send the join command again and drive off the track onto the rest of your layout!

.. note:: In some split motor shield hardware configurations JOIN will not be able to work.  

Engine Decoder (CAB) Operation Commands
========================================


**The CAB throttle format**  is ``<t REGISTER CAB SPEED DIRECTION>``  

Breakdown for this example ``<t 1 03 20 1>`` is:

* ``<`` = Start delimiter of a DCC++ EX command. (A space after ``<`` is not required but acceptable)
* ``t`` = (lower case t) This command is for a Decoder installed in a engine or simply a "cab".
* ``1`` = deprecated. We no longer use this but need something here for compatibility with legacy systems. Enter any single digit.
* ``03`` = CAB: the short (1-127) or long (128-10293) address of the engine decoder  (this has to be already programmed in the decoder) See Programming Commands bellow.
* ``20`` = SPEED: throttle speed from 0-126, or -1 for emergency stop (resets SPEED to 0)
* ``1`` = DIRECTION: 1=forward, 0=reverse. Setting direction when speed=0 or speed=-1 only effects directionality of cab lighting for a stopped train
* ``>`` = I am the end of this command

.. code-block:: none

   RETURNS: "<T 1 20 1>" if the command was successful, meaning :
   "<" = Begin DCC++ EX command
   "T" = (upper case T) DCC++ EX Cab command was sent from DCC++ EX Command Station
   "1" = register 1 was changed
   "20" = set to speed 20
   "1" = forward direction
   "<" = End DCC++ EX command

**Forget Locos**

* ``<- [CAB]>`` - (Minus symbol as in "subtract") Forgets one or all locos. The "CAB" parameter is optional. Once you send a throttle command to any loco, throttle commands to that loco will continue to be sent to the track. If you remove the loco, or for testing purposes need to clear the loco from repeating messages to the track, you can use this command. Sending ``<- CAB>`` will forget/clear that loco. Sending ``<->`` will clear all the locos. This doesn't do anything destructive or erase any loco settings, it just clears the speed reminders from being sent to the track. As soon as a controller sends another throttle command, it will go back to repeating those commands.

.. code-block:: none

   RETURNS: NONE

Examples:

* ``<- 74>`` - Forgets loco at address 74
* ``<->`` - Forgets all locos

**Emergency Stop**

* ``<!>`` - Emergency Stop ALL TRAINS.  (But leaves power to the track turned on)

.. code-block:: none

       RETURNS: NONE

CAB FUNCTIONS
--------------

There are two formats for setting CAB functions, the DCC++ Classic legacy method (maintained for compatibility) and the new DCC++ EX method. Both methods are described here though new applications are encouraged to use the newer ``<F>`` command (capital F vs. small f).


* The ``<F>`` command turns engine decoder functions ON and OFF
* F0-F28 (F0 is sometimes called FL)
* F29-F68 (Support for the RCN-212 Functions)
* NOTE: setting requests are transmitted directly to mobile engine decoder   
* Current state of engine functions (as known by commands issued since power on) is stored by the CommandStation  
* All functions within a group get set all at once per NMRA DCC standards.
* Using the new F command, the command station knows about the previous
  settings in the same group and will not, for example, unset F2 because you change F1. If however, you have never set F2, then changing F1 WILL unset F2.     

**CAB Functions format** is ``<F CAB FUNC 1|0>``

To set functions **F0-F68** on=(1) or off=(0): ``<F CAB FUNC 0|1>``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* ``<`` = Begin DCC++ EX command
* ``F`` = (upper case F) This command is for a CAB function ie: Lights, horn, bell  
* ``CAB``  : the short (1-127) or long (128-10293) address of the engine decoder
* ``FUNC`` : the CAB function number (0-28) whose function is defined by your decoder
* ``0|1`` : a value of 0 to set the function OFF and 1 to set the function ON
* ``>`` = End DCC++ EX command

Examples:

*  ``<F 3 0 1>`` Turns the headlight ON for CAB (loco address) 3
*  ``<F 126 0 0>`` Turns the headlight OFF for CAB 126
*  ``<F 1330 1 1>`` Turns the horn ON for CAB 1330

**The Legacy CAB Functions format** is ``<f CAB BYTE1 [BYTE2]>``

To set functions **F0-F4** on=(1) or off=(0): ``<f CAB BYTE1 [BYTE2]>``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* ``<`` = Begin DCC++ EX command
* ``f`` = (lower case f) This command is for a CAB function ie: Lights, horn, bell  
* ``CAB`` :  the short (1-127) or long (128-10293) address of the engine decoder
* ``BYTE1`` :  128 + F1*1 + F2*2 + F3*4 + F4*8 + F0*16

  * ADD the ones you want **ON** together
  * Add 1 for F1 ON
  * Add 2 for F2 ON
  * Add 4 for F3 ON
  * Add 8 for F4 ON
  * Add 16 for F0 ON
  * 128 Alone Turns OFF **F0-F4**

* ``BYTE2`` :  omitted
* ``>`` = End DCC++ EX command

To make BYTE1 add the values of what you want ON together, the ones that you want OFF do not get added to the base value of 128.

* F0 (Light)=16, F1 (Bell)=1, F2 (Horn)=2, F3=4, F4=8
* All off = 128
* Light on 128 + 16 = 144
* Light and bell on 128 + 16 + 1 = 145
* Light and horn on 128 + 16 + 2 = 146
* Just horn 128 + 2 = 130
* If light is on (144), Then you turn on bell with light (145), Bell back off but light on (144)  


Breakdown for this example ``<f 3265 144>``

* ``<`` = Begin DCC++ EX command
* ``f`` = (lower case f) This command is for a CAB,s function ie: Lights, horn, bell
* ``3265`` = CAB: the short (1-127) or long (128-10293) address of the engine decoder
* ``144`` = Turn on headlight
* ``>`` = End DCC++ EX command  

To set functions **F5-F8** on=(1) or off=(0): **<f CAB BYTE1 [BYTE2]>**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* ``<`` = Begin DCC++ EX command
* ``f`` = (lower case f) This command is for a CAB,s function.
* ``BYTE1`` :  176 + F5*1 + F6*2 + F7*4 + F8*8

  * ADD 176 + the ones you want **ON** together
  * Add 1 for F5 ON
  * Add 2 for F6 ON
  * Add 4 for F7 ON
  * Add 8 for F8 ON
  * 176 Alone Turns OFF **F5-F8**

* ``BYTE2`` :  omitted
* ``>`` = End DCC++ EX command  

To set functions **F9-F12** on=(1) or off=(0): **<f CAB BYTE1 [BYTE2]>**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* ``<`` = Begin DCC++ EX command
* ``f`` = (lower case f) This command is for a CAB,s function.
* ``BYTE1:``  160 + F9*1 +F10*2 + F11*4 + F12*8

  * ADD 160 + the ones you want **ON** together
  * Add 1 for F9 ON
  * Add 2 for F10 ON
  * Add 4 for F11 ON
  * Add 8 for F12 ON
  * 160 Alone Turns OFF **F9-F12**

* ``BYTE2:``  omitted
* ``>`` = End DCC++ EX command  

To set functions **F13-F20** on=(1) or off=(0): **<f CAB BYTE1 [BYTE2]>**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* ``<`` = Begin DCC++ EX command
* ``f`` = (lower case f) This command is for a CAB,s function.
* ``BYTE1:`` 222 
* ``BYTE2:`` F13*1 + F14*2 + F15*4 + F16*8 + F17*16 + F18*32 + F19*64 + F20*128

  * ADD the ones you want **ON** together
  * Add 1 for F13 ON
  * Add 2 for F14 ON
  * Add 4 for F15 ON
  * Add 8 for F16 ON
  * Add 16 for F17 ON
  * Add 32 for F18 ON
  * Add 64 for F19 ON
  * Add 128 for F20 ON
  * 0 Alone Turns OFF **F13-F20**

* ``>`` = End DCC++ EX command  

To set functions **F21-F28** on=(1) or off=(0): **<f CAB BYTE1 [BYTE2]>**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* ``<`` = Begin DCC++ EX command
* ``f`` = (lower case f) This command is for a CAB function.
* ``BYTE1:`` 223
* ``BYTE2:`` F21*1 + F22*2 + F23*4 + F24*8 + F25*16 + F26*32 + F27*64 + F28*128

  * ADD the ones you want **ON** together
  * Add 1 for F21 ON
  * Add 2 for F22 ON
  * Add 4 for F23 ON
  * Add 8 for F24 ON
  * Add 16 for F25 ON
  * Add 32 for F26 ON
  * Add 64 for F27 ON
  * Add 128 for F28 ON
  * 0 Alone Turns OFF **F21-F28**

* ``>`` = End DCC++ EX command  

RETURNS: NONE
^^^^^^^^^^^^^^^


* CAB Functions do not have a Return
* CAB Functions do not get stored in the DCC++ EX CommandStation
* Each group does not effect the other groups. To turn on F0 and F22 you would need to send two separate commands to the DCC++ EX CommandStation. One for F0 on and another for F22 on. 

STATIONARY ACCESSORY DECODERS & TURNOUTS
------------------------------------------

DCC++ EX COMMAND STATION can keep track of the direction of any turnout that is controlled by a DCC stationary accessory decoder once its Defined (Set Up).  

All decoders that are not in an engine are accessory decoders including turnouts.

Any DCC Accessory Decoder based turnouts, as well as any other DCC accessories connected in this fashion, can always be operated using the DCC COMMAND STATION Accessory command:

Accessory Decoder Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two interchangeable commands for controlling Accessory Decoders, the Address/Subaddress method (aka "Dual-Coil" method) and linear addressing method. 
You can either specify an address and its subaddress (Addresses 0-511 with Subaddresses from 0-3) or the straight linear address (Addresses from 1-2044).

In the mapping used by DCC++EX, linear addresses range from linear address 1, which is address 1 subaddress 0, up to linear address 2040 which is address 510 subaddress 3.
Decoder address 511 (linear addresses 2041-2044) is reserved for use as a broadcast address and should not be used for decoders.
Decoder address 0 does not have a corresponding linear address.  This seems strange, but it is the mapping used by many, but not all, commercial manufacturers.
If your decoder does not respond on the expected linear address, try adding and subtracting 4 to see if it works.  Or use the address/subaddress versions of the commands.

Here is a spreadsheet in .XLSX format to help you: `Decoder Address Decoder Table <../downloads/documents.html#stationary-decoder-address-table-xlsx-spreadsheet>`_

NOTE: Both the following commands do the same thing. Pick the one that works for your needs.

Controlling an Accessory with ``<a LINEAR_ADDRESS ACTIVATE>``
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

* ``<`` = Begin DCC++ EX command
* ``a`` (lower case a) this command is for a Accessory Decoder
* ``LINEAR_ADDRESS:``  the linear address of the decoder controlling this turnout (1-2044)
* ``ACTIVATE:`` (0 or OFF) (for Deactivate, Straight, Closed) or (1 or ON) (for Activate, Turn, Thrown)
* ``>`` = End DCC++ EX command

Controlling an Accessory Decoder with ``<a ADDRESS SUBADDRESS ACTIVATE>``
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

* ``<`` = Begin DCC++ EX command
* ``a`` (lower case a) this command is for a Accessory Decoder
* ``ADDRESS:``  the primary address of the decoder controlling this turnout (0-511)
* ``SUBADDRESS:`` the subaddress of the decoder controlling this turnout (0-3)
* ``ACTIVATE:`` (0) (Deactivate, Straight, Closed) or (1) (Activate, Turn, Thrown)
* ``>`` = End DCC++ EX command


.. Note:: This general command simply sends the appropriate DCC instruction packet to the main tracks to operate connected accessories. It does not store or retain any information regarding the current status of that accessory.

Defining (Setting up) a Turnout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Turnout commands provide a more flexible and more functional way of operating turnouts.  It requires that the turnout be pre-defined through the ``<T ...>`` commands, described below.

Turnouts may be in either of two states:  Closed or Thrown.  The turnout commands below use the values ``1`` for ``Throw`` or ``Thrown`` and ``0`` for ``Close`` or ``Closed``.

* Command to define a DCC Accessory Turnout: ``<T ID ADDRESS SUBADDRESS>`` :

  * Creates a new turnout ``ID``, with specified ``ADDRESS`` and ``SUBADDRESS`` if turnout ``ID`` already exists, it is updated (overwritten) with the new specified ``ADDRESS`` and ``SUBADDRESS``
  * Example:  ``<T 23 5 0>``
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)
  * From Version 3.2.0, this command is deprecated and has been replaced by ``<T ID DCC ADDRESS SUBADDRESS>``.

* Command to define a DCC Accessory Decoder turnout: ``<T ID DCC ADDRESS SUBADDRESS>`` :

  * Create a new turnout ``ID`` which operates the DCC Accessory Decoder configured for the ``ADDRESS`` and ``SUBADDRESS``. 
    ``ADDRESS`` ranges from 0 to 511 and ``SUBADDRESS`` ranges from 0 to 3. 
  * Example: ``<T 23 DCC 5 0>``
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)
  * This command is available from Version 3.2.0
  
* Command to define a DCC Accessory Decoder turnout: ``<T ID DCC LINEARADDRESS>`` :

  * Create a new turnout ``ID`` which operates the DCC Accessory Decoder configured for the ``LINEARADDRESS``. 
    ``LINEARADDRESS`` ranges from 1 (address 1/subaddress 0) to 2044 (address 511/subaddress 3).
  * Example: ``<T 23 DCC 44>`` (corresponds to address 11 subaddress 3).
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)
  * This command is available from Version 3.2.0
  
* Command to define a Servo-based turnout: ``<T ID SERVO PIN THROWNPOSITION CLOSEDPOSITION PROFILE>`` :

  * Create a new turnout ``ID`` using the servo output pin ``PIN``.  The positions for thrown and closed states are ``THROWNPOSITION`` and ``CLOSEDPOSITION`` 
    respectively.  For an SG90 servo, positions in the range of 102-490 will give up to 180 degrees motion, but the range of 205-410 (corresponding to
    1.0-2.0 millisecond pulses) is recommended for the SG90.  
    The transition between states is defined by ``PROFILE``, as 0 (immediate), 1 (fast=0.5 sec), 2 (medium=1 sec), 3 (slow=2 sec) or 4 (bounce, for semaphore signals).
  * Example: ``<T 24 SERVO 100 410 205 2>``  defines a servo turnout on the first PCA9685 pin, moving at medium speed between positions 205 and 410.
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)
  * This command is available from Version 3.2.0.

* Command to define a VPIN-based turnout: ``<T ID VPIN PIN>`` :

  * Create a new turnout ``ID`` which operates the output defined by ``PIN``.  If ``PIN`` is in the range of Arduino digital output pins, then 
    throwing the turnout will cause the specified pin to be set to HIGH, and closing the turnout will set the pin to LOW.  If ``PIN`` is associated 
    with an external device, then the device will be operated accordingly.
  * Example: ``<T 25 VPIN 30>`` defines a turnout that operates Arduino digital output pin D30.  
  * Example: ``<T 26 VPIN 164>`` defines a turnout that operates the first pin on the first MCP23017 GPIO Extender (if present).
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)
  * This command is available from Version 3.2.0.
  
* Command to Delete a turnout ``<T ID>`` :

  * Deletes the definition of a turnout with this ``ID``.
  * Example: ``<T 25>`` deletes the previously defined turnout number 25.
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. ID does not exist)

* Command to List all defined turnouts: ``<T>`` :

  * Lists all defined turnouts.
  * Before Version 3.2.0: Returns: ``<H ID ADDRESS SUBADDRESS THROWN>`` for each defined DCC Accessory Turnout or ``<X>`` if no turnouts have beed defined or saved.  
  * After Version 3.2.0: Returns the parameters that would be used to create the turnout, with the ``THROWN`` state (1=thrown, 0=closed) appended.  For example, 
    a servo turnout definition will be listed as ``<H ID SERVO PIN THROWNPOSITION CLOSEDPOSITION PROFILE THROWN>`` and a DCC turnout
    will be listed as ``<H ID DCC ADDRESS SUBADDRESS THROWN>``, a VPIN turnout as ``<H ID VPIN PIN THROWN> and an LCN turnout as ``<H ID LCN THROWN>``.

* ``ID`` : The numeric ID (0-32767) of the turnout to control.  

  * (NOTE: You pick the ID. IDs are shared between Turnouts, Sensors and Outputs)

* ``ADDRESS`` :  the primary address of a DCC accessory decoder controlling a turnout (0-511)
* ``SUBADDRESS`` : the subaddress of a DCC accessory decoder controlling a turnout (0-3)
* ``PIN`` : the pin number of the output to be controlled by the turnout object.  For Arduino output pins, this is the same as the digital pin number.  For 
  servo outputs and I/O extenders, it is the pin number defined for the HAL device (if present), for example 100-115 for servos attached to the first PCA9685 Servo Controller module,
  116-131 for the second PCA9685 module, 164-179 for pins on the first MCP23017 GPIO Extender module, and 180-195 for thesecond MCP23017 module.
* ``THROWNPOSITION`` : the PWM value corresponding to the servo position for THROWN state, normally in the range 102 to 490.
* ``CLOSEDPOSITION`` : the PWM value corresponding to the servo position for CLOSED state, normally in the range 102 to 490.
* ``PROFILE`` : the profile for the transition between states.  0=Immediate, 1=Fast (0.5 sec), 2=Medium (1 sec), 3=Slow (2 sec), 3=Bounce (for semaphore signals).

Once all turnouts have been properly defined, Use the ``<E>`` command to store their definitions to EEPROM.
If you later make edits/additions/deletions to the turnout definitions, you must invoke the ``<E>`` command if you want those new definitions updated in the EEPROM.
You can also **ERASE everything; (turnouts, sensors, and outputs)** stored in the EEPROM by invoking the ``<e>`` (lower case e) command. **WARNING: (There is no Un-Delete)**  

   Example: You have a turnout on your main line going to warehouse industry. The turnout is controlled by an accessory decoder with a address of 123 and is wired to output 3. 
   You want it to have the ID of 10.
   You would send the following command to the DCC++ EX CommandStation:
   ``<T 10 DCC 123 3>``  

   * This Command means:  
   * ``<`` : Begin DCC++ EX command  
   * ``T`` : (Upper case T) Define a Turnout  
   * ``DCC`` : The turnout is DCC Accessory Decoder based
   * ``10`` : ID number I am setting to use this turnout  
   * ``123`` : The accessory decoders address  
   * ``3`` : The turnout is wired to output 3  
   * ``>`` : End DCC++ EX command
   * RETURNS: ``<O>``  Meaning Command Successful

 |    Next you would send the following command to the DCC++ EX CommandStation:
     ``<E>``

   * This Command means:  
   * ``<`` : Begin DCC++ EX command  
   * ``E`` : (Upper case E) Store (save) this definition to EEPROM  
   * ``>`` : End DCC++ EX command
   * RETURNS: ``<O>``  Meaning Command Successful  

If turnout definitions are stored in EEPROM, the turnout thrown/closed state is also written to EEPROM whenever the turnout is switched.  
Consequently, when the DCC++ EX CommandStation is restarted the turnout outputs may be set to their last known state (applicable for Servo and VPIN turnouts).
This is intended so that the servos don't perform a sweep on power-on whem their physical position does not match initial position in the CommandStation.


Controlling a Defined Turnout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* Sets turnout ID to either the "closed" (turned) or "thrown" (closed) position  
* The Turnout format is ``<T id throw>``  
* ``id`` : The numeric ID (0-32767) That you gave the turnout to control when you defined it. 
* ``throw`` : 0 or C (closed), or 1 or T (thrown)  
* 
  RETURNS: ``<H id throw>`` or ``<X>`` if turnout ID does not exist  

  ..

     Example Continued from above:
     To throw turnout 10 so an engine can go to the warehouse siding you would send the following command.
     ``<T 10 1>``  


     * This Command means:  
     * ``<`` : Begin DCC++ EX command  
     * ``T`` : (Upper case T) Throw a turnout.  
     * ``10`` : ID number of the defined turnout I want to control.  
     * ``1`` : Set turnout to Thrown (turned, on) position.  
     * 
       ``>`` : End DCC++ EX command
       DCC++ EX should return ``<H 10 1>``  Meaning Command was Successful

       NOTE: The ``<T>`` command by itself with no parameters will list all turnout definitions and their directions


SENSORS (Inputs)
=================

DCC++ EX CommandStation supports Sensor inputs that can be connected to any Arduino Pin not in use by this program, as well as pins on external I/O extenders
and other devices. 
Physical sensors can be of any type (infrared, magnetic, mechanical...).  They may be configured to pull-up or not.  
When configured for pull-up, the input is connected (within the CS) to 
+5V via a resistor.  This sort of input is suited to sensors that have two wires (a switch or relay contacts, or a device with an 'open collector' or 'open drain' output.
Some sensors may be sensitive to the pull-up resistor and not operate as expected - in this case you can turn off the pull-up.

The sensor is considered INACTIVE when at +5V potential, and ACTIVE when the pin is pulled down to 0V.

To ensure proper voltage levels, some part of the Sensor circuitry MUST be tied back to the same ground as used by the Arduino.  

The Sensor code utilizes debouncing logic to eliminate contact 'bounce' generated by mechanical switches on transitions. This avoids the need to create smoothing circuitry for each sensor. 
You may need to change the parameters in Sensor.cpp through trial and error for your specific sensors,
but the default parameters protect against contact bounces for up to 20 milliseconds, which should be adequate for almost all mechanical switches and all electronic sensors.

To have this sketch monitor one or more Arduino pins for sensor triggers, first define/edit/delete sensor definitions using the following variation of the ``<S>`` command:  


* ``<S ID PIN PULLUP>`` : Creates a new sensor ID, with specified PIN and PULLUP if sensor ID already exists, it is updated with specified PIN and PULLUP (You choose the number).  

  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)

* ``<S ID>`` : Deletes definition of sensor ID  

  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. ID does not exist)  

* ``<S>`` : Lists all defined sensors  

  * RETURNS: ``<Q ID PIN PULLUP>`` for each defined sensor or ``<X>`` if no sensors defined  

``ID`` : The numeric ID (0-32767) of the sensor
(You pick the ID & they are shared between Turnouts, Sensors and Outputs)

``PIN`` : the pin number of the output to be controlled by the turnout object.  For Arduino output pins, this is the same as the digital pin number.  For 
servo outputs and I/O extenders, it is the pin number defined for the HAL device (if present), for example 100-115 for servos attached to the first PCA9685 Servo Controller module,
116-131 for the second PCA9685 module, 164-179 for pins on the first MCP23017 GPIO Extender module, and 180-195 for thesecond MCP23017 module.

``PULLUP`` : 1 = Use internal pull-up resistor for PIN (ACTIVE=LOW), 0 = don't use internal pull-up resistor for PIN (ACTIVE=HIGH).

Once all sensors have been properly defined, use the ``<E>`` (upper case E) command to store their definitions to EEPROM.
If you later make edits/additions/deletions to the sensor definitions, you must invoke the ``<E>`` (upper case E) command if you want those new definitions updated in the EEPROM.
You can also clear **everything (turnouts, sensors, and outputs)** stored in the EEPROM by invoking the ``<e>`` (lower case e) command.
**(There is NO UN-Delete)**  

All sensors defined as per above are repeatedly and sequentially checked within the main loop of this sketch. If a Sensor Pin is 
found to have transitioned from one state to another, one of the following serial messages are generated:  


* ``<Q ID>`` - for transition of Sensor ID from INACTIVE state to ACTIVE state (i.e. the sensor is triggered)  
* ``<q ID>`` - for transition of Sensor ID from ACTIVE state to INACTIVE state (i.e. the sensor is no longer triggered)  

Depending on whether the physical sensor is acting as an "event-trigger" or a "detection-sensor," you may decide to ignore the ``<q ID>`` return and only react to ``<Q ID>`` triggers.

OUTPUTS (DIO Pins)
=====================

DCC++ EX CommandStation supports optional OUTPUT control of any unused Arduino Pins for custom purposes. Pins can be activated or de-activated. 
The default is to set ACTIVE pins HIGH and INACTIVE pins LOW. However, this default behavior can be inverted for any pin in which case ACTIVE=LOW and INACTIVE=HIGH.  

Definitions and state (ACTIVE/INACTIVE) for pins are retained in EEPROM and restored on power-up.
The default is to set each defined pin to active or inactive according to its restored state. 
However, the default behavior can be modified so that any pin can be forced to be either active or inactive upon power-up regardless of its previous state before power-down.  

To have DCC++ EX CommandStation utilize one or more Arduino pins as custom outputs, first define/edit/delete output definitions using the following variation of the ``<Z>`` command:  


* ``<Z ID PIN IFLAG>`` : Creates a new output ID, with specified PIN and IFLAG values.  

  * if output ID already exists, it is updated with specificed PIN and IFLAG.  
  * Note: output state will be immediately set to ACTIVE/INACTIVE and pin will be set to HIGH/LOW according to IFLAG value specifcied (see below).  
  * RETURNS: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory).  

* ``<Z ID>`` : Deletes definition of output ID  

  * RETURNS: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. ID does not exist)  

* ``<Z>`` : Lists all defined output pins

  * RETURNS: ``<Y ID PIN IFLAG STATE>`` for each defined output pin or ``<X>`` if no output pins defined.

``ID`` : The numeric ID (0-32767) of the output
(You pick the ID & they are shared between Turnouts, Sensors and Outputs)

``PIN`` : the pin number of the output to be controlled by the output object.  For Arduino output pins, this is the same as the digital pin number.  For 
servo outputs and I/O extenders, it is the pin number defined for the HAL device (if present), for example 100-115 for servos attached to the first PCA9685 Servo Controller module,
116-131 for the second PCA9685 module, 164-179 for pins on the first MCP23017 GPIO Extender module, and 180-195 for the second MCP23017 module.

``STATE`` : The state of the output (0=INACTIVE / 1=ACTIVE)

``IFLAG`` : Defines the operational behavior of the output based on bits 0, 1, and 2 as follows:  

.. code-block::

   IFLAG, bit 0: 0 = forward operation (ACTIVE=HIGH / INACTIVE=LOW)
                 1 = inverted operation (ACTIVE=LOW / INACTIVE=HIGH)

   IFLAG, bit 1: 0 = state of pin restored on power-up to either ACTIVE or INACTIVE 
                     depending on state before power-down. 
                 1 = state of pin set on power-up, or when first created,
                     to either ACTIVE of INACTIVE depending on IFLAG, bit 2

   IFLAG, bit 2: 0 = state of pin set to INACTIVE upon power-up or when first created
                 1 = state of pin set to ACTIVE upon power-up or when first created 

Once all outputs have been properly defined, use the ``<E>`` Upper Case "E" command to store their definitions to EEPROM.
If you later make edits/additions/deletions to the output definitions, you must invoke the ``<E>`` command if you want those new definitions updated in the EEPROM.
You can also **ERASE everything (turnouts, sensors, and outputs)** stored in the EEPROM by invoking the ``<e>`` (lower case e) command.
**(There is no Un-Delete)**  

To change the state of outputs that have been defined use:  


* ``<Z ID STATE>`` : Sets output ID to either ACTIVE or INACTIVE state  
* RETURNS: ``<Y ID STATE>`` , or ``<X>`` if output ID does not exist  

  * ``ID`` : The numeric ID (0-32767) of the defined output to control  
  * ``STATE`` : The state of the output (0=INACTIVE / 1=ACTIVE)  

When controlled as such, the Arduino updates and stores the direction of each output in EEPROM so that it is retained even without power. 
A list of the current states of each output in the form ``<Y ID STATE>`` is generated by DCC++ EX CommandStation whenever the ``<s>`` 
status command is invoked. This provides an efficient way of initializing the state of any outputs being monitored or controlled by a separate interface or GUI program.  

Engine Decoder Programming Commands
======================================

PROGRAMMING-MAIN TRACK
-----------------------

WRITE CV BYTE TO ENGINE DECODER ON MAIN TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes, without any verification, a Configuration Variable BYTE to the decoder of an engine on the main operations track. 


* Write CV BYTE Format is: ``<w CAB CV VALUE>``  
* ``CAB`` : The short (1-127) or long (128-10293) address of the engine decoder  
* ``CV`` : The number of the Configuration Variable memory location in the decoder to write to (1-1024)  
* ``VALUE`` : The value to be written to the Configuration Variable memory location (0-255)  
* RETURNS: NONE

WRITE CV BIT TO ENGINE DECODER ON MAIN TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes, without any verification, a single bit within a Configuration Variable BIT to the decoder of an engine on the main operations track. 


* Write CV BIT Format is: ``<b CAB CV BIT VALUE>``
* ``CAB`` :  the short (1-127) or long (128-10293) address of the engine decoder  
* ``CV`` : the number of the Configuration Variable memory location in the decoder to write to (1-1024)  
* ``BIT`` : the bit number of the Configurarion Variable register to write (0-7)  
* ``VALUE`` : the value of the bit to be written (0-1)  

  * RETURNS: NONE

PROGRAMMING-PROGRAMMING TRACK
-------------------------------

.. NOTE:: By design, for safety reasons, the NMRA specification prevents locos from responding to throttle or function commands while on the service track. A loco WILL NOT MOVE on the service track! Don't let the little "jumps" you may see when you are programming a CV confuse you. The loco pulses the motor to give a jump in current that we read as an "ACK" (acnowledgment), that causes some locos to stutter ahead slightly every time you read or write a CV.

WRITE LOCO ADDRESS TO ENGINE DECODER ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes, and then verifies, the address to decoder of an engine on the programming track. This involves clearing any consist and automatically setting a long or short address. This is an easy way to put a loco in a known state to test for issues like not responding to throttle commands when it is on the main track.

Write loco address Format is: ``<W ADDRESS>``
ADDRESS: The loco address to be written (1-10239).


WRITE CV BYTE TO ENGINE DECODER ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes, and then verifies, a Configuration Variable BYTE to the decoder of an engine on the programming track  


* Write CV BYTE Format is: ``<W CV VALUE CALLBACKNUM CALLBACKSUB>``
* ``CV`` : The number of the Configuration Variable memory location in the decoder to write to (1-1024  ).  
* ``VALUE`` : The value to be written to the Configuration Variable memory location (0-255).  
* ``CALLBACKNUM`` : An arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs that call this function.  
* ``CALLBACKSUB`` : a second arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs (e.g. DCC++ EX Interface) that call this function.  

  * ``RETURNS:`` ``<r CALLBACKNUM|CALLBACKSUB|CV Value>``  
  * ``CV VALUE:`` Is a number from 0-255 as read from the requested CV, or -1 if verification read fails.  

WRITE CV BIT TO ENGINE DECODER ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes, and then verifies, a Configuration Variable BIT to the decoder of an engine on the programming track  


* Write CV BIT Format is: ``<B CV BIT VALUE CALLBACKNUM CALLBACKSUB>``  
* ``CV`` : The number of the Configuration Variable memory location in the decoder to write to (1-1024).  
* ``BIT`` : The bit number of the Configuration Variable memory location to write (0-7).  
* ``VALUE`` : The value of the bit to be written (0-1).  
* ``CALLBACKNUM`` : An arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs that call this function.  
* ``CALLBACKSUB`` : A second arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs (e.g. DCC++ EX Interface) that call this function.  

  * ``RETURNS:`` ``<r CALLBACKNUM|CALLBACKSUB|CV BIT VALUE>``  
  * ``CV VALUE`` is a number from 0-1 as read from the requested CV bit, or -1 if verification read fails.  

READ CONFIGURATION VARIABLE BYTE FROM ENGINE DECODER ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If specified with parameters, reads a Configuration Variable from the decoder of an engine on the programming track. If no parameters are specified, it returns the Address of the loco on the programing track.


Read CV BYTE Format is: ``<R CV CALLBACKNUM CALLBACKSUB>``  

* ``CV`` : The number of the Configuration Variable memory location in the decoder to read from (1-1024).  
* ``CALLBACKNUM`` : An arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs that call this function.  
* ``CALLBACKSUB`` : A second arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs (e.g. DCC++ EX Interface) that call this function. 

  * ``RETURNS:`` ``<r CALLBACKNUM|CALLBACKSUB|CV VALUE>``  
  * ``CV VALUE`` is a number from 0-255 as read from the requested CV, or -1 if read could not be verified.

Read Engine address format is simply: ``<R>``

* ``RETURNS:`` ``<r ADDRESS>`` when successul and ``<r -1>`` if it is not.

**IMPORTANT: If the loco is on a consist, the address returned will be the consist address**

.. Note:: When combined with the ``<D ACK ON>`` Command, the <R> Command (with or without parameters) can be used for diagnostics, for example when you get a "-1" response. (See `Diagnosing Issues <https://github.com/DCC-EX/CommandStation-EX/wiki/Diagnosing-Issues>`_\ ** for more help)

VERIFY CONFIGURATION VARIABLE BYTE FROM ENGINE DECODER ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is designed to offer faster verification of the value held in a CV and can be used instead of the ``<R>`` commands. Instead of reading a byte value or looking at each bit, it compares the byte to an expected value. It will attempt to verify the value first, and if it is successful, will return the value as if it was simply "read". If the verify fails, it will perform a read byte command (see above) and return the value read.


* Verify CV BYTE Format is: ``<V CV BYTEVALUE>``
* ``CV`` : The number of the Configuration Variable memory location in the decoder to read from (1-1024).
* ``BYTEVALUE`` : The value of they byte expected to be in the CV
* ``RETURNS:`` ``<v CV BYTEVALUE>`` 
* ``BYTEVALUE:`` reports the value of the byte if the verify was successful. A value of -1 indicates a fault condition such as no loco, no power, no ACK etc., not a bad validation 

VERIFY CONFIGURATION VARIABLE BIT FROM ENGINE DECODER ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is designed to offer faster verification of the value held in a CV and can be used instead of the ``<R>`` commands. Instead of reading a bit value, it compares the bit to an expected value. It will attempt to verify the value first, an if it is successful, will return the value as if it was simply "read". If the verify fails, it will perform a read bit command (see above) and return the value read.


* Verify CV BIT Format is: ``<V CV BIT BITVALUE>``
* ``CV`` : The number of the Configuration Variable memory location in the decoder to read from (1-1024).
* ``BIT`` : The bit position of the bit in the CV byte being validated (0-7)
* ``BITVALUE`` : 0 or 1 indicating the expected value
* ``RETURNS:`` ``<v CV BIT BITVALUE>`` A return value of -1 indicates a fault condition such as no loco, no power, no ACK etc., not a bad validation 
* ``BIT:`` Reports the bit in the CV byte that was verified
* ``BITVALUE:`` reports the value of the individual bit in the CV byte being verified if the verify was successful. A value of -1 indicates a fault condition such as no loco, no power, no ACK etc., not a bad validation. 

DIAGNOSTICS
============

"D" Commands
-------------

.. Note:: 1 and 0 and ON and OFF can be used interchangeably in DCC++ EX

* ``<D CABS>`` Shows cab numbers and speed in reminder table.
* ``<D RAM>`` Shows remaining RAM.
* ``<D ACK 1|0>`` Enables ACK diagnostics
* ``<D CMD 1|0>`` Enables Command Parser diagnostics
* ``<D WIFI 1|0>`` Enables Wifi diagnostics
* ``<D WIT 0|1>`` Enables Withrottle diagnostics
* ``<D TEST|NORMAL>`` DCC Signal Diagnostics (See `Diagnosing Issues <https://github.com/DCC-EX/CommandStation-EX/wiki/Diagnosing-Issues>`_\ ** for more help)
* ``<D SPEED28|SPEED128`` Switch between 28 and 128 speed steps
* ``<D SERVO pin pos profile>`` Set servo on VPIN ``pin`` to position ``pos``, moving according to profile ``profile``.  
  ``pos`` is normally in the range of about 102 to 490 for SG90 servos; values outside of this range may drive the servo outside of its normal range.
  ``profile`` (optional, default=0) may be 0 (Immediate), 1 (Fast), 2 (Medium), 3 (Slow) or 4 (Bounce).  This command is intended to help users to identify appropriate 
  position values for configuring the servo in-situ.  This command is available from Version 3.2.0.
* ``<D ANOUT pin value param2>`` Write the specified value and param2 to the analogue output VPIN pin.  This is an alias for the <D SERVO...> command.  
  The significance of param2 depends on the device type associated with the VPIN.  The command is ignored if the pin is not configured or does not 
  support analogue write operations.  This command is available from Version 3.2.0.
* ``<D ANIN pin>`` Read the analogue value of the specified pin and display it.  The value will be zero if the pin is not configured or does not support
  analogue read operations.  This command is available from Version 3.2.0.
* ``<D HAL SHOW>`` List the configured I/O drivers in the Hardware Abstraction Layer (HAL).  This command is available from Version 3.2.0.

example: <D ACK ON>

DECODER TEST
-------------

These following commands are detailed above but are worth repeating here. The ``<R>`` command will attempt to read the decoder on the service (programming) track and attempt to read its long or short address and display it in the serial monitor. To do this, it also resets any consist. So if your loco isn't moving on the MAIN track, this command is a good way to make sure a consist is enabled as well as to make sure you have the correct address. Put together with the ``<D ACK ON>`` command, this shows a log giving detailed information about track current and ACK detection timings that you can provide to our support team to find out why a particular decoder may not be behaving correctly.

``<R>`` - Reads the address of the decoder and reports the long or short value to the serial monitor

``<D ACK ON><R>`` - When sent together as shown or one right after the other, this combined command shows the detailed results of what happened when trying to read the Address CV(s) and any response back from the decoder.-



SEND PACKET TO THE TRACK
--------------------------

.. Warning:: THIS IS FOR DEBUGGING AND TESTING PURPOSES ONLY.  DO NOT USE UNLESS YOU KNOW HOW TO CONSTRUCT NMRA DCC PACKETS - YOU CAN INADVERTENTLY RE-PROGRAM YOUR ENGINE DECODER

| ``<M>`` Command writes a packet the MAIN track
| ``<P>`` Command writes a packet to the PROG track

Writes a DCC packet of two, three, four, or five hexidecimal bytes to a register driving the selected track

  **FORMAT:** ``<M|P REGISTER BYTE1 BYTE2 [BYTE3] [BYTE4] [BYTE5]>``

.. code-block::

   ``REGISTER:`` an internal register number, from 0 through MAX_MAIN_REGISTERS (inclusive), to write (if REGISTER=0) or write and store (if REGISTER>0) the packet
   ``BYTE1:``  first hexadecimal byte in the packet
   ``BYTE2:``  second hexadecimal byte in the packet
   ``BYTE3:``  optional third hexadecimal byte in the packet
   ``BYTE4:``  optional fourth hexadecimal byte in the packet
   ``BYTE5:``  optional fifth hexadecimal byte in the packet

   returns: NONE

WiFi "AT Commands
==================

``<+COMMAND>`` Plus sign followed by a command. Sends AT commands to the WiFi board (ESP8266, ESP32, etc.) There is not space betwen the "+" and the command.

Users familiar with the AT Command Set of WiFi board may enter commands directly into the serial monitor in real-time or as setup commands in the :doc:`mySetup.h file <../../advanced-setup/startup-config>`. This allows users to override the default WiFi connect sequence or to send any command to change a WiFi device setting.

``<+X>`` A special command to force the "connected" flag to on inside the CS so that our loop will start seeing network traffic. If your code creates a connection outside of our normal WiFi code, this provides a way for you to notify the CS that it needs to process commands on a connection you created.

Examples:

  <+GMR> - Sends the "AT+GMR" command that prints version information from the WiFi device.
  <+CIFSR> - Gets the local IP Address.

For more detail follow these links:

:doc:`DCC-EX WiFi Configuration <../../advanced-setup/wifi-config>`

`Expressif AT Command Set PDF File (Exressif makes the ESP8266) <https://www.espressif.com/sites/default/files/documentation/4a-esp8266_at_instruction_set_en.pdf>`_


User Commands
==============

 ``<U>`` Is reserved for user commands.

 This is a detailed reference. For a summary version, please see :doc:`Command Summary <command-summary>`
