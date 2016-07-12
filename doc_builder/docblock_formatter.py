class DocBlockFormatter(object):
    """ M<<<<<<<<<<<<<<<<<<<<<<<<<
    # Class: DocBlockFormatter
    Reformats text lines when formatted as part of a DocBlock
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>M """

    def __init__(self):
        self.params_section = False

    def reformat_line(self, line):
        """ M<<<<<<<<<<<<<<<<<<<<<<<<<
        ### Method: format_line
        Handles all lines beginning "param", "return" and "throws".
        Strips the "@", capitalises and emboldens the key word.

        @param string line
        
        @return string - reformatted line
        >>>>>>>>>>>>>>>>>>>>>>>>M """
        line = self._reformat_param(line)
        line = self._reformat_return(line)
        line = self._reformat_throws(line)
        return line
    
    def _reformat_param(self, line):
        """
        If "@param" found in the line, put "Parameters" in bold above the first such line and strip "@param" from the line
        """
        if '@param' not in line:
            return line
        line = line.replace('@param ', '')
        if self.params_section:
            return "%s  " % line
        else:
            self.params_section = True
            self.tempx = "Y"
            return "__Parameters:__\n%s" % line

    def _reformat_return(self, line):
        if '@return' in line:
            self.params_section = False
        return line.replace('@return', '__Returns:__')

    def _reformat_throws(self, line):
        if '@throws' in line:
            self.params_section = False
        return line.replace('@throws', '__Throws:__')
