.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst
|EX-CS-LOGO|

********************************
Do-It-YourSelf - Getting Started
********************************

|SUITABLE| |conductor| |tinkerer| |engineer| |support-button|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

In order to get the most out of this website, we ask you at first to make 2 choices:

1. To self-identify your **"level"** with regards to DCC-EX. |BR| If you have not chosen whether you are a |Conductor-text|, |Tinkerer-text|, or |Engineer-text|, please go to the :doc:`/begin/levels` page before proceeding further. |BR| |BR|

2. Choose will be whether you want **"Ready-To-Run" (RTR)** path or the **"Do-It-Yourself" (DIY)** path. |BR| If you want the ready-to-run (RTR) path we suggest that you look at the :doc:`/ex-commandstation/ready-to-run/index` page.

**If you are still interested the do-it-yourself (DIY) path then read on...**

.. note:: 
  :class: note-float-right-narrow

  If you need a definition of what an |EX-CS| is, please see :ref:`ex-commandstation/index:what is ex-commandstation?`.

You are here on the DIY path where you will build your own |EX-CS| from commonly available parts.

The following pages will instruct you on how to build an |EX-CS| including; assembling your hardware, installing software, and running your first train. 

After that, we will provide examples for how the |EX-CS| can be extended and upgraded.

|HR-DASHED|

The Components of a Full EX-CommandStation
==========================================

To actually run your model railroad you will need a few items:

.. figure:: /_static/images/wifi/wangtongze_jumpered.png
   :alt: EX-CommandStation
   :scale: 15%
   :align: right

1. a |EX-CS| - This consists of:

  - an **Arduino microprocessor**,
  - a **Motor Driver** board / motor shield,
  - Optionally: 

    - a **WiFi shield (Recommended)** [#inst]_ (*This option is described on the following pages*), or
    - an ethernet shield, or
    - a Bluetooth board, or
    - direct connection to a PC [#jmri]_, and

  - our free, open source, custom software 

.. figure:: /_static/images/engine_driver/vertical_slider.png
   :alt: Engine Driver
   :scale: 75%
   :align: right

2. a **Throttle (Controller)** - Something to control your trains with.  |BR| Such as our |EX-WT|, or other apps like |JMRI|, |Engine Driver|, |WiThrottle|, etc.
3. Power - The Arduino and the Motor shields need to be powered separately, so 
 
  - a **9-14v DC power supply** for the motor shield to the track, and 
  - a **5-9v DC power supply** for the Arduino

4. a **"Main" track,** aka "Operations" track - most people already have this: it's your layout!
5. a **"Programming" track,** aka "Service" track - an isolated short section of track that you will use to program locomotives
6. a **Train** - Specifically, a locomotive equipped with a DCC decoder (either a standard or sound decoder). Ideally, it should be a loco already proven to work on DCC. Otherwise, if you have a problem, you may not be able to tell if the problem is the decoder or the EX-CommandStation

Next Steps - Purchasing Parts
=============================

See the :doc:`purchasing` page or click the 'Next' button to see what you need to acquire to create your |EX-CS|.

----

.. [#inst]  The Instructions on the following pages assume that that you will use a WiFi Shield.
.. [#jmri]  Requires |JMRI| installed on a computer.

.. toctree::
    :hidden:

    purchasing
    assembly
    wifi-setup
    ../installer-diy.rst
    ../controllers-diy.rst
    ../testing-diy.rst
    /support/ex-cs-troubleshooting__included-diy
    /support/wifi-at-version