def _heapify(arr, i, sz):
    while True:
        max = i
        p = i * 2 + 1
        if p < sz and arr[p] > arr[max]:
            max = p
        if p+1 < sz and arr[p+1] > arr[max]:
            max = p+1
        if max == i:
            break
        arr[max], arr[i] = arr[i], arr[max]
        i = max


def heap_sort(arr):
    N = len(arr)
    if N <= 1: return

    for i in range((N-1)//2, -1, -1):
        _heapify(arr, i, N)

    for i in range(N-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, 0, i)