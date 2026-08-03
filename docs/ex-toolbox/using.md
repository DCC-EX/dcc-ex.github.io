\|EX-TB-LOGO\|

# EX-Toolbox - Installing and Using

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="2" local=""}
On this page
:::
::::

## Installing

\|EX-TB\| can be installed on your Android phone or tablet via the
[Google Play
Store](https://play.google.com/store/apps/details?id=dcc_ex.ex_toolbox)
.

Open the *Play Store* app on your phone or tablet and search for
\"EX-Toolbox\".

Once installed, open \|EX-TB\| and it will go through the initial setup
wizard where it will ask for one permission, and for which which theme
you would like to use.

After you complete the setup wizard, you will be shown the
\'Connection\' Screen.

\|force-break\|

------------------------------------------------------------------------

## Connecting

<figure class="align-right">
<img src="/_static/images/ex-toolbox/connect.png" alt="Connecting" />
<figcaption>EX-Toolbox Connecting</figcaption>
</figure>

Other than the very first time you start \|EX-TB\|, when the app opens
you will be shown the \'Connection\' screen.

On the \'Connection\' screen there are three ways you can select a
\|EX-CS\| to connect to:

> - IP Address and Port
> - Discovered Servers (including via a USB connection)
> - Recent servers

### Discovered Servers

*Wifi*

This is the most common way to connect. If the server you want to
connect to is in the list, simply click on it and you will be taken to
the \'CV-Programming\' screen.

If the server does not appear in the recent list try one of the other
two methods. Your server not appearing in the recent list is not
necessarily a problem and there can be a number of reasons why.

:::: important
::: title
Important
:::

\|EX-TB\| can only connect *directly* to an \|EX-CS\| or JMRI\'s
`'DCC++ over TCP Server'<ex-toolbox/using:connecting via jmri>`{.interpreted-text
role="ref"}, however \|JMRI\|, the \|EX-CS\| and other devices and apps
can, or do, advertise as \"WiThrottle\" mDNS services. EX-Toolbox cannot
determine which are actually direct connections to an \|EX-CS\| or
JMRI\'s
`'DCC++ over TCP Server'<ex-toolbox/using:connecting via jmri>`{.interpreted-text
role="ref"}.

So\... just because a server is in this list, doesn\'t mean that
\|EX-TB\| will be able to connect to it.
::::

*Direct USB*

As of Version 0.1.35 of \|EX-TB\|, the discovered server list will also
include an entry \'DCC-EX-USB-OTG\' if you have a \|EX-CS\| connected
directly to your phone or tablet using a USB on-the-go (OTG) cable.

:::: note
::: title
Note
:::

The direct USB connection is only supported on Android devices that
support USB on-the-go (OTG).

In general USB-C to the USB-C cables are automatically OTG, but if you
are using a USB-C to USB-A cable, you will need to check that the cable
supports OTG. If it doesn\'t, the \'DCC-EX-USB-OTG\' entry won\'t appear
in the discovered server list.
::::

\|HR-DASHED\|

<figure class="align-right">
<img src="/_static/images/ex-toolbox/usb_utg_prompt.png"
alt="USB OTG" />
<figcaption>EX-Toolbox USB OTG Prompt</figcaption>
</figure>

:::: note
::: title
Note
:::

Anytime you connect any USB device to your phone or tablet, you will
likely get a pop up asking if you want to allow \|EX-TB\| to access the
USB. IF you connect devices other that an \|EX-CS\| to your phone or
tablet, just cancel the pop up, but if you only connect an \|EX-CS\| you
can check the box to always open \|EX-TB\|.
::::

\|HR-DASHED\|

### Recent Server List

If the server you want to connect to is in the list, simply click on it
and you will be taken to the \'CV-Programming\' screen.

A server being in this list *does not* necessarily mean that you will be
able to connect it *now*. It just means that you have successfully
connected to it in the past.

\|HR-DASHED\|

### IP Address and Port

Type in the **IP address** and **Port** of the \|EX-CS\| and press
`Connect`{.interpreted-text role="guilabel"}.

To find your EX-CommandStation\'s IP address and Port refer you original
setup or, if you have a OLED screen on your command station the details
will be displayed on it.

If you only ever connect to one \|EX-CS\| you can effectively bypass
this screen by setting the \'Auto-Connect to WiThrottle Server?\'
preference.

------------------------------------------------------------------------

## CV Programming

<figure class="align-right">
<img src="/_static/images/ex-toolbox/cv_programmer_menu.png"
alt="Connecting" />
<figcaption>EX-Toolbox Connecting</figcaption>
</figure>

DCC Decoder CV programming is available:

- on the Programming track (PROG) - Service Mode
- on the main line (MAIN) - Operation mode / Ops Mode

By default \|EX-TB\| shows the Service Mode options. To switch to
Operation Mode, select \"Program on Main (Operation Mode)\" on the drop
down list at the top of the screen.

### CV Programming (Service Mode)

<figure class="align-right">
<img src="/_static/images/ex-toolbox/cv_programmer.png"
alt="Connecting" />
<figcaption>EX-Toolbox Connecting</figcaption>
</figure>

Service Mode CV Programming is available form the \'CV Programming\'
screen, when \'Programming Track (ServiceMode)\' is selected in the drop
down list at the top of the screen.

Service Mode CV Programming allows you to both *Read* (if the
decoder/loco supports it) and *Write* CVs.

You do not need to know the DCC Address of the decoder being changed, as
all decoders/locos currently on the programming track will have the CV
changed at the same time.

On this screen you can:

- read the decoder\'s DCC Address
- write a new DCC Address to the decoder
- read a CV value from the decoder
- write a CV value to the decoder
- select from a list of named, common CVs
- issue \<\> commands to the \|EX-CS\|

To read the DCC Address of the decoder click the
`Read`{.interpreted-text role="guilabel"} button on the DCC Address row.

To write a DCC Address to the decoder, enter the address and click the
`Write`{.interpreted-text role="guilabel"} button on the DCC Address
row.

To read a CV of the decoder, enter the CV number and click the
`Read`{.interpreted-text role="guilabel"} button on the CV row.

To write a CV value to the decoder, enter the CV number, enter the value
and click the `Write`{.interpreted-text role="guilabel"} button on the
CV row.

If you select a \'common CV value\' it will enter the CV number into the
field. From there follow the instructions above for reading or writing
the CV.

Note: Issuing a read or write will automatically turn the track power
on.

See below for issuing DCC-EX commands.

\|force-break\|

### CV Programming (Operation Mode)

<figure class="align-right">
<img src="/_static/images/ex-toolbox/cv_programmer_ops_mode.png"
alt="CV Programming (Ops Mode) Screen" />
<figcaption>EX-Toolbox CV Programming (Operation Mode)
Screen</figcaption>
</figure>

Operation Mode CV Programming is available from the \'CV Programming\'
screen, when \'Program on Main (Operation Mode)\' is selected in the
drop down list at the top of the screen.

Operation Mode CV Programming ONLY allows you to *Write* CVs.

To use Operation Mode CV Programming **you must know the DCC Address**
of the decoder/loco you want to change. Note: you should never try to
change the DCC Address of the decoder/loco using Operation Mode CV
Programming.

On this screen you can:

- write a new DCC Address to the decoder
- write a CV value to the decoder
- select from a list of named, common CVs
- issue \<\> commands to the \|EX-CS\|

To write a CV value to the decoder, enter the DCC Address of the
decoder, enter the CV number, enter the value and click the
`Write`{.interpreted-text role="guilabel"} button on the CV row.

If you select a \'common CV value\' it will enter the CV number into the
field. From there follow the instructions above for writing the CV.

> Issuing a read or write will automatically turn the track power on.
>
> The CV Programming Page has a feature specific to CV29. When you read
> CV29; \|BR\| a) it explains what you need to change the value to to
> disable the \'Speed Table\', and \|BR\| b) it explains what you need
> to change the value to to change default direction of the loco.

