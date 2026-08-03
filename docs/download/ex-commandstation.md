\|EX-DL-LOGO\|

# EX-CommandStation

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\| \|support-button\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="2" local=""}
On this page
:::
::::

:::: note
::: title
Note
:::

The \|EX-CSB1\| already comes with the \|EX-CS\| software installed. You
can, however, use this page for instructions on how to upload a newer
version, or upload your EXRAIL scripts
::::

Welcome to the \|EX-CS\| download page. You have several choices:

- **\[RECOMMENDED\]** If you are a \|conductor-text\|, or you just want
  an easy installer to do the work for you, go to the
  [ex-Installer](#ex-installer) section.
- If you are a \|tinkerer-text\| the [ex-Installer](#ex-installer) is
  still the recommended solution, but if would like to download a zip
  file and install the firmware using the \|Arduino IDE\| or \|VSC\|, go
  to the [Latest EX-CommandStation Official
  Release](#latest-ex-commandstation-official-release) section.
- To get the latest unreleased development version, go to the [Latest
  EX-CommandStation Unreleased Development
  Version](#latest-ex-commandstation-unreleased-development-version) (or
  use the [ex-Installer](#ex-installer) ).
- If you are an \|engineer-text\| or developer, and want to clone the
  repository onto your computer, go to the [EX-CommandStation Repository
  (project source
  files)](#ex-commandstation-repository-project-source-files) section.
- If you\'re still looking for the old, and unsupported, \|BSC\|, go to
  the [BaseStation-Classic](#basestation-classic) section.

------------------------------------------------------------------------

\|EX-I-LOGO-SMALL\|

## EX-Installer

:::: {.note .note-float-right}
::: title
Note
:::

If you have any difficulties with the automated installer link try
these:

> ::: rst-class
> dcclink
>
> [For Windows
> x64](https://github.com/DCC-EX/EX-Installer/raw/main/dist/EX-Installer-Win64.exe)
> :::
>
> ::: rst-class
> dcclink
>
> [For Windows
> x32](https://github.com/DCC-EX/EX-Installer/raw/main/dist/EX-Installer-Win32.exe)
>
> [For MacOS /
> OSX](https://github.com/DCC-EX/EX-Installer/raw/main/dist/EX-Installer-macOS)
> :::
>
> ::: rst-class
> dcclink
>
> [For Linux
> x64](https://github.com/DCC-EX/EX-Installer/raw/main/dist/EX-Installer-Linux64)
> :::
::::

This is the new version of the \|EX-I\|.

Clicking on the link below will automatically find the correct version
of the installer for your Computer and Operating system (Windows, Apple,
Linux) and download it.

This downloads a self contained app that can automatically load the
software from your computer to your Arduino or other supported board.
Click here for
`EX-Installer installation instructions </ex-commandstation/installer-diy>`{.interpreted-text
role="doc"}.

*Note* that the new \|EX-I\| will unfortunately not work on Windows 7.

<p class="dcclink"><a onclick="getNewLink()"><span class="problematic">Automated Installer</span></a></p>

\|force-break\|

------------------------------------------------------------------------

\|EX-CS-LOGO-SMALL\|

## Manually loading the software

If you plan to use the the \|Arduino IDE\| or \|VSC\| to configure your
\|EX-CS\| you can use the links below to download the appropriate
version.

:::: important
::: title
Important
:::

A word of caution on using the \|Arduino IDE\| to install the software:

While it is possible install the software using the \|Arduino IDE\|, we
*seriously* **DO NOT RECOMMEND IT** for a \|conductor-text\| or
\|tinkerer-text\|. It is an order of magnitude more complex, much
slower, and with a very high probability of getting something wrong
unless you really know what you are doing.

The \|EX-I\| will meet 100% of the needs of a \|conductor-text\| or
\|tinkerer-text\| with considerably less effort.
::::

### Latest EX-CommandStation Official Release

::::: note
::: title
Note
:::

On the releases page, select the most recent version and download the
.zip file. You will see the 2 files for download, choose the compression
format you prefer: CommandStation-EX.zip or CommandStation-EX.tar.gz.
The zip/tar file contains the Arduino Sketch file for \|EX-CS\|. You
will need either the \|Arduino IDE\| or the PlatformIO development
environment in order to upload it to your microcontroller board. Click
here for
`Arduino IDE installation instructions </ex-commandstation/advanced-setup/installation-options/arduino-ide>`{.interpreted-text
role="doc"}.

::: rst-class
dcclink
:::

[Official Release
page](https://github.com/DCC-EX/CommandStation-EX/releases)
\|EXTERNAL-LINK\|
:::::

### Latest EX-CommandStation Unreleased Development Version

:::: note
::: title
Note
:::

The link below is to the \"devel\" branch in GitHub. You can use the
\"Download ZIP\" option from the \"Code\" pulldown menu to obtain a
local copy of this code. Please open the zip file, go into the
\"CommandStation-EX-master\" folder, and unzip all the files in that
folder into your \"CommandStation-EX\" sketch folder. Make sure you **DO
NOT** just unzip the entire zip file, since it will have the incorrect
folder name. The \|Arduino IDE\| requires that the folder name and the
.ino file inside that folder match names exactly, i.e.:
\"CommandStation-EX\" not \"CommandStation-EX-master\".
::::

::::: attention
::: title
Attention
:::

[Discord](https://discord.gg/y2sB4Fp) is the best place to keep
up-to-date on new code releases, and you may be directed to download the
latest version here from time to time, as new features are added and
updated often.

::: rst-class
dcclink
:::

[Development
Version](https://github.com/DCC-EX/CommandStation-EX/tree/devel)
\|EXTERNAL-LINK\|
:::::

\|force-break\|

### EX-CommandStation Repository (project source files)

::::: note
::: title
Note
:::

The link below will take you the the EX-CommandStation GitHub
repository, where you can clone the project to your computer. Click on
the green button to get a clone link or to download the zip file. We
have made sure that you can still use the \|Arduino IDE\| if you like,
but we recommend developers use the PlatformIO development environment.
See the
`Contributing Page </about/contributing/index>`{.interpreted-text
role="doc"} for more information.

::: rst-class
dcclink

[EX-CommandStation GitHub](https://github.com/DCC-EX/CommandStation-EX)
\|EXTERNAL-LINK\|
:::
:::::

\|force-break\|

------------------------------------------------------------------------

\|EX-BSC-LOGO-SMALL\|

## BaseStation-Classic

:::: warning
::: title
Warning
:::

BaseStation-Classic (the original DCC++) is no longer maintained or
supported by the DCC-EX Team.
::::

We recommend using the newer \|EX-CS\| as it will run on the same
hardware and is maintained and supported.

The new \|EX-I\|
`does not provide an option to install BaseStation-Classic`{.interpreted-text
role="dcc-ex-red-bold"} so if you wish to install it you will need to
use the \|Arduino IDE\| or \|VSC\| and download the links below.

> ::: rst-class
> dcclink
>
> [BaseStation-Classic .zip
> file](https://github.com/DCC-EX/BaseStation-Classic/archive/master.zip)
> \|EXTERNAL-LINK\|
> :::
>
> ::: rst-class
> dcclink
>
> [BaseStation-Classic
> GitHub](https://github.com/DCC-EX/BaseStation-Classic)
> \|EXTERNAL-LINK\|
> :::
