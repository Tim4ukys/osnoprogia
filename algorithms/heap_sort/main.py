from heap_sort import heap_sort
from random import randint

tests=[
    [],
    [13],
    [4, 1],
    [54, 12, 24],
    [4, 4, 4],
    [1, 2, 2, 5],
    [4, 3, 1, 2, 6, 5, 9, 8, 7]
]

for a in range(100):
    tests.append([randint(-1000, 1000) for _ in range(randint(100, 1000))])

for i in tests:
    cp = i.copy()
    cp.sort()
    heap_sort(i)
    assert(i == cp)