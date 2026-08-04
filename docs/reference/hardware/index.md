\|EX-REF-LOGO\|

# Hardware

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

::: 
microcontroller-boards pin-vpin-allocations motor-boards wifi-boards
ethernet-boards bluetooth index-i2c accessory-controllers
:::

\|HR-DASHED\|

## Microcontroller List

::: 
- - Type / Brand \|\_xa\| \|\_xa\| \|\_xa\| \|\_xa\| \|\_xa\|
  - R \|BRxa\| e \|BRxa\| c \|BRxa\| o \|BRxa\| m \|BRxa\| m \|BRxa\| e
    \|BRxa\| n \|BRxa\| d \|BRxa\| e \|BRxa\| d
  - S \|BRxa\| u \|BRxa\| p \|BRxa\| p \|BRxa\| o \|BRxa\| r \|BRxa\| t
    \|BRxa\| e \|BRxa\| d
  - Level
  - S \|BRxa\| h \|BRxa\| i \|BRxa\| e \|BRxa\| l \|BRxa\| d
    \|BRxa\|[^1]
  - HAL \|BRxa\| / \|BRxa\| \|I2Cxa\|
  - E \|BRxa\| E \|BRxa\| P \|BRxa\| R \|BRxa\| O \|BRxa\| M
  - EX- \|BRxa\| RAIL \|BRxa\| Sup- \|BRxa\| port
  - Track \|BRxa\| Man- \|BRxa\| ager \|BRxa\| Sup- \|BRxa\| port
  - D C \|BRxa\| Sup- \|BRxa\| port
  - W \|BRxa\| i \|BRxa\| F \|BRxa\| i
  - Wifi \|BRxa\| \# \|BRxa\| Con- \|BRxa\| nect- \|BRxa\| ions
    \|BRxa\|[^2]
  - Comments / Notes \|\_xa\| \|\_xa\| \|\_xa\| \|\_xa\| \|\_xa\|
    \|\_xa\| \|\_xa\| \|\_xa\| \|\_xa\|
- - EX-CSB1
  - Yes
  - Yes
  - Conductor
  - Mega
  - Yes
  - Yes
  - Yes
  - Yes
  - Yes
  - Yes
  - \~11
  - This is our stable, well supported platform
- - Arduino
    `Mega2560</reference/hardware/microcontrollers/arduino-mega>`
  - Yes
  - Yes
  - Conductor
  - UNO
  - Yes
  - Yes
  - Yes
  - Yes
  - Yes[^3]
  - yes[^4]
  - 4
  - This is our stable, well supported platform
- - `ESP32-WROOM</reference/hardware/microcontrollers/esp32>`
  - Yes
  - Yes
  - Tinkerer
  - UNO
  - Yes[^5]
  - No
  - Yes
  - Yes
  - Yes[^6]
  - Yes
  - \~11
  - Inexpensive and includes both WiFi and Bluetooth connectivity,
    limited in I/O pins. Most require hardware modifications to work.
- - `STM32 Nucleo</reference/hardware/microcontrollers/stm32-nucleo>`
  - Yes
  - Yes
  - Tinkerer
  - UNO
  - Yes
  - No
  - Yes
  - Yes
  - Yes[^7][^8]
  - Yes[^9][^10]
  - 4
  - Lots of memory and 32 bit architecture, still in the convenient Uno
    form factor but with more I/O pins
- - Arduino
    `Uno R3</reference/hardware/microcontrollers/arduino-uno>`[^11]
  - No
  - Yes
  - Tinkerer
  - UNO
  - No
  - Yes
  - Limit- \|BRxa\| ed[^12]
  - No
  - No[^13]
  - No
  - \-
  - Ok for small layouts with no programming, or a dedicated programmer
    with JMRI
- - Arduino Uno R4
  - \-
  - `No`
  - `8` -
  - `Different architecture to the R3. Will never be supported.`
- - Arduino
    `Nano</reference/hardware/microcontrollers/nano>`[^14]
  - No
  - Yes
  - Tinkerer
  - \-
  - No
  - Yes
  - Limit- \|BRxa\| ed[^15]
  - No
  - No[^16]
  - No
  - \-
  - Similar to Uno, but without the convenient Uno footprint
