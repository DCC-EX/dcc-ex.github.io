.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-cs.rst
|EX-CS-LOGO|

***********************
Direct Connection (USB)
***********************

|tinkerer| |engineer| |support-button|

Connection Type: Direct to Command Station
==========================================

If your |EX-CS| is an Arduino Nano or Uno, or you're using |JMRi|, or you have a throttle that connects via a serial connection, you only need a direct connection method and don't need Bluetooth or wireless capabilities.

This is also all that's required if you're using API commands via the serial console. However, this is probably only relevant if you need to do so if requested as part of a support ticket.

The direct connection is provided by simply connecting to |EX-CS| via the USB interface.

If you are using |JMRi|, refer to the :doc:`/ex-commandstation/advanced-setup/supported-connections/jmri` page.

If you're using a throttle with a physical serial interface, this may require connecting directly to the Tx/Rx pins on the |EX-CS|, but the specifics of this will need to be outlined by the throttle instructions.

If you're using a Mega2560 or another microcontroller that has more than one serial connection available, you will need to uncomment the appropriate line in your "config.h" file:

.. code-block:: cpp

  #define SERIAL1_COMMANDS    // Broadcast to throttles on Tx1/Rx1
  #define SERIAL2_COMMANDS    // Broadcast to throttles on Tx2/Rx2
  #define SERIAL3_COMMANDS    // Broadcast to throttles on Tx3/Rx3