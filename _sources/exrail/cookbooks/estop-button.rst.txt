.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Emergency stop button
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

``ONBUTTON(173)`` will start a sequence at this point when a button on vpin 173 is pressed.

The ``ESTOPALL`` command will stop all locos and inform all throttles.

The ``DONE`` command completes/terminates the process started by ``ONBUTTON``.

.. code-block:: cpp

    ONBUTTON(173) 
      ESTOPALL 
    DONE