See below for issuing DCC-EX commands.

------------------------------------------------------------------------

### Issuing \<\> Commands

On several of the screens in \|EX-TB\| you can issue native DCC-EX `<>`
commands to your \|EX-CS\|.

Enter the command you want to send, and click `Send`{.interpreted-text
role="guilabel"}.

The command you send, and any responses from the command station will be
shown below.

If you select a \'common command value\' it will enter the command the
field. From there follow the instructions above for issuing the command.

You can use the `Next`{.interpreted-text role="guilabel"} and
`Prior`{.interpreted-text role="guilabel"} buttons to retrieve
previously issues commands.

\|force-break\|

------------------------------------------------------------------------

## Speed Matching

Speed Matching assists with making two or more locos run at similar
speeds.

<figure class="align-right">
<img src="/_static/images/ex-toolbox/speed_matching.png"
alt="Speed Matching Screen" />
<figcaption>EX-Toolbox Speed Matching Screen</figcaption>
</figure>

To access the Speed Matching either:

- Swipe Left from the CV-Programming Screen

- Swipe Right from the Loco Status Screen

- Select \'Speed Matching (PoM)\' from the Menu

  > <iframe width="336" height="189" src="https://www.youtube.com/embed/7WyWR8xYvgY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Requirements

1.  A loop of track - `MAIN`
2.  A `PROG` track - or be prepared to switch the loop to `PROG`
    temporarily. (see Notes)
