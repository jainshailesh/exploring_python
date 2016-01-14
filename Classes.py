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


# Attributes in python - getattr and setattr are inbuilt methods which work with all/any attribute

e = Example()
print e.a
print getattr(e, 'a')
setattr(e, 'a', 4)
print getattr(e, 'a')


# Properties in a python class
# use the built-in decorator @property to make sure that this method is called whenever the function's name is used as
# an attribute

class Student(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return '%s, %s' % (self.first_name, self.last_name)

    @name.setter
    def name(self, name):  # Note: setter takes only one argument, use a tuple when dealing with multiple arguments
        self.first_name, self.last_name = name
        return

s = Student('Tim', 'Peters')
print s.name
s.name = 'Shailesh', 'Jain'
print s.name
