.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-cs.rst
|EX-CS-LOGO|

*********************************
Supported WiFi Shields and Boards
*********************************

|tinkerer| |engineer|

:dcc-ex-red-bold:`Please read the warning before you proceed.`

.. warning:: 
   :class: warning-float-right

   Please be aware that the Espressif firmware shipped with these devices **will probably NOT work** with |EX-CS| out of the box.

   This can be corrected, but is probably beyond Conductor level and requires additional hardware.  

   See :doc:`/support/wifi-at-version` for details on how to check the version and how to correct it if needed.

   We are currently investigating other options.
   
The following pages describe all the supported WiFi options of the |EX-CS|.  If you identify as a |conductor-text| and have installed only the recommended hardware we suggest that you look at the guide on the :doc:`/ex-commandstation/get-started/wifi-setup` page.

Supported devices    
-----------------

.. toctree::
    :maxdepth: 1

    /reference/hardware/wifi-boards/makerfabs-esp8266
    /reference/hardware/wifi-boards/duinopeak-esp8266
    /reference/hardware/wifi-boards/esp-01
    /reference/hardware/wifi-boards/mega-wifi

|hr-dashed|

See also    
--------

.. toctree::
   :maxdepth: 1

   wifi-config
   /support/wifi-at-version
