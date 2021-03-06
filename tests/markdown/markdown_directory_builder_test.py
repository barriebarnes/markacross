import os
import unittest
from tests.test_framework.fixture import Fixture
from mock import MagicMock
from tests.test_framework.mock_container import MockContainer
from doc_builder.markdown_directory_builder import MarkdownDirectoryBuilder
from doc_builder.markdown_file_builder import MarkdownFileBuilder
from doc_builder.markdown_index import MarkdownIndex
import pprint

class MarkdownFileBuilderTest(unittest.TestCase):
    """
    Test the markdown file builder class
    """

    def setUp(self):
        self.container = MockContainer().get()
        self.set_up_mock_container()
    
    def set_up_mock_container(self):        
        # Set up mock markdown_index object
        mock_markdown_index = MarkdownIndex(self.container)
        index_filename = "abc/def_index.md"
        mock_markdown_index.build = MagicMock(return_value=index_filename)
        self.container.put_variable("MarkdownIndex", mock_markdown_index)

        # Set up mock markdown_file_builder object
        mock_markdown_file_builder = MarkdownFileBuilder(self.container)
        markdown_filename = "code_1.md"
        mock_markdown_file_builder.build = MagicMock(return_value=markdown_filename)
        self.container.put_variable("MarkdownFileBuilder", mock_markdown_file_builder)

    def test_build(self):
        # Build expected results
        test_file_1 = Fixture().get_fixture_path("directory_builder_test/code_1.txt")
        test_directory = os.path.dirname(test_file_1)
        expected_file_contents = """## Documentation for %s.
<sup><i>This file is automatically generated.</i></sup>

AAA

BBB

CCC
""" % test_file_1

        # Create markdown
        markdown_directory_builder = MarkdownDirectoryBuilder(self.container)
        markdown_filename = markdown_directory_builder.build(test_directory)
        
        # Check markdown file contents are as expected
        fp = open(markdown_filename, 'r')
        markdown_result = fp.read()
        fp.close()        
        self.assertEqual(expected_file_contents, markdown_result)
        pprint.pprint(markdown_result)
        
        os.remove(markdown_filename)
        