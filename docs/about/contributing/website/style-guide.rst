.. include:: /include/include.rst
.. include:: /include/include-l2.rst
*************
Style Guide
*************

|conductor| |tinkerer| |engineer|

.. sidebar::

   .. contents:: On this page
      :depth: 2
      :local:

This page aims to ...

Text and Style Standards
========================

Please ensure to follow the standards below when creating or updating documentation to ensure the look and feel of the website remains consistent.

.. highlight:: rst



Style Guidelines
________________

* every page (except a few pages like home, about, contact, etc.) MUST start with one or more level images (after the title) to indicate the intended base audience for the page. 
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

* Where possible, use the expansions for the level text 

  * \|conductor-text\| |conductor-text|
  * \|tinkerer-text\| |tinkerer-text|
  * \|engineer-text\| |engineer-text|

* Use British/Australian/Canadian/Indian (pretty much every except the USA) spelling e.g. 'colour' not 'color'.  |br|\ (Primarily because it is used in more English speaking countries)
* Preferred Terms:
  
  * Use **"Motor Driver"**, not "Motor Shield", "Motor Board", "Motorboard"
  * In general use **'loco'** instead of 'locomotive' or 'engine'

*	Use railroad/railway terminology that is understandable by all English-speaking people. |br|\ Where there are clear differences from US to non-US terminology use both with a slash between and use the US version first. e.g. turnouts/points, consists/multiple units, switching/shunting.
*	No full stop at the end of a numbered or unnumbered list
*	Numbered lists should generally only be used if they are describing a specific sequence, or the numbering is important to the text
* Use first person (you and your; not I, me, my or am) language
*	A string of nouns should be generally be sequenced in alphabetic order, unless it makes more sense within the context to display them in some other sequence
* Double quotes (") should only be used for quoting text from people, documents or web sites
*	No quotes around 'Also See' type references
*	Avoid '(above)' or '(below)' in text.  Use hypertext links instead
*	**``.. todo:: description...``** means that it is still a work-in-process and needs to be updated.  It may be followed by descriptive text in italics describing the issue to be fixed.  If you want to to show in the page you will need add a separate line 
* Use **\`\`\literal text blocks\`\`** when describing preference values  - ``literal text blocks``
* Use **\:menuselection\:\`Menu --> Preferences --> ..\`** for menu descriptions - :menuselection:`Menu --> Preferences --> ..` 
* Use **\:guilabel\:\`\GUI labels\`** for buttons  - :guilabel:`GUI labels`
* For dates, use dd-mmm-yyyy or yyyy-mm-dd to avoid confusion with the way dates are uniquely written in the US. |br|\ e.g. 2-Mar-2022 or 2022-3-2, not 2-3-2022 
* Heading levels:

  * **#########** with overline, for parts - not really used
  * \*\*\*\*\*\*\*\*\*\*\*\* Page Titles
  * **=========** for sections
  * **\_\_\_\_\_\_\_\_\_\_\_\_** for subsections  (underscore)
  * **\^\^\^\^\^\^\^\^\^\^** for subsubsections
  * **\~\~\~\~\~\~\~\~\~\~** for paragraphs
  * only if really needed (i.e. avoid): 
  
     * **\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'\'** for sub paragraphs
     * **----------------------** for sub-sub-paragraphs (hyphens)

* To force a :

  * Line break/new line use **\|br\|**
  * Non-breaking space use **\|_\|**
  * Paragraph break that a 'float right' element must not be placed before a point use **\|force-break\|**  |br| useful if the 'float right' element is being placed beside another 'float right' element, rather than below.