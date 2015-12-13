# A set is a collection of objects which does not allow any duplicates, no order is maintained in an ordinary set.


def unique_letters(word):
    return set(word.lower())

print unique_letters("hello")

sample_set = {1, 2, 3}  # a set is a mutable collection in python, it can be updated
print 1 in sample_set
print 4 in sample_set
sample_set.add(4)  # adds a new element to a set
print sample_set
sample_set.update({6, 7})  # adds the contents of the argument set
print sample_set
sample_set.remove(6)  # remove an element from the set, throws a KeyError if element not found
sample_set.discard(7)
sample_set.discard(7)  # discard removes the element from the set, if found, else noop
sample_set.clear()  # empty the set

# basic set operations:

sample1 = {1, 2, 3, 4}
sample2 = {3, 4, 5}
print sample1 | sample2  # union of sets
print sample1.union(sample2)
print sample1 & sample2  # intersection of sets
print sample1.intersection(sample2)
print sample1 - sample2  # difference between 2 sets
print sample1.difference(sample2)
print sample1.symmetric_difference(sample2)  # XOR of two sets
print {1}.issubset(sample1)
print sample1.issuperset(sample_set)
print not sample1
print not (sample1 - sample1)
