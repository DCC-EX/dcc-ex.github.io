\|EX-REF-LOGO\|

# Glossary

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

  -------------------------------------------------------------------------------------------------------------------------------------------
  Term                  Meaning
  --------------------- ---------------------------------------------------------------------------------------------------------------------
  Access Point (AP)     In Access Point (AP) mode, the tiny ESP-WiFi chip acts as a very basic WiFi server and provides a small IP network
  Mode                  for your throttle or for your computer running JMRI with the WiThrottle Server enabled. It acts much like your router
                        does to let things connect directly to it (currently up to four connections). \|BR\| Using the Command Station in AP
                        mode allows you to have a separate network so you can keep your layout network separate from your home network.
                        \|BR\|
                        `Refer here for more information. </ex-commandstation/advanced-setup/supported-wifi/wifi-config>`{.interpreted-text
                        role="doc"}

  Arduino IDE           A free app running on your PC, specifically designed to install software onto Arduino microprocessors. \|BR\|
                        <https://www.arduino.cc/en/software> \|EXTERNAL-LINK\|

  BaseStation-Classic   The original inexpensive Command Station based on the Arduino platform by Gregg Berman.
  \|BR\| DCC++          `This is no longer maintained or supported by the DCC-EX Team`{.interpreted-text role="dcc-ex-red-bold-italic"}.
  (Original)            \|BR\| \|EX-CS\| is a completely new build which maintains backward compatibility with the original DCC++. \|BR\| See
                        `DCC++ VS DCC-EX? <../../news/posts/20201001>`{.interpreted-text role="doc"} for more information

  Base Station \|BR\|   See <https://dccwiki.com/Command_Station> \|EXTERNAL-LINK\|
  Command Station       
  \|BR\| DCC Command    
  Station \|BR\| DCC    
  Base Station          

  Consist \|BR\|        Multiple locos hauling a singe train. see <https://dccwiki.com/Multiple_Unit_Consisting> \|EXTERNAL-LINK\|
  Multiple Unit         

  Cab                   A Cab can refer to a throttle (or controller) as well as a loco or locomotive \|BR\| In the context of DCC-EX
                        commands, [cab]{.title-ref} refers to a loco\'s/Decoder\'s DCC Address

  DC                    Direct Current

  DCC                   Digital Command Control. NMRA Specification for controlling trains. \|BR\| See
                        <https://dccwiki.com/NMRA/NMRA_Standards> \|EXTERNAL-LINK\|

  Engine Driver \|BR\|  Android app for controlling DCC locos using the WiThrottle Protocol \|BR\| See
  Engine Driver         `/throttles/software/engine-driver`{.interpreted-text role="doc"}
  Throttle              

  DCC++ Commands \|BR\| Old name for the DCC-EX Native Commands / DCC-EX Native Protocol. \|BR\| Some references to this still remain for
  \<DCC++\> \|BR\|      backward compatibility. i.e. JMRI still refers to DCC++.
  DCC++ Protocol \|BR\| 
  DCC++ API             

  DCC-EX Native         New name for the DCC++ Commands/Protocol/API. \|BR\| Refer to
  Commands \|BR\|       `/reference/software/command-summary-consolidated`{.interpreted-text role="doc"} for details.
  DCC-EX Native         
  Protocol \|BR\|       
  DCC-EX Native API     

  JMRI                  [Java Model Railroad Interface](https://www.jmri.org/)

  Motor Driver          Same as \"Motor Shield\" \"Motor Board\" \"Motorboard\" \|BR\| See
                        `/reference/hardware/motor-boards`{.interpreted-text role="doc"}

  Native Protocol /     Native protocol used by the \|EX-CS\| in preference to the WitThrottle protocol. This is the preferred protocol for
  Native DCC-EX         communication with the Command Station as it is considerably more powerful and comprehensive. This was originally
  Protocol / DCC++      developed for the now defunct DCC++ project, hence it is still referred to in JMRI as \'DCC++\', but have been
  Protocol              considerably enhanced since then.

  Station (STA) Mode    Station Mode allows you to connect the Command Station to your existing home network. \|BR\| The Command Station
                        becomes a Station or Client rather than an Access Point. \|BR\| That means instead of being a host that manages the
                        IP of the smartphone that runs your Throttle, it becomes a station that connects to your existing network just like
                        any of the other computers or devices connected to your network. The Throttle then connects to the Command Station by
                        finding its IP address on the network. \|BR\|
                        `Refer here for more information. </ex-commandstation/advanced-setup/supported-wifi/wifi-config>`{.interpreted-text
                        role="doc"}

  Switching[^1] \|BR\|  The process of moving individual carriages to/from specific locations on yards or sidings.
  Shunting[^2]          

  Turnouts[^3] \|BR\|   A mechanical device to guide a train from one track to another
  Points[^4]            

  Switch[^5]            A switch is another term for a turnout, but may also refer to a physical electronic switch (as in a light switch).

  USB                   Universal Serial Bus

  Visual Studio Code    A free app running on your PC that, among other capabilities, can install software onto Arduino microprocessors
  (VSC)                 \|BR\| <https://code.visualstudio.com/> \|EXTERNAL-LINK\|

  WiThrottle            1\. Trademark owned by Brett Hoffman \|BR\|2. proprietary iOS app developed by Brett Hoffman. See
                        `/throttles/software/withrottle`{.interpreted-text role="doc"}

  WiThrottle Protocol   A proprietary protocol developed by Brett Hoffman

  WiThrottle Server     A piece of software that listens and acts on WiThrottle commands \|BR\| \|EX-CS\| contains a WiThrottle Server, as
                        does \|JMRI\|

  Roster                A roster is a list of locomotives that are known in advance by the command station so that DCC addresses, name, and
                        functions can be used by throttles to configure buttons etc.

  VPIN                  A VPIN is an Arduino pin number that has been extended to include pins on external devices or expanders. Once the
                        mapping of VPIN numbers to devices has been done, the commands that set or test pins do not have to care how the
                        electronics works.
  -------------------------------------------------------------------------------------------------------------------------------------------

[^1]: Term primariarly used in North American railroading.

[^2]: Term used in most of the English speaking world other than North
    America. (British/United Kingdom origin)

[^3]: Term primariarly used in North American railroading.

[^4]: Term used in most of the English speaking world other than North
    America. (British/United Kingdom origin)

[^5]: Term primariarly used in North American railroading.
