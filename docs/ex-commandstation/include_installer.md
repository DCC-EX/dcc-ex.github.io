::: {.meta keywords="EX-Installer"}
:::

\|EX-CS-LOGO\|

# Install the Software

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="3" local=""}
On this page
:::
::::

::: rst-class
dcclink

`Download EX-Installer <download/ex-commandstation:ex-Installer>`{.interpreted-text
role="ref"}
:::

Once you have assembled your do-it-yourself \|EX-CS\| hardware you need
to load our software onto it to make it usable. \|BR\| To make it as
simple as possible we have created the \|EX-I\| app.

If you have purchased a \|EX-CSB1\| it will have come with the \|EX-CS\|
software already installed. You only need to look at this page if you
want to change the default configuration.

:!!! note "::: title
Note"
:::

This page is specifically intended for a \|conductor-text\| or
\|tinkerer-text\| who has either:

- Purchased a ready-to-run (RTR) \|EX-CSB1-SHORT\|, or
- Assembled *just* the recommended do-it-yourself (DIY) hardware
  (including WiFi).

This page is as simplified version of the
`/ex-installer/installing`{.interpreted-text role="doc"} page. If you
are a \|tinkerer-text\| or \|engineer-text\| or have installed some of
the additional, or different, hardware from that recommended for a
\|conductor-text\| then we suggest that you look at the
`Detailed Instructions </ex-installer/installing>`{.interpreted-text
role="doc"} page for the full instructions.
::::

:!!! warning "::: title
Warning"
:::

We have found that there are a small number of users who can have an
issue when trying to update firmware or upload EXRAIL scripts to an
EX-CSB1 Command Station (or any ESP32 based device).

If you are having problems, look at our [uploading troubleshooting
guide](https://dcc-ex.com/news/posts/20250128.html).
::::

:::: important
::: title
Important
:::

A word of caution on the *alternate approach* of using the \|Arduino
IDE\| to install the software:

While it is possible install the software using the \|Arduino IDE\|, we
*seriously* **DO NOT RECOMMEND IT** for a \|conductor-text\| or
\|tinkerer-text\|. It is an order of magnitude more complex, much
slower, and with a very high probability of getting something wrong
unless you really know what you are doing.

The \|EX-I\| described below will meet 100% of the needs of a
\|conductor-text\| or \|tinkerer-text\| with considerably less effort.
::::

\|force-break\|

------------------------------------------------------------------------

**Instructions for Windows, Mac OS X, and Linux**

------------------------------------------------------------------------

## Requirements (for installing)

::: sidebar
****USB Cable****

Make sure your USB Cable is connected from your computer to the
\|EX-CS\|. Make sure no other programs (like the \|Arduino IDE\|) are
using the same USB port.
:::

To run \|EX-I\| you need:

- A Windows, Linux or MacOS X **Computer**
- An \|EX-CS\| (\|EX-CSB1\| or Arduino Mega/Uno + \|Motor shield\| +
  optional WiFi shield)
- A **USB cable** to connect your computer to the Microcontroller

------------------------------------------------------------------------

## 1. Getting Ready

To begin with\...

- **Connect** your \|EX-CS\| **hardware** to your computer via USB.
  \|BR\| Make sure your USB Cable is connected from your computer to the
  EX-CommandStation.
- Make sure no other programs (like the \|Arduino IDE\| or \|EX-WT\|)
  are using the same USB port. (i.e. close them.)

------------------------------------------------------------------------

## 2. Download and Run EX-Installer

:::: {.warning .warning-float-right}
::: title
Warning
:::

**Antivirus Software** \|BR\| You *may* need to turn off your antivirus
software before you try to install. \|BR\| Sometimes our software gets
blocked by antivirus apps. If you see any errors on the install screen,
this is usually the issue.
::::

- Download the
  `EX-Installer <download/ex-commandstation:ex-Installer>`{.interpreted-text
  role="ref"} app. \|BR\| \|BR\|
- For **Microsoft Windows**:
  - Open the Windows *File Manager*
  - Find the folder in which the **EX-Installer-Win64.exe** or
    **EX-Installer-Win32.exe** was saved. \|BR\| Generally this will
    default to downloading to the *downloads* folder but your browser
    may be configured differently.
  - **Run** `EX-Installer-Win64.exe` or **EX-Installer-Win32.exe** or
    **EX-Installer-Win32.exe** \|BR\| \|BR\| Note: depending on the
    configuration of your computer the \'.exe\' may or may not appear.
    This is not of concern. \|BR\| \|BR\|

:::: {.important .important-float-right}
::: title
Important
:::

EX-Installer creates a folder (\<home\>\\ex-installer) to hold the
information it needs.
`Do not directly modify anything in this folder`{.interpreted-text
role="dcc-ex-red-bold"} as it a) will be overwritten or deleted by the
installer at any time, and b) will cause the installer to fail to load.
::::

