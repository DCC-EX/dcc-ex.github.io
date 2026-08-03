# WiThrottle

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="2" local=""}
On this page
:::
::::

![iOS Logo](/_static/images/throttles/icon_ios.png){.align-left}

This is an iOS App from the USA. \|WiThrottle\| is probably the most
popular iOS throttle since early on when \|JMRI\| built a \|WiThrottle
Server\| into its program. You can connect WiThrottle to \|JMRI\| and
connect \|JMRI\| to \|EX-CS\|, or you if you are not going to use
\|JMRI\|, you can connect directly to the Command Station if you install
a WiFi board.

Please visit their website: <https://www.withrottle.com>
\|EXTERNAL-LINK\|

You can find it in the App Store:
[WiThrottle](http://itunes.apple.com/app/id344172578) \|EXTERNAL-LINK\|

For more information more information about these protocols, see
`WiThrottle Server, Web Server, DCC-EX Native Commands Explained </throttles/protocols>`{.interpreted-text
role="doc"}

## Features {#withrottle-features}

- Supports WiThrottle Protocol
- Connects to \|JMRI\|
- Connects to \|EX-CS\| if not using \|JMRI\|
- Connects via WiFi

## Screenshots {#withrottle-screenshots}

![WiThrottle Screenshot 1](/_static/images/throttles/withrottle1.png)

## Requirements {#withrottle-requirements}

- A \|EX-CS\| (Mega based for WiFi)
- An iOS Cell Phone or Tablet
- A WiFi Shield (or other ESP8622 solution) if you want to connect using
  WiFi
  `Wifi Setup </ex-commandstation/diy/wifi-setup>`{.interpreted-text
  role="doc"}

## Operation {#withrottle-operation}

To use WiFi, make sure you have a WiFi enabled \|EX-CS\| as described in
the `Wifi Setup </ex-commandstation/diy/wifi-setup>`{.interpreted-text
role="doc"} section.

- Open the network settings on your phone
- Change to same network of the PC that \|JMRI\| is on
- Start the \|WiThrottle\| App
- \|WiThrottle\| will try to find the \|WiThrottle Server\| on the
  \|EX-CS\|
- If you are using \|Access Point Mode\|
  - It should find the \|WiThrottle Server\| in \|JMRI\| and
    automatically connect to it

:::: {.important .important-float-right}
::: title
Important
:::

\|wiThrottle Lite\| (the free version) does not have the `Track Power`
function. You will either need to purchase the full version, or you can
`add a startup command </ex-commandstation/advanced-setup/startup-config>`{.interpreted-text
role="doc"}.
::::

- You should then see the \'Address Screen\'

- Turn the track power on by selecting the \'settings\' tab and clicking
  on the `Track Power`

  > - The four red LEDs on the Motor board will turn on

- Go back to the \'Address\' tab

- Enter the DCC Address of the loco you put on the track in the `Keypad`
  field

- Select `Long` or `Short` (normally if the address is less than 127, it
  should be a \'Short\' address.)

- Click the `Set`{.interpreted-text role="guilabel"} button

- The address should appear in the green box at the top left.

- Select the \'Throttle\' tab

- You can now use the sliders to move your train
