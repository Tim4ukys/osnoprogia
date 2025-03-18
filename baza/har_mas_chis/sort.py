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
test_arr = [3, 2, 5, 1, 4]
quick_sort(test_arr, 0, len(test_arr))
assert(test_arr == [1, 2, 3, 4, 5] and "quick sort don't work")
