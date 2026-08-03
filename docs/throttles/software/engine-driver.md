# Engine Driver

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="2" local=""}
On this page
:::
::::

![Android Logo](/_static/images/throttles/icon_android.png){.align-left}

![Android Logo](/_static/images/throttles/engine_driver_logo.png){.align-left}

**Engine Driver** (ED) is an Android App that uses the \|WiThrottle
Protocol\| *or* the \|DCC-EX Native Commands\| to connect directly to
the \|EX-CS\| via WiFi. It can also connect to the JMRI WiThrottle
Server via WiFi using the \|WiThrottle Protocol\|.

If you wish to connect Engine Driver directly to \|EX-CS\|, you need to
add a WiFi option to your \|EX-CS\| as explained here:
`WiFi Setup </ex-commandstation/diy/wifi-setup>`{.interpreted-text
role="doc"}.

If you wish to connect Engine Driver to \|JMRI\|, you need to start the
\|WiThrottle Server\| and (optionally[^1]) the Web Server in JMRI on the
computer running \|JMRI\|. The \|JMRI\| computer must be connected to
the \|EX-CS\| using a USB cable.

## Platforms {#ed-platforms}

![Android Logo](/_static/images/throttles/icon_android.png){.align-left}

[Get \'Engine Driver Throttle\' from the Google Play
Store](https://play.google.com/store/apps/details?id=jmri.enginedriver)
\|EXTERNAL-LINK\|

Visit the Engine Driver Website: <https://enginedriver.mstevetodd.com/>
\|EXTERNAL-LINK\| for more information.

Extensive help is available at the [Engine Driver
Home](https://flash62au.github.io/EngineDriver_Home/index.html)
\|EXTERNAL-LINK\| site.

> <iframe width="336" height="189" src="https://www.youtube.com/embed/N6TWR7fIl0A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Standard Features (all WiThrottle servers) {#ed-features}

- Control one to six locomotives or consists
- Speed and direction control
- Up to 29 DCC functions
- Create and edit consists (software-defined)
- Control layout power, turnouts, routes, and access JMRI web panels and
  windows
- \'Discover Server\' Detect, Select & Connect to WiFi enabled Command
  Stations
- \'Roster Server\' download Engine ID\'s & function keys from the
  Command Station
- \'Virtual Engine Sounds\' {Bell, Horn, Short Horn, Mute} for motor
  only decoders, on first two throttles
- Able to use inexpensive Bluetooth gamepads for tactile control
- Multiple theme, colours and throttle layout options

## EX-CommandStation Specific or Advantageous Features

- DCC-EX EXRAIL Automation {Handoff}, Route {Set} and EXRAIL Command
  function buttons
- Able to select local images for roster locos
- New \'Request Loco ID\' & \'Drive Away\' feature from a Program track
  onto Mainline track with \|EX-CS\|

`/throttles/driveaway`{.interpreted-text role="doc"}

## EX-CommandStation Specific Features - when using the DCC-EX Native Protocol

- Read and write DCC addresses on the Programming Track
- Read and write CVs of decoders on the Programming Track
- Write CVs of decoders on the Main Track
- Issue Native commands to the \|EX-CS\|
- TrackManager control - able to change the type and state of each
  Track/Channel (e.g DCC and DC))

`/throttles/software/engine-driver-native-protocol`{.interpreted-text
role="doc"}

## Screenshots {#ed-screenshots}

![Engine Driver Main Screen](/_static/images/throttles/ed1.png){.align-left}

![Engine Driver 2](/_static/images/throttles/ed2.png){.align-left}

![Engine Driver 3](/_static/images/throttles/ed3.png){.align-left}

![Engine Driver 4](/_static/images/throttles/ed4.png){.align-left}

::: rst-class
clearer
:::

## Operation {#ed-operation}

See <https://enginedriver.mstevetodd.com/operation/getting_started.html>
\|EXTERNAL-LINK\|

and <https://enginedriver.mstevetodd.com/videos/index.html>
\|EXTERNAL-LINK\|

::: todo
[LOW -
Software](https://github.com/DCC-EX/dcc-ex.github.io/issues/436) - Give
some setup tutorial here. Need a video to match since ED is the top used
software
:::

------------------------------------------------------------------------

## Using a Bluetooth Gamepad Controller

Here is one of a number of Bluetooth controllers that provides extra
function buttons and you can hold by placing your finger in the ring and
using the buttons and DPAD.

![Ring Shape Hand Controller](/_static/images/throttles/bt_controller2.jpg){.align-center}

[Walmart](https://www.walmart.com/ip/Gamepad-Ring-Shape-Wireless-VR-Joystick-Rechargeable-Bluetooth-compatible-V4-0-Game-Controller/443871148?wmlspartner=wlpa&selectedSellerId=101036302)
\|EXTERNAL-LINK\|

[AliExpress](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20220515220821&isPremium=y&SearchText=%22r1%22+bluetooth+game+controller&spm=a2g0o.productlist.1000002.0)
\|EXTERNAL-LINK\|

:::: note
::: title
Note
:::

From Steve: I set speedsteps to 10, change amount to 1, repeat delay to
9999, horizontal switching layout, throttle web view. I acquire
loco/consist using my phone, then dim & lock and put phone in my
holster. Then I can \"bump\" the joystick up and down 3,2,1,0,-1,-2,-3,
easily keeping track of the current \"notch\". 1 is coupling speed, 2 is
switching/yard speed, 3 is mainline. If I\'m at home, I put the
Conductor view in the web and I have my work for each location.
::::

![Engine Driver Conductor View](/_static/images/throttles/ed_conductor_view1.png){.align-center}

More information is available on the [Engine
Driver](https://enginedriver.mstevetodd.com/operation/gamepads.html#example-gamepads&gsc.tab=0l)
\|EXTERNAL-LINK\| site.

## Adding a Physical Dial (Knob)

It is possible to easily add a rotary dial (knob) to \|Engine Driver\|.
see `/throttles/hardware/engine-driver-physical-knobs`{.interpreted-text
role="doc"} for more information.

## Recording a log file in EngineDriver

If you are having difficulties with Engine Driver connecting to an
\|EX-CS\| it is very helpful if you can provide the support team with a
log file of when the problem occurs.

To record a log file in EngineDriver:

1.  Start ED.
2.  From the menu, select `View Log`
3.  Click `Start recording to a file`{.interpreted-text role="guilabel"}
4.  Click `Close`{.interpreted-text role="guilabel"}
5.  Attempt whatever is causing the problem a few times
6.  Exit ED
7.  Connect a USB cable to your phone and PC
8.  Allow access if the phone asks.
9.  In some versions of Android you may also need to change the
    connection type on the phone from \'charging\' to \'file transfer\'
10. Open a file manager and find the connected phone
11. Browse down to the folder
    `...\Internal shared storage\Android\data\jmri.enginedriver\files`
12. Find the most resent file that looks like `logcatxxxxxxxxxxxxx.txt`
    e.g. logcat1699833098998.txt
13. Attach that file to a message here in discord using the paperclip
    button on the toolbar above the message content

------------------------------------------------------------------------

### Footnotes

- The \|WiThrottle Protocol\| is the proprietary protocol developed by
  Brett Hoffman at <https://www.WiThrottle.com> \|EXTERNAL-LINK\|

[^1]: the Web server is required if you want to show the Loco images in
    Engine Driver.
