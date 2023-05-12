n = int(input())
d = {}
g = {}
for i in range(n):
    x = input()
    if x not in d:
        d[x] = [i, 1]
    else:
        d[x][1] += 1
for (i, j) in d.items():
    g[j[0]] = j[1]
gs = sorted(g.keys())
print(len(d.keys()))
for i in gs:
    print(g[i], end=" ")

# https://www.hackerrank.com/challenges/word-order/problem