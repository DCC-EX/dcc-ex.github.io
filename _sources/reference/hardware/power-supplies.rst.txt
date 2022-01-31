****************
Power Supplies
****************

The power supply is one of the most important parts of your setup. You need to select a clean, filtered power supply that can supply the correct voltage and deliver the amount of current required by your devices.

**What's covered here:**

* :ref:`Do I need two power supplies?`
* :ref:`Four ways to power the Arduino`
* :ref:`Powering the Motor Controller`
* :ref:`Wall Warts`
* :ref:`Bricks (Laptop Style)`
* :ref:`Adjustable Power Supplies`
* :ref:`Cage Power Supplies`
* :ref:`Dual voltage power supplies`
* :ref:`Using one power supply with cheap converters to power everything`
* :ref:`Using Buck Converters`


Do I need two power supplies?
==============================

Well, you at least need two voltages. It is possible to get multiple voltages from one power supply, how to do that is covered below in the :ref:`Using one power supply with cheap converters to power everything`. Both your microcontroller (the Arduino) and the motor controller need power. While we recommend a 7-9 Volt, 1 Amp, DC power supply for an Arduino Uno or Mega, there are other ways to power it. The voltage requirement to the motor controller does not change based on how you power your Arduino, you need the correct voltage and amperage for your guage and layout.

Four ways to power the Arduino
----------------------------------

**Barrel Connector** - This is where we can connect our 7-9V DC supply. The power goes through a voltage regulator on the Arduino and converts the 7-9V to the 5V the board can use. You will still need a separate source of power for the motor controller.

**Vin pin** - You can connect a 7-9V DC power supply with jumper wires. The positive from the power supply goes to Vin and negative to any pin marked "gnd" for ground. This also uses the voltage regulator on the Arduino to convert your supply voltage to 5V. You will still need a separate power supply for the motor controller.

**USB Connector** - If you always will have a computer connected to your Command Station (for example when using JMRI or exWebThrottle), the 5V from your computer can power it. You won't need separate power supply in addition to the one you need for the motor controller. Most USB ports can only supply 500 milliamps, and this input is protected by a 500mA polyfuse that resets when a short is removed, so be careful about adding anything that will draw current from the CS. A motor shield, a wifi shield and a fan that draws 50mA should be fine. Even if you don't have a laptop, you can use a 5V, 800mA or more USB power supply like a phone charger and connect it to the USB port.

**5V pin** - Engineers only! Arduino recommends against this. You can connect a good quality 5V power supply directly to the 5V pin and ground. You can NOT ever plug anything into the other power connectors if you connect power this way! This bypasses the voltage regulator on the board which means you can use more current. But it also connects voltage to the output of the 5V regulator. Be aware that there is no diode for reverse voltage protection and no fuse for overcurrent. Research this option before attempting it.

**Barrel Connector and USB at the same time?** You may wonder what happens if you have a 7-9V power supply connected to the barrel connector and plug your laptop into the USB port to use the serial monitor. The Uno and Mega actually have a conflict protection circuit. If you plug in a 7V or more power supply to the barrel connector, the Arduino automatically switches internally to use that power supply. So regardless of which connector you plug in first, if the barrel connector has a voltage 7V or greater applied to it, that is the voltage the Arduino will use and the USB connection will just provide communication signals.

.. warning:: We recommend only a 7-9V DC power supply for your Arduino because, despite what may be said on a specification sheet, anything over 5V is generates unnecessary heat in the voltage regulator on an Arduino. There is a 2V voltage drop in this regulator, so you need a minimum of 7 volts to power the board. 7-9 is perfect. If you used 12V and connected a WiFi board or other devices that also use the 5V power supply on the arduino, the voltage regulator is likely to overheat.

Powering the Motor Controller
-------------------------------

Voltage
^^^^^^^^^

N and Z scale layouts should run at at about 12V-14V to avoid damage to the motors. See this thread to learn more about the pros and cons of running at higher voltages at this `Trainboard Thread <https://www.trainboard.com/highball/index.php?threads/dcc-voltage-and-n-scale-locomotives.56342/>`_ Another good link (along with just about anything written by Mark Gurries), is here: `Mark Gurries - Choosing the Right Booster <https://sites.google.com/site/markgurries/dcc-welcome-page/advanced-topics/boosters/choosing-the-right-booster>`_

Most larger scales will run higher voltages. For reference, Digitrax systems put the rails at around 14V and garden scale could be 18V. Do some homework to determine what voltage is best for your system.

Amperage
^^^^^^^^^

