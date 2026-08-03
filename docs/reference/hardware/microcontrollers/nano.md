\|EX-CS-LOGO\|

# Arduino Nano (Not recommended)

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

**As of version 5.4.0, this is no longer a recommended option, see**
`/news/posts/20250301`{.interpreted-text role="doc"}

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="1" local=""}
On this page
:::
::::

The Arduino Nano is an Uno in disguise. It has the same processor, the
same speed, the same (small) amount of memory. It\'s just small. The
disadvantage is that you can\'t plug shields on top of it, but the
benefit is that it can fit in a small box. You can always use all the
same Uno shields, like the full-sized \|motor shield\|, you just have to
solder or use wire jumpers to make the connections.

:::: note
::: title
Note
:::

Be sure to compare the Mega before using the Nano
::::

Validate none of the limitations of a Nano will prevent you using
features you will need by reading through the section on
`ex-commandstation/advanced-setup/index:microcontrollers`{.interpreted-text
role="ref"}.

![Arduino Nano](/_static/images/microcontrollers/nano.png)

## What You need

**Hardware**

- Arduino Nano (or clone)
- Gravitech Nano Motor Shield (or clone, or any supported \|motor
  shield\|)
- 5V 1A Power Supply with Mini-USB for Arduino and Micro-USB for clones
- 12-14.5V 3-5A Power Supply[^1] for the \|motor shield\|
- Barrel Connector to Screw Terminal Adapter if using the Nano Motor
  Shield
- Wire of the appropriate gauge for hookup
- Computer to load the software (Windows, Mac, Linux)

## Software

- See
  `Command Station Download Page </download/ex-commandstation>`{.interpreted-text
  role="doc"}
- A Controller (aka Throttle or CAB). More on this below.

## Optional Hardware

Supported
`ESP8266 WiFi Option </reference/hardware/wifi-boards>`{.interpreted-text
role="doc"}

:::: note
::: title
Note
:::

Before you order a Nano, be sure whether the headers are soldered or
not. The Arduino brand is not soldered, while many of the Chinese sites
give you the option. If you are a conductor, you probably don\'t want to
solder. If you are an Engineer, you may want to solder directly to the
board and having to unsolder headers would be an unwelcome surprise.
::::

## Using the special Nano Motor Shield

<figure class="align-left">
<img src="/_static/images/motorboards/nano_gravitech.png"
alt="Gravitech Nano Motor Shield" />
<figcaption aria-hidden="true">Gravitech Nano Motor Shield</figcaption>
</figure>

<figure class="align-left">
<img src="/_static/images/motorboards/nano_cheap_motor_shield.png"
alt="Nano Motor Shield Clone" />
<figcaption aria-hidden="true">Nano Motor Shield Clone</figcaption>
</figure>

\|force-break\|

The above image shows a Gravitech Nano Motor Shield on the left, and a
clone from China on the right. The image on the left shows a Nano
(separately purchased) plugged into the board. Search \"Nano Motor
Shield\" or \"Nano-L298p\". And remember to order a Nano from the same
source or from someone else.

The Gravitech is available from RobotShop and direct from Gravitech for
\$29 US plus shipping. The Chinese clone costs between \$9 and \$18
(shipping included) from sources like AliExpress, eBay, Amazon, etc.

:::: note
::: title
Note
:::

There is a slight difference in the brand name Gravitech board and the
board from the Chinese suppliers. There is a reset button on the Chinese
board for one. We will post more information when we can test them
side-by-side.
::::

To use this board, you simple plug the Nano into the motor shield
(really a carrier board), upload the software and wire it to your track.
It is just as easy as Using a Mega and an Arduino Motor shield.

::: todo
[LOW -
Hardware](https://github.com/DCC-EX/dcc-ex.github.io/issues/422) -
Finish the above and the below sections
:::

::: todo
[LOW -
Hardware](https://github.com/DCC-EX/dcc-ex.github.io/issues/422) - Show
VCC power wiring option
:::

::: todo
[LOW -
Hardware](https://github.com/DCC-EX/dcc-ex.github.io/issues/422) - Show
all the other Nano sized terminal boards and the ethernet board
:::

## Wiring a Motor Shield

You will need jumpers to connect the Nano to the Arduino Motor Shield

## Wiring other Motor Boards

As long as you know the pinouts, you can jumper wires to any motor
shield you can connect to an Uno or Mega.

[^1]: The voltage you need for the [\|Motor
    Driver\|](##SUBST##|Motor Driver|) depends on the scale/gauge of the
    layout you are using. Bigger is not always better. Too high a
    voltage can damage your locos. See the
    `reference/hardware/power-supplies:powering the motor driver`{.interpreted-text
    role="ref"} for more information.
