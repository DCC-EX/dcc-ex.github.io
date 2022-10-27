.. include:: /include/include.rst
.. include:: /include/include-l3.rst
*****************************
VL53L0X Time of Flight Sensor
*****************************

|conductor| |tinkerer|

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

.. image:: /_static/images/vl53l0x/vl53l0x.jpg
  :alt: VL53L0X sensor
  :scale: 25%

Time of Flight (or ToF) sensors can provide a more reliable and accurate sensor than traditional IR sensors as they are not susceptible to interference from different and varying lighting conditions.

Further to this, these sensors can be programmed to activate only within a specific distance range, enabling a large variety of use cases.

|EX-CS| has support for the VL53L0X ToF sensor via the "IO_VL53L0X.h" HAL device driver which connects to the I2C bus of the CommandStation.

Theory of operation
===================

The VL53L0X Time-Of-Flight sensor operates by sending a short laser pulse and detecting the reflection of the pulse.  The time between the pulse and the receipt of reflections is measured and used to determine the distance to the reflecting object.

For economy of memory and processing time, this driver includes only part of the code that ST provide in their API.  Also, the API code isn't very clear and it is not easy to identify what operations are useful and what are not. The operation shown here doesn't include any calibration, so is probably not as accurate as using the full driver, but it's probably accurate enough for the purpose.

Physical connection
===================

.. todo:: `MEDIUM - VL53L0X <https://github.com/DCC-EX/dcc-ex.github.io/issues/266>`_ - add Fritzing diagram for single and multiple devices

Each VL53L0X device will, by default, reside on the same I2C address of 0x29, and therefore connecting multiple devices to the same I2C bus requires consideration and planning.

Connecting a single device
--------------------------

Connecting a single device is a simple matter of connecting the SDA and SCL pins to the SDA and SCL pins of your |EX-CS|, or your I2C bus if you have multiple other devices connected.

.. warning:: 

  If the device's XSHUT pin is not connected, then it is very prone to noise, and the device may even reset when handled.  If you're not using XSHUT, then it's best to tie it to +5V.

Once connected, you will need to configure the device driver as per :ref:`reference/hardware/other/vl53l0x-tof-sensor:configuring a single device`.

Connecting multiple devices
---------------------------

Connecting multiple devices also require connecting each device to the SDA and SCL pins, however in addition to this, you will need to connect each device's XSHUT pin to an available I/O pin either directly on your |EX-CS|, or to an available I/O pin on an I/O expander such as an MCP23017. The XSHUT pin connection is required in order to be able to have each device addressed separately.

Once connected, you will need to configure the device driver for each device as per :ref:`reference/hardware/other/vl53l0x-tof-sensor:connecting multiple devices`.

Device driver configuration
===========================

Configuring support for one or more VL53L0X devices requires modifying "myHal.cpp" to include the device driver "IO_VL53L0X.h" and add an entry for each device to be configured.

The device driver allocates up to 3 vpins to each device:

- A digital read on the first pin will return a value that indicates whether an object is within the threshold range, and the return value will be 1 for true, or 0 for false
- An analogue read on the first pin returns the last measured distance (in mm)
- An analogue read on the second pin returns the signal strength
- An analogue read on the third pin returns detected ambient light level

By default, the device takes around 60ms to complete a ranging operation, so we do a 100ms cycle (10 samples per second).

The VL53L0X is initially set to respond to I2C address 0x29.  If you only have one module, you can use this address. However, the address can be modified by software.  If you select another address, that address will be written to the device and used until the device is reset.

To enable support for one or more devices, ensure the "IO_VL53L0X.h" device driver is included at the beginning of your "myHal.cpp" file:

.. code-block:: cpp

  #if !defined(IO_NO_HAL)

  // Include devices you need.
  #include "IODevice.h"
  #include "IO_VL53L0X.h"   // Laser time-of-flight sensor
  ...

Configuring a single device
---------------------------

For a single device, you need a single entry to create the device also in "myHal.cpp":

.. code-block:: cpp

  ...
  
  void halSetup() {
    VL53L0X::create(firstVpin, nPins, i2cAddress, lowThreshold, highThreshold);
    ...

Where:

- firstVpin is an available vpin reserved for reading the device
- nPins is 1, 2 or 3
- i2cAddress is the address of the device (normally 0x29 - should be no need to change this for a single device)
- lowThreshold is the distance at which the digital vpin state is set to 1 (in mm)
- highThreshold is the distance at which the digital vpin state is set to 0 (in mm)

For example, this entry configures a device on vpin 4000 using the default address of 0x29. A digital read of this vpin will return a 1 if an object is within 200mm, and will return a 0 if an object moves more than 250mm from the sensor:

.. code-block:: cpp

  ...
  
  void halSetup() {
    VL53L0X::create(4000, 3, 0x29, 200, 250);
    ...

Configuring multiple devices
----------------------------

.. note:: 

  When using multiple devices, do not configure any device to use the default I2C address of 0x29, as this address needs to be free in order to configure each device on startup.

If you have more than one module, then you will need to specify a digital vpin (Arduino digital output or I/O expander pin) which you connect to the module's XSHUT pin.  When the device driver starts, the XSHUT pin is set LOW to turn the module off.  Once all VL53L0X modules are turned off, the driver works through each module in turn by setting XSHUT to HIGH to turn the module on, then writes the module's desired I2C address. In this way, many VL53L0X modules can be connected to the one I2C bus, each one using a distinct I2C address.

Each device needs its own specific entry in "myHal.cpp", and requires an additional argument to specify the digital vpin that connects to the device's XSHUT pin.

.. code-block:: cpp

  ...
  
  void halSetup() {
    VL53L0X::create(firstVpin, nPins, i2cAddress, lowThreshold, highThreshold, xshutPin);
    ...

Where:

- firstVpin is an available vpin reserved for reading the device
- nPins is 1, 2 or 3
- i2cAddress is the address of the device (normally 0x29 - should be no need to change this for a single device)
- lowThreshold is the distance at which the digital vpin state is set to 1 (in mm)
- highThreshold is the distance at which the digital vpin state is set to 0 (in mm)
- xshutPin is the vpin number corresponding to either a direct I/O pin or an I/O pin on an I/O expander

For example, these entries configure two devices on vpins 4000 and 4001, with I2C addresses 0x30 and 0x31. The device at 0x30 is connected directly to an Arduino Mega2560's digital pin 20, and the device at 0x31 is connected to the first digital I/O pin of the first MCP23017 device at vpin 164. A digital read of each of the device's vpins will return a 1 if an object is within 200mm, and will return a 0 if an object moves more than 250mm from the sensor:

.. code-block:: cpp

  ...
  
  void halSetup() {
    VL53L0X::create(4000, 3, 0x30, 200, 250, 20);
    VL53L0X::create(4001, 3, 0x31, 200, 250, 164);
    ...

Sensor configuration for JMRI
=============================

If you are using JMRI and require these to be available as sensors...

Sensor::create(4000, 4000, 0);  // Create a sensor

When an object comes within 200mm of the sensor, a message 
<Q 4000>
will be sent over the serial USB, and when the object moves more than 250mm from the sensor, 
a message
<q 4000>
will be sent.

EX-RAIL integration
===================