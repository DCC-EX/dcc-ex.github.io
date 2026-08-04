\|EX-REF-LOGO\|

# Writing a HAL Driver

\|SUITABLE\| \|engineer\| \|support-button\|

Suppose you have a particular device you want to use with \|EX-CS\|, but
there isn\'t a driver for it. Well, you could ask for one, and we may
well write one for you. Or you could write it yourself.

The HAL framework is designed to be extendable by the creation of device
drivers, without needing to modify the base \|EX-CS\| software or the
HAL itself.

A HAL driver is normally created as an include (.h) file, although for
more complex ones it may include source (.cpp) files as well.

The driver follows a simple design pattern. It doesn\'t need to
implement all of the pattern, if you don\'t implement a particular bit
then a default will be used instead.

- Creation - a [create()] function and constructor are
  required;
- Initialisation - a [\_begin()] function is written
  (optional);
- Background operations - a [\_loop()] function is written
  (optional);
- Operations - you can optionally supply any of [\_write()]
  (digital) function, [\_writeAnalogue()] function,
  [\_read()] (digital) function and
  [\_readAnalogue()] function.

Here is a template for a HAL driver, showing these elements:

``` cpp
#ifndef IO_MYDEVICE_H
#define IO_MYDEVICE_H

#include "IODevice.h"
#include "DIAG.h"  // for DIAG calls

class MyDevice: public IODevice 
  static void create(VPIN firstVpin, int nPins, uint8_t i2cAddress) 
private:
  void _begin() override 
  void _loop(unsigned long currentMicros) override 
  int _readAnalogue(VPIN vpin) override 
  int _read(VPIN vpin) override 
  void write(VPIN vpin, int value) override 
  void writeAnalogue(VPIN vpin, int value) override 
  void _display() override 
  uint16_t _value[16];
};
#endif // IO_MYDEVICE_H
```

Take a look at some of the existing HAL drivers, they vary in complexity
but you will see a few different ways of handling devices.

## Performance

One thing to be aware of is the time that the functions you write will
take to execute. If you have a [read]() function that polls a
device, waits for a calculation to be performed and then reads a result,
it may, for example, take some milliseconds to complete. During this
time, nothing else in \|EX-CS\| is able to run (apart from interrupt
code). While this doesn\'t seem a long time, if you have multiple parts
of \|EX-CS\| (Sensor objects, EXRAIL Sequences, etc.) that are reading
the values of multiple pins, then the time will be multiplied and you
may find that other parts of \|EX-CS\| start to slow down.

It is recommended, that:

- Wherever possible, the driver should not wait or delay.
- If possible, data acquisition should be done in the
  [\_loop()] function, so that the [\_read()]
  and [\_readAnalogue()] functions just return the latest
  value acquired.
- Where possible, non-blocking operations should be performed (e.g. in
  i2c) so that an operation can be set up in one [\_loop()]
  entry, and its status be checked in subsequent [\_loop()]
  entries for completion.
