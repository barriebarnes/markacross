import os

class Fixture:
    def get_fixture_path(self, name):
        """
        Generates the full path for the given fixture filename, checks it exists and returns the path
        """
        current_folder = os.path.dirname(os.path.realpath(__file__))
        test_folder = current_folder.replace("/test_framework", "")
        fixture_file = "%s/fixtures/%s" % (test_folder, name)
        if not os.path.exists(fixture_file):
            raise ValueError("Couldn't find fixture file: %s" % fixture_file)
        return fixture_file
    
