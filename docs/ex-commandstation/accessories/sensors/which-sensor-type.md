# Which sensor type to use?

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="1" local=""}
On this page
:::
::::

A common topic that arises in support chats in Discord is which sensor
type to use in various scenarios.

There are a number of different advantages and disadvantages to the
various sensor types which we aim to cover on this page.

There are five types of sensors we will cover here:

- Infrared sensors
- Hall effect sensors
- Block occupancy detectors
- Proximity (and time-of-flight) sensors
- Video Sensors

------------------------------------------------------------------------

## Infrared sensors

Infrared sensors consist of a light emitting source and receiver to
detect when an object passes over or through the beam of infrared light.

There are two different ways to have these configured:

- Using reflection, whereby the emitter/receiver are side-by-side and
  are activated by the infrared light reflecting back to the receiver
  (typically the default option when purchasing)
- Using beam break, whereby the emitter/receiver are facing each other,
  and are activated by an object breaking the beam (typically requires
  modification by desoldering and relocating the transmitter and
  receiver)

  -----------------------------------------------------------------------
  Advantages                          Disadvantages
  ----------------------------------- -----------------------------------
  Inexpensive, can be purchased in    Are affected by room and natural
  bulk at very low prices             lighting changes, although beam
                                      break can combat this

  Simple to setup and use             Can be difficult to hide in beam
                                      break configuration

  No locomotive or rolling stock      Can be difficult to install under
  modifications required (e.g.        track in smaller scales (N and Z)
  resistor wheels or magnets)         

  Can be used to detect both ends of  Typically require modification to
  a train                             use in beam break configuration

  Can be used to detect a train       
  entering or exiting a specific      
  point on a layout                   
  -----------------------------------------------------------------------

:!!! note "::: title
Note"
:::

There are options for using modulation or sending data streams via
infrared to make these sensors more reliable, but these are commonly
either DIY options or are more expensive than the bulk buy options
available on eBay or AliExpress.
::::

Refer to
`/ex-commandstation/accessories/sensors/ir-sensor`{.interpreted-text
role="doc"} for further information on infrared sensors.

------------------------------------------------------------------------

## Hall effect sensors

Hall effect sensors consist of a hall effect device mounted between the
track rails, and a suitable magnet located on the underside of
locomotives and rolling stock.

  -----------------------------------------------------------------------
  Advantages                          Disadvantages
  ----------------------------------- -----------------------------------
  Inexpensive, can be purchased in    Requires suitable magnets to be
  bulk at very low prices             attached to locomotives and rolling
                                      stock

  Not prone to interference from      Can be unreliable at faster train
  changes to light sources            speeds

  Can be used to detect a train       Can only detect the point at which
  entering or exiting a specific      the magnet is attached, not the
  point on a layout (caveat being the front/rear of a train
  point at which the magnet is        
  attached)                           
  -----------------------------------------------------------------------

:!!! note "::: title
Note"
:::

It\'s been observed that the reliability of hall effect sensors can be
improved by connecting them to MCP23017 I/O expanders and using the
interrupt capability rather than simply letting the polling cycles
detect the sensor changes.

Refer to
`reference/developers/hal:hal programming interface`{.interpreted-text
role="ref"} for further information on using the interrupt pin.
::::

------------------------------------------------------------------------

## Block occupancy detectors

Block occupancy detectors are quite commonly found in \|DC\| layouts and
have been a very popular method for detecting when a locomotive and/or
rolling stock is occupying a \|DC\| power district or a specific,
isolated section of track.

These typically work by detecting current being drawn through the track
power wiring, requiring resistor wheelsets to be installed on rolling
stock. A locomotive requires no modification as the motor (or DCC
decoder) will enable this detection.

  -----------------------------------------------------------------------
  Advantages                          Disadvantages
  ----------------------------------- -----------------------------------
  No locomotive modifications         Rolling stock requires resistor
  required                            wheelsets to be detected

  DC layouts converting to DCC may    May require track wiring
  already have these in place         alterations

                                      Cannot detect the front or rear of
                                      a train, nor a specific point on a
                                      layout
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Proximity sensors

Proximity sensors work by detecting objects within a specific distance
range from the sensor, and are also able to measure the specific
distance to objects, improving detection reliability.

There are various types of proximity sensors available, with the most
commonly available on breakout boards being time-of-flight sensors such
as the VL53L0X.

  -----------------------------------------------------------------------
  Advantages                          Disadvantages
  ----------------------------------- -----------------------------------
  Can typically work reliably in all  Typically a more expensive option
  lighting situations                 

  No locomotive or rolling stock      More complex to setup and configure
  modifications required (e.g.        than infrared sensors
  resistor wheels or magnets)         

  Can be used to detect both ends of  Limited options on breakout boards,
  a train                             other sensors are a DIY option

  Can be used to detect a train       
  entering or exiting a specific      
  point on a layout                   
  -----------------------------------------------------------------------

Refer to
`/ex-commandstation/accessories/sensors/vl53l0x-tof-sensor`{.interpreted-text
role="doc"} for further information on the VL53L0X time-of-flight
sensor.

------------------------------------------------------------------------

## Video Sensors

Video sensors are a recent invention that monitor a large number of
predefined points (or lines) to detect the presence of a locomotive or
rolling stock at specific locations. The current version of EX-SensorCAM
can monitor up to 80 spots or up to 10 lines for detection of image
changes. It can also be used for human/cat intrusion detections.

A single sensorCAM camera looks for changes from a reference image of
the spot (or line) and communicates with the Command Station via i2c
cable. Multiple CAM\'s can be used to cover wider areas.

**Advantages**

- Can replace many of the sensors above
- No layout wiring and hiding of discrete sensors required
- Extremely easy to add or relocate sensors for automations
- Replace multiple GPIO expanders
- May use mirrors to see round corners.

**Disadvantages**

- Initial setup is more complex
- Suitable environment (e.g. lighting) conditions are essential
- Can\'t see into tunnels, so user may need a mix of sensor types
- Power-on requirements need consideration
- Not currently suitable for exhibition layouts

Refer to <https://github.com/DCC-EX/EX-SensorCAM/> \|EXTERNAL-LINK\| for
further information on sensorCAM.
