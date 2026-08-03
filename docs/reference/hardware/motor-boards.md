\|EX-REF-LOGO\|

# Supported Motor Drivers

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="2" local=""}
On this page
:::
::::

\|EX-CS\| is compatible with a wide variety of motor drivers, also known
as \"dual H-bridges\" and \"motor shields\". We\'ve sorted them from
least difficult to most difficult to use to help you decide what to use.
When it comes to selecting a board, some considerations are size,
whether it is a shield or needs to be connected with jumper wires, the
amount of current you need, and whether it has current sensing
capability built-in or if you have to supply it yourself.

If you have trouble finding a particular board from the list, try
searching based on it\'s name or the type of chip on the board and the
terms \"H-Bridge\" or \"\|motor shield\|\". There are often many places
that sell these, especially the Chinese sites like AliExpress and
Banggood.

**TL;DR** (aka short version): We currently recommend the \|DCC-EX\|
EX-MotorShield8874, and the Arduino Motor Shield R3 or a supported clone
like the Deek-Robot.

![DCC-EX EX-MotorShield8874
RevA](/_static/images/motorboards/ex_motorshield8874.png)

![Deek Robot Motor
Shield](/_static/images/motorboards/deek-robot_motor_shield.png)

:!!! note "::: title
Note"
:::

Where appropriate, we have used the terms \"single\" and \"dual\" to
indicate on the non-shield type boards, which ones have just a single
H-Bridge for one track and which ones have two. A single H-Bridge board
will power your main track, but you will then need another board of some
kind to connect to your programming track
::::

## What is a Motor Driver?

