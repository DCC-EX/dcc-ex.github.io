*****************************
Troubleshooting Turntable-EX
*****************************

.. image:: ../_static/images/conductor.png
  :alt: Conductor Level
  :scale: 40%
  :align: right

Troubleshooting common Turntable-EX issues
===========================================

You will find resolutions to a number of common issues encountered with Turntable-EX on this page.

Homing failure
_______________

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes
  * - | Turntable rotates on start up and ends in a random position
      | Serial console reports "ERROR: Turntable failed to home, setting random home position"
    - | The magnet in the turntable is too far away from the sensor
      | Hall effect sensor is connected incorrectly

Calibration failure
_____________________

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes
  * - | Turntable rotates on start up and ends in a random position
      | Serial console reports "ERROR: Turntable failed to home, setting random home position"
      | Serial console reports "CALIBRATION: FAILED, could not home, could not determine step count"
    - | The magnet in the turntable is too far away from the sensor
      | Hall effect sensor is connected incorrectly

Turntable judders, stalls, or fails to rotate
______________________________________________

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes
  * - When attempting to rotate, the turntable judders or shakes
    - | An incorrect stepper driver has been configured
      | Something is physically interfering with the turntable or stepper operation, check for interference
  * - The turntable does not rotate at all
    - | An incorrect stepper driver has been configured
      | Something is physically interfering with the turntable or stepper operation, check for interference

Track power is cut when locomotive enters turntable bridge track
_________________________________________________________________

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes
  * - The CommandStation detects a current overload and turns track power off
    - | The DCC phase is out of sync between the layout and bridge track, phase inversion flag is required for the position
      | Tracks opposite each other around the turntable are wired with inverted phases, wiring must be adjusted

CommandStation-EX compile errors with device driver enabled
____________________________________________________________

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes
  * - CommandStation-EX software fails to compile with "#include IO_TurntableEX.h" in myHal.cpp
    - The version of CommandStation-EX is too old, upgrade to X.X.X

Turntable-EX showing as offline with <D HAL SHOW>
__________________________________________________

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes
  * - | \<D HAL SHOW\> reports Turntable-EX as OFFLINE
      | Turntable-EX does not respond to EX-RAIL or diagnostic commands
    - | Turntable-EX is not powered on, or was powered on after the CommandStation
      | The I2C interfaces are not connected correctly, refer to :ref:`turntable-ex/get-started:9. connect turntable-ex to your commandstation`
      | The I2C address in Turntable-EX's config.h does not match the address in the CommandStation's myHal.cpp file