- - Arduino
    `Mega+WiFi</reference/hardware/microcontrollers/wifi-mega>`
  - No[^17]
  - Yes
  - Tinkerer
  - Mega
  - Yes
  - Yes
  - Yes
  - Yes
  - Yes[^18]
  - Yes
  - 4
  - This is our stable, well supported platform, but with WiFi on board,
    but beware quality issues
- - SAMD21
  - No
  - Dep- \|BRxa\| re- \|BRxa\| cat- \|BRxa\| ed \|BRxa\|[^19][^20]
  - Engineer
  - \-
  - Yes
  - No
  - Yes
  - Yes
  - No[^21]
  - Yes[^22]
  - 4
  - Limited support only, will be removed in 6.0.0
- - `Nano Every</reference/hardware/microcontrollers/nano-every>`
  - No
  - Dep- \|BRxa\| re- \|BRxa\| cat- \|BRxa\| ed \|BRxa\|[^23]
  - Engineer
  - \-
  - Yes
  - Yes
  - Yes
  - No
  - No[^24]
  - Yes[^25]
  - 4
  - Limited support only, will be removed in 6.0.0
- - `Teensy</reference/hardware/microcontrollers/teensy>`
  - No
  - Dep- \|BRxa\| re- \|BRxa\| cat- \|BRxa\| ed \|BRxa\|[^26]
  - Engineer
  - \-
  - Yes[^27]
  - Yes
  - Yes
  - No
  - No[^28]
  - Yes[^29]
  - 4
  - Limited support only, will be removed in 6.0.0
:::

\|HR-DASHED\|

## Motor Board List

::: 
- - Type / Brand \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\|
    \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\|
  - R \|BRxb\| e \|BRxb\| c \|BRxb\| o \|BRxb\| m \|BRxb\| m \|BRxb\| e
    \|BRxb\| n \|BRxb\| d \|BRxb\| e \|BRxb\| d
  - S \|BRxb\| u \|BRxb\| p \|BRxb\| p \|BRxb\| o \|BRxb\| r \|BRxb\| t
    \|BRxb\| e \|BRxb\| d
  - Com- \|BRxb\| fort \|BRxb\| Level
  - For- \|BRxb\| mat
  - S \|BRxb\| t \|BRxb\| a \|BRxb\| c \|BRxb\| k \|BRxb\| a \|BRxb\| b
    \|BRxb\| l \|BRxb\| e
  - Short \|BRxb\| Cir- \|BRxb\| cuit \|BRxb\| Pro- \|BRxb\| tect-
    \|BRxb\| ion
  - Cur- \|BRxb\| rent \|BRxb\| Sen- \|BRxb\| se \|BRxb\|[^30]
  - DC \|BRxb\| Sup- \|BRxb\| port
  - No. \|BRxb\| Out- \|BRxb\| puts \|BRxb\| / \|BRxb\| Tra- \|BRxb\|
    cks
  - Max \|BRxb\| Amps \|BRxb\|[^31]
  - Comments / Notes \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\|
    \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\| \|\_xb\|
    \|\_xb\| \|\_xb\| \|\_xb\|
- - `DCC-EX EX-MotorShield8874 RevA</reference/hardware/motorboards/ex-motor-shield-8874>`
  - Yes
  - Yes
  - Conductor
  - UNO / Mega
  - Yes[^32]
  - Yes
  - Yes
  - Yes
  - 2
  - 5
  - 
- - `Arduino Motor Shield R3</reference/hardware/motorboards/arduino-motor-shield>`[^33]
  - Yes
  - Yes
  - Conductor
  - UNO / Mega
  - Yes[^34]
  - Yes
  - Yes
  - Yes
  - 2
  - 1.3 - 1.5
  - 
- - `Deek-Robot Motor Shield</reference/hardware/motorboards/deek-robot-motor-shield>`[^35]
  - Yes
  - Yes
  - Conductor
  - UNO / Mega
  - Yes[^36]
  - Yes
  - Yes
  - Yes
  - 2
  - 1.3 - 1.5
  - 
- - `Flashtree Motor Shield</reference/hardware/motorboards/flashtree-motor-shield>`
  - No
  - Yes
  - Tinkerer
  - UNO / Mega
  - No
  - Yes
  - Yes
  - Yes
  - 2
  - 1.3 - 1.5
  - 
