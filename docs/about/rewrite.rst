
*************************
What's New in DCC++ EX?
*************************

Everything you loved is still there
=====================================

First, we want to stress that we didn't break anything! Whether you are using JMRI as a controller/front-end to send commands to your track, handle turnouts or read and write CVs, or any using any other software or the serial monitor, the commands are still the same. We have expanded the API (Application Programming Interface) to add new commands and provide new responses, but they won't affect your old control methods. One example of a new command is the one to handle turning power on and off to individual tracks.

DCC++ EX is all new!
=====================

While we made minor changes to the original DCC++ "BaseStation-Classic", all new development is going forward with DCC++ EX. At first, we expanded features, added functionality and fixed bugs by working from the existing code base. The updated "Classic" release of DCC++ will be familiar to any of you who played with the code. However, we want to stress that the next release, DCC++ EX, is a complete re-write from the ground up and is greatly improved.

What's different?
===================

We started with the DCC Signal Generation code, what we call the "Waveform Generator". We got together as a team and looked at how we could make it better. It soon became clear that rather than make piecemeal changes, the entire concept of how the signal could be generated and how to use timers and interrupts would need to be re-imagined. This not only sped things up considerably, but allowed us to allow you to connect some shields right on top of your Command Station board without jumpers!

Next we focused on packet generation. We looked at the complexities of reading and maintaining code that was using binary math, multiple "registers" to hold train data, and doing bit shifting everywhere to build bytes and stuff them into data packets. The new method gets rid of the old registers and simplifies the whole structure for building packets. Things like start and stop bits and preamble bits are static pieces of information. Do being able to just insert them where they need to go saves time and processor bandwidth.

We created an internal API for how modules communicated with each other. So the code is more modular and each unit is dedicated to its specific task.

We completely re-wrote current sense and ACK detect routines to better protect your trains and make programming more accurate. There are complete diagnosicts to allow you see see exactly why a particular decoder is not reading or writing and provides settings to get it to work in most cases.

We added many functions like individual track power control, user add-on functions, a much simpler Function (F0-28) command, extended functions up to 68, better turnout handling, built in support for the LCN accessory bus, WiThrottle compatibility, support for more motor controllers, LCD and OLED display support, WiFi, Ethernet, Bluetooth, an easy to use Installer, Nano and Teensy support, new DCC++ EX features added to JMRI, custom add-ons for Engine Driver, and so much more.

Why did we do this?
====================

First and foremost, we just wanted to have fun. We saw an engineering problem and we wanted to tackle it. Second, we saw an opportunity to provide something really amazing to the Model Railroad Community for low cost and that worked as well or better than anything on the market.

To Make Engineer's Propellers Spin
====================================

.. image:: ../_static/images/engeneer.png
   :

We needed a platform that would allow us to grow into the future. The first thing we found was that in order to allow easy changes and to be able to adapt to technology we might want to use going forward, the code needed to be more modular. Each unit needed to be a "black box" that either did just one task and do it well, or take input and generate output without having to know anything about the module it was communiating with. Therefore, we created an interal API through which the modules could communicate. By simply unplugging one unit and plugging in another we could continue to work using a differnt devices. An example of this is input and output. It doesn't matter whether JMRI is sending commands to DCC++ EX or if it is a wireless Cab Controller. It doesn't matter if the output device is the serial monitor or an I2C display. It doesn't matter if you want to use a serial port or a network device to route data. This makes it very easy to implement new features with new devices. We just have to create a small interface for whatever new device we want to implement. This has the side benefit of allowing the code to be more readable.

Next, the Waveform Generator needed 2 timers and interrupts, one for the Main track signal and one for the Programming track. The Uno only has 3 timers. So 2 of them were already tied up for sending the DCC signal. Since the programming track sits idle most of the time, and both signals were always being generated to the input of the motor board, processing power was being wasted that could be put to use for something else. In addition, because of the way the Arduino is designed, we were forced to use jumpers to connect pins on the Arduino to those on the motor board. Our new design eliminates the need for jumpers!

The packet generation routine was complex, hard to maintain, and limited us with regard to the hardware we could run on and new features we could implement (like the Railcom cut-out). We replaced the slow DigitalRead() and DigitalWrite() routines with a fast write library. The packet generation is now streamlined, fast (which allows us to be able to use on only 1 timer to create signals for 2 tracks), and much easier to read.

The 3 most requested features were: 1. More reliable CV read and writes, 2. Railcom cut-out, 3. Automation. We haven't limited ourselves to just these features, but we put a lot of time into redesigning things to accomodate them. 

The current detection routines are completely different. One key difference is all current readings are in milliAmps instead of meaningless pin readings. So if you want to set your overload protection to kick in at 3 Amps, you just enter 3000 for 3000 milliAmps instead of looking up a value from a table.

We are still testing all the motorboard and Arduino combinations at different voltages to refine our current readings. This is important because we want to have accurate and fast short-circuit detection, and because the reason CV reading was occasionally unreliable in the past was due to not always sensing a current pulse on the track. In addition to more accurately reading current, we had to completely change the way we look for an "ACK" (acknowledgement from the train that it received a command). So we now check immedately after we send a command instead of waiting for a dozen or more packets. This means we don't miss an ACK while this is happening and we jump out of sending uneccessary packes as soon as we get one. We also use our knowledge of CVs and the probability of what a CV may contain, so save time by skipping ahead if our first guess is correct. You will appreciate how much faster we can read CVs now!

We not only are working on a RailCom cutout within the Command Station, but are developing a way of reading the RailCom data and reporting it.

Automation
===========

EX-RAIL (Extended Railroad Automation Interface for Layouts) brings new capability to the world of automation. You don't have to be a programmer to write a script that tells a train to start moving forward at a set speed until some action (like reaching a sensor) occurs. We will be providing a document and tutorial on EXRAIL once Beta testing is complete. This will be an open-ended project since who knows what people will come up with they want to automate. It will be easy to extend the commands to handle whatever your imagination can dream of.

The bottom line
=================

So while maintaining proper deference to Gregg Bermann's original concept of an inexpensive Command Station based on the Arduino platform, we don't want to do a disservice to DCC++ EX or develpers like Chris Harlow (UkBloke) and Dave Cutting who brought a new vision to the project and who used very little of the original code. This is NOT DCC++ v2.0, this is a completely new, yet API and feature compatible Command Station. And just a tease: What Command Station would be complete without a wireless Cab Controller that speaks DCC++? Keep looking at our web page for new announcments.

Thanks
=======

This is a team effort. There are a dedicated and organize group of about 15-20 core people involved in the project. In addition, there is all of you who contribute with your comments, feature ideas, evangelizing and testing. So we give you our heartfelt thanks. We will see you online!

Click here for `The DCC++ EX Team Credits <index.html>`_

Fred Decker
October 2020 
