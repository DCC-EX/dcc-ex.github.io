***************************************************
WiThrottle Server, Web Server, DCC++ API Explained
***************************************************

There are several competing standards and ways to connect external software such as Throttles to the DCC++ EX Command Station or to JMRI. These standards are called "protocols" and the definition and instructions for how to implement them is called an API (Application Programming Interface). There is the WiThrottle API using a WiThrottle Server, the JMRI API using a Web Server, and the DCC++ EX API using <DCC++> Commands. You need to know that the language your throttle uses will work with how you want to connect to your Command Station.

The DCC++ API
==============

The first way to connect to DCC++ EX is to use our DCC++ API. This is the set of commands that tell the Command Station how to control your trains. DCC++EX understands simple command surrounded by brackets like this: "<1 MAIN>". That command turns your main track power on.

Since this is just sending characters back and forth across a serial connection, anything that can connect to an Arduino through a USB cable or one of the other serial ports using WiFi of Bluetooth can send DCC++ commands to the CS. This method is fast, direct, and can take advantage of special features that exist only in DCC++ EX. You can even connect using the Arduino Serial Monitor or connect to our WiFi with a terminal program like PuTTY and type DCC++ commands manually. Our WebThrottle-EX, JMRI and CABs like DCCpp CAB and DigiTrainsPro send commands in DCC++ format.

The WiThrottle Server
========================

The WiThrottle Protocol is the proprietary protocol developed by Matt Hoffman at https://www.WiThrottle.com. Like the DCC++ API, is consists of messages composed of strings of text characters sent across a serial connection that tell the Command Station how to control your layout. The command "PPA1", for example turns the power on in WiThrottle. It can be confusing, but WiThrottle can refer to the protocol (as in WiThrottle Server or WiThrottle compatible), but it also refers to the iOS throttle App called "WiThrottle" (it stands for WiFi Throttle).

DCC++ EX allows you to use WiThrottle "servers" built into JMRI and other software and have them connect to your Command Station via a USB or serial connection, but DCC-EX also implements a WiThrottle server in our Command Station software itself. A "server" is just a fancy way of saying that there is software running inside JMRI and DCC++ EX that can understand WiThrottle commands and "serve" or "service" clients that want to connect and send WiThrottle commands. The ability of DCC-EX to natively "speak" WiThrottle means you can directly connect a WiThrottle compatible Throttle (aka CAB) via Wifi or Bluetooth to the CS and run trains. But you can still connect to JMRI WiThrottle instead and connect JMRI to DCC++EX with a USB cable. So DCC++ EX is bi-lingual, we speak DCC++ AND WiThrottle! Apps like Engine Driver and WiThrottle for iOS send commands in the WiThrottle format.

The JMRI WEB Server
====================

JMRI has two kinds of servers you can connect to built into the JMRI software. We already mentioned the WiThrottle server, but JMRI also has a WEB Server. Devices can connect to JMRI and send commands like it would to a WEB page. This is yet another protocol and is supported by throttles like DigiTrainsPro. When connecting using a throttle that uses the WEB Server, you connect your throttle to that via WiFi, and then connect to DCC++EX with a USB or Serial connection.

A Note about WiFi Dropped Connections
=======================================

Phones and laptop like to think they are "smart" and want to connect you to the strongest signal and to a network that has internet capability. If you use the DCC++ EX Command Station as an Access Point (AP), which doesn't connect to the internet, and you connect to DCC++ EX with your throttle, your device may disconnect you from the CS without you knowing and without your permission. You should turn off the option to "automatically connect" to your home network. You may even have to "forget" your home network when you are using your wireless device to connect to DCC-EX. If you would rather, you can change settings in your config.h file to connect to your home network as a client instead running as an AP, and then have your throttle devices find the CS by its IP Address on your home network. You can find out more about that in :doc:`Wifi Setup <../get-started/wifi-setup>`

