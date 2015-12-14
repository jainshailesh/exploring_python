def sample_function():
    pass


# there are 4 types of arguments a function supports
# required positional arguments
def add(x, y):
    return x + y
add(2, 3)


# optional arguments, with default set
def add_prefix(x, prefix='pro_'):
    return prefix + x
add_prefix('python')


# variable position arguments, all the additional arguments after list are clubbed into a tuple named items
def add_to_list(a_list, *items):
    return a_list.extend(items)
add_to_list([1], 2, 3, 4)


# variable keyword arguments, all the additional keywords are clubbed into a dictionary named record
def display_employee(**record):
    print record
display_employee(name='Sam', age='23')


# the most widely used sequence while having different types of arguments is:
# def func(required, optional='', *variable_positional, **variable_keyword)
