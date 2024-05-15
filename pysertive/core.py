from functools import wraps


def pre_condition(check, exception_type=AssertionError, message="Precondition failed"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not check(*args, **kwargs):
                raise exception_type(message)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def post_condition(
    check, exception_type=AssertionError, message="Postcondition failed"
):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not check(result):
                raise exception_type(message)
            return result

        return wrapper

    return decorator


def invariant(
    check, exclude=None, exception_type=AssertionError, message="Invariant failed"
):
    if exclude is None:
        exclude = []

    def method_decorator(method):
        @wraps(method)
        def wrapped_method(self, *args, **kwargs):
            if not check(self):
                raise exception_type(message)
            result = method(self, *args, **kwargs)
            if not check(self):
                raise exception_type(message)
            return result

        return wrapped_method

    def class_decorator(cls):
        original_init = cls.__init__

        @wraps(original_init)
        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)
            if not check(self):
                raise exception_type(message)

        cls.__init__ = new_init

        for name, method in cls.__dict__.items():
            if callable(method) and name not in exclude and name != "__init__":
                setattr(cls, name, method_decorator(method))

        return cls

    def decorator(item):
        if isinstance(item, type):
            return class_decorator(item)
        else:
            return method_decorator(item)

    return decorator
