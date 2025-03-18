
def my_strstr(str, pattern):
    if len(str) < len(pattern):
         return -1
    d = dict()
    for i in range(len(pattern) - 2, -1, -1):
        if pattern[i] not in d:
            d[pattern[i]] = len(pattern) - 1 - i

    i = len(pattern)-1
    while i < len(str):
        for k in range(len(pattern)-1, -1, -1):
            if str[i - (len(pattern)-1-k)] != pattern[k]:
                i += d[str[i]] if str[i] in d else len(pattern)
                break
            if k == 0:
                return i - len(pattern) + 1
    return -1

