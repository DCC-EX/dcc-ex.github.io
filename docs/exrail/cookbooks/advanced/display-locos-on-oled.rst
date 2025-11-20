.. include:: /include/include.rst
.. include:: /include/include-l3.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**************************************
Display Loco speeds on OLED (Advanced)
**************************************

|SUITABLE| |tinkerer| |engineer| |support-button|

The following example creates a C++ function to display loco details on an OLED screen. By using a generic HAL driver, the function can be invoked repeatedly according to a time delay.

**BEWARE** that code like this is sensitive to many restrictions such as time taken and memory use. It is also subject to version changes in some of the internal dcc-ex routines so is only given here as an example.

|EX-R| macros cannot be used inside STEALTH sections. Users using ``STEALTH`` and ``STEALTH_GLOBAL`` are expected to understand the implications and the C++ language features used and the need to avoid any lengthy process.

The ``STEALTH_GLOBAL`` macro allows the creation of C++ functions within the command station environment.
This function displays the first 8 locos in the DCC speed reminders table on LCD/OLED screen 2.

Notice that it will only update one OLED row per call, and will not update the row if the speed byte has not changed. This is because OLED updates are very "expensive" in terms of cpu time and |I2C| traffic volumes and attempting to do too much in one call can cause blocking of other more important functions.

.. code-block:: cpp

    STEALTH_GLOBAL(
      void updateLocoScreen() {
        const byte loco_slots=8;
        static byte current_slot=loco_slots-1;
        static byte shown_speed[loco_slots]; // remember whats already shown
        static bool first_call=true;
        
        if (first_call) {
          first_call=false;
          for (int i=0; i<loco_slots; i++) shown_speed[i]=127;
        }
        
        // switch to next row
        current_slot= (current_slot + 1) % loco_slots;
        auto loco=DCC::speedTable[current_slot].loco;
        if (loco<0) return; // this slot is no longetr used
        if (loco==0) return; // we are beyond the last loco   
        
        auto speed = DCC::speedTable[current_slot].speedCode;
        if (speed== shown_speed[current_slot]) return; // no change in speed
        shown_speed[current_slot] = speed; // remember speed for next time

        auto direction = (speed & 0x80) ? 'F' : 'R';
        speed = speed & 0x7f;
        if (speed > 0) speed = speed - 1; // make it look like JMRI
        StringFormatter::lcd2(2, current_slot+2, F("Loco:%4d %3d %c"), loco, speed, direction);
      }
    )

To ensure the function is called twice per second we use the UserAddin HAL feature.
The LCD/OLED number 2 used by the function is connected by I2C. 

.. code-block:: cpp

    HAL(UserAddin,updateLocoScreen,500) 
    HAL(HALDisplay<OLED>, 2, 0x3d, 128, 64)  
