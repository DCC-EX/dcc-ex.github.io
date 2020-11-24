Wifi Configuration
==================

**work in progress**

This page describes the software configuration options for using WiFi to connect your Command Station wirelessly to JMRI or a WiFi throttle like Engine Driver. For information on how to connect your hardware, go to `WiFi Setup <../get-started/wifi-setup.html>`_

Wireless Connections
--------------------

As mentioned in `WiFi Setup <../get-started/wifi-setup.html>`_, there are two main reasons for wanting to use WiFi; to connect to JMRI without a USB cable, or to connect to a WiThrottle controller like the Engine Driver mobile app. In addition, you have two options for connecting your WiThrottle Controller to your Command Station. If you are using JMRI, you can leave your CS connected to the JMRI computer via the USB cable and connect your Controller via WiFi to the WiThrottle server running on the JMRI computer. If you don't need JMRI or just want to connect your WiFi Controller directly to the CS, then you connect to the WiThrottle Server running on your CS.

What's a "WiThrottle Server"?
-----------------------------

WiThrottle stands for "WiFi Throttle" and a "WiThrottle Server" is just software running on your JMRI computer or on the DCC-EX Command Station. It's called a "server" because it allows you to connect to it and it "serves" or provides service to you via another application. That application is called a "Client". So your throttle in this case is the client.

WiThrottle itself is a standard for how WiFi throttles can communicate with Command Stations much like the DCC standard is a standard for how data packets are communicate to decoders. What this means for you, is that any device that is WiThrottle compatible should work with DCC-EX.

AP Mode vs. Station Mode
------------------------

