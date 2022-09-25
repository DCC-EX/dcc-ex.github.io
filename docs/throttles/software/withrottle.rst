.. include:: /include/include.rst
.. include:: /include/include-l2.rst
***********
WiThrottle
***********

|conductor|

.. sidebar:: 

   .. contents:: On this page
      :depth: 2
      :local:

.. image:: /_static/images/throttles/icon_ios.png
   :alt: iOS Logo
   :scale: 30%
   :align: left

This is an iOS App (with plans for iOS) from the USA. |WiThrottle| is probably the most popular iOS throttle since early on |JMRI| built a |WiThrottle Server| into its program. You can connect WiThrottle to |JMRI| and connect |JMRI| to |EX-CS|, or you if you are not going to use |JMRI|, you can connect directly to the Command Station if you install a WiFi board.

Please visit their website: https://www.withrottle.com

You can find it in the App Store: `WiThrottle <http://itunes.apple.com/app/id344172578>`_

For more information more information about these protocols, see :doc:`WiThrottle Server, Web Server, DCC++ API Explained </throttles/protocols>`

.. _withrottle-features:

Features
=========

* Supports WiThrottle Protocol
* Connect to JMRI
* Connect to |EX-CS| if not using JMRI
* Connect via WiFi
* Read and Write CVs

.. _withrottle-screenshots:

Screenshots
============

.. image:: /_static/images/throttles/withrottle1.png
   :alt: WiThrottle Screenshot 1
   :scale: 90%

..
   The next line is trying to avoid a duplicate label name since many files may have a requirements section

.. _withrottle-requirements:

Requirements
=============

* A |EX-CS| (Mega based for WiFi)
* An iOS Cell Phone or Tablet
* A Wifi Shield (or other ESP8622 solution) if you want to connect using WiFi :doc:`Wifi Setup </ex-commandstation/get-started/wifi-setup>`

.. _withrottle-operation:

Operation
==========

To use Wifi, make sure you have a WiFi enabled |EX-CS| as described in the :doc:`Wifi Setup </ex-commandstation/get-started/wifi-setup>` section.

* Open the network settings on your phone
* Change to same network of the PC that JMRI is on
* Start the |wiThrottle| App
* |wiThrottle| will try to find the |wiThrottle Server| on the |EX-CS|
* If you are using |Access Point Mode| 

  * It should find the |wiThrottle Server| in |JMRI| and automatically connect to it

* You should then see the 'Address Screen'
* Turn the track power on by selecting the 'settings' tab and clicking on the ``Track Power``

   * The four red LEDs on the Motor board will turn on

* Go back to the 'Address' tab
* Enter the DCC Address of the loco you put on the track in the ``Keypad`` field
* Select ``Long`` or ``Short`` (normally if the address is less than 127, it should be a 'Short' address.)
* Click the :guilabel:`Set` button
* The address should appear in the green box at the top left.
* Select the 'Throttle' tab
* You can now use the sliders to move your train 
