.. include:: /include/include.rst
.. include:: /include/include-l2.rst
.. include:: /include/include-description.rst

|EX-CONTRIBUTING-LOGO|

**********************************
Versioning and the Release Process
**********************************

|SUITABLE| |engineer| |support-button|

.. sidebar:: 
   :class: sidebar-on-this-page

   .. contents:: On this page
      :depth: 2
      :local:

This page outlines how to determine version numbers, create a release, and outlines what is required before a release can be done.

Software Versioning
===================

The |DCC-EX| team utilise semantic versioning for all official software releases, which is associated with either a GitHub tag or a GitHub release.

This means all version numbers are in the format "X.Y.Z", and GitHub tags are in the format "vX.Y.Z-[Prod|Devel]", where:

- X is the **major** version number
- Y is the **minor** version number
- Z is the **patch** version number
- Select either suffix "Prod" for a Production release, or "Devel" for a Development release

For example, a production version of |EX-CS| might be "5.4.6", which will have the GitHub tag "v5.4.6-Prod", where as a development version "5.5.1" would have a GitHub tag "v5.5.5-Devel".

These are the guidelines for determining version numbers:

- Development versions have an odd **minor** version number, Production versions are even numbers (eg. X.1.Z is a development version, X.0.Z is production).
- Increment the **major** version number if a new feature is going to introduce a **breaking change** that is not backwards compatible.
- Increment the **minor** version number when adding new features that are backwards compatible.
- Increment the **patch** version number when making minor fixes that don't have overall functional impacts.

So, when fixing a bug a user has reported, you should only increment the **patch** number, whereas introducing a new feature that lets the rest of the software function normally should have a **minor** version increment.

Any time existing functionality is no longer compatible with the new version, the **major** version must be incremented.

GitHub Tags vs. Releases
------------------------

Every GitHub release has an associated tag, but not every tag has an associated release. A tag simply represents the state of the GitHub repository at a specific point in time (it will be associated with a commit), whereas a relase also has an associated description and attached archive files for users to download.

Tagging independently of a release is helpful for development versions for users to be referred to, but ideally each production tag should also be a release.

|EX-I| uses tags, not releases, so users can select a published tag to use, whereas for users using the Arduino IDE, they need to download the archives from a release.

Release Requirements
====================

These items are mandatory for creating a release:

- Where applicable, files such as "Version.h" must be up to date with notes on what has changed
- Release notes must be up to date with the changes in the release
- A DCC-EX News article has been prepared
- The lead developer for the associated product and the majority of the DCC-EX leadership team have agreed the release is ready

Creating a Release
==================

For products that are intended to work with the Arduino IDE, archive files (both .zip and .tar.gz) must be attached to the release with the correct folder structure the Arduino IDE expects.

Archive File Structure
----------------------

The folder containing the files must be the exact same name (including case) of the main ".ino" file, minus the .ino extension.

Ideally, the .zip or .tar.gz file will contain the version in the name, and will contain a folder with the correct name, which contains the repository files.

For |EX-CS|, this means the archive files for version 5.4.6 would be:

- CommandStation-EX-5.4.6-Prod.zip
- CommandStation-EX-5.4.6-Prod.tar.gz

Each of these would contain a folder called ``CommandStation-EX`` as this matches the ``CommandStation-EX.ino`` filename without the extension, satisfying the Arduino IDE requirement.

This folder would contain all files as shown in this image from 7Zip on Windows. Note the archive filename is ``CommandStation-EX-5.4.6-Prod.zip`` which contains the folder ``CommandStation-EX``, and this folder contains all the repository files.

.. image:: /_static/images/github/release-archive-contents.png
   :scale: 50%

Create the Release
------------------

This is the process to create a new, untagged release:

1. Navigate to the GitHub repository in your favourite browser.
2. Download the ZIP of the repository by clicking the ``Code`` button and selecting ``Download ZIP``.
3. Create the appropriate .zip and .tar.gz archive files as outlined in :ref:`about/contributing/release-process:archive file structure` using your favourite archiving software.
4. Navigate to the Releases tab in GitHub and click ``Draft new release``.
5. Create the new tag based on :ref:`about/contributing/release-process:software versioning`.
6. Enter an appropriate title and add some release information, ideally linking to release notes, a |DCC-EX| news article, or some other reference containing details.
7. For a Development release, untick ``Set as the latest release`` and tick ``Set as a pre-release``.
8. For a Production release, tick ``Set as the latest release`` provided it is indeed the latest release.
9. Attach both archive files created in step 3.
10. Click ``Publish release``.

If, instead, you need to create a release for an existing tag, this is the process:

1. Navigate to the GitHub repository in your favourite browser.
2. Click ``Tags`` in the code window and locate the tag this release should be associated with.
3. Download the source code associated with the tag from the ``Assets`` section.
4. Click ``Create release from tag``.
5. Create the appropriate .zip and .tar.gz archive files as outlined in :ref:`about/contributing/release-process:archive file structure` using your favourite archiving software and the source code as downloaded in step 3.
6. Enter an appropriate title and add some release information, ideally linking to release notes, a |DCC-EX| news article, or some other reference containing details.
7. For a Development release, untick ``Set as the latest release`` and tick ``Set as a pre-release``.
8. For a Production release, tick ``Set as the latest release`` provided it is indeed the latest release.
9. Attach both archive files created in step 5.
10. Click ``Publish release``.
