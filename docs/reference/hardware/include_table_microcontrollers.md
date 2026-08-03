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
