.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Using CALL and RETURN
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

Where you want to use the same sequence of commands from several places in other sequences you can avoid copying the repeated stuff by using ``CALL`` and ``RETURN``

.. code-block:: cpp

    ROUTE(1,"Platform A to mainline")
      CALL(911)
      THROW(1)
      CLOSE(2)
      DONE

    ROUTE(2,"Platform B to mainline")
      CALL(911)
      CLOSE(1)
      CLOSE(2)
      DONE

    SEQUENCE(911)
      SERVO(123,100,Slow)  // move the cow out of the way
      PLAYSOUND(500,3) // Make it Moo
      DELAYRANDOM(5000,10000) // make the route wait 5 to 10 seconds
      RETURN      // return to the calling sequence

Notes
=====

- You can nest CALLs 4 deep.
- If the called sequence executes a ``DONE`` statement, the task is terminated and there is no return.
