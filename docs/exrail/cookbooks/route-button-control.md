\|EX-R-LOGO\|

# Manipulating Route Buttons

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="1" local=""}
On this page
:::
::::

## Hiding, disabling, and re-captioning route buttons

Route buttons appear on the throttle and can be controlled from \|EX-R\|
to hide, disable or recaption the button. Everything here applies
equally to AUTOMATIONs.

If a route button can be in one of 4 states:

- Inactive (waiting to be pressed)
- Active (highlighted as if selected)
- Disabled (you can\'t press this)
- Hidden (the entire route is not visible on the throttle)

This allows \|EX-R\| to prevent multiple conflicting routes to be set,
or to replace the default \"Set\" button with open/close, start/stop,
yes/no, on/off or whatever makes most sense in context.

Here are examples of solving the same problem but with different user
experiences. In this case we want a way of setting a light on or off.

## Simple light switch route

> This example just has the logic to switch a light on/off with the
> \"Set\" button. It uses the route state to remember whether the light
> is on or off. Note that the route state will default to inactive and
> the light will default to off.

``` cpp
ROUTE(600,"Shed lights")
  IFROUTE_ACTIVE(600)  // is the light on? 
    RESET(120)        // lights off
    ROUTE_INACTIVE(600)
  ELSE  // light is off 
    SET(120)  // lights on
    ROUTE_ACTIVE(600)
  ENDIF
DONE
```

## Changing button captions

The same logic includes changing the button caption from \"Set\" to
\"Turn On\" or \"Turn Off\". The `AUTOSTART` section is to make sure the
caption is set correctly at startup.

``` cpp
ROUTE(600,"Shed lights")
  IFROUTE_ACTIVE(600)  // is the light on? 
    RESET(120)        // lights off
    ROUTE_INACTIVE(600)
    ROUTE_CAPTION(600,"Turn on") // change button caption
  ELSE  // light is off 
    SET(120)  // lights on
    ROUTE_ACTIVE(600)
    ROUTE_CAPTION(600,"Turn off") // change button caption
  ENDIF
DONE

AUTOSTART
  ROUTE_CAPTION(600,"Turn on") // set button caption default at startup
DONE
```

## Two separate routes example

This example has two \"routes\" to control lights, but only one of them
will be visible at a time so we dont need a flag. Each route will have
the default \"Set\" button.

``` cpp
ROUTE(600,"Shed lights on")
  SET(120)
  ROUTE_HIDDEN(600) // hide self
  ROUTE_INACTIVE(601) // reveal off 
DONE

ROUTE(601,"Shed lights off")
  RESET(120)
  ROUTE_HIDDEN(601)
  ROUTE_INACTIVE(600)
DONE

AUTOSTART
  ROUTE_HIDDEN(601)  // shed lights are off already
DONE
```

\|EX-R\| has the full set of route setting and testing commands which
should be self explanitory once the above simple examples have been
understood. Each route can only be in one of the 4 states.

``` cpp
IFROUTE_INACTIVE(route_id)
IFROUTE_ACTIVE(route_id)
IFROUTE_HIDDEN(route_id)
IFROUTE_DISABLED(route_id)

ROUTE_INACTIVE(route_id)
ROUTE_ACTIVE(route_id)
ROUTE_HIDDEN(route_id)
ROUTE_DISABLED(route_id)
```