A 3A power supply will give you plenty of current to handle the maximum of 2A on channel A to the MAIN track (assuming you're using the Arduino motor shield or Pololu motor shield). Channel B for the programming track will only be used occasionally and does not need much current. In fact, it is limited to protect your trains (normally to 250mA). Running trains on main and programming a loco on Prog at the same time will be fine. The overcurrent limit set in the CS will automatically cut power if you go over that number of Amps. A rule of thumb is you can operate 3 to 5 N or HO sound locos on the 2A boards. For larger layouts with higher current requriements on the MAIN track and a motor driver that can handle those currents, you'll want power supply that can deliver that larger current. See :doc:`Motor Boards <motor-boards>` for more information about higher current motor controllers.

A device will only draw the current it needs. So whether you have a 2A power supply or a 20A power supply, if you setup only needs 1A, then both supplies will work just fine, but no sense paying for more than you need. And it is also worth noting that devices that can supply a large current can cause a large amount of damage if you don't have proper safety features installed like the overprotection feature of the CS AND fuses to the track.

.. warning:: If you think you need more that 5 Amps to your track, you should strongly consider using boosters and power districts. 

Wall Warts
=============

* Wall warts are a good choice for beginners and those not comfortable with mains wiring. You can get a 12V, 3A, relatively small one for around $8 US. 

.. image:: ../../_static/images/12v-3A-wall-wart-sm.jpg
   :align: left
   :scale: 100%
   :alt: 12V Wall Wart

|
|
|
|
|
|
|
|
|
|

Bricks (Laptop Style)
=======================

* You can also find plenty of laptop type "brick" power supplies. They come in ranges from 12V to 18V and 3-5 Amps.

.. image:: ../../_static/images/12v-3A-brick.jpg
   :align: center
   :scale: 100%
   :alt: 12V 3A Brick Power Supply



* This is a good 14V, 3A unit

.. image:: ../../_static/images/power/samsung_brick.jpg
   :align: center
   :scale: 25%
   :alt: Samsung brick

https://www.amazon.com/Samsung-Monitor-SoulBay-SyncMaster-Notebook/dp/B07QLRBLWC/ref=sr_1_3?dchild=1&keywords=14V+3A+power+supply&qid=1613861442&s=electronics&sr=1-3


Adjustable Power Supplies
==========================

* These have a selector switch to choose the voltage. Be careful to get a model that can deliver the current you need at the voltage you want. Sometimes the maximum output current will vary depending on the voltage selected.

.. image:: ../../_static/images/power/belker_adjustable.jpg
   :align: left
   :scale: 25%
   :alt: Belker_adjustable wall-wart

|
|
|
|
|
|


https://www.amazon.com/dp/B07J6RC43S/ref=cm_sw_r_cp_api_glt_fabc_HFY5CW4MH3XJXFXQT4BW

.. image:: ../../_static/images/power/belker_adjustable_45w.jpg
   :align: left
   :scale: 25%
   :alt: Belker_adjustable brick

|
|
|
|
|



https://www.amazon.com/Belker-5V-15V-Universal-Adapter-Speaker/dp/B015H0UPWU



   |
   |
   |


Cage Power Supplies
======================

* The Meanwell LRS-100-15 power supply is a good choice for larger scales. It supplies 15V and 105W (that's 7 amps), so it is plenty for running two channels simutaneously. At only $18, it is an inexpensive and solid option.

.. image:: ../../_static/images/meanwell-lrs100.jpg
   :align: left
   :scale: 100%
   :alt: Meanwell

`See on Digi-Key <https://www.digikey.com/product-detail/en/mean-well-usa-inc/LRS-100-15/1866-3313-ND/7705005>`_

.. warning:: For the Meanwell LRS-100-15 you will need to do your own mains wiring. If you don't have experience with this get a friend who does or hire an electrician to do it for you. **MAINS POWER IS DANGEROUS!**

Dual voltage power supplies
=============================

With a dual voltage power supply, you can provide 12V for the motor controller and 5V for the Arduino. You may also be able to find higher voltage units if you need such as 14-15V if your scale trains require it.

* Mean Well Dual Voltage Power Supply (5V and 12V)

.. image:: ../../_static/images/meanwell_rd125A.jpg
   :align: left
   :scale: 100%
   :alt: Mean Well RD125A Dual voltage power supply

`See on Amazon <https://www.amzn.com/B005T9FF4I/>`_

.. warning:: For the Meanwell RD125A, you will need to do your own mains wiring. If you don't have experience with this get a friend who does or hire an electrician to do it for you. **MAINS POWER IS DANGEROUS!**

Using one power supply with cheap converters to power everything 
====================================================================

**Tinkerers and Engineers**

* Using this method, you select a power supply that can power the track (or your highest voltage devices) and deliver enough Amps to power everything you will connect to it. This includes the DC-DC downconverters (Buck Converters) that take your higher voltage and reduce it to 5V, 7V, 9V, etc. Note that most buck converters are also boost converters, then can take a lower voltage and raise it to a higher one. We will just cover the first option here.

.. NOTE:: You will still need a wall voltage AC to 12-18V DC power supply with enough Amperage to handle what you want to power. Ex: You need 5A max to the track, are powering 2A worth of lights, and you have 2A of accessories. That is 9A. So you should get a 10A or greater power supply.

15V 13A Power Supplies
-----------------------

Some options for a power supply are the **Meanwell SP-200-15** or the **ATOS-300-15**. They are 15V, 13A supplies. You can use 15V to the motor controller and use buck converters to step down the 15V to whatever voltages you need.

.. image:: ../../_static/images/power/15v_13A_power_supply.jpg
   :align: center
   :scale: 50%
   :alt: 15V 20A supply

Here is a link to where you can find the `Meanwell SP-200-15 Power Supply <https://www.walmart.com/ip/NEW-Mean-Well-15Vdc-PFC-Power-Supply-SP-200-15/628549676?wmlspartner=wlpa&selectedSellerId=844>`_

Using Buck Converters
-----------------------

The following image shows how to connect buck converters. You start with a power supply with more voltage than the highest voltage you want to convert and with enough current to drive everything you want to power. This example shows a 15V supply that you can connect directly to the input to the motor controller which will in turn power your track. If you need to power 5V and 12V devices, you simply get 2 buck converters, connect them in parallel to the 15V output of your power supply (or to extra 15V outputs on the supply), and adjust each one to the voltage output you want. Then connect the converters to your 5V and 12V bus and connect your devices to the correct bus.

.. image:: ../../_static/images/power/using_buck_converters.jpg
   :align: center
   :scale: 70%
   :alt: Using Buck Converters

High Power Buck Converters
----------------------------

These come in different sizes. Show here is a 2A and a 6A Version. You can look for "60W 6A Adjustable Voltage Regulator with Cooling Fan", or "DC to DC 5.5V-30V to 0.5V-30V Power Supply Module". Or just "Buck Boost Voltage Converter". The bigger unit usually comes with a fan. A model number is a **"ZK-DP60"**.

.. image:: ../../_static/images/power/35W_4A_variable_buck_w_display.jpg
   :align: left
   :scale: 20%
   :alt: 35W 4A 5-24v Buck Power Supply

.. image:: ../../_static/images/power/60W_6A_variable_buck_w_display.jpg
   :align: left
   :scale: 18%
   :alt: 60W 6A 5-24V Buck Power Supply

|
|
|
|
|
|
|
|
|
|

**One example from Amazon**, click to follow the link: `5 to 30V Adjustable regulator converter <https://www.amazon.com/DROK-5-5-30V-Adjustable-Regulator-Converter/dp/B07VNDGFT6/ref=pd_vtp_6?pd_rd_w=NMR1C&pf_rd_p=55cbb45e-2534-4809-9135-12f41eecb852&pf_rd_r=696YH3MQ2QHKXXR9VDW0&pd_rd_r=3e7133ca-ea27-4967-8d7e-ea1c40c8381a&pd_rd_wg=GZd2x&pd_rd_i=B07VNDGFT6&psc=1>`_


4 Pack of Buck Regular Converters
-----------------------------------

.. image:: ../../_static/images/power/4_pack_buck_converters.jpg
   :align: center
   :scale: 22%
   :alt: 4 pack of buck converters

These are Input Voltage: DC 4-38V, error ±0.1V. Output Voltage: DC 1.25V to 36V at 5A.

https://www.amazon.com/dp/B079N9BFZC?tag=amz-mkt-chr-us-20&ascsubtag=1ba00-01000-a0049-win10-other-nomod-us000-pcomp-feature-scomp-wm-5&ref=aa_scomp


Cheap Buck Converter with Display $5
---------------------------------------

.. image:: ../../_static/images/power/20W_DC_buck.jpg
   :align: center
   :scale: 30%
   :alt: 20W DC Buck converter with display

This is a push button programmable 20W adjustable DC-DC buck converter module with digital display. It is based on LM2596 3A step-down voltage regulator and supports an input of 0~40V DC to an output of 1.25 to 37V with an accuracy of ± 0.05V.

Here is one example sold by DFRobot, click to follow the link: `20W 3A programmable buck converter <https://www.dfrobot.com/product-1552.html?gclid=CjwKCAiAg8OBBhA8EiwAlKw3ks8tC8ywVBKBOQ6dKOSRZZSxoKMphpav7r7WmfW29Nl9uU7Mn7SJzRoCMSUQAvD_BwE>`_