3.  A loco that you wish to be the Master. i.e. that you want to make to
    other locos match.
4.  One or more \'Second\' locos that you wish to match to the Master.
5.  That you have run all the locos (the \'Master *and* any \'Second\'
    loco) for 5-10 minutes to warm them up. Many locos run differently
    when warm.

### Assumptions

1.  Assumes that you have already configured the \'Master\' to be the
    way you want it and the other locos to behave.

> The \'Master\' should be the naturally slowest loco of the set, not
> necessarily the one that will be run in the lead position. \|BR\| i.e.
> Test your locos on their default settings first, and find the slowest.
>
> The low speed test uses a speed setting of [5]{.title-ref} (0-126). If
> your locos don\'t start moving at that setting it would be advisable
> to adjust Low speed setting and/or the Kick Start of the \'Master\'
> first.

2.  Assumes that, at least, the \'Second\' loco is configured to use the
    High, Mid, Low CVs, not the full 28 step \'Speed Table\'. (Part of
    CV29) \|BR\| Not critical, but it is advisable to have the
    \'Master\' also use the High, Mid, Low CVs.

    The CV Programming Page of \|EX-TB\| has a feature specific to CV29.
    When you read CV29, it explains what you need to change the value to
    to disable the \'Speed Table\'.

3.  It is highly advisable that **BACK-EMF** is turned off on all locos
    that will be run in a consist. If you don\'t you will likely
    encounter surging of the locos as they speed up and slow down under
    individual load.

    **BACK-EMF** is referred to by some manufacturers as \'Dynamic
    Compensation for Speed Stabilisation\', \'Scaleable Speed
    Stabilisation\' or \'Load Compensation\'. Unfortunately there is no
    standard way to disable BACK-EMF. You will need to refer to the
    manuals for your decoders.

    [This
    page](https://tonystrains.com/news/dcc-motor-control-with-back-emf-and-p-i-d/)
    has a detailed explanation of BACK-EMF and details on how to change
    it for a number of manufacturers.

### Instructions

1.  Open \|EX-TB\| and go to the Speed Matching screen.
2.  Put the/a second (non-master) loco on the `PROG` track. (see Notes)
3.  Click `Read -PROG trk`{.interpreted-text role="guilabel"}.

> This reads 8 CV values, including the loco address and CV29, and loads
> them in to the fields, with a 3 second delay between each read. \|BR\|
> Watch for any -1 responses (failed reads), and redo the read if any
> have failed.

4.  Put the \'Master\' on the `MAIN` track (the loop of track), along
    with the \'Second\' loco.
5.  Enter the [DCC address]{.title-ref} of the Master.
6.  Click the Low `Set Speed`{.interpreted-text role="guilabel"} button.
7.  Watch and adjust the speeds of the Second loco in relation the
    Master, util they run at the same speed:

> If the \'Second\' is too slow, either:
>
> > a)  Edit and increase the [Low]{.title-ref} value and click
> >     `Write`{.interpreted-text role="guilabel"}.
> > b)  Click the `+`{.interpreted-text role="guilabel"} button.
>
> If the \'Second\' is too fast, either:
>
> > a)  Edit and decrease the [Low]{.title-ref} value and click
> >     `Write`{.interpreted-text role="guilabel"}.
> > b)  Click the `-`{.interpreted-text role="guilabel"} button.

