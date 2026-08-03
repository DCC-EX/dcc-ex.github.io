::: {.meta keywords="EX-CommandStation Command Station EX-Installer Testing"}
:::

# Testing your installation

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|
\|githublink-ex-installer-button-small\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="1" local=""}
On this page
:::
::::

## Using the EX-Installer Device Monitor

Once you have selected a device in \|EX-I\| on the \"Select your
device\" screen, or after successfully loading software onto your
device, a `View device monitor` button will be available.

\|force-break\|

<figure class="align-left">
<img src="/_static/images/ex-installer/view-device-monitor.png"
alt="Select Device screen" />
<figcaption>Select your device screen</figcaption>
</figure>

<figure class="align-center">
<img
src="/_static/images/ex-installer/view-device-monitor-load-screen.png"
alt="Load software screen" />
<figcaption aria-hidden="true">Load software screen</figcaption>
</figure>

\|force-break\|

When clicking this button, the \|Device Monitor\| window will open,
allowing you to interact with your device by sending commands and
viewing the serial console output.

<figure class="align-center">
<img src="/_static/images/ex-installer/device-monitor.png"
alt="Device Monitor" />
<figcaption aria-hidden="true">Device Monitor</figcaption>
</figure>

Within the \|Device Monitor\| window, you will see the serial console
output of your device. As you can see in this screen shot, certain key
bits of information are highlighted to help identify these when asked by
the \|DCC-EX\| team.

The following information is highlighted for \|EX-CS\|:

- \|EX-CS\| version information (green)
- WiFi firmware version (green)
- WiFi SSID and password in access point mode (blue)
- WiFi SSID in station (STA) mode (blue)
- WiFi IP address and port (purple)

### Sending commands

You can send any supported command to your device by typing it into the
\"Enter command\" box and clicking the \"Send\" button. Refer to the
`/reference/software/command-summary-consolidated`{.interpreted-text
role="doc"} for the list of available commands. This will also work for
the \|EX-TT\|
`ex-turntable/test-and-tune:ex-turntable interactive serial console commands`{.interpreted-text
role="ref"} and \|EX-IO\| `/ex-ioexpander/index`{.interpreted-text
role="doc"} commands.

### Saving startup or serial console logs

When interacting with the \|DCC-EX\| team for support, you will likely
be asked to provide the \"startup logs\", or output from the serial
console of your device.

Using \|Device Monitor\| is the simplest way to obtain this information
by using the `Save log` button.

<figure class="align-center">
<img src="/_static/images/ex-installer/save-device-log.png"
alt="Save device log" />
<figcaption>Save device log screen</figcaption>
</figure>

Using this option, you can browse to a location on your computer you can
easily find (such as your Desktop), allowing you to upload this to
Discord or a GitHub issue and share with the team.

When clicking the `Save and open log` button, it will save the file, but
also open it on your screen. This way, if you\'re unable to upload the
file for some reason, you can copy and paste the text instead.

## Using the Arduino IDE Serial Monitor

This page is a brief introduction to using the \|IDE Serial Monitor\|.
For additional information see the
`/reference/tools/serial-monitor`{.interpreted-text role="doc"} page.

To test with the \|IDE Serial Monitor\|, download the \|Arduino IDE\|
from the following link and install it on your computer.

[Download the Arduino IDE](https://www.arduino.cc/en/software)

To do a quick test, open the Arduino application:

![The Arduino
IDE](/_static/images/installer/arduino_ide.jpg){alt="Arduino IDE"}

- Select \"Tools -\> Serial Monitor\" from the \|Arduino IDE\| menu

![Open the Serial Monitor from the Tools
Menu](/_static/images/installer/arduino_ide2.jpg){alt="Open the Serial Monitor"}

You will see the following screen:

![Serial Monitor](/_static/images/installer/serial_monitor.jpg)

- Select \"115200\" as the baud rate in the dropdown in the lower right
- Select \"Both NL & CR\" from the dropdown next to the baud rate

When you open the \|IDE serial monitor\| you will see at least one line
sent out as status information. If you have a WiFi board or Ethernet
Shield you will see a page full of log information as it configures and
connects to your network.

At the top of the \|IDE serial monitor\| type `<s>` (lowercase \"s\")
into the command textbox and press \"Send\". You should see:

``` cpp
<iDCC-EX V-0.2.1 / MEGA / STANDARD_MOTOR_SHIELD G-9db6d36>
```

This is the \"status\" command and reports your version, types of boards
you are using, and a build number.

There are a lot of other commands you can enter here. As a matter of
fact, you could use the \|IDE serial monitor\| to test any of the DCC-EX
API (application programming interface) commands. Please see the [DCC-EX
Wiki](https://github.com/DCC-EX/CommandStation-EX/wiki) for a list of
commands or for additional information on using the \|IDE serial
monitor\| see the `/reference/tools/serial-monitor`{.interpreted-text
role="doc"} page.

## Using EX-WebThrottle

![EX-WebThrottle](/_static/images/installer/exwebthrottle.jpg)

Click this link:
`EX-WebThrottle </ex-webthrottle/index>`{.interpreted-text role="doc"}
to run EX-WebThrottle hosted on our site, or visit
[GitHub](https://github.com/DCC-EX/WebThrottle-EX) to get the latest
version to run on your computer.

## Using Engine Driver (or other WiThrottle Protocol Throttle) - Requires WiFi

![Engine Driver](/_static/images/installer/engine_driver.png)

You will need to install \|Engine Driver\| on your mobile device and
then connect to the Command Station, either directly with AP mode or
through your router with Station Mode. You can then use your phone to
control your trains.
