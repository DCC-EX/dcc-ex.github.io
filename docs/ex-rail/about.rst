.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-description.rst
|EX-R-LOGO|

*****************
About and History
*****************

|tinkerer| |engineer|

.. sidebar:: 

   .. contents:: On this page
      :depth: 1
      :local:

How It Works
============

A small amount of code in the Command Station, the |EX-R| executor, lets you write an automation script in the form of simple, easy to use text commands that it interprets and runs on your layout. You don't have to be a programmer and you don't have to learn code. You simply add your own myAutomation.h file in the same program you use to upload the Command Station Software to your Arduino (the Arduino IDE, PlatformIO, etc). This means that you already have all the tools you will need, and there is nothing else to download or install. The method of creating your script file is described in the next section.

.. note:: 
   :class: note-float-right

   The |EX-R| code is only included in the compilation of the Command Station if the compiler detects a “myAutomation.h” file. If you don't create that file, no extra space is wasted for something you don't use.

The |EX-R| code is surprisingly small and requires very little PROGMEM (memory that holds the program code) or SRAM (the runtime workspace that stores variables and things the program needs) to operate. However, you will still need a Mega for your CS; the UNO and Nano memory is simply too small to include EX-RAIL with the rest of the Command Station code.

EX-RAIL automation is *much* (perhaps 2 orders of magnitude) more time efficient than the code required to process incoming requests from an external automation processor, or the continuous polling of every sensor.

History - A note from the Author
================================

My original aim was to see if I could create an automated layout with lots going on, that didn't just run around in circles. Having looked at |JMRI| (briefly, I must say) and DCC-EX, I began to wonder whether I could actually make a simpler automation system, and run it entirely on the Arduino used for the |EX-CS|.

Some of the automation techniques I read about, using Jython scripts in JRMI, seem to require extensive programming skills and complex table configurations which appeared awkward to me, despite my years of programming in dozens of languages.

It seemed to me that basing an automation on block occupancy detection leaves a lot of complex technical problems to be solved… and wanting to be cheap, I didn't want to invest in a range of block occupancy detectors, or ABC braking modules, which are all very well on circular layouts, but not good at complex crossings or single line operations with passing places. Also, I didn't want the automation to be an obvious cycle of movements… some random timings and decisions need to be introduced so that two trains don't always arrive at the same place in the same order, nor go on the same journey in a predictable cycle.

By reversing the usual assumptions, I think I have a workable, extensible and cheap solution.

Because the original DCC++ used a software design inappropriate for internal automation, I had to start by rewriting the entire Command Station code and this became the |EX-CS|, so automation has been in the plan from the start.

- Chris Harlow

Why Can't I Put a Script on an SDCard?
======================================

From time to time, we are asked why we can't put automation scripts (the contents of a myAutomation.h file) on an SDCard or load it into EEPROM storage on the Arduino. This is not possible, and as you will see in the last paragraph of this section, would not provide much of a benefit. For you Engineers and advanced Tinkerers:

1) Being able to read an SD card on the Arduino platforms requires a significant amount of code because there is no operating system or file system which we would take for granted on a PC. We simply don't have enough free memory on an Arduino to hold that code. The same problems exist for using EEPROM.   

2) myAutomation.h is actually generating compiled code as an integral part of the Command Station. To have this file loaded separately at run time would require that the Command Station contained all the code necessary to read the file and interpret the contents. This would be a significant additional code burden on the Command Station (>1000 lines of code) and also require huge amounts of precious RAM to store the interpreted version of the file because it cannot be written into flash memory at run time.   

3) By compiling the code on your pc, you have the advantage of the vast majority of syntax errors being detected by the compiler (albeit somewhat opaquely) rather than having to move the SDCard to the Command Station before discovering an issue.   

4) The current implementation requires no additional PC code/tool download or installation. If you are able to setup your Command Station, you already have everything you need to add your myAutomation.

5) To implement an SD card solution requires a user to have access to the Command Station, which could involve climbing under their layout, opening the Command Station case if you have one, dismounting the motor shield to get access to the SDCard slot, potentially damaging the Command Station, the layout, or your body, etc. The card would have to be placed into a computer, an editor opened, the file edited and saved, and then the process reversed to get the SDCard back into the Command Station.

In contrast... with the current system: One takes the end of the USB cable that has been thoughtfully left connected to the Command Station and plugs it into ones laptop. The Arduino IDE (or suitable alternative) is opened and the myAutomation.h files is edited. A SINGLE CLICK on the upload button is sufficient to save the file, check it for errors, upload to the Command Station and restart the Command Station. 

As more powerful processors become available and affordable, we may find other ways to handle saving settings and adding automations, but the current method, as you can see, is efficient, easy to use, and fast.

