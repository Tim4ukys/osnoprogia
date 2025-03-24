from rational import *
from random import randint

# create
assert create(0, 1) == [0, 0]
assert not create(1, 0)
assert create(6, -4) == [-3, 2]
assert create(32, -16) == [-2, 1]

# cmp
a, b, c = create(5, 9), create(4, 7), create(5, 3)
assert compare(a, b) == compare(b, c) == -1
assert compare(b, a) == compare(c, b) == 1

# add and sub
d = add(add(a, b), c)
assert d == [176, 63] and add(a, b) == [71, 63] and add(a, c) == [20, 9] and add(b, c) == [47, 21]
assert sub(create(-1, 2), create(1, 2)) == [0, 0]
assert sub(d, b) == add(a, c) and sub(d, a) == add(c, b)

# mul and div
assert mul(a, power(a, -1)) == [1, 1] == div(a, a)
assert mul(a, c) == [25, 27] and div(mul(a, c), a) == c

# power
assert power(create(1, 2), 0) == [1, 1]
assert power(create(228, 0), 0) == create(228, 0)

for _ in range(10):
    a, b, p = [randint(-100, 100) for _ in range(3)]
    r = create(a, b)
    assert power(r, p) == create(int(a**p), int(b**p))
    print(str(r))

