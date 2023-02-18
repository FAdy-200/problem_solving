x = []
n = int(input())
for _ in range(n):
    x.append(list(map(int, input().split())))
m = 0
o = 0
for i in range(n):
    m += x[i][i]
    o += x[n-i-1][i]
print(abs(o-m))
