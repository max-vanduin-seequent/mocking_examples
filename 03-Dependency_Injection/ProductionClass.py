
class ProductionClass:
    def sub_method(self, arg):
        return 'do something complex'

    def sub_method_2(self, arg2, arg3):
        return 'do a different complex thing'

    def method(self, arg1, arg2, arg3):
        if arg1:
            return self.sub_method(arg1)
        else:
            return self.sub_method_2(arg2, arg3)

    def complex_sub_method(self, arg4, arg5):
        return arg4 + arg5

    def complex_method(self, arg1, arg2, arg3):
        arg4 = self.sub_method(arg1)

        arg5 = self.sub_method_2(arg2, arg3)

        result = self.complex_sub_method(arg4, arg5)

        return 'hello ' + result

    def method_that_will_fail(self, arg):
        raise KeyError("This always fails")
