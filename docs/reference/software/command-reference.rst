.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-REF-LOGO|

************************
DCC-EX Command Reference
************************

|engineer|

.. sidebar:: 

  .. contents:: On this page
    :depth: 1
    :local:

This is a detailed reference. For a summary version, please see :doc:`Command Summary <command-summary>`

`EX-CommandStation <https://github.com/DCC-EX/CommandStation-EX>`_ Provides an Application Programming Interface (API) that other applications use to send simple text commands that can operate your Command Station. Several "front end" controllers are available or you can easily create your own. Here are some examples:

* :doc:`EX-WebThrottle </throttles/software/ex-webthrottle>` - Our |EX-WT| browser based throttle using your USB cable. See it and run from the web. You can also install it by clicking a button from within |EX-WT| itself!

* `Engine Driver <https://enginedriver.mstevetodd.com/>`_ - Cellphone App WiFi Throttle  

* `JMRI (Java Model Railroad Interface) <http://www.jmri.org/>`_

* A serial console, like the Arduino Serial Monitor or PuTTY

* `Gregg Berman's DCC++ Controller Software <https://github.com/DccPlusPlus/Controller>`_

This reference explains the available command structure, and for commands that provide them, their responses. If you are testing your Command Station or writing your own control program, make sure you have the latest release of the `EX-CommandStation Firmware <https://github.com/DCC-EX/CommandStation-EX>`_.

You can view and edit this code in the `Arduino IDE <https://www.arduino.cc/en/Main/Software>`_ or in `PlatformIO <https://github.com/DCC-EX/CommandStation-EX/blob/master/CONTRIBUTING.md>`_ Software from `GitHub <https://github.com/DCC-EX>`_. If you are new to we suggest you start with the `DCC-EX Webpage <https://dcc-ex.com>`_.  

Conventions used on this page
=============================

- "<" and ">" - All DCC-EX API commands are surrounded by these characters to indicate the beginning and end, these must always be included
- First letter or number - These are called OPCODES, are case sensitive, and must be specified as directed, eg. 1, c, or -
- CAPITALISED words - These are also called OPCODES, are case sensitive, and must be specified as directed, eg. MAIN
- lowercase words - These are parameters that must be provided or are returned, with multiple parameters separated by a space, eg. cabid
- Square brackets [] - Parameters within square brackets [] are optional and may be ommitted, and if specifying these parameters, do not include the square brackets themselves
- \| - Use of the \| character means you need to provide one of the provided options only, for example ``<0|1 MAIN|PROG|JOIN>`` becomes either ``<0 MAIN>`` or ``<1 MAIN>``

Track Power Commands
=====================

The following commands provide control over power to the MAIN and PROG tracks (voltage), as well as monitoring the current used.

``<0|1 MAIN|PROG|JOIN>`` - Turns power on and off to the MAIN and PROG tracks independently from each other and allows joining the MAIN and PROG tracks together

  .. code-block::

      RETURNS: <pX [MAIN|PROG|JOIN]> where "X" is 0 for off and 1 for on. MAIN, PROG and JOIN are returned when you invoke commands on just one track.

Examples:

``<1>`` - Turn power to all tracks **on**. RETURNS: <p1>

``<0>`` - Turn power to all tracks **off**. RETURNS: <p0>

``<1 MAIN>`` - Turns on power just to the MAIN track. RETURNS: <p1 MAIN>

``<0 PROG>`` - Turns off power just to the PROG track. RETURNS: <p0 PROG>

``<1 JOIN>`` - Joins both tracks together to be both MAIN (ops) tracks. Any other power command turns it off. RETURNS: <p1 JOIN>


.. note:: The use of the JOIN function ensures that the DCC signal for the MAIN track is also sent to the PROG track. This allows the prog track to act as a siding (or similar) in the main layout even though it is isolated electrically and connected to the programming track output. However, it is important that the prog track wiring be in the same phase as the main track i.e. when the left rail is high on MAIN, it is also high on PROG. You may have to swap the wires to your prog track to make this work. If you drive onto a programming track that is "joined" and enter a programming command, the track will automatically switch to a programming track. If you use a compatible Throttle, you can then send the join command again and drive off the track onto the rest of your layout!

.. note:: In some split motor shield hardware configurations JOIN will not be able to work.

``<c>`` Lower case c: Displays the instantaneous current on the MAIN Track

  .. code-block::

      RETURNS: <c "CurrentMAIN" current C "Milli" "0" max_ma "1" trip_ma>
      

  Example <c CurrentMAIN 120 C Milli 0 1996 1 1800>

  The above shows a MAIN track current of 120mA, 1.996A max, 1.8A trip current

  * ``c`` - the current response indicator
  * ``CurrentMAIN`` - Static text for software like JMRI
  *  ``current`` - Current in MilliAmps
  *  ``C`` - Designator to signify this is a current meter (V would be for voltage)
  *  ``Milli`` - Unit of measure for external software with a meter like JMRI (Milli, Kilo, etc.)
  *  ``0`` - numbered parameter for external software (1,2,3, etc.)
  *  ``max_ma`` - The maximum current handling of the motor controller in MilliAmps
  *  ``1`` - number parameter for external software (we use 2 parameters here, 0 and 1)
  *  ``trip_ma`` - The overcurrent limit that will trip the software circuit breaker in mA
    

Engine Decoder (CAB) Operation Commands
========================================


**The CAB throttle format**  is ``<t register cab speed direction>``  

Breakdown for this example ``<t 1 03 20 1>`` is:

