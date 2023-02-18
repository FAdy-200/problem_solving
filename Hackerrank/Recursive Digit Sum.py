n, m = map(int, input().split())
k = 0
for j in str(n):
    k += m * int(j)
n = list(map(int, list(str(k))))
while len(n) != 1:
    n = list(map(int, list(str(sum(n)))))
print(n[0])
