def binary_searchr(a, x):
    l, r = 0, len(a)
    mid = ((r + l) // 2)
    mo = -1
    try:
        while x != a[mid]:
            mid = ((l + r) // 2)
            if x > a[mid]:
                l = mid
            elif x < a[mid]:
                r = mid
            if mo == mid:
                return -1
            mo = mid
    except:
        return -1
    if a[0] == x:
        return mid + binary_searchr(a[mid + 1:], x) + 1
    else:
        return mid


def binary_searchl(a, x):
    l, r = 0, len(a)
    mid = ((r + l) // 2)
    mo = -1
    try:
        while x != a[mid]:
            mid = ((l + r) // 2)
            if x > a[mid]:
                r = mid
            elif x < a[mid]:
                l = mid
            if mo == mid:
                return -1
            mo = mid
    except:
        return -1
    if a[0] == x:
        return mid + binary_searchl(a[mid + 1:], x) + 1
    else:
        return mid


def mine(a, left, right):
    ri = right - 1
    le = left
    m = (ri + le) // 2
    rh = a[m:]
    lh = a[:m + 1][::-1]
    mr = binary_searchr(rh, a[m])
    ml = binary_searchl(lh, a[m])
    if (mr + ml + 1) > right / 2:
        return 1
    else:
        return 0


def ma(A):
    d = {}
    for j in range(len(A)):
        if A[j] in d:
            d[A[j]] += 1
        else:
            d[A[j]] = 1
    if len(d) == len(A):
        return True, 0, 0
    m = max(d.values())
    for i, j in d.items():
        if j == m:
            return False, i, j


def co(e, f):
    n = 0
    for i in f:
        if i == e:
            n += 1
    return n


def lec_s(A):
    if len(A) <= 6:
        x = A[:len(A) // 2]
        y = A[len(A) // 2:]
        xc, xi, xn = ma(x)
        if xc:
            xc, xi, xn = ma(y)
            if xc:
                c = 0
                for i in y:
                    h = co(i, x)
                    if h >= c:
                        c = h + 1
                        xi = i
                if c > len(A) / 2:
                    return xi, c
                else:
                    return -1, -1
            gg = co(xi, x)
            xn += gg
            if xn > len(A) / 2:
                return xi, xn
            else:
                return -1, -1
        gg = co(xi, y)
        xn += gg
        if xn > len(A) / 2:
            return xi, xn
        else:
            return -1, -1
    else:
        f1 = A[:len(A) // 2]
        f2 = A[len(A) // 2:]
        z1 = (lec_s(f1))
        z2 = (lec_s(f2))
        if z1[0] >= 0:
            nz1 = z1[1] + co(z1[0], f2)
            if nz1 > len(A) / 2:
                return z1[0], nz1
        if z2[0] >= 0:
            nz2 = z2[1] + co(z2[0], f1)
            if nz2 > len(A) / 2:
                return z2[0], nz2
            else:
                return -1, -1
        else:
            return -1, -1


def lec(A):
    f1 = A[:len(A) // 2]
    f2 = A[len(A) // 2:]
    z1 = (lec_s(f1))
    z2 = (lec_s(f2))

    if z1[0] >= 0:
        nz1 = z1[1] + co(z1[0], f2)
        if nz1 > len(A) / 2:
            return 1
    if z2[0] >= 0:
        nz2 = z2[1] + co(z2[0], f1)
        if nz2 > len(A) / 2:
            return 1
        else:
            return 0
    else:
        return 0

def fast_me(A):
    d={}
    ma = 0
    for i in A:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        if d[i] > ma:
            ma = d[i]
    if ma > len(A)/2:
        return 1
    else:
        return 0













def naive(A):
    for j in range(len(A)):
        e = A[j]
        c = 0
        for k in range(j, len(A)):
            if A[k] == e:
                c += 1
        if c > len(A) / 2:
            return 1
    return 0


hjhj = int(input())
# hjhj = 1
if hjhj:
    # import numpy as np
    A = list(map(int, input().split()))
    # print(lec(A))
    # A = sorted(list(map(int, input().split())))
    # A = list(np.random.choice(1000000, 10000000))
    print(fast_me(A))
else:
    import numpy as np
    import pandas as pd

    z = []
    for i in range(100
            # int(input())
    ):
        h = []
        A = sorted(list(np.random.choice(100, np.random.randint(low=1, high=100), replace=True)))
        h.append(mine(A, 0, len(A)))
        try:
            h.append(fast_me(A))
        except:
            lec(A)
        # h.append(A)
        # z.append(h)
    # ss = pd.DataFrame(z, columns=["r", "m", "A"])
    # ss["c"] = ss["r"] == ss["m"]
    # ss = ss[["r", "m", 'c', 'A']]
    # ss = ss[ss["c"] == False]
    # print(ss)
