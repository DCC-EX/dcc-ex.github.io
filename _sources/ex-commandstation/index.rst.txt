.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-cs.rst
|EX-CS-LOGO|

***********************************************************************
EX-CommandStation (RTR or DIY)
***********************************************************************

|SUITABLE| |conductor| |tinkerer| |engineer| |support-button|

.. sidebar::

   .. contents:: On this page
      :local:
      :depth: 1

What is EX-CommandStation?
==========================

First some quick definitions. |EX-CS| is two things:

* It is the name of our command station software that runs on different hardware platforms such as the |EX-CSB1|, |BR| and 
* It is the actual hardware with our software installed that runs your model train layout. 

  That means that when you apply power to your Command Station (CS) it will be an |EX-CS| running the latest version of the |EX-CS| software.

|HR-DASHED|

.. figure:: /_static/images/ex-csb1/csb1_render_drop_shadow.png
   :alt: EX-CommandStation
   :scale: 25%
   :align: right

   RTR EX-CSB1 Command Station / Booster
   
An |EX-CS| is a simple, but powerful, DCC and DC Command Station which you can purchase ready-to-run or assemble yourself from widely available parts. It supports much of the NMRA Digital Command Control (DCC) standards, including:

* Simultaneous control of multiple locomotives
* Control of all cab/loco functions (F0-F28 and F29-F68)
* Control of accessory/function decoders (F0-F28 and F29-F68)
* Main Track: Write configuration variable (CV) bytes and set/clear specific CV bits (aka Programming on Main, or POM)
* Programming Track: Same as the main track with the addition of reading CV bytes

|FORCE-BREAK|

It includes advanced features, such as:

.. figure:: /_static/images/wifi/wangtongze_jumpered.png
   :alt: EX-CommandStation
   :scale: 14%
   :align: right

   DIY EX-CommandStation

* A |WiThrottle Server| implementation for instant compatibility with popular throttles/controllers 
* General purpose inputs and outputs (I/O) for extensibility
* I2C bus for controlling accessories with I2C capability 
* |JMRI| integration
* |EX-R| Automation and Animation scripting that can control everything on your layout, including the locos

It also supports:

* :doc:`Direct Current (DC) </reference/hardware/dcc-vs-dc>` locomotive control using Pulse Width Modulation (PWM)

----

Ready-to-Run (RTR) or Do-It-YourSelf (DIY)
------------------------------------------

To get started, simply choose your path. 

  Whether you are a |Conductor-text|, |Tinkerer-text|, or |Engineer-text|, most people will choose the easy, :doc:`Ready-To-Run</ex-commandstation/rtr-index>` (RTR), option and purchase an |EX-CSB1|. 
  
  Some Tinkerers and Engineers may opt to go the :doc:`Do-It-Yourself</ex-commandstation/diy/index>` (DIY) route by purchasing separate components (or a kit), connecting it together themselves, and installing the |EX-CS| software. 
  
  The choice is yours.

|HR-DASHED|

.. list-table::
    :widths: 50 50
    :header-rows: 0
    :class: table-wrap-text
    :width: 900

    * - |EX-CSB1-LOGO-SMALL|
      - |EX-CS-DIY-LOGO-SMALL|
    * - Our ready-to-run (RTR) DCC & DC command station / booster for controlling your model railroad
      - Do-it-yourself (DIY) instructions on the parts to buy to build your own DCC & DC command station

----

.. list-table::
    :widths: 25 75
    :header-rows: 0
    :class: table-wrap-text
    :width: 900

    * - |conductor| 
      - If you are just starting on the |DCC-EX| journey we recommend you start with the |BR| :doc:`Ready-to-Run</ex-commandstation/rtr-index>` (RTR) page though feel free to try the :doc:`Do-It-Yourself</ex-commandstation/diy/index>` (DIY) path.

----

.. list-table::
    :widths: 25 75
    :header-rows: 0
    :class: table-wrap-text
    :width: 900

    * - |tinkerer| |BR| |BR| |engineer|
      - If you are just starting on the |DCC-EX| journey we also recommend you start with the |BR| :doc:`Ready-to-Run</ex-commandstation/rtr-index>` (RTR) or :doc:`Do-It-Yourself</ex-commandstation/diy/index>` (DIY). |BR| But if you wish to discover more you may want to look at the :doc:`/ex-commandstation/advanced-setup/index` pages for additional options that may be of interest.

.. toctree::
    :maxdepth: 1
    :hidden:

    rtr-index
    diy/index
    advanced-setup/index
    accessories/index