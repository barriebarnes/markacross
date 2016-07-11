class Container(object):
    """
    A simple service injection container.
    """
    def __init__(self):
        self.variables = {}
        self.singletons = {}
        self.factories = {}
        self.singleton_instances = {}
        
    def put_variable(self, name, variable):
        """
        Put the given variable name/value pair into the container's variables dictionary
        """
        self.variables[name] = variable
    
    def put_singleton(self, name, object_builder):
        """
        Put the given name/object_builder pair into the container's singletons dictionary
        """
        self.singletons[name] = object_builder
    
    def put_factory(self, name, object_builder):
        """
        Put the given name/object_builder pair into the container's factories dictionary
        """
        self.factories[name] = object_builder
    
    def get(self, name, params=[]):
        """
        Find the first variable, singleton or factory in the container that matches the given name.
        For a variable, return it. 
        For a singleton, see if an object has already been created and if so return it, otherwise build and return a new one.
        For a factory, create an object with the stored object builder and return it.
        """
        if name in self.variables:
            return self.__find_variable(name)

        if name in self.singletons:
            return self.__find_singleton(name, params)
            
        if name in self.factories:
            return self.__find_factory(name, params)
        
        raise Exception("Couldn't find container item for %s" % name)        
    
    def __find_variable(self, name):
        return self.variables[name]

    def __find_singleton(self, name, params):
        if not name in self.singleton_instances:
            self.singleton_instances[name] = self.singletons[name](*params)

        return self.singleton_instances[name]
        
    def __find_factory(self, name, params):
        return self.factories[name](*params)
        