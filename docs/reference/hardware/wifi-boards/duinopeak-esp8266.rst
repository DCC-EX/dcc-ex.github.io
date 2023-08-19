.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst
|EX-CS-LOGO|
**************************************
Duinopeak ESP8266 WiFi Expansion Board
**************************************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

This board is designed as an expansion/prototyping board as well as a WiFi board. Tinkerers that want the extra space on the board to solder your experiments can have a party on the PCB! The only caveat with this board is that it cannot easily be connected in "passthrough mode" if you needed to use the Arduino to test a direct connection to the onboard ESP8266. It does not like the USB cable connected at the same time as a signal is on the Tx/Rx pins. This is a minor issue and does not affect normal operation since you won't have anything connected to the USB port.

.. note:: This is just a carrier board for an ESP-01 or 01s. You will still need an ESP-01s to place onto this board. See the next section.

.. figure:: /_static/images/assembly/duinopeak.jpg
   :alt: Duinopeak WiFi Board
   :scale: 75%

   Duinopeak WiFi Board

Install the Shield
==================

To install this board on your Arduino, follow the same steps as above, with the added step of installing an ESP-01s onto the board:

* Remove or place the plastic pin jumpers to the side
* Align and seat the board
* Use wire jumpers to connect any Rx pin to Tx1 on the Mega, and any Tx pin to Rx1 on the Mega
* Seat an ESP-01s onto the 8 pin header on the board, oriented with the white ESP-01 outline
