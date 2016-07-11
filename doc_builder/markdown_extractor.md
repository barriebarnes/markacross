## markdown_extractor.py
_This file is automatically generated._

# Class: MarkdownExtractor
Extracts all Markdown from a given file

### Method: extract
Reads the given file and extracts and concatenates all markdown and returns it as an array of paragraphs.
Markdown is held between the following lines
```
/* M<<<<<<<<<
>>>>>>>>>M */
```
where there should be 10 or more "<" or >" signs.
N.B. the markdown between these two boundaries is referred to as a paragraph.
As most Markdown will be indented to match the surrounding code, that indentation is removed during extraction.
As some Markdown will be contained with DocBlocks with a leading "*", this too is removed during extraction.
DocBlock syntax is formatted appropriately
__Parameters__
        string filename

__Returns__ array - paragraphs of Markdown extracted from the given file
