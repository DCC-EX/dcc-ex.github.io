\|EX-R-LOGO\|

# Virtual Bitmap device pins (VPINs)

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: 

::: 
On this page
:::
::::

A VPIN is an Arduino pin number that has been extended to include pins
on external devices or expanders.

By giving external device pins unique VPIN numbers, the vast majority of
the pin manipulation required by the user is controlled the same way
regardless of whether the pin is an actual Arduino pin on the main CPU,
an expander pin over \|I2C\| perhaps behind a multiplexer, a virtual pin
or even a software-only pin simulation.

The vast majority of VPINs are either output (e.g. LEDs and servos) or
input (e.g. buttons and sensors) but rarely both.

## Creating virtual pins

Virtual pins are normally defined by specifying the Hardware Driver that
is used to connect to an external device. There is no way for the
command station to know for sure what devices are connected so it must
be told. This is done by including HAL commands in myAutomation.h which
configure the device.

For Example

``` cpp
HAL(PCA9685, 100, 16, 0x40) 
HAL(PCA9685, 116, 16, 0x41) 
HAL(PCA9685, 132, 16, 0x42) 
HAL(PCA9685, 148, 16, )

HAL(MCP23017, 164, 16, 0x20) 
HAL(MCP23017, 180, 16, 0x21) 
```

This would create VPINs 100 to 115 to represent the 16 servo outputs on
the first `PCA9685 </reference/hardware/servo-module>` servo control board at \|I2C\| address 0x40 and VPINs 164 to
179 on the first
`MCP23017 </reference/hardware/gpio-module>` i/o expander. VPINs for two PCA9685 and two MCP23017 are
pre-defined, except for PCA9685 used with Nucleo-144. Refer to wiring
details and fuller list of
`supported I2C devices </reference/hardware/index-i2c>` elsewhere.

## Using OUTPUT VPINS

Pin values can be changed with basic digital pin commands common to all
VPINs. In \|EX-R\|

`SET(180)` `RESET(180)` sets value HIGH or LOW.

`SET(181,5)` or `RESET(181,5)` sets/resets a range of pins (181..185 in
this case).

`BLINK(180,250,750)` sets pin 180 blinking for 250mS on and 750mS off.
Blinking is stopped by a SET or RESET of the pin.

Serial commands can set HIGH/LOW values to VPINs using
`<z 180> <z -180>[ as for any digital output.

## Using INPUT VPINs

`IF(200)` tests if pin value is HIGH.

`ONBUTTON(200)` triggers when a pin goes HIGH. This is most useful for
push buttons connected between the pin and ground. This causes a new
\|EX-R\| task to start and switch bounce will be ignored until the task
completes.

For example:

``` cpp
ONBUTTON(202) 
  RED(11) 
  THROW(2)
  CLOSE(1)
  GREEN(12)
  DONE
```

`ONSENSOR(200)` triggers when a sensor changes state. This is less
useful and you need to use `IF(200)` to see what state the sensor has
changed to.

Other more advanced commands are available, see
`cookbooks ](/exrail/cookbooks/index.md).

## Using INPUT/OUTPUT VPINs

Bitmap pins are software flags with no actual hardware implementation.
They can be used as *INPUT* and *OUTPUT* and thus can be used as flags
between \|EX-R\| processes. See
`Bitmaps </exrail/cookbooks/flags-and-latches/flags>`.
