:orphan:

.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-cs.rst
  
|EX-CS-LOGO| |donate-button|

.. index:: EXCSB1, EX-CSB1

******************
|EX-CSB1|
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

The |EX-CSB1| is the first fully integrated DCC Command Station with DC PWM and Booster mode capabilities developed by the DCC-EX Team. This versatile board that can function as a complete Command Station with USB or WiFi connectivity or serve as a stand-alone booster, making it an ideal addition to any layout, including those using non-DCC-EX systems.

Key Features:
  * All-in-one DCC Command Station/Booster: Compatible with DCC and capable of PWM DC output
  * Built-in Fast WiFi: Supports up to 10 simultaneous throttle connections, expandable with JMRI
  * Advanced Hardware: Utilizes an ESP32 microcontroller with dual DCC or PWM DC 5A outputs, including variable current limit control
  * Expandable Outputs: Can accept an EX-MotorShield8874 for two additional DCC/DC PWM/PROG outputs, providing power to for total districts
  * Protection & Safety: Programmable over-current protection, and hardware over temperature and reverse voltage protection
  * Versatile Power Supply: Operates with a single 12V to 25V power supply that powers the entire system
  * USB-C Interface: Fore easy software updates, connection to EX-WebThrottle or JMRI, and logging/debugging
  * Accessory Support: Qwiic/STEMMA QT 3.3V, compatible I2C connector and extra I2C pin headers
  * Pre-Installed with DCC-EX Command Station Software
  * Auto-Reverser capability
  * RailSync DCC input for automatic booster mode engagement
  * OLED Display: Bundled graphical display for status and diagnostics, with support for additional displays

Benefits include: 
  * Ready-To-Run: Pre-assembled, with no need for additional assembly or configuration
  * Enhanced Performance: More memory than an Arduino Mega for complex EXRAIL automation/animation scripts
  * Efficient Power Usage: Less voltage drop, ensuring more power reaches the track
  * Flexible Output Management (TrackManager :sup:`tm` support): Dynamically assign outputs to different modes (DC/DCC/PROG), with proper NMRA current limits

The EX-CSB1's robust, single-PCB design includes integrated MOSFET motor drivers from Texas Instruments, providing up to 5A peak power per track output. This allows for simultaneous operation of multiple locomotives with reduced power consumption and heat generation compared to traditional systems.

With its dual role as a command station or booster, the EX-CSB1 can be strategically placed around a layout, seamlessly switching to booster mode upon detecting a RailSync input signal. This feature is particularly useful for modular layouts, ensuring smooth operation across different sections.

An additional EX-MotorShield 8874 can be snapped onto the command station board to provide two more DCC or PWM DC outputs.

The system includes comprehensive protection features such as reverse polarity protection, hardware and software overcurrent protection, overvoltage protection, and thermal protection. It also provides clear status indications via LEDs for microcontroller power, track input supply, track output power, and WiFi connection status.

The |EX-CSB1|'s built-in EXRAIL Automation and Animation capabilities enable advanced control of layout operations, including automated train routing, crossing controls, signal management, and more.


Why did we make it?
====================

After seeing the such success of our original EX-CommandStation software, which allowed modellers to build their own setups, we realized there was a need for something even simpler. The DCC-EX Team wanted to create a solution that would appeal to a wider range of modellers, especially those who might not feel as confident with the electronics or those who just prefer to spend time enjoying their layouts instead of tinkering with tech.

We wanted to keep the sense of accomplishment that comes with a DIY project, but make it much easier, smaller, and more "plug-and-play". After all, most of us would rather focus on running our trains than on troubleshooting wiring or connections. Whether you consider yourself a Conductor, Tinkerer, or Engineer, you might appreciate an all-in-one solution that saves time and space, and reduces complexity. That's why we asked ourselves, "What features would the ideal command station have?". And that's how the |EX-CSB1| was born.

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

Entrepreneurs wanting to use the design to offer commercial quantities to their local communities should contact DCC-EX (sales @ dcc-ex.com) to arrange a bulk purchase or a license to manufacture. Licensing includes donating a royalty to DCC-EX per board sold.XXX move this section to the bottom and just link to it? XXX How about a link to a separate section for reseller inquiries?

Board layout
==============

.. figure:: /_static/images/ex-csb1/csb1_render_layout_top.png
   :alt: DCC-EX EX-CSB1 Express
   :scale: 40%

