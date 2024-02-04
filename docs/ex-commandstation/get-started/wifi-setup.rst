.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: WiFi setup

|EX-CS-LOGO|

***********
Adding WiFi
***********

|conductor|

.. sidebar::

   .. contents:: On this page
      :local:
      :depth: 1

:dcc-ex-red-bold:`Please read the warning before you proceed.`

This page is specifically intended for a |conductor-text| who intends to install *just* the recommended hardware. If you are a |tinkerer-text| or |engineer-text| or want to install some of the additional, or different, hardware from that recommended for a |conductor-text| then we suggest that you look at the :doc:`/ex-commandstation/advanced-setup/supported-connections/wifi-setup` page for the full list of WiFi options.

----

.. warning:: 

   Please be aware that the Espressif AT firmware currently being shipped with these devices **will probably NOT work** with |EX-CS| out of the box.

   This can be corrected, but is probably beyond Conductor level and requires additional hardware.  

   See :doc:`/support/wifi-at-version` for details on how to check the version and how to correct it if needed.

   We are currently investigating other options.

The purpose of adding WiFi to your |EX-CS| is allow connection up to 5 WiFi throttles (e.g. phones) DIRECTLY to it, eliminating the need for a computer and another software controller. 

However, WiFi is optional. If you wish to simply use your computer connected via a USB cable to the |EX-CS| using the |JMRI| application (or similar), you can :doc:`skip ahead to the next page <installer>`.

.. rst-class:: clearer

.. sidebar:: Using JMRI (Alternate)
   
   |conductor| |BR| An *Alternate* to connecting to your |EX-CS| directly via WiFi is to do so indirectly through |JMRI|. To do this, you don't need a WiFi board. You only need to use a USB cable instead. This is described on the :doc:`/ex-commandstation/advanced-setup/supported-connections/jmri` page.

There are many ways to add WiFi to your Command Station. **We will cover only one method here.** You may need to know a little bit about networking, but if you can get your phone to connect to your home network, you can do this.

|image-note|

For a video to help you, click below.

   .. raw:: html
      
      <iframe width="336" height="189" src="https://www.youtube.com/embed/N6TWR7fIl0A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Why Use WiFi?
=============

.. sidebar:: 

   |tinkerer| |engineer| |BR| Using WiFi (OR Ethernet) to talk between |JMRI| and |EX-CS| is complex, slow and functionally limited and is NOT SUPPORTED. However, you can STILL use a wireless throttle with a |JMRI| setup. Assuming your PC already has WiFi capability, you can connect through THAT instead of directly to the Command Station, while the Command Station gets its commands through the USB connection.

**BEFORE you purchase a WiFi card, please consider whether you actually need it.**

If you wish to run trains from your phone, tablet or other |WiThrottle protocol| devices connected directly to the |EX-CS|, without a PC involved, then you **should follow the instructions below**.

   However, with the base |EX-CS| without a WiFi shield, you can use a USB cable to connect to a computer to run |JMRI| or our web browser based |EX-WT|. So, if you intend to run trains from a PC, or by only using a web browser, |JMRI|, Rocrail, or similar, then **YOU DO NOT NEED WiFi ON THE CS**. If this the case you can :doc:`skip ahead to the next page <installer>`.

|force-break|

.. sidebar:: 

   |tinkerer| |engineer|

   While it may be possible to run WiFi on an Uno, Nano or Pro Mini, it is not supported. The Uno simply does not have enough memory.

What you will need (for WiFi)
=============================

* A |EX-CS| made from an **Arduino Mega** and a Motor Driver (from the previous page)
* A WiFi board
* Two (2) Male to Female Jumpers leads

.. rst-class:: clearer

Makerfabs ESP8266 WiFi Shield -  installation instructions
================================================================================

.. sidebar:: 
   
   |tinkerer|

   **Alternate WiFi boards** |br| For more boards you can be to used, see the :doc:`WiFi Boards Section </reference/hardware/wifi-boards>`

Most boards based on the ESP8266 should work with the |EX-CS|. However, with all the variations and software versions out there this is the one that we recommend for people starting out with |DCC-EX|.

We like this board here at |DCC-EX|. It is simple, inexpensive, easy to use, and it works.

.. figure:: /_static/images/assembly/wifi_jumpers1.jpg
   :alt: Makerfabs ESP-8266 WiFi Shield
   :scale: 75%

   Makerfabs ESP8266 WiFi Shield

Installing the board follows the same procedure in the previous section on :doc:`assembly`. Start by noting the tab end of the board and align it with the tab end of the motor board. You will stack this board on top to make a three board stack.

Remove the plastic jumpers
---------------------------

Note the two black plastic jumpers: we need to remove both of them. You can pull them off with your fingers or needle nose pliers and either stick them in a drawer or move them to the side by having them connect via one side to any of the row of Rx pins. The other end of the connector will just hang out over the WiFi Board.


