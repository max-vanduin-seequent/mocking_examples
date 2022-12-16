from ProductionClass import ProductionClass


class ImportingClass:

    def __init__(self, complex_object, second_complex_object):
        self.complex_object = complex_object
        self.second_complex_object = second_complex_object

    def local_method(self, arg):
        return "Local method called"

    def method_using_imports(self, arg):
        if arg:
            return ProductionClass.method_that_will_fail(arg)
        else:
            return self.local_method(arg)
