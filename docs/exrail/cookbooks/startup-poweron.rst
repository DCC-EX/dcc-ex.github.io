.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Startup power
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

By default the Command station will start with the track power OFF.

This can be inconvenient if you are using the free version of the |WiThrottle| app from the Apple store which does not have a power button.

You can configure |EX-R| to power on at startup by using

.. code-block:: cpp
  
    AUTOSTART POWERON DONE

Alternatively, you can power tracks individually

.. code-block:: cpp
  
    AUTOSTART
      SET_POWER(A,ON)
      SET_POWER(D,ON)
    DONE
