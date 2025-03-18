def quick_sort(arr, start, end):
    if end-start <= 1:
        return

    st = start
    en = end

    mid = arr[start]
    cp_arr = arr.copy()
    for i in range(1+start, end):
        if cp_arr[i] <= mid:
            arr[start] = cp_arr[i]
            start+=1
        else:
            end-=1
            arr[end] = cp_arr[i]

    arr[end-1] = mid
    quick_sort(arr, st, start)
    quick_sort(arr, end, en)

## check quick sort
from random import randint

tests=[
    [],
    [13],
    [4, 1],
    [54, 12, 24],
    [4, 4, 4],
    [1, 2, 2, 5],
    [4, 3, 1, 2, 6, 5, 9, 8, 7],
    [3, 2, 5, 1, 4]
]

for a in range(100):
    tests.append([randint(-1000, 1000) for _ in range(randint(100, 1000))])

for i in tests:
    cp = i.copy()
    cp.sort()
    quick_sort(i)
    assert(i == cp)