* ``t`` = (lower case t) This command is for a Decoder installed in a engine or simply a "cab".
* ``1`` = deprecated. We no longer use this but need something here for compatibility with legacy systems. Enter any single digit.
* ``03`` = CAB: the short (1-127) or long (128-10293) address of the engine decoder  (this has to be already programmed in the decoder) See Programming Commands bellow.
* ``20`` = SPEED: throttle speed from 0-126, or -1 for emergency stop (resets SPEED to 0)
* ``1`` = DIRECTION: 1=forward, 0=reverse. Setting direction when speed=0 or speed=-1 only effects directionality of cab lighting for a stopped train

.. code-block::

   RETURNS: "<T 1 20 1>" if the command was successful, meaning :
   "T" = (upper case T) DCC++ EX Cab command was sent from the Command Station
   "1" = register 1 was changed
   "20" = set to speed 20
   "1" = forward direction

**Show number of supported cabs**

* ``<#>`` - Will display the number of available cab slots. This will typically be ``<# 20>``, ``<# 30>``, or ``<# 50>`` depending on how much memory your |EX-CS| has available. This is a design limit based on the memory limitations of the particular hardware and a compromise with other features that require memory such as WiFI. If you need more slots and are comfortable with code changes you can adjust this by changing ``MAX_LOCOS`` in "DCC.h", knowing that each new slot will take approximately 8 bytes of memory. The ``<D RAM>`` command will display the amount of free memory. If you fill the available slots, the “Forget Locos” command (``<- [CAB]>``) will free up unused locos. Currently there is no automatic purging of unused locos.

**Forget Locos**

* ``<- [cab]>`` - (Minus symbol as in "subtract") Forgets one or all locos. The "cab" parameter is optional. Once you send a throttle command to any loco, throttle commands to that loco will continue to be sent to the track. If you remove the loco, or for testing purposes need to clear the loco from repeating messages to the track, you can use this command. Sending ``<- cab>`` will forget/clear that loco. Sending ``<->`` will clear all the locos. This doesn't do anything destructive or erase any loco settings, it just clears the speed reminders from being sent to the track. As soon as a controller sends another throttle command, it will go back to repeating those commands.

.. code-block::

   RETURNS: NONE

Examples:

* ``<- 74>`` - Forgets loco at address 74
* ``<->`` - Forgets all locos

**Emergency Stop**

* ``<!>`` - Emergency Stop ALL TRAINS.  (But leaves power to the track turned on)

.. code-block::

       RETURNS: NONE

CAB FUNCTIONS
-------------

There are two formats for setting CAB functions, the DCC++ Classic legacy method (maintained for compatibility) and the new DCC-EX method. Both methods are described here though new applications are encouraged to use the newer ``<F>`` command (capital F vs. small f).


* The ``<F>`` command turns engine decoder functions ON and OFF
* F0-F28 (F0 is sometimes called FL)
* F29-F68 (Support for the RCN-212 Functions)
* NOTE: setting requests are transmitted directly to mobile engine decoder   
* Current state of engine functions (as known by commands issued since power on) is stored by the CommandStation  
* All functions within a group get set all at once per NMRA DCC standards.
* Using the new F command, the command station knows about the previous
  settings in the same group and will not, for example, unset F2 because you change F1. If, however, you have never set F2, then changing F1 WILL unset F2.     

**CAB Functions format** is ``<F cab func 1|0>``

To set functions **F0-F68** on=(1) or off=(0): ``<F cab func 0|1>``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``F`` = (upper case F) This command is for a CAB function i.e.: Lights, horn, bell  
* ``cab``  : the short (1-127) or long (128-10293) address of the engine decoder
* ``func`` : the CAB function number (0-28) whose function is defined by your decoder
* ``0|1`` : a value of 0 to set the function OFF and 1 to set the function ON

Examples:

*  ``<F 3 0 1>`` Turns the headlight ON for CAB (loco address) 3
*  ``<F 126 0 0>`` Turns the headlight OFF for CAB 126
*  ``<F 1330 1 1>`` Turns the horn ON for CAB 1330

**The Legacy CAB Functions format** is ``<f cab byte1 [byte2]>``

To set functions **F0-F4** on=(1) or off=(0): ``<f cab byte1 [byte2]>``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``f`` = (lower case f) This command is for a CAB function i.e.: Lights, horn, bell  
* ``cab`` :  the short (1-127) or long (128-10293) address of the engine decoder
* ``byte1`` :  128 + F1*1 + F2*2 + F3*4 + F4*8 + F0*16

  * ADD the ones you want **ON** together
  * Add 1 for F1 ON
  * Add 2 for F2 ON
  * Add 4 for F3 ON
  * Add 8 for F4 ON
  * Add 16 for F0 ON
  * 128 Alone Turns OFF **F0-F4**

* ``byte2`` :  omitted

To make "byte1" add the values of what you want ON together, the ones that you want OFF do not get added to the base value of 128.

* F0 (Light)=16, F1 (Bell)=1, F2 (Horn)=2, F3=4, F4=8
* All off = 128
* Light on 128 + 16 = 144
* Light and bell on 128 + 16 + 1 = 145
* Light and horn on 128 + 16 + 2 = 146
* Just horn 128 + 2 = 130
* If light is on (144), Then you turn on bell with light (145), Bell back off but light on (144)  


Breakdown for this example ``<f 3265 144>``

* ``f`` = (lower case f) This command is for a CAB,s function i.e.: Lights, horn, bell
* ``3265`` = CAB: the short (1-127) or long (128-10293) address of the engine decoder
* ``144`` = Turn on headlight

