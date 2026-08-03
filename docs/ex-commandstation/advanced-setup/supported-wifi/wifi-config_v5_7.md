orphan

: 

\|EX-CS-LOGO\|

# WiFi Configuration for version 5.7.0+

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="2" local=""}
On this page
:::
::::

This page is exclusively for users of \|EX-CS\| version 5.7.0 and later.
Version 5.7.0 is currently in the experimental / development (DEVEL)
phase and is not recommended for general users.

If you are using an earlier version, please see
`WiFi Config  <wifi-config>`{.interpreted-text role="doc"}.

Also see [WiFi configuration (CSB1 or ESP32
ONLY)](https://dcc-ex.com/mkdocs-test/products/ex-commandstation/config-wifi-esp32/#configuring-the-host-name)
on the new web site for more technical information.

## Background

Prior to version 5.7.0, WiFi configuration for \|EX-CS\| was done
through options in the `config.h` file. This method required users to
modify the firmware (by editing `config.h`) and recompile it for their
specific WiFi settings.

From version 5.7.0, WiFi configuration options in `config.h` are
*ignored* by the CSB1 or ESP32 EX-CommandStations.

It is now necessary to use a new WiFi configuration method, which
involves connecting to the \|EX-CS\| *after you have flashed the
firmware.* You do so by connecting to the \|EX-CS\| via USB or by
connecting to the WiFi Access Point network of the CS and issuing a set
of new commands. (Note that the WiFi Access Point network approach has
limitations. See below.)

The advantage of this is that it is independent of the flashing process,
and will remember your WiFi settings across firmware updates and
changes.

From version 5.7.0, you must configure the WiFi settings through one of
the following methods:

a)  \|EX-WT\| (via USB),
b)  \|EX-TB\| (via USB or over WiFi),
c)  the serial monitor / device monitor of \|EX-I\|, the **Arduino IDE**
    or **VSC** (via USB)
d)  any wifi throttle or app that can send the appropriate commands to
    the \|EX-CS\| over WiFi

\|EX-WT\| and \|EX-TB\| provide a user-friendly interface for
configuring WiFi settings, while the serial monitor method allows for
more direct access to the configuration process but requires more
technical knowledge.

## The WiFi different modes

WiFi on the \|EX-CS\| has two possible operating modes:

- **Access point (AP) mode** means the Command Station acts as its own
  private WiFi network so throttle devices must connect first to the
  Command Station\'s own WiFi network.
- **Station (STA) mode** means the command station connects to your WiFi
  router and appears as a device on that network. If the WiFi is
  configured for STA mode, but fails to connect to your router, it will
  fall back to AP mode in much the same way as smart plugs, lights etc.

There are some additional settings that are not modes but effect the
wifi connection:

- **Channel**: If you need to use an alternate channel in Access Point
  mode (we recommend using only 1,6, or 11) you may change it.

- **Hidden AP mode**: If enabled, the Command Station\'s WiFi network
  will not be visible in the list of available networks on devices. This
  can enhance security by making it less obvious to potential attackers,
  but it also means that users will need to manually enter the network
  name (SSID) to connect.

  > Note that this does not provide any performance advantages.

- **Temporary STA mode**: If enabled, the Command Station will start in
  Station mode and connect to an existing Wifi network. But will forget
  this setting the next time the \|EX-CS\| is restarted.

  > This may be useful if visiting a location with a different WiFi
  > network which you would like to connect to without changing the
  > permanent WiFi settings on the Command Station.

- The **HOSTNAME** setting allows you to set the name that appears in
  your Throttle app, once you have connected to the appropriate network
  for the Command Station.

------------------------------------------------------------------------

## Using USB vs WiFi - Limitations of WiFi

There are significant limitations to be aware of when configuring WiFi
settings over WiFi compared to using a USB connection:

Only **Station (STA) mode** and the **HOSTNAME** can be changed over
WiFi.

**Access Point (AP)** mode changes require a serial/USB connection. This
is a security feature. If you could change AP mode settings over WiFi,
then anyone who could connect to the Command Station\'s WiFi network
could change the AP settings and potentially lock you out of your
Command Station. By requiring a USB connection for AP mode changes, we
ensure that only someone with physical access to the Command Station can
modify these critical settings.

------------------------------------------------------------------------

## Changing the settings

### Using EX-WebThrotttle

1.  Connect your PC to the \|EX-CS\| via USB. Open the \|EX-WT\| and
    select the appropriate COM port for your \|EX-CS\|. You should see
    the current WiFi settings displayed in the interface. See
    `EX-WebThrottle </ex-webthrottle/index>`{.interpreted-text
    role="doc"} for more details.
