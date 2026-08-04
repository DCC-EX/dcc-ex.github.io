\|EX-R-LOGO\|

# AUTOMATIONS

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

An [AUTOMATION ](/exrail/getting-started.md)
is a sequence of \|EX-R\| commands used to drive a loco.

By creating an AUTOMATION in \|EX-R\|, your throttle/controller app will
show the automation on its **Routes** display. To send a loco along an
AUTOMATION, you must first drive the loco to a point where the
automation can start and then select the automation from the Routes
screen of your throttle.

The AUTOMATION will take over driving the loco but you will still see
the throttle moving if the loco changes speed. If you manually alter the
speed with the throttle that will take effect normally as the automation
spends most of its time in an AT command waiting for the train to reach
a sensor, and will not wake up again until the sensor is detected. You
may, for example, stop the train manually to fix a derailment, dropped
rolling stock or cat sitting on the track. When you restart the loco and
drive it to the sensor the automation is expecting, the automation will
carry on.

Of particular interest, compared with a PC (JMRI, iTrain, RocRail etc)
running the loco, \|EX-R\| is only interested in the sensor your task is
trying to reach. This makes it vastly more efficient than even the
fastest PC system.
