import itertools as itr
n = list(map(int, input().split()))
x = []
for i in range(n[0]):
    k = list(map(int, input().split()))
    k.pop(0)
    x.append(k)
gg = list(itr.product(*x))
res = 0
for i in gg:
    s = 0
    for k in i:
        s += (k**2)
    s%=n[1]
    if s > res:
        res = s
print(res)

# https://www.hackerrank.com/challenges/maximize-it/problem