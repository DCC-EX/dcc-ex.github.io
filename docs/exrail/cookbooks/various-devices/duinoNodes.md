\|EX-R-LOGO\|

# Lew\'s Duino Gear boards

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: 

::: 
On this page
:::
::::

CAUTION: these boards require several GPIO pins on the Command Station
and are therefore unsuitable for use with a CSB1 which has all available
pins essentially reserved for track management.

## DNIN8 8 Input board

This is a shift-register implementation of a digital input collector.
Multiple DNIN8 may be connected in a chain sequence but it is IMPORTANT
that the software configuratuion correctly represents the number of
boards connected otherwise the results will be meaningless.

Define boards in \|EX-R\| using
`HAL(IO_DNIN8, firstVpin, numPins, clockPin, latchPin, dataPin)`

``` cpp
HAL(IO_DNIN8, 400, 16, 40, 42, 44)
```

This will create VPINs 400-415 using two DNIN8 boards connected in
sequence. VPINS 400-407 will be on the first board (closest to the CS)
and 408-415 on the second.

Note: 16 pins uses two boards. You may specify a non-multiple-of-8 pins
but this will be rounded up to a multiple of 8 and you must connect ONLY
the number of boards that this takes.

This example used Arduino GPIO pins 40,42,44 as these are conveniently
side-by-side on a Mega which is easier when you are using a 3 strand
cable.

## DNIN8K 8 Input board

This module works the same as DNIN8 but you must use DNIN8K in the HAL
setup instead of DNIN8. You can\'t mix 8 and 8k versions in the same
string of boards but you can create another string of boards.

## DNOU8 8 Output board

DNOU8 works in a very similar fashion to the the DNIN boards and is defined in \|EX-R\| using

: HAL(IO_DNOU8, firstVpin, numPins, clockPin, latchPin, dataPin)

``` cpp
HAL(IO_DNOU8, 450, 16, 45, 47, 49)
```

This creates a string of output VPINs 450-465 (and thus on 2 boards).
Note the clock/latch/data pins must be different to any DNIN8 or DNIN8K
pins.
