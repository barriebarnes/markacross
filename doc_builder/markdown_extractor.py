import fileinput
import re
import pprint

class MarkdownExtractor(object):
    """ M<<<<<<<<<<<<<<<<<<<<<<<<<
    # Class: MarkdownExtractor
    Extracts all Markdown from a given file
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>M """

    def __init__(self, container):
        self.container = container

    def extract(self, filename):
        """ M<<<<<<<<<<<<<<<<<<<<<<<<<
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

        @param string filename
        
        @return array - paragraphs of Markdown extracted from the given file
        >>>>>>>>>>>>>>>>>>>>>>>>M """
        markdown_found = False
        self.markdown_paragraphs = []
        paragraph = ""
        line_num = 0
        self.doc_block_prefix = None
        docblock_formatter = self.container.get("DocBlockFormatter")
        for line in fileinput.input(filename):
            line_num += 1
            self._check_for_docblock_start(line)
            self._check_for_docblock_end(line)
            line = docblock_formatter.reformat_line(line)
            
            if self._is_end_marker(line):
                if markdown_found:
                    markdown_found = False
                    self.markdown_paragraphs.append(paragraph)
                    paragraph = ""
                else:
                    self.markdown_paragraphs.append("On line %i, markdown end-marker found without a previous start-marker in file %s\n" % (line_num, filename))
                    
            elif self._is_start_marker(line):
                if not markdown_found:
                    self._determine_start_marker_line_offset(line)
                    markdown_found = True
                else:
                    self.markdown_paragraphs.append("On line %i, markdown start-marker found when expecting an end-marker in file %s\n" % (line_num, filename))
                    
            elif markdown_found:
                line = self._remove_line_prefix(line)
                paragraph = self._add_markdown_line_to_paragraph(line, paragraph)

        fileinput.close
        
        # Capture remaining markdown (if any)
        if paragraph != "":
            self.markdown_paragraphs.append(paragraph)

        return self.markdown_paragraphs
                    
                
    def _check_for_docblock_start(self, line):
        """
        Checks whether the given line is the start of a DocBlock and, if so, records its style
        N.B. this is needed to remove (for example) stars from the start of all subsequent lines
        """
        patn = re.compile('^[ \t]*\/\*\*')
        match = patn.match(line)
        if match:
            self.doc_block_prefix = "\*"        

    def _check_for_docblock_end(self, line):
        """
        Checks whether the given line is the end of a DocBlock and, if so, reset its style record
        """
        patn = re.compile('[\s\S]*\*\/[ \t]*[\r\n]+$')
        match = patn.match(line)
        if match:
            self.doc_block_prefix = None       

    def _is_start_marker(self, line):
        """
        Check for a line that starts a comment and contains > 10 ">" characters
        e.g. /* M<<<<<<<<<
        """
        patn = re.compile('(^[\s\S]*[Mm]{1}[<]{10,})[ \t]*[\r\n]+$')
        match = patn.match(line)
        return (match != None) 
    
    def _is_end_marker(self, line):
        """
        Check for a line that ends a comment and contains > 10 ">" characters
        e.g. >>>>>>>>>M */
        """
        patn = re.compile('^[ \t]*[>]{10,}[Mm]{1}[\t \S]*[\S]+[ \t]*[\r\n]+$')
        match = patn.match(line)
        return (match != None) 
    
    def _determine_start_marker_line_offset(self, line):
        """
        Count the number of spaces before the start marker in the given line.
        """
        offset = self._count_leading_white_spaces(line)
        self.line_offset = offset
        
    def _remove_line_prefix(self, line):
        """
        If there's leading white space on the string, strip off as much as was found for the paragraph's start marker.
        The property self.line_offset was set to this value.
        Also remove any doc_block prefix that maybe applied
        """
        leading_spaces_count = self._count_leading_white_spaces(line)
        min_offset = min(leading_spaces_count, self.line_offset)
        line = line[min_offset:]
        
        if self.doc_block_prefix == None:
            return line
        else:
            patn = re.compile('^\s*' + self.doc_block_prefix + '[ ]?([\s\S]*)$')
            match = patn.match(line)
            if match == None:
                return line
            else:
                return match.group(1)
        
    def _add_markdown_line_to_paragraph(self, line, paragraph):
        """
        Add the given line to the given paragraph appending a line feed in the process.
        """
        return paragraph + line
        
    def _count_leading_white_spaces(self, line):
        """
        Determine the number of spaces at the start of the given line.
        Expand tabs into 4 spaces (might not always be the case but at least internally consistent)
        """
        patn = re.compile('^(\s*)[\s\S]*$')
        match = patn.match(line)
        starting_spaces = match.group(1)
        starting_spaces = starting_spaces.replace("\t", "    ")
        return len(starting_spaces)
        