*******************
Wifi Configuration
*******************

This page describes the software configuration options for using WiFi to connect your Command Station CS wirelessly to JMRI or a wireless throttle like Engine Driver. For information on how to connect your hardware, go to `WiFi Setup <../get-started/wifi-setup.html>`_

As mentioned in the above link, you will need the following to proceed:

* A DCC++ EX Command station with Motor Controller
* A WiFi board (for Blutooth configuration, click here ***TODO: link to bluetooth***

For a video click `Setting up WiFi <https://www.youtube.com/watch?v=N6TWR7fIl0A&t=5s>`_

   .. raw:: html

      <iframe width="336" height="189" src="https://www.youtube.com/embed/N6TWR7fIl0A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Wireless Connections
=====================

As mentioned in `WiFi Setup <../get-started/wifi-setup.html>`_, there are two main reasons for wanting to use WiFi; to connect to JMRI without a USB cable, or to connect to a wireless controller like the Engine Driver mobile app. While it can work to simply use WiFi to replace the USB cable to connect the computer running JMRI to your CS, there are better ways and frankly, your electronics are usually under the benchwork, so just buy the right sized cable. But if you have no alternative and need to replace the cable with wireless, we recomend the HC-12 serial wireless bridge boards which we cover in ***TODO: Link here***.

That said, there are two main wireless technologies that let you send commands to your CS and control your trains:

* WiFi
* Bluetooth

Your particular controller hardware (a separate controller or your cell phone) may be able to use one, the other or both depending on the controller you choose. This tutorial covers WiFi configuration, for Bluetooth, click here ***TODO:Insert link here***

Connection Type: Direct to Command Station or through JMRI
============================================================

Everything on this page seems to come in twos. You have two options for connecting your controller to your CS depending on its capabilities and your preferences:

* Connect directly to DCC++ EX using WiFi or BlueTooth (JMRI not required but optional)
* Connect to DCC++ EX through JMRI with the USB cable and connect a WiThrottle compatible throttle to JMRI's WiThrottle Server via WiFi

If you don't need JMRI or just want to connect your wireless Controller directly to the CS, then you connect to the CS using a WiFi or BlueTooth device that speaks either the <DCC++> command language or the WitThrottle command language. 

For example, Engine Driver uses the WiThrottle protocol so can connect either directly to the CS via WiFi or indirectly through the JMRI computer that has WiFi and its own WiThrottle Server. DCCpp CAB can connect directly to DCC++ EX via WiFi or Bluetooth and sends native <DCC++> commands.

What's a "WiThrottle Server"?
==============================

WiThrottle stands for "WiFi Throttle" and a "WiThrottle Server" is just software running on your JMRI computer or on the DCC-EX Command Station. It's called a "server" because it allows you to connect to it and it "serves" or services requests from another application. That application is called a "Client". So your throttle in this case is the client.

WiThrottle itself is a standard for how WiFi throttles can communicate with Command Stations much like the DCC standard is a standard for how data packets communicate with decoders. What this means for you, is that any device that is WiThrottle compatible should work with DCC-EX. Also, any device that sends <DCC++> commands should work with DCC++ EX.

Access Point Mode vs. Station Mode
===================================

There are two ways to configure the Wifi board connected to DCC++ EX: "Access Point Mode" (aka "AP MODE") and "Station Mode". We often abbreviate the latter to "STA". You will also see people refer to it as "Client Mode".

AP Mode
--------

In AP mode the tiny ESP-WiFi chip acts as a very basic Wifi server and provides a small IP network for your throttle or for your computer running JMRI and WiThrottle. It acts much like your router does to let things connect directly to it (currently up to four connections). Using the CS in AP mode allows you to have a separate network so you can keep your layout network separate from your home network. This is the simplest way to enable a connection for a WiFi throttle.

If you travel to shows or take your setup to a friend's house, this allows for an autonomous, transportable system that does not need a connection to and hopefully will not interfere with, other networks. 

NOTE: In this mode there is no connection to the Internet for any of the devices that are only connected to the AP. It simply provides a private network to allow a direct connection to your throttles.

(Remember you can click on images to enlarge them)

.. figure:: ../_static/images/wifi/Wifi_softap_mode.png
   :alt: AP Mode
   :scale: 50%

   Figure 1: Access Point Mode - Things connect to the WiFi Board

Station Mode
-------------

Station mode allows you to connect the Command Station to your existing home network. The CS becomes a Station or Client rather than an AP. That means instead of being a host that manages the IP of the smartphone that runs your Throttle, it becomes a station that connects to your existing network just like any of the other computers or devices connected to your network. The Throttle then connects to the CS by finding its IP address on the network. You will have to find what IP address is assigned to the CS (see below). Alternately, you can define a static IP address in your router to assign to the CS.

.. figure:: ../_static/images/wifi/Wifi_station_mode.png
   :alt: Station Mode
   :scale: 50%

   Figure 2: Station Mode - Things connect to the router and find the WiFi board by its IP

Images are courtesy of, and you can find a great tutorial on WiFi by `NodeMCU <https://nodemcu.readthedocs.io/en/latest/modules/wifi/>`_

We will focus on how to connect a Throttle to the Command Station. For info on using WiFi with JMRI, click here **TODO:Add link***.


Default Operation - AP Mode (No Configuration Necessary)
=========================================================

To use the default AP mode, you don't have to do anything other than connect an ESP8266 board as described in `WiFi Setup <../get-started/wifi-setup.html>`_. 

That's it! If there is no previously configured network in range or the Wifi setup in your config.h file is still unconfigured, the default for DCC-EX is AP mode. We find your Wifi board, no matter which of the extra serial ports you attached it to. DCC++ EX then accepts commands from WiFi throttles in either WiThrottle or <DCC++> format.

To see other configuration options you can set in your config.h file, see `WiFi Config Options`_ below.

You will need to know:

* The IP address assigned by the WiFi board (Usually **192.168.4.1**)
* The port to communicate through. (**port 2560** unless you change it in your config.h file)
* The SSID or Server name to connect to (**DCCEX_xxxxxx** where the x's are the last 6 digits of your MAC
* The password (Unless you change it in config.h, to your local SSID password.)  It's default is **PASS_xxxxxx** where the x's are the last 6 digits of your MAX

.. Note:: All of this information is displayed in the startup log if you connect the CS to a serial monitor. The IP and port also appear on the optional LCD or OLED display.

Whenever you connect a USB cable and open the serial monitor, you reset the program running on your CS. It will go through the bootup sequence and try to connect to a network. If you did not setup a "Station Mode" configuration, or if that network is not in range, it will configure itself in AP mode. You will see this process by watching the serial monitor log window. Here are the important lines you need to look for. While the IP address is almost always 192.168.4.1, it could be different on your system. You are looking for the items in the blue box below that are highlighted in red. 

.. image:: ../_static/images/wifi/ap_mode1.jpg
   :alt: IP Address
   :scale: 80%

**Figure 1** - Serial Monitor Log (click to enlarge)

You will see the line that has ``AT+CIPSERVER=1,2560\r\r\nno change\r\n\r\nOK\r\n``, where 2560 is your port number

Next you will see ``+CIFSR:APIP,"192.168.4.1"``, where your IP address is 192.168.4.1.

APIP here stands for "Access Point IP Address". Your throttle is assigned an IP in the same IP range, typically 192.168.4.10 to 15. As in this case your AP is at the same time your DCC-EX CS, you connect your throttle to the AP IP. Remember to enter IP xxx.xxx.x.xx and port xxxx numbers correctly into your WiFi Throttle when you configure that later.

You will also see your SSID and Password in the log.

Once you see an AP IP Address and see ```++ Wifi Setup OK ++`` at the bottom of the log (it may take a few seconds for the CS to complete the configuration), you can connect to it. See the next section.

Connecting to the Access Point 
----------------------------------

There are two steps to get you running trains with your WiFi throttle, the first is to connect to the AP instead of your home network, the second is to connect your throttle to the AP.

On your mobile device, go into your WiFi settings that same way you would to connect to your home router. Look for another network  name to connect to. 
You should see a new network that begins with "DCCEX" like this example: ``DCCEX_6e321b``. Remember those last 6 digits.

Simply click on that network and connect to it on your mobile device. You will need to enter the password you specified in the config.h file. If you did not enter one, the default will be **PASS_xxxxxx** where "xxxxxx" are the same last 6 digits of your device's MAC address displayed in the SSID like this example:
``PASS_6e321b``

.. Note:: The last 6 letters and numbers of your AP name and default password will be specific to your WiFi board and uniquely identify it. They are the last 6 letters of that device's MAC address. You can always find it in the log or by simply looking at the DCCEX_xxxxxx SSID name in your list of available networks.

Ignore the warning that may popup telling you that "Internet may not be available". The CS is not connected to the internet, you are connecting the CS directly to your mobile device. Depending on the config and OS of your mobile device you may still have Internet over mobile data through a cell tower connection. If you wish to use your home network internet (for example if your data plan is expensive), turn off mobile data and see the section below on Station Mode to connect using your home network instead.

Once you are connected to the CS, you can run your WiFi Throttle program, enter the IP Address for the Server Address (**the default is usually 192.168.4.1, but it will be displayed in your serial monitor log if you are unsure**), enter **2560 for the port number**, and then select and acquire your loco by its address. If you don't know your loco address, see the ``<R>`` command in the `Decoder Test <../reference/software/command-reference.html#decoder-test>`_ section of the Command Reference. 

Note: Your Mobile Throttle function keys are user defined default function keys and Not the function keys you used in either JMRI or Rockrail engine roster function keys.

**Once again:**

* IP Address - Normally 192.168.4.1
* Port Number - 2560
* Server Name - DCCEX_123456 where the last 6 characters are unique to your WiFi device
* Server Password - PASS_123456 where the last 6 charaters are the same as above

**All this information appears in the startup log if you are connected using a serial monitor in case you forget.**

.. Note:: If you experience dropped connections to the AP, turn off the auto-connect feature on your phone to prevent it from randomly disconnecting from the AP and connecting to your home router because it thinks it's a better connection. You can also "forget" the connection it wants to switch to and then manually connect to that network when you need it.


Connecting to your Network - Station Mode "STA" (edit config.h)
==================================================================

In order to connect to your home network, you must open the config.h file in a text editor and enter your login credentials or you have already entered your credentials earlier via the automated exInstaller. The easiest way to do this other than the installer is to use the Arduino IDE and open the project.
Look for these lines in the file:

.. code-block::

   /////////////////////////////////////////////////////////////////////////////////////
   //
   // NOTE: Only supported on Arduino Mega
   // Set to false if you do not want it even on the Arduino Mega
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

Save your config.h file and upload the sketch to your CS.

WiFi Config Options
====================

The following defines are all the possible network settings found the config.h file. If you used the automated installer, you may see a few of these already listed. If you do a manual Arduino IDE install, you will see all of these in the file you renamed from "config.example.h" to "config.h".

| :ref:`#define IP_PORT 2560`
| :ref:`#define ENABLE_WIFI true`
| :ref:`#define DONT_TOUCH_WIFI_CONF`
| :ref:`#define WIFI_SSID "Your network name"`
| :ref:`#define WIFI_PASSWORD "Your network passwd"`
| :ref:`#define WIFI_HOSTNAME "dccex"`
| :ref:`#define WIFI_CONNECT_TIMEOUT 14000`
| :ref:`#define ENABLE_ETHERNET true`
| :ref:`#define IP_ADDRESS { 192, 168, 1, 200 }`
| :ref:`#define MAC_ADDRESS {  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xEF }`

#define IP_PORT 2560
--------------------
**Default: 2560** - This is the port used to communicate with the WiFi board or Ethernet Shield. We use the default value of 2560 because that is the port JMRI uses. You can change this value if you would prefer it to be something else. You will need to enter this in sofware like Engine Driver in order to connect to the CS via networking.

#define ENABLE_WIFI true
------------------------
**Default: true** - WiFi is supported only on a Mega. If you do not wish to use WiFi and want to save boot time by not having the Mega check for a WiFi board each time, you may set this to "false"

#define DONT_TOUCH_WIFI_CONF
----------------------------
**Default: commented out** If uncommented, this tells the CS to NOT process any WiFi commands in the CS. If other WiFi defines are enabled, the CS will ignore them. With this command, you can leave #define ENABLE_WIFI true so that networking is active, but send no configuration commands to ESP8266. This allows you to enter your own AT commands to set up your Wifi however you want. To do this, you would enter <+> commands in the serial monitor or add code to send these commands automatically.

#define WIFI_SSID "Your network name"
--------------------------------------
**Default: "Your network name"** - To connect to your CS as an AP (Access Point), do not change this setting. If you wish to connect to your home network instead, enter the SSID (network name) for that network. If you do NOT set the WIFI_SSID, the WiFi chip will first try to connect to the previously configured network and if that fails fall back to Access Point mode. The SSID of the AP will be automatically set to DCCEX_xxxxxx, where xxxxxx is the last 6 digits of the MAC address for the WiFi chip.
Your SSID may not contain ``"`` (double quote, ASCII 0x22).

#define WIFI_PASSWORD "Your network passwd"
--------------------------------------------
**Default: "Your network passwd"** - WIFI_PASSWORD is the network password for your home network or if you want to change the password from default AP mode password to the AP password you want.  Your password may not contain ``"`` (double quote, ASCII 0x22).  
If you don't change this setting and start up in AP mode instead, the default password is PASS_xxxxxx where xxxxxx is the last 6 digits of the MAX address for your ESP board.


#define WIFI_HOSTNAME "dccex"
-----------------------------
**Default: "dccex"** You would normally not want to change this, it is the host name that will appear in the list of available networks that a device you want to connect to DCC-EX will display. It helps you know which device is your Command Station.

#define WIFI_CONNECT_TIMEOUT 14000
-----------------------------------
**Default: 14000 milliseconds (14 seconds)** - You only need to set this if you have an extremely slow Wifi router and the response to the connection request takes longer than normal.

#define ENABLE_ETHERNET true
-----------------------------
**Default: commented out** - Uncomment this line if you with to use an Ethernet Shield {cable}, (not WiFi, see above for that). You will also need to install the Arduino Ethernet Library on whatever development environment you use to compile and upload your sketch.

#define IP_ADDRESS { 192, 168, 1, 200 }
----------------------------------------
**Default: commented out** - Uncomment this line if you wish to use a static IP address, otherwise the CS will use DHCP to automatcally assign an IP address from your router. If you use a static IP, you will also have to configure this IP in your router.

#define MAC_ADDRESS {  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xEF }
------------------------------------------------------------
**Default: commented out** - This is for Ethernet only! Ethernet shields do not normally come with a defined MAC address. We give you two and you can uncomment the one you prefer. You can also choose any other validly formatted MAC address that will not conflict with any devices already on your network.


Resetting Network Settings
===========================

Once you enter a network SSID and password, the CS will always try to connect to it, even after removing the power and restarting. If you want to connect in AP mode, or your network credentials change, or you need to connect to a different network, you simply need to tell your WiFi board to clear the settings.

Clearing the ESP-WiFI SSID Settings
------------------------------------
Go into your serial monitor and wait until the CS has gone through the startup sequence. 
Then in command textbox enter ``<+RESTORE>``
and press "SEND".

You will then see an "Ok" message. The WiFi Settings are forgotten. However, if the last config.h used when you uploaded it to the CS had WiFi Credentials in it, then as soon as your CS restarts, it will load and save those settings again. So...

If you want to run in AP mode
------------------------------

Edit the config.h, change your SSID name, and password lines back to default. It MUST look like the following. If it is anything else it will try to login with whatever you type there as credentials!:

.. code-block::

    #define WIFI_SSID "Your network name"
    #define WIFI_PASSWORD "Your network passwd"

Then upload the project into the CS

If you want to change your network login
------------------------------------------

Edit the config.h file, change your SSID and password to your new credentials, and then upload the project into the CS


Disabling WiFi
===============

Edit the config.h file. Comment out the line ``#define WIFI_ENABLE true`` by adding two forward slash marks (``//``) infront of the line.
Then upload the project back to the CS.

Network Startup sequence
=========================

For reference, it may be helpful to know the sequence the Command Station uses to try and establish a network connection. The following provides the flow of this sequence.

1. Check for a WiFi Device - Scan serial ports 1, 2, and 3 in order to look for Wifi. If no response, abort network setup and start the Command Station without WiFi.
2. If we find a WiFi device, next look if ``#define DONT_TOUCH_WIFI_CONF`` is uncommented. If so, abort config attempts here - done
3. Next, IF no SSID is configured, check if the ESP is configured in STATION mode already from a previous network connection. If so, try to connect to that network. If we connect, stop and start the CS, if not, go to step 4.
4. Try to configure in STATION mode from values in the config.h file - done
5. If none of the above, set up as an AP with an ID of DCCEX_xxxxxx and a password set in the config.h file. If unconfigured, the default will be PASS_xxxxxx (xxxxxx will be the last 6 characters of the device MAC address)

Tips and Tricks
=================
There are circumstances where you may want to make temporary changes to your network, such as when you take your layout to a show. The following are some handy things you can do. Use a serial monitor connected to the USB port of your CS and enter the commands you need. Remember that if you disconnect the serial monitor and reconnect it (or anything else) to the USB port, it will reset the CS and it will go back to the default configuration. Remember to press "send" after each command.

Temporarily Log Into A Different Network
-----------------------------------------

1. Forget your network settings by entering ``<+CWQAP>`` on the serial monitor.
2. Login to the new network by entering either a new local SSID & Passwrd, or using the CS in Access Point AP Mode.

Create a Static IP for your CS in AP Mode
------------------------------------------

You are stil going to have to go into your router, find the MAC address for your WiFi board (or find it in the serial monitor log) and then assign a static IP address (sometimes called "reserved" IP address) to that MAC. That should be all you need as the DHCP server on your network will assign that IP to your CS when the CS asks for one.

You can try these commands also. You must have a recent version of the firmware to support _DEF commands. If they don't work, try entering them without this suffix (Example: <+CIPAP> instead of <+CIPAP_DEF>)

1. Forget your network settings by entering <+RESTORE>
2. Enter ``<+CIPAP_DEF="192.168.5.1","192.168.5.1","255.255.255.0">`` to setup the AP with your IP address
3. Enter ``<+CWDHCP_DEF=1,1>`` 
4. Enter ``<+CWDHCPPS_DEF="1,10,"192.168.5.100","192.168.5.150">``