- - `DIY More L298NH</reference/hardware/motorboards/diy-more-l298nh-motor-shield>`
  - No
  - Yes
  - Tinkerer
  - UNO / Mega
  - No
  - Yes
  - Yes
  - Yes
  - 2
  - 2
  - 
- - `YFRobot L298P</reference/hardware/motorboards/yfrobot-l298p>`
  - No
  - Yes
  - Tinkerer
  - UNO / Mega
  - No
  - No
  - No
  - No
  - 2
  - 2
  - 
- - `L298N (dual)</reference/hardware/motorboards/L298N-motor-board-setup>`
  - No
  - Yes
  - Engineer
  - 
  - No
  - No
  - No
  - No
  - 2
  - 2
  - It doesn\'t have current sense
- - `Dual Module H-bridge MOSFET IRF3205</reference/hardware/motorboards/IRF3205-motor-board-setup>`
  - No
  - Yes
  - Tinkerer
  - 
  - No
  - No
  - No
  - No
  - 2
  - 15
  - 
- - `Pololu MC33926</reference/hardware/motorboards/pololu-mc33926>`
  - No
  - Yes
  - Tinkerer
  - UNO / Mega
  - No
  - No
  - No
  - No
  - 2
  - 3
  - current sense is not acceptable. We recommend using an external
    current sense board like the MAX471
- - `MiniIBT L6201P (single)</reference/hardware/motorboards/miniibt-motor-driver-l6201p>`
  - No
  - Yes
  - Tinkerer
  - 
  - No
  - No
  - ?
  - No
  - 1
  - 5
  - 
- - `BTS7960 IBT_2 (single)</reference/hardware/motorboards/IBT_2-motor-board-setup>`
  - No
  - Yes
  - Tinkerer
  - 
  - No
  - No
  - ?
  - No
  - 1
  - 43
  - 
- - `Keyes/Fundumoto ("Beeper Board")</reference/hardware/motorboards/keyes-fundumoto>`
  - No
  - Yes
  - Engineer
  - UNO / Mega
  - No
  - Yes[^37]
  - Yes[^38]
  - No
  - 2
  - 2
  - 
- - `Makerfabs H-Bridge</reference/hardware/motorboards/makerfabs-h-bridge-motor-shield>`
  - No
  - Yes
  - Engineer
  - 
  - No
  - No
  - No
  - No
  - 2
  - 8
  - 
- - `Velleman KA03/VMA03</reference/hardware/motorboards/velleman-ka03-kit-vma03>`
  - No
  - Yes
  - Engineer
  - 
  - No
  - No
  - No
  - No
  - 2
  - 2
  - 
- - `DFRobot 2x2A DC Motor Shield (DRI0009)</reference/hardware/motorboards/dfrobot-2x2a-dc-motor-shield>`
  - No
  - Yes
  - Engineer
  - UNO / Mega
  - No
  - No
  - No
  - No
  - 2
  - 2
  - 
- - VNH2SP30 - SparkFun Monster Moto and others
  - \-
  - `No`
  - `7` -
  - Does not work. It can\'t switch fast enough to generate a reliable
    DCC signal
- - IFX9202ED - Infineon Dual H-Bridge
  - \-
  - `No`
  - `7` -
  - Does not work. Can\'t switch fast enough.
- - DFRobot Romeo V2
  - \-
  - `No`
  - Engineer
  - `6` -
  - Well, an Engineer could perhaps get this one to work.
- - Kuman Board (and any L293D based boards)
  - \-
  - `No`
  - `7` -
  - Does not work. Not enough current.
- - Pololu TB9051FTG based motor shield
  - \-
  - `No`
  - `7` -
  - Does not work. It can\'t switch fast enough to generate a reliable
    DCC signal
:::

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

::: 
index-decoder wire-gauge power-supplies
:::

[^1]: If the board supports stackable shields. UNO, Mega = Supports both
    Uno/Mega shields, - = no shield format

[^2]: Number of *direct* WiFi connections. If connected via JMRI, more
    are are supported

[^3]: Requires a supported motor driver that supports
    `TrackManager <trackmanager/index:trackmanager technical details and detailed instructions>`

[^4]: Requires an additional
    `Ethernet <reference/hardware/ethernet-boards:ethernet boards>` or
    `WiFi <reference/hardware/wifi-boards:wifi boards>` shield

