:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-cs.rst
  
|EX-CS-LOGO| |donate-button|

.. index:: EXCSB1, EX-CSB1

******************
EX-CSB1 Express
******************

|conductor| |tinkerer| |engineer| |support-button|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

Designed by the |DCC-EX| development team, the EX-CSB1 replaces up to 3 different stacked boards to provide a complete, expandible DCC and DC command station or booster with dual 5A track outputs, integrated programming track capability, and built-in fast WiFi for throttle control connections.

.. figure:: /_static/images/ex-csb1/csb1_render_drop_shadow.png
   :alt: DCC-EX EX-CSB1 Express
   :scale: 40%

What is the EX-CSB1 Express?
=============================

The EX-CSB1 is the first complete DCC Command Station capable of DC PWM with Booster mode from the DCC-EX Team. That's right, one board that can function as a full USB connected or Wireless WiFi Command Station or be deployed as a stand-alone booster anywhere on your layout! The EX-CSB1 saves you money while allowing you to more easily expand your layout XXXXXXX (really want to say something about booster mode being useful for non-DCC-EX DCC systems??)

Features include:
  * All-in-one DCC compatible Command Station/Booster with PWM DC output capability
  * Fast Wifi built-in
  * Runs DCC-EX Command Station Software (Open Source, so FREE **and** having new features added)
  * Runs DCC or DC locomotives
  * Handles up to 10 Wifi clients simultaneously to allow you to run your layout with your friends
  * Dual DCC or PWM DC 5A outputs and variable limit software to control current to the tracks
  * Accepts an EX-MotorShield8874 for additional 2 DCC/DC PWM/PROG outputs
  * DC outputs for 4 total power districts!
  * Programmable over-current protection on each output
  * Auto-reverser capability on any DCC output
  * Railsync DCC signal input for DCC Booster mode
  * DCC Booster mode can be automatically engaged on receipt of a Railsync DCC input signal - perfect for modular layouts!
  * Single power supply required (12V to 25V) to power the command station and the tracks!
  * USB-C connection for software updates, connection to EXWebThrottle or JMRI, and full logging/debugging
  * ESP32 fast 32-bit microcontroller with built-in WiFi for up to 10 simultaneous throttle connections (more with JMRI)
  * Qwiic/STEMMA QT 3v3 compatible I2C connector for accessories like displays, turnouts, lighting, etc.
  * Bundled graphical OLED display for status and diagnostics (extra displays can be added)
  * Short circuit protection for both tracks and reverse voltage input protection

Benefits include: 
  * Works immediatley out of the box - no need to assemble
  * More memory for larger EXRAIL automation/animation scripts than an Arduino Mega
  * Less voltage drop so that more of the power from the power supply reaches the track
  * No jumper wires, trace cutting, or bending pins required
  * Dynamically assign any output to programming mode, with NMRA current limit enforced
  * TrackManager :sup:`tm` support for configuring any output to any one of the DC/DCC/Prog modes to suit your layout

The EX-CSB1 is based on the 32-bit ESP32 microcontroller that operates on 3.3V rather than 5V for increased efficiency and more options for powering the board. It uses a robust, single-PCB design with dual outputs to provide an expandible Command Station and/or Booster in a small portable form factor.

The EX-CSB1 comes with two integrated MOSFET based motor drivers from Texas Instruments to reduce power consumption, put more power to the layout, and generate less heat than traditional solutions. They provide up to 5A peak power to each track output to be able to run more locos simultaneously. An additional EX-MotorShield 8874 can be plugged on top of the command station board to provide two more DCC or PWM DC outputs.

Since the EX-CSB1 can be a booster or a command station, you can spread more of them around your layout connected to the Railsync port. The CSB1 can automatically switch to booster mode when it senses a Railsync input.

The EX-CSB1 also has auto-reverser mode which can be enabled for any DCC output on a per-output basis. An overload is first tested with a reversing of the phase before deciding if the overload remains present.

Just a single 12V to 25V power supply is required to power the track and all the electronics on the EX-CSB1. The reverse polarity protection on the power input prevents damage to the circuit and its components in case the power supply is accidentally connected backwards. In addition, there is both hardware and software backup over current protection, over voltage protection, and over heating protection.

The EX-CSB1 features two power status LEDs, which provide visual indication of the microcontroller power status and track input supply status in addition to separate LEDs to show each side of the A and B power outputs to show the DCC and DC status of power to the tracks. There is also an LED that lights once Wifi is connected (STA mode) or available (AP mode.)

