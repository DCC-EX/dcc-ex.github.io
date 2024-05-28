.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-throttles.rst
************************
 Android apps on Windows
************************

|conductor| |tinkerer| |engineer| |support-button|

All the Android based throttle apps listed can be run on Microsoft Windows PCs.

There are a least two methods:

- Using *BlueStacks*
- Using *Windows Subsystem for Android*

BlueStacks
==========

The `BlueStacks <https://www.bluestacks.com/>`_ app allows you to install and run most Android apps on most recent Windows PCs.

It has the advantages of:

- Works on most recent Windows PCs
- User Friendly installation of apps
- Allows you to run multiple instances of same app at the same time

Disadvantages include:

- Has advertisements

Follow the instructions on their `site <https://www.bluestacks.com/>`_ to install BlueStacks, then get the appropriate .apk to install the throttle app you want.  e.g. The Engine Driver .apk is available from the `Engine Driver site <https://enginedriver.mstevetodd.com/downloads>`_`

Windows Subsystem for Android
=============================

`Windows Subsystem for Android <https://https://learn.microsoft.com/en-us/windows/android/wsa//>`_ is a built in feature of Windows 11 that allows you to install and run most Android apps on *some* Windows PCs.

It has the advantages of:

- Built in feature of Windows 11
- No Advertisements

Disadvantages include:

- Only works of Windows 11 PCs with an SSD (not a physical Hard Drive)
- Not very user friendly installation (sideloading) of non-Amazon approved apps (i.e. the throttle apps)
- Does *not* allow you to run multiple instances of same app at the same time

Follow the `instructions here <https://www.windowscentral.com/how-sideload-android-apps-using-wsa-windows-11>`_  (or `a slightly differnt version of instructions here <https://www.xda-developers.com/how-to-sideload-android-apps-on-windows-11/>`_) to setup *Windows Subsystem for Android* to allow 'sideloading'.

You will also need to install the `SDK Platform Tools <https://developer.android.com/tools/releases/platform-tools>`_.

You will also need to get the appropriate .apk to install the throttle app you want.  e.g. The Engine Driver .apk is available from the `Engine Driver site <https://enginedriver.mstevetodd.com/downloads>`_

|hr-dashed|

Refer to pages linked above for details but a summary of the process for installing with Windows Subsystem for Android is:

# Install *Windows Subsystem for Android*
# Download the *SDK Platform Tools*

    # Extract the files from the zip file and record the folder there are in |BR| e.g. C:\Users\your_username\Downloads\platform-tools\

# Download the APK you want to install

    # Note the name of the file where you saved it |BR| e.g. ``C:\Users\your_username\Downloads\EngineDriver-2.36.177.apk``

# Start *Windows Subsystem for Android*

    # Enable the Developer option

        # click the overflow menu (the three bars) in the top left
        # Then ``Advanced settings``
        # Turn on ``Developer mode``
        # Note the ip address and port on the same row (normally 127.0.0.1:58526)

# Start a command prompt with Administrator privileges 

    # Click :guilabel:`Start`
    # Type in ``CMD`` or ``command`` 
    # Right click on ``Command Prompt`` from the found list and select ``Run as Administrator``
    # Click :guilabel:`Yes` when it asks

# Connect the PC to the Windows Subsystem for Android

    # Enter the command |BR| ``<extracted_location>\adb connect <ip_address_&_port>`` |BR| where **<extracted_location>** is the folder you you extracted the *SDK Platform Tools* to above, and |BR| **<ip_address_&_port>** are the ip address and port that you recorded above |BR| e.g. ``C:\Users\your_username\Downloads\platform-tools\adb connect 127.0.0.1:58526``.
    # You should see a request to 'Allow ADB debugging'.  Click :guilabel:`Allow`

        # If you don't see the request. |BR| e.g. you see something like ``cannot connect to 127.0.0.1:58526: No connection could be made because the target machine actively refused it. (10061)``

            # In the 'Windows Subsystem for Android' app (on the PC), click ``Turn Off``
            # Then open the 'Amazon Appstore' (that you should have installed as part of installing Windows Subsystem for Android).  this will automatically restart the subsystem.
            # Enter the adb connect command again.

    # Note: it is normal (not sure why) to see ``failed to authenticate to 127.0.0.1:58526``

# Install the sdk.

    #  enter the command |BR| ``<extracted_location>\adb install <apk_file_location>`` |BR| where **<extracted_location>** is the folder you you extracted the *SDK Platform Tools* to above, and |BR| **<apk_file_location>**  is the floaction and name of the downlaoded apk above. |BR| e.g. ``C:\Users\your_username\Downloads\platform-tools\adb install C:\Users\your_username\Downloads\EngineDriver-2.36.177.apk``

# Close the command prompt windows

|hr-dashed|

To run the app once installed 

# Click :guilabel:`Start`
# Click :guilabel:`all Apps`
# Scroll down to ``Engine Driver`` (or whatever app you installed) and click it.
# First use only: When **Engine Driver** start the first time you will be asked a number of questions
# When you get the "Connect" screen, **Engine Driver** cannot 'discover' the |EX-CS|, so you will need to enter the IP address and port, then click :guilabel:`Connect`