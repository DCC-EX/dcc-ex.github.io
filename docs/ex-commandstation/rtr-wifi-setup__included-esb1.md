\|EX-CS-LOGO\|

# WiFi Configuration

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

The \|EX-CSB1\| comes with WiFi onboard.

::: sidebar
**Using JMRI (Alternate)**

\|conductor\| \|BR\| An *Alternate* to connecting to your
\|EX-CSB1-SHORT\| directly via WiFi is to do so indirectly through
\|JMRI\|. To do this you use a USB cable instead. This is described on
the
`/ex-commandstation/advanced-setup/supported-connections/jmri`{.interpreted-text
role="doc"} page.
:::

The WiFi on your \|EX-CSB1-SHORT\| allows connection up to 10 WiFi
throttles (e.g. phones) DIRECTLY to it, eliminating the need for a
computer and another software controller.

However, use use of WiFi is optional. If you wish to simply use your
computer connected via a USB cable to the \|EX-CSB1-SHORT\| with the
\|JMRI\| application (or similar), you can
`skip ahead to the next page </ex-commandstation/installer-rtr>`{.interpreted-text
role="doc"}.

If you wish to run trains from your phone, tablet or other \|WiThrottle
protocol\| devices connected directly to the \|EX-CSB1-SHORT\| over
WiFi, without a PC involved, then you will only need to select how you
are going to configure the WiFi during the software installation stage,
by choosing either **Access Point** mode or **Station** mode.

- **Access Point mode** \|BR\| You can configure the EX-CommandStation
  to have its own, completely isolated, WiFi Network. This is referred
  to as *Access Point Mode*. (Most useful if your layout is away from
  the house / home network, or you transport your layout frequently.)
  \|BR\| \|BR\|
- **Station mode** \|BR\| The EX-CommandStation can be setup so that it
  connects to your existing home WiFi Network. This is referred to as
  *Station Mode*.

\|HR-DASHED\|

:!!! warning "::: title
Warning"
:::

\|SUITABLE\| \|tinkerer\| \|engineer\| \|BR\| Using *WiFi (OR Ethernet)*
to talk between \|JMRI\| and \|EX-CS\| is complex, slow and functionally
limited and, while it generally works, it is NOT SUPPORTED.
::::

:!!! note "::: title
Note"
:::

\|SUITABLE\| \|tinkerer\| \|engineer\| \|BR\| For the \|EX-CSB1-SHORT\|
and DIY ESP32 based Command Stations, the Expermental / Development
(DEVEL) versions of the software from 5.7.0 ignore the WiFi
configuration in the config.h file. see [WiFi configuration (CSB1 or
ESP32
ONLY)](https://dcc-ex.com/mkdocs-test/products/ex-commandstation/config-wifi-esp32/)
for more information.
::::

\|HR-HEAVY\|

## Next Steps

Click the \'Next\' button to see how to install the software on your
\|EX-CSB1\|.