To set functions **F5-F8** on=(1) or off=(0): **<f cab byte1 [byte2]>**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``f`` = (lower case f) This command is for a CAB,s function.
* ``byte1`` :  176 + F5*1 + F6*2 + F7*4 + F8*8

  * ADD 176 + the ones you want **ON** together
  * Add 1 for F5 ON
  * Add 2 for F6 ON
  * Add 4 for F7 ON
  * Add 8 for F8 ON
  * 176 Alone Turns OFF **F5-F8**

* ``byte2`` :  omitted

To set functions **F9-F12** on=(1) or off=(0): **<f cab byte1 [byte2]>**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``f`` = (lower case f) This command is for a CAB,s function.
* ``byte1:``  160 + F9*1 +F10*2 + F11*4 + F12*8

  * ADD 160 + the ones you want **ON** together
  * Add 1 for F9 ON
  * Add 2 for F10 ON
  * Add 4 for F11 ON
  * Add 8 for F12 ON
  * 160 Alone Turns OFF **F9-F12**

* ``byte2:``  omitted

To set functions **F13-F20** on=(1) or off=(0): **<f cab byte1 [byte2]>**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``f`` = (lower case f) This command is for a CAB,s function.
* ``byte1:`` 222 
* ``byte2:`` F13*1 + F14*2 + F15*4 + F16*8 + F17*16 + F18*32 + F19*64 + F20*128

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

To set functions **F21-F28** on=(1) or off=(0): **<f cab byte1 [byte2]>**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``f`` = (lower case f) This command is for a CAB function.
* ``byte1:`` 223
* ``byte2:`` F21*1 + F22*2 + F23*4 + F24*8 + F25*16 + F26*32 + F27*64 + F28*128

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

**RETURNS:** <l cab slot speed/dir func>

Where:

* ``cab`` is the loco DCC address/CAB ID.
* ``slot`` is the slot assignment for the CAB.
* ``speed/dir`` is the 8 bit speed byte:

  * Bit 7 provides the direction (1 = Fwd, 0 = Rev).
  * Bits 0 to 6 provide the speed (0 - 128).

* ``func`` is the bit pattern for the functions that are set.

.. note:: 

  Strictly speaking, this is not a response, it's a broadcast of status and can arise when any throttle is changed by someone else. Thus there is no guarantee that you will get the message if your throttle command changed nothing, nor that the next message you receive will be from your most recent throttle command.

Other notes:

* CAB Functions do not get stored in the EX-CommandStation
* Each group does not effect the other groups. To turn on F0 and F22 you would need to send two separate commands to the |EX-CS|. One for F0 on and another for F22 on. 

Stationary Accessory Decoder & Turnout Commands
-----------------------------------------------

|EX-CS| can keep track of the direction of any turnout that is controlled by a DCC stationary accessory decoder once its Defined (Set Up).  

All decoders that are not in an engine are accessory decoders including turnouts.

Any DCC Accessory Decoder based turnouts, as well as any other DCC accessories connected in this fashion, can always be operated using the DCC COMMAND STATION Accessory command:

Accessory Decoder Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two interchangeable commands for controlling Accessory Decoders, the Address/Subaddress method (aka "Dual-Coil" method) and linear addressing method. 
You can either specify an address and its subaddress (Addresses 0-511 with Subaddresses from 0-3) or the straight linear address (Addresses from 1-2044).

In the mapping used by |EX-CS|, linear addresses range from linear address 1, which is address 1 subaddress 0, up to linear address 2040 which is address 510 subaddress 3.
Decoder address 511 (linear addresses 2041-2044) is reserved for use as a broadcast address and should not be used for decoders.
Decoder address 0 does not have a corresponding linear address.  This seems strange, but it is the mapping used by many, but not all, commercial manufacturers.
If your decoder does not respond on the expected linear address, try adding and subtracting 4 to see if it works.  Or use the address/subaddress versions of the commands.

Here is a spreadsheet in .XLSX format to help you: :ref:`Decoder Address Decoder Table <reference/downloads/documents:Stationary Decoder Address Table (xlsx Spreadsheet)>`

NOTE: Both the following commands do the same thing. Pick the one that works for your needs.

Controlling an Accessory with ``<a linear_address activate>``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``a`` (lower case a) this command is for a Accessory Decoder
* ``linear_address`` is the linear address of the decoder controlling this turnout (1-2044)
* ``activate`` is either (0 or OFF) (for Deactivate, Straight, Closed) or (1 or ON) (for Activate, Turn, Thrown)

Controlling an Accessory Decoder with ``<a address subaddress activate>``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``a`` (lower case a) this command is for a Accessory Decoder
* ``address`` is the primary address of the decoder controlling this turnout (0-511)
* ``subaddress`` is the subaddress of the decoder controlling this turnout (0-3)
* ``activate`` is either (0) (Deactivate, Straight, Closed) or (1) (Activate, Turn, Thrown)

.. Note:: This general command simply sends the appropriate DCC instruction packet to the main tracks to operate connected accessories. It does not store or retain any information regarding the current status of that accessory.

Defining (Setting up) a Turnout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Turnout commands provide a more flexible and more functional way of operating turnouts.  It requires that the turnout be pre-defined through the ``<T ...>`` commands, described below.

Turnouts may be in either of two states:  Closed or Thrown.  The turnout commands below use the values ``1`` for ``Throw`` or ``Thrown`` and ``0`` for ``Close`` or ``Closed``.

