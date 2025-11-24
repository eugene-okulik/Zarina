def decorator_with_count(count):
    def repeat_me(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return repeat_me


@decorator_with_count(2)
def example(text):
    print(text)


example('print me')
