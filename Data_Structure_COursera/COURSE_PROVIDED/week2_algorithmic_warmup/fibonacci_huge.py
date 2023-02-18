# Uses python3
def pat(x):
    p = [x[0]]
    h = True
    i = 1
    while h:
        c = i
        ff = x[c:c + c]
        if len(ff) < c:
            h = False
            p += ff
        if ff == p:
            h = False
        else:
            p.append(x[c])
            i += 1
    return p, i


def calc_fib(n):
    if n == 0:
        return 0
    p = 0
    c = 1
    for i in range(1, n):
        p, c = c, c + p
    return c


def calc_fib1(n, m):
    # t1 = time.time()
    kok = [calc_fib(j) % m for j in range(4000)]
    # t2 = (time.time()-t1)
    # print(t2)
    p = pat(kok)
    return p[0][n % p[1]]


n, m = map(int, input().split())
# import time
# t = time.time()
print(calc_fib1(n, m))
# print(time.time()-t)
# import pandas as pd
# v = []
# fn = calc_fib(n)
# for i in range(1,m+1):
#     d = []
#     d.append(fn % i)
#     gg = calc_fib1(n, i)
#     d.append(n % len(gg))
#     d.append(gg[(n % len(gg))])
#     d.append(gg)
#     v.append(d)
#
# s1 = pd.DataFrame(v, columns=["real","n%m", 'mine',
#                              "all"
#                              ])
#
# s1["check"] = s1['real'] == s1["mine"]
# s1 = s1[["n%m","real","mine",'check',
#        "all"
#        ]]
# print(s1[s1['check'] == False])