The built-in EXRAIL Automation and Animation capability lets you use pre-written scripts or ones you can create yourself to operate everything on the layout. Trains can run pre-determined routes, automatically stop for each other, operate crossings, signals,turnouts, and more.


Why did we make it?
====================

After experiencing such success of the DIY kit approach of the original EX-CommandStation software, the DCC-EX team wanted to address the need for something that was even simpler. We felt an all on one board that would appeal to a broader range of modellers, especially our Conductors who are less confident with electronics, or even our Engineers and Tinkerers who don't want to spend their precious hobby time on electronics.

In doing so we also wanted to maintain a bit of the "I did it myself" satisfaction, while making things far simpler, smaller, and more "plug and play". Most of us want more time playing with our layouts and not fiddling with connections or debugging issues. And whether you are a Conductor, Tinkerer, or Engineer, you still may want an all-in-one solution to save time, space, and reduce complexity. We asked the team, "what features would you want on the ideal command station?". That is how the EX-CSB1 Express came to be.


How can I get one?
==================

Units may be purchased from the following sources:

* In Australia, New Zealand and South East Asia from `Millennium Engineering Pty Ltd <https://www.milleng.com.au>`_
* In Europe from `Semify's Web Store <https://www.semify-eda.com/ex-motorshield8874/>`_ (based in Austria)
* In the US from the `DCC-EX Store <https://store.dcc-ex.com/>`_ or...
* from `Smart Hobby, LLC <https://www.smarthobbyllc.com/>`_. You can also find Smart Hobby on Facebook
* In the UK from `Chesterfield Model Making & Miniature Electronics <https://chesterfield-models.co.uk/product/semify-dcc-ex-motor-shield/>`_
* and other manufacturers licensed by DCC-EX.

The EX-CSB1 Command Stations normally come with an OLED status display and a carrier base mount (sometimes called a "sled" ) There are different options for the board such as with or without an additional EX-MotorShield 8874 for two additional DCC/PWM DC outputs. Prices vary from around $105-$145 in the US, to approximately £ XXX -fnd in the UK, € XXX -fnd in Europe, and in Australia starting from $AU175 -fnd. Prices typically do not include tax and shipping.

Ordering in Quantity or wishing to Resell
==========================================

For quantities of 10 or less per annum, you may utilize a PCB manufacturing and assembly service such as JLCPCB without licensing fees. A donation to DCC-EX would be appreciated, so click the DONATE button! The production files are available on the `DCC-EX GitHub <https://github.com/DCC-EX/EX-Motorshield8874>`_. XXX

Entrepreneurs wanting to use the design to offer commercial quantities to their local communities should contact DCC-EX (sales @ dcc-ex.com) to arrange a bulk purchase or a license to manufacture. Licensing includes donating a royalty to DCC-EX per board sold.

Board layout
==============

  * Input Power Barrel jack
  * USB-C Input Power / Data Connector
  * Track A and B outputs
  * Track Power LEDs
  * QwiiC I2C connector
  * Railsync connector
  * Oled I2C Header
  * GPIO Headers
  * Dual I2C Pin Header
  * Reset button
  * ESP32 Microprocessor
  * Antenna
  * WiFi / User LED
  * Unpopulated power pads - Just because you are going to ask. For possible future use.
  * Motor Controller Chips - Hot area!
  * Board labels

.. figure:: /_static/images/ex-csb1/csb1_render_top.png
   :alt: DCC-EX EX-CSB1 Express
   :scale: 40%

**Input Power Barrel Jack** - The CSB1 normally comes with a barrel jack for compatibility with most laptop-type power supplies that use a 2.1mm inner hole diameter and a 5.5mm outer shank diameter. Be careful since some power supplies have a 2.5mm inner hole which is too loose a fit. The barrel jack input power is reverse voltage protected. Power from the barrel jack powers the 5V regulator to power an optional EX-MotorShield 8874 (to allow for 2 more power districts), the 3.3V regulator to power the EX-CSB1, and power out to the track.

**USB-C Power/Data Connector** - The USB connector can supply 5V DC from a computer or any 500mA or larger power supply. The 5V is converted through a regulator to the 3.3V that runs the circuitry on the board. In this way you can connect your EX-CSB1 to a computer and update your software version or test EXRAIL scripts that run your accessories. However, without another power supply, you cannot supply power to the rails to run trains. You can connect your 12V DC to 25V DC track Power supply to the barrel jack while the USB is connected. 

