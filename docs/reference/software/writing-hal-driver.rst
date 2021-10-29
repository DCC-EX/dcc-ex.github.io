===========================
Writing a HAL Driver
===========================

Suppose you have a particular device you want to use with DCC++EX,
but there isn't a driver for it.  Well, you could ask for one, and 
we may well write one for you.  Or you could write it yourself.

The HAL framwork is designed to be extendable by the creation
of device drivers, without needing to modify the base DCC++EX 
software or the HAL itself.  

A HAL driver is normally created as an include (.h) file, although for more
complex ones it may include source (.cpp) files as well.

The driver follows a simple design pattern.  It doesn't need to 
implement all of the pattern, if you don't implement a particular bit
then a default will be used instead.

* Creation - a `create()` function and constructor are required;
* Initialisation - a `_begin()` function is written (optional);
* Background operations - a `_loop()` function is written (optional);
* Operations - you can optionally supply any of `_write()` (digital) function, 
  `_writeAnalogue()` function, `_read()` (digital) function and 
  `_readAnalogue()` function.

Here is a template for a HAL driver, showing these elements:

.. code-block:: cpp

  #ifndef IO_MYDEVICE_H
  #define IO_MYDEVICE_H

  #include "IODevice.h"
  #include "DIAG.h"  // for DIAG calls

  class MyDevice: public IODevice { 
  public:
    // Constructor
    MyDevice(VPIN firstVpin, int nPins) {
      _firstVpin = firstVpin;
      _nPins = min(nPins,16);
      // Other object initialisation here
      // ...
      addDevice(this);
    }
    static void create(VPIN firstVpin, int nPins, uint8_t i2cAddress) {
      new MyDevice(firstVpin, nPins);
    }
  private:
    void _begin() override {
      // Initialise device
      // ...
    }
    void _loop(unsigned long currentMicros) override {
      // Regular operations, e.g. acquire data
      // ...
      delayUntil(currentMicros + 10*1000UL);  // 10ms till next entry
    }
    int _readAnalogue(VPIN vpin) override {
      // Return acquired data value, e.g. 
      int pin = vpin - _firstVpin;
      return _value[pin];
    }
    int _read(VPIN vpin) override {
      // Return acquired data value, e.g.
      int pin = vpin - _firstVpin;
      return _value[pin];
    }
    void write(VPIN vpin, int value) override {
      // Do something with value , e.g. write to device.
      // ...
    }
    void writeAnalogue(VPIN vpin, int value) override {
      // Do something with value, e.g. write to device.
      // ...
    }
    void _display() override {
      DIAG(F("MyDevice Configured on Vpins:%d-%d %S"), _firstVpin, _firstVpin+_nPins-1,
        _deviceState == DEVSTATE_FAILED ? F("OFFLINE") : F(""));
    }
    uint16_t _value[16];
  };
  #endif // IO_MYDEVICE_H

Take a look at some of the existing HAL drivers, they vary in complexity but 
you will see a few different ways of handling devices.

Performance
--------------

One thing to be aware of is the time that the functions you write will take to execute.
If you have a _read() function that polls a device, waits for a calculation to be performed
and then reads a result, it may, for example, take some milliseconds to complete. 
During this time, nothing else in DCC++EX is able to run (apart from interrupt code). 
While this doesn't seem a long time, if you have multiple parts of DCC++EX (Sensor objects, EX-RAIL Sequences, etc.) that 
are reading the values of multiple pins, then the time will be multiplied and you may find 
that other parts of DCC++EX start to slow down.

It is recommended, that:

* Wherever possible, the driver should not wait or delay.
* If possible, data acquisition should be done in the `_loop()`
  function, so that the `_read()` and `_readAnalogue()` functions just return the 
  latest value acquired.
* Where possible, non-blocking operations should be performed (e.g. in I2C) so that
  an operation can be set up in one `_loop()` entry, and its status be checked in 
  subsequent `_loop()` entries for completion.


