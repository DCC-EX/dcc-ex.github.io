.. include:: /include/include.rst
.. include:: /include/include-l0.rst
|donate-button|

************************
DCC-EX Model Railroading 
************************

.. rst-class:: dcclink-right

  `We have a New Name! <about/press/new-name.html>`_


Welcome! |BR|\ |DCC-EX| is a team of dedicated enthusiasts producing, easy to use, affordable, do-it-yourself, open source, DCC solutions to allow you to run your complete model railroad layout. 
Based on off-the-shelf Arduino technology, our products currently include:
 
* |EX-CS| - our DCC command station for controlling your model railroad

  * |EX-I| - our user friendly installer for loading the command station firmware onto your Arduino hardware
  * |EX-R| - the scripting language, built into the |EX-CS|, allowing to to automate your model railroad |BR| |BR|

* |EX-WT| - a simple web based controller for your command station
* |EX-TT| - an integrated, stepper based turntable controller running on an additional Arduino microcontroller via an I2C connection
* |EX-DCCI| -  a DCC packet sniffing tool
* |BSC| - the original DCC++ [#bcs]_  software, packaged in a stable release. (No active development, bug fixes only)

Our products are supported by many third party controllers and applications like |JMRI|, |Engine Driver|, |WiThrottle|, Rocrail and more

..
   .. table::
      :align: left
      :class: intro-table

      ==================   ==================   ====================
      |Timer|_             |Arrow|_             |Binder|_
      ------------------   ------------------   --------------------
      |Get Started|        |Download|           |Reference|
      ------------------   ------------------   --------------------
      |Lightning|_         |Question|_          |Puzzle|_
      ------------------   ------------------   --------------------
      |Advanced Setup|     |Support|            |Contribute|
      ==================   ==================   ====================

   .. |Timer| image:: ./_static/images/timer_bl.png
   .. _Timer: get-started/index.html
   .. |Get Started| replace:: :doc:`/ex-commandstation/get-started/index`

   .. |Arrow| image:: ./_static/images/download_bl.png
   .. _Arrow: download/index.html
   .. |Download| replace:: :doc:`Download </download/index>`

   .. |Binder| image:: ./_static/images/api_bl.png
   .. _Binder: reference/index.html
   .. |Reference| replace:: :doc:`/reference/index`

   .. |Lightning| image:: ./_static/images/advanced_bl.png
   .. _Lightning: advanced-setup/index.html
   .. |Advanced Setup| replace:: :doc:`/ex-commandstation/advanced-setup/index`

   .. |Question| image:: ./_static/images/question_bl.png
   .. _Question: support/index.html
   .. |Support| replace:: :doc:`/support/index`

   .. |Puzzle| image:: ./_static/images/puzzle_bl.png
   .. _Puzzle: contributing/index.html
   .. |Contribute| replace:: :doc:`Contribute </about/contributing/index>`

If you are just starting your journey with |DCC-EX| we recommend you look at our :doc:`Choose Your Comfort Level <levels>` which will help guide you through this web site.

----

|EX-CS-LOGO-SMALL| |EX-I-LOGO-SMALL| |EX-WT-LOGO-SMALL| |EX-R-LOGO-SMALL| |EX-TT-LOGO-SMALL| |EX-DCCI-LOGO-SMALL| |EX-BSC-LOGO-SMALL|

----

.. [#bcs] |EX-CS| is a :doc:`major rewrite <about/press/rewrite>` to the original |BSC| code. |br| If you are still using DCC++, we recommend that you move to |EX-CS|.  It will run on the same hardware.


.. toctree::
   :hidden:
   :maxdepth: 4

   levels
   ex-commandstation/index
   ex-installer/index
   ex-webthrottle/index
   ex-rail/index
   ex-turntable/index
   ex-dccinspector/index
   big-picture/index
   throttles/index
   download/index
   support/index
   reference/index
   projects/index
   about/index

..   advanced-setup/index
   roadmap/index
   site-map/index
   automation/index
   get-started/index
   big-picture/index
   turntable-ex/index
   donate/index
   press/index
   contributing/index
   developer-reference/index
