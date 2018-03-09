---
title: A brief history of Markdown
layout: 2018
---

Formal markup languages
-----------------------

    informal        /---------formatted text----------\        formal
    <------v-------------v-------------v-----------------------v---->
     plain text     informal markup   formal markup    binary format
                    (Markdown)        (HTML, XML, etc.)

- Text vs binary
  - Text
    - If an editor understands a text encoding, it can display the data
    - One corrupted byte doesn't cause failure to parse
  - Binary requires specialised parser and (probably) viewer
  - Binary good for non-textual data but not always interoperable; one bad byte can cause complete failure to process
- Character overloading
- Markup languages usually written for programs to process, not humans

Informal markup languages
-------------------------

- Don't need technical knowledge
- Easy for humans to enter
- Can use basic text editor
- Few security implications

Markdown
========

- Syntax
  - Headers
  - Unordered lists
  - Inline code
  - Code blocks (orig. indented style)
  - Links
    - Inline
    - Reference
  - Images
  - Quotes
- Q. What is Markdown?
  - Lightweight markup language
  - Perl script
    - "The code is the spec"
    - In beta
    - Unmaintained
  - Text-to-HTML convertor
  - Ambiguous
  - NOT formally specified
  - NOT test suite
  - It's flawed but it filled a need, for writers not programmers
  - Have you seen text formats for programmers?!
    - reStructuredText
    - LaTeX
- Gruber's version 1.0.1
- Flaws
  - Ambiguous
  - Paragraph-based, not line-based
  - Intraword emphasis
  - No auto-linking
- Flavours
  - CommonMark
  - GFM
  - Pandoc Markdown
    - Fenced code blocks
    - Citations

Pandoc
======

- CLI

R Markdown
==========

- YAML header
- Body
- Code
  - Useful setup

Example
=======

- Text
  - Inline R code
- Citations
- Pandoc YAML extras
- Plot
- Data table

Links
=====

- <https://blog.codinghorror.com/responsible-open-source-code-parenting/>
- <https://blog.codinghorror.com/the-future-of-markdown/>
- <https://blog.codinghorror.com/standard-flavored-markdown/>
- <https://blog.codinghorror.com/standard-markdown-is-now-common-markdown/>
- <https://github.github.com/gfm/>
- <https://twitter.com/davewiner/status/508957733811265537>
- <https://tools.ietf.org/html/rfc7763>
- <https://tools.ietf.org/html/rfc7764>
- <http://johnmacfarlane.net/babelmark2/?text=%23+Hello+there%0A%0AThis+is+a+paragraph.%0A%0A-+one%0A-+two%0A-+three%0A-+four%0A%0A1.+pirate%0A2.+ninja%0A3.+zombie>
