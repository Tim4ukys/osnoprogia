import SList
from random import randint


def initList(arr):
    r = None
    for i in arr:
        r = SList.append(r, i)
    return r


# Проверка работы массива
numbs = [randint(-50, 50) for _ in range(50)]

# prepend(none) and append(none)
l = None
l_two = None
for i in numbs:
    l = SList.prepend(l, i)
    l_two = SList.append(l_two, i)

# get and height
assert (SList.length(None) == 0)
assert (SList.get(None, 1) is None)

assert (len(numbs) == SList.length(l))
assert ([SList.get(l, i) for i in range(len(numbs))] == numbs[::-1] and
        [SList.get(l_two, i) for i in range(len(numbs))] == numbs)

# remove
assert (SList.remove(None, 2) == (None, None) and SList.remove(None, 0) == (None, None))

l = initList([i for i in range(1, 6)])
v, l = SList.remove(l, 0)
assert (v == 1 and SList.get(l, 2) == 4)

# get_last
assert (SList.get_last(l) == 5)
assert (SList.get_last(None) is None)

# find (неявно find_custom)
assert (SList.find(l, v) == -1 and SList.find(l, SList.get_last(l)) == SList.length(l) - 1)
assert (SList.find(None, 1) == -1)

# find_custom
assert (SList.find_custom(None, None) ==  (None, -1))

l = initList([i for i in range(3, 16)])
predicate = lambda x: x % 3 == 0
_, vi = SList.find_custom(l, predicate)
_, l = SList.remove(l, vi)

assert (vi == 0 and SList.find_custom(l, predicate)[1] == 2)

# remove_first
assert (SList.remove_first(None, 1) is None)

l = initList([2, 4, 2, 3, 5, 2, 6, 2, 7])
l = SList.remove_first(l, 2)
l = SList.remove_first(l, 7)
assert (SList.find(l, 2) == 1 and SList.find(l, 7) == -1 and SList.length(l) == 7)

# remove_all
assert (SList.remove_all(None, 2) is None)

l = SList.append(SList.prepend(l, 2), 2)
l = SList.remove_all(l, 2)
assert (SList.find(l, 2) == -1 and SList.length(l) == 4)


# foreach
def raise_(_):
    raise IOError("Error")


assert (SList.foreach(None, raise_) is None)

l = initList([i for i in range(1, 26)])
sm = 0


def sum_arr(x):
    global sm
    sm += x


SList.foreach(l, sum_arr)
assert (sm == sum([i for i in range(1, 26)]))

# copy
assert (SList.copy(None) is None)

l_two = SList.copy(l)
assert (all([SList.get(l_two, i) == SList.get(l, i) for i in range(26 - 1)]) and
        SList.length(l) == SList.length(l_two))

# concat
assert (SList.concat(None, l) == SList.concat(l, None) == l and
        SList.length(l) == SList.length(SList.concat(l, None)) and
        SList.concat(None, None) is None)

l = initList([1, 2, 3, 4])
l_two = initList([5, 6, 7, 8])
l = SList.concat(l, l_two)
assert ([SList.get(l, i) for i in range(SList.length(l))] == [i for i in range(1, 9)])
