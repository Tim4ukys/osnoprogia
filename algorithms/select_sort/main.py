from sorts import insertion_sort
from random import randint

test = [3, 1, 4, 5, 2]
insertion_sort(test)
assert(test == [1, 2, 3, 4, 5])

test = [1]
insertion_sort(test)
assert(test == [1])

test = []
insertion_sort(test)
assert(test == [])


test = [3, 3, 3]
insertion_sort(test)
assert(test == [3, 3, 3])

test = [randint(0, 10**6) for i in range(10**3)]
test1 = test.copy()
test1.sort()
insertion_sort(test)
assert(test1 == test)

