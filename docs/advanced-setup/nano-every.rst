*******************
Nano Every
*******************

The Nano Every is a direct replacement for the Arduino Nano. It runs on 5V and is the same size as a Nano, 45 x18mm. However it is a much more powerful board than a standard Nano or Uno. In particular:

* Uses the ATmega4809 instead of the ATmega328
* Has 50% More program memory (you can use WiFi or Ethernet!)
* Has 200% More flash memory
* Micro-USB connector instead of

Clock 16 MHz 
Flash Memory 32 KB 
SRAM 2 KB
EEPROM 1 KB
14 Digital I/O Pins
Analog Input Pins 8 (with 10-bit resolution)
Digital IO Pins 22
PWM Pins 6

**Nano Every**

* Clock 16 MHz * 
* Flash Memory 48 KB 
* SRAM 6 KB 
* EEPROM 256 Byte
* Analog Input pins 8 (with 10-bit resolution)
* Digital IO Pins 23
* PWM pins 6

* no chrystal, internal clock. Not sure about steady interrups. And despite advertizing 20MHz, it runs instead at 16.

5V regulator can handle much more power (1A theoretical), 3.3V 600mA
4 UARTS! But serial1 is wired differently than on the Nano. Where pins 0 and 1 on a Nano are serial and connected to the USB and pins 0 and 1, the Every runs serial 1 to those pins.

