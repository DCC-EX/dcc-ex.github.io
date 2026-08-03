\|EX-FC-LOGO\|

# Configuration options

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|
\|githublink-ex-fastclock-button-small\|

:::: 

::: 
On this page
:::
::::

If you already have a FastCLock \|EX-FC\| has a number of couple of
configuration options which allow you to connect your own clock to a
\|EX-CS\|.

The various configuration options are outlined below

## Connecting your own FastClock

### Connecting via Serial

Connecting via Serial is the simplest option if available.

- Run a dupont cable from the TX pin on the arduino to a RX pin on the
  EX-CommandStation. It is not usually necessary to run a cable from RX
  to the TX on the EX-CommandStation as the FastClock is not receiving
  data back.

- Find the Serial defines in the config.h file (or copy config.example.h
  to config.h if you dont have one), locate the following lines:

  ``` cpp
  //#define SERIAL1_COMMANDS
  //#define SERIAL2_COMMANDS
  //#define SERIAL3_COMMANDS
  ```

  and uncomment the appropriate one for the serial port you are using.

- Add the following code to your Setup() function:

  ``` cpp
  Serial.begin(115200);
  while (!Serial) 
  ```

- Include the following routine within your code:

  ``` cpp
  void SendTime(byte hour, byte mins, byte speed) 
  ```

  In the function above HH is the time as hours (24hr. clock) and MM is
  the minutes.

- The CommandStation-EX will now poll the FastClock to request the time.
  The frequency at which it does so is influenced by the clock speed
  (i.e. on a slow clock speed it polls less often).

\|HR-HEAVY\|

## Next Steps

Now that you know how to connect your existing FastCLock, click the
\'Next\' button see how you use \|EX-FC\|.
