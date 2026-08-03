\|EX-R-LOGO\|

# Command Filters

\|SUITABLE\| \|tinkerer\| \|engineer\| \|support-button\|

A command filter intercepts `< >` type commands from throttles or the
serial monitor and can be used to override, block or modify existing
commands and implement completely new commands.

The following code, added to myAutomation.h like any other \|EX-R\|
code, gives a basic example.

``` cpp
STEALTH_GLOBAL(
  void myFilter(Print * stream, byte & opcode, byte & paramCount, int16_t p[]) {
    (void)stream;
    // use command <U locoid> to display name from roster
    if (opcode == 'U' && paramCount == 1) {
      auto locoId=p[0];
      auto name=RMFT2::getRosterName(locoId);
      if (!name) return; // caller will <X> this
      opcode=0; // caller can now ignore this
      StringFormatter::lcd(0, F("Loco %d name %S"), locoId, name);
    }
  }
)
```

- All `<>` commands will be broken into an opcode and numeric parameters
  before being passed to myFilter.
- You can only have one myFilter function but it can filter multiple
  commands by inspecting the opcode.
- The filter function can inspect or modify the opcode and parameters,
  make changes and return. If the opcode is set to 0, the caller will
  assume that the filter has completely handled the command and will not
  check it further.
- Output directed to the stream parameter will be transmitted back to
  the originating throttle. If no output is expected then casting to
  void is a good way of eliminating the \"unused parameter\" compiler
  warning.
- the `<U>` and `<u>` opcodes are reserved for use by users. They will
  not clash with any future DCC-EX commands.
- Although this is a conventional c++ function, the use of
  `STEALTH_GLOBAL` in \|EX-R\| avoids the need to #include a vast array
  of weird and wonderful API and memory management definitions.
- To recognize keyword parameters (e.g `<1 MAIN>`) you would test using
  the [hk]{#hk} suffix like this

``` cpp
if (opcode == '1' && paramCount == 1 && p[0] == "MAIN"_hk) 
```