.. figure:: /_static/images/assembly/wifi_pins.jpg
   :alt: Remove the plastic jumpers
   :scale: 75%

   Remove the plastic jumpers

Align the boards
------------------

Turn the board so that the tab end is to the left and the power connectors on the other boards are to the right. You will be looking at the left side of the shield. Align it so that the pins align starting with the tab end of the boards. The Rx, Tx, 2, 3, 4, 5, 6, 7 pins on the Motor Shield line up with the 0 through 7 pins on the Makerfabs WiFi Board. 

Start to get this row partially seated so all the pins are lined up with the holes. Note that there are more holes than pins. The two header holes closest to the power connectors will be empty.


.. figure:: /_static/images/assembly/wifi_seat1.jpg
   :alt: Get the left side pins aligned
   :scale: 75%

   Get the left side pins aligned

Seat the boards
---------------

Now do the the other side. If all the pins are straight and lined up properly, hold both sides of the board and press it together gently (:numref:`wifi-right-side-pins-aligned`). 

Note that the pins are quite long and will not go all the way into the header. You should have even more of the pins showing between the bottom of the WiFi board and the top of the header on the Motor Board than between the Motor Board and the Arduino. This is normal (see :numref:`wifi-fully-seated-boards`).


.. figure:: /_static/images/assembly/wifi_seat2a.jpg
   :alt: Get the right side pins aligned
   :scale: 75%
   :name: wifi-right-side-pins-aligned

   Get the right side pins aligned

.. figure:: /_static/images/assembly/wifi_seat_full.jpg
   :alt: Fully seated boards
   :scale: 75%
   :name: wifi-fully-seated-boards

   Fully seated boards

Install the jumper wires
-------------------------

We now need to connect The Transmit (Tx) and Receive (Rx) pins on the ESP8266 to the Rx and Tx pins for Serial1 on the Mega. The Mega has one serial port connected to the USB port, and then 3 extra ones we can access from pins on the board. You can think of Tx as "talking" and Rx as "listening". That will help you remember that if one thing is talking, the other has to use its ears to listen. So we must connect the Tx of the WiFi board to Rx1 on the Mega and the Rx pin on the WiFi Board to Tx1 on the Mega.

There are three rows of pins on the Makerfabs WiFi shield. The middle pins each connect to one of the first 8 pins on the header. Pin 0 goes to header pin 0, pin 1 goes to header pin 1, and so on. We aren't going to need those. With the plastic jumpers removed, nothing will be connected to any of those pins on the WiFi Board, and therefore not connected down to the Mega through the Motor Shield.

ALL of the pins in the row marked Tx (the row closest to the header) are connected to the Tx pin of the ESP8266. ALL of the pins in the row marked Rx (the row closest to the middle of the board) are connected to the Rx pin on the ESP8266.

.. note:: 
   :class: note-float-right

   The screen printing on the board may make it hard to see which pins are 18 and 19, they may not be aligned exactly. 
   
   Count the pins if you need to to make sure that you are using the correct ones.

Take a jumper wire and connect it to any one of the Tx pins on the WiFi Board, and connect the other end to the Rx1 pin on the mega (pin 19).

Take a second jumper wire and connect it to any one of the Rx pins on the WiFi Board and connect the other end to Tx1 on the mega (pin 18).

.. figure:: /_static/images/assembly/wifi_jumpers2.png
   :alt: Install the Jumper wires
   :scale: 75%

   Install the jumper wires

Next Steps - Install the Software
=================================

Click :doc:`here </ex-commandstation/get-started/installer>` or click the "next" button to learn how to install the software on your |EX-CS|.

.. 
   If you already have the Command Station software running and are just adding WiFi, there is nothing further you need to do if you want to use the Command Station as an Access Point (AP) and connect a WiThrottle compatible CAB (|Engine Driver|). The next time you power up the Command Station, it will automatically find your WiFi board and which port it is connected to. See the detailed instructions here: :doc:`WiFi Configuration <../advanced-setup/wifi-config>`

..
   .. note:: 
      
      LOGIN PASSWORD - If you use AP Mode, you must connect your throttle to the DCCEX network, not your home network. The AP will be called DCCEX_abcdef and the password will be PASS_abcdef, where "abcdef" is the last 6 characters of the ESP MAC address. Just look at the list of available networks on your phone and you can see this information. It is also shown in the boot log if you connect your Command Station to a computer running a serial monitor. Please click on the "WiFi Configuration" link above for more detailed instruction.

.. 
   If you are setting up your Command Station for the first time, or are making changes to the basic setup, navigate to :doc:`Command Station Downloads </download/ex-commandstation>` to load firmware onto the Command Station.
