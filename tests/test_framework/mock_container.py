from config.container.container import Container

class MockContainer(object):
    def __init__(self):
        self.mock_container = Container()

    def get(self):
        return self.mock_container
