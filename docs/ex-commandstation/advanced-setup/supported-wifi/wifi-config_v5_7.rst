:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-cs.rst
|EX-CS-LOGO|

************************************
WiFi Configuration for version 5.7+
************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

.. sidebar:: 
   :class: sidebar-on-this-page

   .. contents:: On this page
      :depth: 2
      :local:

This page is exclusively for users of |EX-CS| version 5.7.0 and later. Version 5.7.0 is currently in the experimental / development (DEVEL) phase and is not recommended for general users.

If you are using an earlier version, please see :doc:`WiFi Config  <wifi-config>`. 

Also see `WiFi configuration (CSB1 or ESP32 ONLY) <https://dcc-ex.com/mkdocs-test/products/ex-commandstation/config-wifi-esp32/#configuring-the-host-name>`_ on the new web site for more technical information.


Background
===========

Prior to version 5.7.0, WiFi configuration for |EX-CS| was done through options in the ``config.h`` file. This method required users to modify the firmware source code and recompile it for their specific WiFi settings, which could be cumbersome and error-prone.

From version 5.7.0, config.h options for WiFi configuration in ``config.h`` ignored by CSB1 or ESP32 EX-CommandStations.  

It is now necessary to use the new WiFi configuration method, which involves connecting to the |EX-CS| *after you have flashed the firmware.*  You do so by connecting to the |EX-CS| via USB or by connecting to the WiFi Access Point network of the CS. (Note that the WiFi Access Point network approach has limitations.)

The advantage of this is that it is independent of the flashing process, and will remember your WiFi settings across firmware updates and changes.

You can configuring WiFi settings through:

a) |EX-WT| (via USB),
b) |EX-TB| (via USB or over WiFi),
c) the serial monitor / device monitor of |EX-I|, the **Arduino IDE** or **VSC** (via USB)
d) any wifi throttle or app that can send the appropriate commands to the |EX-CS| over WiFi 

|EX-WT| and |EX-TB| provide a user-friendly interface for configuring WiFi settings, while the serial monitor method allows for more direct access to the configuration process but requires more technical knowledge.

The different modes
====================

WiFi on the |EX-CS| has two operating modes:

* **Access point (AP) mode** means the Command station acts as its own private WiFi network so throttle devices must connect first to the Command Station WiFi network.

* **Station (STA) mode** means the command station connects to your WiFi router and appears as a device on that network. If the WiFi is configured for STA mode, but fails to connect to your router, it will fall back to AP mode in much the same way as smart plugs, lights etc.

The are some additional settings that are not modes but effect the wifi connection:

* **Hidden AP mode**: When enabled, the Command Station's WiFi network will not be visible in the list of available networks on devices. This can enhance security by making it less obvious to potential attackers, but it also means that users will need to manually enter the network name (SSID) to connect.

* **Temporary STA mode**: When enabled, the Command Station will start in Station mode and connect to an existing Wifi network. But will forget this setting the next time the |EX-CS| is restarted.

* The **HOSTNAME** setting allows you to set the name that appears in you Throttle app, once you have connected to the appropriate network for the Command Station.

Accessing via USB vs WiFi
==========================

Only **Station (STA) mode** and the **HOSTNAME** can be changed over WiFi. 

**Access Point (AP)** mode changes require a serial/USB connection.

----

Changing the settings
======================

EX-WebThrotttle
-----------------

1. Connect your PC to the |EX-CS| via USB. Open the |EX-WT| and select the appropriate COM port for your |EX-CS|. You should see the current WiFi settings displayed in the interface.  See :doc:`EX-WebThrottle </ex-webthrottle/index>` for more details.

