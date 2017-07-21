# generators = flexibity of functions, performance of iterators


def generate_even(count):
    a = 2
    while count > 0:
        yield a
        a += 2
        count -= 1

for num in generate_even(10):
    print num


def fibbonaci(count):
    a, b = -1, 1
    while count > 0:
        c = a + b
        yield c
        a, b = b, c
        count -= 1


print list(fibbonaci(10))  # list internally interates over a generator until it exhausts

# Just like list-comprehensions, generators can be created in a single line of code,
# use '()' instead of '[]' to create a generator
even_numbers = (i for i in range(100) if i % 2 == 0)
for num in even_numbers:
    print num

fib = fibbonaci(10)
print "Fib object: ", fib
for i in range(10):
    print next(fib)
