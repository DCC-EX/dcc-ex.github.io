\|EX-R-LOGO\|

# Flags, Counters and Bitmaps

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="1" local=""}
On this page
:::
::::

These are implemented by a software-only driver that mimics a set of
VPINs that can be used for both digital and analogue values. Unlike
sensors and leds, these VPINs are both **INPUT** and **OUTPUT** These
can be used in many ways:

- As a simple digital flag to assist in inter-thread communication.
- A flag or value that can be set from commands and tested in
  \|EX-R\|.(e.g. to stop a sequence)
- As a counter for looping or occupancy counts such as trains passing
  over a multi track road crossing.
- As a collection of 16 digital bits that can be set, reset, toggled,
  masked and tested.

Existing `<>` and \|EX-R\| commands for vpins work on these pins.

## Creating virtual pins

``` cpp
HAL(Bitmap,firstpin,npins) 
```

creates 1 or more virtual pins in software.

e.g. `HAL(Bitmap,1000,20)` creates pins 1000..1019

## Use as flags

When used as a digital flag, these pins can be changed or tested with
the basic digital pin commands common to all VPINs. `SET`, `RESET`,
`BLINK`, `IF`, `ONBUTTON`, `ONSENSOR` and so forth. Serial commands
operate in the same way.

## Use as counters

For loop counting, counters can be incremented by `BITMAP_INC(1013)` and
decremented by `BITMAP_DEC(1013)` and tested with IF/IFNOT/IFGTE etc.

Counters be used to automate a multi track crossing where each train
entering increments the counter and decrements it on clearing the
crossing. Crossing gate automation can be started when the value changes
from 0, and be stopped when the counter returns to 0.

Detecting the first increment from 0 to 1 can be done with
`ONBUTTON(1013)` and the automation can use `IF(1013)` or `IFNOT(1013)`
to detect when it needs to reopen the road gates.

## Use as analogue values (advanced)

Analog values may be set into the virtual pins and tested using the
existing analog value commands and exrail macros. `<z vpin value>`
`<D ANIN vpin>` etc. and in EXRAIL `ANOUT(vpin,value,0,0)`

## Use as binary flag groups (advanced)

Virtual pins (and others that respond to an analog read in order to
provide bit mapped digital data, such as SensorCam) can be set and
tested with new special EXRAIL commands

`IFBITMAP_ALL(vpin,mask)` Bitwise ANDs the the vpin value with the mask
value and is true if ALL the 1 bits in the mask are also 1 bits in the
value.

> e.g. `IFBITMAP_ALL(1013,0x0f)` would be true if ALL the last 4 bits of
> the value are 1s.

`IFBITMAP_ANY(1013,0x0f)` would be true if ANY of the last 4 bits are
1s.

### Modifying bitmap values

`BITMAP_AND(vpin,mask)` performs a bitwise AND operation.
`BITMAP_OR(vpin,mask)` performs a bitwise OR operation
`BITMAP_XOR(vpin,mask)` performs a bitwise EXCLUSIVE OR (which is
basically a toggle).
