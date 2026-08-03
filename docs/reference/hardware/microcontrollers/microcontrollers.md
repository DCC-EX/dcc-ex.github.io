\|EX-CS-LOGO\|

# Beta microcontrollers

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|
\|githublink-ex-commandstation-button-small\|

:::: 

::: 
On this page
:::
::::

## Newer, faster, better

As technology progresses, newer, faster, and better microcontrollers
become available, and therefore the dev team works in the background on
porting and testing of \|DCC-EX\| on newer generations of
microcontrollers to see if they might better suit the \|DCC-EX\|
project.

This is never done lightly, as the effort to support a new
microcontroller might be high and the benefits may be too
inconsequential, or indeed may mean loss of functionality.

### Considerations for new microcontrollers

When considering new microcontrollers to test and experiment with as
potential candidates for \|EX-CS\|, these are the sorts of concerns
taken into account (there are more considerations than this of course,
these are just the highlights):

- Architecture/code portability - how much work is required to adapt the
  codebase to support the architecture?
- Form factor - can existing users use their existing motor shields and
  accessories with them?
- Availability - with continuing microchip shortages impacting supply,
  is it still generally and easily available in quantity, and globally
  as we have users all over the world?
- Sustainability - is the manufacturer deprecating the series or likely
  to?
- Price - is it available at a price point that would encourage users to
  adopt it readily?
- Quality - is it available with a sufficient build quality to make it
  reliable?

### Notes on 3v3 vs. 5V microcontrollers

It\'s important to note that the newer generations of microcontrollers
almost always operate at 3.3 volts rather than 5 volts.

For some, like the STM32F4xx range, this is a non-issue as their digital
I/O pins are designed to be 5V tolerant, meaning your existing sensors,
serial devices, and \|I2C\| devices running at 5V are expected to be
compatible. Outputs may need further consideration though, as while a
\"high\" signal at 3v3 will trigger most 5V input logic devices, in some
rare instances it can potentially not provide a high enough voltage.
Using level shifters for digital outputs will resolve these issues, and
if you want an extra layer of caution, you can use level shifters for
the digital inputs as well.

For others that are not 5V tolerant, using 5V accessories will cause
damage to the microcontroller, so using digital I/O level shifters is
mandatory with these.

ALL 3v3 microcontrollers require analog inputs to be restricted to no
more than 3.3V. This means only some Motor Driver boards are compatible
unmodified with 3v3 microcontrollers to read output current. For the
moment we recommend the genuine Ardiuno Motor Driver R3, and only the R3
version of it. Motor Drivers such as the Deek Robot can be modified
readily enough. We will document this, but in the meantime ask on the
Discord server.

:!!! note "::: title
Note"
:::

Some devices such as the ESP01 WiFi board and HC05/06 Bluetooth boards
are already 3v3 devices, so if you have set these up with level
shifters, the level shifters will no longer be required when using 3v3
microcontrollers.
::::
