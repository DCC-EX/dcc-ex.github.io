**************************
Mega+WiFi Configuration
**************************

This is a combination of a Mega Clone and an ESP8266 WiFi board. Our guess is that like many boards made in China, this is only made by one or two factories, but sold under several names. Search for WiFi+Mega or ATmega2560+ESP8266. Here are some of the brands:

* Wemos
* RobotDyn
* Geekcreit

A Operational Standalone WiFI DCC Command Station
==================================================

What You Will Need
-------------------

This is a tested and proven configuration

* DCC++EX 3.0.5 or greater
* ATMega2560 + ESP8266 WiFI - Combo Board
* Deek Robot L298P Standard Motor Shield (or other approve motor controller)
* 12-16Vdc Laptop power supply to the Motor Shield (16V provides 14.5Vdc to the tracks for HO Gauge)
* 7.5-9Vdc power supply to the ATmega boards with a female 2.1mm power barrel
* Android Smartphone w Engine Driver v2.28.123 or iOS Smarphone with WiThrottle
* USB-A male to Micro USB-B cable

What You Will Do
-----------------

1. Download the ESP Files
2. Flash the ESP8266 chip
3. Edit your config file and Load the DCC++EX 3.0.5+ to the Mega2560 chip
4. Setup your Throttle

Note: This board uses a Micro-USB connector instead of the USB-B printer type connector uses on regular Arduino Boards. It also uses the CH340G USB to Serial Driver chip instead of the FTDI on Arduino brands,so may require you to install a driver.

Steps;
------
**1)** Downloaded the Flash Download Tool 3.8.5 nodencu-flasher & download the ESP8266_NONOS_AT_Bin_v1.7.4 Bin files found here;
 -   https://wakwak2popo.wordpress.com/2021/01/05/flashing-at-command-set-on-combined-mega-8266-board/


**2)** To Flash with ESP8266_NONOS_AT_Bin_v1.7.4 set the ESP section of the board with the USB unplugged. (no power)
 -  set dip switches 1,2,3,4,8 off .. 5,6,7 on
 -  (set TX/RX Slide Pin to RxD3 & TxD3)
 -  Plugged in Mega+WiFI board to comm port X, press the **Mode button**,

Run the 3.8.5 Flasher Tool {relax give it time to completely open}
- press [Developer Mode] button
- Press [ESP8266 Download Tool] button

Set up file location in the Tool version 385
- Pay close attention setting up the Exact *.bin Files & locations 0x......
- [​IMG]

And then set the Exact radial dial & baud rate settings;
- (26M, 40MHz, DIO, 16Mbit-C1, com: xx, 460800 baud).

First press the **Erase button** and let the ESP erase the chip memory.   
Then press the **Start button** and the bin files will flash load onto the ESP-WiFi chip

After flashing, the ESP8266 Log will show it uploaded them all successfully and it closes the port.
- You disconnect the USB cable.


**3)** Set up the Arduino ATmega2560 side of the board with DCC++EX version 3.0.5+
- dip switches 1,2,5,6,7,8 off .. 3,4 on
- (Leave the TX/RX slide Pin on RxD3 TxD3)
- re-connected the USB cable

Download and install DCC++EX from either the Automated exInstaller or the Latest DCC++ EX Release >= 3.0.5
- https://dcc-ex.com/download/index.html

Once you have DCC-EX installed on the Mega you need to Open the CommandStation-EX Folder make a Copy of the config.example.h file and rename the copy to config.h

Decide which Mode of WiFi Communication you wish to run, Either Access Point AP Mode, Or Station STA Mode.

AP mode is Local Intranet, No Internet access.  Station Mode is your local WiFi Router With Internet access.
**Note:**  See WiFi Configuration for more details.

Setting up in Access Point AP Mode
- No additional changes require, Leave SSID & Passwd alone
- Your ESP-Wifi chip will assign a SSID as DCCEX_xxxxxx and PASS_xxxxxx, Where xxxxxx is the ESP8266 MAC ID number.

Setting up WiFi in Station STA Mode with Router
- Open the CommandStation-EX.ino in the Arduino IDE Interactive Development Editor then
- Edited & change the new config.h file to your local or home Router's SSID & Password.
- #define WIFI_SSID "Your network name" to your "Local SSID"
- #define WIFI_PASSWORD "Your network passwd" to your "Local PW" 

Compile and Re-upload DCC-EX to the
- ATMega2560 board (com: xx, baud 115200),
- Verify your com port and baud rate in Windows device manager

After the Arduino IDE uploads DCC-EX 3.0.5 sketch
- Disconnect USB cable
- Reset dip switches 1,2,3,4 on .. 5,6,7,8 off
- (Leave the TX/RX slide Pin on RxD3 TxD3)

Power up the Arduino ATMega2560 + ESP8266 WiFi board by Either a USB cable, Or  
  **Note:** {For Standalone Operations (no USB) you can use a 7-12vdc power supply in the Arduino 2.1mm female barrel.}

- When powered on through a USB cable, check the Arduino IDE Tools > Serial Monitor.
- It should show the ATMega2560 & ESP8266 WiFI communicating and assigning a xxx.xxx.x.xxx IP Address and Port 2560 to the new DCC++EX Command Station.
- ++ Wifi Setup CONNECTED ++


**4)** Set your Smartphone WiFi to the same local SSID & PASSwd you entered into the DCC++EX config.h file
- Start your Smart Phone (Andriod) Engine Driver App Or (Apple iOs) WiTHrottlle App and enter the IP address XXX.XXX.X.XXX assigned in the Arduino Serial Monitor above and Port 2560.


If the Engine driver fails to connect the first time with the Command Station just press the Mega's red Reset button and try the IP/Port connection again.

You should have a direct Throttle connection to the DCC++EX 3.0.5+ Standalone WiFI Command Station Via your home router.

**.. Note::** This is an Operations only config, the Engine Driver Power button only powers on the Main track, Not the Prog track. Function Keys are only local Default Function Settings, and are Not transferred from the JMRI Server Roster.

 Enjoy your New DCC++EX MEGA + WiFI On-Board Command Station!

* The RobotDyn Mega2560+ESP8266 WiFI combo-board May also be setup & configured this same way. We have not as yet tested it.