**Track A and B Outputs** - These are female pluggable terminals that accept a removable male screw terminal plug (included with your CSB1). Using the removable connectors allows for easy reconfiguration, testing, and placement of your command station. You can unsolder these connectors (or ask for a special order) and replace them with 3.5mm pitch screw terminals if you prefer. For DCC operation, output A is usually the MAIN track and output B is the programming track. However, with our TrackManager :sup:`tm` feature, you can configure any output to be DCC, DC, MAIN, or PROG. You should keep the phase of the tracks aligned. More in this here. XXX. Power to each output can be controlled together or individually.

**Track Power LEDs** - These are indicators that power is being sent to the track. With DC operation, both LEDs should shine brightly when your throttle issues the power on command. You can also configure the CSB1 to start with power on using a mySetup.h or myAutomation.h file. See more here XXX. For DC operation, when power is on, ONE LED will light for each direction. That is, forward will light one LED and when you select reverse, the other LED will light. 

**QWiic Connector (I2C)** - This is a standard for an I2C bus connection so that the same cable can be used to daisy chain I2C devices like displays, sensors, servos, etc. Please note the pin connection order when making your own cables or when purchasing from discount sites that often wire them incorrectly. For example, red should always be positive power and black is negative DC or "GND". IMPORTANT: The voltage for this connector is ALWAYS 3.3V!

**RailSync Connector** - This is a standard Railsync input. Connecting a RailSync output from a Command Station or Booster will automatically set the EXCSB1 to booster mode. XXX (describe or link to booster mode). Any voltage between 5V and 26V at the input will work. The Digitrax specification is from 12V to 26V.

**OLED I2C Header** - This is primarily designed for an OLED display, but can also be used as a female header for any OLED device that has male pins or for use with Dupont jumper wires. IMPORTANT: Many .96", 1.3" OLED displays, and some others will connect directly to the pins. However, there is no standard for pin order. Make absolutely sure that if you connect a display directly to the header that its pins are in the correct order.

**Dual I2C Header** - This is a dual male pin I2C header with 2 I2C bus connectors one above the other. They are wired together on the same I2C bus as the QWiic connector and OLED I2C Header. IMPORTANT: Note that the pin order on these two rows are different from the OLED header, pay attention to the pin order when using Dupont female wires. The EX-CSB1 is a 3.3V device, so all the I2C connectors supply 3.3V. When using 5V boards like the Arduino Mega, the OLED header and the I2C headers supply 5V (the Qwiic connector always supplies 3.3V no matter what microcontroller you are using). Keep that in mind if you are upgrading from a DIY Arduino Command Station to a 3.3V device ike the EX-CSB1 and are connecting I2C devices.

**Reset Button** - Pressing reset button does a soft reset of the command station. This means that if the Command Station gets into an unexpected state, you can reset the EX-CSB1. The software, EXRAIL Scripts, and any other settings are maintained. Boards stacked on top of the EX-CSB1 may not be reset. This is different from a restart which requires unplugging all power from the EX-CSB1. A restar will make sure everything, including boards stacked on the EX-CSB1 are reset.

