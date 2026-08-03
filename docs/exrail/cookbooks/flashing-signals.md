\|EX-R-LOGO\|

# Signals with flashing (Blink)

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: 

::: 
On this page
:::
::::

## Blinking Signals

Blinking is achieved with the command:

``` cpp
BLINK(vpin, onMs, offMs)
```

which will start a vpin blinking until such time as it is `SET`, `RESET`
or set by a signal operation such as `RED`, `AMBER`, `GREEN`.

`BLINK` returns immediately, the blinking is autonomous.

## Always Blink AMBER

A signal that always blinks amber could be done like this:

``` cpp
SIGNALH(130,131,132)

ONAMBER(130) 
  BLINK(131,500,500) 
DONE
```

The `RED` or `GREEN` calls will turn off the amber pin and that will
stop the blink automatically.

Amber and Flashing Amber

A signal that has normal `AMBER` and flashing `AMBER` could be done by
creating a new macro to implement a `FLAMBER(signalid)` command

``` cpp
// create a new command
#define FLAMBER(signal) \
        AMBER(signal) \
        BLINK(signal+1,500,500)

SIGNAL(130,131,132) 

// then where necessary you can 
AMBER(130)   // set signal to AMBER
// or 
FLAMBER(130) // set signal to flashing amber
```

(Caution: this assumes that the amber pin is redpin+1 in the `SIGNAL` or
`SIGNALH` definition)
