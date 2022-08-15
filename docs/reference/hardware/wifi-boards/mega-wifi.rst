.. include:: /include/include.rst
.. include:: /include/include-l3.rst
|EX-CS-LOGO|

**************************************
Mega+WiFi Combo Board
**************************************

|conductor| |tinkerer| |engineer|

.. figure:: /_static/images/assembly/mega_wifi.png
   :alt: Mega WiFi
   :scale: 40%
   :align: center

The Mega+WiFi is a board from China that combines an Arduino Mega design with an on-board ESP8266 WiFi chip. The advantage of this configuration is that with WiFI on the same board with the Microcontroller, you only need two boards. Your "stack" will have just the Mega+WiFi board with the Motor Shield on top. The disadvantage is that you will have to "flash" (upload new firmware) to the ESP chip on the board. This requires a computer, downloading a flash tool and a zipped data file, setting some switches, connecting the Mega+WiFi to the computer with a USB cable, and uploading the new firmware. A |Conductor-text| should be able to follow the instructions, but Tinkerers may feel more comfortable. It takes about 15-20 minutes from start to finish (read, download, unzip, flash, done). Click on the link below for detailed instructions on exactly how to configure and use a Mega+WiFi board.

:doc:`/reference/hardware/microcontrollers/wifi-mega`
