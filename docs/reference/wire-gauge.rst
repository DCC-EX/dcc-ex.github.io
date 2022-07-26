.. include:: /include/include.rst
************************
Wire Gauge Information
************************

Why is Wire Size Important?
============================

Voltage, current, and resistance to that current are all interrelated and described by the Ohm's law formula, Voltage = Current * Resistance (V=IR). The thinner the wire, the more resistance it has. As you can see from the formula, if your wire had a .5 Ohm resistance and there was 5 Amps flowing through it, you would lose... we're waiting. Get out your calculator... Yes, 2.5 Volts. If you only started with say, 12V, that would leave you with only 9.5 to run your trains. And that lost energy is wasted as heat. This is an exaggerated example, but you get the idea.

There can be a lot of wiring on a complicated layout, here are the main areas that require wiring, they are often different wire sizes.

* The main DCC Bus
* Feeder wires
* The accessory bus (optional)


Main DCC Bus
=============

The main bus provides a low resistance, high current capable path for the voltage and current to your track. It may power several locos and all your lights, servos, switches and other accessories. Optionally, you may want to have a separate bus for accessory control and reserve the main bus just for your locos. More on that later.

.. todo::
   Add link here. fnd

.. image:: /_static/images/icons/thumb_up.png
   :alt: thumbs-up icon
   :scale: 100%
   :align: left

**Rule of Thumb:** 14 gauge (2.08mm\ :sup:`2`) solid core wire for main bus up to 100ft (30m) for HO.  24 gauge (.205mm\ :sup:`2`) stranded wire for short feeder wires from the bus to short sections of track around the layout.

.. NOTE:: In the USA the smaller the number, the bigger the wire!

Our general rules are based on 2 to 5 Amps of current maximum. Most model railroaders will be well within this range, most never going above 2 Amps. If you need more than 5 Amps, then you need separate power districts to distribute the load around the track. For example, you have have a motor or a lot of lights connected to one part of the track in its district. Breaking the track up into power districts ensures that there probably won't me more than few locos in any district in a given time.

Feeders
========

Feeder wires a smaller, more manageable wires that you run from the main bus to the tracks. You will need feeders every few feet on larger scales and on every track for N and Z scales. The wires can be smaller because they are only a few inches long and the current is distributed between feeders.

Current
========

If you want to compute how much current you are actually going to use, you will have to refer to some tables. You may need a different size wire. For example to only carry 2 Amps, your bus wire can be 18 gauge. To handle more than 5A, you would need larger wire.

Here are some examples of the electrical specifications of a few sizes of wire:

+-------+--------+--------+--------+--------+---------+--------+------+---------+
| AWG   | dia.   | dia.   | x-Sec. | Ohms   | Ohms    | Amps   | Amps | freq.   |
| gauge | in.    | mm.    | mm2    | 1000ft | km.     | feeder | bus  | skin ef.|
+=======+========+========+========+========+=========+========+======+=========+
| 10    | 0.1019 | 2.5882 | 5.26   | 0.9989 | 3.2763  |  55    | 15   | 2600 Hz |
+-------+--------+--------+--------+--------+---------+--------+------+---------+
| 12    | 0.0808 | 2.0523 |  3.31  | 1.588  | 5.2086  |  41    | 9.3  | 4150 Hz |
+-------+--------+--------+--------+--------+---------+--------+------+---------+
| 14    | 0.0641 | 1.6281 |  2.0   | 2.525  | 8.282   |  32    | 5.9  | 6700 Hz |
+-------+--------+--------+--------+--------+---------+--------+------+---------+
| 16    | 0.0508 | 1.2903 |  1.31  | 4.016  | 13.1724 |  22    | 3.7  | 11 k Hz |
+-------+--------+--------+--------+--------+---------+--------+------+---------+
| 18    | 0.0403 | 1.0236 | 0.823  | 6.385  | 20.9428 |  16    | 2.3  | 17 kHz  |
+-------+--------+--------+--------+--------+---------+--------+------+---------+
| 20    | 0.032  | 0.8128 | 0.519  | 10.15  | 33.292  |  11    | 1.5  | 27 kHz  |
+-------+--------+--------+--------+--------+---------+--------+------+---------+
| 22    | 0.0253 | 0.6451 | 0.327  | 16.14  | 52.9392 |   7    | 0.92 | 42 kHz  |
+-------+--------+--------+--------+--------+---------+--------+------+---------+
| 24    | 0.0201 | 0.5105 | 0.205  | 25.67  | 84.1976 |   3.5  | 0.577| 68 kHz  |
+-------+--------+--------+--------+--------+---------+--------+------+---------+
| 26    | 0.0159 | 0.4038 | 0.128  | 40.81  | 133.8568|   2.2  | 0.361| 107 kHz |
+-------+--------+--------+--------+--------+---------+--------+------+---------+
| 28    | 0.0126 | 0.3200 | 0.080  | 64.9   | 212.872 |   1.4  | 0.226| 170 kHz |
+-------+--------+--------+--------+--------+---------+--------+------+---------+

You can see from the above table, for example, that 14 gauge wire can handle a 5Amp current, and 22 gauge wire would be good for feeders. But don't trust this table, especially if you are using higher currents and have a large layout. Voltage, current, length of wire and the fact that these numbers are for 50/60 cycle house current instead of our ~8kHz DCC, mean that the more current you are going to use, the more you will need to know. Find more information in the following resources:

https://dccwiki.com/Wire_Sizes_and_Spacing

https://tonystrains.com/news/wire-sizes-to-use-in-dcc/

https://sites.google.com/site/markgurries/home/technical-discussions/track-wire-gauge-selection

http://www.sumidacrossing.org/LayoutControl/DCC/DCCLayoutPower/

A little more involved, but worth the read if you already are an experienced railroader:

http://4dpnr.com/wp-content/uploads/2015/07/DCC_Wiring.pdf

Read all the above and you will be a DCC-EX Engineer!

Accessory Bus
==============

If you have a small to medium sized layout you could usually power your locos, turnouts, and other accessories and lighting all from the power from the tracks. But there are a few reasons why you may want to expand your system to have a separate bus for accessories.

**1. Efficiency** - The Command station already has a lot to do if you are running a lot of locos. While you could run 10, 20... even 50 trains or more, each train can get only so many commands per second. If you are running in a club situation and If you add a lot of accessories, you could find a short delay before a train responds to something like an emergency stop.

**2. Voltage and current needs** - If you take the power requirements of your accessories off your main track, and power them from a separate supply, you can either run with less Amps or run more locos.

**3. Bi-Directional Communication** - The DCC standard provides no way for accessories or locos to talk back to the CS using the signal on the track. DCC++ EX *does* have this capability by using the GPIO pins as outputs to accessories and inputs from sensors instead of having decoders on your accessories. You can power your accessories with another power supply. There are also several bus structures and accessory control systems, like LCN, that allow not only a separate power system, but 2-way communication system with dedicated microcontrollers that handle turnouts, sensors, lights and other accessories. DCC++ EX can work directly with some of those systems with a simple software switch to hand off commands.


