.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-description.rst
|EX-REF-LOGO|

****************************
Single character OPCODE list
****************************

This page is intended to be a quick list of all single character OPCODEs in use by the |DCC-EX| native commands and |EX-R| commands.

When investigating the feasibility of new features, discussions around an appropriate single character OPCODE arise, and this page is designed to assist in understanding which characters are available or in use to help facilitate those discussions and decisions, and select an appropriate character.

For information on |DCC-EX| native commands, refer to the :doc:`/reference/software/command-summary-consolidated`, and for information on |EX-R| commands, refer to the :doc:`/ex-rail/EX-RAIL-command-reference`.

.. csv-table:: Single character OPCODE list
  :widths: auto
  :header-rows: 1

  Character, Usage
  /, |EX-R| interactive commands
  \-, Remove from reminder table
  =, |TM| configuration
  !, Emergency stop
  @, Reserved for future use
  #, Request number of supported cabs/locos; heartbeat
  \+, WiFi AT commands
  ?, Reserved for future use
  0, Track power off
  1, Track power on
  a, DCC accessory control
  A,
  b, Write CV bit on main
  B, Write CV bit
  c, Request current command
  C,
  d,
  D, Diagnostic commands
  e, Erase EEPROM
  E, Store configuration in EEPROM
  f, Loco decoder function control (deprecated)
  F, Loco decoder function control
  g,
  G,
  h,
  H, Turnout state broadcast
  i, Reserved for future use
  I, Reserved for future use
  j, Throttle responses
  J, Throttle queries
  k, Reserved for future use
  K, Reserved for future use
  l, Loco speedbyte/function map broadcast
  L,
  m,
  M, Write DCC packet
  n,
  N,
  o,
  O, Output broadcast
  p, Broadcast power state
  P, Write DCC packet
  q, Sensor deactivated
  Q, Sensor activated
  r, Broadcast address read on programming track
  R, Read CVs
  s, Display status
  S, Sensor configuration
  t, Cab/loco update command
  T, Turnout configuration/control
  u, Reserved for user commands
  U, Reserved for user commands
  v,
  V, Verify CVs
  w, Write CV on main
  W, Write CV
  x,
  X, Invalid command
  y,
  Y, Output broadcast
  z,
  Z, Output configuration/control
