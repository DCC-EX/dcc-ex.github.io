.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/throttles.rst
   
**********************************************
TCS UWT-50 & UWT-100 WiFi Throttles (Physical)
**********************************************

|conductor| |tinkerer| |engineer|

Train Control Systems (TCS) makes a nice line of physical tactile hardware based controllers. 
Since they support the |WiThrottle protocol|, they work seemlessly with the |EX-CS|. 
Recently preliminary testing on both the UWT-50 and the UWT-100 WiFi Throttles are very encouraging.

Some of the major benefits of |EX-CS| for TCS UWT-Throttle users are;

* Direct WiFi connection of TCS UWT-Throttles to the |EX-CS|.
* |WiThrottle protocol| built into DCC-EX EX-Command Station giving access to all the EXRAIL macro scripts.  No JMRI connection required
* EXRAIL macros run on the Command Station and do not need a PC connected in order to operate engines and accessories on the layout.
* JMRI WiThrottle Server Protocol compliant
* JMRI Routes can be created to point to existing EXRAIL macros residing on DCC-EX  and be run through the WiThrottle Server connection
* EXRAIL scripts are simpler more powerful & easier to write than JMRI Jython/Python.py scripts.
* Both DCC & DC Layouts can use TCS UWT-WiFi Throttles and other smartphone WiFi Throttle Apps together with DCC-EX and our new TrackManager.


.. figure:: /_static/images/throttles/uwt50_a.png
   :alt: UTW-50 Throttle
   :scale: 70%

   UTW-50 Throttle

On the first screen, press the menu button:

.. figure:: /_static/images/throttles/uwt50_1.jpg
   :alt: UTW-50 Network Options
   :scale: 30%

   WiTcontroller connection diagram

From the main menu scroll down or press 6 for Network Options:

.. figure:: /_static/images/throttles/uwt50_2.jpg
   :alt: UTW-50 Saved Networks 
   :scale: 30%


From the Network Options menu, select 2 for Saved Networks:

.. figure:: /_static/images/throttles/uwt50_3.jpg
   :alt: UTW-50 select DCCEX
   :scale: 30%

   UTW-50 select DCCEX

Scroll through the list and select the one that begins with DCCEX:

.. figure:: /_static/images/throttles/uwt50_4.jpg
   :alt: UTW-50
   :scale: 30%

   UTW-50

The |EX-CS| has the ability to automatically upload EXRAIL Automation, Routes & Command macros to the TCS UWT-Throttles.

Examples of UWT-100 Throttle and DCC-EX |EX-CS| in action;


DCC-EX Commands Cmd Power On|Off, and Join Programming Track < == > Main line, and DCC-EX Turnout Control

.. figure:: /_static/images/throttles/uwt100_join.jpg
   :alt: UTW-100 Join
   :scale: 100%

   UTW-100 Join

.. figure:: /_static/images/throttles/uwt100_turnout.jpg
   :alt: UTW-100 Turnouts/Points
   :scale: 70%

   UTW-100 Turnouts/Points

.. figure:: /_static/images/throttles/uwt100_roundhouse.jpg
   :alt: UTW-100 Roundhouse
   :scale: 70%

   UTW-100 Roundhouse


DCC-EX Cmd to Pause & Resume EXRAIL macro scripts, and DCC-EX Cmd to Reboot Command Station

.. figure:: /_static/images/throttles/uwt100_resume.jpg
   :alt: UTW-100 Resume
   :scale: 70%

   UTW-100 Resume

.. figure:: /_static/images/throttles/uwt100_reboot.jpg
   :alt: UTW-100 Reboot
   :scale: 70%
  
   UTW-100 Reboot
  
Visit the TCS website here:
 https://tcsdcc.com/uwt-50 

 https://www.tcsdcc.com/uwt-100 
