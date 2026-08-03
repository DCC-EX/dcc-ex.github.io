\|EX-CS-LOGO\|

# Do-It-YourSelf - Getting Started

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

:::: 

::: 
On this page
:::
::::

In order to get the most out of this website, we ask you at first to
make 2 choices:

1.  To self-identify your **\"level\"** with regards to DCC-EX. \|BR\|
    If you have not chosen whether you are a \|Conductor-text\|,
    \|Tinkerer-text\|, or \|Engineer-text\|, please go to the
    `/begin/levels` page before proceeding
    further. \|BR\| \|BR\|
2.  Choose whether you want the **\"Ready-To-Run\" (RTR)** path or the
    **\"Do-It-Yourself\" (DIY)** path. \|BR\| If you want the
    ready-to-run (RTR) path we suggest that you look at the
    `/ex-commandstation/rtr-index` page.

**If you are still interested the do-it-yourself (DIY) path then read
on\...**

You are here on the DIY path where you will build your own \|EX-CS\|
from commonly available parts.

The following pages will instruct you on how to build an \|EX-CS\|
including; assembling your hardware, installing software, and running
your first train.

After that, we will provide examples for how the \|EX-CS\| can be
extended and upgraded.

\|HR-DASHED\|

## The Components of a Full EX-CommandStation

To actually run your model railroad you will need a few items:

<figure class="align-right">
<img src="/_static/images/wifi/wangtongze_jumpered.png"
alt="EX-CommandStation" />
</figure>

1.  a \|EX-CS\| - This consists of:

> - an **Arduino microprocessor**,
> - a **Motor Driver** board / motor shield,
> - Optionally:
>   - a **WiFi shield (Recommended)**[^1] (*This option is described on
>     the following pages*), or
>   - an ethernet shield, or
>   - a Bluetooth board, or
>   - direct connection to a PC[^2], and
> - our free, open source, custom software

<figure class="align-right">
<img src="/_static/images/engine_driver/vertical_slider.png"
alt="Engine Driver" />
</figure>

2.  a **Throttle (Controller)** - Something to control your trains with.
    \|BR\| Such as our \|EX-WT\|, or other apps like \|JMRI\|, \|Engine
    Driver\|, \|WiThrottle\|, etc.
3.  Power - The Arduino and the \|Motor shield\| need to be powered
    separately, so

> - a **12-16v DC power supply**[^3] for the \|motor shield\| to the
>   track, and
> - a **7-9v DC power supply** for the Arduino

4.  a **\"Main\" track,** aka \"Operations\" track - most people already
    have this: it\'s your layout!
5.  a **\"Programming\" track,** aka \"Service\" track - an isolated
    short section of track that you will use to program locomotives
6.  a **Train** - Specifically, a locomotive equipped with a DCC decoder
    (either a standard or sound decoder). Ideally, it should be a loco
    already proven to work on DCC. Otherwise, if you have a problem, you
    may not be able to tell if the problem is the decoder or the
    EX-CommandStation

\|HR-DASHED\|

\|HR-HEAVY\|

## Next Steps - Purchasing Parts

See the `purchasing` page or click the
\'Next\' button to see what you need to acquire to create your
\|EX-CS\|.

------------------------------------------------------------------------

::: 
purchasing assembly wifi-setup ../installer-diy.rst
../controllers-diy.rst ../testing-diy.rst
/support/ex-cs-troubleshooting\_\_included-diy /support/wifi-at-version
:::

[^1]: The Instructions on the following pages assume that that you will
    use a WiFi Shield.

[^2]: Requires [\|JMRI\|](##SUBST##**JMRI**) installed on a computer.

[^3]: The voltage you need for the [\|Motor
    Driver\|](##SUBST##|Motor Driver|) depends on the scale/gauge of the
    layout you are using. Bigger is not always better. Too high a
    voltage can damage your locos. See the
    `reference/hardware/power-supplies:powering the motor driver` for more information.
