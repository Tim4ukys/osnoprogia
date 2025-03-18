from sort import quick_sort
from sys import exit

arr = [float(i) for i in input("числа: ").split()]
if len(arr) == 0:
    print("Нужно ввести числа")
    exit(-1)
if len(arr) == 1:
    print(f"min: {arr[0]}\nmax: {arr[0]}\nср. арифм. число: {arr[0]}")
    print(f"медиана: {arr[0]}")
    print(f"СКВО: 0.0\nМакс. число идущих подряд чисел: 1")
    print(f"Максимальная длина монотонного участка: 1")
    exit(0)

mn = mx = mean = arr[0]

twins = 0
twins_mx = 0
stonks = None
mono = 0
mono_mx = 0

for i in range(1, len(arr)):
    n = arr[i]
    
    if stonks == None:
        if arr[i-1] != n:
            stonks = arr[i-1] < n
        mono += 1
    elif n == arr[i-1] or stonks == (n > arr[i-1]):
        mono += 1
    else:
        stonks = not stonks
        if mono > mono_mx:
            mono_mx = mono
        mono = twins + 1

    if n == arr[i-1]: twins += 1
    else:
        if twins>twins_mx:
            twins_mx = twins 
        twins = 0

    if n < mn: mn = n
    elif n > mx: mx = n

    mean += n

mean /= len(arr)
meansq = 0
for i in arr:
    meansq += (i - mean) ** 2
meansq = (meansq/(len(arr)-1))**0.5

quick_sort(arr, 0, len(arr))
print(f"min: {mn}\nmax: {mx}\nср. арифм. число: {mean}")
print(f"медиана: {(arr[len(arr)//2] + arr[len(arr)//2+1]) / 2 if len(arr)&1==1 else arr[len(arr)//2]}")
print(f"СКВО: {meansq}\nМакс. число идущих подряд чисел: {twins_mx + 1 if twins_mx > twins else twins + 1}")
print(f"Максимальная длина монотонного участка: {(mono_mx if mono_mx > mono else mono) + 1}")