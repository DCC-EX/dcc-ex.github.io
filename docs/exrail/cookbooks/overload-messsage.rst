.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Message on Overload or Short Circuit
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

``ONOVERLOAD(output)`` will start a sequence when an overload or short circuit is detected on the track/output. |BR|
``MESSAGE(message)`` will display a message on all throttles. |BR|
``AFTEROVERLOAD(output)`` will continute the sequence at this point after the overload or short circuit is cleared.

.. code-block:: cpp

    ONOVERLOAD(A)
      PRINT("Overload Detected on A")
      BROADCAST("Overload Track A")
      MESSAGE("Overload Track A")
      AFTEROVERLOAD(A)
        DELAY(2000)
        BROADCAST("Overload Track A - Cleared")
        MESSAGE("Overload Track A - Cleared")
    DONE

For tracks/outputs B-H, duplicate the entire block above and replace 'A' with the appropriate track/output letter.