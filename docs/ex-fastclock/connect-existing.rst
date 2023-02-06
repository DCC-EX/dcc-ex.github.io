.. include:: /include/include.rst
.. include:: /include/include-l1.rst

|EX-FC-LOGO|

**********************
Configuration options
**********************

|tinkerer| |githublink-ex-fastclock-button2|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

If you already have a FastCLock |EX-FC| has a number of couple of configuration options which allow you to connect your own clock to a |EX-CS|.

The various configuration options are outlined below


Connecting your own FastClock
=============================


Connecting via Serial
---------------------

Connecting via Serial is the simplest option if available.  

* Run a dupont cable from the TX pin on the arduino to a RX pin on the EX-CommandStation.  It is not usually necessary to run a cable from RX to the TX on the EX-CommandStation as  the FastClock is not receiving data back.
* Find the Serial defines in the config.h file (or copy config.example.h to config.h if you dont have one), locate the following lines:
    
    .. code-block:: 

      //#define SERIAL1_COMMANDS
      //#define SERIAL2_COMMANDS
      //#define SERIAL3_COMMANDS
  
  and uncomment the appropriate one for the serial port you are using.
* Add the following code to your Setup() function:

.. code-block:: 
    
  Serial.begin(115200);
  while (!Serial) {
  ; // wait for serial port to connect. Needed for native USB port only
  }

* Include the following routine within your code:
  
  .. code-block:: 

    void SendTime(byte hour, byte mins, byte speed) {

      int itime = (hour * 60) + mins;
      char buffer[20];
      sprintf(buffer, "<JC %d %d>", itime, speed);
      Serial.println(buffer);

* Each time the time changes call the SendTime routine as follows:
  
  .. code-block:: 

    SendTime(HH, MM, clockSpeed);

  where HH = the hour, MM = minutes and clockSpeed = the fast speed (e.g. at spped 4, 15 seconds represents a minute).


Connecting via I2C
------------------

Connecting via |I2C| involves a HAL driver file to the |EX-CS| as well as adding some code to the existing FastClock code.  Follow the follwing steps:

* In the |EX-CS| code copy the file myHal.cpp_example.txt to myHal.cpp.
* Edit the file myHal.cpp and uncomment the following line near the beginning of the file
    
  //  #include "IO_EXFastClock.h"  // FastClock driver

* Uncomment the following line near the end of the file
  //  EXFastClock::create(0x55);
  0x55 (decimal 85) is the default address but needs to match that in the FastClock code (see below).
* Using Dupont connectors connect SDA/SCL/Gnd on the clock to SDA/SCL/Gnd on the |EX-CS|
* Include the following code in your Fastlock code:

  Near the top of the sketch:

  .. code-block:: 

    #include <Wire.h>


  Within your Setup():

  .. code-block:: 

    Wire.begin(I2CAddress);
    Wire.onRequest(TransmitTime);


  Add the following function within the sketch

  .. code-block:: 

    void TransmitTime() {
        // send the data over I2C
        // send the time as <mmmm> as two bytes followed by clockspeed
        int timetosend = (HH * 60) + MM;
        byte TimeArray[2];
      
        TimeArray[0] = (timetosend >> 8);
        TimeArray[1] = timetosend & 0xFF;
        Wire.write(TimeArray, 2);
        Wire.write(clockSpeed);      
    }
    

  In the function above  HH is the time as hours (24hr. clock) and MM is the minutes.
* The CommandStation-EX will now poll the FastClock to request the time.  The frequency at which it does so is influenced by the clockspeed (i.e. on a slow clock speed it polls less often).


Next Steps
==========

Now that you know how to connect your existing FastCLock, click the "next" button see how you use |EX-FC|.  

