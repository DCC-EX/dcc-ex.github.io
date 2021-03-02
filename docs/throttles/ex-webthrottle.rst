**********************
DCC++ EX Web Throttle
**********************

This is a new DCC++ EX Throttle/Controller that can connect to the DCC++ EX Commmand Station directly through the USB port of a computer.

For a video on how to install and use WebThrottle-EX click below.

   .. raw:: html
   
      <iframe width="336" height="189" src="https://www.youtube.com/embed/BkgsEOjxWaU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

What you need to run WebThrottle-EX
====================================

* Chromium-Based Browser version 80 or above
  (Chrome, Opera, Edge)
* You must enable the experimental Web Serial API

You don't need anything else to test it out and to run in emulator mode, just run it and play. To use it to run real trains you will need:

* An Arduino Mega or Uno Microcontroller
* An Arduino Motor Control Shield
* The DCC++ EX Command Station sketch loaded on your Arduino


Getting started
=================

First, you must enable the Web Serial API, in your browser URL bar type:

.. code-block::

   chrome://flags


If you are using a different Chromium browser, substitute your browser name for chrome (ex: edge://flags).

Then set the **#enable-experimental-web-platform-features** flag by looking on the page for "Experimental Web Platform Features" and click on the "enable" button.


.. note:: If you don't have your hardware yet or just want to play with the throttle and see commands being sent to the log window, you can skip the part about connecting your Command Station.

To get started, connect your Command Station to a computer that has a USB port and have a compatible browser installed. Use a USB serial cable from your computer to the USB connector on the Arduino. Power everything up and put a loco on the MAIN track.

Run or Install WebThrottle-EX
==============================

You have an option for how you would like to run WebThrottle-Ex, from the cloud or installed locally on your machine. We recommend using it from the cloud or as a web app, but the choice is yours.

Try it now (Run from the cloud)
=================================

Just click this link and you will load a web page from our server that will run the web throttle on your machine. You can connect it to DCC++ EX or just run it in emulator mode where you don't have to have any hardware. Please read the requirements above for what you need in order to run exWebThrottle in your browser. If you want to remember the link to run the throttle, it is https://dcc-ex.github.io/WebThrottle-EX.

.. raw:: html 

  <p><a class="dcclink" href="https://DCC-EX.github.io/WebThrottle-EX">Try It Now</a></p>

WebThrottle-EX is also a Progressive Web App (PWA). That means you can install it on your computer and run it right from your start menu! If you go into the WT-EX settings panel (click the 3 line "hamburger menu" at the top left), you will find a "Settings" menu. Click on "Apps" and then select "Install as an App". You can now work offline and always find WebThrottle-EX with your other Apps!

Download
==========

This will install all the files to run locally on your machine. You won't need an internet connection to run the software. Just download the latest zip file from the link below and extract it to any folder you have run permission on. Then click on the index.html file to launch the throttle in your browser. Create a shortcut to it on your desktop so you can launch it more easily.

.. raw:: html 

  <p><a class="dcclink" href="https://github.com/DCC-EX/WebThrottle-EX/releases"> Download</a></p>

.. note:: We recommend using the version hosted on our servers as this will auto-update whenever we release a new update!


Operation
==========

To use the program, you can either click on the "Serial" dropodown button and select "Emulator" to run in emulator mode or after making sure your hardware is properly connected, select "Serial".

Next, click on the "Connect DCC++ EX" button. 

If you are in "emulator mode", you can skip to the next step. When using the serial connection, if the program finds a compatible device, it will open a popup a window showing you a selection. It may show a line at the top such as "Arduino Mega 2560 (COM3)". Your com port may vary. Click on your board to select it and then click the "Connect DCC++ EX" button.


.. raw:: html

   <insert pic here>



You should then be connected to the Command Station (CS) and should see the response from the CS in the log textbox of the debug console at the bottom of the throttle window. Make sure your debug console is open. If it isn't, use the slider button in the lower left to open it. You can also open the DevTools window in your browser to see more developer logging.


.. raw:: html

   <insert pic here>



Once you are connected, you can enter the ``<s>`` command in the "direct command" textbox to get status information from your Command Station. To do this just enter ``s`` (without the quotes) and press the SEND button. You can send any DCC++ API command in this way. You should see <iDCC++...> returned in the log window with your version, type of arduino, type of motor shield, and some other information.


.. raw:: html

   <insert pic here>



Now you are ready to run trains! Place your loco on the track and click the power slider button to turn on power to your track. You should see lights on your Arduino Motor Shield and an indication that your loco has power.

.. note:: Make sure you place the loco on the MAIN track, not the PROGRAM track. Check your wiring. On an Arduino Motor Shield, Motor Output "A" should connect to your MAIN track and "B" to the PROGRAM track.

Next go to the "Locomotive ID" textbox and enter the address of your loco and press the "Acquire" button. You should now have full control over your loco.


.. raw:: html

   <insert pic here>



All the function buttons should be working, so you can play with the headlight, horn and bell and any other function assigned to a function button. The commands being sent to the CS and its responses will display in the log window if it is open

In the throttle control area to the left of the function buttons are vertical controls to control direction. The up arrow selects forward, the square button is stop and the down arrow is reverse.


.. raw:: html

   <insert pic here>



The circular control or vertical slider (chosen by the throttle select slider) can be moved by clicking and holding down the mouse button and dragging, clicking at a spot where you want the throttle to move, or clicking the + and - buttons.


.. raw:: html

   <instert throttle select pic here>



The options button lets you save labels to go on your function buttons for each of your locos. We will be updating this document soon to give you more information on this and other new features.

.. note:: Not all CS functions are fully supported in the emulator yet. This means that although the software works, not all the responses will be shown in the debug console. This will be completed in a next release.


Going Further / Developing
===========================

If you want to really delve into how this works and help us improve it with your comments or your development skills, please contact us.

To load the Chrome DevTools to look at logging and be able to manually enter "write" commands for testing, click on the Menu (the 3 vertical dots in the upper right hand corner of the Chrome Window), then select "more tools" and then "Developer Tools". Or you can just hit "Ctrl-Shift-I".

License
========

Copyright 2020 DCC-EX

Licensed under the GNU open source licese.

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

`DCC-EX <https://dcc-ex.com>`_