* Command to define a DCC Accessory Decoder turnout: ``<T id DCC address subaddress>`` :

  * Create a new turnout ``id`` which operates the DCC Accessory Decoder configured for the ``address`` and ``subaddress``. 
    ``address`` ranges from 0 to 511 and ``subaddress`` ranges from 0 to 3. 
  * Example: ``<T 23 DCC 5 0>``
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)
  
* Command to define a DCC Accessory Decoder turnout: ``<T id DCC linear_address>`` :

  * Create a new turnout ``id`` which operates the DCC Accessory Decoder configured for the ``linear_address``. 
    ``linear_address`` ranges from 1 (address 1/subaddress 0) to 2044 (address 511/subaddress 3).
  * Example: ``<T 23 DCC 44>`` (corresponds to address 11 subaddress 3).
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)
  
* Command to define a Servo-based turnout: ``<T id SERVO vpin thrown_position closed_position profile>`` :

  * Create a new turnout ``id`` using the servo output pin ``vpin``.  The positions for thrown and closed states are ``thrown_position`` and ``closed_position`` 
    respectively.  For an SG90 servo, positions in the range of 102-490 will give up to 180 degrees motion, but the range of 205-410 (corresponding to
    1.0-2.0 millisecond pulses) is recommended for the SG90.  
    The transition between states is defined by ``profile``, as 0 (immediate), 1 (fast=0.5 sec), 2 (medium=1 sec), 3 (slow=2 sec) or 4 (bounce, for semaphore signals).
  * Example: ``<T 24 SERVO 100 410 205 2>``  defines a servo turnout on the first PCA9685 pin, moving at medium speed between positions 205 and 410.
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)

* Command to define a VPIN-based turnout: ``<T id VPIN vpin>`` :

  * Create a new turnout ``id`` which operates the output defined by ``vpin``.  If ``vpin`` is in the range of Arduino digital output pins, then 
    throwing the turnout will cause the specified pin to be set to HIGH, and closing the turnout will set the pin to LOW.  If ``vpin`` is associated 
    with an external device, then the device will be operated accordingly.
  * Example: ``<T 25 VPIN 30>`` defines a turnout that operates Arduino digital output pin D30.  
  * Example: ``<T 26 VPIN 164>`` defines a turnout that operates the first pin on the first MCP23017 GPIO expander (if present).
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)
  
* Command to Delete a turnout ``<T id>`` :

  * Deletes the definition of a turnout with this ``id``.
  * Example: ``<T 25>`` deletes the previously defined turnout number 25.
  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. ID does not exist)

* Command to List all defined turnouts: ``<T>`` :

  * Lists all defined turnouts.
  * Returns the parameters that would be used to create the turnout, with the ``thrown`` state (1=thrown, 0=closed) appended.

      .. code-block::

          RETURNS: One of the following for each defined turnout or <X> if no turnouts defined.
          <H id DCC address subaddress thrown>     -- DCC Accessory Turnouts
          <H id SERVO vpin thrown_position closed_position profile thrown>  -- Servo Turnouts
          <H id VPIN vpin thrown>  -- VPIN Turnouts
          <H id LCN thrown>  -- LCN Turnouts
     
      The rest of the parameters are as defined for the turnout definition commands.

* ``id`` : The numeric ID (0-32767) of the turnout to control.  

  * (NOTE: You pick the ID. IDs are shared between Turnouts, Sensors and Outputs)

* ``address`` is the primary address of a DCC accessory decoder controlling a turnout (0-511)
* ``subaddress`` is the subaddress of a DCC accessory decoder controlling a turnout (0-3)
* ``vpin`` is the pin number of the output to be controlled by the turnout object.  For Arduino output pins, this is the same as the digital pin number.  For 
  servo outputs and I/O expanders, it is the pin number defined for the HAL device (if present), for example 100-115 for servos attached to the first PCA9685 Servo Controller module,
  116-131 for the second PCA9685 module, 164-179 for pins on the first MCP23017 GPIO expander module, and 180-195 for the second MCP23017 module.
* ``thrown`` - "0" is closed.  "1" is thrown.
* ``thrown_position`` : the PWM value corresponding to the servo position for THROWN state, normally in the range 102 to 490.
* ``closed_position`` : the PWM value corresponding to the servo position for CLOSED state, normally in the range 102 to 490.
* ``profile`` : the profile for the transition between states.  0=Immediate, 1=Fast (0.5 sec), 2=Medium (1 sec), 3=Slow (2 sec), 3=Bounce (for semaphore signals).

Once all turnouts have been properly defined, Use the ``<E>`` command to store their definitions to EEPROM.
If you later make edits/additions/deletions to the turnout definitions, you must invoke the ``<E>`` command if you want those new definitions updated in the EEPROM.
You can also **ERASE everything; (turnouts, sensors, and outputs)** stored in the EEPROM by invoking the ``<e>`` (lower case e) command. **WARNING: (There is no Un-Delete)**  

   Example: You have a turnout on your main line going to warehouse industry. The turnout is controlled by an accessory decoder with a address of 123 and is wired to output 3. 
   You want it to have the ID of 10.
   You would send the following command to the |EX-CS|:
   ``<T 10 DCC 123 3>``  

   * This Command means:  
   * ``T`` : (Upper case T) Define a Turnout  
   * ``DCC`` : The turnout is DCC Accessory Decoder based
   * ``10`` : ID number I am setting to use this turnout  
   * ``123`` : The accessory decoders address  
   * ``3`` : The turnout is wired to output 3  
   * RETURNS: ``<O>``  Meaning Command Successful

 |    Next you would send the following command to the |EX-CS|:
     ``<E>``

   * This Command means:  
   * ``E`` : (Upper case E) Store (save) this definition to EEPROM  
   * RETURNS: ``<O>``  Meaning Command Successful  

