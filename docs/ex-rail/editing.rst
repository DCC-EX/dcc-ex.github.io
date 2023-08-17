.. include:: /include/include.rst
.. include:: /include/include-l1.rst
.. include:: /include/include-ex-r.rst
|EX-R-LOGO|

**********************
Editing myAutomation.h
**********************

|tinkerer| |conductor|

.. sidebar:: 

   .. contents:: On this page
      :depth: 4
      :local:

The instructions containing all your objects and sequences is added to your |EX-CS| by creating a file called **'myAutomation.h'** in the same folder as 'CommandStation-EX.ino'.

Connecting your Arduino and pressing the :guilabel:`Upload` button in the usual way will save the file and upload your script into the Command Station.

You can create and edit the myAutomation.h using a text editor (like Notepad), but if you are using the Arduino IDE (rather than the |EX-I|) you can create the myAutomation.h file in the Arduino IDE. Use the pulldown button and select New Tab (or simply press Ctrl+Shift+N).

.. image:: /_static/images/ex-rail/setup1.jpg
   :alt:  Setup pulldown button
   :align: center
   :scale: 100%
   :target: #myautomation-h-editing-your-sequences

.. image:: /_static/images/ex-rail/setup2.jpg
   :alt:  Setup pulldown menu
   :align: center
   :scale: 100%
   :target: #myautomation-h-editing-your-sequences

Enter the file name "myAutomation.h" (This is case sensitive)

.. image:: /_static/images/ex-rail/setup3.jpg
   :alt:  Setup myAutomation.h
   :align: center
   :scale: 100%
   :target: #myautomation-h-editing-your-sequences

And type your script in.

.. image:: /_static/images/ex-rail/setup4.jpg
   :alt:  Setup Example file
   :align: center
   :scale: 100%
   :target: #

|

Content
=======

What you will need to add to your **myAutomation.h** file will be explained in the next few pages, but can be catogorised as:

* :doc:`Objects </ex-rail/creating-elements>`
* :doc:`Sequences </ex-rail/getting-started>`

----

Re-upload the EX-CommandStation software
========================================

Using EX-Installer
------------------

#. Place your 'myAutomation.h' file in the ``CommandStation-EX`` subfolder of wherever you extracted the |EX-I| files.
#. Re-Run |EX-I|
#. Select the same options that you originally chose and upload

The myAutomation.h file will be automatically loaded with the |EX-CS| software.

Using the Arduino IDE
---------------------

#. Place your 'myAutomation.h' file in the ``CommandStation-EX`` subfolder of wherever you extracted the |EX-CS| files from GitHub.
#. Run the Arduino IDE
#. Open the ``CommandStation-EX`` folder
#. Select the Board, COM port etc. as before
#. click :guilabel:`Upload`

The myAutomation.h file will be automatically loaded with the |EX-CS| software.

----

Next Steps - Objects
====================

   
Click :doc:`here <creating-elements>` or click the :guilabel:`Next` button to learn how to add the key objects you will need to create your automation sequences.