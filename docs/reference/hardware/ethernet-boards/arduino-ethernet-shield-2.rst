.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst
|EX-CS-LOGO|

*************************
Arduino Ethernet Shield 2
*************************

|tinkerer| |engineer|

There have been different revisions for the Arduino Network Shields, the main difference is the version of the ethernet controller on the board. The "2" board uses the Wiznet W5500, other versions used the older W5100 chip. The only supported chip currently is the W5500, but the other boards may work as well. The W5500 can handle 8 simultaneous socket connections while the W5100 can handle 4. These boards provide a network (IP) stack capable of both TCP and UDP. This board also has an SDCard which can be used for your own custom features or for storing settings with a possible future version of |EX-CS|.

.. image:: /_static/images/ethernet/arduino_ethernet_shield_2.jpg
   :alt: Arduino Ethernet Shield 2
   :scale: 85%