2.  Go to the `Wifi Setup` page from the menu or the toolbar buttons.
    - To set the **Access Point (AP) mode**, enter the SSID and password
      for the Command Station\'s WiFi network and click the
      `Set Access Point`{.interpreted-text role="guilabel"} button. You
      can optional set a channel for the AP mode, but it is not
      required, and generally not recommended.

      The Command Station will restart and create its own WiFi network
      with the specified SSID and password.

      To set the **Station (STA) mode**, enter the SSID and password for
      your existing WiFi network (eg your home router) and click the
      `Set Station Mode`{.interpreted-text role="guilabel"} button. The
      Command Station will attempt to connect to the specified WiFi
      network. If the connection is successful, it will operate in
      Station mode. If the connection fails, it will revert to Access
      Point mode.

    - To set the **Temporary Station (STA) mode**, enter the SSID and
      password for your existing WiFi network and click the
      `Set Temporary Station Mode`{.interpreted-text role="guilabel"}
      button. The Command Station will attempt to connect to the
      specified WiFi network.

      If the connection is successful, it will operate in Station mode.
      If the connection fails, it will revert to Access Point mode.

    - To set the **Hostname**, enter the desired hostname and click the
      `Set Hostname`{.interpreted-text role="guilabel"} button. The
      Command Station will update its hostname, which will be visible in
      your Throttle app when connected to the appropriate network.

      This is useful if you have more than one \|EX-CS\| on your network
      to make them show up with different names.

**Resetting the Wifi settings**

The `Reset WiFi Settings`{.interpreted-text role="guilabel"} button on
the WiFi Setup page will reset all WiFi settings to their default
values. This will cause the Command Station to restart and create its
own WiFi network in Access Point mode with the default SSID and
password.

:!!! note "::: title
Note"
:::

In every case above, the Command Station will restart to apply the new
settings. You will need to reconnect to the Command Station in the
\|EX-WT\| interface.
::::

\|HR-DASHED\|

### Using EX-Toolbox

\|EX-TB\| provides a similar interface to the \|EX-WT\| for configuring
WiFi settings, but it can be accessed either via USB or over WiFi. The
process for changing WiFi settings in the \|EX-TB\| is essentially the
same as in the \|EX-WT\|, with the same options for AP mode, STA mode,
Temporary STA mode and Hostname.

1.  Connect your PC to the \|EX-TB\| via USB or Wifi. See
    `EX-Toolbox </ex-toolbox/using>`{.interpreted-text role="doc"} for
    more details.
2.  Go to the `WiFi Setup` page from the menu or the toolbar buttons and
    follow the same steps as outlined for the \|EX-WT\| above.

Note: Only **Station (STA) mode** and the **HOSTNAME** can be changed
over WiFi. **Access Point (AP) mode** changes require a USB connection.

:!!! note "::: title
Note"
:::

In every case above, the Command Station will restart to apply the new
settings. You will need to reconnect to the Command Station in the
\|EX-TB\| interface.
::::

\|HR-DASHED\|

### Using EX-Installer, Arduino IDE, VSC, throttle apps

The process for configuring WiFi settings using the serial monitor or
device monitor on any of the EX-Installer, Arduino IDE, VSC or WiFi
throttle apps are esentially the same.

:!!! note "::: title
Note"
:::

In every case below, the Command Station will restart to apply the new
settings. You will need to reconnect to the Command Station in the
app\'s interface.
::::

#### Changing to Station Mode

i.e. your home router. You will need to issue the command:

``` cpp
<C WIFI "routerSSID" "routerPassword">
```

e.g. Sets the STA mode to connect to a router with SSID \"routerSSID\"
and password

The command station will attempt to connect to this network immediately,
and on each rerstart. If it fails to connect, it will revert to AP mode.

#### Changing the Access Point settings

To give the Access point a specific name and a password that will not be
revealed on the OLED use the command:

``` cpp
<C WIFI AP "MyCSB1" "SpamWonderfulSpam">
```

e.g. Sets the AP name to \"MyCSB1\" and the password to
\"SpamWonderfulSpam\":

The AP mode password must be at least 8 characters long.

The default channel is set to \"11\". If you need to use an alternate
channel (we recommend using only 1,6, or 11) you may change it with the
command:

``` cpp
<C WIFI AP "MyCSB1" "SpamWonderfulSpam" 6>
```

Use a phone WiFi analyser app to see which channels are relatively quiet
in your area.

#### Hidden Access Point mode

In some environments you may want to hide the SSID from phones scanning
for access points. If you do hide the SSID, it is still possible to
connect by entering the SSID manually on the phone/tablet.

``` cpp
<C WIFI HIDDENAP "MyCSB1" "SpamWonderfulSpam" 6>
```

#### Configuring the Host Name

The default hostname \"DCCEX\" but you can change this if you have more
than one CS on your network to make them show up with different names.
Host names containing \"DCCEX\" are more readily found by WiFi
throttles.

``` cpp
<C WIFI HOSTNAME "DCCEX-MYCSB1">
```

e.g. Sets the hostname to \"DCCEX-MYCSB1\":

#### Clearing WiFi settings

``` cpp
<C WIFI DEFAULT>
```

WiFi will revert to the internally generated ssid and password.
