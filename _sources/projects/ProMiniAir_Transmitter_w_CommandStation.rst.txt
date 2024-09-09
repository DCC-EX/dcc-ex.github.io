.. include:: ../include/include.rst
.. include:: ../include/include-l1.rst
.. include:: ../include/include-description.rst

*********************************************************************************************************
Battery Power, Radio Control: ProMiniAir Transmitter Integrated with a WiFi-equipped |EX-CS| (PMA Tx/WCS)
*********************************************************************************************************

|engineer|

.. figure:: /_static/images/projects/New_PMA_Tx_WCS_CNV_Annotated.png
   :alt: New_PMA_Tx_WCS_CNV_Annotated
   :scale: 20%
   :align: center

   The components of the ProMiniAir Tx/WCS

The open-source availability and flexibility of the |EX-CS|
makes it easy to adapt it for battery power, radio control (bprc or
"Dead Rail") of DCC-equipped locomotives and DCC accessories.  A
WiFi-equipped ESP32-WROOM, hosting a slightly-modified version of 
|EX-CS|, is integrated with an 869/915 MHz ProMiniAir
"Dead Rail" Transmitter to:

1. Receive control and programming commands from multiple sources:

   * Apps transmitting
     WiThrottle or native |DCC-EX| commands via WiFi
   * JMRI or other PC-based throttle applications sending
     WiThrottle or native |DCC-EX| commands via USB
   * Optionally: DCC Track Right/Left from a standard DCC throttle

2. Wirelessly transmit DCC control and programming commands from the
   |EX-CS| to onboard radio receivers


The ProMiniAir Transmitter is integrated with a WiFi-equipped
ESP32-WROOM hosting a slightly modified version of |EX-CS| firmware,
which is available, along with additional libraries, at this `GitHub site 
<https://github.com/darrelllamm0/EX-CommandStation_ESP32_for_ProMiniAir>`_.
Instead of a motor shield, the DCC commands from the |EX-CS|
are sent to the ProMiniAir Transmitter that wirelessly transmits
the DCC to compatible onboard radio receivers with their integrated
amplifiers that "reconstitute" DCC Track Right/Left for onboard DCC
decoders.  

The ProMiniAir Transmitter can be reconfigured (e.g., transmit channel
number and transmit power) by changing its Configuration Variables at
DCC address 9900 using |DCC-EX| "Programming On Main" commands (e.g.,
<w 9900 255 channel_number> and <w 9900 254 power_level>).

You can find more detailed information on the PMA Tx/CNV at this `website
<https://oscaledeadrail.com>`_.

The "plug and play" PMA Tx/WCS includes the following:

* A WiFi-equipped ESP32-WROOM hosting modified |EX-CS| firmware,
* An 869/915 MHz ProMiniAir "Dead Rail" Transmitter,
* A "DCC Converter" that accepts DCC Track Right/Left from "traditional" DCC throttles and
  converts it to 3.3 V DCC that is input to the |EX-CS| and interwoven with 
  the |EX-CS|'s DCC output,
* Two OLEDs to display status information from the |EX-CS| and the
  ProMiniAir Transmitter,
* All components are mounted on a PCB in a protective box,
* Power comes from either a USB cable and USB power converter (provided) or from the Track Right/Left
  of a DCC throttle,
* A detailed `ProMiniAir Users Manual 
  <http://oscaledeadrail.com/wp-content/uploads/2022/09/ProMiniAir_Users_Manual.pdf>`_ 
  and `detailed online setup instructions 
  <https://oscaledeadrail.com/instructions-for-the-standalone-prominiair-transmitter/>`_
  for the PMA Tx/WCS are available.


The ProMiniAir Tx/WCS can be found on eBay at this `link <https://www.ebay.com/itm/144861071035>`_
or by using the "ProMiniAir" search string.


.. figure:: /_static/images/projects/New_PMA_Tx_WCS_CNV_Connections.png
   :alt: Connections
   :scale: 20%
   :align: center

   Connections of the ProMiniAir Tx/WCS with other components
   for battery power, radio control (Dead Rail)