- For **Apple macOS**:
  - Open a terminal window and navigate to the that folder that you
    downloaded the file to. e.g.: \|BR\| `cd Downloads`
  - Enter the following command to tell the OS that it is an executable:
    \|BR\| `chmod +x EX-Installer-macOS`
  - **Run the installer with** the following command: \|BR\|
    `./EX-Installer-macOS` \|BR\| \|BR\|
- For **Linux**:
  - Right-click on the file, go to Properties, then the Permissions tab,
    and check \"Allow executing file as program\"
  - Open a terminal window and navigate to that folder
  - **Run the installer with** the following command:
    `./EX-Installer-Linux64` \|BR\| \|BR\|

------------------------------------------------------------------------

**You will be presented with the following screen\...**

## 3. Installer Screens

### The \'EX-Installer Welcome\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/welcome.png"
alt="EX-Installer - Welcome" />
</figure>

This screen provides some basic information about the process of loading
the Software.

To proceed, click the `Manage Arduino CLI`{.interpreted-text
role="guilabel"} button.

\|force-break\|

\|HR-DASHED\|

### \'Manage Arduino CLI\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/manage_cli.png"
alt="EX-Installer - Manage CLI" />
<figcaption>EX-Installer - Welcome screen</figcaption>
</figure>

This screen allows you to install or update the *Arduino Command Line
Interface (CLI)*.

We use the *Arduino Command Line Interface (CLI)* to upload the DCC-EX
products to your Arduino.

If you have not installed the CLI previously you *must* have Arduino CLI
installed to proceed, simply click the
`Install Arduino CLI`{.interpreted-text role="guilabel"} button if it is
showing.

If you already have the Arduino CLI installed, it is recommended that
you refresh it periodically (e.g. weekly) to ensure support for the
various device details are kept up to date. To refresh the CLI, simply
click the `Refresh Arduino CLI`{.interpreted-text role="guilabel"}
button.

:::: {.hint .hint-float-right-narrow}
::: title
Hint
:::

**Expressif ESP32** is required for the \|EX-CSB1-SHORT\|
::::

If you are using the \|EX-CSB1-SHORT\| or the recommended DIY Mega
hardware, you should not need to adjust the other settings on this page.

The \|EX-CSB1-SHORT\| requires the `Expressif ESP32` option to be
enabled. It should be enabled by default.

Installing the CLI can take some time. Once the CLI is installed, To
proceed, click the `Select your device`{.interpreted-text
role="guilabel"} button.

\|force-break\|

\|HR-DASHED\|

### \'Select Your Device\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/select_device.png"
alt="EX-Installer - Select Device" />
<figcaption>EX-Installer - Device screen</figcaption>
</figure>

On this screen you will need to \|BR\| a) select the type of device you
wish to load the \|EX-CS\| software onto, and \|BR\| b) the USB port you
have connected the device to on your computer.

\|EX-I\| will attempt to work out both of these for you, but it may need
assistance.

Click on the `Scan for Devices`{.interpreted-text role="guilabel"}
button.

#### No Devices Found

After you have clicked on the `Scan for Devices`{.interpreted-text
role="guilabel"} button, if you see **No devices found** to means that
you either a) have not connected the device to the computer, or b) the
device was not recognised by the computer.

If you have not connected the device, connect it now then click the
`Scan for Devices`{.interpreted-text role="guilabel"} button again.

If the device *is* connected but not found refer to the
`/support/ex-cs-diagnose`{.interpreted-text role="doc"} page for
assistance.

#### Multiple Devices Found

<figure class="align-center">
<img
src="/_static/images/ex-installer/select_device_multiple_devices.png"
alt="EX-Installer - Select Device - Multiple Devices" />
<figcaption>EX-Installer - Device - Multiple Devices</figcaption>
</figure>

If more than one device is found (on different USB ports), you will need
to select which one you wish to load the software on to.

<figure class="align-center">
<img src="/_static/images/ex-installer/select_device_selection.png"
alt="EX-Installer - Select Device - Selection" />
<figcaption>EX-Installer - Device - Selection</figcaption>
</figure>

:::: {.hint .hint-float-right-narrow}
::: title
Hint
:::

For the \|EX-CSB1-SHORT\| select \'\*\*DCC-EX EX-CSB1\*\*\'
::::

\|EX-I\| will attempt to work out what type of microprocessor you have
connected, but some cases it will not be able to do so. (This is
especially common with cheap clone devices.)

Check and select the appropriate board from the drop down list.

Once you have a port and device type selected, to proceed, click the
`Select product to install`{.interpreted-text role="guilabel"} button.

\|force-break\|

\|HR-DASHED\|

