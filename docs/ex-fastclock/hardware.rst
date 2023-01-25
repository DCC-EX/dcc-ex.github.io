.. include:: /include/include.rst
.. include:: /include/include-l1.rst

|EX-FC-LOGO|

**********
Hardware
**********

|tinkerer| |githublink-ex-turntable-button2|

.. sidebar:: 

  .. contents:: On this page
    :depth: 2
    :local:
  
What you need for EX-FastClock
==============================

* An |EX-CS| running the "devel" branch of `EX-CommandStation <https://github.com/DCC-EX/CommandStation-EX/tree/devel>`_ (this displays as version 4.2.9rc1)
* An Arduino Uno microcontroller
* An MCUFRIEND type plug in sheild TFT touchscreen
* A suitable power supply
* Dupont type wires to connect the components, male to female or female to female as required
* A USB cable to connect the Arduino to a PC to load the software

The software for the |EX-FastClock| can be found in the |EX-FastClock| repository in the |DCC-EX| GitHub.  The code can be configured to run a clock which will communicate to the |EX-CommandStation| by either Serial or I2C.  The options are chosen from the file config.h.  Instructions are contained in the README.md file.  Which option you choose will depend upon wether you have serial throttles connected to the serial ports in which case I2C might be the better option.  Alternatively if you already have lots of I2C devices then it might be better to run the Serial option.


ToDo
====

Add a more detailed description here

Next Steps
==========

Now that you know what you need, click the "next" button see how you use |EX-FC|.