
def insertion_sort(arr):
    if len(arr) <= 1:
        return

    for i in range(1, len(arr)):
        for a in range(i):
            if arr[i] < arr[a]:
                arr[i], arr[a] = arr[a], arr[i]