### \'Select the Product to Install\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/select_product.png"
alt="EX-Installer - Select Product" />
<figcaption>EX-Installer - Product Screen</figcaption>
</figure>

Currently only the \|EX-CS\| product can be installed by the \|EX-I\|.

Click on the \|EX-CS\| logo to proceed.

\|force-break\|

\|HR-DASHED\|

### \'Select EX-CommandStation Version\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/select_cs_version.png"
alt="EX-Installer - Select EX-CommandStation version" />
<figcaption>EX-Installer - Select EX-CommandStation version
screen</figcaption>
</figure>

On this screen you need to select:

- Which version of the EX-CommandStation software you wish to load
- How you wish to configure the software

#### Which version

Select which version of the \|EX-CS\| software to load onto your
hardware. If you are unsure, or unless you have been otherwise directed
by the support team, we recommend you select `Latest Production`.

#### How to configure

Select how you wish to configure your \|EX-CS\|. Unless you are updating
a previous version that you manually configured, or want to manually
make advanced configuration changes, select
`Configure options on the next screen`

If you do want to manually make advanced configuration changes, see the
`/ex-installer/installing`{.interpreted-text role="doc"} page for
instructions on how to enable them.

If you have selected `Configure options on the next screen`, to proceed,
click the `Configure EX-CommandStation`{.interpreted-text
role="guilabel"} button.

\|force-break\|

\|HR-DASHED\|

### \'Install EX-CommandStation\' - Configuration screen

<figure class="align-left">
<img src="/_static/images/ex-installer/ex_cs_configure-general.png"
alt="EX-Installer - EX-CommandStation Configuration" />
<figcaption>EX-Installer - EX-CommandStation Configuration
screen</figcaption>
</figure>

On this screen you can select some of the flexible and optional features
of the \|EX-CS\|:

- Motor Driver type
- LCD or oLED display
- WiFi
- Ethernet
- Set track modes
- Advanced Config

Only the *Motor Driver* and *WiFi* will be covered on this page. If you
have installed different hardware to that recommended, see the
`/ex-installer/installing`{.interpreted-text role="doc"} page for
instructions on all the available configuration options.

\|force-break\|

#### Motor Driver

:::: {.hint .hint-float-right-narrow}
::: title
Hint
:::

For the \|EX-CSB1-SHORT\| alone select \'\*\*EX-CSB1\*\*\' \|BR\| If you
have the additional \|EX-MS\| select \'\*\*EXCSB1_WITH_EX8874\*\*\'
::::

<figure class="align-center">
<img src="/_static/images/ex-installer/ex_cs_configure_motor_shield.png"
alt="EX-Installer - EX-CommandStation - Configure Motor Driver" />
<figcaption>EX-Installer - Configure Motor Driver</figcaption>
</figure>

You *must* select the motor driver type that you have installed. The
installer can\'t detect this, so you must select the correct board or
the \|EX-CS\| may not work. If you have installed the recommended Motor
Driver, select [STANDARD_MOTOR_SHIELD]{.title-ref} if you purchased a
\|standard Motor Driver\|, or [EX8874_SHIELD]{.title-ref} if you
purchased our **EX-MotorShield8874**.

::: sidebar
**Station Mode VS Access Point Mode**

\|conductor\| \|BR\| There is no right or wrong selection here. Both
options here may be valid for you to use, depending on how you wish to
use your \|EX-CS\|.

If a) your layout is close to your home WiFi network, b) you don\'t
transport the layout around, c) you need to use more than four WiFi
controllers at a time, and/or d) you are not likely to, or have no
concerns about letting visitors access your home WiFi (for them to use
their own devices on your layout), then **Station Mode** is probably a
better option.

If the above is not generally true, then **Access Point Mode** may be a
better choice.

You must choose one of these options now, but you can always come back
later and re-load the software with a different option.
:::

\|HR-DASHED\|

#### WiFi

If you have installed and optional WiFi board, or are using a
microcontroller board with integrated WiFi, enable the `I have WiFi`
option, which will present you with additional options.

You can configure the WiFi for EX-CommandStation two ways:

- **Access Point mode** \|BR\| You can configure for EX-CommandStation
  to have its own, completely isolated, WiFi Network. This is referred
  to as *Access Point Mode*. (Most useful if your layout is away from
  the house, or you transport your layout frequently.) \|BR\| To enable,
  select `Use my EX-CommandStation as an Access Point` \|BR\| \|BR\|
- **Station mode** \|BR\| The EX-CommandStation can be setup so that it
  connects to your existing home WiFi Network. This is referred to as
  *Station Mode*. \|BR\| To enable, select
  `Connect my EX-CommandStation to my existing wireless network`

:!!! note "::: title
Note"
:::

