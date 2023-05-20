.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-REF-LOGO|

*************
I2C Displays
*************

|tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:


|EX-CS| is designed to accommodate a display. You don't need a display since the Control Station is often hidden away under the layout. However, if you like the idea of a nice visual display for your panel, just about any |I2C| (serial to parallel interface) display will work. We recommend either a 20 character by 2 line or 4 line display. The code is easily configurable in order to change the display settings, as well as add or change what is printed on the display.

.. image:: /_static/images/display/I2C_LCD_Display_wired.jpg
  :alt: Example: 4 line |I2C| Display
  :scale: 80%

We currently support LCDs based on the PCF8574 backpack:

* 16 column by 2 row (16x2) and 20 column by 4 row (20x4) LCD displays 
* .96" and 1.3" OLED displays.

.. NOTE:: Do NOT modify any code related to displays without contacting us. We use our own included code, NOT an external library you have to download. The code was written to support LCD and OLED displays and to fit on a Mega *and* an Uno. It has a custom font table and the LCD macro works to output diagnostics even if there is no display. If your display is not supported, let us know and we can take a look.

The LCD displays require a "backpack" that converts the raw display to |I2C|. |I2C| allows us to use just 2 lines (SDA (serial data) and clock (SCL)) to send text to the display. Without this board, we wouldn't have enough pins, especially on an Uno, to use a display. 

.. warning:: You MUST make sure to order TWO (2) parts for your LCD Displays. You need the display AND a backpack based on the PCF8574 controller chip. Some displays come with this already soldered together. Make sure before you buy!

Examples of compatible displays
================================

Here is an example of a 20 x 4 LCD screen. They come in different colors like blue and green. The controller board (backpack) is shown before soldering it to the back of the display. Soldering is very simple since you just match the two boards together and quickly solder the pins. Though there are 16 of them.


.. image:: /_static/images/display/lcd_20x4_backpack.jpg
  :alt: 20 x 4 LCD
  :scale: 80%

20 x 4 LCD with backpack

And here is an example of a 16 x 2 Display with its backpack sitting above it. Remember to either order a display with the backpack already soldered or two order both pieces from your vendor and solder it yourself:


.. image:: /_static/images/display/lcd_16x2_backpack.jpg
  :alt: 16 x 2 LCD
  :scale: 80%

16 x 2 LCD with backpack

Connecting an LCD Display
==========================

Soldering on the Backpack (if you purchased separate pieces)
------------------------------------------------------------

And here is a picture of the board after soldering or if you purchase a board already soldered (or "welded" as some of the Chinese sites call it)


.. image:: /_static/images/display/lcd_soldered.jpg
  :alt: Backpack Soldered to LCD
  :scale: 80%

LCD with backpack soldered to the back

Connecting the Jumper Wires
---------------------------

To connect the Display to the Command Station, you will need 4 male to female jumper wires:

#. Connect a wire from +5V on the Motor Shield or WiFi Board to Vcc on the backpack
#. Connect a wire from Gnd on the Command Station to Gnd on the backpack
#. Connect SDA on the Arduino (pin 20 on the Mega, pin 16 on the Uno) to SDA on the backpack
#. Connect SCL on the Arduino (pin 21 on the Mega, pin 17 on the Uno) to SCL on the backpack

.. Note:: Look closely on the Uno or Mega for markings, including on the inside or outside of the black header. SCA and SCL are usually clearly labeled.

Upload the sketch to your CS
----------------------------

To upload the new sketch on your Command Station

#. Open the Arduino IDE
#. Open the CommandStation-EX project
#. Open the config.h file (If you haven't renamed config.example.h to config.h do this now)
#. Find the line that says: ``// define LCD_DRIVER for i2c LCD address 0x3f,16 cols, 2 rows
   #define LCD_DRIVER  0x3F,16,2`` 
