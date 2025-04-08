import avl_tree as avl
from random import randint

my_tree = avl.create(lambda a, b: (a > b) - (a < b))
for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    avl.insert(my_tree, i)

avl.delete(my_tree, 1)
avl.delete(my_tree, 2)
avl.delete(my_tree, 6)

assert not avl.create(None)
tree = avl.create(lambda a, b: (a > b) - (a < b))
assert not avl.insert(tree, 1)
assert not avl.delete(tree, 3)
assert avl.delete(tree, 1) == 1

numbs = list(set([randint(-10**6, 10**6) for i in range(10**3)]))
sorted_numbs = numbs.copy()
sorted_numbs.sort()

for i in numbs:
    avl.insert(tree, i)

avl_sort = list()
def srt(d, arr : list):
    arr.append(d)
avl.foreach(tree, srt, avl_sort)

assert sorted_numbs == avl_sort
