from random import randint

def _hash(str, sz, q):
    r = 0
    for i in range(sz):
        r += (2**(sz-1-i))*ord(str[i])
    return r%q

def my_strstr(str, pattern):
    sz = len(pattern)
    if len(str) < sz:
        return -1

    q = randint(2, int(len(str)**3))
    hash_pattern = _hash(pattern, sz, q)
    hash_str = _hash(str, sz, q)
    i = 0
    while True:
        if hash_str == hash_pattern and str[i:sz+i] == pattern:
            return i
        elif i > len(str) - sz - 1:
            return -1

        r0 = ord(str[i]) * (2**(sz-1))
        i += 1
        hash_str = ((hash_str - r0)*2 + ord(str[sz+i-1]))%q