8.  Repeat for the \'Mid\' Speed.
9.  Repeat for the \'High\' Speed.
10. Adjust the decoder momentum (Acceleration/Deceleration) and [Kick
    Start]{.title-ref} as needed. Test by starting and stopping the
    locos from the three different speeds.
11. If you have more locos to match, repeat from step 2.

### Notes:

> 1.  By default, the `+`{.interpreted-text role="guilabel"} and
>     `-`{.interpreted-text role="guilabel"} buttons change the CV
>     values by 1. You can change this step amount by editing the
>     \'Step\' field. \|BR\| e.g. When I start on a loco, I normally
>     have the Step at 10. When it gets closer to a match I change the
>     step to 1.
> 2.  You don\'t need a separate `PROG` track. You can use the \'Track
>     Manager\' screen to temporarily set the loop of track to `PROG`
>     for steps 2-3, then change it back to `MAIN` for steps 4 on.
> 3.  Some decoders don\'t support Kick Start.
> 4.  Some decoders don\'t allow you to turn BACK-EMF off. Check your
>     decoder manual.
> 5.  The low speed test uses a speed setting of `5` (0-126). If your
>     locos don\'t start moving at that setting it would be advisable to
>     adjust Low speed setting and/or the Kick Start of the \'Master\'
>     first.

\|force-break\|

------------------------------------------------------------------------

## Speedometer

<figure class="align-right">
<img src="/_static/images/ex-toolbox/speedometer.png"
alt="Speedometer Screen" />
<figcaption>EX-Toolbox Speedometer Screen</figcaption>
</figure>

The Speedometer allows you to calulate the scale speed of a loco as it
passes two defined sensors. The sensors can be of any type, but must be
configured in your \|EX-CS\| and be a known (any) distance apart.

1.  Define you sensors in the \|EX-CS\| configuration, and note their
    numbers.
2.  Measure the distance between the sensors.
3.  Open the Speedometer screen in \|EX-TB\|.
4.  Enter the two sensor numbers.
5.  Enter the distance between the sensors, and select the Scale.
6.  Put the loco you want to measure on the track before the first
    sensor.
7.  Start the loco moving.

The Speedometer will display the speed as the loco after it passes the
second sensor.

The speed and times will automatically reset after 10 seconds, but you
can overide this by clicking the `Start`{.interpreted-text
role="guilabel"} button. Or you can change the delay period.

To check the speed in the opposite direction, simply reverse the sensor
numbers, using the `Swap`{.interpreted-text role="guilabel"} button.

The Speedometer will remember the last used sensors and distance between
sessions.

Example configuration of two IR sensors in `mySetup.h`

``` cpp
SETUP("<S 22 22 1>");  // Infrared Or Optical Sensor {S22} on pin 22
SETUP("<S 23 23 1>");  // Infrared Or Optical Sensor {S23} on pin 23
```

\|force-break\|

------------------------------------------------------------------------

## Loco Status

Loco Status allows you to watch changes to all locos being controlled by
the command station.

