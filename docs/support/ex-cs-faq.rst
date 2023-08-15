.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-ex-cs.rst
.. meta::
   :keywords: EX-CommandStation Command Station diagnosing Issues Troubleshooting

|EX-CS-LOGO|

********************************
Frequently Asked Questions (FAQ)
********************************

|conductor| 

This is a list of **Frequently Asked Questions** that we answer on our various support channels:

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Question
    - Answer
  * - Can I run a loco on the programming track?
    - Yes, by issuing the command ``<1 JOIN>`` via the serial console.  |BR| This is intended to be temporary, for running a loco from a programming track onto your layout, not for normal running of the layout. |BR| |BR| (In |Engine driver| you can :guilabel:`Request Loco ID` which will also temporarily allow the loco to be driven from the programming track. see :doc:`/throttles/driveaway` for more information.)
  * - Why Can't I Put an EX-RAIL Script on an SDCard?
    - Being able to read an SD card on the Arduino platforms requires a significant amount of code because there is no operating system or file system which we would take for granted on a PC. We simply don’t have enough free memory on an Arduino to hold that code. |BR| |BR| See :ref:`ex-rail/about:why can't i put a script on an sdcard?` for more information.

.. todo:: `LOW - More FAQs to follow <https://github.com/DCC-EX/dcc-ex.github.io/issues/434>`_
