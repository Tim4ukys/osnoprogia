

def bin_search(arr, key):
    a, b = 0, len(arr)-1
    while a<=b:
        mid = (a+b)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            b = mid - 1
        else:
            a = mid + 1
    return -1

tmp = []
assert(bin_search(tmp, 1) == -1)

tmp = [1]
assert(bin_search(tmp, 1) == 0)
assert(bin_search(tmp, 2) == -1)

tmp = [1, 3, 5, 8, 10]
for i in range(len(tmp)):
    assert(bin_search(tmp, tmp[i]) == i)
for i in [0, 2, 4, 6, 7, 9, 11]:
    assert(bin_search(tmp, i) == -1)

tmp.append(12)
for i in range(len(tmp)):
    assert(bin_search(tmp, tmp[i]) == i)
for i in [0, 2, 4, 6, 7, 9, 11, 13]:
   assert(bin_search(tmp, i) == -1)
tmp.append(12)