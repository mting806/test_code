from schema import Schema
from schema import SchemaError

class DataValideErr(Exception):
    def __init__(self, message: str, name: str = None) -> None:
        self.name = name
        self.message = message
        super().__init__(message)

class data_validator_func(object):
    @staticmethod
    def not_none(func):
        def wrapper(self, *args, **kwargs):
            try:
                name = self.name
                return Schema(lambda x: x>0).validate(func(self, *args, **kwargs))
            except SchemaError as e:
                raise DataValideErr("not_none")
        return wrapper

    def unique(func):
        def wrapper(self, *args, **kwargs):
            return Schema(lambda x: x==0).validate(func(self, *args, **kwargs))
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
        self.name = "data_test"

    def __str__(self):
        return str(self.__class__)

    @data_validator_func.not_none
    @data_validator_func.unique
    def set_date(self, data):
        self.data = data
        return data

a = data_test(15)
a.set_date(20)
print(a.data)
