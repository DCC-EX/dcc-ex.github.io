.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-CS-LOGO|

******************
EX-CommandStation
******************

What is EX-CommandStation?
==========================

A basic |EX-CS| hardware setup can be made from easy to find, widely available, Arduino boards that you can assemble yourself. It supports much of the NMRA Digital Command Control (DCC) standards, including:

* simultaneous control of multiple locomotives
* Activate/de-activate all accessory function addresses 0-2048
* Control of all cab functions F0-F28 and F29-F68
* Main Track: Write configuration variable (CV) bytes and set/clear specific CV bits (aka Programming on Main, or POM)
* Programming Track: Same as the main track with the addition of reading CV bytes

It includes advanced features such as:

* A WiThrottle server implementation, 
* Turnout operation, 
* General purpose inputs and outputs (I/O) for extensibility, and 
* JMRI integration


.. list-table::
    :widths: 25 75
    :header-rows: 0
    :class: table-wrap-text
    :width: 900

    * - |conductor| 
      - If you are just starting on the |DCC-EX| journey we recommend to start with the |br| :doc:`Getting started Page <get-started/index>`
    * - |BR| |tinkerer| |engineer|
      - If you wish to discover more you can look at the :doc:`Advanced Options <advanced-setup/index>`

.. toctree::
    :maxdepth: 1
    :hidden:

    get-started/index
    advanced-setup/index    