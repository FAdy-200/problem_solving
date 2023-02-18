#  https://www.hackerrank.com/challenges/3d-surface-area/problem


h, w = map(int, input().split())

x = [[0] * (w + 2)]

for i in range(h):
    z = [0]
    z += list(map(int, input().split()))
    z.append(0)
    x.append(z)
x.append([0] * (w + 2))
# print(x)
ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        imp = x[i][j]
        a = (imp - x[i][j - 1])
        b = (imp - x[i - 1][j])
        c = (imp - x[i][j + 1])
        d = (imp - x[i + 1][j])
        nz = [a, b, c, d]
        ans += 2
        for idk in nz:
            if idk > 0:
                ans += idk
print(ans)
