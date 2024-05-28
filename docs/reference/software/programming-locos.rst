.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-reference.rst
|EX-REF-LOGO|

***********************
Programming Locos (CVs)
***********************

|conductor| |tinkerer| |engineer| |support-button|

Requirements
=============

* A DCC Enabled loco with a working Decoder
* A separate section of track, a siding electrically isolated from the main track, or possibly a rolling road
* A motor shield or motor driver with current sense capability

.. NOTE:: The default EX-CommandStation with a dual output Arduino Motor shield has everything you need, a main track output, a programming track output, and a configuration that handles current sense for programming a loco on output B and current sense for overlimit detection on output A.

There are a number of ways you can program decoders with the |EX-CS| including:

* `JMRI DecoderPro`_
* `Programming CVs with EX-Toolbox app`_
* `Programming CVs with Engine Driver app`_ 

JMRI DecoderPro
===============

While it is possible to use the |DCC-EX| API to program decoders, the recommended course of action at the moment is to use |JMRi| DecoderPro for this as it provides a comprehensive yet relatively simple to use interface for all your programming needs.

For a quick intro to setting up roster entries in |JMRi| and changing basic items such as the decoder address, refer to :ref:`big-picture/stage1:jmri (programming decoders)`.

When launching |JMRi| DecoderPro, you will see your list of roster entries by default.

To make changes to your decoder settings, select the loco you wish to program, then click the :guilabel:`Program` button to launch the programming dialog.

* To set basic items such as the decoder address and speed steps, use the options on the "Basic" tab
* For options such as acceleration and deceleration, use the "Motor" tab, noting there is also a "Momentum" tab for more control over inertia settings
* To adjust speed matching, you can update speed options on either the "Basic Speed Control" or "Speed Table" tabs, depending upon your appetite for pain and frustration
* If you have a sound decoder, then adjust the appropriate settings on the "Sound" and "Sound Levels" tabs

When you're finished editing, you need to write the changes to the decoder. To do so, there are four options:

* :guilabel:`Write changes on sheet` - use this if you've only made a few changes on one tab
* :guilabel:`Write full sheet` - use this if you're not sure if all settings on the tab are already set or not, it will take a little longer to write
* :guilabel:`Write changes on all sheets` - use this if you've made changes on multiple tabs
* :guilabel:`Write all sheets` - use this if you want to ensure every setting on every tab is written, noting this will take some time to write

Note that this really is just scratching the surface of the capabilities of DecoderPro, and we highly recommend you read the full documentation on the `JMRI website <https://www.jmri.org/help/en/html/apps/DecoderPro/index.shtml>`_.

Even if you don't intend to use |JMRi| to control your layout, it still has the best decoder programming functionality by far.

DCC-EX & JMRI DecoderPro Getting Started Guide
----------------------------------------------

To assist you in setting up a DCC-EX & JMRI DecoderPro Programming Station please download and follow the :ref:`reference/downloads/documents:comprehensive dcc-ex & jmri decoderpro getting started guide pdf`.

Programming CVs with EX-Toolbox app
===================================

Refer to the :ref:`EX-Toolbox page <ex-toolbox/using:cv programming>` for information on how to program CVs with EX-Toolbox app.

Programming CVs with Engine Driver app
======================================

.. todo:: Programming CVs with Engine Driver