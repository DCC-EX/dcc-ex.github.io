orphan

: 

::: {.meta keywords="EX-CommandStation Command Station EX-Installer"}
:::

\|EX-I-LOGO\|

# Using EX-Installer - Detailed Instructions

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|
\|githublink-ex-installer-button-small\|

\|force-break\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="4" local=""}
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

:::: note
::: title
Note
:::

If you already have, or wish to create, your own custom config files, we
recommend that you
`read this page first <managing-config-files>`{.interpreted-text
role="doc"}.
::::

:::: warning
::: title
Warning
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

## Requirements (for installing)

To run \|EX-I\| you need:

- a Microsoft Windows, Apple MacOS or Linux based **computer** - **Note
  this will not run on Raspberry Pi**

- \|EX-CS\| **hardware**, comprising of:

  - an **Arduino microprocessor**, based on any of:
    - Arduino Mega, Arduino Uno or Nano
    - Expressif ESP32
    - STMicroelectronicsm Nucleo/STM32
  - a **motor Driver**
  - optionally, a **WiFi shield** or ethernet shield
  - optionally, an **LCD or oLED display**

  or

  - an \|EX-CSB1\|

- a **USB cable** to connect your computer to the Microcontroller

## Getting Ready

:::: {.warning .warning-float-right}
::: title
Warning
:::

Close all other programs that might be using the USB port. (Like the
\|Arduino IDE\|, \|EX-WT\| or \|JMRI\|.)
::::

To begin with\...

- **Connect** your \|EX-CS\| **hardware** to your computer via USB.
  \|BR\| Make sure your USB Cable is connected from your computer to the
  EX-CommandStation.
- Make sure no other programs (like the \|Arduino IDE\|, \|EX-WT\| or
  \|JMRI\|) are using the same USB port. (i.e. close them.)

------------------------------------------------------------------------

## Download and Run EX-Installer

:::: {.warning .warning-float-right}
::: title
Warning
:::

**Antivirus Software** \|BR\| You *may* need to turn off your antivirus
software before you try to install. \|BR\| Sometimes our software gets
blocked by antivirus apps. If you see any errors on the install screen,
this is usually the issue.
::::

### Download EX-Installer

::: rst-class
dcclink

`Download EX-Installer <download/ex-commandstation:ex-Installer>`{.interpreted-text
role="ref"}
:::

\|HR-DASHED\|

### Run EX-Installer

#### For Microsoft Windows

> - Open the Windows *File Manager*
> - Find the folder in which the **EX-Installer-Win64.exe** or
>   **EX-Installer-Win32.exe** was saved. \|BR\| Generally this will
>   default to downloading to the *downloads* folder but your browser
>   may be configured differently.
> - **Run** `EX-Installer-Win64.exe` (or **EX-Installer-Win32.exe**)
>   \|BR\| \|BR\| Note: depending on the configuration of your computer
>   the \'.exe\' may or may not appear. This is not of concern. \|BR\|
>   \|BR\|

#### For Apple macOS

> - Open a terminal window and navigate to the that folder that you
>   downloaded the file to. e.g.: \|BR\| `cd Downloads`
> - Enter the following command to tell the OS that it is an executable:
>   \|BR\| `chmod +x EX-Installer-macOS`
> - **Run the installer with** the following command: \|BR\|
>   `./EX-Installer-macOS` \|BR\| \|BR\|

:::: {.note .note-float-right}
::: title
Note
:::

A 64bit version of Linux is required to run the EX-Installer. The
Raspberry Pi is 32bit so not supported by the EX-Installer.
::::

#### For Linux

> - Right-click on the file, go to Properties, then the Permissions tab,
>   and check \"Allow executing file as program\"
> - Open a terminal window and navigate to that folder
> - **Run the installer with** the following command: \|BR\|
>   `./EX-Installer-Linux64` \|BR\| \|BR\|

\|HR-DASHED\|

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

**You will be presented with the following screen\...**

\|HR-DASHED\|

### a. The \'EX-Installer Welcome\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/welcome.png"
alt="EX-Installer - Welcome" />
<figcaption>EX-Installer - Welcome screen</figcaption>
</figure>

This screen provides some basic information about the process of loading
the Software.

To proceed, click the `Manage Arduino CLI`{.interpreted-text
role="guilabel"} button.

\|force-break\|

\|HR-DASHED\|

### b. \'Manage Arduino CLI\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/manage_cli.png"
alt="EX-Installer - Manage CLI" />
<figcaption>EX-Installer - Manage CLI screen</figcaption>
</figure>

This screen allows you to install or update the *Arduino Command Line
Interface (CLI)*.

