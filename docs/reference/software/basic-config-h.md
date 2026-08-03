\|EX-REF-LOGO\|

# Basic config.h settings

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: 

::: 
On this page
:::
::::

**Basic config.h settings for Command Station build**

During compilation and build, there are a number of settings that
control the way the code is constructed and important features are
configured.

Most configuration takes place in EXRAIL but some things just need
setting before that.

If you are using the EX-Installer, the important options will be
automatically managed and configured. There are several more advanced
options covered in the
`/reference/software/advanced-config-h`
but these should not trouble the vast majority of users.

These options should be coded in the file [config.h] which
will be automatically included in the compilation process.

## Motor shield definition (Mandatory) 

``` cpp
#define MOTOR_SHIELD_TYPE typeName
```

The motor shield definition tells the code how many tracks your command
station has and which pins are used to talk to the motor shield(s). It
also describes the electrical characteristics of the current sensing and
the current limits to be applied to each track.

There are a number of pre-defined motor shield typeNames available of
which the most common are:

- STANDARD_MOTOR_SHIELD : Arduino Motor shield Rev3 based on the L298
  with 18V 2A per channel
- EX8874_SHIELD : DCC-EX TI DRV8874 based motor shield
- EXCSB1 : DCC-EX CSB-1 hardware
- EXCSB1_WITH_EX8874 : DCC-EX CSB-1 hardware with DCC-EX TI DRV8874
  shield
- NO_SHIELD : CS without any motor shield (as an accessory only CS)

Further pre-defined shield names can be found in the code file
MotorDrivers.h although their presence there does not necessarily mean
that we can provide support for issues.

## WiFi settings

Ignore this if you do not have WiFi on your command station or choose to
avoid it.

WiFi has two operating modes:

- AP (Access point) means the Command station acts as its own private
  WiFi network so throttle devices must connect first to the Command
  Station Wifi network.
- STA (Station mode) means the command station connects to your WiFi
  router and appears as a device on that network. If the WiFI is
  configured for STA mode, but fails to connect to your router, it will
  fall back to AP mode in much the same way as smart plugs, lights etc.

### Setup STA (Station) mode

``` cpp
#define ENABLE_WIFI true
#define WIFI_SSID "deadBudgie"
#define WIFI_PASSWORD "myHovvercraftIsFullOfEels"
```

### Setup AP (Access Point) default mode

``` cpp
#define ENABLE_WIFI true
```

The WiFi chip will first try to connect to the previously configured
network and if that fails fall back to Access Point mode.

The SSID of the AP will be automatically set to [DCCEX\_\*]
where the [\*] part is taken from an internal device number
(for example [DCCEX_12b7c]) to try and avoid duplications.
The password will be set to [PASS\_\*] where the
[\*] part matches the generated SSID name.

### Setup AP (Access Point) advanced mode

``` cpp
#define ENABLE_WIFI true
#define WIFI_FORCE_AP true
#define WIFI_SSID "MyCSB1"
#define WIFI_PASSWORD "Don't tell him Pike!"
#define WIFI_CHANNEL 1
```

The AP mode password must be at least 8 characters long.

The default channel is set to \"1\". Use a phone WiFi analyser app to
see which channels are relatively quiet in your area. If you need to use
an alternate channel (we recommend using only 1,6, or 11) you may change
it here.

- WIFI_HOSTNAME: The default is \"dccex\" but you can change this if you
  have more than one CS on you home router to make them show up with
  different names on the network. \|BR\| Host names starting with
  \"dccex\" are more readily found by WiFi throttles.

``` cpp
#define WIFI_HOSTNAME "dccex-csb1"
```

In some environments you may want to hide the SSID from phones scanning
for access points. If you do hide the SSID, it is still possible to
connect by entering the SSID manually on the phone/tablet.

``` cpp
#define WIFI_HIDE_SSID
```

## Ethernet settings

It is not valid to enable Ethernet and WiFi at the same time.

``` cpp
#define ENABLE_ETHERNET true
```

## LCD/OLED support 

The LCD feature requires an I2C enabled LCD screen using a Hitachi
HD44780 controller and a commonly available PCF8574 based I2C
\'backpack\'. To define LCD_DRIVER for I2C address 0x27, 16 cols, 2 rows

``` cpp
#define LCD_DRIVER  0x27,16,2
```

For an OLED display define OLED_DRIVER \[address,\]width,height in
pixels (address auto detected if not supplied)

128x32 or 128x64 I2C SSD1306-based devices are supported. Use 132,64 for
a SH1106-based I2C device with a 132x64 display.

For example

``` cpp
#define OLED_DRIVER 132,64
```

OR

``` cpp
#define OLED_DRIVER 0x3c,132,64
```

Define scroll mode as 0, 1 or 2

- 0 is scroll continuous (fill screen if possible),
- 1 is by page (alternate between pages),
- 2 is by row (move up 1 row at a time).

``` cpp
#define SCROLLMODE 1
```

In order to avoid wasting memory the current scroll buffer is limited to
8 lines. Some users wishing to display additional information such as
TrackManager power states have requested additional rows aware of the
warning that this will take extra RAM. if you wish to include additional
rows

``` cpp
#define MAX_CHARACTER_ROWS 12
```

## Disable EEPROM

The EEPROM feature is only there for backward support of deprecated
methods of turnout, sensor and output creation inherited from DCC++. You
are advised to turn this off to save memory.

``` cpp
#define DISABLE_EEPROM
```

## Delayed startup

Some newer 32bit microcontrollers boot very quickly, so powering on I2C
and other peripheral devices at the same time may result in the
CommandStation booting too quickly to detect them.

To work around this, set STARTUP_DELAY to a value in milliseconds that
works for your environment.

``` cpp
#define STARTUP_DELAY 3000
```