<figure class="align-right">
<img src="/_static/images/ex-toolbox/loco_status.png"
alt="Loco Status Screen" />
<figcaption>EX-Toolbox Loco Status Screen</figcaption>
</figure>

To access the Track Manager either:

- Swipe Right from the Speed Matching Screen
- Swipe Left from the Current Status Screen
- Select \'Loco Status\' from the Menu

\|force-break\|

------------------------------------------------------------------------

## Track Manager

(Only available when connected to EX-CommandStation version 5.0.0 and
above.)

<figure class="align-right">
<img src="/_static/images/ex-toolbox/track_manager.png"
alt="Track Manager" />
<figcaption>EX-Toolbox Track Manager Screen</figcaption>
</figure>

To access the Track Manager either:

- Swipe Right from the CV-Programming Screen
- Swipe Left from the Current Status Screen
- Select \'Track Manager\' from the Menu

Track Manager allow you to change up to 8 channels (depending on the
Motor Driver you are using)

Each channel can be one of:

- `DCC PROG` - Programming Track
- `DCC MAIN` - Main Track
- `DC`
- `DC reversed polarity (DCX)`
- `OFF`

Select the value you want for the channels and click
`Set`{.interpreted-text role="guilabel"}

Note. If you select `DC` or `DCX` you must select a DCC address for the
channel before pressing `Set`. What ever address you select, selecting
that address on your throttle (e.g. Engine Driver) will result in the DC
locomotive on the track connected to that channel to respond.

Note. Only one channel can be `PROG`. If you select more that one, one
will turned `OFF`.

\|force-break\|

------------------------------------------------------------------------

## Servo motor testing and adjustment

<figure class="align-right">
<img src="/_static/images/ex-toolbox/servos.png" alt="Servos Screen" />
<figcaption>EX-Toolbox Servos Screen</figcaption>
</figure>

The servo motor test screen will allow you to test and fine tune the
settings needed for configuring servo motors attached to the \|EX-CS\|.
This is intended to be temporary. To permanently configure a servo motor
you will need to record the values and include the in the configuration
of your \|EX-CS\|.

To access the Servo configuration screen either:

- Swipe Right from the Sensor Screen
- Swipe Left from the CV Programming Screen
- Select \'Servos\' from the Menu

On the Servo motor screen,

- Enter the VPin of the servo motor you want adjustment
- Enter any known starting values for Close, Mid, Throw
- Test the Close, Mid, Throw positions by pressing the appropriate
  button. The servo will move to that position.
- Fine adjust any of the three positions by using the
  `+`{.interpreted-text role="guilabel"} or `-`{.interpreted-text
  role="guilabel"} buttons \|BR\| The servo will gradually move.
- when you are happy, record the three values

\|EX-TB\| remembers the servos that you have changed (up to 10) in this
and previous sessions, and you can select one of the previous servos
from the drop down list. \|EX-TB\| will restore the last settings you
used for the selected servo to the main fields.

\|force-break\|

------------------------------------------------------------------------

## Sensor testing

<figure class="align-right">
<img src="/_static/images/ex-toolbox/sensors.png"
alt="Sensors Screen" />
<figcaption>EX-Toolbox Sensors Screen</figcaption>
</figure>

The Sensor test screen will allow you to test any sensors configured in
your \|EX-CS\|.

To access the Sensor Testing configuration screen either:

- Swipe Right from the Current Status Screen
- Swipe Left from the CV Servos Screen
- Select \'Sensors\' from the Menu

When the screen opens the first 100 sensors found will be shown.
Activity on the sensors will be shown on the screen. Scroll down to if
needed.

The `Watch`{.interpreted-text role="guilabel"} button is generally not
needed, but will force \|EX-TB\| to check the available sensors on the
\|EX-CS\| again.

\|force-break\|

------------------------------------------------------------------------

## Current Meter

(Only available when connected to EX-CommandStation version 5.0.0 and
above.)

