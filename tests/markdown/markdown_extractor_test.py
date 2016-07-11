import unittest
from tests.test_framework.fixture import Fixture
from doc_builder.markdown_extractor import MarkdownExtractor
import pprint

class MarkdownExtractorTest(unittest.TestCase):
    """
    Test the markdown extractor class
    """

    def setUp(self):
        self.test_file_1 = Fixture().get_fixture_path("markdown_test_1.txt")
    
    def test_extract(self):
        expected_markdown = ['Markdown para 1 line 1\nMarkdown para 1 line 2\nMarkdown para 1 line 3\n',
                             'Markdown para 2 line 1\n  Markdown para 2 line 2\nMarkdown para 2 line 3\n',
                             'On line 18, markdown end-marker found without a previous start-marker in file /Users/barriebarnes/dev/markacross/tests/fixtures/markdown_test_1.txt\n',
                             'On line 24, markdown start-marker found when expecting an end-marker in file /Users/barriebarnes/dev/markacross/tests/fixtures/markdown_test_1.txt\n',
                             'Markdown para 3 line 1\nMarkdown para 3 line 2\n'
                             ]
        extracted_markdown = MarkdownExtractor().extract(self.test_file_1)
        self.assertEqual(expected_markdown, extracted_markdown)