**Input Power Barrel Jack** - The CSB1 normally comes with a barrel jack for compatibility with most laptop-type power supplies that use a 2.1mm inner hole diameter and a 5.5mm outer shank diameter. Be careful since some power supplies have a 2.5mm inner hole which is too loose a fit. The barrel jack input power is reverse voltage protected. Power from the barrel jack powers the 5V regulator to power an optional EX-MotorShield 8874 (to allow for 2 more power districts), the 3.3V regulator to power the EX-CSB1, and power out to the track. For the correct voltage (Normally between 12V DC and 14.5V DC for N and HO Scales, see XXX) Also XXX, Do we need a picture of the connector?

**USB-C Power/Data Connector** - The USB connector can supply 5V DC from a computer or any 500mA or larger power supply. The 5V is converted through a regulator to the 3.3V that runs the circuitry on the board. In this way you can connect your EX-CSB1 to a computer and update your software version or load EXRAIL scripts that run your accessories. However, without another power supply, you cannot supply power to the rails to run trains. You can connect your track Power supply (see above) to the barrel jack while the USB is connected, they will not interfere with each other. XXX (will they???). The USB port is also very useful for connecting a serial monitor to test the command station and view logging information. link? XXX

**Track A and B Outputs** - These are female pluggable terminals that accept a removable male screw terminal plug (included with your CSB1). Using the removable connectors allows for easy reconfiguration, testing, and placement of your command station. You can unsolder these connectors (or ask for a special order) and replace them with 3.5mm pitch screw terminals if you prefer. For DCC operation, output A is usually the MAIN track and output B is the programming track. However, with our TrackManager :sup:`tm` feature, you can configure any output to be DCC, DC, MAIN, or PROG. You should keep the phase of the tracks aligned. More in this here. XXX. Power to each output can be controlled together or individually. Correct wired gauge for the screw terminals is XXX to XXX. Be sure your wire gauge can handle the current you expect on the track. See here XXX

**Track Power LEDs** - These are indicators that power is being sent to the track. With DC operation, both LEDs should shine brightly when your throttle issues the power on command. You can also configure the CSB1 to start with power on using a mySetup.h or myAutomation.h file. See more here XXX. For DC operation, when power is on, ONE LED will light for each direction. That is, forward will light one LED and when you select reverse, the other LED will light. 

**QWiic Connector (I2C)** - This is a standard for an I2C bus connection so that the same cable can be used to daisy chain I2C devices like displays, sensors, servos, etc. Please note the pin connection order when making your own cables or when purchasing from discount sites that often wire them incorrectly. For example, red should always be positive power and black is negative DC or "GND". IMPORTANT: The voltage for this connector is ALWAYS 3.3V!

**RailSync Connector** - This is a standard Railsync input. Connecting a RailSync output from a Command Station or Booster will automatically set the EXCSB1 to booster mode. XXX (describe or link to booster mode). Any voltage between 5V and 26V at the input will work. The Digitrax specification is from 12V to 26V. See here for railsync wiki??? XXX

**OLED I2C Header** - This is primarily designed for an OLED display, but can also be used as a female header for any OLED device that has male pins or for use with Dupont jumper wires. IMPORTANT: Many .96", 1.3" OLED displays, and some others will connect directly to the pins. However, there is no standard for pin order. Make absolutely sure that a display you purchase to connect directly to the header has its pins in the correct order.

**Dual I2C Header** - This is a dual male pin I2C header with 2 I2C bus connectors one above the other. They are wired together on the same I2C bus as the QWiic connector and OLED I2C Header. IMPORTANT: Note that the pin order on these two rows are different from the OLED header, pay attention to the pin order when using Dupont female wires. The EX-CSB1 is a 3.3V device, so all the I2C connectors supply 3.3V. When using 5V boards like the Arduino Mega, the OLED header and the I2C headers supply 5V (the Qwiic connector always supplies 3.3V no matter what microcontroller you are using). Keep that in mind if you are upgrading from a DIY Arduino Command Station to a 3.3V device ike the EX-CSB1 and are connecting I2C devices.

**Reset Button** - Pressing reset button does a soft reset of the command station. This means that if the Command Station gets into an unexpected state, you can reset the EX-CSB1. The software, EXRAIL Scripts, and any other settings are maintained. Boards stacked on top of the EX-CSB1 may not be reset. This is different from a hard restart which requires unplugging all power from the EX-CSB1. A hard restart will make sure everything, including boards stacked on the EX-CSB1 are reset.

