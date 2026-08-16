EXRAIL compiler and resource usage
==================================

EXRAIL expands ``myAutomation.h`` into a byte-coded route table and lookup tables during firmware compilation. The route table is stored in flash. At startup, routes and event handlers are indexed in RAM, and each active sequence has an ``RMFT2`` task object.

Task lifetime and recycling
---------------------------

Running sequences are linked in a task ring. When a task reaches ``DONE`` or is killed, its destructor releases the task object so a later sequence can reuse that heap allocation. Concurrent sequences increase peak RAM use; completed tasks can be recycled. Each task stores program-counter, delay, locomotive, event, pause, and call-stack state. The current upstream implementation sets the call-stack depth to 4.

Runtime resource use
--------------------

Startup allocates RAM-backed lookup arrays for routes and event handlers including ``ONTHROW``, ``ONCLOSE``, ``ONACTIVATE``, ``ONCHANGE``, ``ONTIME``, and overload/block handlers when used. Signals and route-state features add further tables. The exact cost depends on the target board, definitions, optional features, and simultaneous tasks. There is no portable maximum-lines limit: available flash and free heap are the practical limits.

Compile-time checks
-------------------

The assertion pass over ``myAutomation.h`` checks sequence references and duplicate route/automation/sequence IDs; flag IDs 0--255; speed values 0--127; ``SPEED_REL`` 1--500 percent; valid signal addresses; and reserved motor-shield/critical pins used by ``SET``, ``RESET``, ``BLINK``, and signal macros. These checks do not measure runtime capacity: compile success and sufficient free RAM are separate checks.

When a script grows, inspect compiler flash/RAM output and test the largest expected number of simultaneous automations and event handlers. Let finished sequences reach ``DONE``, avoid unnecessary concurrent tasks, remove unused event handlers/features, and keep ``CALL`` nesting within 4. These details are based on upstream ``EXRAIL2.h``, ``EXRAIL2.cpp``, and ``EXRAILAsserts.h`` and may change with firmware revisions.
