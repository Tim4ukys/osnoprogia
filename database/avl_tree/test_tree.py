import avl_tree as avl
from random import randint

assert not avl.create(None)
tree = avl.create(lambda a, b: (a > b) - (a < b))
assert not avl.insert(tree, 1)
assert not avl.delete(tree, 3)
assert avl.delete(tree, 1) == 1
assert avl.size(tree) == 0

numbs = list(set([randint(-10**7, 10**7) for i in range(10**4)]))
sorted_numbs = numbs.copy()
sorted_numbs.sort()

for i in numbs:
    avl.insert(tree, i)
assert avl.size(tree) == len(numbs)

avl_sort = list()
def srt(d, arr : list):
    arr.append(d)
avl.foreach(tree, srt, avl_sort)

assert sorted_numbs == avl_sort

while numbs:
    vl = numbs[randint(0, len(numbs)-1)]
    numbs.remove(vl)
    r = avl.delete(tree, vl)
    l = avl.size(tree)
    assert len(numbs) == l
    assert r == vl

assert not avl.delete(None, None)
assert not avl.insert(None, 2)
assert not avl.foreach(None, None, None)
assert not avl.size(None) == 0
avl.clear(None)
