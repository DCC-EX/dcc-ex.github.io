\|EX-R-LOGO\|

# Power On at Startup

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

By default the Command station will start with the track power OFF.

This can be inconvenient if you are using the free version of the
\|WiThrottle\| app from the Apple store which does not have a power
button.

You can configure \|EX-R\| to power on at startup by using

``` cpp
AUTOSTART 
  POWERON 
DONE
```

Alternatively, you can power tracks individually

``` cpp
AUTOSTART
  SET_POWER(A,ON)
  SET_POWER(D,ON)
DONE
```
