.. include:: /include/include.rst
.. include:: /include/include-l2.rst
****************************************
Example - Turntable and traverser ROUTEs
****************************************

|tinkerer| |engineer|

.. code-block:: 

  // On startup, ensure our turntable and traverser move automatically to the first position
  MOVETT(600, 114, Turn)
  MOVETT(601, 100, Turn)
  DONE

  // Definition of the EX_TURNTABLE macro to correctly create the ROUTEs required for each position.
  // This includes RESERVE()/FREE() to protect any automation activities.
  //
  #define EX_TURNTABLE(route_id, reserve_id, vpin, steps, activity, desc) \
    ROUTE(route_id, desc) \
      RESERVE(reserve_id) \
      MOVETT(vpin, steps, activity) \
      WAITFOR(vpin) \
      FREE(reserve_id) \
      DONE

  /**************************************************************************************************
  * TURNTABLE POSITION DEFINITIONS
  *************************************************************************************************/
  // EX_TURNTABLE(route_id, reserve_id, vpin, steps, activity, desc)
  //
  // route_id = A unique number for each defined route, the route is what appears in throttles
  // reserve_id = A unique reservation number (0 - 255) to ensure nothing interferes with automation
  // vpin = The Vpin defined for the Turntable-EX device driver, default is 600
  // steps = The target step position
  // activity = The activity performed for this ROUTE (Note do not enclose in quotes "")
  // desc = Description that will appear in throttles (Must use quotes "")
  //
  EX_TURNTABLE(TTRoute1, Turntable, 600, 114, Turn, "Roundhouse stall 1")
  EX_TURNTABLE(TTRoute2, Turntable, 600, 228, Turn, "Roundhouse stall 2")
  EX_TURNTABLE(TTRoute3, Turntable, 600, 344, Turn, "Roundhouse stall 3")
  EX_TURNTABLE(TTRoute4, Turntable, 600, 459, Turn, "Roundhouse stall 4")
  EX_TURNTABLE(TTRoute5, Turntable, 600, 573, Turn, "Roundhouse stall 5")
  EX_TURNTABLE(TTRoute6, Turntable, 600, 688, Turn, "Roundhouse stall 6")
  EX_TURNTABLE(TTRoute7, Turntable, 600, 2523, Turn, "Yard connection")
  EX_TURNTABLE(TTRoute8, Turntable, 600, 0, Home, "Home turntable")
  EX_TURNTABLE(TTRoute9, Traverser, 601, 100, Turn, "Staging 1")
  EX_TURNTABLE(TTRoute10, Traverser, 601, 699, Turn, "Staging 2")
  EX_TURNTABLE(TTRoute11, Traverser, 601, 1299, Turn, "Staging 3")
  EX_TURNTABLE(TTRoute12, Traverser, 601, 1898, Turn, "Staging 4")
  EX_TURNTABLE(TTRoute13, Traverser, 601, 2498, Turn, "Staging 5")
  EX_TURNTABLE(TTRoute14, Traverser, 601, 3097, Turn, "Staging 6")
  EX_TURNTABLE(TTRoute15, Traverser, 601, 0, Home, "Home traverser")

  // Pre-defined aliases to ensure unique IDs are used.
  ALIAS(Turntable, 255)
  ALIAS(Traverser, 254)

  // Turntable ROUTE ID reservations, using <? TTRouteX> for uniqueness:
  ALIAS(TTRoute1)
  ALIAS(TTRoute2)
  ALIAS(TTRoute3)
  ALIAS(TTRoute4)
  ALIAS(TTRoute5)
  ALIAS(TTRoute6)
  ALIAS(TTRoute7)
  ALIAS(TTRoute8)
  ALIAS(TTRoute9)
  ALIAS(TTRoute10)
  ALIAS(TTRoute11)
  ALIAS(TTRoute12)
  ALIAS(TTRoute13)
  ALIAS(TTRoute14)