[^5]: HAL/[\|I2Cxa\|](##SUBST##|I2Cxa|) connectivity is only available
    via the blocking Arduino Wire library at present

[^6]: Requires a supported motor driver that supports
    `TrackManager <trackmanager/index:trackmanager technical details and detailed instructions>`

[^7]: Requires a supported motor driver that supports
    `TrackManager <trackmanager/index:trackmanager technical details and detailed instructions>`

[^8]: Features and support in Beta testing can and will change
    regularly, be sure to keep up to date with developments on our
    [Discord server](https://discord.gg/y2sB4Fp)

[^9]: Requires an additional
    `Ethernet <reference/hardware/ethernet-boards:ethernet boards>` or
    `WiFi <reference/hardware/wifi-boards:wifi boards>` shield

[^10]: Features and support in Beta testing can and will change
    regularly, be sure to keep up to date with developments on our
    [Discord server](https://discord.gg/y2sB4Fp)

[^11]: Requires the use of JMRI.

[^12]: Limited EXRAIL scripts are possible only when disabling EEPROM
    and programming

[^13]: Requires a supported motor driver that supports
    `TrackManager <trackmanager/index:trackmanager technical details and detailed instructions>`

[^14]: Requires the use of JMRI.

[^15]: Limited EXRAIL scripts are possible only when disabling EEPROM
    and programming

[^16]: Requires a supported motor driver that supports
    `TrackManager <trackmanager/index:trackmanager technical details and detailed instructions>`

[^17]: While the Mega+WiFi boards seem like a good option and are based
    on our well-known, stable Mega2560 platform, there are many reports
    of quality issues with these, so buyer beware, and use of these is
    not recommended

[^18]: Requires a supported motor driver that supports
    `TrackManager <trackmanager/index:trackmanager technical details and detailed instructions>`

[^19]: The core development team no longer have access to these, and
    testing is limited to ensuring the software compiles for the board
    type

[^20]: The core Arduino library has a bug affecting serial console
    output which can be patched but renders the device unsuited for
    future development until fixed in the main Arduino core library for
    SAMD21

[^21]: Requires a supported motor driver that supports
    `TrackManager <trackmanager/index:trackmanager technical details and detailed instructions>`

[^22]: Requires an additional
    `Ethernet <reference/hardware/ethernet-boards:ethernet boards>` or
    `WiFi <reference/hardware/wifi-boards:wifi boards>` shield

[^23]: The core development team no longer have access to these, and
    testing is limited to ensuring the software compiles for the board
    type

[^24]: Requires a supported motor driver that supports
    `TrackManager <trackmanager/index:trackmanager technical details and detailed instructions>`

[^25]: Requires an additional
    `Ethernet <reference/hardware/ethernet-boards:ethernet boards>` or
    `WiFi <reference/hardware/wifi-boards:wifi boards>` shield

[^26]: The core development team no longer have access to these, and
    testing is limited to ensuring the software compiles for the board
    type

[^27]: HAL/[\|I2Cxa\|](##SUBST##|I2Cxa|) connectivity is only available
    via the blocking Arduino Wire library at present

[^28]: Requires a supported motor driver that supports
    `TrackManager <trackmanager/index:trackmanager technical details and detailed instructions>`

[^29]: Requires an additional
    `Ethernet <reference/hardware/ethernet-boards:ethernet boards>` or
    `WiFi <reference/hardware/wifi-boards:wifi boards>` shield

[^30]: CV Programming

[^31]: Per output

[^32]: Requires modification of the board to stack the second board

[^33]: The *Arduino Motor Shield R38* and the *Deek-Robot Motor Shield*
    are interchangeably referred to in this documentation as the
    *standard motor driver*

[^34]: Can be stacked, but it is complicated. See
    `/reference/hardware/motorboards/arduino-motor-shield-stacked`

[^35]: The *Arduino Motor Shield R38* and the *Deek-Robot Motor Shield*
    are interchangeably referred to in this documentation as the
    *standard motor driver*

[^36]: Can be stacked, but it is complicated. See
    `/reference/hardware/motorboards/arduino-motor-shield-stacked`

[^37]: Requires modification of the board to support Current Sense

[^38]: Requires modification of the board to support Current Sense