<figure class="align-right">
<img src="/_static/images/ex-toolbox/currents.png"
alt="Current Meter Screen" />
<figcaption>EX-Toolbox Current Meter Screen</figcaption>
</figure>

The Current Status screen will show you the current values for up to
eight channels on the motor driver on your \|EX-CS\|.

To access the Current Meter screen either:

- Swipe Right from the Track Manager Screen
- Swipe Left from the Sensors Screen
- Select \'Current Status\' from the Menu

For each channel the following is shown:

- the up-to-date value in Milliamps
- the highest value seen recently in Milliamps
- the maximum value able to be supplied by the moto shield in Milliamps

The readings start as soon as you open the screen and are paused as soon
as you exit the screen. The readings are taken every three seconds.

You can manually stop the readings with the `Stop`{.interpreted-text
role="guilabel"} button.

You can manually restart the readings with the `Start`{.interpreted-text
role="guilabel"} button. This will also clear the \'Highest\' values.

\|force-break\|

------------------------------------------------------------------------

## WiFi Setup

(The WiFi Settings screen is only available when connected to
EX-CommandStation version 5.7.0 and above.)

Prior to version 5.7.0, WiFi configuration for \|EX-CS\| was done
through options in the `config.h` file. This method required users to
modify the firmware (by editing `config.h`) and recompile it for their
specific WiFi settings.

From version 5.7.0, it is necessary to use a new WiFi configuration
method, which involves connecting to the \|EX-CS\| *after you have
flashed the firmware.* You do so by connecting to the \|EX-CS\| via USB
or by connecting to the WiFi Access Point network of the CS and issuing
a set of new commands.

See the
`/ex-commandstation/advanced-setup/supported-wifi/wifi-config_v5_7`{.interpreted-text
role="doc"} page for more details.

\|EX-TB\| provides a screen to allow you to issue the necessary commands
to change the WiFi settings of your \|EX-CS\|.

<figure class="align-right">
<img src="/_static/images/ex-toolbox/wifi_setup_sta_mode.png"
alt="WiFi Settings Screen - STA mode" />
<figcaption>EX-Toolbox WiFi Settings Screen - STA Mode</figcaption>
</figure>

### Station Mode

Station Mode WiFi configuration is available from the \'WiFi Setup\'
screen, when \'WiFi Station Mode\' is selected in the drop down list at
the top of the screen.

The Station Mode WiFi configuration allows you to set the
[SSID]{.title-ref} and [password]{.title-ref} of the WiFi network that
your \|EX-CS\| will connect to, and also allows you to set the
[hostname]{.title-ref} of the \|EX-CS\| on that network.

To change the *Station Mode* enter a [SSID]{.title-ref} (the name of the
network), and a [password]{.title-ref} of at least 8 characters and
presse either the `Set Station`{.interpreted-text role="guilabel"}
button for a permanent change, or the `Set Temp`{.interpreted-text
role="guilabel"} button for a temporary change.

To change the *hostname* enter the hostname and press the
`Set Hostname`{.interpreted-text role="guilabel"} button.

\|force-break\|

<figure class="align-right">
<img src="/_static/images/ex-toolbox/wifi_setup_ap_mode.png"
alt="WiFi Settings Screen - AP mode" />
<figcaption>EX-Toolbox WiFi Settings Screen - AP Mode</figcaption>
</figure>

### Access Point Mode

Access Point Mode WiFi configuration is available from the \'WiFi
Setup\' screen, when \'WiFi Access Point Mode\' is selected in the drop
down list at the top of the screen.

The Access Point Mode WiFi configuration allows you to set the
[SSID]{.title-ref}, [password]{.title-ref} and optional
[Channel]{.title-ref} of the WiFi Access Point network that your
\|EX-CS\| will create, and also allows you to set the
[hostname]{.title-ref} of the \|EX-CS\| on that network.

:::: note
::: title
Note
:::

The \'Access Point\' mode buttons will not become avaliable if you are
connected to the \|EX-CS\| via WiFi, as you can\'t change the Access
Point mode settings over WiFi. You need to be connected via USB to
change the Access Point mode settings.
::::

