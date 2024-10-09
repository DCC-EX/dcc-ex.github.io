.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-cs.rst
  
|EX-CS-LOGO| |donate-button|

.. index:: EXCSB1, EX-CSB1

***************************************
Connecting your EX-CSB1 to Run Trains
***************************************

Instruction manual for how to use the EX-CSB1. Call this the "EX-CSB1 Operating Manual"?

Board layout
==============

.. figure:: /_static/images/ex-csb1/csb1_render_layout_top.png
   :alt: DCC-EX EX-CSB1 Express
   :scale: 40%

   EX-CSB1 top (click image to enlarge it)

.. image:: /_static/images/ex-csb1/barrel_jack1.png
   :alt: Barrel Jack
   :scale: 40%
   :align: right

**Input Power Barrel Jack** - The CSB1 normally comes with a barrel jack for compatibility with most laptop-type power supplies that use a 2.1mm inner hole diameter and a 5.5mm outer shank diameter. Be careful since some power supplies have a 2.5mm inner hole which is likely to be too loose. The barrel jack input power is reverse voltage protected. This supplies a 5V switching regulator for all electronics on the board including a 3.3V regulator for 3.3V components, an optional EX-MotorShield 8874 stacked on top, and power out to the track. While it is capable of 10v-25v operation, it is best to choose a suitable track voltage for your scale. Typically this is 12-15v for N scale, and 14-16v for HO scale. With help in choosing your power supply or using one with bare wires instead of a barrel connector, see `Powering the EX-CSB1`_ below.

.. image:: /_static/images/ex-csb1/usb_conn1.png
   :alt: USB Connector
   :scale: 50%
   :align: right

**USB-C Power/Data Connector** - The USB connector can provide power from a computer or any 500mA or larger USB or USB-C Power Delivery (USB-C PD) power supply.  In this way you can connect your EX-CSB1 to a computer and update your software version or load EXRAIL scripts that run your accessories. However, without a power supply powering the DC input jack, you cannot supply power to the rails to run trains. You can connect your track Power supply (see above) to the barrel jack while the USB is connected, as they will not interfere with each other. You may also wish to do this to isolate the EX-CSB1 processor power from any interruptions to track power due to overload for example. The USB port is also very useful for connecting a serial monitor to test the command station and view logging information in real time to aid in fault finding. See :doc:`/reference/tools/serial-monitor`

.. image:: /_static/images/ex-csb1/pluggable_connectors.png
   :alt: Pluggable Track Output Connectors
   :scale: 40%
   :align: right

**Track A and B Outputs** - These are female pluggable terminals that accept a removable male screw terminal plug (included with your CSB1). Using the removable connectors allows for easy reconfiguration, testing, and placement of your command station. You can unsolder these connectors (or ask for a special order) and replace them with 3.5mm pitch screw terminals if you prefer. For DCC operation, output A is usually the MAIN track and output B is the programming track. However, with our TrackManager :sup:`tm` feature, you can configure any output to be DCC, DC, MAIN, or PROG. You should keep the phase of the tracks aligned, so if a train crosses from one power district to another it doesn't intentionally cause a short (unless it's a reversing loop and you have assigned that output to have Auto-Reverse capability.) See: :doc:`/ex-installer/managing-config-files`. Power to each output can be controlled together or individually. Correct wired gauge for the screw terminals is 16 to 28AWG (1.5mm^2). Be sure your wire gauge can handle the current you expect on the track.

.. image:: /_static/images/ex-csb1/track_output_leds.png
   :alt: Pluggable Track Output Connectors
   :scale: 70%
   :align: right

**Track Power LEDs** - These are indicators that power is being sent to the track, and the mode of the output. With DCC operation, both LEDs should shine brightly when your throttle issues the power-on command. You can also configure the CSB1 to start with power on using a mySetup.h or myAutomation.h file. See more here XXX. For DC PWM mode operation, when power is on, ONE LED will light for each direction. That is, forward will light one LED and when you select reverse, the other LED will light. 

.. image:: /_static/images/ex-csb1/qwiic_conn.png
   :alt: Qwiic Connector
   :scale: 30%
   :align: right

**QWiic Connector (I2C)** - This is a standard for an I2C bus connection so that the same cable can be used to daisy chain I2C devices like displays, sensors, servos, etc. Please note the pin connection order when making your own cables or when purchasing from discount sites that often wire them incorrectly. For example, red should always be positive power and black is negative DC or "GND". IMPORTANT: The voltage for this connector is ALWAYS 3.3V!

