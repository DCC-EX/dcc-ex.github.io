\|EX-TT-LOGO\|

# EX-Turntable \|BR\| FAQ and Troubleshooting

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|
\|githublink-ex-turntable-button-small\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="1" local=""}
On this page
:::
::::

## Frequently Asked Questions

This is a list of common questions that we answer by our various support
channels:

  Question   Answer
  ---------- --------
             

## Troubleshooting tips

In this section, you will find some tips on troubleshooting the various
issues encountered with \|EX-TT\|.

### Homing failure

+----------------------------------+----------------------------------+
| Symptoms                         | Common Causes                    |
+==================================+==================================+
| | Turntable rotates on start up  | | The magnet in the turntable is |
|   and ends in a random position  |   too far away from the sensor   |
| | Serial console reports         | | Hall effect sensor is          |
|   \"ERROR: Turntable failed to   |   connected incorrectly          |
|   home, setting random home      |                                  |
|   position\"                     |                                  |
+----------------------------------+----------------------------------+

### Calibration failure

+----------------------------------+----------------------------------+
| Symptoms                         | Common Causes                    |
+==================================+==================================+
| | Turntable rotates on start up  | | The magnet in the turntable is |
|   and ends in a random position  |   too far away from the sensor   |
| | Serial console reports         | | Hall effect sensor is          |
|   \"ERROR: Turntable failed to   |   connected incorrectly          |
|   home, setting random home      |                                  |
|   position\"                     |                                  |
| | Serial console reports         |                                  |
|   \"CALIBRATION: FAILED, could   |                                  |
|   not home, could not determine  |                                  |
|   step count\"                   |                                  |
+----------------------------------+----------------------------------+

### Turntable judders, stalls, or fails to rotate

+----------------------------------+----------------------------------+
| Symptoms                         | Common Causes                    |
+==================================+==================================+
| When attempting to rotate, the   | | An incorrect stepper driver    |
| turntable judders or shakes      |   has been configured            |
|                                  | | Stepper motor or driver is not |
|                                  |   connected correctly, ensure    |
|                                  |   all wiring is securely         |
|                                  |   connected                      |
|                                  | | Something is physically        |
|                                  |   interfering with the turntable |
|                                  |   or stepper operation, check    |
|                                  |   for interference               |
+----------------------------------+----------------------------------+
| The turntable does not rotate at | | An incorrect stepper driver    |
| all                              |   has been configured            |
|                                  | | Something is physically        |
|                                  |   interfering with the turntable |
|                                  |   or stepper operation, check    |
|                                  |   for interference               |
+----------------------------------+----------------------------------+

### Track power is cut when locomotive enters turntable bridge track

+----------------------------------+----------------------------------+
| Symptoms                         | Common Causes                    |
+==================================+==================================+
| The CommandStation detects a     | | The DCC phase is out of sync   |
| current overload and turns track |   between the layout and bridge  |
| power off                        |   track, phase inversion flag is |
|                                  |   required for the position      |
|                                  | | Tracks opposite each other     |
|                                  |   around the turntable are wired |
|                                  |   with inverted phases, wiring   |
|                                  |   must be adjusted               |
+----------------------------------+----------------------------------+

### EX-CommandStation compile errors with device driver enabled

  Symptoms                                                                                      Common Causes
  --------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  EX-CommandStation software fails to compile with \"#include IO_TurntableEX.h\" in myHal.cpp   The version of EX-CommandStation is incorrect, you need the \"add-turntable-controller\" branch of [EX-CommandStation](https://github.com/DCC-EX/CommandStation-EX/tree/add-turntable-controller)

### EX-Turntable showing as offline with \<D HAL SHOW\>

+----------------------------------+-----------------------------------------------------------------------------------------------+
| Symptoms                         | Common Causes                                                                                 |
+==================================+===============================================================================================+
| | \<D HAL SHOW\> reports         | | EX-Turntable is not powered on, or was powered on after the CommandStation                  |
|   EX-Turntable as OFFLINE        | | The \|I2C\| interfaces are not connected correctly, refer to                                |
| | EX-Turntable does not respond  |   `ex-turntable/assembly:9. connect ex-turntable to your ex-commandstation`{.interpreted-text |
|   to EXRAIL or diagnostic        |   role="ref"}                                                                                 |
|   commands                       | | The \|I2C\| address in EX-Turntable\'s config.h does not match the address in the           |
|                                  |   CommandStation\'s myHal.cpp file                                                            |
+----------------------------------+-----------------------------------------------------------------------------------------------+