We use the *Arduino Command Line Interface (CLI)* to upload the DCC-EX
products to your Arduino. The CLI eliminates the need to install the
more daunting \|Arduino IDE\|. \|EX-I\| is able to manage the
installation and updating of the Arduino CLI for you at the click of a
button.

If you have not installed the CLI previously you will see a
`Install Arduino CLI`{.interpreted-text role="guilabel"} button.

If have previously installed the CLI you will see a
`Refresh Arduino CLI`{.interpreted-text role="guilabel"} button.

:::: {.hint .hint-float-right-narrow}
::: title
Hint
:::

**Expressif ESP32** is required for the \|EX-CSB1-SHORT\|
::::

If you are using an Espressif or STMicroelectronics device (including
the \|EX-CSB1-SHORT\|, as opposed to the more common Uno or Mega based
Arduinos, you will need to enable support for these by selecting the
appropriate additional platform option.

:::: note
::: title
Note
:::

Enabling additional platforms *that you will not be using* will take
more space on your hard drive and is likely to add several minutes to
the installation process.
::::

You *must* have Arduino CLI installed to proceed, simply click the
`Install Arduino CLI`{.interpreted-text role="guilabel"} button if it is
showing.

If you already have the Arduino CLI installed, it is recommended that
you refresh it periodically (e.g. weekly) to ensure support for the
various device details are kept up to date. To refresh the CLI, simply
click the `Refresh Arduino CLI`{.interpreted-text role="guilabel"}
button.

Installing the CLI can take some time. Maybe grab a cup of tea or a
coffee!

Once the CLI is installed, To proceed, click the
`Select your device`{.interpreted-text role="guilabel"} button.

\|force-break\|

\|HR-DASHED\|

### c. \'Select Your Device\' screen

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

When navigating to this page, a scan for devices will start
automatically.

If you see **No devices found** it means that you either a) have not
connected the device to the computer, or b) the device was not
recognised by the computer.

#### No Devices Found

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

\|EX-I\| will attempt to work out what type of Arduino you have
connected, but in some cases it will not be able to do so. (This is
especially common with cheap clone devices.)

Check and select the appropriate board from the drop down list.

Once you have a port and device type selected, to proceed, click the
`Select product to install`{.interpreted-text role="guilabel"} button.

\|force-break\|

\|HR-DASHED\|

### d. \'Select the Product to Install\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/select_product.png"
alt="EX-Installer - Select Product" />
<figcaption>EX-Installer - Product Screen</figcaption>
</figure>

Currently, \|EX-CS\|, \|EX-IO\|, and \|EX-TT\| can be installed by the
\|EX-I\|, however this page will focus only on \|EX-CS\|. For the other
products, refer to the relevant documentation section.

Click on the \|EX-CS\| logo to proceed.

\|force-break\|

\|HR-DASHED\|

### e. Product Specific screens - EX-CommandStation

#### i) \'Select EX-CommandStation Version\' screen

<figure class="align-right">
<img src="/_static/images/ex-installer/select_cs_version.png"
alt="EX-Installer - Select EX-CommandStation version" />
<figcaption>EX-Installer - EX-CommandStation version screen</figcaption>
</figure>

On this screen you need to select:

- Which version of the **EX-CommandStation** software you wish to load
- How you wish to configure the software

##### Which Version

Select which version of the \|EX-CS\| software to load onto your
hardware. If you are unsure, or unless you have been otherwise directed
by the support team, we recommend you select `Latest Production`.

Options are:

- Latest Production - Recommended!
- Latest Development
- Select a specific version

##### How to Configure

Select how you wish to configure your \|EX-CS\|. Unless you are updating
a previous version that you manually configured, or want to manually
make advanced configuration changes, select
`Configure options on the next screen`

Options are:

- Configure options on the next screen
- Use my existing configuration files

<figure class="align-right">
<img src="/_static/images/ex-installer/ex_cs_select_existing_config.png"
alt="EX-Installer - EX-CommandStation select existing config" />
<figcaption>EX-Installer - Select existing configuration
files</figcaption>
</figure>

If you select `Use my existing configuration files` you will be prompted
to find the folder where the configuration files are located:

- Click the `Browse`{.interpreted-text role="guilabel"} button and
  navigate through your computer\'s folders and files to select the
  location containing your existing configuration files
- Select one of the files in the folder and click the
  `Open`{.interpreted-text role="guilabel"} button to select it
- The chosen folder will be displayed

\|FORCE-BREAK\|

If you have selected `Configure options on the next screen`, to proceed,
click the `Configure EX-CommandStation`{.interpreted-text
role="guilabel"} button.

