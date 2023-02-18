def min_s(v, w):
    v = v.copy()
    w = w.copy()
    h = True
    nu = 0
    s = []
    while h:
        mn = min(v)
        ma = list(map(lambda x: x - mn, w))
        ind = ma.index(min(ma))
        mx = w[ind]
        s.append(str(mx))
        v.pop(ind)
        w.pop(ind)
        nu += 1
        j = 0
        while j < len(v):
            if mx in range(v[j], w[j] + 1):
                v.pop(j)
                w.pop(j)
            else:
                j += 1
        if len(v) == 0:
            return nu, s




# n = int(input())
# v = []
# w = []
# for i in range(n):
#     x, y = map(int, input().split())
#     v.append(x)
#     w.append(y)
n = 3
x = [1,2,3]
y = [3,5,6]
for i in range(1000):
    jk = (min_s(x, y))
# print(jk[0])
# print(" ".join(jk[1]))


