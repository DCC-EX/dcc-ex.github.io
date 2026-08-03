# VL53L0X Time of Flight Sensor

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: 

::: 
On this page
:::
::::

Time of Flight (or ToF) sensors can provide a more reliable and accurate
sensor than traditional IR sensors as they are not susceptible to
interference from different and varying lighting conditions.

Further to this, these sensors can be programmed to activate only within
a specific distance range, enabling a large variety of use cases.

\|EX-CS\| has support for the VL53L0X ToF sensor via the
\"IO_VL53L0X.h\" HAL device driver which connects to the \|I2C\| bus of
the CommandStation.

![VL53L0X sensor](/_static/images/vl53l0x/vl53l0x.jpg)

![Adafruit VL53L0X sensor](/_static/images/vl53l0x/adafruit-vl53l0x.jpg)

## Theory of operation

The VL53L0X Time-Of-Flight sensor operates by sending a short laser
pulse and detecting the reflection of the pulse. The time between the
pulse and the receipt of reflections is measured and used to determine
the distance to the reflecting object.

For economy of memory and processing time, this driver includes only
part of the code that ST provide in their API. Also, the API code isn\'t
very clear and it is not easy to identify what operations are useful and
what are not. The operation shown here doesn\'t include any calibration,
so is probably not as accurate as using the full driver, but it\'s
probably accurate enough for the purpose.

## Physical connection

Each VL53L0X device will, by default, reside on the same \|I2C\| address
of 0x29, and therefore connecting multiple devices to the same \|I2C\|
bus requires consideration and planning.

### Connecting a single device

Connecting a single device is a simple matter of connecting the SDA and
SCL pins to the SDA and SCL pins of your \|EX-CS\|, or your \|I2C\| bus
if you have multiple other devices connected.

:!!! warning "::: title
Warning"
:::

If the device\'s XSHUT pin is not connected, then it is very prone to
noise, and the device may even reset when handled. If you\'re not using
XSHUT, then it\'s best to tie it to +5V.
::::

Once connected, you will need to configure the device driver as per
`ex-commandstation/accessories/sensors/vl53l0x-tof-sensor:configuring a single device`.

![Mega2560 with VL53L0X](/_static/images/vl53l0x/mega2560-single-vl53l0x.png)

### Connecting multiple devices

Connecting multiple devices also require connecting each device to the
SDA and SCL pins, however in addition to this, you will need to connect
each device\'s XSHUT pin to an available I/O pin either directly on your
\|EX-CS\|, or to an available I/O pin on an I/O expander such as an
MCP23017. The XSHUT pin connection is required in order to be able to
have each device addressed separately.

Once connected, you will need to configure the device driver for each
device as per
`ex-commandstation/accessories/sensors/vl53l0x-tof-sensor:configuring multiple devices`.

![Mega2560 two VL53L0Xs](/_static/images/vl53l0x/mega2560-dual-vl53l0x.png)

## Device driver configuration

Configuring support for one or more VL53L0X devices requires modifying
\"myHal.cpp\" to include the device driver \"IO_VL53L0X.h\" and add an
entry for each device to be configured.

The device driver allocates up to 3 vpins to each device:

- A digital read on the first pin will return a value that indicates
  whether an object is within the threshold range, and the return value
  will be 1 for true, or 0 for false
- An analogue read on the first pin returns the last measured distance
  (in mm)
- An analogue read on the second pin returns the signal strength
- An analogue read on the third pin returns detected ambient light level

By default, the device takes around 60ms to complete a ranging
operation, so we do a 100ms cycle (10 samples per second).

The VL53L0X is initially set to respond to \|I2C\| address 0x29. If you
only have one module, you can use this address. However, the address can
be modified by software. If you select another address, that address
will be written to the device and used until the device is reset.

To enable support for one or more devices, ensure the \"IO_VL53L0X.h\"
device driver is included at the beginning of your \"myHal.cpp\" file:

``` cpp
#if !defined(IO_NO_HAL)

// Include devices you need.
#include "IODevice.h"
#include "IO_VL53L0X.h"   // Laser time-of-flight sensor
...
```

### Configuring a single device

For a single device, you need a single entry to create the device also
in \"myHal.cpp\":

``` cpp
...

void halSetup() .

## EXRAIL integration

\|EX-R\| enables utilising these devices as both digital and analogue
sensors.

Using the standard digital sensor commands (AT, AFTER, ATTIMEOUT, IF,
IFNOT, IFTIMEOUT) operates as per any other digital sensor, using the
ranges specified when configuring the devices.

For example:

``` cpp
AT(4000)        // Will trigger when an object is within 200mm
AFTER(4003)     // Will trigger 0.5s after an object moves 250mm away
```

::: todo
[LOW - VL53L0X](https://github.com/DCC-EX/dcc-ex.github.io/issues/447)
\|EXTERNAL-LINK\| - validate VL53L0X works with EXRAIL\'s analogue
sensor commands ATGTE, ATLT, IFGTE, IFLT
:::

:!!! note "::: title
Note"
:::

Using a VL53L0X with EXRAIL\'s analogue sensor commands has not been
validated, this may not work.
::::

With \|EX-R\|, you can also use the analogue sensor commands (ATGTE,
ATLT, IFGTE, IFLT) to have automation based on the actual distance from
the sensor, rather than it operating like a simple on/off switch.

For example:

``` cpp
ATGTE(4000, 150)    // Will trigger when an object is 150mm or further away from the sensor
ATLT(4003, 100)     // Will trigger when an object is less than 100mm away
```
