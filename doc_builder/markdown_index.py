import os
import fileinput
import re
import pprint

class MarkdownIndex(object):
    """ M<<<<<<<<<<<<<<<<<<<<<<<<<<
    A markdown page that acts as an index to a number of other markdown files typically contained within the 
    same folder or its immediate sub-folders
    >>>>>>>>>>>>>>>>>>>>>>>>>>M """
    
    def __init__(self, container):
        self.container = container
        
    def build(self, folder_path, handmade_markdown_files, auto_gen_markdown_files, sub_directory_indexes):
        """ M<<<<<<<<<<<<<<<<<<<<<<<<<<
        Create a markdown file containing an index comprising a list of handmade_markdown_files
        followed by a list of automatically generated markdown files and then a list of sub-directory indexes.
        
        @param string folder_path
        @param list handmade_markdown_files - contains the filename of each manually created md file
        @param list auto_gen_markdown_files - contains the filename of each automatically generated md file
        @param list sub_directory_indexes - contains the filepath of an md index for each sub-folder with markdown
        
        @return string - the index filename
        >>>>>>>>>>>>>>>>>>>>>>>>>>M """
        # If there are no markdown files present in this or any sub-folders, return None as no index is required
        if len(handmade_markdown_files) == 0 and len(auto_gen_markdown_files) == 0 and len(sub_directory_indexes) == 0:
            return None
        
        # Generate the index file
        folder_path_parts = folder_path.split('/')
        base_dirname = folder_path_parts[-1]
        markdown = "## Index for folder: %s\n_This file is automatically generated._\n\n" % base_dirname
        markdown = self._add_handmade_markdown_files_list(markdown, folder_path, handmade_markdown_files)
        markdown = self._add_auto_gen_markdown_files_list(markdown, auto_gen_markdown_files)
        markdown = self._add_sub_directory_indexes_list(markdown, folder_path, sub_directory_indexes)

        index_filename = self._generate_index_filename(folder_path, base_dirname)
        self._write_index(index_filename, markdown)
        return index_filename

    def _add_handmade_markdown_files_list(self, markdown, folder_path, handmade_markdown_files):
        if len(handmade_markdown_files) > 0:
            markdown += "Documentation for this folder:  \n"
            for handmade_markdown_file in handmade_markdown_files:
                title = self._get_markdown_title("%s/%s" % (folder_path, handmade_markdown_file))
                link = handmade_markdown_file
                markdown += "* [%s](%s)\n" % (title, link)

        return markdown + "\n"
            
    def _add_auto_gen_markdown_files_list(self, markdown, auto_gen_markdown_files):
        if len(auto_gen_markdown_files) > 0:
            markdown += "Documentation for code in this folder:  \n"
            for auto_gen_markdown_file in auto_gen_markdown_files:
                title = self._get_markdown_title(auto_gen_markdown_file)
                link = auto_gen_markdown_file
                markdown += "* [%s](%s)\n" % (title, link)

        return markdown + "\n"
        
    def _add_sub_directory_indexes_list(self, markdown, folder_path, sub_directory_indexes):
        if len(sub_directory_indexes) > 0:
            markdown += "Documentation for sub-folders:  \n"
            for sub_directory_index in sub_directory_indexes:
                title = self._get_markdown_title(sub_directory_index)
                (path, filename) = os.path.split(sub_directory_index)
                path_parts = path.split('/')
                dir_name = path_parts[-1]
                link = "%s/%s" % (dir_name, filename)
                markdown += "* [%s](%s)\n" % (title, link)

        return markdown + "\n"
        
    def _get_markdown_title(self, markdown_file):
        """
        Return the first line of the given file having stripped off any leading #'s or spaces.
        Truncate the result to 50 chars
        """
        for line in fileinput.input(markdown_file):
            title = line
            break;
        fileinput.nextfile()
        
        matches = re.match(r'^[#]*[ ]*([ \S]+)\n$', title)
        title = matches.group(1)
        title = title[:50]
        title = title.replace("\n", "")
        return title
        
    def _generate_index_filename(self, folder_path, base_dirname):
        return "%s/%s_index.md" % (folder_path, base_dirname)
    
    def _write_index(self, index_filename, markdown):
        fp = open(index_filename, 'w')
        fp.write(markdown)
        fp.close()