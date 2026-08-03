# EX-IOExpander \|BR\| FAQ and Troubleshooting

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|
\|githublink-ex-ioexpander-button-small\|

:::: 

::: 
On this page
:::
::::

## Frequently Asked Questions

This is a list of common questions that we answer by our various support
channels:

  Question                                            Answer
  --------------------------------------------------- --------------------------------------------------------------------------------------------------------------------
  What microcontrollers can be used with \|EX-IO\|?   At present, Arduino Nano, Uno, and Mega2560 (see `/ex-ioexpander/supported-devices`)

## Troubleshooting tips

In this section, you will find some tips on troubleshooting the various
issues encountered with \|EX-IO\|.

### EX-IOExpander device offline

+----------------------------------+-------------------------------------------------------------------------------+
| Symptoms                         | Common Causes                                                                 |
+==================================+===============================================================================+
| | I/O activities are not working | | \|I2C\| connectivity issue between \|EX-CS\| and \|EX-IO\| - ensure SDA     |
| | Diagnostic command             |   connects to SDA, SCL to SCL, and ground is connected                        |
|   `<D HAL SHOW>` reports device  | | \|EX-CS\| turned on before \|EX-IO\| - ensure \|EX-IO\| is turned on before |
|   as offline                     |   \|EX-CS\|                                                                   |
|                                  | | Incorrect \|I2C\| address defined - ensure the \|I2C\| address is correct   |
|                                  |   in myHal.cpp on \|EX-CS\| and myConfig.h on \|EX-IO\|                       |
|                                  | | Incorrect number of digital/analogue pins defined - ensure the pins defined |
|                                  |   in myHal.cpp are valid according to                                         |
|                                  |   `/ex-ioexpander/supported-devices`            |
|                                  | | \|I2C\| clock speed issue, define slower clock speed in myHal.cpp:          |
|                                  |   `reference/hardware/i2c-devices:changing the clock speed`                                                                 |
+----------------------------------+-------------------------------------------------------------------------------+
| Digital pin 13 is always low in  | On non-genuine Uno devices (possibly Nano also), the onboard LED can cause    |
| input mode                       | this behaviour when pullups are enabled, with a suggested workaround of       |
|                                  | adding an external 1K pullup resistor                                         |
+----------------------------------+-------------------------------------------------------------------------------+