**ESP32 Microcontroller / WiFi / WiFi Antenna** - One microcontroller controls everything on the EX-CSB1. It runs the |EX-CS| software, any mySetup.h file instructions, any myAutomation.h scripts, and the WiFi connection to throttles. Be careful in your setup to A. Protect the antenna from being damaged from contact with anything and B. Keep anything at least 2cm (.75") from the antenna and do not allow any metallic objects to be near or surrounding the antenna.

**WiFi / User LED** - When WiFi is enabled, this LED will stay on. It is under software control in the EX-CommandStation software, so the LED can be repurposed to indicate a user defined function.

**3.3V LED** - The 3.3V LED will light whenever the 3.3V regulator is powered, this will be when powered by USB or from an external power supply connected to the barrel jack. This is simply an indicator that the circuitry on the board is powered.

**5V LED** - The 5V LED will light whenever power is supplied to the barrel jack. This LED indicates that power is being supplied to the 5V regulator which can power an EX-MotorShield 8874 stacked onto the GPIO Headers. Power from the barrel jack will power the 5V regulator which in turn powers the 3.3V regulator, therefore, when power is supplied via the barrel jack, both the 5V and 3.3V LEDs will be lit.

**GPIO Headers** - The 4 GPIO headers accept a DCC-EX EX-MotorShield 8874. The EX-CSB1 itself has 2 outputs for 2 track power districts. Stacking the 8874 on these headers provides 2 additional power districts for a total of 4. Any of the 4 outputs can be used for any combination of DCC MAIN, DCC PROG, or DC PWM.




Powering the EX-CSB1
=====================

The CSB1 has a 2.1mm x 5.5mm power jack. You can use an optional 2.1mm x 5.5mm screw terminal block adapter if you already have a power supply with bare wires. See our section on recommended power supplies for more information XXX. Simply plug your power supply into Mains power and plug the male barrel end into the Command Station. Make sure your supply has the proper voltage for the scale of your locos (between 12V and 25V DC) and at least 4A of current capability. To use the full capacity of the EX-CSB1, we recommend 6A or more. For Z scale 12V would be adequate, but for N, HO and OO scale we would recommend between 14V and 16V DC. The DC input must be fully regulated, preferably a modern switch-mode power supply brick with double insulation and good overload current protection.

Don't worry about having more Amps than needed, too much voltage is a bad thing, but too much current doesn't hurt anything since an electronic device will only use as much current as it needs. Better to have a little extra than to have too little. Do keep in mind, however, that both voltage and current can be dangerous. The barrel connector provides a bit of extra safety, but if you drop a screwdriver across the terminals of your 10A power supply, it could become an arc welder. Be cautious.

See "how much current do I need" XXX

You should see the bright green power LED light when when power is applied letting you know the electronics are operating, however in the default configuration as delivered to you, track power will be OFF for safety. You normally would not want power to unexpectedly come on as soon as you plug the EX-CSB1 into the wall power in case the layout was not in a condition ready to accept power to the tracks. This default behaviour can be changed here XXX

Connecting to Your tracks
==========================

Before connecting wires to your tracks, make sure you have unplugged the power supply from the wall or removed the barrel connector from the command station. You do NOT want to have power to the command station while working on your connections.

Once you are sure power is disconnected and the power led indication is off, you can connect wires from the A output + and - to the track. For DCC operation it is not important which wire is which, since there is no polarity, but it is important as your layout grows to be consistent so that different power districts are in phase. That just means that when one track is positive relative to the other as they switch back and forth quickly, all the different districts have that same side of the track synced the same way. More detail on this in in the wiring section XXX.

For DC operation, there is polarity in that one track is positive and the other negative and the train will move forward when voltage is applied through the command station. When that voltage is reversed, the train will run in reverse.


DCC Operation
=====================

The EX-CSB1 defaults to DCC operation. To see how to operate DC mode see here XXX

The track outputs are shown here labelled A and B. Normally, for DCC operation, output A is for your MAIN track and output B is for your PROG (Programming) track. However, the EX-CommandStation software allows you to make any track a MAIN, a PROG, DCC, DC, or a Booster, but that is covered in the TrackManager help XXX For now, let's just keep it simple.


What to put here? XXX Cover more theory of DCC and basics of the voltage and signal and DC having polarity and being PWM? Or just talk about how to turn on DC and DCC in Trackmanager?

DC Operation
===============

It is important to note that this is not a varying DC voltage, Full voltage is always at the track when the throttle is set to a speed greater than zero. Speed is controlled by using a PWM (pulse width modulated) signal that turns the voltage on and off to the track at a rate that changes the "effective" voltage the motor in the locomotive "sees". This mimics what a DCC decoder does in a DCC loco to control a motor. The benefit of this method is that starting and stopping and operating at slow speed is more smooth.

USB Connection to install the Command Station Software
======================================================

The EX-CSB1 Express should come from your reseller with the EX-CommandStation software already installed. However, you may want to upgrade to the latest firmware or create your own EX-RAIL automation/animation scripts and upload them to the CS. A USB-A to USB-C cable (or a USB-C to USB-C cable if your computer has a USB-C connector) allows you to connect your CS to a computer to use our EX-Installer application or the Arduino IDE to install your files.

Resetting the CS
=================

USB Connection to a Serial Monitor
===================================

Using the appropriate USB-A to USB-C or USB-C to USB-C cable, you can use the Arduino IDE, EX-WebThrottle, or JMRI to act as a serial monitor to view diagnostic messages from the CS or send manual commands for testing or configuration.

USB Connection to JMRI
=======================

Integrated displays
====================

Connecting Accessories (I2C)
=============================

