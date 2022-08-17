.. include:: /include/include.rst
.. include:: /include/include-l2.rst
***********************
List of Tested Decoders
***********************

|conductor| |tinkerer| |engineer|

We often receive reports on DCC multifunction decoders via Discord and our support channels as well as requests for help when things don't quite work "out of the box".

As a result, we've started compiling a list of decoders that we've experienced with a view to helping people get up and running quicker with their DCC layouts.

The table below is a growing list of multifunction decoders we've had reasons to support or test for ourselves with various supporting information, and a rating from one to three stars on how easy it is to use and program them.

If you wish to add to this list, please fill out the `DCC Decoder Feedback <https://github.com/DCC-EX/dcc-ex.github.io/issues/new/choose/>`_ form and provide the details as per the table below.

* Brand - The brand/manufacturer of the decoder.
* Model - The specific model or part number of the decoder.
* Type:

  * MF - Multifunction.
  * MFS - Multifunction with sound.
  * ACC - Accessory.
  * SND - Sound only.
* Firmware - The specific version of firmware on the decoder when tested.
* Connector:

  * NEM651.
  * NEM652.
  * 21MTC.
  * PLUX8/12/16/22.
  * N/A (bare wires).
* ACK Settings - Specific settings to enable correct ACK behaviour for service mode programming.
* Rating:

  * Rating is out of 3, purely from the perspective of compatibility and ease of use getting them working and programming specifically with |EX-CS|. No consideration is given to how easy or complicated these are to install as the use cases vary too widely.
  * 1/3 - Can be quite difficult or complicated to get working or testing had inconsistent results.
  * 2/3 - Works as expected, with some extra effort required such as unique ACK settings.
  * 3/3 - Works exactly as expected.
* Comments - Any other relevant information discovered during testing or support tickets.

Note to manufacturers: This list is not designed in any way to disparage or favour specific manufacturers, and is simply a factual observation of what the DCC++ EX team have noted while helping people get up and running with various DCC decoders.

.. list-table:: Decoder List
  :widths: auto
  :class: command-table

  * - Brand
    - Model
    - Type
    - Firmware
    - Connector
    - ACK Settings
    - Rating
    - Comments
  * - SoundTrax
    - Tsunami2
    - MFS
    - New in 2020
    - Unknown
    - Default
    - 2.5/3
    - Installed in Athearn Genesis OEM SD70ACe (ATHG01943). Half point deduction due to ACK being low.
  * - TCS
    - 1527 WOW 121 Diesel + GEN-MB1 Motherboard w/KA2
    - MFS
    - New in 2020
    - 21MTC
    - D ACK MAX 9200
    - 2.5/3
    - Half point deduction due to non-standard method for indexed CVs, and increased ACK pulse time.   |
  * - Digitrax
    - SDXH186MT
    - MFS
    - New in 2021
    - 21MTC
    - Default
    - 2.5/3
    - Half point deduction due to fewer options.
