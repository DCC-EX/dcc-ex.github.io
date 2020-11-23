Power Supplies
==============

The power supply is one of the most important parts of your setup. You need to select a clean, filtered power supply that can supply at least the amount of current required by your motor controllers. 

Do I need two power supplies?
-----------------------------

Both your microcontroler (the Arduino) and the motor controller need power. While we recommend a 9 Volt, 1 Amp, DC power supply for the microcontroler, there are other ways to power it. The voltage to the motor controller does not change, you need the correct voltage and amperage for your guage and layout.

Three ways to power the Arduino
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Barrel Connector** - This is where we can connect our 7-9V DC supply. The power goes through a voltage regulator on the Arduino and converts the 9V to the 5V the board can use. You will still need a separate source of power for the motor controller.

**Vin pin** - You can connect a 7-9V DC power supply with jumper wires. The positive from the power supply goes to Vin and negative to any pin marked "gnd" for ground. This also uses the voltage regulator on the Arduino to convert your supply voltage to 5V. You will still need a separate poer supply for the motor controller.

**USB Connector** - If you always will have a computer connected to your Command Station (for example when using JMRI or exWebThrottle), the 5V from your computer can power it. You won't need separate power supply in addition to the one you need for the motor controller. Most USB ports can only supply 500 milliamps, and this input is protected by a 500mA polyfuse that resets when a short is removed, so be careful about adding anything that will draw current from the CS. A motor shield, a wifi shield and a fan that draws 50mA should be fine. Even if you don't have a laptop, you can use a 5V, 1A USB power supply like a phone charger and connect it to the USB port.

**5V pin** - You can connect a good quality 5V power supply directly to the 5V pin and ground. This bypasses the voltage regulator on the board which means you can use more current. We recommend a 5V, 1A power supply. Since there are many dual-voltage power supplies on the market, you can use one power supply with two outputs. Be aware that there is no diode for reverse voltage protection and no fuse for overcurrent

**Barrel Connector and USB at the same time?** You may wonder what happens if you have a 7-9V power supply connected to the barrel connector and plug your laptop into the USB port to use the serial monitor. The Uno and Mega actually have a conflict protection circuit. Whichever you plug in last wins. So if you plug in the USB cable first, then plug in the external power supply, the power supply will be the one supplying power and the USB connection will just provide communication signals.

.. warning:: We recommend only a 7-9V DC power supply for your Arduino because, despite what may be said on a specification sheet, anything over 5V is generated as heat in the voltage regulator on an Arduino. There is a 2V voltage drop in this regulator, so you need a minimum of 7 volts to power the board. 7-9 is perfect. If you used 12V and connected a WiFi board or other devices that also use the 5V power supply on the arduino, the voltage regulator is likely to overheat.

Powering the Motor Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Voltage
~~~~~~~

N and Z scale layouts should run at at about 12V-14V to avoid damage to the motors. See this thread to learn more about the pros and cons of running at higher voltages at this `Trainboard Thread <https://www.trainboard.com/highball/index.php?threads/dcc-voltage-and-n-scale-locomotives.56342/>`_ Another good link (along with just about anything written by Mark Gurries), is here: `Mark Gurries - Choosing the Right Booster <https://sites.google.com/site/markgurries/home/technical-discussions/boosters/choosing-the-right-booster>`_

Most larger scales will run higher voltages. For reference, Digitrax systems put the rails at around 14V. Do some homework to determine what voltage is best for your system.

Amperage
~~~~~~~~

You'll need to be able to supply 3A on channel A to the MAIN track (assuming you're using the Arduino motor shield or Pololu motor shield). Channel B for the programming track will only be used occasionally and does not need much current. In fact, it is limited to protect your trains. For larger layouts with higher current requriements on the MAIN track and a motor driver that can handle those currents, you'll want power supply that can deliver that current.

.. warning:: If you think you need more that 5 Amps to your track, you should strongly consider using boosters and power districts. 

Recommended Power Supplies
--------------------------

* Wall warts are a good choice for beginners and those not comfortable with mains wiring. You can get a 12V, 3A, relatively small one for around $8 US. 

.. image:: ../../_static/images/12v-3A-wall-wart-sm.jpg
   :alt: 12V Wall Wart

* You can also find plenty of laptop type "brick" power supplies. They come in ranges from 12V to 18V and 3-5 Amps.

.. image:: ../../_static/images/12v-3A-brick.jpg
   :alt: 12V 3A Brick Power Supply

* The Meanwell LRS-100-15 power supply is a good choice for larger scales. It supplies 15V and 105W (that's 7 amps), so it is plenty for running two channels simutaneously. At only $18, it is an inexpensive and solid option.

.. image:: ../../_static/images/meanwell-lrs100.jpg
   :alt: Meanwell

`See on Digi-Key <https://www.digikey.com/product-detail/en/mean-well-usa-inc/LRS-100-15/1866-3313-ND/7705005>`_

.. warning:: For the Meanwell LRS-100-15 you will need to do your own mains wiring. If you don't have experience with this get a friend who does or hire an electrician to do it for you. MAINS POWER IS DANGEROUS.

Dual voltage power supplies
^^^^^^^^^^^^^^^^^^^^^^^^^^^

With a dual voltage power supply, you can provide 12V for the motor controller and 5V for the Arduino. You may also be able to find higher voltage units if you need such as 14-15V if your scale trains require it.

* Mean Well Dual Voltage Power Supply (5V and 12V)

.. image:: ../../_static/images/meanwell_rd125A.jpg
   :alt: Mean Well RD125A Dual voltage power supply

`See on Amazon <https://www.amzn.com/B005T9FF4I/>`_

.. warning:: For the Meanwell RD125A, you will need to do your own mains wiring. If you don't have experience with this get a friend who does or hire an electrician to do it for you. MAINS POWER IS DANGEROUS.
