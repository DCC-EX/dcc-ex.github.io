.. include:: /include/include.rst
.. include:: /include/include-l1.rst
|EX-TT-LOGO|

****************************
Troubleshooting EX-Turntable
****************************

|tinkerer| |githublink-ex-turntable-button2|

.. sidebar::

  .. contents:: On this page
    :depth: 1
    :local:

You will find resolutions to a number of common issues encountered with |EX-TT| on this page.

Homing failure
==============

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
===================

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
=============================================

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
================================================================

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes
  * - The CommandStation detects a current overload and turns track power off
    - | The DCC phase is out of sync between the layout and bridge track, phase inversion flag is required for the position
      | Tracks opposite each other around the turntable are wired with inverted phases, wiring must be adjusted

EX-CommandStation compile errors with device driver enabled
===========================================================

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes
  * - EX-CommandStation software fails to compile with "#include IO_TurntableEX.h" in myHal.cpp
    - The version of EX-CommandStation is incorrect, you need the "add-turntable-controller" branch of `EX-CommandStation <https://github.com/DCC-EX/CommandStation-EX/tree/add-turntable-controller>`_

EX-Turntable showing as offline with <D HAL SHOW>
=================================================

.. list-table:: 
  :widths: auto
  :header-rows: 1
  :class: command-table

  * - Symptoms
    - Common Causes
  * - | \<D HAL SHOW\> reports EX-Turntable as OFFLINE
      | EX-Turntable does not respond to EX-RAIL or diagnostic commands
    - | EX-Turntable is not powered on, or was powered on after the CommandStation
      | The i2c interfaces are not connected correctly, refer to :ref:`ex-turntable/assembly:9. connect ex-turntable to your ex-commandstation`
      | The i2c address in EX-Turntable's config.h does not match the address in the CommandStation's myHal.cpp file