If turnout definitions are stored in EEPROM, the turnout thrown/closed state is also written to EEPROM whenever the turnout is switched.  
Consequently, when the |EX-CS| is restarted the turnout outputs may be set to their last known state (applicable for Servo and VPIN turnouts).
This is intended so that the servos don't perform a sweep on power-on when their physical position does not match initial position in the CommandStation.

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
     * ``T`` : (Upper case T) Throw a turnout.  
     * ``10`` : ID number of the defined turnout I want to control.  
     * ``1`` : Set turnout to Thrown (turned, on) position.  
     * 
       |EX-CS| should return ``<H 10 1>``  Meaning Command was Successful

       NOTE: The ``<T>`` command by itself with no parameters will list all turnout definitions and their directions


Sensors (Input) Commands
=========================

|EX-CS| supports Sensor inputs that can be connected to any Arduino Pin not in use by this program, as well as pins on external I/O expanders
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


* ``<S id vpin pullup>`` : Creates a new sensor ID, with specified PIN and PULLUP if sensor ID already exists, it is updated with specified PIN and PULLUP (You choose the number).  

  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory)

* ``<S id>`` : Deletes definition of sensor ID  

  * Returns: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. ID does not exist)  

* ``<S>`` : Lists all defined sensors  

  * RETURNS: ``<Q id vpin pullup>`` for each defined sensor or ``<X>`` if no sensors defined

``id`` : The numeric ID (0-32767) of the sensor
(You pick the ID & they are shared between Turnouts, Sensors and Outputs)

``vpin`` : the pin number of the input to be controlled by the sensor object.  For Arduino input pins, this is the same as the digital pin number.  For servo inputs and I/O expanders, it is the pin number defined for the HAL device (if present), for example 164-179 for pins on the first MCP23017 GPIO expander module, and 180-195 for the second MCP23017 module.

``pullup`` : 1 = Use internal pull-up resistor for PIN (ACTIVE=LOW), 0 = don't use internal pull-up resistor for PIN (ACTIVE=HIGH).

Once all sensors have been properly defined, use the ``<E>`` (upper case E) command to store their definitions to EEPROM.
If you later make edits/additions/deletions to the sensor definitions, you must invoke the ``<E>`` (upper case E) command if you want those new definitions updated in the EEPROM.
You can also clear **everything (turnouts, sensors, and outputs)** stored in the EEPROM by invoking the ``<e>`` (lower case e) command.
**(There is NO UN-Delete)**  

All sensors defined as per above are repeatedly and sequentially checked within the main loop of this sketch. If a Sensor Pin is 
found to have transitioned from one state to another, one of the following serial messages are generated:  


* ``<Q id>`` - for transition of Sensor ID from INACTIVE state to ACTIVE state (i.e. the sensor is triggered)  
* ``<q id>`` - for transition of Sensor ID from ACTIVE state to INACTIVE state (i.e. the sensor is no longer triggered)  

Depending on whether the physical sensor is acting as an "event-trigger" or a "detection-sensor," you may decide to ignore the ``<q id>`` return and only react to ``<Q id>`` triggers.

* ``<Q>`` - List the status of all defined sensors
*   
      RETURNS: <Q id> (active) or <q id> (not active)

Example: This shows sensors 1 and 2 are tripped or active while 3 and 4 are not.

         <Q 1><Q 2><q 3><q 4>
  

Outputs (DIO Pin) Commands
===========================

|EX-CS| supports optional OUTPUT control of any unused Arduino Pins for custom purposes. Pins can be activated or de-activated. 
The default is to set ACTIVE pins HIGH and INACTIVE pins LOW. However, this default behavior can be inverted for any pin in which case ACTIVE=LOW and INACTIVE=HIGH.  

Definitions and state (ACTIVE/INACTIVE) for pins are retained in EEPROM and restored on power-up.
The default is to set each defined pin to active or inactive according to its restored state. 
However, the default behavior can be modified so that any pin can be forced to be either active or inactive upon power-up regardless of its previous state before power-down.  

To have |EX-CS| utilize one or more Arduino pins as custom outputs, first define/edit/delete output definitions using the following variation of the ``<Z>`` command:  


* ``<Z id vpin iflag>`` : Creates a new output ID, with specified ``vpin`` and ``iflag`` values.

  * if output ID already exists, it is updated with specified ``vpin`` and ``iflag``.
  * Note: output state will be immediately set to ACTIVE/INACTIVE and pin will be set to HIGH/LOW according to ``iflag`` value specified (see below).
  * RETURNS: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. out of memory).

* ``<Z id>``: Deletes definition of output ID

  * RETURNS: ``<O>`` if successful and ``<X>`` if unsuccessful (e.g. ID does not exist)  

* ``<Z>`` : Lists all defined output pins

  * RETURNS: ``<Y id vpin iflag state>`` for each defined output pin or ``<X>`` if no output pins defined.

``id`` : The numeric ID (0-32767) of the output
(You pick the ``id`` & they are shared between Turnouts, Sensors and Outputs)

``vpin`` : the pin number of the output to be controlled by the output object.  For Arduino output pins, this is the same as the digital pin number.  For servo outputs and I/O expanders, it is the pin number defined for the HAL device (if present), for example 100-115 for servos attached to the first PCA9685 Servo Controller module, 116-131 for the second PCA9685 module, 164-179 for pins on the first MCP23017 GPIO expander module, and 180-195 for the second MCP23017 module.