To change the *Access Point* enter a [SSID]{.title-ref} (the name of the
network), and a [Password]{.title-ref} of at least 8 characters and
press the `Set Access Point`{.interpreted-text role="guilabel"} button.

To change the *hostname* enter the hostname and press the
`Set Hostname`{.interpreted-text role="guilabel"} button.

\|HR-DASHED\|

:::: note
::: title
Note
:::

In every case above where you press one of the buttons, the Command
Station will restart to apply the new settings. You will need to
reconnect to the Command Station.
::::

See the
`/ex-commandstation/advanced-setup/supported-wifi/wifi-config_v5_7`{.interpreted-text
role="doc"} page for more details on the meaning of these settings.

\|force-break\|

------------------------------------------------------------------------

## Secondary Screens

### Power

<figure class="align-right">
<img src="/_static/images/ex-toolbox/power.png" alt="Power Screen" />
<figcaption>EX-Toolbox Power Screen</figcaption>
</figure>

<figure class="align-right">
<img src="/_static/images/ex-toolbox/power_menu.png" alt="Power menu" />
<figcaption>EX-Toolbox Power menu</figcaption>
</figure>

**Turning Track Power On**

There are two ways to turn the Track Power on/off:

- Power Screen - accessed from the menu
- Power Action Bar button - needs to be enable in the preferences

The *Power Screen* can be accessed from the
`Menu --> Power`{.interpreted-text role="menuselection"}. This will open
the Power Screen where there is a simple button that to turn the power
on or off. Use the `Close`{.interpreted-text role="guilabel"} button or
Android\'s `Back`{.interpreted-text role="guilabel"} button to return to
the CV-Programming Screen.

If the *Power Action Bar button* is enabled, simply click on it to turn
track power on or off.

:::: note
::: title
Note
:::

You can also optionally enable the Power Button on the Action bar in the
preferences.
::::

\|force-break\|

### Preferences

Most configuration options are found in the *Preferences* which is
accessed via the overflow menu which is normally three dots (⁞) or three
bars (≡).

### View log

Accessed from any of the main screens via
`Menu --> View Log`{.interpreted-text role="menuselection"}.

