import numpy as np


def naive(a, b):
    d = [0] * (len(b) * 2 - 1)
    for i in range(len(b)):
        for j in range(len(a)):
            d[i + j] += (b[i] * a[j])
    return d


def mult(a, b, n, an, bn):
    r = [0] * ((2 * n) - 1)
    if n == 1:
        r[0] = a[an] * b[bn]
        return r
    r[:n - 1] = mult(a, b, (n // 2), an, bn)
    r[n:((2 * n) - 1)] = mult(a, b, n // 2, an + n // 2, bn + n // 2)
    d0 = mult(a, b, n // 2, an, bn + n // 2)
    d1 = mult(a, b, n // 2, an + n // 2, bn)
    try:

        r[n // 2:(n + (n // 2) - 1)] = [d0[i] + d1[i] + r[n // 2:(n + (n // 2) - 1)][i] for i in
                                        range(len(r[n // 2:(n + (n // 2) - 1)]))]
    except:
        g = r[n // 2:(n + (n // 2) - 1)]
        for i in range(len(g)):
            g[i] += d0[i] + d1[i]

    return r
def fg(a,b, n, an,bn):
    r = [0] * ((2 * n) - 1)
    for i in range(len(r)):
        r[i] = a[an+i] + a[an+1+i]
    return r

def mult1(a, b, n, an, bn):
    r = [0] * ((2 * n) - 1)
    if n == 1:
        r[0] = a[an] * b[bn]
        return r
    r[:n - 1] = mult1(a, b, (n // 2), an, bn)
    r[n:((2 * n) - 1)] = mult1(a, b, n // 2, an + n // 2, bn + n // 2)
    d0 = fg(a, b, n // 2, an, bn+n//2)
    d1 = fg(b, a, n // 2, bn, an+n//2)
    try:

        g = r[n // 2:(n + (n // 2) - 1)]
        for i in range(len(r[n // 2:(n + (n // 2) - 1)])):
            k = r[:n - 1][i]
            m = r[n:((2 * n) - 1)][i]
            g[i] = d0[i]*d1[i] - k - m
        r[n // 2:(n + (n // 2) - 1)] = g
    except:
        g = r[n // 2:(n + (n // 2) - 1)]
        for i in range(len(g)):
            g[i] += d0[i] * d1[i] - r[:n - 1][i] -r[n:((2 * n) - 1)][i]
        r[n // 2:(n + (n // 2) - 1)] = g
    return r


# a = np.random.randint(0, 200, 300)
# b = np.random.randint(0, 200, 300)
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = mult(a, b, len(b), 0, 0)
c1 = mult1(a, b, len(b), 0, 0)
print(c)
print(c1)