``state`` : The state of the output (0=INACTIVE / 1=ACTIVE)

``iflag`` : Defines the operational behavior of the output based on bits 0, 1, and 2 as follows:  

.. code-block::

   ``iflag``, bit 0: 0 = forward operation (ACTIVE=HIGH / INACTIVE=LOW)
                 1 = inverted operation (ACTIVE=LOW / INACTIVE=HIGH)

   ``iflag``, bit 1: 0 = state of pin restored on power-up to either ACTIVE or INACTIVE 
                     depending on state before power-down. 
                 1 = state of pin set on power-up, or when first created,
                     to either ACTIVE of INACTIVE depending on IFLAG, bit 2

   ``iflag``, bit 2: 0 = state of pin set to INACTIVE upon power-up or when first created
                 1 = state of pin set to ACTIVE upon power-up or when first created 

Once all outputs have been properly defined, use the ``<E>`` Upper Case "E" command to store their definitions to EEPROM.
If you later make edits/additions/deletions to the output definitions, you must invoke the ``<E>`` command if you want those new definitions updated in the EEPROM.
You can also **ERASE everything (turnouts, sensors, and outputs)** stored in the EEPROM by invoking the ``<e>`` (lower case e) command.
**(There is no Un-Delete)**  

To change the state of outputs that have been defined use:  


* ``<Z id state>`` : Sets output ``id`` to either ACTIVE or INACTIVE state  
* RETURNS: ``<Y id state>`` , or ``<X>`` if output ID does not exist  

  * ``id`` : The numeric ID (0-32767) of the defined output to control  
  * ``state`` : The state of the output (0=INACTIVE / 1=ACTIVE)  

When controlled as such, the Arduino updates and stores the direction of each output in EEPROM so that it is retained even without power. 
A list of the current states of each output in the form ``<Y id state>`` is generated by |EX-CS| whenever the ``<s>`` 
status command is invoked. This provides an efficient way of initializing the state of any outputs being monitored or controlled by a separate interface or GUI program. 

Storing and Erasing Turnouts, Sensors and Outputs in EEPROM
=============================================================

 ``<E>`` Upper case E : Command to **Store** definitions to EEPROM, returns the number of stored turnouts, sensors, and outputs.

  .. code-block::

      RETURNS: <e nTurnouts nSensors nOutputs>

 ``<e>`` Lower Case e: Command to **Erase ALL (turnouts, sensors, and outputs)** definitions from EEPROM 

  .. code-block::

      RETURNS: <0> EEPROM Empty


  *NOTE:There is NO Un-Delete*

Engine Decoder Programming Commands
======================================

PROGRAMMING-MAIN TRACK
----------------------

WRITE CV BYTE TO ENGINE DECODER ON MAIN TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes, without any verification, a Configuration Variable BYTE to the decoder of an engine on the main operations track. 


* Write CV BYTE Format is: ``<w cab cv valule>``  
* ``cab`` : The short (1-127) or long (128-10293) address of the engine decoder  
* ``cv`` : The number of the Configuration Variable memory location in the decoder to write to (1-1024)  
* ``value`` : The value to be written to the Configuration Variable memory location (0-255)  
* RETURNS: NONE

WRITE CV BIT TO ENGINE DECODER ON MAIN TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes, without any verification, a single bit within a Configuration Variable BIT to the decoder of an engine on the main operations track. 


* Write CV BIT Format is: ``<b cab cv bit value>``
* ``cab`` :  the short (1-127) or long (128-10293) address of the engine decoder  
* ``cv`` : the number of the Configuration Variable memory location in the decoder to write to (1-1024)  
* ``bit`` : the bit number of the Configuration Variable register to write (0-7)  
* ``value`` : the value of the bit to be written (0-1)  

  * RETURNS: NONE

PROGRAMMING-PROGRAMMING TRACK
-----------------------------

.. NOTE:: By design, for safety reasons, the NMRA specification prevents locos from responding to throttle or function commands while on the service track. A loco WILL NOT MOVE on the service track! Don't let the little "jumps" you may see when you are programming a CV confuse you. The loco pulses the motor to give a jump in current that we read as an "ACK" (acnowledgment), that causes some locos to stutter ahead slightly every time you read or write a CV.

READ LOCO ADDRESS ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  ``<R>`` Upper Case R : Read Loco address (programming track only)

  .. code-block::

      RETURNS: <r address> where it finds the address of our loco or <r -1> for a read failure.

Example: <r 3450> shows that Loco with ID 3450 is on the programming track.


WRITE LOCO ADDRESS TO ENGINE DECODER ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes, and then verifies, the address to decoder of an engine on the programming track. This involves clearing any consist and automatically setting a long or short address. This is an easy way to put a loco in a known state to test for issues like not responding to throttle commands when it is on the main track.

Write loco address Format is: ``<W address>``
ADDRESS: The loco address to be written (1-10239).


WRITE CV BYTE TO ENGINE DECODER ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes, and then verifies, a Configuration Variable BYTE to the decoder of an engine on the programming track  

* Write CV BYTE Format is: ``<W cv value>``
* ``cv`` : The number of the Configuration Variable memory location in the decoder to write to (1-1024  ).  
* ``value`` : The value to be written to the Configuration Variable memory location (0-255).

  * ``RETURNS:`` ``<r cv value>``
  * ``cv:`` The number of the Configuration Variable memory location written to.
  * ``value:`` Is a number from 0-255 as read from the CV, or -1 if verification read fails.

