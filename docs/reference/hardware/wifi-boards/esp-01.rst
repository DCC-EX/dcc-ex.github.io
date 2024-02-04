.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst
|EX-CS-LOGO|

**************************************
ESP-01 and ESP-01s
**************************************

|tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :depth: 1
      :local:

This is the board that started it all. It fuelled the WiFi revolution in small devices. In fact, this little board is actually a microcontroller that is more powerful than the Arduino Uno! The difference between the 01 and the 01S is primarily that there is more memory on the 01-"S". Since the 01 version has been retired, any new board you get should be the 01s, but either will work.

.. figure:: /_static/images/assembly/esp-01s_2.png
   :alt: ESP-01s
   :scale: 75%

   ESP-01s

.. warning:: 
   :class: warning-float-right

   Please be aware that the Espressif AT firmware currently being shipped with these devices **will probably NOT work** with |EX-CS| out of the box.

   This can be corrected, but is probably beyond Conductor level and requires additional hardware.  

   See :doc:`/support/wifi-at-version` for details on how to check the version and how to correct it if needed.

   We are currently investigating other options.
    
Install the Module
==================

Below is a wiring diagram for connecting the ESP8266 to the Arduino. For clarity, the image does not show the motor board already on top of the Mega, but since the headers connect all the pins together vertically, you can find the same pins on the motor board to get the 3.3V and Gnd to power the ESP8266.


.. figure:: /_static/images/assembly/esp8266_mega.png
   :alt: ESP-8266 Wiring to a Mega
   :scale: 75%

   Wiring an ESP-01s to a Mega

**Wiring**

.. code-block::

   Arduino   ESP8266
   3.3V -----> Vcc
   3.3V -----> CH_PD
   Gnd  -----> Gnd
   Tx   -----> Rx
   Rx   -----> Tx

In order to connect both Vcc and CH_PD to the 3.3V output of the Arduino, you can make a "Y" shaped jumper or put the ESP-01s on a small circuit board and wire it that way. Below are little boards you can buy called "ESP-01 Breakout Board" or "ESP-01 Breadboard adapter". Some even have a voltage regulator so you can use the 5V power from the Mega instead of 3.3V, and "level shifters" to adapt the IO pins from 5V to 3.3. We highly recommend these little boards. In `esp-01s-adapters`_ below, the board on the left is just a plain breadboard adapter. The other two boards have the regulator and logic level shifters.

.. note:: About current requirements: While we at |DCC-EX| Labs have had success with running the ESP-01s off the 3.3V Mega power supply, this is at the limit of what the Mega can supply. The Mega 3.3V regulator is only rated for 200mA. The ESP can exceed this in short bursts. If you want to be safe, you can power a 5V to 3.3V regulator from the 5V supply, or find another way to provide clean, regulated 3.3V to the ESP.

.. figure:: /_static/images/assembly/esp-01_adapter.png
   :alt: ESP-01s Adapters
   :scale: 75%
   :name: esp-01s-adapters

   ESP-01 Breakout Boards

.. warning:: The ESP8266 chips are designed for 3.3V. DO NOT TRY TO CONNECT THEM TO 5V!! While they cannot handle 5V for power, their GPIO pins are 5V tolerant. Because of this, you don't need any additional circuitry. However, to be safe, you can use a small `level shifter board <https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide/all>`_, or use one of the breakout boards like the one above and to the right that has a 3.3V regulator and level shifters for the Tx and Rx pins.
