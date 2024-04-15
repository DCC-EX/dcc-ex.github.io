.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst

|EX-CS-LOGO|

*****************************
Arduino Uno (Not recommended)
*****************************

|conductor|

**As of version 5.4.0, this is no longer a recommended option, see :doc:`/news/posts/20240328`**

If you already have an Uno, or will use |JMRI| to control your trains, then by all means use an Uno. Just remember that you can't have WiFi, Ethernet or a few other options due to memory limitations. But as a Command Station connected to |JMRI| with a USB cable it works great.

.. image:: /_static/images/microcontrollers/uno.png
   :alt: Arduino Uno R3
   :scale: 75%

Setting up the UNO is essentially the same as setting up a Mega, so refer to the :doc:`/ex-commandstation/get-started/assembly` page for information on setting up this microcontroller.

.. warning:: 

    **Uno R4 is not supported** |BR| If you choose to purchase an Arduino Uno, it is vital that you purchase the **Revision 3 (R3)** version, :dcc-ex-red-bold:`not` the **Revision 4 (R4)** version.  The |EX-CS| :dcc-ex-red:`cannot run` on the R4 version.  :doc:`See here from more information</news/posts/20230728>`.
