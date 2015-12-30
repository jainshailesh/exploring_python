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
