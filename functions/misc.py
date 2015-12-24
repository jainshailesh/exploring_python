# inline methods in python
# syntax 'lambda arg1, arg2: single_expression_which_will_be_the_return_value

add = lambda a, b: a + b

print add
print add(1, 2)


# to identify an object type, use isinstance
if isinstance(1, int):
    print "integer!"

# various attributes for introspection
from generators import fibbonaci
print fibbonaci.__module__
print fibbonaci.__name__

from decorators import memoize
print memoize.__doc__
print add.__module__
