from schema import Schema

class data_validator_func(object):
    @staticmethod
    def validate(func):
        def wrapper(self, *args, **kwargs):
            return Schema(lambda x: x>5).validate(func(self, *args, **kwargs))
        return wrapper


class data_validator_class(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, *args, **kwargs):
        def wrapper(*args, **kwargs):
            return Schema(lambda x: x>5).validate(self.func(obj, *args, **kwargs))
        return wrapper


class data_test(object):
    def __init__(self, data):
        self.data = data

    @data_validator_class
    def set_date(self, data):
        self.data = data
        return data

a = data_test(15)
a.set_date(2)
print(a.data)