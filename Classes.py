# All classes in python are created/instantiated at runtime. Essentially, we can have anything inside a class code
# block, and it will be executed.

# All classes in python inherit from the base class type()
# only three things are required to create a class in python, 1. Name, 2. Base Classes, 3. Namespaces dictionary


class Example(object):
    if True:
        print "This is like a normal code block!"
    a = 1

print Example

Example2 = type('Example2', (Example,), {'b': 2})

print Example2
print Example2.a
print Example2.b
