\|EX-R-LOGO\|

# Simple shuttle

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="1" local=""}
On this page
:::
::::

Imagine we have a track like this with sensors 164 and 165 at each end.

``` 
Dogbath                                                  Catflap
||════════════════════════════════════════════════════════════||
  |                                                          |
164                                                        165
```

## Sensor positioning

This illustrates an important aspect of \|EX-R\| driving. The sequence
is only interested in one sensor at a time, there is no case for logic
that says \"Oh wait! Sensor 164 has been hit, how do I know which loco
it was and which way it was going\... and was it the loco that hit it or
the end of the reversing train..\"

If you are using magnet-operated sensors that only detect the loco, you
must adjust the sensor positions to take into account the length of the
train when it is reversing. In this case, moving the sensors at the
Dogbath end by one train length towards Catflap.

## Creating the basic AUTOMATION

Create an automation like this. The automation id needs to be unique
amongst all AUTOMATION, ROUTE or SEQUENCE definitions.

``` cpp
AUTOMATION(123,"Dogbath to Catflap shuttle")
  FWD(40) // Set off from Dogbath
  AT(165) // wait until we get to Catflap stopping point 
    STOP // and then stop
    DELAYRANDOM(15000,20000) // wait for driver to have a smoke 
    REV(40) // reverse back 
  AT(164) STOP // At Dogbath 
    DELAYRANDOM(5000,10000) // wait 5 to 10 seconds 
FOLLOW(123) // and follow the sequence again
```

First drive your train to Dogbath, with the front facing Catflap. Select
the automation from your throttle and the train should start after a
random wait.

It should be pretty obvious what this does and where the sensors need to
be to give a reasonable stopping point, but this may depend on inertia
settings in your loco decoder or command station setup.

The `AT` command pauses the driving task until the sensor is activated.

\|EX-R\| commands can be on the same line or separate lines, it makes no
difference but sometimes it\'s easier to read if you put things like
\"AT something DO something\" on one line.

Also notice that this automation will work just as well for a DC loco or
when DCC is being run at 28 speed steps for very old decoders.
