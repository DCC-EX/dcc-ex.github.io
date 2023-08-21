.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-hardware.rst
|EX-REF-LOGO|

*************************************************
Using Bluetooth with your ESP32 EX-CommandStation
*************************************************

|tinkerer| |engineer|

For users wishing to use an ESP32 as their |EX-CS|, it is possible to utilise the built-in Bluetooth as the connection method.

To enable Bluetooth support on the there are some important considerations to take into account:

- WiFi performance may suffer as Bluetooth and WiFi share the same radio
- The app will be bigger than 1.2MB, so the default partition scheme will not work any more, meaning you need to choose a partition scheme with at least 2MB (For example "NO OTA (2MB APP, 2MB SPIFFS)" in the Arduino IDE)
- There is no security (PIN) implemented, so anyone within radio range can pair with the |EX-CS|

The Bluetooth interface on ESP32 is not the primary serial interface, so it will not receive debug output and is not intended to be a replacement for the USB interface.

You will need to enable ``SERIAL_BT_COMMANDS`` in your "config.h" file:

.. code-block:: 

  #define SERIAL_BT_COMMANDS

When pairing with the ESP32 Bluetooth device, it will appear as a pairable classic Bluetooth device with a device name "DCCEX-<hex number>".

Once paired, you will need to configure your throttle or controller application to use the paired device.