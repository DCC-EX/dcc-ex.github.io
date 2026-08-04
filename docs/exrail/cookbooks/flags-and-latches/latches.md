\|EX-R-LOGO\|

# Latches

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

Latches were first introduced into \|EX-R\| as a way of latching a
sensor value or pushbutton on, so that once detected it could be checked
later and not suffer from bouncing. This use is comparatively rare and
has generally been superseded by the more recent
`ONBUTTON </exrail/exrail-command-reference>` event handler.

Latches were also used as a way of setting a flag that could be read
later, for example to remember whether a light had been switched on by a
`ROUTE` so that the next call to the same route could switch it off
again.

Unfortunately, the `LATCH` implementation was designed in a limited way
to support tiny processors like the UNO or NANO so the latch numbers
were limited and could only apply to on-board pins and not extended
VPINs. It became common to use latch numbers above the real pin numbers
but below the artificial software limit (63 on a UNO, 255 on bigger
CPUs) for various flags in routes and automations.

Because of these limitations, it is recommended that you use the much
simpler `/exrail/cookbooks/flags-and-latches/flags` feature which provides virtual VPINs that can be set, reset
and tested without the limitations of `LATCH`.

For example:

``` cpp
HAL(Bitmap,800,16) // create flags 800..815 

ROUTE(600,"Shed lights")
  IF(800)  // is the light on? 
   RESET(120)  // lights off
   RESET(800)
  ELSE  // light is off 
   SET(120)  // lights on
   SET(800)
  ENDIF
DONE
```

Note that the code cannot use `IF(120)` to test if the light is on
because pin 120 is an OUTPUT pin on a physical device.
