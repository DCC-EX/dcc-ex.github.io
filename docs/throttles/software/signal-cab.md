# Signal Cab

\|conductor\| \|tinkerer\| \|engineer\|

![Signal Cab Logo](/_static/images/throttles/signal_cab_logo.png)

[Signal Cab](https://signalcab.com) \|EXTERNAL-LINK\| is a modern DCC
controller for iPhone and iPad, built by model railroaders for model
railroaders. It combines precision locomotive control with a clean,
intuitive interface --- manage your fleet, run consists, program
decoders, and control track power, all from your iOS device.

Please visit their website: <https://signalcab.com> \|EXTERNAL-LINK\|

## Features 

**Throttle & Control**

- Multi-throttle support --- control multiple locomotives with a
  swipeable carousel; quick-switch between active locos without missing
  a beat
- Full 128 speed step resolution for smooth, precise control
- One-tap Emergency Stop (E-Stop)
- Configurable E-Stop behavior and track power management (main and
  programming track)

**Locomotive Library**

- Full roster management with search, favorites, and group organization
- Supports short DCC addresses (1--127) and long DCC addresses
  (128--10293)
- Import locomotive rosters from \|EX-CS\| and \|JMRI\|; DigiTrains Pro
  import coming soon
- DCC address conflict detection --- prevents two locomotives sharing
  the same address from entering service simultaneously

**Function Control**

- Full F0--F28 function support with both momentary and latching modes
- Built-in decoder defaults for SoundTraxx, Digitrax, and NMRA standards
- Fully customizable function labels, icons, and colors

**Consist Control**

- Build virtual and advanced consists
- Per-member direction control and speed trim
- Automated decoder programming for consist members

**CV Programming** *(Beta)*

- Read and write configuration variables (CVs) directly on the
  programming track --- no separate programmer or computer required
- Visual speed curve editor supporting CV2--6 and full 28-point speed
  tables
- Fine-tune acceleration, deceleration, and trim to match your prototype

**Connectivity**

- Automatic command station discovery via mDNS --- no IP addresses to
  enter; Signal Cab finds your station on the local network
  automatically
- Auto-reconnect with exponential backoff and a configurable resume
  window (10--60 minutes)
- Connects via WiFi

**Protocol Support**

- \|DCC-EX Native Commands\| --- stable; connects directly to \|EX-CS\|
  with full command set including programming, turnouts, and diagnostics
- \|WiThrottle Protocol\| --- beta; connects directly to \|EX-CS\| or
  via \|JMRI\| and other WiThrottle-compatible command stations
- Z21 / SRCP --- planned for a future release

**Apple Platform Integration**

- Siri commands, App Shortcuts, and Spotlight integration --- trigger
  actions hands-free
- Customizable iPhone Action Button support
- Tactile haptic feedback on the throttle
- Designed for iPhone and iPad

## Requirements 

- An \|EX-CS\| with WiFi enabled
- An iOS device (iPhone or iPad) running iOS 15 or later
- WiFi connectivity --- see
  `Wifi Setup </ex-commandstation/diy/wifi-setup>`
