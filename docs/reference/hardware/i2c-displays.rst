I2C Displays
============

DCC++ EX is designed to accommodate a display. You don't need a display since the Control Station is often hidden away under the layout. However, if you like the idea of a nice visual display for your panel, just about any I2C (serial to parallel interface) display will work. We recommend either a 20 character by 2 line or 4 line display. The code is easily configurable in order to change the display settings, as well as add or change what is printed on the display.

.. image:: ../../_static/images/display/I2C_LCD_Display_wired.jpg
   :alt: Example: 4 line I2C Display
   :scale: 80%

We currently support:

* 16 column by 2 row (16x2) and 20 column by 4 row (20x4) LCD displays 
* .96" and 1.3" OLED displays.

The LCD displays require a "backpack" that converts the raw display to I2C. I2C allows us to use just 2 lines (SDA (serial data) and clock (SCL)) to send text to the display. Without this board, we wouldn't have enough pins, especially on an Uno, to use a display. 

Examples of compatible displays

.. warning:: You MUST make sure to order TWO (2) parts for your LCD Displays. You need the display AND a backpack based on the PCF7584 controller chip. Some displays come with this already soldered together. Make sure before you buy!

Connecting an LCD Display
-------------------------

Here is an example of a 20 x 4 LCD screen. They come in different colors like blue and green. The controller board (backpack) is shown before soldering it to the back of the display. Soldering is very simple since you just match the two boards together and quickly solder the pins. Though there are 16 of them.


.. image:: ../../_static/images/display/lcd_20x4_backpack.jpg
   :alt: 20 x 4 LCD
   :scale: 80%

**Figure 1** - 20 x 4 LCD with backpack

And here is an example of a 16 x 2 Display with its backpack sitting above it. Remember to either order a display with the backpack already soldered or two order both pieces from your vendor and solder it yourself:


.. image:: ../../_static/images/display/lcd_16x2_backpack.jpg
   :alt: 16 x 2 LCD
   :scale: 80%

**Figure 2** - 16 x 2 LCD with backpack

Soldering on the Backpack (if you purchased separate pieces)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

And here is a picture of the board after soldering or if you purchase a board already solderd (or "welded" as some of the Chinese sites call it)


.. image:: ../../_static/images/display/lcd_soldered.jpg
   :alt: Backpack Soldered to LCD
   :scale: 80%

**Figure 3** - LCD with backpack soldered to the back

Connecting the Jumper Wires
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To connect the Display to the CS, you will need 4 male to female jumper wires:

#. Connect a wire from +5V on the Motor Shield or WiFi Board to Vcc on the backpack
#. Connect a wire from Gnd on the CS to Gnd on the backpack
#. Connect SCL on the Arduino (pin x on the Mega, pin x on the Uno) to SCL on the backpack
#. Connect SDA on the Arduino (pin x on the Mega, pin x on the Uno) to SDA on the backpack

Installing the Software (LCD)
-----------------------------

There are two steps to install the software:


* Install the LiquidCrystal I2C library
* Edit the config.h file and upload the sketch to your CS

Install the library
^^^^^^^^^^^^^^^^^^^

To install the library, open the Arduino IDE and do the following:


#. Select Tools -> Manage libraries
#. Wait for the download to finish updating the list of libraries
#. In the "Filter your search..." box, type "liquidcrystal_i2c"
#. Scroll down the search results until you find the ``"LiquidCrystal_I2C by Frank Brabander"`` entry. Click on that library to select it
#. Click "Install"
#. Wait for the installation to finish.
#. Click "Close"

Once the library is installed on your computer, you don't have to install it again.

Upload the sketch to your CS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To upload the new sketch on your Command Station


#. Open the Arduino IDE
#. Open the CommandStation-EX project
#. Open the config.h file (If you haven't renambed config.example.h to config.h do this now)
#. Find the line that says: ``// define LCD_DRIVER for I2C LCD address 0x3f,16 cols, 2 rows
   #define LCD_DRIVER  0x3F,16,2`` 
#. make sure to uncomment this line if it has 2 slashes in front of it by removing them.
#. Find the 4 characters that start with ``0x`` and add the address for your I2C backpack after it. We default to 3F, but your display may be 27. The text would read ``0x27`` if that was the case.
#. In the next field, enter the number of columns in your dispay. The default is 16. If you have a 20 row display, enter that instead.
#. In the last field, enter the number of rows in your display. We default to a 2 line display. If you have a 4 line display, change this to 4.
#. Save the file
#. Make sure to connect the Arduino to your computer with the USB cable and click the upload button to compile and upload the updated Command Station sketch.

Connecting an OLED display
--------------------------

OLED displays come in more varieties than LCD displays. The library to run them also takes more memory. Therefore, OLED displays won't work with an UNO. You will require a Mega. Here are some examples of OLED displays:


.. image:: ../../_static/images/display/adafruit_96in_oled_sm.jpg
   :alt: Adafruit .96" OLED
   :scale: 80%

**Figure 4** - Adafruit .96" OLED Display


.. image:: ../../_static/images/display/makerfocus_oled_sm.jpg
   :alt: Makerfocus OLED Display
   :scale: 80%

**Figure 5** - Makerfocus 128x32 .91" OLED Display

Soldering Wires to the Display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For any of these boards you can buy male header pins (either straight or 90 angle) and solder them to the display to then use jumper wires, or you can solder your wires directly to the holes on the board.

Connecting Jumper Wires to the CS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

** Not Finished. Coming soon! **

Installing the Software (OLED)
------------------------------

** Not Finished. Coming soon! **

Changing the I2C Address
------------------------

If you have other I2C devices, like an I2C bus to control turnouts or other accessories, you may need to change the address of your I2C display to avoid a conflict. The display should have instructions available for how to do this.

** Not Finished. Coming soon! **
