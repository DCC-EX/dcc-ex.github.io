.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Naming sequences for easy commands
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

The DCC-EX command

.. code-block:: cpp

    </START id>

can be used to start a sequence when the sequence id is known.

However its is sometimes more convenient to code a sequence so that it can be started by name.

This is made possible by using upper case quoted sequence names with the _hk suffix.

.. code-block:: cpp

    SEQUENCE("BEER"_hk)  
      PRINT("BEER sequence started")
      ... and so on

The name must be specified in upper case but it can be started by the command in any mixed case.

.. code-block:: cpp

     </start beer>
