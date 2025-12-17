.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Multiple Files in EXRAIL
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

|EX-R| commands are read by the compiler only from the file ``myAutomation.h``. The absence of a file with this name means no |EX-R| code is loaded into the command station.

However, it is simple to partition ``myAutomation.h`` into separate files for the convenience of editing. For example ``myTurnouts.h``, ``myRoster.h`` and so on. By ensuring all the files start with "my" it avoids issues with name clashes or Git.

To include your additional files, use the c++ preprocessor ``#include`` control in ``myAutomation.h`` to insert the file contents exactly as if you had typed them into ``myAutomation.h``

.. code-block:: cpp

    // Include my roster file
    #include "myRoster.h"
    // Include my turnout definitions
    #include "myTurnouts.h"
    // Special animation
    #include "myCowOnElectricFence.h"

A note to hardened C++ programmers... do not be tempted to add include guards to your .h files.
