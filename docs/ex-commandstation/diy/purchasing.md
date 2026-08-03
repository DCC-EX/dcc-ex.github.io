::: 
:::

\|EX-CS-LOGO\|

# Purchasing Parts

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

:::: 

::: 
On this page
:::
::::

This page explains what you will need to acquire to build a \|EX-CS\|
using the recommended parts for a \|conductor-text\|.

Some of the parts (like track and some wire) you will likely already
have on hand.

::: rst-class
clearer
:::

## What you need to Acquire

::: sidebar
**Optional configuration**

\|conductor\| \|BR\| \|EX-CS\| can be configured in an additional
\'Conductor friendly\' way, without WiFi, but it requires \|JMRI\| to be
installed on a computer.

\|tinkerer\| \|engineer\| \|BR\| \|EX-CS\| is also supported on a
variety of different hardware that you might also consider

To help choose a suitable microcontroller, try our handy new table here:
`reference/hardware/microcontroller-boards:choosing a microcontroller`

- Supported
  `Arduino boards </reference/hardware/microcontroller-boards>`
- Supported
  `motor shields </reference/hardware/motor-boards>`
- Supported
  `ESP8266 WiFi shield </reference/hardware/wifi-boards>`
- Supported
  `Ethernet shield </reference/hardware/ethernet-boards>`
:::

### Hardware

You will need to find or purchase:

:::: 
::: title
Important
:::

**Uno R4 is not supported!** \|BR\| If you choose to purchase an Arduino
Uno (not recommended), it is vital that you purchase the **Revision 3
(R3)** version, `not` the
**Revision 4 (R4)** version. The \|EX-CS\|
`cannot run` on the R4
version.
`See here for more information</news/posts/20230728>`.
::::

1.  a supported **Arduino board** \|BR\| We recommend the [Elegoo Mega
    2560](https://www.amazon.com/ELEGOO-ATmega2560-ATMEGA16U2-Projects-Compliant/dp/B01H4ZLZLQ/)
    \|BR\| \|BR\|
2.  a supported **Motor Driver** \|BR\| We recommend either our own
    `EX-MotorShield8874 </reference/hardware/motorboards/ex-motor-shield-8874>` or the [Arduino Motor Shield
    Rev3](https://store.arduino.cc/collections/shields/products/arduino-motor-shield-rev3)
    \|BR\| \|BR\|
3.  a supported **WiFi shield** \|BR\| We recommend the [EX-WiFi Shield
    8266 (aka Makerfabs WiFi
    Shield)](https://www.makerfabs.com/esp8266-wifi-shield.html) \|BR\|
    \|BR\|
4.  Two (2) Male to Female **Jumpers leads** \|BR\| \|BR\|
5.  a 12-16v DC
    `power supply </reference/hardware/power-supplies>`[^1] for the \|motor shield\| \|BR\| We recommend [12v
    5Amp Power Supply for the
    Track](https://www.amazon.com/LEDMO-Power-Supply-Transformers-Adapter/dp/B01461MOGQ/)
    for Z and N Scale with the \|EX-MS\| \|BR\| \|BR\|
6.  a 2.5mm x 5.5mm Female DC Plug to **Screw Terminal (optional, but
    recommended)** to connect the \|motor shield\| power supply \|BR\|
    \|BR\|
7.  a **7-9v DC power supply** \|BR\| for the Arduino - be sure it is
    **tip positive** such as [this one on
    amazon](https://www.amazon.com/Adapter-Arduino-Schwinn-Elliptical-Recumbent/dp/B06Y1LF8T5/ref=sr_1_2_sspa)
    (while it is connected to the PC, this is not needed) NOTE: You do
    not need this power supply if you use the \|EX-MS\|. It powers the
    Arduino \|BR\| \|BR\|
8.  any **computer** running Windows, macOS, or Linux (only needed for
    the initial install of the software) \|BR\| \|BR\|
9.  a **USB Cable** from the computer to the Arduino \|BR\| \|BR\|
10. a **piece of track** to run trains or program on \|BR\| \|BR\|
11. some **wire** (18 to 16 AWG twisted pair recommended[^2].) \|BR\|
    \|BR\|
12. a \'known\' working **DCC-equipped locomotive**

\|HR-DASHED\|

:!!! note "::: title
Note"
:::

You can also find more detailed hardware information in the
`/reference/hardware/index` section. Check
our list of dealers to find some products locally to you.
::::

\|force-break\|

### Software

Our \|EX-I\| app is recommended for most users as it automatically
downloads and installs the required software.

13. See the
    `Command Station download page </download/ex-commandstation>` to download a copy to your computer.

### A Throttle (Controller)

14. You\'ll also need something to control your trains. \|BR\| There are
    several options. We will discuss these following the system setup,
    but the introductory configuration covered in the following pages
    lends itself to using a smart phone (Android or Apple iOS).

\|HR-HEAVY\|

## Next Steps

Click the \'Next\' button to see how to assemble your \|EX-CS\|.

[^1]: The voltage you need for the [\|Motor
    Driver\|](##SUBST##|Motor Driver|) depends on the scale/gauge of the
    layout you are using. Bigger is not always better. Too high a
    voltage can damage your locos. See the
    `reference/hardware/power-supplies:powering the motor driver` for more information.

[^2]: **Wire Gauge** - The standard Arduino/Deek [\|Motor
    Driver\|](##SUBST##|Motor Driver|) can only provide about 1.5 Amps
    of power (despite being rated for 2A), so 18 AWG wire is ample. If
    you use a different [\|Motor Driver\|](##SUBST##|Motor Driver|) and
    deliver more current to your track, you may need thicker wire (lower
    number gauge).