\|SUITABLE\| \|tinkerer\| \|engineer\| \|BR\| For the \|EX-CSB1-SHORT\|
and DIY ESP32 based Command Stations, the Experimental / Development
(DEVEL) versions of the software from 5.7.0 ignore the WiFi
configuration in the config.h file. see [WiFi configuration (CSB1 or
ESP32
ONLY)](https://dcc-ex.com/mkdocs-test/products/ex-commandstation/config-wifi-esp32/)
for more information.
::::

#### Use my EX-CommandStation as an Access Point

> <figure class="align-center">
> <img
> src="/_static/images/ex-installer/ex_cs_configure_wifi_access_point.png"
> alt="EX-Installer - EX-CommandStation - Configure WiFi Access Point" />
> <figcaption>EX-Installer - Configure WiFi - Access Point</figcaption>
> </figure>
>
> :::: {.note .note-float-right}
> ::: title
> Note
> :::
>
> If possible, choose a channel that is unused (or least used) by other
> WiFi networks around your location. \|BR\| There are numerous phone
> apps that can help you determine which channels are being used by
> other networks. For Android, *\'Wifi Analyzer\'* is one that works.
> For iOS *\'Netspot\'* is suitable
> `(you don't need to purchase WiPry device they mention)`{.interpreted-text
> role="dcc-ex-text-size-60pct"}.
> ::::
>
> If `Use my EX-CommandStation as an Access Point` is selected, two
> additional options are presented:
>
> - WiFi Password
> - WiFi Channel
>
> **WiFi Password** is optional. \|BR\| **We recommend you leave this
> field blank.** \|BR\| If this field is left blank the password will
> default to \"PASS_xxxxx\" where \'xxxxx\' will be the same as the SSID
> *name* that will be automatically configured.
>
> **WiFi Channel** can be any value from 1-11.

#### Connect my EX-CommandStation to my existing wireless network

> <figure class="align-center">
> <img src="/_static/images/ex-installer/ex_cs_configure_wifi_station.png"
> alt="EX-Installer - EX-CommandStation - Configure Wifi - Station Mode" />
> <figcaption>EX-Installer - Configure Wifi - Station Mode</figcaption>
> </figure>
>
> If `Connect my EX-CommandStation to my existing wireless network` is
> selected, two additional options are presented:
>
> - Wifi SSID
> - WiFi Password
>
> Both are required, Though it is possible, but unlikely, that the WiFi
> Password for your network is blank. If so, leave the field blank.
>
> *WiFi SSID* is the name of your home network.
>
> *WiFi Password* is the password for your home network.

To proceed, click the `Compile and Load`{.interpreted-text
role="guilabel"} button.

:!!! note "::: title
Note"
:::

See the
`/ex-commandstation/advanced-setup/supported-wifi/wifi-config`{.interpreted-text
role="doc"} page if you wish to find more detailed information on the
the WiFi options.
::::

\|force-break\|

\|HR-DASHED\|

#### Display Type

:::: {.hint .tip-float-right-narrow}
::: title
Hint
:::

The \|EX-CSB1-SHORT\| will generally be supplied with a **OLED 128 X
64**
::::

![EX-Installer - Configure Display
Driver](/_static/images/ex-installer/ex_cs_configure_screen.png){alt="EX-Installer - EX-CommandStation - Configure Display Driver"}

If you have installed and optional oLED or LED display, enable the
`I have a display` option, which will present you with a drop down list
to select the type of display you have.

\|HR-DASHED\|

#### Start with Power on

:::: {.hint .tip-float-right-narrow}
::: title
Hint
:::

The \|EX-CSB1-SHORT\| will generally be supplied with this enabled
::::

Enabling this option will cause the \|EX-CS\| to automatically start
with the track power on.

If you don\'t enable this, you will need to turn the track power with
you controller, or with \|EX-R\| automations.

\|force-break\|

\|HR-DASHED\|

### \'Compile and Load\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/ex_cs_load.png"
alt="EX-Installer - Load" />
<figcaption>EX-Installer - Compile and Load Screen</figcaption>
</figure>

To proceed, click the `Load`{.interpreted-text role="guilabel"} button.

Results are shown in the lower half of the screen.

If there are **no errors**, you can proceed to
`testing your setup </ex-commandstation/controllers-diy>`{.interpreted-text
role="doc"}.

If there **are errors** or you are having difficulties check the
`/support/ex-cs-troubleshooting`{.interpreted-text role="doc"} page for
assistance.

\|force-break\|

\|HR-HEAVY\|

## Next Steps - Selecting a Throttle (Controller)

:::: {.important .important-float-right}
::: title
Important
:::

The programming track is for programming only. Make sure you are on the
main track if you expect your loco to move or respond to light or sound
commands.
::::

See the `/ex-commandstation/controllers-diy`{.interpreted-text
role="doc"} page or click the \'Next\' button to learn how to select a
throttle (controller) suitable to test and use your \|EX-CS\|.

\|force-break\|