A motor driver (aka \'motor controller\', aka \'motor shield\', aka
\'motor board\') is just a high voltage, high current switch. While
initially designed to power electric motors, we use it to create the DCC
signal to the track in a clever misapplication of technology. Normally,
a pulse width modulated (PWM) signal would be applied to a motor with
the PWM pin to control speed and the direction pin would switch the
voltage from positive to negative to control the motor spin direction.
Instead, we send full DC track voltage to the PWM pin and switch the
direction pin at the DCC frequency (around 8000 times a second) to
generate the bi-polar square wave. In this way, we use the 5V DC (or
3.3V) microcontroller output to switch the voltage from separate 12-16v
DC power supply[^1] connected to the \|motor driver\|, and create a
pulse train signal of 1\'s and 0\'s that a mobile decoder can interpret
as commands.

## Current list of boards

In this section we outline the various details that we know of related
to each of the different boards that we\'ve either tested, or know to
work based on user feedback.

We\'ve compiled this simple summary table to help with this:

::: {.flat-table .command-table widths="auto" header-rows="1"}
- - Type / Brand \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\|
    \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\|
  - R \|BRxb\| e \|BRxb\| c \|BRxb\| o \|BRxb\| m \|BRxb\| m \|BRxb\| e
    \|BRxb\| n \|BRxb\| d \|BRxb\| e \|BRxb\| d
  - S \|BRxb\| u \|BRxb\| p \|BRxb\| p \|BRxb\| o \|BRxb\| r \|BRxb\| t
    \|BRxb\| e \|BRxb\| d
  - Com- \|BRxb\| fort \|BRxb\| Level
  - For- \|BRxb\| mat
  - S \|BRxb\| t \|BRxb\| a \|BRxb\| c \|BRxb\| k \|BRxb\| a \|BRxb\| b
    \|BRxb\| l \|BRxb\| e
  - Short \|BRxb\| Cir- \|BRxb\| cuit \|BRxb\| Pro- \|BRxb\| tect-
    \|BRxb\| ion
  - Cur- \|BRxb\| rent \|BRxb\| Sen- \|BRxb\| se \|BRxb\|[^2]
  - DC \|BRxb\| Sup- \|BRxb\| port
  - No. \|BRxb\| Out- \|BRxb\| puts \|BRxb\| / \|BRxb\| Tra- \|BRxb\|
    cks
  - Max \|BRxb\| Amps \|BRxb\|[^3]
  - Comments / Notes \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\|
    \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\|
    \|\_xb\| \|\_xb\| \|\_xb\|
- - `DCC-EX EX-MotorShield8874 RevA</reference/hardware/motorboards/ex-motor-shield-8874>`{.interpreted-text
    role="doc"}
  - Yes
  - Yes
  - Conductor
  - UNO / Mega
  - Yes[^4]
  - Yes
  - Yes
  - Yes
  - 2
  - 5
  - 
- - `Arduino Motor Shield R3</reference/hardware/motorboards/arduino-motor-shield>`{.interpreted-text
    role="doc"}[^5]
  - Yes
  - Yes
  - Conductor
  - UNO / Mega
  - Yes[^6]
  - Yes
  - Yes
  - Yes
  - 2
  - 1.3 - 1.5
  - 
- - `Deek-Robot Motor Shield</reference/hardware/motorboards/deek-robot-motor-shield>`{.interpreted-text
    role="doc"}[^7]
  - Yes
  - Yes
  - Conductor
  - UNO / Mega
  - Yes[^8]
  - Yes
  - Yes
  - Yes
  - 2
  - 1.3 - 1.5
  - 
- - `Flashtree Motor Shield</reference/hardware/motorboards/flashtree-motor-shield>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Tinkerer
  - UNO / Mega
  - No
  - Yes
  - Yes
  - Yes
  - 2
  - 1.3 - 1.5
  - 
- - `DIY More L298NH</reference/hardware/motorboards/diy-more-l298nh-motor-shield>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Tinkerer
  - UNO / Mega
  - No
  - Yes
  - Yes
  - Yes
  - 2
  - 2
  - 
- - `YFRobot L298P</reference/hardware/motorboards/yfrobot-l298p>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Tinkerer
  - UNO / Mega
  - No
  - No
  - No
  - No
  - 2
  - 2
  - 
- - `L298N (dual)</reference/hardware/motorboards/L298N-motor-board-setup>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Engineer
  - 
  - No
  - No
  - No
  - No
  - 2
  - 2
  - It doesn\'t have current sense
- - `Dual Module H-bridge MOSFET IRF3205</reference/hardware/motorboards/IRF3205-motor-board-setup>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Tinkerer
  - 
  - No
  - No
  - No
  - No
  - 2
  - 15
  - 
- - `Pololu MC33926</reference/hardware/motorboards/pololu-mc33926>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Tinkerer
  - UNO / Mega
  - No
  - No
  - No
  - No
  - 2
  - 3
  - current sense is not acceptable. We recommend using an external
    current sense board like the MAX471
- - `MiniIBT L6201P (single)</reference/hardware/motorboards/miniibt-motor-driver-l6201p>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Tinkerer
  - 
  - No
  - No
  - ?
  - No
  - 1
  - 5
  - 
- - `BTS7960 IBT_2 (single)</reference/hardware/motorboards/IBT_2-motor-board-setup>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Tinkerer
  - 
  - No
  - No
  - ?
  - No
  - 1
  - 43
  - 
- - `Keyes/Fundumoto ("Beeper Board")</reference/hardware/motorboards/keyes-fundumoto>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Engineer
  - UNO / Mega
  - No
  - Yes[^9]
  - Yes[^10]
  - No
  - 2
  - 2
  - 
- - `Makerfabs H-Bridge</reference/hardware/motorboards/makerfabs-h-bridge-motor-shield>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Engineer
  - 
  - No
  - No
  - No
  - No
  - 2
  - 8
  - 
- - `Velleman KA03/VMA03</reference/hardware/motorboards/velleman-ka03-kit-vma03>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Engineer
  - 
  - No
  - No
  - No
  - No
  - 2
  - 2
  - 
- - `DFRobot 2x2A DC Motor Shield (DRI0009)</reference/hardware/motorboards/dfrobot-2x2a-dc-motor-shield>`{.interpreted-text
    role="doc"}
  - No
  - Yes
  - Engineer
  - UNO / Mega
  - No
  - No
  - No
  - No
  - 2
  - 2
  - 
- - VNH2SP30 - SparkFun Monster Moto and others
  - \-
  - `No`{.interpreted-text role="dcc-ex-red-bold-italic"}
  - `7`{.interpreted-text role="cspan"} -
  - Does not work. It can\'t switch fast enough to generate a reliable
    DCC signal
- - IFX9202ED - Infineon Dual H-Bridge
  - \-
  - `No`{.interpreted-text role="dcc-ex-red-bold-italic"}
  - `7`{.interpreted-text role="cspan"} -
  - Does not work. Can\'t switch fast enough.
- - DFRobot Romeo V2
  - \-
  - `No`{.interpreted-text role="dcc-ex-red-bold-italic"}
  - Engineer
  - `6`{.interpreted-text role="cspan"} -
  - Well, an Engineer could perhaps get this one to work.
- - Kuman Board (and any L293D based boards)
  - \-
  - `No`{.interpreted-text role="dcc-ex-red-bold-italic"}
  - `7`{.interpreted-text role="cspan"} -
  - Does not work. Not enough current.
- - Pololu TB9051FTG based motor shield
  - \-
  - `No`{.interpreted-text role="dcc-ex-red-bold-italic"}
  - `7`{.interpreted-text role="cspan"} -
  - Does not work. It can\'t switch fast enough to generate a reliable
    DCC signal
:::

### TrackManager DC compatible boards

:!!! warning "::: title
Warning"
:::

There are specific pin and hardware requirements in order to support DC
mode in \|TM\|. Use of any other board than this short list for DC mode
is unsupported by the \|DCC-EX\| team.
::::

For users wishing to use the new \|TM\| DC feature, there are a very
limited number of boards available for use, and only this list of boards
is supported:

- `/reference/hardware/motorboards/ex-motor-shield-8874`{.interpreted-text
  role="doc"}
- `/reference/hardware/motorboards/arduino-motor-shield`{.interpreted-text
  role="doc"}
- `/reference/hardware/motorboards/deek-robot-motor-shield`{.interpreted-text
  role="doc"}
- `/reference/hardware/motorboards/flashtree-motor-shield`{.interpreted-text
  role="doc"}
- `/reference/hardware/motorboards/diy-more-l298nh-motor-shield`{.interpreted-text
  role="doc"}

### Easy to use boards

\|conductor\|

::: {.toctree maxdepth="1"}
DCC-EX EX-MotorShield8874 - 5A \[RECOMMENDED\]
\</reference/hardware/motorboards/ex-motor-shield-8874\> Arduino Motor
Shield - 1.5A \[RECOMMENDED\]
\</reference/hardware/motorboards/arduino-motor-shield\> Deek-Robot -
1.5A \[RECOMMENDED\]
\</reference/hardware/motorboards/deek-robot-motor-shield\> Flashtree -
1.5A \</reference/hardware/motorboards/flashtree-motor-shield\> DIY More
L298NH - 2A
\</reference/hardware/motorboards/diy-more-l298nh-motor-shield\> YFRobot
L298P - 2A \</reference/hardware/motorboards/yfrobot-l298p\>
:::

### Intermediate boards

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

These boards require wiring.

::: {.toctree maxdepth="1"}
L298N (dual) - 2A
\</reference/hardware/motorboards/L298N-motor-board-setup\> Dual Module
H-bridge MOSFET IRF3205 - 15A
\</reference/hardware/motorboards/IRF3205-motor-board-setup\> Pololu
MC33926 - 3A \</reference/hardware/motorboards/pololu-mc33926\> MiniIBT
L6201P (single) - 5A
\</reference/hardware/motorboards/miniibt-motor-driver-l6201p\> BTS7960
IBT_2 (single) - 43A
\</reference/hardware/motorboards/IBT_2-motor-board-setup\>
:::

### Expert Level Boards

\|SUITABLE\| \|engineer\| \|support-button\|

These boards require you to add your own config to the config.h file,
and may not have good current sensing. That said, if you buy a separate
current sense board, we particularly like the IBT_2 board (though you
will need 2 of them or some other board for the programming track)

::: {.toctree maxdepth="1"}
Keyes/Fundumoto (\"Beeper Board\") - 2A
\</reference/hardware/motorboards/keyes-fundumoto\> Makerfabs H-Bridge -
8A \</reference/hardware/motorboards/makerfabs-h-bridge-motor-shield\>
Velleman KA03/VMA03 - 2A
\</reference/hardware/motorboards/velleman-ka03-kit-vma03\> DFRobot 2x2A
DC Motor Shield (DRI0009) - 2A
\</reference/hardware/motorboards/dfrobot-2x2a-dc-motor-shield\>
:::

### Incompatible boards

- VNH2SP30 - SparkFun Monster Moto and others. It can\'t switch fast
  enough to generate a reliable DCC signal
- IFX9202ED - Infineon Dual H-Bridge. Can\'t switch fast enough.
- `/reference/hardware/motorboards/dfrobot-romeo-v2`{.interpreted-text
  role="doc"} - Well, an Engineer could perhaps get this one to work.
- Kuman Board (and any L293D based boards) - not enough current.
- Pololu TB9051FTG based motor shield. It can\'t switch fast enough to
  generate a reliable DCC signal. [Product
  page](https://www.pololu.com/product/2520) \|EXTERNAL-LINK\|.

### Other boards

\|SUITABLE\| \|engineer\| \|support-button\|

While not fully supported and tested, other boards can potentially be
used. Look for the following criteria:

- We recommend a dual h-bridge board or two discrete h-bridge boards.
  They can be different sizes, one bigger for main track and one smaller
  for programming track operations.
- It must handle enough current for the layout. 2 amps will drive 3-5 HO
  scale locomotives.
- It must have working and accurate current sensing (many do not)
- It must be able to switch at least 10000 times per second (some do
  not)
- Look for an Arduino shield form factor to eliminate wiring (not
  required but preferred)

:!!! note "::: title
Note"
:::

Current capabilities of these boards, especially the boards based on the
L298 with no heat sink fins like the Arduino Motor Shield can really not
deliver 2 Amps. A realistic number would be 1.5 Amps IF you added a heat
sink and a cooling fan. If you need 2 Amps or more, you will need to go
with a higher current board.
::::

## Configuring Motor Drivers

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

If your board is not in the list of supported motor driver types, or if
you need to make changes or have more information about how motor
drivers are configured in \|EX-CS\|, see:

::: {.toctree maxdepth="1"}
Motor Driver Configuration Guide
\</reference/hardware/motorboards/motor-board-config\>
:::

## High Accuracy Waveform

\|SUITABLE\| \|engineer\| \|support-button\|

If you\'re experiencing issues with specific decoders and all attempts
to get them working are failing, you may need to enable the high
accuracy waveform functionality (providing your motor driver supports
it).

::: {.toctree maxdepth="1"}
High Accuracy Waveform Guide
\</reference/hardware/motorboards/high-accuracy\>
:::

[^1]: The voltage you need for the [\|Motor
    Driver\|](##SUBST##|Motor Driver|) depends on the scale/gauge of the
    layout you are using. Bigger is not always better. Too high a
    voltage can damage your locos. See the
    `reference/hardware/power-supplies:powering the motor driver`{.interpreted-text
    role="ref"} for more information.

[^2]: CV Programming

[^3]: Per output

[^4]: Requires modification of the board to stack the second board

[^5]: The *Arduino Motor Shield R38* and the *Deek-Robot Motor Shield*
    are interchangeably referred to in this documentation as the
    *standard motor driver*

[^6]: Can be stacked, but it is complicated. See
    `/reference/hardware/motorboards/arduino-motor-shield-stacked`{.interpreted-text
    role="doc"}

[^7]: The *Arduino Motor Shield R38* and the *Deek-Robot Motor Shield*
    are interchangeably referred to in this documentation as the
    *standard motor driver*

[^8]: Can be stacked, but it is complicated. See
    `/reference/hardware/motorboards/arduino-motor-shield-stacked`{.interpreted-text
    role="doc"}

[^9]: Requires modification of the board to support Current Sense

[^10]: Requires modification of the board to support Current Sense
