# Python supports both multi-level and multiple inheritance
# Usually, we want only some support functionality which a number of classes want to inherit,
# so we write support classes, called mixins which supply some small add-on features.


class SuppressNoAttributes:
    """This overrides the __getattr__ method. Suppresses the AttributeError exception.
    """
    def __getattr__(self, name):
        print self.__class__, 'does not have any attribute named: ', name
        return None


class Example(SuppressNoAttributes):
    pass


e = Example()
print e.sample
print type(e.sample)


# Using Super() to call methods of the base class
# Note: in python 3 onwards, all the classes are new-style classes, i.e. their type is the Class type, in 2.X versions,
# this is done by explicitly inheriting from Object class.

class A(object):
    def test(self):
        print 'A'


class B(A):
    def test(self):
        print 'B'
        super(B, self).test()  # super() takes 2 arguments, a type and an instance object


b = B()
print b.test()
