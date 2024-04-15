.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-hardware.rst
|EX-REF-LOGO|

***********************
List of Tested Decoders
***********************

|conductor| |tinkerer| |engineer| |support-button|

We often receive reports on DCC multifunction decoders via Discord and our support channels as well as requests for help when things don't quite work "out of the box".

As a result, we've started compiling a list of decoders that we've experienced with a view to helping people get up and running quicker with their DCC layouts.

The table below is a growing list of multifunction decoders we've had reasons to support or test for ourselves with various supporting information, and a rating from one to three stars on how easy it is to use and program them.

If you wish to add to this list, please fill out the DCC Decoder Feedback form and provide the details as per the table below.

.. rst-class:: dcclink

  `DCC Decoder Feedback <https://github.com/DCC-EX/dcc-ex.github.io/issues/new/choose/>`_

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

Note to manufacturers: This list is not designed in any way to disparage or favour specific manufacturers, and is simply a factual observation of what the DCC-EX team have noted while helping people get up and running with various DCC decoders.

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
    - DH126D
    - MF
    - Default for 2021/2022
    - JST-9
    - Default
    - 3
    - | I have noticed that these decoders switch on the rear light at power on with no commands, which can be a useful behavior for troubleshooting. They run nicely as installed. The learning curve I had on the 1st was entirely using DCC-EX + JMRI to configure them, additional installations and changes have been smooth.
      | DH126D is meant to be an economy decoder with fewer functions and features than the DH166D.
      | 1st and 2nd in November of 2022, 3rd was installed in December 2023.
  * - Digitrax
    - DH166D
    - MF
    - 51
    - N/A (bare wires)
    - Default
    - 3
    - Worked exactly as expected. No problems with programming or operation.
  * - Digitrax
    - SDXH186MT
    - MFS
    - New in 2021
    - 21MTC
    - Default
    - 2.5/3
    - Half point deduction due to fewer options.
  * - Märklin
    - m83
    - ACC
    - Default
    - Screw terminal
    - Default
    - 2/3
    - 
  * - Decoderwerk
    - 30402/30801
    - ACC
    - Default
    - Screw terminal
    - Default
    - 3/3
    - I can recommend them, because they are very simple, easy to use, small (4cm x 7cm(4-out) / 11cm(8-out)) and in comparison to the ones from Märklin very cheap.
  * - Märklin
    - MSD3/MLD3
    - MFS/MF
    - Various versions/ages
    - Märklin standard
    - Default
    - 3/3
    - No difficulties. On some decoders I have disabled all protocols but DCC, because I previously used a Märklin MobileStation they connected to automatically via mfx, but the decoders are also working perfectly with all enabled. If you should encounter problems, take a look at the CV reference section in the manual. Protocols other than DCC can be disabled with CV50.
  * - Bachmann
    - 4 Function decoder (36-550)
    - MF
    - Man. Version 46
    - N/A (bare wires)
    - Default
    - 2.5/3
    - Still a degree of uncertainty as to the full capabilities of this decoder this decoder
  * - D&H
    - PD10MU
    - MF
    - 3.12
    - N/A (bare wires)
    - Default
    - 3
    - Works perfectly, was my first decoder tested with DCC++EX. Reported it because I couldn't find this decoder in the list yet.
  * - LaisDCC
    - 860011
    - Accessory
    - Unknown
    - N/A (bare wires)
    - Default
    - 3
    - Using this in an unpowered loco B unit to provide lighting functions to mimic the powered unit. Works exactly as expected.
  * - LaisDCC
    - 860015
    - MF
    - Unknown
    - NEXT18
    - Default
    - 3
    - Worked as expected. This is in the powered A unit that complements the unpowered B unit.
  * - ESU
    - Lokpilot 4 21MTC
    - MF
    - Unknown
    - 21MTC
    - Default
    - 3
    - Worked as expected out of the box. CV setup easily via programming track.
  * - ESU
    - Lokpilot 5 59610
    - MF
    - Unknown
    - NEM652
    - Default
    - 3
    - As expected no problems connecting to DCC-EX CS. Biggest advantage with this decoder is multi-format. DCC, MM, M4 (mfx), DC and AC analogue (same feedback from 2 users).
