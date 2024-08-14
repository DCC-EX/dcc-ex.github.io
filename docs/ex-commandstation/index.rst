.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-cs.rst
|EX-CS-LOGO|

******************
EX-CommandStation
******************

|conductor| |tinkerer| |engineer| |support-button|

What is EX-CommandStation?
==========================

|EX-CS| is simple, but powerful, DCC, and DC, Command Station software which runs on the |EX-CSB1| or on hardware that you can assemble yourself made using widely available Arduino or ESPDuino32 boards. It supports much of the NMRA Digital Command Control (DCC) standards, including:

.. image:: /_static/images/wifi/wangtongze_jumpered.png
   :alt: EX-CommandStation
   :scale: 15%
   :align: right
   
* Simultaneous control of multiple locomotives and their functions
* Control of accessory/function decoders
* Programming Track
* Programming on Main Track

It includes advanced features such as:

* A |WiThrottle Server| implementation for instant compatibility with popular throttles 
* General purpose inputs and outputs (I/O) for extensibility
* I2C bus for controlling accessories with I2C capability 
* |JMRI| integration
* |EX-R| Automation and Animation scripting that can control everything on your layout, including the locos

It also supports:

* Direct Current (DC) locomotive control using Pulse Width Modulation (PWM)

To get started, simply choose your path. Whether you are a Conductor, Tinkerer, or Engineer, most people will choose the easy, ready-to-run option and purchase an |EX-CSB1|. Some Tinkerers and Engineers may opt to go the DIY route by purchasing separate components (or a kit), connecting it together themselves, and installing the |EX-CS| software. The choice is yours.

----

.. list-table::
    :widths: 50 50
    :header-rows: 0
    :class: table-wrap-text
    :width: 900

    * - |EX-CSB1-LOGO-SMALL|
      - |EX-PLACEHOLDER|
    * - Our ready-to-run DCC & DC command station / booster for controlling your model railroad
      - DIY instructions on the parts to buy to build your own command station

----

.. list-table::
    :widths: 25 75
    :header-rows: 0
    :class: table-wrap-text
    :width: 900

    * - |conductor| 
      - If you are just starting on the |DCC-EX| journey we recommend you start with the |BR| :doc:`Getting started Page <get-started/index>`

----

.. list-table::
    :widths: 25 75
    :header-rows: 0
    :class: table-wrap-text
    :width: 900

    * - | |tinkerer|
        |
        | |engineer|
      - If you wish to discover more you can look at the :doc:`Advanced Options <advanced-setup/index>`, however if you are just starting on the |DCC-EX| journey we also recommend you start with the |br| :doc:`Getting started Page <get-started/index>`, but also look at the :doc:`/ex-commandstation/advanced-setup/index` pages for additional options that may be of interest.

----

.. toctree::
    :maxdepth: 1
    :hidden:

    ready-to-run/index
    diy/index
    advanced-setup/index
    accessories/index