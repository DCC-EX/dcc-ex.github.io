.. include:: /include/include.rst
.. include:: /include/include-l3.rst
|EX-REF-LOGO|

*************************************************
Using Bluetooth with your ESP32 EX-CommandStation
*************************************************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
      :depth: 2
      :local:

For users wishing to use an ESP32 as their |EX-CS|, it is possible to utilise the built-in Bluetooth as the connection method.

The BT on ESP32 is not the primary Serial, so it will not receive debug output and is not intended to be a replacement for the USB (at least not how it is implemented now)
You need to enable SERIAL_BT_COMMANDS in config.h
You need to compile with >=2MB APP partitioning

You need to tell your device to pair to the BT named DCCEX-hexnumber
You need to tell the app (or whatever) to use the paired device


// BLUETOOTH SERIAL ON ESP32
// On ESP32 you have the possibility to use the builtin BT serial to connect to
// the CS.
//
// The CS shows up as a pairable BT Clasic device. Name is "DCCEX-hexnumber".
// BT is as an additional serial port, debug messages are still sent over USB,
// not BT serial.
//
// If you enable this there are some implications:
// 1. WiFi will sleep more (as WiFi and BT share the radio. So WiFi performance
//    may suffer
// 2. The app will be bigger that 1.2MB, so the default partition scheme will not
//    work any more. You need to choose a partition scheme with 2MB (or bigger).
//    For example "NO OTA (2MB APP, 2MB SPIFFS)" in the Arduino IDE.
// 3. There is no securuity (PIN) implemented. Everyone in radio range can pair
//    with your CS.
//
//#define SERIAL_BT_COMMANDS