**Deprecated old format below, please use the new, brief <W CV VALUE> command instead**

* Write CV BYTE Format is: ``<W cv value callbacknum callbacksub>``
* ``cv`` : The number of the Configuration Variable memory location in the decoder to write to (1-1024  ).  
* ``value`` : The value to be written to the Configuration Variable memory location (0-255).  
* ``callbacknum`` : An arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs that call this function.  
* ``callbacksub`` : a second arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs (e.g. DCC-EX Interface) that call this function.  

  * ``RETURNS:`` ``<r callbacknum|callbacksub|cv value>``
  * ``cv value:`` Is a number from 0-255 as read from the requested CV, or -1 if verification read fails.  

WRITE CV BIT TO ENGINE DECODER ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes, and then verifies, a Configuration Variable BIT to the decoder of an engine on the programming track  


* Write CV BIT Format is: ``<B CV BIT VALUE CALLBACKNUM CALLBACKSUB>``  
* ``CV`` : The number of the Configuration Variable memory location in the decoder to write to (1-1024).  
* ``BIT`` : The bit number of the Configuration Variable memory location to write (0-7).  
* ``VALUE`` : The value of the bit to be written (0-1).  
* ``CALLBACKNUM`` : An arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs that call this function.  
* ``CALLBACKSUB`` : A second arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs (e.g. DCC-EX Interface) that call this function.  

  * ``RETURNS:`` ``<r CALLBACKNUM|CALLBACKSUB|CV BIT VALUE>``  
  * ``CV VALUE`` is a number from 0-1 as read from the requested CV bit, or -1 if verification read fails.  

READ CONFIGURATION VARIABLE BYTE FROM ENGINE DECODER ON PROGRAMMING TRACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If specified with parameters, reads a Configuration Variable from the decoder of an engine on the programming track. If no parameters are specified, it returns the Address of the loco on the programming track.


Read CV BYTE Format is: ``<R CV CALLBACKNUM CALLBACKSUB>``  

* ``CV`` : The number of the Configuration Variable memory location in the decoder to read from (1-1024).  
* ``CALLBACKNUM`` : An arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs that call this function.  
* ``CALLBACKSUB`` : A second arbitrary integer (0-32767) that is ignored by the Command Station and is simply echoed back in the output - useful for external programs (e.g. DCC-EX Interface) that call this function. 

  * ``RETURNS:`` ``<r CALLBACKNUM|CALLBACKSUB|CV VALUE>``  
  * ``CV VALUE`` is a number from 0-255 as read from the requested CV, or -1 if read could not be verified.

Read Engine address format is simply: ``<R>``

* ``RETURNS:`` ``<r ADDRESS>`` when successful and ``<r -1>`` if it is not.

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

Throttle commands for developers
================================

These commands have been provided for those wishing to develop throttles that utilise the DCC-EX API.

As there is existing detailed documentation for these, we will not elaborate here. Instead, refer to :doc:`/reference/developers/tech-reference` for full details on these commands.

``<JT>`` returns the defined turnout IDs

``<JT id>`` returns the ID, state, and description of the specified turnout ID

``<JA>`` Returns the defined automation and route IDs

``<JA id>`` Returns the ID, type (A=automation or R=route), and description of the specified automation/route ID

``<JR>`` Returns the defined roster entry IDs

``<JR id>`` Returns the ID, description, and function map of the specified roster entry ID

``<t cabid>`` Requests a deliberate update of cab speed/functions in the same format as the cab broadcas

Diagnostic Commands
=====================

Status
------

``<s>`` Lowercase "s": EX-CommandStation Status

  .. code-block::

       RETURNS: Track power status, Version, Microcontroller type, Motor Shield type, build number, and then any defined turnouts, outputs, or sensors.
       Example: <iDCC-EX V-3.0.4 / MEGA / STANDARD_MOTOR_SHIELD G-75ab2ab><H 1 0><H 2 0><H 3 0><H 4 0><Y 52 0><q 53><q 50>

"D" Commands
------------

.. Note:: 1 and 0 and ON and OFF can be used interchangeably in EX-CommandStation

* ``<D CABS>`` Shows cab numbers and speed in reminder table.
* ``<D RAM>`` Shows remaining RAM.
* ``<D ACK 1|0>`` Enables ACK diagnostics
* ``<D CMD 1|0>`` Enables Command Parser diagnostics
* ``<D WIFI 1|0>`` Enables Wifi diagnostics
* ``<D WIT 0|1>`` Enables WiThrottle diagnostics
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
    Example output showing a connected PCA9685 Servo controller and an MCP23017 I/O expander: 

    .. code-block:: 

      17:00:10.358 -> <* PARSING:D HAL SHOW * >
      17:00:10.358 -> <* Arduino Vpins:2-69 * >
      17:00:10.358 -> <* PCA9685 I2C:x40 Configured on Vpins:100-115 * >
      17:00:10.358 -> <* PCA9685 I2C:x41 Configured on Vpins:116-131 OFFLINE * >
      17:00:10.358 -> <* MCP23017 I2C:x20 Configured on Vpins:164-179 * >
      17:00:10.358 -> <* MCP23017 I2C:x21 Configured on Vpins:180-195 * >

DECODER TEST
------------

These following commands are detailed above but are worth repeating here. The ``<R>`` command will attempt to read the decoder on the service (programming) track and try to read its long or short address and display it in the serial monitor. To do this, it also resets any consist. So if your loco isn't moving on the MAIN track, this command is a good way to make sure a consist is enabled as well as to make sure you have the correct address. Put together with the ``<D ACK ON>`` command, this shows a log giving detailed information about track current and ACK detection timings that you can provide to our support team to find out why a particular decoder may not be behaving correctly.

