from config.container.container import Container
from config.exemptions.exemptions import Exemptions
from doc_builder.markdown_extractor import MarkdownExtractor
from doc_builder.markdown_file_builder import MarkdownFileBuilder
from doc_builder.markdown_directory_builder import MarkdownDirectoryBuilder
from doc_builder.markdown_index import MarkdownIndex
from doc_builder.docblock_formatter import DocBlockFormatter

def get_filled_container():
    container = Container()
    fill_container(container)
    return container

def fill_container(container):    
    container.put_factory("Exemptions", lambda: Exemptions())
    container.put_factory("MarkdownExtractor", lambda x: MarkdownExtractor(x))
    container.put_factory("MarkdownFileBuilder", lambda x: MarkdownFileBuilder(x))
    container.put_factory("MarkdownDirectoryBuilder", lambda x: MarkdownDirectoryBuilder(x))
    container.put_factory("MarkdownIndex", lambda x: MarkdownIndex(x))
    container.put_factory("DocBlockFormatter", lambda: DocBlockFormatter())
    
