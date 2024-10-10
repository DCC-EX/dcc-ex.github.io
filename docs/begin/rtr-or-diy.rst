.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-cs.rst
|EX-CS-LOGO|

********************************************
Choose Ready-to-Run or DIY Command Station
********************************************

|conductor| |tinkerer| |engineer| |support-button|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

What is EX-CommandStation?
==========================

First some quick definitions. EX-CommandStation is 2 things. It is the name of our command station software that runs on different hardware platforms such as the |EX-CSB1|, and it is the actual hardware with our software installed that runs your model train layout. That means that when you apply power to your Command Station (CS) it will be an |EX-CS| running the latest version of the |EX-CS| software.

An |EX-CS| is a simple, but powerful, DCC and DC Command Station which you can purchase ready-to-run or assemble yourself from widely available parts. It supports much of the NMRA Digital Command Control (DCC) standards, including:

.. image:: /_static/images/wifi/wangtongze_jumpered.png
   :alt: EX-CommandStation
   :scale: 15%
   :align: right

* Simultaneous control of multiple locomotives
* Control of all cab functions (F0-F28 and F29-F68)
* Control of accessory/function decoders (F0-F28 and F29-F68)
* Main Track: Write configuration variable (CV) bytes and set/clear specific CV bits (aka Programming on Main, or POM)
* Programming Track: Same as the main track with the addition of reading CV bytes

It includes advanced features such as:

* A |WiThrottle Server| implementation for instant compatibility with popular throttles 
* General purpose inputs and outputs (I/O) for extensibility
* I2C bus for controlling accessories with I2C capability 
* |JMRI| integration
* |EX-R| Automation and Animation scripting that can control everything on your layout, including the locos

It includes advanced features such as:

XXX

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
      - |EX-CS-DIY-LOGO-SMALL|
    * - Our ready-to-run DCC & DC command station / booster for controlling your model railroad
      - DIY instructions on the parts to buy to build your own command station

----

.. list-table::
    :widths: 25 75
    :header-rows: 0
    :class: table-wrap-text
    :width: 900

    * - |conductor| 
      - If you are just starting on the |DCC-EX| journey we recommend you start with the |BR| :doc:`/ex-commandstation/ready-to-run/index` page though feel free to try the :doc:`/ex-commandstation/diy/index` path.

----

.. list-table::
    :widths: 25 75
    :header-rows: 0
    :class: table-wrap-text
    :width: 900

    * - | |tinkerer|
        |
        | |engineer|
      - If you wish to discover more you can look at the :doc:`Advanced Options </ex-commandstation/advanced-setup/index>`, however if you are just starting on the |DCC-EX| journey we also recommend you start with the |br| :doc:`/ex-commandstation/ready-to-run/index` or :doc:`/ex-commandstation/diy/index`, but also look at the :doc:`/ex-commandstation/advanced-setup/index` pages for additional options that may be of interest.

----

.. toctree::
    :maxdepth: 1
    :hidden:

    /ex-commandstation/ready-to-run/index
    /ex-commandstation/diy/index
    /ex-commandstation/advanced-setup/index
    /ex-commandstation/accessories/index