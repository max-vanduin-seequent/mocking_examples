from ProductionClass import ProductionClass


class ImportingClass:

    def __init__(self, complex_object, second_complex_object, production_class=ProductionClass()):
        self.complex_object = complex_object
        self.second_complex_object = second_complex_object
        self.production_class = production_class

    def local_method(self, arg):
        return "Local method called"

    def method_using_imports(self, arg):
        if arg:
            return self.production_class.method_that_will_fail(arg)
        else:
            return self.local_method(arg)
