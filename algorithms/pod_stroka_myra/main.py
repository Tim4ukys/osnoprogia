from utils import my_strstr

tests = {
    "abcbecbabcbc": [ 'cbc', 'abcbc', 'e', 'bab', 'cbe', 'abcbecbabcbc', 'abcbecbabcbcdgdfhdgf', 'test' ],
    "aboba": [ 'ba', 'bob', 'oba', 'o', 'a', 'test' ]
}

for i in tests:
    for k in tests[i]:
        assert(my_strstr(i, k) == i.find(k))
