n = int(input())

d = {}
for i in range(n):
    k = input()
    d[k] = float(input())
m1 = min(d.values())
m2 = max(d.values())
for i in d.values():
    if m1 < i <= m2:
        m2 = i
x=[]
for (i,j) in d.items():
    if j == m2:
        x.append(i)
x.sort()
for i in x:
    print(i)

# https://www.hackerrank.com/challenges/nested-list/problem