``<R>`` Upper Case R : Read Loco address (programming track only). Returns:

 .. code-block::

      <r ADDRESS> where it finds the address of our loco or <r -1> for a read failure.

``<D ACK ON><R>`` - When sent together as shown or one right after the other, this combined command shows the detailed results of what happened when trying to read the Address CV(s) and any response back from the decoder.

ACK Tuning Commands
^^^^^^^^^^^^^^^^^^^^

To help define the correct ACK parameters required for different decoders, there are several diagnostic commands available, with defaults based on the NMRA standard for ACK responses during service mode programming.

.. note:: 
  
  The basic ACK defaults have changed as of CommandStation-EX version 4.1.0 to:
  
  - LIMIT 50mA
  - MIN 2000 uS
  - MAX 20000uS

  If you still need to override these and need to do so permanently, the commands can be added to "mySetup.h" as per :ref:`ex-commandstation/advanced-setup/startup-config:adding in the startup commands`.

  Note with decoders that are equipped with "keep alives" or capacitors, it can be beneficial to turn the power on with `<1>` or `<1 PROG>` to charge the capacitors prior to programming, which can increase the reliability of the ACK, especially when attemping to read the full sheet.

To quote the relevant section from NMRA S 9.2.3:

.. note:: 

  45 Basic Acknowledgment
  
  Basic acknowledgment is defined by the Digital Decoder providing an increased load (positive-delta) on the programming track of at least 60 mA for 6 ms +/-1 ms. It is permissible to provide this increased load by applying power to the motor or other similar device controlled by the Digital Decoder.

``<D ACK LIMIT mA>`` Use this command to override the minimum milliamps (mA) required to detect the ACK pulse, eg. ``<D ACK LIMIT 30>`` means a minimum 30mA pulse would be accepted.
 
``<D ACK MIN uS>`` Use this command to override the minimum amount of time in microseconds (uS) the pulse needs to be active for, eg. ``<D ACK MIN 2000>`` means a pulse of 2ms or more would be accepted.

``<D ACK MAX uS>`` As above, however overriding the maximum amount of time for a pulse, eg. ``<D ACK MAX 20000>`` means a pulse up to 20ms would be accepted.

``<D ACK RETRY x>`` When reading/writing CVs, the program will try again upon failure.  The default is ``<D ACK RETRY 2>``, which means 3 attempts before a failure is reported.  Each of the unsuccessful attempts is reported in the serial monitor or JMRI monitor log.  The last unsuccessful attempt remains on the display if in use.  To reset the running total, send the command manually: ``<D ACK RETRY 2>``.

``<D PROGBOOST>``  By default, the programming track has a current limit enabled of 250mA, so any programming activities requiring more than this value will cause power to the programming track to be cut for 100ms. Run this command to override this if programming decoders trigger current limiting on the programming track.
 
SEND PACKET TO THE TRACK
------------------------

.. Warning:: THIS IS FOR DEBUGGING AND TESTING PURPOSES ONLY.  DO NOT USE UNLESS YOU KNOW HOW TO CONSTRUCT NMRA DCC PACKETS - YOU CAN INADVERTENTLY RE-PROGRAM YOUR ENGINE DECODER

| ``<M>`` Command writes a packet the MAIN track
| ``<P>`` Command writes a packet to the PROG track

Writes a DCC packet of two, three, four, or five hexadecimal bytes to a register driving the selected track

  **FORMAT:** ``<M|P REGISTER BYTE1 BYTE2 [BYTE3] [BYTE4] [BYTE5]>``

.. code-block::

   ``REGISTER:`` an internal register number, from 0 through MAX_MAIN_REGISTERS (inclusive), to write (if REGISTER=0) or write and store (if REGISTER>0) the packet
   ``BYTE1:``  first hexadecimal byte in the packet
   ``BYTE2:``  second hexadecimal byte in the packet
   ``BYTE3:``  optional third hexadecimal byte in the packet
   ``BYTE4:``  optional fourth hexadecimal byte in the packet
   ``BYTE5:``  optional fifth hexadecimal byte in the packet

   returns: NONE

WiFi "AT" Commands
==================

``<+COMMAND>`` Plus sign followed by a command. Sends AT commands to the WiFi board (ESP8266, ESP32, etc.) There is not space between the "+" and the command.

Users familiar with the AT Command Set of WiFi board may enter commands directly into the serial monitor in real-time or as setup commands in the :doc:`mySetup.h file </ex-commandstation/advanced-setup/startup-config>`. This allows users to override the default WiFi connect sequence or to send any command to change a WiFi device setting.

``<+X>`` A special command to force the "connected" flag (WiFi Connected Mode) to on inside the Command Station so that our loop will start seeing network traffic. If your code creates a connection outside of our normal WiFi code, this provides a way for you to notify the Command Station that it needs to process commands on a connection you created and so you can send your own AT commands.

Examples:

  <+GMR> - Sends the "AT+GMR" command that prints version information from the WiFi device.
  <+CIFSR> - Gets the local IP Address.

For more detail follow these links:

:doc:`DCC-EX WiFi Configuration </ex-commandstation/advanced-setup/supported-wifi/wifi-config>`

`Espressif AT Command Set PDF File (Exressif makes the ESP8266) <https://www.espressif.com/sites/default/files/documentation/4a-esp8266_at_instruction_set_en.pdf>`_


User Commands
==============

``<U>`` Is reserved for user commands.
