.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Roster for Similar Sound Locos
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

The ROSTER command in |EX-R| can be tedious if you have several sound locos with the same function settings. Using a preprocessor definition saves typing.

.. code-block:: cpp

    ROSTER(1201,"Red class 99","light/*horn/flash/bang/wallop/squeal/honk") 
    ROSTER(1202,"Green class 99","light/*horn/flash/bang/wallop/squeal/honk") 
  
Can be simplified by pre-defining the functions:

.. code-block:: cpp

    #define CLASS99F "light/*horn/flash/bang/wallop/squeal/honk" 
    ROSTER(1201,"Red class 99",CLASS99F) 
    ROSTER(1202,"Green class 99",CLASS99F) 
  
This technique is particularly useful for rostering DC tracks where the function keys are related to PWM frequency:

.. code-block:: cpp

    #define DCFuncs"/////////////////////////////FQ490 Hz/FQ3400 Hz/FQ62500 Hz"
    ROSTER(1225,"DC TRACK B 1225",DCFuncs)
    ROSTER(1226,"DC TRACK C 1226",DCFuncs)

It is also possible to utilise the compiler rule that "Hello" "Sailor" is treated as "HelloSailor". This means that common functions can be used with loco specific additions.

.. code-block:: cpp

    #define CommonFuncs "light/*horn" 
    ROSTER(1201,"Noisy class 99",CommonFuncs "/flash/bang/wallop/squeal/honk") 
    ROSTER(1202,"Quieter class 99",CommonFuncs) 