If you have selected `Use my existing configuration files`, to proceed,
click the `Advanced Config`{.interpreted-text role="guilabel"} button.
In this case you will be presented with the \'Advanced Config\' screen.

\|force-break\|

\|HR-DASHED\|

#### ii) \'Install EX-CommandStation\' - Configuration screen

<figure class="align-left">
<img src="/_static/images/ex-installer/ex_cs_configure-general.png"
alt="EX-Installer - EX-CommandStation Configuration" />
<figcaption>EX-Installer - EX-CommandStation Configuration
screen</figcaption>
</figure>

Only if you have selected `Configure options on the next screen` on the
previous screen will you be presented with this screen.

On this screen you can select some of the flexible and optional features
of the \|EX-CS\|:

- Motor Driver type
- LCD or oLED display
- Wifi
- Ethernet
- Set track modes
- Advanced Config

\|force-break\|

\|HR-DASHED\|

##### Motor Driver

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
the \|EX-CS\| may not work.

These options are determined from the chosen version of \|EX-CS\|, and
may include:

- EX-CSB1
- EX-CSB1_WITH_EX8874
- STANDARD_MOTOR_SHIELD
- EX8874_SHIELD
- POLOLU_MOTOR_SHIELD
- FIREBOX_MK1
- FIREBOX_MK1S
- FUNDUMOTO_SHIELD
- IBT_2_WITH_ARDUINO
- YFROBOT_MOTOR_SHIELD
- ORION_UNO_INTEGRATED_SHIELD
- NANOEVERY_EXAMPLE

This list will change over time as new motor drivers are added, and any
older ones no longer supported are removed.

:::: note
::: title
Note
:::

If you have added a an \|EX-MS\| to the \|EX-CSB1\|\...

\|EX-I\| does not have a simple way to configure the additional outputs
so you will need to use the
`TrackManager </trackmanager/index>`{.interpreted-text role="doc"}
feature to configure the outputs as needed in
[myAutomation.h]{.title-ref} in the [Advanced Configuration]{.title-ref}
page of \|EX-I\|.

For example, to always set outputs C and D to be the second and third
DCC MAIN outputs, you would create a AUTOSTART sequence that sets both
outputs C and D to DCC MAIN mode in [myAutomation.h]{.title-ref}.

``` 
AUTOSTART 
   SET_TRACK(A,MAIN)
   SET_TRACK(B,PROG)
   SET_TRACK(C,MAIN)
   SET_TRACK(D,MAIN)
   POWEROFF
DONE
```
::::

\|HR-DASHED\|

##### Optional Display

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

The options include:

- LCD - 16 columns x 2 rows
- LCD - 20 columns x 4 rows
- OLED 128 x 32
- OLED 128 x 64

##### WiFi

If you have installed and optional WiFi board, or are using a
microcontroller board with integrated WiFi, enable the `I have WiFi`
option, which will enable the WiFi Options tab, allowing you to
configure the WiFi settings.

<figure class="align-center">
<img src="/_static/images/ex-installer/ex_cs_enable_wifi.png"
alt="EX-Installer - EX-CommandStation - Enable WiFi" />
<figcaption aria-hidden="true">EX-Installer - EX-CommandStation - Enable
WiFi</figcaption>
</figure>

You can configure the WiFi for **EX-CommandStation** two ways:

- **Access Point mode** \|BR\| You can configure for EX-CommandStation
  to have its own, completely isolated, WiFi Network. This is referred
  to as *Access Point Mode*. (Most useful if your layout is away from
  the house, or you transport your layout frequently, or do not want to
  give guests access to your home WiFi.) \|BR\| To enable, select
  `Use my EX-CommandStation as an Access Point` \|BR\| \|BR\|
- **Station mode** \|BR\| The EX-CommandStation can be setup so that it
  connects to your existing home WiFi Network. This is referred to as
  *Station Mode*. \|BR\| To enable, select
  `Connect my EX-CommandStation to my existing wireless network`

:::: note
::: title
Note
:::

