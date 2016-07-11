from tests.test_framework.fixture import Fixture
from config.container.fill_container import get_filled_container
from doc_builder.markdown_file_builder import MarkdownFileBuilder
import argparse
import pprint

def fetch_args():
    parser = argparse.ArgumentParser(description="Generate a hierarchy of markdown documentation gleaned from the given codebase")
    parser.add_argument('-d', '--delete', action='store_true', help='delete previously generated markdown files')
    parser.add_argument('-s', '--source', required=True, help='the path to the source files containing markdown to be extracted')
    
    args = parser.parse_args()
    
    return args    


"""
Initiate automatic markdown generation with:
   > markacross -s source_folder
Initiate the deletion of previously generated markdown (leaving hand created markdown untouched) with:
   > markacross -s source_folder -d
"""
if __name__ == '__main__':
    container = get_filled_container()

    args = fetch_args()

    markdown_directory_builder = container.get("MarkdownDirectoryBuilder", [container])
    markdown_index = markdown_directory_builder.build(args.source, args.delete)
    if args.delete:
        pprint.pprint("Markdown successfully deleted.")
    else:
        pprint.pprint("Markdown successfully generated. Top level index: %s" % markdown_index)

    # Embryonic e2e test code
    #test_file_1 = Fixture().get_fixture_path("markdown_test_1.txt")
    #test_file_1 = '/Users/barriebarnes/dev/rmh_api_client/src/RmhApiClient/Service/ServiceEndpoints/UltraViolet.php'
    #markdown_file_builder = container.get("MarkdownFileBuilder", [container])
    #markdown_filename = markdown_file_builder.build(test_file_1)
    #pprint.pprint(markdown_filename)

