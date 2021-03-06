def suppress_errors(func):
    """a basic decorator to suppress any exceptions
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            pass
    return wrapper


@suppress_errors
def divide(a, b):
    return a / b


print divide(20, 2)
print divide(2, 0)


def memoize(func):
    """A decorator which caches the results of a function, and uses when necessary.
    """
    cache = {}
    def wrapper(*args):
        if args in cache:
            print "Cache hit!"
            return cache[args]
        print "Value not in cache, computing..."
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@memoize
def multiply(a, b):
    return a * b


print multiply(3, 4)
print multiply(5, 4)
print multiply(3, 4)
print multiply(5, 4)


# passing arguments to a decorator
def suppress_errors(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger(e)
        return wrapper
    return decorator


def print_logger(s):
    print "Logging: %s" % s


@suppress_errors(print_logger)
def divide(a, b):
    return a / b

print divide(20, 2)
print divide(2, 0)


# Understanding the order in which decorators are applied
def deco1(func):
    def wrapper():
        print "Deco 1 starts!"
        func()
        print "Deco 1 done!"
    return wrapper


def deco2(func):
    def wrapper():
        print "Deco 2 starts!"
        func()
        print "Deco 2 done!"
    return wrapper


@deco2
@deco1
def sample():
    print "In sample."

sample()
