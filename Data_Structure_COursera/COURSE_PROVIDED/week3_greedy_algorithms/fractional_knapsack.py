# Uses python3

def get_optimal_value(c, w, v, z):
    value = 0.
    ci = 0
    ma = max(z)
    while ci != c and ma > 0:
        ind = z.index(ma)
        co = c - ci
        if v[ind] <= co:
            value += w[ind]
            ci += v[ind]
        else:
            value += (ma * co)
            ci += co
        z[ind] = -1
        ma = max(z)
    return value



n, c = map(int, input().split())
w = []
v = []
z = []
for i in range(n):
    x, y = map(int, input().split())
    w.append(x)
    v.append(y)
    z.append(x / y)

opt = get_optimal_value(c, w, v, z)
print("{:.4f}".format(opt))
