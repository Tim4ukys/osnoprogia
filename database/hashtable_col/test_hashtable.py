import hashtable as h
from random import randint

users = dict(zip(
    [f"{i}" for i in range(1, 101)],
    ["{0:02d}-{0:02d}-{0:02d}".format(*[randint(1,99) for _ in range(3)]) for _ in range(100)]
))

hs = h.ht_init(10)
for a, b in users.items():
    assert h.ht_set(hs, a, b) is None
    assert h.ht_hash(hs, a) == True

assert sum(h.ht_get_size_info(hs)[0]) == len(users)

h.ht_resize(hs, 15)
for i, dt in enumerate(users.items(), 1):
    a, b = dt
    assert h.ht_get(hs, a) == b
    sz = h.ht_get_size_info(hs)
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



