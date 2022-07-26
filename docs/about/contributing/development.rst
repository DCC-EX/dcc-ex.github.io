************
Development
************

.. sidebar:: On this page

   .. contents:: 
      :depth: 2
      :local:

This page aims to outline what's required for those who wish to contribute to software development.

If you haven't done so already, make sure you are familiar with how we use :doc:`/contributing/github` and are familiar with our :doc:`/contributing/software`.

Bug fixes, features, and releases
==================================

As mentioned earlier, we expect contributors to follow Git best practises when working on our various repositories.

* When working on new features or bug fixes, create a branch.
* Commit and publish regularly.
* When ready for review, submit a pull request.

Level of C++ understanding required
====================================

As a general rule, writing software in C++ for the Arduino platform is fairly simple, with plenty of tutorials and guides available on the internet to help get started.

However, the CommandStation-EX codebase is written using various techniques to fit as much capability as possible into the very limited Arduino AVR architecture and memory limits that are available, and it's important to understand the various techniques in use to support this and avoid adding any dependencies that would compromise this approach.

.. tip:: 

  Anyone wishing to read our code is welcome, and we will do our best to explain anything that's not obvious, but we will expect "basic" C++ skills and a general understanding of Arduinos and DCC which are extensively documented on the web, otherwise you are unlikely to understand our answers.

Reading and understanding our code
___________________________________

Reading any code in any language is always going to require a basic understanding of the language and features in addition to an understanding of the environment (Arduino in this case, and various CPU versions), plus an understanding of the program features the author is trying to implement (Command parsing and DCC in our case).

The level of C++ that we use is a relatively small subset of the language as we don't need or use many of the more complex C++ features such as stdio, templates, lambdas, operator overloading, multiple inheritance etc., but we DO make significant use of the C++ compiler's pre-processor features to automatically customise the code to various CPU or user feature requirements (Wifi, Ethernet etc).

EX-RAIL in particular pulls some very cunning, but legitimate, stunts with the pre-processor to weave your automations into the code as it's compiled.

The Arduino environment is fundamentally very simple for most programming tasks as there is no massive operating system, GUI, or file system to learn. For a very small subset of our code we do need to understand CPU specific interrupts, registers, and timers which are almost never encountered by programmers who are not working in embedded systems or device drivers. In addition, it's necessary to learn about the various hardware devices that may be attached although we have tried to reduce the difficulty for the user by adding code that is not necessarily easy to read for the programmer. (Its a trade-off, the complexity has to go somewhere and we don't want the average user to suffer just to make it easy for a handful of programmers.)

Comments in our code could be better but excessive commenting often leads to confusion as things change and in most cases the use of meaningful function and variable names conveys all the information a comment could.

C++ concepts to understand
___________________________

The following subsets of C++ are good to understand:

* Pointers instead of the String class: For speed and resource usage the String class is frowned upon and all "strings" are classical null terminated C strings. So it is recommended to read up on how those work.
* Static class members: The observant reader finds that there are static and "normal" class members in many classes throughout the code and it is important to keep track of which members exist per object and which only exist once.
* Sized types: To save space data types need to be as small as possible and have a predictable size, even when changing the CPU architecture. Therefore, sized types like uint8_t and uint16_t are used where possible.
* Eliminate float: As float calculations are CPU intensive and need a lot of program memory on a small AVR CPU these kind of calculations have been eliminated. We therefore would use values like 2500mA instead of 2.5A.

Reliance on the C++ pre-processor
__________________________________

We rely on the ability of the compiler/linker to remove functions that are never called so the resulting binary image is as small as possible. This avoids having to manage separate code for large and small cpus.

We also rely on the compiler to propagate constants. This, for example, allows us to use a floating point value for motor shield definitions but have the float to integer calculation performed by the compiler, meaning the large floating point library is not needed at run time.

Other concepts and techniques
______________________________

* Use of bit manipulation operators to pack multiple flags into a byte.
* EX-RAIL and the DCC ACK manager use "virtual machine" techniques to implement multitasking.

Third-party libraries
======================

We avoid third party libraries where possible because they involve additional installation steps, can introduce version issues, and support related problems are outside our control.

Further to this, we need to take into account the licensing used by libraries as not all open source licenses are the same.

If there is no choice but to utilise a third-party library in some form, then this is the recommended approach:

* Ensure the license used by the library is GPL-3.0.
* Identify the version of the library that is stable and known to work reliably with our code.
* Copy the core library only locally to our repo (disregard examples and other extraneous files).
* Include the local copy of the library only.
* Credit the authors of the library appropriately.

For an example of where a third-party library has been successfully incorporated into our code, refer to the `Turntable-EX <https://github.com/DCC-EX/Turntable-EX>`_ repository and the included AccelStepper library.
