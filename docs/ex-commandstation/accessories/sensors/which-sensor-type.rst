.. include:: /include/include.rst
.. include:: /include/include-l3.rst
*************************
Which sensor type to use?
*************************

|conductor|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

A common topic that arises in support chats in Discord is which sensor type to use in various scenarios.

There are a number of different advantages and disadvantages to the various sensor types which we aim to cover on this page.

There are four types of sensors we will cover here:

- Infrared sensors
- Hall effect sensors
- Block occupancy detectors
- Proximity (and time-of-flight) sensors

Infrared sensors
================

Infrared sensors consist of a light emitting source and receiver to detect when an object passes over or through the beam of infrared light.

There are two different ways to have these configured:

- Using reflection, whereby the emitter/receiver are side-by-side and are activated by the infrared light reflecting back to the receiver (typically the default option when purchasing)
- Using beam break, whereby the emitter/receiver are facing each other, and are activated by an object breaking the beam (typically requires modification by desoldering and relocating the transmitter and receiver)

.. list-table:: 
  :align: center
  :widths: 50 50
  :width: 100%
  :header-rows: 1
  :class: command-table

  * - Advantages
    - Disadvantages
  * - Inexpensive, can be purchased in bulk at very low prices
    - Are affected by room and natural lighting changes, although beam break can combat this
  * - Simple to setup and use
    - Can be difficult to hide in beam break configuration
  * - No locomotive or rolling stock modifications required (eg. resistor wheels or magnets)
    - Can be difficult to install under track in smaller scales (N and Z)
  * - Can be used to detect both ends of a train
    - Typically require modification to use in beam break configuration
  * - Can be used to detect a train entering or exiting a specific point on a layout
    - 

.. note:: 

  There are options for using modulation or sending data streams via infrared to make these sensors more reliable, but these are commonly either DIY options or are more expensive than the bulk buy options available on eBay or AliExpress.

Refer to :doc:`/ex-commandstation/accessories/sensors/ir-sensor` for further information on infrared sensors.

Hall effect sensors
===================

Hall effect sensors consist of a hall effect device mounted between the track rails, and a suitable magnet located on the underside of locomotives and rolling stock.

.. list-table:: 
  :align: center
  :widths: 50 50
  :width: 100%
  :header-rows: 1
  :class: command-table

  * - Advantages
    - Disadvantages
  * - Inexpensive, can be purchased in bulk at very low prices
    - Requires suitable magnets to be attached to locomotives and rolling stock
  * - Not prone to interference from changes to light sources
    - Can be unreliable at faster train speeds
  * - Can be used to detect a train entering or exiting a specific point on a layout (caveat being the point at which the magnet is attached)
    - Can only detect the point at which the magnet is attached, not the front/rear of a train

.. note:: 

  It's been observed that the reliability of hall effect sensors can be improved by connecting them to MCP23017 I/O expanders and using the interrupt capability rather than simply letting the polling cycles detect the sensor changes.

  Refer to :ref:`reference/developers/hal:hal programming interface` for further information on using the interrupt pin.

Block occupancy detectors
=========================

Block occupancy detectors are quite commonly found in DC layouts and have been a very popular method for detecting when a locomotive and/or rolling stock is occupying a DC power district or a specific, isolated section of track.

These typically work by detecting current being drawn through the track power wiring, requiring resistor wheelsets to be installed on rolling stock. A locomotive requires no modification as the motor (or DCC decoder) will enable this detection.

.. list-table:: 
  :align: center
  :widths: 50 50
  :width: 100%
  :header-rows: 1
  :class: command-table

  * - Advantages
    - Disadvantages
  * - No locomotive modifications required
    - Rolling stock requires resistor wheelsets to be detected
  * - DC layouts converting to DCC may already have these in place
    - May require track wiring alterations
  * - 
    - Cannot detect the front or rear of a train, nor a specific point on a layout

Proximity sensors
=================

Proximity sensors work by detecting objects within a specific distance range from the sensor, and are also able to measure the specific distance to objects, improving detection reliability.

There are various types of proximity sensors available, with the most commonly available on breakout boards being time-of-flight sensors such as the VL53L0X.

.. list-table:: 
  :align: center
  :widths: 50 50
  :width: 100%
  :header-rows: 1
  :class: command-table

  * - Advantages
    - Disadvantages
  * - Can typically work reliably in all lighting situations
    - Typically a more expensive option
  * - No locomotive or rolling stock modifications required (eg. resistor wheels or magnets)
    - More complex to setup and configure than infrared sensors
  * - Can be used to detect both ends of a train
    - Limited options on breakout boards, other sensors are a DIY option
  * - Can be used to detect a train entering or exiting a specific point on a layout
    - 

Refer to :doc:`/ex-commandstation/accessories/sensors/vl53l0x-tof-sensor` for further information on the VL53L0X time-of-flight sensor.