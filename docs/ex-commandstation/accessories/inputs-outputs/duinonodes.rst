.. include:: /include/include.rst
.. include:: /include/include-l1.rst
  
***************************
Lew's Duino Gear duinoNodes
***************************

|tinkerer| |engineer| |githublink-ex-commandstation-button2|

|NEW-IN-V5-LOGO-SMALL|

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:

Lew's Duino Gear sells various intelligent electronics designed for model railroads, and there is now a device driver available to use two of the I/O products, the DNIN8/DNIN8K Digtail Input duinoNode, and the DNOU8/DNOU8K Digital Output duinoNode.

This page documents the configuration of these boards with |EX-CS| only.

For documentation, support, and reference on the boards themselves, refer to the `Lew's Duino Gear <https://beaglebay.com/duinogear/>`_ website and/or the product documentation supplied with the boards.

DNIN8/DNIN8K Digital Input duinoNode
====================================

This is a shift-register implementation of a digital input collector. Multiple DNIN8 boards may be chained together but it is important that the software configuration correctly represents the number of boards connected otherwise the results will be meaningless.

The new DNIN8 and the original DNIN8K are addressed slightly differently, so you must use the correct device name to match the boards in use when configuring the software.

This also means you can only chain DNIN8 boards with DNIN8 boards, and if you have both types in use, you will need a separate chain for the DNIN8K boards.

Each chain of DNIN8 or DNIN8K boards will require three available direct I/O pins on your |EX-CS| to connect to. These pins can not be on |I2C| I/O expanders.

DNOU8/DNOU8K Digital Output duinoNode
=====================================

The DNOU8/DNOU8K operate in a similar manner to the input modules, but are for outputs. As per the DNIN8/DNIN8K, multiple boards may be chained together but it is important that the software configuration correctly represents the number of boards connected otherwise the results will be meaningless.

These must be connected in a separate chain to either DNIN8 or DNIN8K chains, and therefore require an additional three available direct I/O pins on your |EX-CS|.

DNOU8 and DNOU8K boards can be connected together on the same chain and use the same device driver.

Vpin allocation
===============

You must ensure the correct number of Vpins are allocated to match the number of boards used in a chain, with 8 Vpins required per board, and you must only connect the number of boards in a chain to match the allocated Vpins.

While it is possible to specify a non-multiple of 8 pins, this will be rounded up to a multiple of 8.

Device driver configuration
===========================

You can configure the device driver for the boards either in "myAutomation.h" or in "myHal.cpp".

In both scenarios, these are the required parameters:

- firstVpin = first available Vpin to allocate
- numPins = total number of Vpins to allocate to the entire chain
- clockPin = I/O pin on your CommandStation to connect to the clock pin on the chain of boards
- latchPin = I/O pin on your CommandStation to connect to the latch pin on the chain of boards
- dataPin = I/O pin on your CommandStation to connect to the data pin on the chain of boards

The valid formats for "myAutomation.h" are outlined below with examples:

.. code-block:: 

  HAL(IO_DNIN8, firstVpin, numPins, clockPin, latchPin, dataPin)    // DNIN8 boards only
  HAL(IO_DNIN8K, firstVpin, numPins, clockPin, latchPin, dataPin)   // DNIN8K boards only
  HAL(IO_DNOU8, firstVpin, numPins, clockPin, latchPin, dataPin)    // DNOU8/DNOU8K boards

  HAL(IO_DNIN8, 400, 16, 40, 42, 44)    // Create a chain for two DNIN8 boards
  HAL(IO_DNIN8K, 420, 16, 39, 41, 43)   // Create a chain for two DNIN8K boards
  HAL(IO_DNOU8, 450, 16, 45, 47, 49)    // Create a chain for two DNOU8/DNOU8K boards

The formats for "myHal.cpp" are outlined below with examples:

.. code-block:: cpp

  IO_DNIN8::create(firstVpin, numPins, clockPin, latchPin, dataPin);    // DNIN8 boards only
  IO_DNIN8K::create(firstVpin, numPins, clockPin, latchPin, dataPin);   // DNIN8K boards only
  IO_DNOU8::create(firstVpin, numPins, clockPin, latchPin, dataPin);    // DNOU8/DNOU8K boards

  IO_DNIN8::create(400, 16, 40, 42, 44);    // Create a chain for two DNIN8 boards only
  IO_DNIN8K::create(420, 16, 39, 41, 43);   // Create a chain for two DNIN8K boards only
  IO_DNOU8::create(450, 16, 45, 47, 49);    // Create a chain for two DNOU8/DNOU8K boards

The examples above will result in:

- Two DNIN8 boards with the first board (closest to your |EX-CS|) available on Vpins 400 - 407, and the second on Vpins 408 - 415
- Two DNIN8K boards with the first board (closest to your |EX-CS|) available on Vpins 420 - 427, and the second on Vpins 428 - 435
- Two DNOU8/DNOU8K boards with the first board (closest to your |EX-CS|) available on Vpins 450 - 457, and the second on Vpins 458 - 465