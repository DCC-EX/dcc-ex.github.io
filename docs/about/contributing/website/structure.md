\|EX-CONTRIBUTING-LOGO\|

# Folder and Page Structure

\|SUITABLE\| \|conductor\| \|tinkerer\| \|engineer\|

:::: {.sidebar .sidebar-on-this-page}

::: {.contents depth="4" local=""}
On this page
:::
::::

This page aims to describe the preferred general structure of how files
(pages, images, downloads etc.) should be arranged and named, along with
the preferred structure of the individual pages.

By being consistent with these, it will be a) a better user experience,
and b) be easier to maintain the documentation.

## reStructuredText Standards

Please ensure to follow the standards below when creating or updating
documentation to ensure the look and feel of the website remains
consistent.

## Elements

The elements of the documentation fall into the following broad
categories:

- [Folders](#folders)
- [Pages](#pages)
- `about/contributing/website/basic-rst:Image Types`{.interpreted-text
  role="ref"}
- `about/contributing/website/basic-rst:Documents / Files`{.interpreted-text
  role="ref"}
- `about/contributing/website/basic-rst:Image Artifacts / Original Grpahics`{.interpreted-text
  role="ref"} (used to create the images, but not part of the
  documentation)

## Folders

Folders *follow* the basic structure:

- Folder name
  - index.rst
  - getting-started.rst or overview.rst
  - \.

Every folder SHOULD have a \'index.rst\' file which is the primary
navigation point for the pages in the folder \|BR\| There are exceptions
to this rule, but use them carefully.

Every folder SHOULD have either a \'getting-started.rst\' OR and
\'overview.rst\' file which is the second navigation point for the pages
in the folder \|BR\| There are exceptions to this rule (e.g. the
Throttle options), but use them carefully.

## Pages

Pages *generally* follow the basic structure:

- Page Name (.rst file)
  - [Meta Keywords](#meta-keywords)
  - [Includes](#includes)
  - [Product Icon](#product-icon) (where appropriate)
  - [Page Heading](#page-heading)
  - [Level Logos](#level-logos)
  - [GitHub Issues Link](#github-issues-link)
  - [On This Page - Table of
    Contents](#on-this-page---table-of-contents) (on longer pages with
    multiple headings)
  - [Page Content](#page-content)
    - `about/contributing/website/structure:page heading`{.interpreted-text
      role="ref"}
    - Description or purpose of the page
    - `Other headings <about/contributing/website/structure:page heading>`{.interpreted-text
      role="ref"}
      - Text, links, images, etc.
      - \...
    - Next Steps Heading (if it is part of sequence of pages this is
      mandatory)

### Meta Keywords

The meta keywords help search entries find find the page based on key
words.

By using the recommended includes (below) several key meta keywords are
included in all pages. i.e. `DCC-EX DCC DCC++ EX DCC++EX` Generally each
page should start with any additional meta keywords that are appropriate
to the page.

For example, the meta tags for levels.rst are:

::: admonition
Example

``` rst

:keywords: Levels Conductor Tinkerer Engineer
```
:::

### Includes

All pages MUST include two standard include files.
`/include/include.rst` and, depending on the depth in the folder
structure, one of following as the second file:

- `/include/include-l0.rst`
- `/include/include-l1.rst`
- `/include/include-l2.rst`
- `/include/include-l3.rst`

For example:

::: admonition
Example

``` rst
--8<-- "/include/include.md"
--8<-- "/include/include-l2.md"
--8<-- "/include/include-description.md"
```
:::

:::: {.note .note-float-right}
::: title
Note
:::

The \'include-description.rst\' will add a generic HTML meta
*description* to the page. You can alternately make use of one the the
other include files,or create a new one, to have different description
for the page.
::::

### Product Icon

If the page specifically, and only, relates to one of the \|DCC-EX\|
products, then specify the product icon immediately after include files,
by using the appropriate expansion:

For example:

::: admonition
Example

``` rst
--8<-- "/include/include.md"
--8<-- "/include/include-l3.md"
--8<-- "/include/include-description.md"
|EX-CS-LOGO|

***************************************
```
:::

### Page Heading

Each page must have a Main Heading. Main Headings MUST have asterisks
above and below them:

::: admonition
Example

``` rst
*************
Main Heading
*************
```
:::

See below for more information about heading.

### Level logos

On our `/begin/levels`{.interpreted-text role="doc"} page, we refer to
Conductor, Tinkerer, and Engineer level users, and where possible, we
should be using these logos to help users understand what level the
documentation is targeted at.

There are two types of logos available, one suitable for callouts or
panels which are simply a square graphic, and one suitable for page
headings that contains the graphic and the text.

- Where possible, use the expansions for the level images:
  - \|conductor\| \|conductor\|
  - \|tinkerer\| \|tinkerer\|
  - \|engineer\| \|engineer\|
  - \|conductor-no-text\| \|conductor-no-text\|
  - \|tinkerer-no-text\| \|tinkerer-no-text\|
  - \|engineer-no-text\| \|engineer-no-text\|
- Where possible, use the Team and Product names the expansions (not
  possible in headings)
  - \|DCC-EX\| for \|DCC-EX\|
  - \|EX-CS\| for \|EX-CS\|
  - \|EX-I\| for \|EX-I\|
  - \|EX-R\| for \|EX-R\|
  - \|EX-TT\| for \|EX-TT\|
  - \|EX-DCCI\| for \|EX-DCCI\|
  - \|BSC\| for \|BSC\|
- Where possible, use the expansions for the level text
  - \|conductor-text\| \|conductor-text\|
  - \|tinkerer-text\| \|tinkerer-text\|
  - \|engineer-text\| \|engineer-text\|

Only if really necessary use image tags:

``` 
![](/_static/images/conductor.png)
  :alt: Conductor Level
  :scale: 40%

![](/_static/images/conductor-level.png)
  :alt: Conductor Level 
  :scale: 40%
```

Refer to `about/contributing/website/basic-rst:images`{.interpreted-text
role="ref"} below for details on how to include images, and set the
scale as appropriate. A good example of the use of the different types
of logos is the \|EX-TT\| `/ex-turntable/assembly`{.interpreted-text
role="doc"} page.

------------------------------------------------------------------------

### GitHub Issues Link

It is recommended to include links to the appropriate product\'s GitHub
issue templates by using the appropriate expansion on the same line as
the \'Level\' expansions.

- \|githublink-ex-turntable\|
- \|githublink-ex-turntable-button\|
- \|githublink-ex-turntable-button2\|
- \|githublink-ex-dccinspector-button\|
- \|githublink-ex-dccinspector-button2\|
- \|githublink-ex-webthrottle-button\|
- \|githublink-ex-webthrottle-button2\|
- \|githublink-ex-installer-button\|
- \|githublink-ex-installer-button2\|
- \|githublink-ex-commandstation-button\|
- \|githublink-ex-commandstation-button2\|

------------------------------------------------------------------------

### On This Page - Table of Contents

Pages with multiple headings should generally have a Table of Contents.
The depth of the table is a subjective decision.

``` 

   :class: sidebar-on-this-page

   
      :depth: 4
      :local:
```

------------------------------------------------------------------------

### Page Content

Page content can include:

- [Headings and Sub Headings](#headings-and-sub-headings)
- [Text](#text)
- `about/contributing/website/basic-rst:Links / Hyperlinks`{.interpreted-text
  role="ref"}
- `about/contributing/website/basic-rst:Tables`{.interpreted-text
  role="ref"}
- `about/contributing/website/basic-rst:images`{.interpreted-text
  role="ref"}

After the heading, the page should start with an explanation of the
purpose of the page.

#### Headings and Sub Headings

- Main Headings have asterisks above and below them:

  ``` 
  ************
  Main Heading
  ************
  ```

- Subheadings are underlined with equals signs:

  ``` 
  Subheading
  ==========
  ```

- The next level is underlined with hyphens:

  ``` 
  Next level
  ----------
  ```

- And the next level is underlined with carets:

  ``` 
  Next level
  ^^^^^^^^^^
  ```

- The next one we use is underlined with tildes:

  ``` 
  Next level
  ~~~~~~~~~~
  ```

- The last one we use is underlined with underscores:

  ``` 
  Next level
  __________
  ```

All heading underlines and overlines must be at least as long as the
text of the heading text.

------------------------------------------------------------------------

#### Text

Refer to the `/about/contributing/website/basic-rst`{.interpreted-text
role="doc"} and
`/about/contributing/website/style-guide`{.interpreted-text role="doc"}

\|HR-HEAVY\|

## Next steps - ReStucturedText Basics

Click next to learn how to enhance your content with links, tales,
images, etc.
