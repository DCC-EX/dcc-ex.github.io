.. include:: /include/include.rst
.. include:: /include/include-l2.rst
|EX-CONTRIBUTING-LOGO|

*************
Style Guide
*************

|conductor| |tinkerer| |engineer|

.. sidebar::

  .. contents:: On this page
    :depth: 2
    :local:

This page aims to provide guidance for people contributing to the |DCC-EX| website on how to write individual pages to a) provide a better user experience, and b) be easier to maintain the documentation.

Text and Style Standards
========================

Please ensure to follow the standards below when creating or updating documentation to ensure the look and feel of the website remains consistent.

.. highlight:: rst

Style Guidelines
----------------

* Every page (except a few pages like home, about, contact, etc.) MUST start with one or more level images (after the title) to indicate the intended base audience for the page. 
* Where possible, use the expansions for the level images:

  * \|conductor\| |conductor|
  * \|tinkerer\| |tinkerer|
  * \|engineer\| |engineer|
  * \|conductor-no-text\| |conductor-no-text|
  * \|tinkerer-no-text\| |tinkerer-no-text|
  * \|engineer-no-text\| |engineer-no-text|

* Where possible, use the Team and Product names the expansions (not possible in headings)
  
  * \|DCC-EX\| for |DCC-EX|
  * \|EX-CS\| for |EX-CS|
  * \|EX-I\| for |EX-I|
  * \|EX-R\| for |EX-R|
  * \|EX-TT\| for |EX-TT|
  * \|EX-DCCI\| for |EX-DCCI|
  * \|BSC\| for |BSC|

* Where possible, use the expansions for the level text (not possible in headings)

  * \|conductor-text\| |conductor-text|
  * \|tinkerer-text\| |tinkerer-text|
  * \|engineer-text\| |engineer-text|

* Additional expansions that should be used where possible: (currently these hyperlink to the the glossary but the intention is to have them link somewhere more sensible later.)

  * \|Motor Driver\|
  * \|JMRI\|
  * \|Engine Driver\|
  * \|wiThrottle\| 
  * \|wiThrottle Protocol\|
  * \|wiThrottle Server\|
  * \|Access Point\|
  * \|Access Point Mode\|
  * \|Station Mode\|
  * \|I2C\| (note this has no link, it simply replaces 'I2C' with |I2C|)

* Avoid abbreviations that would not be easily recognised by 'Conductors'.  

  * In particular *don't* use 'CS'.  Use the full name 'Command Station'
  * *don't* use 'AP'.  Use 'Access Point' or 'Access Point Mode'
  * *don't* use 'STA'.  Use 'Station' or 'Station Mode'

* Avoid 'fluff' - unnecessary text that adds no value.

  * Re-read everything you write. Ask yourself a) is there a simpler way of saying it. b) does it add value.
  * The exception to this is a bit of humor now and then, but don't overdo it.

* Keep headings short.  If it fills the page it is too long.
* If you have a number of sections that describe options; present them in list them first, before the sections, with an explanation as to why they are optional.  (i.e. a bullet list with hyperlinks to the headings.) 
* Where possible, avoid starting a section with a negative point of view.  i.e. Talk about the positives of what you are discussing first, before you delve into the negative or problematic aspects. |BR| e.g. Don't start with "... This is not for Conductors...", instead say "..This page is for Tinkerers ... Conductors should...".
* Use British/Australian/Canadian/Indian (pretty much every except the USA) spelling e.g. 'colour' not 'color'.  |br|\ (Primarily because it is used in more English speaking countries)
* Preferred Terms:
  
  * Use **"Motor Driver"**, not "Motor Shield", "Motor Board", "Motorboard"
  * In general use **'train'** or **'loco'** instead of 'locomotive' or 'engine'
  * Use **"Smart Phone"** instead of 'Cell Phone' (US only term) or 'Mobile Phone' (just about everywhere else)
  * Use **Throttle** or **Throttle (controller)** instead of 'controller' or 'controller (throttle)'

*	Use railroad/railway terminology that is understandable by all English-speaking people. |br|\ Where there are clear differences from US to non-US terminology use both with a slash between and use the US version first. e.g. turnouts/points, consists/multiple units, switching/shunting.  (Only because the US term appears in apps like JMRI.)
*	No full stop at the end of a numbered or unnumbered list
*	Numbered lists should generally only be used if they are describing a specific sequence, or the numbering is important to the text
* Use first person (you and your; not I, me, my or am) language
*	A string of nouns should be generally be sequenced in alphabetic order, unless it makes more sense within the context to display them in some other sequence
* Double quotes (") should only be used for quoting text from people, documents or web sites
*	No quotes around 'Also See' type references
*	Avoid '(above)' or '(below)' in text.  Use hypertext links instead
*	**``.. todo:: description...``** means that it is still a work-in-process and needs to be updated.  It must be followed by descriptive text describing the issue to be fixed.  If you want to to show in the page you will need add a separate line. 
* Use **\`\`\literal text blocks\`\`** when describing preference values  - ``literal text blocks``
* Use **\:menuselection\:\`Menu \-\-\> Preferences \-\-\> ..\`** for menu descriptions - :menuselection:`Menu --> Preferences --> ..` 
* Use **\:guilabel\:\`\GUI labels\`** for buttons  - :guilabel:`GUI labels`
* For dates, use dd-mmm-yyyy or yyyy-mm-dd to avoid confusion with the way dates are uniquely written in the US. |br|\ e.g. 2-Mar-2022 or 2022-3-2, not 2-3-2022 
* Heading levels:

  * **#########** with overline, for parts - not really used
  * \*\*\*\*\*\*\*\*\*\*\*\* Page Titles
  * **=========** for sections
  * **----------------------** for subsections (hyphen)
  * **\^\^\^\^\^\^\^\^\^\^** for subsubsections
  * **\~\~\~\~\~\~\~\~\~\~** for paragraphs
  * only if really needed (i.e. avoid): 
  
     * **\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'** for sub paragraphs
     * **\_\_\_\_\_\_\_\_\_\_\_\_** for sub-sub-paragraphs (hyphens)

* To force a :

  * Line break/new line use **\|br\|**
  * Non-breaking space use **\|_\|**
  * Blank line use **\|** on its own line
  * Paragraph break that a 'float right' element must not be placed before a point use **\|force-break\|**  |br| useful if the 'float right' element is being placed beside another 'float right' element, rather than below.

* To add a horizontal line, use **\-\-\-\-** (four hypens) on its own line
* 