.. include:: /include/include.rst
.. include:: /include/include-l2.rst
***********************
Programming Locos (CVs)
***********************

|conductor| |tinkerer| |engineer|

Requirements
=============

* A DCC Enabled loco with a working Decoder
* A separate section of track or a siding electrically isolated from the main track
* A motor shield or motor driver with current sense capability

.. NOTE:: The default EX-CommandStation with a dual output Arduino Motor shield has everything you need, a main track output, a programming track output, and a configuration that handles current sense for programming a loco on output B and current sense for overlimit detection on output A.

JMRI DecoderPro
===============

While it is possible to use the |DCC-EX| API to program decoders, the recommended course of action at the moment is to use |JMRi| DecoderPro for this as it provides a comprehensive yet relatively simple to use interface for all your programming needs.

For a quick intro to setting up roster entries in |JMRi| and changing basic items such as the decoder address, refer to :ref:`big-picture/stage1:jmri (programming decoders)`.

Roster entries
--------------

Programming individual CVs
--------------------------

Comprehensive programmer
------------------------