#. make sure to uncomment this line if it has 2 slashes in front of it by removing them.
#. Find the 4 characters that start with ``0x`` and add the address for your |I2C| backpack after it. We default to 3F, but your display may be 27. The text would read ``0x27`` if that was the case.
#. In the next field, enter the number of columns in your display. The default is 16. If you have a 20 column display, enter that instead.
#. In the last field, enter the number of rows in your display. We default to a 2 row display. If you have a 4 row display, change this to 4.
#. Save the file
#. Make sure to connect the Arduino to your computer with the USB cable and click the upload button to compile and upload the updated Command Station sketch.

Connecting an OLED display
===========================

OLED displays come in more varieties than LCD displays. The library to run them also takes more memory. Therefore, OLED displays won't work with an UNO and you will require a Mega. Here are some examples of OLED displays:


.. image:: /_static/images/display/adafruit_96in_oled_sm.jpg
  :alt: Adafruit .96" OLED
  :scale: 80%

Adafruit .96" OLED Display


.. image:: /_static/images/display/makerfocus_oled_sm.jpg
  :alt: Makerfocus OLED Display
  :scale: 80%

Makerfocus 128x32 .91" OLED Display

Soldering Wires to the Display
------------------------------

For any of these boards you can buy male header pins (either straight or 90 angle) and solder them to the display to then use jumper wires, or you can solder your wires directly to the holes on the board.

Connecting to your EX-CommandStation
------------------------------------

Physically connecting an |I2C| OLED display to your |EX-CS| is relatively straight forward, with SDA connecting to the CommandStation's SDA pin, SCL to SCL, VCC to 5V, and GND to GND.

.. image:: /_static/images/display/mega-with-i2c-oled.png
  :alt: Mega2560 with |I2C| OLED
  :scale: 30%

You can also connect the display to the motor shield's |I2C| headers.

.. image:: /_static/images/display/mega-with-i2c-oled-twi.png
  :alt: Mega2560 with |I2C| OLED
  :scale: 30%

Configuring the software for an OLED
------------------------------------

To enable an OLED display with your |EX-CS|, you need to make some edits to your "config.h" file and then upload the software again.

Look for the LCD section in "config.h" which looks like this:

.. code-block:: cpp

  /////////////////////////////////////////////////////////////////////////////////////
  //
  // DEFINE LCD SCREEN USAGE BY THE BASE STATION

Make sure any line beginning with ``#define LCD_DRIVER`` is commented out by adding ``//``.

You will need to know if your OLED has a 128 x 64 or 128 x 32 pixel resolution, and add the appropriate line:

.. code-block:: cpp

  #define OLED_DRIVER 128,32      // Define for 128 x 32 displays
  #define OLED_DRIVER 128,64      // Define for 128 x 64 displays

Combine IP address and port on OLED
===================================

|tinkerer| |engineer|

To use OLED displays with your |EX-CS|, you can save line LCD5 used for the port number and combine it with line LCD4 IP address.

Be aware that the combined IP address and port number can easily exceed 20 characters, which will exceed the display width.

To accomplish this, you will need to edit "WifiInterface.cpp" included with the |EX-CS| software. Each time you want to upgrade the software, you will need to repeat this edit.

In "WifiInterface.cpp", you need to locate the ``LCD(4...)`` line (should be around line #313):

.. code-block:: cpp

  LCD(4,F("%s"),ipString);  // There is not enough room on some LCDs to put a title to this

Comment out this line by adding ``//`` at the beginning, and add this new line immediately below:

.. code-block:: cpp

  // LCD(4,F("%s"),ipString);  // There is not enough room on some LCDs to put a title to this
  LCD(4,F("%s:%d"),ipString,port); // *** Single IP:Port

You will also need to comment out the ``LCD(5...)`` line by adding ``//`` to the beginning (should be around line 317):

.. code-block:: cpp

  // LCD(5,F("PORT=%d"),port);

Once this is done, line 5 onwards are free to use as you wish.

If you have custom messages you wish to display, you can do this by adding the lines to "mySetup.h":

.. code-block:: cpp

  LCD(5,F("Line 5 custom text"));
  LCD(6,F("Line 6 custom text"));
  LCD(7,F("Line 7 custom text"));