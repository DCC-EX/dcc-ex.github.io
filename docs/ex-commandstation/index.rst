.. include:: /include/include.rst
.. include:: /include/include-l1.rst
..
.. image:: ../_static/images/product-logo-ex-commandstation.png
   :alt: EX-CommandStation
   :scale: 40%
   :align: right

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

|conductor| 

.. toctree::
    :maxdepth: 1
    
    get-started/index

|tinkerer| |engineer|

.. toctree::
    :maxdepth: 1
    
    advanced-setup/index    