2. Go to the ``Wifi Setup`` page from the menu or the toolbar buttons.

   - To set the **Access Point (AP) mode**, enter the SSID and password for the Command Station's WiFi network and click the :guilabel:`Set Access Point` button. You can optional set a channel for the AP mode, but it is not required, and generally not recommended.
   
      The Command Station will restart and create its own WiFi network with the specified SSID and password.

      To set the **Station (STA) mode**, enter the SSID and password for your existing WiFi network (eg your home router) and click the :guilabel:`Set Station Mode` button. The Command Station will attempt to connect to the specified WiFi network. If the connection is successful, it will operate in Station mode. If the connection fails, it will revert to Access Point mode.

   - To set the **Temporary Station (STA) mode**, enter the SSID and password for your existing WiFi network and click the :guilabel:`Set Temporary Station Mode` button. The Command Station will attempt to connect to the specified WiFi network. If the connection is successful, it will operate in Station mode. If the connection fails, it will revert to Access Point mode.

   - To set the **Hostname**, enter the desired hostname and click the :guilabel:`Set Hostname` button. The Command Station will update its hostname, which will be visible in your Throttle app when connected to the appropriate network.

In every case above, the Command Station will restart to apply the new settings. You will need to reconnecting to the Command Station in the |EX-WT| interface.

**Resetting the Wifi settings**

The :guilabel:`Reset WiFi Settings` button on the WiFi Setup page will reset all WiFi settings to their default values. This will cause the Command Station to restart and create its own WiFi network in Access Point mode with the default SSID and password.

----

EX-Toolbox
-----------------

|EX-TB| provides a similar interface to the |EX-WT| for configuring WiFi settings, but it can be accessed either via USB or over WiFi. The process for changing WiFi settings in the |EX-TB| is essentially the same as in the |EX-WT|, with the same options for AP mode, STA mode, Temporary STA mode and Hostname. 


1. Connect your PC to the |EX-TB| via USB or Wifi.  See :doc:`EX-Toolbox </ex-toolbox/using>` for more details.

2. Go to the ``WiFi Setup`` page from the menu or the toolbar buttons and follow the same steps as outlined for the |EX-WT| above.

Note: Only **Station (STA) mode** and the **HOSTNAME** can be changed over WiFi. **Access Point (AP) mode** changes require a USB connection.

In every case above, the Command Station will restart to apply the new settings. You will need to reconnecting to the Command Station in the |EX-TB| interface.

----

EX-Installer, Arduino IDE, VSC, throttle apps
----------------------------------------------

The process for configuring WiFi settings using the serial monitor or device monitor on any of the EX-Installer, Arduino IDE, VSC or WiFi throttle apps are esentially the same.

In every case below, the Command Station will restart to apply the new settings. You will need to reconnecting to the Command Station in the app's interface.

Changing to Station Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~

i.e. your home router.  You will need to issue the command:

.. code-block:: cpp

   <C WIFI "routerSSID" "routerPassword">

e.g. Sets the STA mode to connect to a router with SSID "routerSSID" and password 

The command station will attempt to connect to this network immediately, and on each rerstart. If it fails to connect, it will revert to AP mode.

Changing the Access Point settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To give the Access point a specific name and a password that will not be revealed on the OLED use the command:

.. code-block:: cpp

   <C WIFI AP "MyCSB1" "SpamWonderfulSpam">

e.g. Sets the AP name to "MyCSB1" and the password to "SpamWonderfulSpam":

The AP mode password must be at least 8 characters long.

The default channel is set to "11". If you need to use an alternate channel (we recommend using only 1,6, or 11) you may change it with the command:

.. code-block:: cpp

   <C WIFI AP "MyCSB1" "SpamWonderfulSpam" 6>

Use a phone WiFi analyser app to see which channels are relatively quiet in your area. 

Hidden Access Point mode
~~~~~~~~~~~~~~~~~~~~~~~~~~

In some environments you may want to hide the SSID from phones scanning for access points. If you do hide the SSID, it is still possible to connect by entering the SSID manually on the phone/tablet.

.. code-block:: cpp

   <C WIFI HIDDENAP "MyCSB1" "SpamWonderfulSpam" 6>

Configuring the Host Name
~~~~~~~~~~~~~~~~~~~~~~~~~~

The default hostname "DCCEX" but you can change this if you have more than one CS on your network to make them show up with different names. Host names containing "DCCEX" are more readily found by WiFi throttles. 

.. code-block:: cpp
   
   <C WIFI HOSTNAME "DCCEX-MYCSB1">

e.g. Sets the hostname to "DCCEX-MYCSB1":

Clearing WiFi settings
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: cpp

   <C WIFI DEFAULT>

WiFi will revert to the internally generated ssid and password.