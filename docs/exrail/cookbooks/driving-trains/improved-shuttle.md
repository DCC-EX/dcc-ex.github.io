\|EX-R-LOGO\|

# Improved shuttle

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="1" local=""}
On this page
:::
::::

In this and following examples, the previous example comments have been
removed and new changes commented to make them easier to see. Some lines
have been joined together to keep the example short on screen and make
it generally more human readable.

By adding more sensors, the shuttle can be made more realistic, slowing
down at station approach and making sounds.

``` 
Dogbath                                                  Catflap
||════════════════════════════════════════════════════════════||
  |         |                                      |         |
164       166                                    167       165
```

## Speed changes

Using the \[previous\](40-simple-shuttle.md) example.

``` cpp
AUTOMATION(123,"Dogbath to Catflap shuttle")
  FWD(40)
  AT(167) 
    SPEED(15) // At Catflap slow down point, change speed
  AT(165) 
    ESTOP     // ESTOP avoids any momentum issue   
    DELAYRANDOM(15000,20000)  
    REV(40)  
  AT(166) 
    SPEED(15) // At Dogbath slow down point, change speed
  AT(164) 
    ESTOP 
    DELAYRANDOM(5000,10000)  
FOLLOW(123) 
```

## Sounds and lights

Headlight settings and sounds may be added using the FON(functionNumber)
and FOFF(functionNumber). These numbers will depend on the features of
the loco decoder but it is not an error to send functions to DC or
non-sound locos.

``` cpp
AUTOMATION(123,"Dogbath to Catflap shuttle")
  FON(0) FON(3) DELAY(2000) FOFF(3) // light on, sound whistle for 2 seconds
  FWD(40)
  AT(167) 
    SPEED(15) 
  AT(165) 
    ESTOP
    FOFF(0)  // turn off light 
    DELAYRANDOM(15000,20000)  
    FON(0) FON(3) DELAY(2000) FOFF(3) // Lights and whistle
    REV(40)  
  AT(166) 
    SPEED(15) 
  AT(164) 
    ESTOP 
    DELAYRANDOM(5000,10000)  
FOLLOW(123) 
```

## Signals

Signals don\'t actually control trains, the drivers do. But for model
purposes it is sufficient to include signal changes in the engine
driving script.

In this case we will define a signal at each end of the line using RED &
GREEN leds on extender vpins 170..173. and use them to go green when a
train is allowed to leave each station. Each signal is then only
referred to by the first pin, as you will see.

Remember, its just for show because there can be no other trains on this
line anyway. (Well at least until we get to some more advanced
scenarios.)

Define the signals anywhere but not normally inside an AUTOMATION or
other sequence.

``` cpp
SIGNALH(170,0,171) // Dogbath depart. Red LED on 170, Green on 171, no amber
SIGNALH(172,0,173) // Catflap Depart. 

AUTOMATION(123,"Dogbath to Catflap shuttle")
  GREEN(170) // set Dogbath departure signal to green
  FON(0) FON(3) DELAY(2000) FOFF(3) 
  FWD(40)
  AT(167) 
    SPEED(15)
    RED(170)  // remember to set Dogbath signal red at some point 
  AT(165) 
    ESTOP 
    FOFF(0) 
    DELAYRANDOM(15000,20000)  
    GREEN(172) // Set Catflap departure signal to green
    FON(0) 
    FON(3) 
    DELAY(2000) 
    FOFF(3) 
    REV(40)  
  AT(166) 
    SPEED(15) 
    RED(172) // rember to reset Catflap signal
  AT(164) 
    ESTOP 
    DELAYRANDOM(5000,10000)  
FOLLOW(123) 
```