.. image:: /_static/images/ex-csb1/booster_conn.png
   :alt: Railsync Connector
   :scale: 35%
   :align: right

**RailSync Connector** - This is a standard Railsync input and is labelled "Booster In" on the top of the board. Connecting a RailSync output from a Command Station or Booster will automatically switch the EXCSB1 to booster mode on receipt of an input signal when the CSB1 is running the appropriate EX-RAIL script. Again be sure to wire the DCC outputs to power districts with consistent phasing. Any voltage between 5V and 26V at the input will work. The Digitrax specification is from 12V to 26V. See `the DCCWiki article on RailSync <https://dccwiki.com/LocoNet_and_RailSync_Voltages>`_ |EXTERNAL-LINK|

.. image:: /_static/images/ex-csb1/oled_header.png
   :alt: OLED header
   :scale: 40%
   :align: right

**OLED I2C Header** - This header is primarily designed for an OLED display, but can also be used as a female header for any I2C device that has male pins or for use with Dupont jumper wires. IMPORTANT: Many .96" and 1.3" OLED displays, and some others will connect directly to the pins, however **beware** that sadly there is no standard for pin order. Make absolutely sure that any display you purchase to connect directly to the header has its pins in the correct order! The correct order is GND, V+, SCL, SDA and is different than other OLED connectors on the board. For more information see: :doc:`/reference/hardware/i2c-devices`.

.. image:: /_static/images/ex-csb1/dual_i2c_pins.png
   :alt: Dual Male I2C Header
   :scale: 40%
   :align: right

**Dual I2C Header** - This is a dual male pin I2C header with 2 rows of I2C bus connectors one beside the other. They are wired together on the same I2C bus as the QWiic connector and OLED I2C Header. IMPORTANT: The pin order on these two rows are different from the OLED header, pay attention to the pin order when using Dupont female wires. The correct order for this header is SCL, GND, SDA and V+ as labelled on the board. The EX-CSB1 is a 3.3V device, so all the I2C connectors only supply 3.3V unlike the Arduino Mega. Keep that in mind if you are upgrading from a DIY Arduino Command Station to a 3.3V device ike the EX-CSB1 and are connecting I2C devices. For more information see: :doc:`/reference/hardware/i2c-devices`.

.. image:: /_static/images/ex-csb1/reset_button.png
   :alt: Reset Button
   :scale: 60%
   :align: right

**Reset Button** - Pressing the reset button does a hard reset of the command station. If the Command Station gets into an unexpected state, you can reset it by pressing this button. The DCC-EX software, EXRAIL Scripts, and any other settings are maintained, but the unit reboots as if it had been turned off. Boards stacked on top of the EX-CSB1 also receive the reset signal, but less well designed boards may not be reset depending upon their own circuit peculiarities. Only rarely should it require unplugging all power from the EX-CSB1 to perform a power-on hard reset.

.. image:: /_static/images/ex-csb1/esp32_1.png
   :alt: ESP32 Microcontroller
   :scale: 40%
   :align: right