This screen allows you to view the internal EX-Toolbox log of events.
(referend to as \'logcat\').

The option to [Start recording to file]{.title-ref} creates a
user-accessible file that can be sent to the \|EX-TB\| app developers to
assist you in resolving a problem.

The file will be located on your Android device/phone at: Internal
storage `/Android/data/dcc_ex.ex_toolbox/files` \|br\|and will be named
something like: `logcat9999999999999.txt`

Optionally enable the preference to include the timestamp on each line
of the log.

### Saving a Log File

To record a log file in \|EX-TB\|\....

1.  Start \|EX-TB\|.
2.  From the menu, select `View Log`{.interpreted-text role="guilabel"}
3.  Click `Start recording to a file`{.interpreted-text role="guilabel"}
4.  Click `Close`{.interpreted-text role="guilabel"}\`
5.  Attempt whatever is causing the problem a few times
6.  Exit \|EX-TB\|
7.  Connect a USB cable to your device/phone and PC
8.  Allow access if the device/phone asks.
9.  In some versions of Android you may also need to change the
    connection type on the device/phone from \'charging\' to \'file
    transfer\'
10. Open a file manager and find the connected device/phone
11. Browse down to the folder \...Internal shared
    storageAndroiddatadcc_ex.ex_toolboxfiles
12. Find the most recent file that looks like `logcatxxxxxxxxxxxxx.txt`
    e.g. logcat1699833098998.txt
13. Attach that file to a message in discord using the
    `+`{.interpreted-text role="guilabel"} button on the row of the
    message content\`\`\`

### About

This screen displays

- Information about \|EX-TB\|
- Information about the \|EX-CS\| it is currently connected to (if any)
- A page of basic information about \|EX-CS\|

\|force-break\|

------------------------------------------------------------------------

## Connecting via JMRI

\|EX-TB\| can\'t normally connect to a \|EX-CS\| through \|JMRI\|,
however it is possible if you `Load DCC++ over TCP Server` in the
\'DCC-EX\' menu in \|JMRI\|, then connect \|EX-TB\| to the additional
server that is presented in Connection screen. It will be the same name
as your JMRI Railroad name, but will have \" \[DCC-EX\]\" appended to
it.

------------------------------------------------------------------------

## Connecting via USB

\|EX-TB\| can\'t normally connect to an \|EX-CS\| via USB, however it is
possible to temporarily create a USB to IP connection on your PC using
tools like *socat* or *SerialToIPGUI* (for windows).

Using *socat* in Linux:

> `socat TCP4-LISTEN:2560 /dev/ttyUSB0,b115200,raw,echo=0`
>
> or (to provide more information)
>
> `socat -d -d -d TCP4-LISTEN:2560 /dev/ttyUSB0,b115200,raw,echo=0`
>
> Note: Change \'dev/ttyUSB0\' to the appropriate USB port that the
> command station is connected to.

Using *socat* in Microsoft Windows:

> `socat TCP-LISTEN:2560 /dev/ttyS11,b115200,raw,echo=0`
>
> or (to provide more information)
>
> `socat -d -d -d TCP-LISTEN:2560 /dev/ttyS11,b115200,raw,echo=0`
>
> Note: Change S11 to the appropriate USB port. Whatever \'COM\' number
> appears in the Device Manager, subtract 1. \|BR\| i.e. \'COM12\' in
> the Windows Device Manager becomes \'/dev/ttyS11\'

Using *SerialToIPGUI* (For Microsoft Windows) (Recommended):

> <figure class="responsive-image">
> <img src="/_static/images/SerialToIPGUI/SerialToIPGUI.png"
> class="responsive-image" alt="SerialToIPGUI" />
> <figcaption aria-hidden="true">SerialToIPGUI</figcaption>
> </figure>
>
> - start SerialToIPGUI
> - Select the correct COM port for the command station
> - Enter the port of \'2560\'
> - Click `Start`{.interpreted-text role="guilabel"}
>
> Once started\...
>
> - Open \|EX-TB\| on your Android device
> - Enter the IP address of your PC (The one running socat or
>   SerialToIPGUI)
> - Enter the port of \'2560\'
> - Click `connect`{.interpreted-text role="guilabel"}

:::: important
::: title
Important
:::

This \'trick\' only supports a single connection at a time. So it is
important that \|JMRI\| (if you are using it), or the \|IDE serial
monitor\|, or anything else that might be using the COM (USB) port are
shut down first.
::::

### Downloads

> - *SerialToIPGUI* - <https://sourceforge.net/projects/serialtoip/>
> - *socat* for windows requires downloading the \'cgywin\' and
>   installing the optional \'socat\' package when you install -
>   <https://www.cygwin.com/>

------------------------------------------------------------------------

### Troubleshooting (Windows socat)

In Microsoft Windows and using the command line socat, if you see a
\"command not found\" error, Here is what you need to do to fix it:

- Right click on \"My Computer\" -\> Properties -\> Advanced -\>
  Environment Variables
- Add a new environment variable, called `CYGWIN_HOME` and set its value
  to `C:\cygwin`
- Edit the PATH environment variable and add `C:\cygwin\bin` to it
  (usually separated by a \';\').
- Just click okay, exit any command prompts or bash shells (over cygwin)
  you may have open, and open it again - it\'ll work!

Note that if you installed cgywin to a folder *other than
\"C:\\cgywin\"* (e.g. c:\\cgywin64), use that folder name instead in the
change above.

------------------------------------------------------------------------

## Android apps on Windows

Although\|EX-TB\| is an Android app, it is possible to run it on windows
PCs.

See the `/throttles/software/android-apps-on-windows`{.interpreted-text
role="doc"} page for more information.
