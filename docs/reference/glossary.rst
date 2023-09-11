.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-reference.rst
|EX-REF-LOGO|

********
Glossary
********

|conductor| |tinkerer| |engineer|

.. list-table::
    :widths: 25 75
    :width: 900px
    :header-rows: 1
    :class: table-wrap-text

    * - Term
      - Meaning
    * - Access Point (AP) Mode
      - In Access Point (AP) mode, the tiny ESP-WiFi chip acts as a very basic WiFi server and provides a small IP network for your throttle or for your computer running JMRI with the wiThrottle Server enabled. It acts much like your router does to let things connect directly to it (currently up to four connections). |BR| Using the Command Station in AP mode allows you to have a separate network so you can keep your layout network separate from your home network. |BR| :doc:`Refer here for more information. </ex-commandstation/advanced-setup/supported-wifi/wifi-config>`
    * - Arduino IDE
      - A free app running on your PC, specifically designed to install software onto Arduino microprocessors. |BR| https://www.arduino.cc/en/software
    * - BaseStation-Classic |BR| DCC++ (Original)
      - The original inexpensive Command Station based on the Arduino platform by Gregg Berman. :dcc-ex-red-bold-italic:`This is no longer maintained or supported by the DCC-EX Team`. |BR| |EX-CS| is a completely new build which maintains backward compatibility with the original DCC++. |BR| See :doc:`DCC++ VS DCC-EX? <../../news/posts/20201001>` for more information
    * - Command Station |BR| DCC Command Station |BR| DCC Base Station
      - See https://dccwiki.com/Command_Station
    * - Consist |BR| Multiple Unit
      - Multiple locos hauling a singe train. see https://dccwiki.com/Multiple_Unit_Consisting
    * - Cab
      - A Cab can refer to a throttle (or controller) as well as a loco or locomotive |BR| In the context of DCC-EX commands, `cab` refers to a loco
    * - DC
      - Direct Current
    * - DCC
      - Digital Command Control.  NMRA Specification for controlling trains. |BR| See https://dccwiki.com/NMRA/NMRA_Standards
    * - Engine Driver |BR| Engine Driver Throttle
      - Android app for controlling DCC locos using the wiThrottle Protocol |BR| See :doc:`/throttles/software/engine-driver`
    * - DCC++ Commands |BR| <DCC++> |BR| DCC++ Protocol |BR| DCC++ API
      - Old name for the DCC-EX Native Commands / DCC-EX Native Protocol. |BR| Some references to this still remain for backward compatibility. i.e. JMRI still refers to DCC++.
    * - DCC-EX Native Commands |BR| DCC-EX Native Protocol |BR| DCC-EX Native API
      - New name for the DCC++ Commands/Protocol/API. |BR| Refer to :doc:`/reference/software/command-summary-consolidated` for details.
    * - JMRI
      - `Java Model Railroad Interface <https://www.jmri.org/>`_
    * - Motor Driver 
      - Same as "Motor Shield" "Motor Board" "Motorboard" |BR| See :doc:`/reference/hardware/motor-boards`
    * - Station (STA) Mode
      - Station Mode allows you to connect the Command Station to your existing home network. |BR| The Command Station becomes a Station or Client rather than an Access Point. |BR| That means instead of being a host that manages the IP of the smartphone that runs your Throttle, it becomes a station that connects to your existing network just like any of the other computers or devices connected to your network. The Throttle then connects to the Command Station by finding its IP address on the network. |BR| :doc:`Refer here for more information. </ex-commandstation/advanced-setup/supported-wifi/wifi-config>`
    * - Switching |BR| Shunting
      - The process of moving individual carriages to/from specific locations on yards or sidings.
    * - Turnouts |BR| Points
      - A mechanical device to guide a train from one track to another
    * - USB
      - Universal Serial Bus
    * - Visual Studio Code (VSC)
      - A free app running on your PC that, among other capabilities, can install software onto Arduino microprocessors |BR| https://code.visualstudio.com/
    * - WiThrottle
      - \ 1. Trademark owned by Brett Hoffman |BR|\ 2. proprietary iOS app developed by Brett Hoffman. See :doc:`/throttles/software/withrottle`
    * - WiThrottle Protocol
      - A proprietary protocol developed by Brett Hoffman
    * - WiThrottle Server
      - A piece of software that listens and acts on WiThrottle commands |BR| |EX-CS| contains a WiThrottle Server, as does |JMRi|