**ESP32 Microcontroller / WiFi / WiFi Antenna** - One microcontroller controls everything on the EX-CSB1. It runs the |EX-CS| software, any mySetup.h file instructions, any myAutomation.h scripts, and provides the WiFi connection to throttles. Be careful in your setup to protect WiFi antenna from being damaged from contact with anything or should the unit be dropped. For best WiFi performance, keep items at least 2cm (.75") from the antenna and do not allow any metallic objects to be near, underneath, or surrounding the antenna.

.. image:: /_static/images/ex-csb1/wifi_led2.png
   :alt: WiFi LED
   :scale: 45%
   :align: right

**WiFi / User LED** - When WiFi is enabled, this LED will stay on. It is under software control in the EX-CommandStation software, so the LED can be repurposed to indicate a user defined function with an EXRAIL script or a <U> command function.

.. image:: /_static/images/ex-csb1/3v_led.png
   :alt: 3.3V LED
   :scale: 28%
   :align: right

**3.3V LED** - The 3.3V power LED will light whenever the 3.3V regulator is powered. This occurs when powered by USB, or from an external power supply connected to the barrel jack. This is simply an indicator that the circuitry on the board is powered.

.. image:: /_static/images/ex-csb1/5v_led.png
   :alt: 5V LED
   :scale: 28%
   :align: right

**5V LED** - The 5V LED will light whenever power is supplied to the barrel jack. This LED indicates that power is being supplied to the 5V regulator which can power an EX-MotorShield 8874 stacked onto the GPIO Headers. Power from the barrel jack will power the 5V regulator which in turn powers the 3.3V regulator. Therefore, when power is supplied via the barrel jack, both the 5V and 3.3V LEDs will be lit.

**GPIO Headers** - The 4 GPIO headers accept a DCC-EX EX-MotorShield8874. The EX-CSB1 itself has 2 outputs for 2 track power districts. Stacking the EX8874 on these headers provides 2 additional power districts for a total of 4. Any of the 4 outputs can be used for any combination of DCC MAIN, DCC PROG, or DC PWM. You must enable the extra board from the EX-Installer or your config.h file for a manual install. See XXX.

.. image:: /_static/images/ex-csb1/oled_display.png
   :alt: OLED Display
   :scale: 28%
   :align: right

**OLED Display (not shown above)** - The OLED display provides diagnostics, status, and general information. The OLED display can also show output from EX-RAIL scripts including user defined text. By default, the display shows the version number, license, power status, free memory, and if configured, your WiFi access point login information.

.. image:: /_static/images/ex-csb1/hot_area.png
   :alt: Hot Area Warning
   :scale: 36%
   :align: right

**HOT Surface Area** - The entire area shown in the image to the right can get extremely hot during operation. Be carful not to touch this area at the top or bottom of the board to avoid being burned. This is especially true at high track current levels. Also be sure to provide proper ventilation to the board. If placed in a case, that case must have proper ventilation. Consider using proper vent holes and a fan if you intend to place the EX-CSB1 inside an enclosure.

.. image:: /_static/images/ex-csb1/i2C_jumper_pads.png
   :alt: I2C Jumper Pads
   :scale: 45%
   :align: right

**I2C Jumper Pads** - There are 2 solder pad jumpers on the EX-CSB1 labelled "i2c". XXX why and when would I use these?

.. image:: /_static/images/ex-csb1/unpopulated_power_pins.png
   :alt: Unpopulated Power Pads
   :scale: 45%
   :align: right

**Unpopulated Power Connector** - These unpopulated solder pads are used internally for testing and can provide power connections for an optional header. When operated without an EX-MotorShield8874 on top, a user could remove the barrel jack and solder pins here capable of handling the 5A maximum current to power the board and the track.

.. image:: /_static/images/ex-csb1/pin_legend.png
   :alt: Pin Legend
   :scale: 40%
   :align: right

**Board Bottom Legend** - On the bottom of the board there are several markings such as the DCC-EX logo, board revision, and the QR code that links to this page on our website. Additionally, important pins are labelled should you need access to them from the top of the board headers. Input/Output (GPIO) pins are labelled "IO36", "IO39", etc. GND, 5V, and 3.3V are also labelled. Note that when an EX-MotorShield8874 is stacked on top for extra power districts, there are no free GPIO pins left to connect accessories directly the EX-CSB1. You must use the I2C pins and connect port expanders and/or servo boards to connect your accessories.




Powering the EX-CSB1
=====================

.. figure:: /_static/images/power/2_1mm_screw_terminal_adapter.png
   :scale: 40%
   :align: right
   :alt: 2.1mm screw terminal adapter

   2.1mm Screw Terminal Adapter

The CSB1 has a 2.1mm x 5.5mm power jack. If you already have a power supply with bare wires, you can use an optional 2.1mm x 5.5mm screw terminal block adapter. For more information about power supplies, including how to use one power supply to supply all the different voltages on your layout, see :ref:`Power Supplies <reference/hardware/power-supplies:power supplies>`.

To power up the CSB1, just plug your power supply into the mains power (aka wall outlet) and connect the barrel end to the Command Station. Make sure your power supply matches the needs of your setup: the voltage should be between 12V and 25V DC, depending on the scale of your locomotives, and it should provide at least 2A of current with good over-current performance and voltage stability. To get the most out of your EX-CSB1, we suggest using a moden switching power supply with 4A or more. For Z scale, 12V is usually enough, but for N, HO, and OO scales, we recommend using between 14V and 16V DC. It’s important that your DC power is well-regulated which is why we suggest a modern switch-mode power supply with double insulation and strong overload protection.

.. figure:: /_static/images/12v-3A-brick.jpg
   :alt: 12V 3A brick power supply
   :scale: 100%
   :align: right

   12V/3A Power Supply

Don't worry if your power supply offers more amps than you need. While too much voltage can be harmful, extra current isn't a problem since the CSB1 will only use as much as it needs. In fact, it's better to have a bit more current than too little. However, remember that both voltage and current can be dangerous if not handled properly. The barrel connector helps add some safety, but be cautious—if, for example, a metal tool accidentally touches the terminals of a high-powered supply, it could cause a short circuit.

For more details on how much current do I need, see [link] XXX

When you connect power to the CSB1, you should see one or both bright green power LEDs light up, confirming that the electronics are working. However, for safety, track power will be off by default when you first plug in the EX-CSB1. This is to prevent power from accidentally being applied to your layout before everything is ready. If you prefer, you can change this default setting [link] XXX.

DCC vs. DC PWM: A Quick Overview
================================

**DCC (Digital Command Control):** DCC uses a constant voltage on the track with digital signals embedded in the power to control the speed, direction, and functions of your trains. There’s no need to worry about polarity in DCC, making wiring simpler as your layout expands. The digital signal allows for precise control of multiple trains on the same track, all receiving power at the same time. Each device connected to the track contains a "decoder" that only responds to commands sent to its unique address.

**DC (Direct Current) PWM:** DC PWM operation suits traditional or legacy locomotive control, where the direction and speed of your trains are controlled by varying the voltage and switching polarity. In DC mode, one rail is positive with respect to the other. The train moves forward when voltage is applied and reverses direction when the polarity is flipped. DC control is simpler but less flexible, especially if you want to run multiple trains on the same track simultaneously. Under DCC-EX, DC PWM outputs are given a virtual DCC address which allows WiThrottle/DCC-EX throttles to control your DC locos on the piece of track powered by that output. The DC PWM frequency can be set using virtual DCC Functions 28-31 (XXX check!)

**Managing DCC and DC Modes in TrackManager:** If you are ready to dive into customizing your track outputs, TrackManager is the tool you'll use. It allows you to easily switch between DCC and DC modes for any track connected to your EX-CSB1. You can also set up different tracks for specific purposes, such as making one track a Booster, configuring your PROG track, or enabling Auto-Reverser mode.

For detailed steps on how to use TrackManager to change track modes and settings, check out the :doc:`TrackManager page </trackmanager/index>`.


Connecting and Testing Your Command Station
============================================

What you will need
--------------------

* An EX-CSB1 Command Station
* A Power supply (12V - 16V DC see :ref:`Power Supplies <reference/hardware/power-supplies:power supplies>`)
* A DCC loco (DC can work also)
* Track
* A throttle (You can use your phone or a computer - see below)
* 16 to 28AWG/1.5mm^2 Wire
* Jeweller's flat bladed screwdriver (1.5 - 2mm blade)
* A laptop or other computer*
* A USB cable*

 \*Optional for connecting connecting to a computer

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

DC Operation
-------------

When using DC mode with the EX-CSB1, it is important to understand that this is mode does not produce the traditional varying of the DC voltage to control the speed of your locomotive. The speed of your train is controlled using a method called PWM (Pulse Width Modulation), so instead, the track always receives full voltage whenever the throttle is set above zero.

**How PWM Works** - PWM works by rapidly turning the voltage on and off to the track. The rate at which this happens adjusts the "effective" voltage that the locomotive's motor experiences. For example, if the voltage is on 50% of the time and off 50% of the time, the motor behaves as if it's receiving half of the full voltage. This technique is similar to how a DCC decoder controls a motor in a DCC-equipped locomotive. See the image below from Sparkfun.com for an example:

.. figure:: /_static/images/power/sparkfun_pwm.png
   :alt: PWM waveform image
   :scale: 30%
   :align: center

   PWM Waveform Image. Click the image to enlarge.

**Benefits of PWM in DC Operation** - Using PWM for speed control has several advantages, particularly in terms of smooth operation. Trains start and stop more gradually, and running at slow speeds becomes smoother and more consistent. This gives you better control over your locomotives, making your layout more enjoyable to operate, especially during more delicate maneuvers.

**Frequency of PWM in DC Operation** - PWM can use a variety of frequencies for the pulses it sends, and this can alter motor behaviour and noise etc. The default frequency used for the CSB1 is xxHz, but this can be varied using the virtual DCC functions 28-31 (check) to allow you to alter the frequency to better suit your loco's motor. This can of course be done during running from the throttle.

XXX - map of function number to frequency

Track Outputs
--------------

You will notice that the two track outputs on the EX-CSB1 are labelled A and B. In the standard DCC-EX configuration of a CSB1, A is configured for DCC MAIN operation, and B is configured for PROG or programming track output. We recommend connecting your track to the A MAIN output initially to test your Command Station. To alter this default configuration of DCC outputs, or for DC Mode, you would need to configure outputs with a TrackManager command in the mySetup.h file or via Routes. See :doc:`the TrackManager page </trackmanager/index>`

[screw terminal image] XXX

The pluggable male screw terminals accept to 16 to 28 AWG/1.5mm^2 gauge solid or stranded wire. If you use stranded, we recommend "tinning" the ends of the wire to make a good connection and ensure that stray wire whiskers don't stray outside the screw terminals and cause a short circuit. Larger wire can handle more current and provide less resistance.  18-22 AWG is a good start. Keep your wires short by mounting the CS close to the track. See XXX for more information or wire gauge.

Unscrew both screw terminals with a flat blade jeweller's screwdriver. The screws just need to be loosened enough to fit your wires into the holes. Tighten down both screws once you have inserted the wires.

[plug image]


Turning on Power
------------------

Now you can connect your track power supply to the barrel connector on the CSB1 and then plug the other end into the wall. You should see status information on the display including the CSB1 firmware version. (If you do not have a display, you will need to connect a serial monitor XXX This is a mess of having to have so many options and send people back and forth and have an entire section on using a serial monitor. Just link to it? Yeah... link to it... it's why I insisted on an OLED display XXX PMA :-P )

The DCC-EX EX-CSB1 Command Station/Booster will power up in WiFi Access Point mode as configured out of the box, with a Wifi network SSID of DCCEX_xxxxxx and password of PASS_xxxxxx, both of which will be visible on the OLED display (or serial monitor log) after it boots.

XXX figure link to OLED display. Also link to serial monitor log section?

Access Point (AP) mode creates a separate WiFi network on the Command Station itself, whereas Station (STA) mode allows the Command Station to join as a WiFi device on your home or layout WiFi network. We have the EX-CSB1 set to default to AP mode for convenience of being able to get up and running quickly.

The WiFi LED will illuminate once WiFi is configured and ready as an Access Point (or Station if reconfigured for STA mode.)

XXX figure link showing WiFi LED

Connecting a Throttle
----------------------

XXX suggest we cater for both Wifi and WebThrottle with just a link to a generic page... such as https://dcc-ex.com/throttles/software/index.html#gsc.tab=0 which we may need to make more generic?? XXX


Connecting via Wifi
^^^^^^^^^^^^^^^^^^^^

XXX should title be "connecting with your phone?" Do we link to the engine driver page or give a short version here? Or to we break up the page and the "next" button goes to a mirrored page so there is only one page to maintain?

Please connect your smartphone or tablet where you previously installed Engine Driver or WiThrottle to this WiFi network with the password shown on the OLED to begin running trains immediately! You have nothing further to do to start using your DCC-EX EX-CSB1. You can remove the protective cover on the OLED if you wish.

XXX figure image of phone logging in to the AP

::NOTE: Note too that some smart phones and tablets will try hard to only connect you to a WiFi network that has Internet access, and you may be asked if you really want to connect to a WiFi network without it. For the sake of getting up and running quickly, just dismiss such queries. In the next section we show you how to reconfigure the EX-CSB1 to join your home or layout WiFi network should you prefer it.

Connecting Via USB and EX-WebThrottle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

XXX Do we just link to the webthrottle page or do a quick version here?

Use TrackManager to Set Outputs to DCC or DC Operation
========================================================

XXX why is this restated?? (See somewhere above)

Our Trackmanager technology allows you to configure any of 4 outputs to be DCC MAIN, DCC PROG, or DC PWM in order to run DCC or DC locos. 2 outputs are included with the EX-CSB1 with 2 more available with the purchase of an EX-MotorShield 8874 that just stacks on top. By default, output A is configured as a DCC MAIN track and output B is configured as a DCC PROG Programming track. You can dynamically change the configuration using throttles (such as |EX-WT|, |JMRI|, or |Engine Driver|) or you can configure your CSB1 to always start in your desired configuration. Note that one of the outputs can be configured in such a way that it is another MAIN power district that automatically switches to programming mode when a programming command is issued by your throttle and then automatically switches back to MAIN. XXX have this be a NOTE? See a detailed TM section?
