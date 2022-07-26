.. include:: /include/include.rst
*********************************
DCC++EX 4.0 Release Announcement
*********************************

DCC-EX announces version 4.0 of its DCC++EX Command Station software with EX-RAIL automation and accessory control
==================================================================================================================================

*Operators can now have a fully automated model railroad or a separate accessory control bus for their entire layout and read CVs up to 8 times faster*

February 1, 2022 7am Eastern Standard Time


**Holly Springs, North Carolina USA** – DCC-EX released the next version of its popular free and open source DCC Command Station software today. Version 4.0 of DCC++EX includes the new EX-RAIL :sup:`tm` (Extended Railroad Automation Instruction Language) system that revolutionizes the way model railroaders can control and interact with their layouts. This new concept allows users to fully automate the operation of their trains and to manage turnouts, signals, lights, automations, animations, and virtually any kind of sensor, switch, servo, motor, or output, all with a very simple set of commands.

DCC++EX :sup:`tm` with EX-RAIL runs on inexpensive and readily available hardware like the Arduino and Teensy series of microcontrollers and supports standard switches, servos, and accessory boards.

Concurrent with this rollout, enhancements to the popular JMRI model railroad software and Engine Driver smartphone and tablet app integrate tightly with the new features. Operators can create routes or automation/animation sequences and have them appear as buttons in Engine Driver. Press a button to begin an automation, or drive trains manually and press a button to hand them off to EX-RAIL to run everything unattended. Take back control with another press of a button.

Users no longer have to search for “sketches” and libraries or learn complicated C++ programming. There is no need to modify the Command Station software and risk bringing the whole system down. The only file that needs to be modified is a myAutomation file where simple commands allow the operator to define their devices and tell them what to do when the conditions they specify are triggered. An engine can be sent out from the yard, triggering turnouts to engage for a specific route. Along the way, all the signals and crossings operate automatically in response to sensors along the track or timings or other conditions specified by the operator.

Animations that involve a sequence, like operating cranes, arc welders, station operations, trolleys, etc. are simple to script. To make it even easier, EX-RAIL comes with many standard sequences so that an operator just needs to copy them into their script, load the file into their Command Station and connect their devices. For the first time, everything can be run from the Command Station, without the need for separate devices running custom C++ programs scattered all over the layout.

Interfacing with hardware has never been easier with the new HAL (Hardware Abstraction Layer) feature. Supported hardware such as port expander and servo controller boards are automatically detected. New types of hardware can be added by implementing a driver from a standardized interface without having to write a custom program.

The new DriveAway :sup:`tm` feature allows users to drive an engine onto a siding or other electrically isolated block used as a programming track. The engine can be programmed and then driven back onto the main section of the layout, all without touching the locomotive.

DCC++EX has enhanced capabilities to read difficult decoders, provide detailed diagnostics to avoid the dreaded “308 Error”,  and when using JMRI with CV values matching what is in the its decoder file, improve performance by a factor of 8x. Reading and writing CVs in general, whether using JMRI or another method, is still significantly faster than before.

DCC-EX is a global joint effort of a group of developers and engineers located in the US, UK, Sweden, France, Australia, New Zealand, and India. For more information visit their website at https://www.dcc-ex.com.

| Contact info:
| Name: Fred Decker
| Organization: DCC-EX
| Address: 113 Main Street #767, Holly Springs, NC 27540
| Phone: +1 919-285-1576

`PDF version of this pressser for download </_static/documents/press_release_v40.pdf>`_