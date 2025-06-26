:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-csb1.rst
|EX-CS-LOGO|

***************************************
EX-CSB1 as a DCC Booster (Booster Mode)
***************************************

|SUITABLE| |conductor| |tinkerer| |engineer| |support-button|

The |EX-CSB1| can be configured as a DCC Booster.  As a booster it can take input from any DCC Command Station, not just an |EX-CS|, to provide additional two power districts to your layout.  With the addition of a |EX-MS|, it can provide up to 4 power districts.

To configure the |EX-CSB1| as a DCC Booster, you will need to install the |EX-CS| software on it with the addition of the following commands to the ``myConfiguration.h`` file:

  .. code-block::

   AUTOSTART
      SET_TRACK(A,"BOOST")
      SET_TRACK(B,"BOOST")
      DONE

If you are using an |EX-CSB1| with a |EX-MS| as your booster you will need to add the following commands to the myConfiguration.h file:

  .. code-block::

   AUTOSTART
      SET_TRACK(A,"BOOST")
      SET_TRACK(B,"BOOST")
      SET_TRACK(C,"BOOST")
      SET_TRACK(D,"BOOST")
      DONE

You also need to add these two lines to the ``config.h`` file:

  .. code-block::

   #define WIFI_LED 33
   #define BOOSTER_INPUT 32

You will then need to connect a ``MAIN`` output from your command station to Railsync connector on the |EX-CSB1| Booster.  The |EX-CSB1| Booster will then provide power to the rails on the A and B outputs.  If you are using a |EX-MS|, it will provide power to the rails on the C and D outputs.

If you are using an |EX-CSB1| as your Command Station, it is recommended that you use one of the outputs as the dedicated output to the |EX-CSB1| Booster. If you use the output to the booster, as well as to a block of track, a short or overload on that block will cause the |EX-CSB1| Booster to also kill power to all of its outputs.

.. note:: 

   The outputs can be configured as:

   * ``BOOST`` - Booster mode
   * ``BOOST_INV`` - Booster mode inverted
   * ``BOOST_AUTO`` - Booster mode + Auto-reverser mode
