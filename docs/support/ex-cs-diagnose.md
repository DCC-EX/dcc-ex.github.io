::: {.meta keywords="EX-CommandStation Command Station diagnosing Issues Troubleshooting"}
:::

\|EX-CS-LOGO\|

# Diagnosing Basic Problems

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="2" local=""}
On this page
:::
::::

This page is intended to help you diagnose and fix some of the most
common problems with the \|EX-CS\|. If you have a more specific issue
see the `ex-cs-troubleshooting`{.interpreted-text role="doc"} page.

Depending on how you have your EX-CommandStation configured, the steps
to diagnose problems are different:

- [When Connected to a PC via USB](#when-connected-to-a-pc-via-usb)
- [When Configured as an Access
  Point](#when-configured-as-an-access-point)
- [When Configured in Station mode](#when-configured-in-station-mode)

------------------------------------------------------------------------

## EX-CommandStation Software fails to load

::: todo
[MEDIUM -
Diagnosing](https://github.com/DCC-EX/dcc-ex.github.io/issues/433) -
EX-CommandStation Software fails to load
:::

Either using the \|EX-I\| or the \|Arduino IDE\|.

+---------------------------+-------------+---------------------------------------------------------------+
| Question                  | If Yes      | If No - Possible reasons                                      |
+===========================+=============+===============================================================+
| \"Failed to upload        | Go to       | (a) Have you selected the correct COM port? \|BR\| See        |
| because uploading         | Question 2. |     `ex-installer/installing:getting ready`{.interpreted-text |
| error:\"                  |             |     role="ref"} for information on finding the correct COM    |
|                           |             |     port.                                                     |
|                           |             | (b) Have you selected the correct Arduino board type?         |
+---------------------------+-------------+---------------------------------------------------------------+
| 2.  (\|Arduino IDE\|      | Go to       | ToDo                                                          |
|     only) \|BR\| Have you | Question 3. |                                                               |
|     selected the correct  |             |                                                               |
|     Baud rate?            |             |                                                               |
+---------------------------+-------------+---------------------------------------------------------------+
| 3.  Do you receive a      | Go to       | (a) Your PC may not have an internet connection.              |
|     message starts with   | Question 4. | (b) Your PC\'s firewall software may be stopping the          |
|     \"Failed to           |             |     installer from accessing the internet. Temporarily        |
|     download\...\"        |             |     disable the firewall, or create an exception for          |
|                           |             |     EX-Installer. \|BR\| \|BR\| An internet connection is     |
|                           |             |     required to download some files.                          |
+---------------------------+-------------+---------------------------------------------------------------+
| 4.  ToDo?                 | ToDo.       | ToDo                                                          |
+---------------------------+-------------+---------------------------------------------------------------+

::: todo
LOW - Finish this
:::

------------------------------------------------------------------------

## When Connected to a PC via USB

**If you have connected your EX-CommandStation to a PC via USB**
(including for using \|JMRI\|).

### Initial Check

As an initial check we recommend you should try to connect to your
EX-CommandStation using \|EX-WT\|, even if you plan to use it via
\|JMRI\| or a WiFi throttle.

+---------------------------+------------------+---------------------------+
| Question                  | If Yes           | If No - Possible reasons  |
+===========================+==================+===========================+
| 1.  Is the LED on the     | Go to Question   | (a) EX-CommandStation not |
|     Arduino board on?     | 2.               |     connected to PC via   |
|                           |                  |     USB.                  |
|                           |                  | (b) CommandStation        |
|                           |                  |     software may not have |
|                           |                  |     loaded correctly.     |
|                           |                  | (c) Possible dead Arduino |
|                           |                  |     board.                |
|                           |                  |                           |
|                           |                  | \|BR\| For (b) or (c),    |
|                           |                  | try loading the           |
|                           |                  | EX-CommandStation         |
|                           |                  | software again.           |
+---------------------------+------------------+---------------------------+
| 2.  Can you connect to it | Go to Question   | (a) EX-CommandStation not |
|     using EX-WebThrottle? | 3.               |     connected to your     |
|                           |                  |     **PC** via USB.       |
|                           |                  | (b) Software may not have |
|                           |                  |     loaded correctly.     |
|                           |                  |                           |
|                           |                  | \|BR\| Try loading the    |
|                           |                  | EX-CommandStation         |
|                           |                  | software again.           |
+---------------------------+------------------+---------------------------+
| 3.  When you click the    | Go to Question   | (a) Have you plugged in   |
|     power on slider, it   | 4.               |     and turned on a       |
|     should say power on.  |                  |     12-16v DC power       |
|     \|BR\| Do the 4 LEDs  |                  |     supply[^1] into the   |
|     on the motor board    |                  |     motor board           |
|     turn on and stay on?  |                  | (b) Have you made sure    |
|                           |                  |     the polarity of the   |
|                           |                  |     power supply is       |
|                           |                  |     correct.              |
|                           |                  |                           |
|                           |                  | \|br\| Do the 4 LEDs on   |
|                           |                  | the motor board turn on   |
|                           |                  | briefly, then turn off?   |
|                           |                  |                           |
|                           |                  | (c) there is a short      |
|                           |                  |     circuit on the track. |
|                           |                  | (d) there is a short      |
|                           |                  |     circuit in the loco.  |
+---------------------------+------------------+---------------------------+
| 5.  When you select a     | Congratulations, | (a) Wrong loco DCC        |
|     loco and move the     | your \|EX-CS\|   |     Address selected.     |
|     throttle, does the    | is essentially   | (b) loco is not DCC       |
|     loco move?            | working.         |     decoder equipped.     |
|                           |                  |     (You will likely hear |
|                           |                  |     a humming coming from |
|                           |                  |     the loco. If you do   |
|                           |                  |     remove it from the    |
|                           |                  |     track urgently, the   |
|                           |                  |     loco may be being     |
|                           |                  |     damaged.)             |
+---------------------------+------------------+---------------------------+

\|HR-DASHED\|

| 

### Using JMRI

::: todo
[MEDIUM -
Diagnosing](https://github.com/DCC-EX/dcc-ex.github.io/issues/433) -
Using JMRI
:::

+---------------------------+------------------+---------------------------------------------------------------------------------+
| Question                  | If Yes           | If No - Possible reasons                                                        |
+===========================+==================+=================================================================================+
| 1.  Have you selected     | Go to Question   | (a) Select \'DCC++\' as the System Manufacturer and \'DCC++ Serial Port\' as    |
|     \'DCC++\' as the      | 2.               |     the System connection in the preferences.                                   |
|     System Manufacturer   |                  |                                                                                 |
|     and \'DCC++ Serial    |                  |                                                                                 |
|     Port\' as the System  |                  |                                                                                 |
|     connection in the     |                  |                                                                                 |
|     preferences?          |                  |                                                                                 |
+---------------------------+------------------+---------------------------------------------------------------------------------+
| 2.  Have you selected the | Go to Question   | (a) Check which com port the EX-CommandStation is connected to. \|BR\| See      |
|     correct COM port?     | 3.               |     `ex-commandstation/installer-diy:1. getting ready`{.interpreted-text        |
|                           |                  |     role="ref"} for details on how to determine the correct com port.           |
+---------------------------+------------------+---------------------------------------------------------------------------------+
| 3.  Can you turn the      | Go to Question   | (a) Have you plugged in and turned on a 12-16v DC power supply[^2] into the     |
|     track power on?       | 4.               |     motor board                                                                 |
|     \|BR\| Do the LEDs on |                  | (b) Have you made sure the polarity of the power supply is correct.             |
|     the \|motor shield\|  |                  |                                                                                 |
|     turn on?              |                  |                                                                                 |
+---------------------------+------------------+---------------------------------------------------------------------------------+
| 4.  When you open a       | Congratulations, | (a) Have you connected the track to the \'MAIN\' outputs of the Motor Board.    |
|     throttle window in    | your \|EX-CS\|   |     \|BR\| \|JMRI\| cannot directly control trains on the \'PROGRAMMING\'       |
|     \|JMRI\|, select a    | is essentially   |     outputs without using additional commands. See                              |
|     loco and move the     | working.         |     `support/ex-cs-troubleshooting:cannot drive a locomotive`{.interpreted-text |
|     throttle, does the    |                  |     role="ref"} for more information.                                           |
|     loco move?            |                  | (b) Wrong loco DCC Address selected.                                            |
|                           |                  | (c) loco is not DCC decoder equipped. (You will likely hear a humming coming    |
|                           |                  |     from the loco. If you do remove it from the track urgently, the loco is     |
|                           |                  |     being damaged.)                                                             |
+---------------------------+------------------+---------------------------------------------------------------------------------+

\|HR-DASHED\|

| 

## When Configured as an Access Point

**If you have configured your EX-CommandStation as an Access Point**
(separate network)

+------------------------------------+----------------------------------------------+-----------------------------------------+
| Question                           | If Yes                                       | If No - Possible reasons                |
+====================================+==============================================+=========================================+
| 1.  Is the LED on the Arduino      | Go to Question 2.                            | (a) You have not connected a 7-9v DC    |
|     board on?                      |                                              |     power supply to Arduino Board.      |
|                                    |                                              |     \|BR\| *or* \|BR\|                  |
|                                    |                                              | (b) You have not connected a USB cable  |
|                                    |                                              |     connected to a power supply, to     |
|                                    |                                              |     Arduino Board.                      |
|                                    |                                              | (c) Software may not have loaded        |
|                                    |                                              |     correctly.                          |
|                                    |                                              | (d) Possible dead Arduino board.        |
|                                    |                                              |                                         |
|                                    |                                              | For c & d, try loading the              |
|                                    |                                              | EX-CommandStation software again.       |
+------------------------------------+----------------------------------------------+-----------------------------------------+
| 2.  Can your phone see the WiFi    | Go to Question 3                             | (a) WiFi shield is connected            |
|     network of the                 |                                              |     incorrectly to the CommandStation - |
|     EX-CommandStation in the       |                                              |     The Rx pin of the WiFi shield must  |
|     phone\'s available network     |                                              |     connect to the Tx pin on the        |
|     list?                          |                                              |     CommandStation, and Tx to the Rx    |
|                                    |                                              |     pin                                 |
|                                    |                                              | (b) ToDo                                |
+------------------------------------+----------------------------------------------+-----------------------------------------+
| 3.  The WiFi network name appears  | See                                          | Go to Question 4                        |
|     as                             | `/support/wifi-at-version`{.interpreted-text |                                         |
|     \"DCCEX-SAYS-BROKEN-FIRMWARE\" | role="doc"} for details.                     |                                         |
|     or \"UPDATE_ESP_FIRMWARE\"     |                                              |                                         |
+------------------------------------+----------------------------------------------+-----------------------------------------+
| 4.  Can your phone connect the     | Go to Question 5                             | (a) ToDo                                |
|     WiFi network of the            |                                              | (b) ToDo                                |
|     EX-CommandStation              |                                              |                                         |
+------------------------------------+----------------------------------------------+-----------------------------------------+
| 5.  Can your throttle app connect  | Go to Question 6                             | (a) ToDo                                |
|     the WiThrottle server of the   |                                              | (b) ToDo                                |
|     EX-CommandStation \|BR\|       |                                              |                                         |
|     \|BR\| \|Engine Driver\|       |                                              |                                         |
|     should show you the WiThrottle |                                              |                                         |
|     server in the discovered       |                                              |                                         |
|     servers list \|BR\| For        |                                              |                                         |
|     \|WiThrottle\| you will need   |                                              |                                         |
|     to type in the IP address and  |                                              |                                         |
|     Port                           |                                              |                                         |
+------------------------------------+----------------------------------------------+-----------------------------------------+
| 6.  Can you turn the track power   | Go to Question 7.                            | (a) Have you plugged in and turned on a |
|     on? \|BR\| Do the LEDs on the  |                                              |     12-16v DC power supply[^3] into the |
|     \|motor shield\| turn on?      |                                              |     motor board                         |
|                                    |                                              | (b) Have you made sure the polarity of  |
|                                    |                                              |     the power supply is correct.        |
+------------------------------------+----------------------------------------------+-----------------------------------------+
| 7.  When select a loco in the      | Congratulations, your \|EX-CS\| is           | (a) Have you connected the track to the |
|     throttle app and move the      | essentially working.                         |     \'MAIN\' outputs of the Motor       |
|     throttle, does the loco move?  |                                              |     Board. \|BR\| You cannot directly   |
|                                    |                                              |     control trains on the               |
|                                    |                                              |     \'PROGRAMMING\' outputs without     |
|                                    |                                              |     using additional commands which can |
|                                    |                                              |     be done in \|Engine Driver\| but    |
|                                    |                                              |     not other WiFi throttle apps (Use   |
|                                    |                                              |     the                                 |
|                                    |                                              |     `Request Loco ID`{.interpreted-text |
|                                    |                                              |     role="guilabel"} button in \|Engine |
|                                    |                                              |     Driver\|.) \|BR\| recommend that    |
|                                    |                                              |     the MAIN outputs be used to run a   |
|                                    |                                              |     layout.                             |
|                                    |                                              | (b) Wrong loco DCC Address selected.    |
|                                    |                                              | (c) loco is not DCC decoder equipped.   |
|                                    |                                              |     (You will likely hear a humming     |
|                                    |                                              |     coming from the loco. If you do     |
|                                    |                                              |     remove it from the track urgently,  |
|                                    |                                              |     the loco is being damaged.)         |
+------------------------------------+----------------------------------------------+-----------------------------------------+

\|HR-DASHED\|

| 

## When Configured in Station mode

**If you have configured your EX-CommandStation in Station mode
(connected to your home WiFi network)**

+---------------------------+------------------+-----------------------------------------+
| Question                  | If Yes           | If No - Possible reasons                |
+===========================+==================+=========================================+
| 1.  Is the LED on the     | Go to Question   | (a) You have not connected a 7-9v DC    |
|     Arduino board on?     | 2.               |     power supply to Arduino Board       |
|                           |                  | (b) You have not connected a USB cable  |
|                           |                  |     connected to a power supply, to     |
|                           |                  |     Arduino Board                       |
|                           |                  | (c) Software may not have loaded        |
|                           |                  |     correctly.                          |
|                           |                  | (d) Possible dead Arduino board.        |
|                           |                  |                                         |
|                           |                  | For c & d, try loading the              |
|                           |                  | EX-CommandStation software again.       |
+---------------------------+------------------+-----------------------------------------+
| 2.  Can your throttle app | Go to Question   | (a) You may be on a different network   |
|     connect to the        | 3.               |     to the EX-CommandStation (e.g.      |
|     WiThrottle server of  |                  |     2.5gHz VS 5gHz connection to you    |
|     the EX-CommandStation |                  |     home router.) Try entering the IP   |
|     \|BR\| \|BR\|         |                  |     address and Port manually. To       |
|     \|Engine Driver\|     |                  |                                         |
|     should show you the   |                  |                                         |
|     WiThrottle server in  |                  |                                         |
|     the discovered        |                  |                                         |
|     servers list \|BR\|   |                  |                                         |
|     For \|WiThrottle\| It |                  |                                         |
|     should connect        |                  |                                         |
|     automatically.        |                  |                                         |
+---------------------------+------------------+-----------------------------------------+
| 3.  When select a loco in | Congratulations, | (a) Have you connected the track to the |
|     the throttle app and  | your \|EX-CS\|   |     \'MAIN\' outputs of the Motor       |
|     move the throttle,    | is essentially   |     Board. \|BR\| You cannot directly   |
|     does the loco move?   | working.         |     control trains on the               |
|                           |                  |     \'PROGRAMMING\' outputs without     |
|                           |                  |     using additional commands which can |
|                           |                  |     be done in \|Engine Driver\| but    |
|                           |                  |     not other WiFi throttle apps (Use   |
|                           |                  |     the                                 |
|                           |                  |     `Request Loco ID`{.interpreted-text |
|                           |                  |     role="guilabel"} button in \|Engine |
|                           |                  |     Driver\|.) \|BR\| recommend that    |
|                           |                  |     the MAIN outputs be used to run a   |
|                           |                  |     layout.                             |
|                           |                  | (b) Wrong loco DCC Address selected.    |
|                           |                  | (c) loco is not DCC decoder equipped.   |
|                           |                  |     (You will likely hear a humming     |
|                           |                  |     coming from the loco. If you do     |
|                           |                  |     remove it from the track urgently,  |
|                           |                  |     the loco is being damaged.)         |
+---------------------------+------------------+-----------------------------------------+

[^1]: The voltage you need for the [\|Motor
    Driver\|](##SUBST##|Motor Driver|) depends on the scale/gauge of the
    layout you are using. Bigger is not always better. Too high a
    voltage can damage your locos. See the
    `reference/hardware/power-supplies:powering the motor driver`{.interpreted-text
    role="ref"} for more information.

[^2]: The voltage you need for the [\|Motor
    Driver\|](##SUBST##|Motor Driver|) depends on the scale/gauge of the
    layout you are using. Bigger is not always better. Too high a
    voltage can damage your locos. See the
    `reference/hardware/power-supplies:powering the motor driver`{.interpreted-text
    role="ref"} for more information.

[^3]: The voltage you need for the [\|Motor
    Driver\|](##SUBST##|Motor Driver|) depends on the scale/gauge of the
    layout you are using. Bigger is not always better. Too high a
    voltage can damage your locos. See the
    `reference/hardware/power-supplies:powering the motor driver`{.interpreted-text
    role="ref"} for more information.
