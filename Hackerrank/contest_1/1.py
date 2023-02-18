n = int(input())
a = "abcdefghijklmnopqrstuvwxyz"
x = []
for i in range(n):
    x.append(a[i])
z = []
for i in range(1, n + 1):
    z.append(x[len(x) - i:])
    k = z[i - 1].copy()
    z[i - 1].reverse()
    z[i - 1] = z[i - 1] + k[1:]
l = (((n * 2 - 2) * 2 + 1) - 1) // 2
ans = []
for i in z:
    if len(i) == 1:
        ans.append('-' * l + i[0] + '-' * l)
    else:
        l -= 2
        g = []
        g.append('-' * l)
        for j in i:
            g.append(j)
            g.append('-')

        g.pop()
        g.append('-'*l)
        ans.append("".join(g))
m = ans[:-1].copy()
m.reverse()
ans = ans + m
for i in ans:
    print(i)