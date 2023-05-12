n, m = int(input()), []
for i in range(n):
    m.append(list(map(int, input().split())))
d1, d2 = 0, 0
for i in range(1, n+1):
    d2 += m[-i][i-1]
    d1 += m[i-1][i-1]
print(abs(d1-d2))







