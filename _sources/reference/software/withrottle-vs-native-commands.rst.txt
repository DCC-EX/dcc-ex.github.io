.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-reference.rst
|EX-REF-LOGO|

*********************************************
WiThrottle Protocol VS DCC-EX Native Commands
*********************************************

|SUITABLE| |engineer| |support-button|

.. sidebar:: 
   :class: sidebar-on-this-page

   .. contents:: On this page
      :depth: 2
      :local:

|EX-CS| supports both the **WiThrottle protocol** and the **DCC-EX Native protocol / commands**.

This page describes the difference between the **WitThrottle Protocol** and the **DCC-EX Native protocol / commands**.

|HR-DASHED|

WiThrottle
==========

'WiThrottle' is a trademark owned by Brett Hoffman. 

'WiThrottle' is also an `iOS app <https://www.withrottle.com/html/home.html>`_ developed by Brett Hoffman which has similar capabilities to |Engine Driver|. 

The 'WiThrottle protocol' is a communications protocol developed by Brett Hoffman.  It is used by |JMRI|, |Engine Driver|, the WiThrottle app and a number of other apps and DCC Command Stations. 

WiThrottle Servers
------------------

WiThrottle stands for 'WiFi Throttle', and a 'WiThrottle Server' is just software running on your |JMRI| computer, DCC-EX EX-CommandStation, or dedicated device. It's called a 'Server' because it allows you to connect to it and it 'serves', or services, requests from another application. That application is called a 'Client'.

The |WITHROTTLE PROTOCOL| itself is a standard for how WiFi throttles can communicate with the WiThrottle Server, much like the DCC standard is a standard for how data packets communicate with decoders. What this means for you, is that |Engine Driver| and other apps can talk to any WiThrottle compatible server, which in turn can talks to your DCC encoders in your locos.

|HR-DASHED|

DCC-EX Native protocol / commands
=================================

When the |DCC-EX| team designed the **DCC-EX** |EX-CS| they found the |WITHROTTLE PROTOCOL| too limiting and came up with a new protocol referred to originally as **DCC++** but later as :doc:`DCC-EX Native Protocol or DCC-EX Native Commands </reference/software/command-summary-consolidated>`.

|Engine Driver|, |EX-WT|, |JMRI| and a few other apps can use the more powerful **DCC-EX Native Protocol** when connecting to a **DCC-EX** |EX-CS|.

|Engine Driver| can also use the **DCC-EX Native Protocol** to connect to a **DCC-EX** |EX-CS| via |JMRI| but you need to enable the **'DCC++ over TCP Server'** in the **'DCC++'**' menu in **Decoder-Pro**.

----

Which Should You Use?
=====================

The **WiThrottle Protocol** is adequate for running trains, throwing turnouts/points and selecting Routes.

What the **WiThrottle Protocol** can't do is *CV programming*, *Track Manager changes*, and *system configuration*.

The **DCC-EX Native Commands** can do these and more.

So if you have the option to use a controller that uses the **DCC-EX Native Commands** it is worthwhile doing so.  However if you can't then the **WiThrottle protocol** is just fine for running the average layout.

You can refer the :ref:`throttle/controller table <throttles/index:table - throttles by technology>` to see which controllers support **DCC-EX Native Commands**.