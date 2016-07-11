import fileinput

class Exemptions(object):
    """ M<<<<<<<<<<<<<<<<<<<<<<<<<<
    For speed and so as not to pick up any extraneous markdown files, a set of folders can be exempted.
    The names of these are held in the file 'config/exemptions/exempt_files.txt'
    >>>>>>>>>>>>>>>>>>>>>>>>>>M """
    def __init__(self):
        self.exempt_folders = []
        exempt_folders_file = 'config/exemptions/exempt_files.txt'
        for line in fileinput.input(exempt_folders_file):
            line = line.strip()
            if line == "":
                continue
            self.exempt_folders.append(line)

        fileinput.close()
        
    def get(self):
        """ M<<<<<<<<<<<<<<<<<<<<<<<<<<
        Having read in the list of exempt folders, return it. These will be ignored when building markdown.
        
        @return list - exempt files & folders
        >>>>>>>>>>>>>>>>>>>>>>>>>>M """
        return self.exempt_folders
        