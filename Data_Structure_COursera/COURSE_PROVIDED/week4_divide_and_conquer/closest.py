# Uses python3

def srtx(x, y):
    a = x[0]
    b = y[0]
    z = x[1]
    w = y[1]
    m = len(a)
    n = 0
    f = True
    for i in range(len(b)):
        while n < len(a):
            if b[i] <= a[n]:
                a.insert(n, b[i])
                z.insert(n, w[i])
                f = False
                n += 1
                d = i
                break
            n += 1
        if n == len(a) and f:
            a = a + b
            z = z + w
            d = -1
            break
    if len(a) != m + len(b):
        a = a + (b[d + 1:])
        z = z + (w[d + 1:])
    return a, z


def srty(x, y):
    a = x[0]
    b = y[0]
    z = x[2]
    w = y[2]
    m = len(a)
    n = 0
    f = True
    for i in range(len(b)):
        while n < len(a):
            if b[i] <= a[n]:
                a.insert(n, b[i])
                z.insert(n, w[i])
                f = False
                n += 1
                d = i
                break
            n += 1
        if n == len(a) and f:
            a = a + b
            z = z + w
            d = -1
            break
    if len(a) != m + len(b):
        a = a + (b[d + 1:])
        z = z + (w[d + 1:])
    return a, x[1] + y[1], z


def quick_sortx(a, b):
    if len(a) == 1:
        return a, b
    return srtx(quick_sortx(a[len(a) // 2:], b[len(b) // 2:]), quick_sortx(a[:len(a) // 2], b[:len(b) // 2]))


def quick_sorty(a, b, index):
    if len(a) == 1:
        return a, b, index
    return srty(quick_sorty(a[len(a) // 2:], b[len(b) // 2:], index[len(a) // 2:]),
                quick_sorty(a[:len(a) // 2], b[:len(b) // 2], index[:len(a) // 2]))


def minimum_distance(x, y, k, d=False):
    if len(x) == 1:
        return x, y, k, True
    else:
        h1 = ([x[i] for i in range(len(x)) if x[i] >= k[0]], [y[i] for i in range(len(x)) if x[i] >= k[0]])
        h2 = ([x[i] for i in range(len(x)) if x[i] < k[0]], [y[i] for i in range(len(x)) if x[i] < k[0]])
        q1 = ([h1[0][i] for i in range(len(h1[1])) if h1[1][i]>=k[1]], [h1[1][i] for i in range(len(h1[1])) if h1[1][i]>=k[1]])
        q2 = ([h1[0][i] for i in range(len(h1[1])) if h1[1][i]<k[1]], [h1[1][i] for i in range(len(h1[1])) if h1[1][i]<k[1]])
        q3 = ([h2[0][i] for i in range(len(h2[1])) if h2[1][i]>=k[1]], [h2[1][i] for i in range(len(h2[1])) if h2[1][i]>=k[1]])
        q4 = ([h2[0][i] for i in range(len(h2[1])) if h2[1][i]<k[1]], [h2[1][i] for i in range(len(h2[1])) if h2[1][i]<k[1]])
        import matplotlib.pyplot as plt
        plt.figure()
        plt.scatter(q1[0], q1[1])
        plt.scatter(q2[0], q2[1])
        plt.scatter(q3[0], q3[1])
        plt.scatter(q4[0], q4[1])
        plt.legend(['q1','q2','q3','q4'])
        plt.show()
        m1 = minimum_distance(q1[0],q1[1])
        m2 =



x = []
y = []
n = int(input())
for i in range(n):
    data = list(map(int, input().split()))
    x.append(data[0])
    y.append(data[1])
k = [0,0]
# print("{0:.9f}".format(minimum_distance(x, y)))
bm = (minimum_distance(x, y, k))
print(bm)
s = 2828427125
for i in bm:
    if i[3] < s:
        s = i[3]
print(s)
