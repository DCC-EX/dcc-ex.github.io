\|EX-R-LOGO\|

# Editing myAutomation.h

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="4" local=""}
On this page
:::
::::

The instructions containing all your objects and sequences is added to
your \|EX-CS\| by creating a file called [myAutomation.h]{.title-ref} in
the same folder as \'CommandStation-EX.ino\'.

Connecting your Arduino and pressing the `Upload`{.interpreted-text
role="guilabel"} button in the usual way will save the file and upload
your script into the Command Station.

You can create and edit the [myAutomation.h]{.title-ref} using a text
editor (like Notepad), but if you are using the \|Arduino IDE\| (rather
than the \|EX-I\|) you can create the myAutomation.h file in the
\|Arduino IDE\|. Use the pulldown button and select New Tab (or simply
press Ctrl+Shift+N).

[![Setup pulldown button](/_static/images/exrail/setup1.jpg){.align-center}](#myautomation-h-editing-your-sequences)

[![Setup pulldown menu](/_static/images/exrail/setup2.jpg){.align-center}](#myautomation-h-editing-your-sequences)

Enter the file name \"myAutomation.h\" (This is case sensitive)

[![Setup myAutomation.h](/_static/images/exrail/setup3.jpg){.align-center}](#myautomation-h-editing-your-sequences)

And type your script in.

[![Setup Example file](/_static/images/exrail/setup4.jpg){.align-center}](#)

| 

:::: warning
::: title
Warning
:::

Do not waste your time asking ChatGPT, Copilot or Gemini to create
EXRAIL scripts. They do not understand EXRAIL and will get it wrong 100%
of the time.
::::

## Content

What you will need to add to your [myAutomation.h]{.title-ref}\` file
will be explained in the next few pages, but can be categorised as:

- `Objects </exrail/creating-elements>`{.interpreted-text role="doc"}
- `Commands </exrail/getting-started>`{.interpreted-text role="doc"}
- `Sequences </exrail/getting-started>`{.interpreted-text role="doc"}

------------------------------------------------------------------------

## Re-upload the EX-CommandStation software

### Using EX-Installer

:::: important
::: title
Important
:::

If you are using \|EX-I\| **DO NOT** create or edit the myAutomation.h
file in the EX-Installer installation folder (the folder the
EX-Installer creates).

Instead, create you myAutomation.h anywhere else and point EX-Installer
to that folder when it askes.
::::

1.  create your \'myAutomation.h\' file in any `CommandStation-EX`,
    anywhere on your computer (except the EX-Installer installation
    folder.)
2.  Run \|EX-I\|
3.  When asked, point EX-Installer to the folder and file that you
    created.

The myAutomation.h file will be automatically loaded with the \|EX-CS\|
software.

See `/ex-installer/managing-config-files`{.interpreted-text role="doc"}
for more information.

------------------------------------------------------------------------

### Using the Arduino IDE

1.  Place your \'myAutomation.h\' file in the `CommandStation-EX`
    subfolder of wherever you extracted the \|EX-CS\| files from GitHub.
2.  Run the \|Arduino IDE\|
3.  Open the `CommandStation-EX` folder
4.  Select the Board, COM port etc. as before
5.  click `Upload`{.interpreted-text role="guilabel"}

The myAutomation.h file will be automatically loaded with the \|EX-CS\|
software.

\|HR-HEAVY\|

## Next Steps - Objects

See the `creating-elements`{.interpreted-text role="doc"} page or click
the \'Next\' button to learn how to add the key objects you will need to
create your automation sequences.