\|SUITABLE\| \|tinkerer\| \|engineer\| \|BR\| For the \|EX-CSB1-SHORT\|
and DIY ESP32 based Command Stations, the Experimental / Development
(DEVEL) versions of the software from 5.7.0 ignore the WiFi
configuration in the config.h file. see [WiFi configuration (CSB1 or
ESP32
ONLY)](https://dcc-ex.com/mkdocs-test/products/ex-commandstation/config-wifi-esp32/)
for more information.
::::

##### Use my EX-CommandStation as an Access Point

> <figure class="align-center">
> <img
> src="/_static/images/ex-installer/ex_cs_configure_wifi_access_point.png"
> alt="EX-Installer - EX-CommandStation - Configure WiFi - Access Point" />
> <figcaption>EX-Installer - Configure WiFi - Access Point</figcaption>
> </figure>
>
> :::: {.note .note-float-right}
> ::: title
> Note
> :::
>
> If possible, choose a channel that is unused (or least used) by other
> WiFi networks around your location. \|BR\| There are numerious phone
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
> **WiFi Password** is optional. \|BR\| If this field is left blank the
> password will default to \'PASS_xxxxxx\' where \'xxxxxx\' will be the
> same as the SSID *name* that will be automatically configured.
>
> **WiFi Channel** can be any value from 1-11.

##### Connect my EX-CommandStation to my existing wireless network

> <figure class="align-center">
> <img src="/_static/images/ex-installer/ex_cs_configure_wifi_station.png"
> alt="EX-Installer - EX-CommandStation - Configure WiFi - Station Mode" />
> <figcaption>EX-Installer - Configure Wifi - Station Mode</figcaption>
> </figure>
>
> If `Connect my EX-CommandStation to my existing wireless network` is
> selected, two additional options are presented:
>
> - WiFi SSID
> - WiFi Password
>
> Both are required.
>
> *WiFi SSID* is the name of your home network.
>
> *WiFi Password* is the password for your home network.
>
> Additionally, if you choose, you may customise the WiFi hostname, or
> leave it as the default \"dccex\".
>
> :::: note
> ::: title
> Note
> :::
>
> See the
> `/ex-commandstation/advanced-setup/supported-wifi/wifi-config`{.interpreted-text
> role="doc"} page for more detailed information on the the WiFi
> options.
> ::::

\|HR-DASHED\|

##### I have Ethernet

If you have installed and Ethernet board, select this option.

Note that it is not possible to have both WiFi and Ethernet enabled at
the same time.

\|HR-DASHED\|

##### Start with power on

:::: {.hint .tip-float-right-narrow}
::: title
Hint
:::

The \|EX-CSB1-SHORT\| will generally be supplied with this enabled
::::

Enabling this option will cause the \|EX-CS\| to automatically start
with the track power on.

If you don\'t enable this, you will need to turn the track power with
you controller, or with TrackManger automations.

\|HR-DASHED\|

##### Override current limit

Enabling this option will allow you to override the default current
limit.

##### Set track modes

If you have selected an appropriate version of \|EX-CS\|, you will be
able to enable the option to configure TrackManager. If the
`Configure TrackManager` switch is disabled, you have not selected a
version that includes the TrackManager feature.

Enabling this option will enable the TrackManager Config tab.

<figure class="align-center">
<img
src="/_static/images/ex-installer/ex_cs_configure_enable_trackmanager.png"
alt="EX-Installer - EX-CommandStation - Enable TrackManager" />
<figcaption>EX-Installer - Enable TrackManager</figcaption>
</figure>

<figure class="align-left">
<img
src="/_static/images/ex-installer/ex_cs_configure_set_track_mode_options.png"
alt="EX-Installer - EX-CommandStation - Configure TrackManager" />
<figcaption>EX-Installer - Select Track Modes</figcaption>
</figure>

<figure class="align-center">
<img
src="/_static/images/ex-installer/ex_cs_configure_set_track_mode.png"
alt="EX-Installer - EX-CommandStation - Configure TrackManager" />
<figcaption>EX-Installer - Configure Track Modes</figcaption>
</figure>

\|force-break\|

The tracks (channels) on your motor driver can be configured in a
variety of different ways.

- `MAIN` - DCC main
- `MAIN_INV` - DCC main inverted
- `PROG` - DCC Programming Track
- `DC`
- `DC_INV` - DC with the positive/negative inverted
- `DCX` - DC with the positive/negative inverted (same as DC_INV)
- `MAIN_AUTO` - DCC Auto-reverser mode
- `EXT`
- `NONE`

If the Command Station is configured as a booster (ESP32
microcontrollers only), then the channels can asl be configured as:

- `BOOST` - \|Booster Mode\|
- `BOOST_INV` - \|Booster Mode\| inverted
- `BOOST_AUTO` - \|Booster Mode\| + Auto-reverser mode

By default track (channel) **A** will default to `MAIN` and Track
(channel) **B** to `PROG`.

When selecting `DC` or `DCX` / `DC_INV` modes, you can customer the
associated loco/cab ID.

##### Advanced Config

<figure class="align-center">
<img
src="/_static/images/ex-installer/ex_cs_configure_advanced_config.png"
alt="EX-Installer - EX-CommandStation - Advanced Config" />
<figcaption>EX-Installer - Advance Config</figcaption>
</figure>

If you wish to edit the \'config\' files directly, select this option.
An additional screen will be presented for to edit the main config
files.

Note there is an additional option `Create myAutomation.h` that allows a
blank myAutomation.h file to be created, which you can edit on the
following *Advanced Config* screen. Leaving this option disabled means a
myAutomation.h file will not be generated if it is not required, which
saves memory on your \|EX-CS\| device.

Unless you have selected *Advanced Config*, to proceed, click the
`Compile and Load`{.interpreted-text role="guilabel"} button. See *iv*
below.

If you have selected *Advanced Config*, to proceed, click the
`Advanced Config`{.interpreted-text role="guilabel"} button. See *iii*
below.

\|force-break\|

#### iii) \'Advanced Configuration\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/ex_cs_advanced_config.png"
alt="EX-Installer - EX-CommandStation - Configure WiFi - Station Mode" />
<figcaption>EX-Installer - Advanced Config Screen</figcaption>
</figure>

<figure class="align-center">
<img
src="/_static/images/ex-installer/ex_cs_advanced_config_multifiles.png"
alt="EX-Installer - EX-CommandStation - Advanced Config with multiple files" />
<figcaption>EX-Installer - Advance Config - more than two
files</figcaption>
</figure>

\|force-break\|

If you have selected `Advanced Config` on the previous screen, or if you
chose to copy your existing configuration files, you will be presented
with this screen.

On this screen you can edit the configuration files. If you have more
than two files to edit, they will be separated into tabs as shown in the
second figure above.

Note that if you did not enable any options requiring myAutomation.h,
and did not enable `Create myAutomation.h`, you will only be able to
edit config.h on this screen.

To proceed, click the `Compile and Load`{.interpreted-text
role="guilabel"} button. See *iv* below.

\|force-break\|

#### iv) \'Compile and Load\' screen

<figure class="align-left">
<img src="/_static/images/ex-installer/ex_cs_load.png"
alt="EX-Installer - Load" />
<figcaption>EX-Installer - Compile and Load Screen</figcaption>
</figure>

To proceed, click the `Load`{.interpreted-text role="guilabel"} button.

Results are shown in the lower half of the screen.

If there are **no errors**, you can proceed to
`testing your setup </ex-installer/testing>`{.interpreted-text
role="doc"}.

If there **are errors** or you are having difficulties check the
`/support/ex-cs-troubleshooting`{.interpreted-text role="doc"} page for
assistance.

\|force-break\|

\|HR-DASHED\|

##### Backup

After loading the software onto your device, you can optionally copy the
generated configuration files to a folder of your choice as a backup by
clicking the `Backup config files`{.interpreted-text role="guilabel"}
button.

<figure class="align-center">
<img src="/_static/images/ex-installer/ex_cs_backup.png"
alt="EX-Installer - Backup" />
<figcaption>EX-Installer - Backup Option</figcaption>
</figure>

You will be prompted to select a folder, and if the chosen folder
already contains config files, you can overwrite these, or you can
select an alternative location.

<figure class="align-left">
<img src="/_static/images/ex-installer/ex_cs_backup_select.png"
alt="EX-Installer - Backup select folder" />
<figcaption>EX-Installer - Select backup folder</figcaption>
</figure>

<figure class="align-center">
<img src="/_static/images/ex-installer/ex_cs_backup_overwrite.png"
alt="EX-Installer - Overwrite existing files" />
<figcaption>EX-Installer - Overwrite existing backup</figcaption>
</figure>

\|force-break\|

------------------------------------------------------------------------

### Device Monitor

Once you have selected a device in \|EX-I\| on the \"Select your
device\" screen, or after successfully loading software onto your
device, a `View device monitor` button will be available.

When clicking this button, the \|Device Monitor\| window will open,
allowing you to interact with your device by sending commands and
viewing the serial console output.

![Device Monitor](/_static/images/ex-installer/device-monitor.png){.align-center}

| 

For further details on using \|Device Monitor\|, continue on to the next
page with the \'Next\' button, or go straight to
`ex-installer/testing:using the ex-installer device monitor`{.interpreted-text
role="ref"}.

\|force-break\|

\|HR-HEAVY\|

## Next Steps - Test your setup

:::: {.important .important-float-right}
::: title
Important
:::

The programming track is for programming only. Make sure you are on the
main track if you expect your loco to move or respond to light or sound
commands.
::::

See the `/ex-installer/testing`{.interpreted-text role="doc"} page or
click the \'Next\' button to learn how to test and use your \|EX-CS\|.

\|force-break\|
