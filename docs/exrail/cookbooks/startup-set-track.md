\|EX-R-LOGO\|

# Define Track Modes at Startup

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

By default the Command station will start with:

- Track A - [MAIN`
- Track B - `PROG`

The following lines can be added to `myAutomation.h` to define tracks as
needed.

``` cpp
AUTOSTART 
  SET_TRACK(A,MAIN)
  SET_TRACK(B,PROG)
  SET_TRACK(C,MAIN)
  SET_TRACK(D,MAIN)
  POWEROFF
DONE
```

`POWEROFF` is the default.

`POWERON` will set MAIN tracks ON.

Other track modes require the `SET_POWER` command, for each track. \|BR\|

: \|\_\| \|\_\|
  `Example: Set a track to DC ](dc-tracks.md)
  \|BR\| \|\_\| \|\_\| \|\_\| \|\_\| **NOTE:** The use of the `SET_LOCO`
  command for DC mode tracks.
