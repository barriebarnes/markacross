import unittest
from config.container.container import Container

class ContainerTest(unittest.TestCase):
    """
    Test the Dependency Injection Container class
    """

    def test_container_variable(self):
        container = Container()
        
        expected_value = 25
        container.put_variable("TestVariable", expected_value)
        self.assertEqual(expected_value, container.get("TestVariable"))

    def test_container_singleton(self):
        container = Container()
        
        container.put_singleton("TestClass", lambda x: TestClass(x))
        expected_value = 4
        test_class = container.get("TestClass", [expected_value])
        self.assertEqual(expected_value, test_class.test_get())
        
        same_test_class = container.get("TestClass", [9])
        self.assertEqual(test_class, same_test_class)
        self.assertEqual(expected_value, same_test_class.test_get())  # Ensure no new instance is created & original expected value returned

    def test_container_factory(self):
        container = Container()
        
        container.put_factory("TestClass", lambda x: TestClass(x))
        expected_value = 4
        test_class = container.get("TestClass", [expected_value])
        self.assertEqual(expected_value, test_class.test_get())
        
        new_expected_value = 9
        new_test_class = container.get("TestClass", [new_expected_value])
        self.assertNotEqual(test_class, new_test_class)
        self.assertEqual(new_expected_value, new_test_class.test_get())  # Ensure new instance is created & original expected value returned

 
class TestClass(object):
    """
    Test class for use with ContainerTest
    """
    def __init__(self, initial_val):
        self.initial_value = initial_val
     
    def test_get(self):
        return self.initial_value 
    