There are two ways to setup the Wifi chip connected to DCC++: "Access Point Mode" (aka "AP MODE) and "Station Mode". We often abbreviate the latter to "STA". You will also see people refer to it as "Client Mode". 

In AP mode the tiny ESP chip acts as a very basic Wifi base and provides a small IP network for your throttle and maybe your computer with JMRI only. In this mode there is no connection to the Internet for any of the devices only connected to the AP of the ESP chip.

In STA (Client) mode the ESP chip uses an existing (home) Wifi network and connects to that along with all the other devices you might have in your home. If you have a stable Wifi network where you place your Command Station this is a good choice because the Wifi Station of your home network is normally better in managing all devices and the frequencies involved in runnung a stable Wifi network that the ESP chip.

We will focus on how to connect a Throttle to the Command Station. For info on using WiFi with JMRI, click here **missing link**

AP Mode
^^^^^^^

If there is no exising Wifi or the Wifi is still unconfigured, the default for DCC-EX is AP mode. In this mode, your CS acts like an AP. In other words, it acts just like any other wireless router you could connect to. The router in your home is in effect, an AP. Using the CS in AP mode allows you to have to separate network so you can keep your layout network separate from your home network. If you travel to shows or take your setup to a friend's house, this allows for an autonomous, transportable system that does not need a connection to and hopefully will not interfere with, other networks. See **dealing with interference (missing link)**

Station Mode (STA Mode)
^^^^^^^^^^^^^^^^^^^^^^^

Station mode allows you to connect the Command Station to your existing home network. The CS becomes a Station or Client rather than an AP. That means instead of being an AP which manages the IP of the smartphone that contains your Throttle, it becomes a station that connects to your existing network. The Throttle then connects to the CS by finding its IP address on the network.

Default Operation - AP Mode (No Configuration Necessary)
--------------------------------------------------------

To use the default AP mode, you don't have to do anything other than connect an ESP8266 board as described in `WiFi Setup <../get-started/wifi-setup.html>`_. That's it! We find your device, no matter which of the extra serial ports you attached it to and create a WiThrottle server running and waiting for you to connect to. All you need to know is the IP address assigned by the WiFi board and the port to communicate through. You can find this using the Arduino Serial Monitor.

Whenever you connect a USB cable and open the serial monitor, you reset the program running on your CS. It will go through the bootup sequence and try to connect to a network. If you did not setup a "Station Mode" configuration, or if that network is not in range, it will configure itself in AP mode. You will see this process by watching the serial monitor log window. Here are the important lines you need to look for. While the IP address is almost always 192.168.4.1, it could be different on your system. You are looking for the items in the blue box below that are highlighted in red

.. image:: ../_static/images/wifi/ap_mode1.jpg
   :alt: IP Address

**Figure 1** - Serial Monitor Log

You will see the line that has ``AT+CIPSERVER=1,2560\r\r\nno change\r\n\r\nOK\r\n``, where 2560 is your port number

Next you will see ``+CIFSR:APIP,"192.168.4.1"``, where your IP address is 192.168.4.1.

AP IP here stands for "Access Point IP Address". Your throttle is assigned an IP in the same IP range, typically 192.168.4.10 to 15. As in this case your AP is at the same time your DCC-EX CS, you connect your throttle to the AP IP. Remember to enter it correctly into your WiFi Throttle when you configure that later.

Once you see an AP IP Address and see ```++ Wifi Setup OK ++`` at the bottom of the log (it may take a few seconds for the CS to complete the configuration), you can connect to it. See the next section.

Connecting to the AP
^^^^^^^^^^^^^^^^^^^^

There are two steps to get you running trains with your WiFi throttle, the first is to connect to the AP instead of your home network, the second is to connect your throttle to the AP.

On your mobile device, go into your WiFi settings that same way you would to connect to your home router. Look for another network to connect to. You should see a new network that begins with "DCCEX" like this: ``DCCEX_6e321b``

Note that the last 6 letters and numbers will be specific to your WiFi board and uniquely identify it.

Simply click on that network and connect to it. Ignore the warning that may popup telling you that "Internet may not be available". The CS is not connected to the internet and you are connecting your mobile device directly to it. Depending on the config and OS of your device you may still have Internet over mobile data through a cell tower connection. If you wish to use your home network internet (for example if your data plan is expensive), turn off mobile data and see the section below on Station Mode to connect using your home network instead.

Once you are connected to the CS, you can run your WiFi Throttle program, enter the IP Address for the Server Address, 2560 for the Port number, and then select and acquire your loco by its address.

Connecting to your Network - Station Mode (edit config.h)
---------------------------------------------------------

In order to connect to your home network, you must open the config.h file in a text editor and enter your login credentials or you have already entered your credentials via the installer. The easiest way to do this is to use the Arduino IDE and open the project. Look for these lines in the file:

.. code-block::

   /////////////////////////////////////////////////////////////////////////////////////
   //
   // NOTE: Only supported on Arduino Mega
   // Set to false if you not even want it on the Arduino Mega
   //
   #define ENABLE_WIFI true

   /////////////////////////////////////////////////////////////////////////////////////
   //
   // DEFINE WiFi Parameters (only in effect if WIFI is on)
   //
   #define WIFI_SSID "Your network name"
   #define WIFI_PASSWORD "Your network passwd"
   #define WIFI_HOSTNAME "dccex"

Figure 2 - Station Mode Configuration

First, make sure that the #define ENABLE_WIFI true line is not commented out. two slashes ``//`` in front of a line make it a comment and not a line of code

Next, enter your network information into the WIFI_SSID, WIFI_PASSORD and WIFI_HOSTNAME fields. Here is an example:

.. code-block::

   #define WIFI_SSID "JonesFamily"
   #define WIFI_PASSWORD "Secret!2020"

We recommend leaving WIFI_HOSTNAME to "dccex", but you can change it if you like. If your ESP8266 WiFi board has a later version of firmware, that can allow you to connect using this name instead of the IP address. In other words, it allows that name to be an alias for the IP address.

Resetting Network Settings
--------------------------

Once you enter a network SSID and password, the CS will always try to connect to it, even after removing the power and restarting. If you want to connect in AP mode, or your network credentials change, or you need to connect to a different network, you simply need to tell your WiFi board to clear the settings.

Go into your serial monitor and wait until the CS has gone through the startup sequence. Then in command textbox enter ``+CWQAP``

and press "SEND".

You will then see an "Ok" message. The WiFi Settings are forgotten. However, if your config.h has WiFi Credentials in it, then as soon as your CS restarts, it will load and save those settings again. So...

If you want to run in AP mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Edit the config.h, remove your SSID and password, and then upload the project into the CS

If you want to change your network login
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Edit the config.h file, change your SSID and password, and then upload the project into the CS

Disabling WiFi
--------------

Edit the config.h file. Comment out the line ``#define WIFI_ENABLE true`` by adding two forward slash marks (``//``). Then upload the project back to the CS.
