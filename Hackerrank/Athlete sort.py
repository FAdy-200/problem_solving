n = list(map(int, input().split()))
x = []
for i in range(n[0]):
    x.append(list(map(int, input().split())))
k = int(input())
g = {}

for i in x:
    if i[k] not in g:
        g[i[k]] = ' '.join(list(map(str, i)))
    else:
        g[i[k]] = g[i[k]] + '\n' + ' '.join(list(map(str, i)))

l = sorted(g.keys())
for i in l:
    print(g[i])
# https://www.hackerrank.com/challenges/python-sort-sort/problem