**ESP32 Microcontroller / WiFi / WiFi Antenna** - One microcontroller controls everything on the EX-CSB1. It runs the |EX-CS| software, any mySetup.h file instructions, any myAutomation.h scripts, and the WiFi connection to throttles. Be careful in your setup to A. Protect the antenna from being damaged from contact with anything and B. Keep anything at least 2cm (.75") from the antenna and do not allow any metallic objects to be near or surrounding the antenna.

**WiFi / User LED** - When WiFi is enabled, this LED will stay on. It is under software control in the EX-CommandStation software, so the LED can be repurposed to indicate a user defined function.

**3.3V LED** - The 3.3V LED will light whenever the 3.3V regulator is powered, this will be when powered by USB or from an external power supply connected to the barrel jack. This is simply an indicator that the circuitry on the board is powered.

**5V LED** - The 5V LED will light whenever power is supplied to the barrel jack. This LED indicates that power is being supplied to the 5V regulator which can power an EX-MotorShield 8874 stacked onto the GPIO Headers. Power from the barrel jack will power the 5V regulator which in turn powers the 3.3V regulator, therefore, when power is supplied via the barrel jack, both the 5V and 3.3V LEDs will be lit.

**GPIO Headers** - The 4 GPIO headers accept a DCC-EX EX-MotorShield 8874. The EX-CSB1 itself has 2 outputs for 2 track power districts. Stacking the 8874 on these headers provides 2 additional power districts for a total of 4. Any of the 4 outputs can be used for any combination of DCC MAIN, DCC PROG, or DC PWM.

**OLED Display (not shown above)** - The OLED display provides diagnostics, status, and information display. 

XXX Add to image to include hot area, unpopulated power pin, and any silkscreening. Add the bottom of the board help.


Powering the EX-CSB1
=====================

The CSB1 has a 2.1mm x 5.5mm power jack. If you already have a power supply with bare wires, you can use an optional 2.1mm x 5.5mm screw terminal block adapter. For more information about power supplies, see our section on recommended power supplies XXX. 

To power up the CSB1, just plug your power supply into the mains (aka wall outlet) and connect the barrel end to the Command Station. Make sure your power supply matches the needs of your setup: the voltage should be between 12V and 25V DC, depending on the scale of your locomotives, and it should provide at least 4A of current. To get the most out of your EX-CSB1, we suggest using a power supply with 6A or more. For Z scale, 12V is usually enough, but for N, HO, and OO scales, we recommend using between 14V and 16V DC. It’s important that your DC power input is well-regulated—ideally, a modern switch-mode power supply with double insulation and strong overload protection.

.. figure:: /_static/images//12v-3A-brick.jpg
   :alt: 12V 3A brick power supply
   :scale: 100%
   :align: right

   12V/3A Power Supply

Don't worry if your power supply offers more amps than you need. While too much voltage can be harmful, extra current isn't a problem since the CSB1 will only use as much as it needs. In fact, it's better to have a bit more current than too little. However, remember that both voltage and current can be dangerous if not handled properly. The barrel connector helps add some safety, but be cautious—if, for example, a metal tool accidentally touches the terminals of a high-powered supply, it could cause a short circuit.

For more details on how much current do I need, see [link] XXX

When you connect power to the CSB1, you should see a bright green power LED light up, confirming that the electronics are working. However, for safety, track power will be off by default when you first plug in the EX-CSB1. This is to prevent power from accidentally being applied to your layout before everything is ready. If you prefer, you can change this default setting [link].


Connecting and Testing Your Command Station
============================================

What you will need
--------------------

* An EX-CSB1 Command Station
* A Power supply (12V - 16V DC see xxx)
* A DCC loco (DC can work also)
* Track
* A throttle (You can use your phone or a computer - see below)
* 16 to 22 AWG Wire
* Jeweller's flat bladed screwdriver (1.5 - 2mm blade)
* A laptop or other computer*
* A USB cable*

  *Optional for connecting connecting to a computer

Start with all power disconnected
----------------------------------

Before connecting any wires to your command station or tracks, make sure you have unplugged the power supply from the wall or removed the barrel connector from the command station. It is crucial to ensure that the command station has no power while you are working on your connections.

Connecting to Your Tracks
--------------------------

The power connection to your track will be either wires you solder yourself to the rails or via a power connector that plugs into track such as Kato Unitrack. We will leave it up to you to determine the proper connection to your track.

Once you are sure power is disconnected from the CS and the power LED is no longer illuminated, you can connect wires from the A output (+ and -) of the command station to the track. For DCC operation it does not matter which wire goes to which rail, since there is no polarity. However, as you layout grows, it is important to stay consistent with your wiring to ensure that different power districts remain in phase. That just means that when the tracks rapidly switch between one being energized and the other at ground potential, all the districts stay synchronized. You can find more detail on this in our wiring section XXX. [link]

For DC operation, polarity does matter. One rail is positive, and the other is negative, which determines the direction your train will move when voltage is applied through the command station. If you reverse the voltage, the train will change direction and run in reverse.

DCC Operation
---------------

The EX-CSB1 is set to operate in DCC mode by default. If you want to switch to DC mode, you can find instructions on how to do that here XXX [link]

Track Outputs
^^^^^^^^^^^^^^^

You will notice that the two track outputs on the EX-CSB1 are labelled A and B. In standard DCC operation, A is configured for DCC MAIN operation, and B is configured for PROG or programming track. We recommend connecting your track to the A MAIN output initially to test your Command Station.

The pluggable male screw terminals accept to 16 to 28 AWG (gauge) solid or stranded wire. If you use stranded, we recommend "tinning" the ends of the wire to make a good connection and ensure that stray wire whiskers don't stray outside the screw terminals and cause a short circuit. Larger wire can handle more current and provide less resistance.  18-22 is a good start. Keep your wires short by mounting the CS close to the track. See XXX for more information or wire gauge.

Unscrew both screw terminals with a flat blade jeweller's screwdriver. The screws just need to be loosened enough to fit your wires into the holes. Tighten down both screws once you have inserted the wires.

XXX insert image here of screwing terminals

Powering up
------------

Now you can connect your track power supply to the barrel connector on the CSB1 and then plug the other end into the wall. You should see status information on the display including the CSB1 firmware version. (If you do not have a display, you will need to connect a serial monitor XXX This is a mess of having to have so many options and send people back and forth and have an entire section on using a serial monitor. Just link to it?)

The DCC-EX EX-CSB1 Command Station/Booster will power up in WiFi Access Point mode, with a Wifi network SSID of DCCEX_xxxxxx and password of PASS_xxxxxx, both of which will be visible on the OLED display (or serial monitor log) after it boots

XXX figure link to OLED display. Also link to serial monitor log section?

Access Point (AP) mode creates a separate WiFi network on the Command Station itself, whereas Station (STA) mode allows the Command Station to join as a WiFi device on your home or layout WiFi network. We have the EX-CSB1 set to default to AP mode for convenience of being able to get up and running quickly.

The WiFi LED will illuminate once WiFi is configured. 

XXX figure link showing WiFi LED

Connecting via Wifi
-------------------- 

XXX should title be "connecting with your phone?"

Please connect your smartphone or tablet where you previously installed Engine Driver or WiThrottle to this WiFi network with the password shown on the OLED to begin running trains immediately! You have nothing further to do to start using your DCC-EX EX-CSB1. You can remove the protective cover on the OLED if you wish.

XXX figure image of phone logging in to the AP

::NOTE: Note too that some smart phones and tablets will try hard to only connect you to a WiFi network that has Internet access, and you may be asked if you really want to connect to a WiFi network without it. For the sake of getting up and running quickly, just dismiss such queries. In the next section we show you how to reconfigure the EX-CSB1 to join your home or layout WiFi network should you prefer it.

Connecting Via USB and EX-WebThrottle
---------------------------------------


Use TrackManager to Set Outputs to DCC or DC Operation
========================================================

Our Trackmanager technology allows you to configure any of 4 outputs to be DCC MAIN, DCC PROG, or DC PWM in order to run DCC or DC locos. 2 outputs are included with the EX-CSB1 with 2 more available with the purchase of an EX-MotorShield 8874 that just stacks on top. By default, output A is configured as a DCC MAIN track and output B is configured as a DCC Programming track. You can dynamically change the configuration using throttles (such as |EX-WT|, |JMRI|, or |Engine Driver|) or you can configure your CSB1 to always start in your desired configuration. Note that one of the outputs can be configured in such a way that it is another MAIN power district that automatically switches to programming mode when a programming command is issued by your throttle and then automatically switches back to MAIN. XXX have this be a NOTE? See a detailed TM section?


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

The EX-CSB1 Express should come from your reseller with the EX-CommandStation software already installed. However, you may want to upgrade when a new version is released or create your own EX-RAIL automation/animation scripts and upload them to the CS. A USB-A to USB-C cable (or a USB-C to USB-C cable if your computer has a USB-C connector) allows you to connect your CSB1 to a computer to use our EX-Installer application or the Arduino IDE to install your files.

Resetting the CS
=================

USB Connection to a Serial Monitor
===================================

Using the appropriate USB-A to USB-C or USB-C to USB-C cable, you can use the Arduino IDE, EX-WebThrottle, or JMRI to act as a serial monitor to view diagnostic messages from the Command Station or send manual commands for testing or configuration.

USB Connection to JMRI
=======================

Integrated displays
====================

Connecting Accessories (I2C)
=============================

