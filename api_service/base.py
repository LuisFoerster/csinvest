import inspect
from functools import wraps


class APIMeta(type):
    def __new__(mcs, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                attrs[attr_name] = mcs.request(attr_value)
        return super().__new__(mcs, name, bases, attrs)

    @staticmethod
    def request(method):
        @staticmethod
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            print(f'Common behavior injected in {self.__class__.__name__}')
            print(f'Domain: {self.Config.domain}')
            print(f'Cookie: {self.Config.cookie}')
            print(f'Method: {self.Config.method}')
            print(f'Method: {self.Config.domain}')
            bound_arguments = inspect.signature(method).bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            args_dict = dict(bound_arguments.arguments)
            print(args_dict.get("steamid"))
            result = method(self, *args, **kwargs)
            return result

        return wrapper


class APIBase(metaclass=APIMeta):
    pass


class HTTPMethods:
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
