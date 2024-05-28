.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-hardware.rst
|EX-REF-LOGO|

***********
WiFi Boards
***********

|conductor| |tinkerer| |engineer| |support-button|

You can connect up to 5 WiFi throttles. For the standard Mega board, we recommend the Conductor-Friendly Makerfabs WiFi shield below. Keep in mind you can also purchase a Mega+WiFi board online that has both a Mega clone and an ESP8266 built onto the same board. However, you will have to upload new firmware to that board, so that would be a Tinkerer option. See the :doc:`Mega+WiFi page </reference/hardware/wifi-boards/mega-wifi>`

.. warning:: 

   While the recommended :doc:`Makerfabs ESP8266 WiFi Shield </reference/hardware/wifi-boards/makerfabs-esp8266>` is now shipping with the correct firmware version and **will work** with |EX-CS| *without modification*, please be aware that the Espressif firmware shipped with *Duinopeak ESP8266 WiFi Expansion* and *ESP-01 or ESP-01S* devices :dcc-ex-red-bold:`will probably NOT work` with |EX-CS| out of the box.

    See :doc:`/support/wifi-at-version` for details on how to check the version and how to correct it if needed.

For more information on how to configure your Command Station to use the boards below, see :doc:`Wifi Setup </ex-commandstation/get-started/wifi-setup>`

.. toctree::
    :maxdepth: 1

    /reference/hardware/wifi-boards/ex-wifi-shield-8266
    /reference/hardware/wifi-boards/makerfabs-esp8266
    /reference/hardware/wifi-boards/duinopeak-esp8266
    /reference/hardware/wifi-boards/esp-01
    /reference/hardware/wifi-boards/wangtongze-board
    /reference/hardware/wifi-boards/mega-wifi
    /reference/hardware/wifi-boards/sparkfun-thing-plus
    /reference/hardware/wifi-boards/esp32-ant-01
    /reference/hardware/wifi-boards/hc12-bridge

.. NOTE:: This is NOT to make a connection to |JMRI|. Use a USB cable instead. The WiFi and Ethernet solutions are designed to allow throttles to connect directly to the |EX-CS| without the need for any other software such as |JMRI|. While using a WiFi/Ethernet connection to |JMRI| will work, the overhead required internally will slow performance, take up valuable system memory, and prevent broadcast messages for sensors and power state.
