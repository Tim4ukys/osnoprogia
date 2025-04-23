import hashtable as h
from random import randint


COUNT_USERS = int(1e4)
users = dict(zip(
    [f"{i}" for i in range(1, COUNT_USERS+1)],
    ["{0:02d}-{0:02d}-{0:02d}".format(*[randint(1,99) for _ in range(3)]) for _ in range(COUNT_USERS)]
))

def _list_get_sz(l : h._List):
    ls = l
    sz = 0
    while ls:
        sz += 1
        ls = ls.next
    return sz

def ht_get_size_info(ht : h.HashTable):
    r = []
    for tb in ht.tabs:
        r.append([_list_get_sz(l) for l in tb.table])
    return r

hs = h.ht_init(1000)
for a, b in users.items():
    assert h.ht_set(hs, a, b) is None
    assert h.ht_has(hs, a) == True

assert sum(ht_get_size_info(hs)[0]) == len(users)

h.ht_resize(hs, 3333)
for i, dt in enumerate(users.items(), 1):
    a, b = dt
    assert h.ht_get(hs, a) == b
    sz = ht_get_size_info(hs)
    if i != len(users):
        assert sum(sz[0])+i == len(users) and sum(sz[1]) == i
    else:
        assert sum(sz[0]) == len(users)

h.ht_destroy(hs)
text = []
hs = h.ht_init(15, hash, lambda x: text.append(x))
for a, b in enumerate(['a', 'b', 'c'], 1):
    assert h.ht_set(hs, f"{a}", b) is None
    assert h.ht_set(hs, f"{a}", b) == b
assert len(set(text)) == 3
text.clear()
for i in range(1, 4):
    assert h.ht_delete(hs, f"{i}") in text
    assert h.ht_delete(hs, f"{i}") not in text
assert len(set(text)) == 3
h.ht_destroy(hs)



