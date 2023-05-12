n, m = map(int, input().split())
x = list(map(int, input().split()))
s = 0
for i in range(n):
    ins = x[i]
    g = 0
    for j in x[i+1:i + 2 * m + 1]:
        if abs(ins - j) == m:
            if g == 1:
                s += 1
                break
            g = 1
            ins = j
print(s)



