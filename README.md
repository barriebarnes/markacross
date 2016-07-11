# Markacross Introduction
The Markacross documentation system lets project repos to be a canonical source of both software and software explanation. It allows documentation to be embedded both in and amongst source code files thereby helping resolve issues of the two being out of sync.

Markacross is built upon the popular Markdown markup language. This being chosen partially because of its good support within GitHub - where Markdown (md) files are automatically rendered on the repo's web pages.

The Markacross compiler extracts documentation from within the source code and builds a hierarchy of Markdown files with menus linking everyting together.

Unlike solutions such as Javadoc and PHPDoc, Markacross is programming language neutral. It works equally in Java, PHP, Javascript, Python, CSS and other languages.

Nonetheless, Markacross can be used in conjunction with these common documentation systems such that it can be embedded inside DocBlocks or be the whole DocBlock where required.

## Markacross Basics
Within the Markacross system, documentation is held in two forms:
* Standalone Markdown files with no special constraints
* Markdown embedded into source files with distinctive headers and footers
Embedded Markdown should be held within a comment block and commence with "M<<<<<<<<<<" and end with ">>>>>>>>>>M". For example (in Java, PHP or Javascript):

```
/* M<<<<<<<<<<<<<<<<<<<<
#### Some Title
Some explanation
* Point 1 in a list
* Point 2 in a list
>>>>>>>>>>>>>>>>>>>>>>>M */
```

which produces:
#### Some Title
Some explanation
* Point 1 in a list
* Point 2 in a list

Equally, the DocBlock below produces exactly the same Markdown:
```
/** M<<<<<<<<<<<<<<<<<<<<
 *  #### Some Title
 *  Some explanation
 *  * Point 1 in a list
 *  * Point 2 in a list
 >>>>>>>>>>>>>>>>>>>>>>>M */
```

As does this Python example:
```
""" M<<<<<<<<<<<<<<<<<<<<
#### Some Title
Some explanation
* Point 1 in a list
* Point 2 in a list
>>>>>>>>>>>>>>>>>>>>>>>M """
```

## Markacross Compilation
At any time, the Markacross compiler can be run to produce the repo's documentation. This does the following:
* For each code file that contains Markacross, generates and concatenates Markdown which is placed in a Markdown file.
* For each folder that contains Markdown files, generates a Markdown menu file with links to each file. This menu file also includes links to sub-folders that contain markdown.

The result is a Markdown menu in the repo's root folder that links to a hierarchy of markdown files.

All automatically generated Markdown files begin with a comment indicating they shouldn't be changed manually. At the start of Markacross compilation, all such files are deleted before recreation.

## Running the Markacross Compiler
The Markacross compiler can be obtained by cloning the Markacross repo.

To run the compiler to generate Markdown, enter:
```
$ markacross -s source_folder
```
To initiate the deletion of previously generated Markdown (leaving hand created Markdown untouched), enter:
```
$ markacross -s source_folder -d
```
