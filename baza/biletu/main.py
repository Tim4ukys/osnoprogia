import itertools

a = [0 for i in range(9*8+1)]
for t in itertools.product([i for i in range(10)], repeat=8):
    s = sum(t)
    a[s] += 1

ans = 0
for i in a:
    ans += i**2
    
print(f"Процент счастливых билетов: {(ans*100)/10**16:.4}% | Общее кол-во сч. билетов: {ans}")
