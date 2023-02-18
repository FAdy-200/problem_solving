# python3


def car_refueling_MINE(d, t, y):
    s = y
    s.append(d)
    s.insert(0, 0)
    if t >= d:
        return 0
    co = 0
    x = 0
    i = 0
    while i < len(s):
        if (s[i] - s[x]) > t:
            x = i - 1
            co += 1
        c1 = (s[i] // t - s[x] // t) >= 2
        c2 = ((s[i] // t - s[x] // t) == 1)
        c3 = s[i] - s[x] > t
        if c1 or (c2 and c3):
            return -1
        i += 1
    return co


def car_refueling(d, t, y):
    s = y
    s.append(d)
    s.insert(0, 0)
    i = 1
    st = 0
    if t >= d:
        return 0
    while i < len(s):
        if s[i] > t:
            if t < (s[i]-s[i-1]):
                return -1
            s = list(map(lambda x: x - s[i - 1], s[i - 1:]))
            i = 1
            st += 1
            continue
        i += 1
    if len(s) > 2 and t < (s[-1] - s[0]):
        return -1
    return st

def car_refuel_lec(d,r,y):
    y.insert(0, 0)
    y.append(d)
    nr = 0
    cp = 0
    n = len(y)-2
    while cp <= n:
        lp = cp
        while cp <= n and y[cp+1]-y[lp] <= r:
            cp += 1
        if cp == lp:
            return -1
        else:
            nr += 1
    return nr














import numpy as np
# import pandas as pd
# v =[]
# n = int(input())
n = 10000
for i in range(n):
#     h = []
    du = np.random.randint(low=1, high=1e5)
    tu = np.random.randint(low=1, high=400)
    su = sorted(list(np.random.randint(low=0, high=du, size=np.random.randint(low=1, high=300))))
    # car_refueling(du,tu,su)
    car_refueling_MINE(du,tu,su)
    car_refuel_lec(du,tu,su)
#     h.append(car_refueling_MINE(du, tu, su))
#     h.append(car_refueling(du, tu, su))
#     h.append(du)
#     h.append(tu)
#     h.append(su)
#     v.append(h)
# ss = pd.DataFrame(v, columns=["True", "Expr", "d", "t", "s1"])
# ss["check"] = (ss["True"] == ss["Expr"])
# ss = ss[["True", "Expr", "check", "d", "t", "s1"]]
# ss = ss[ss["check"] == False]
# # ss = ss[ss["True"] != -1]
# print(ss)
# d = int(input())
# t = int(input())
# input()
# s1 = list(map(int, input().split()))
# print(car_refueling_MINE(d, t, s1))
# print(car_refueling(d, t, s1))
# print(car_refuel_lec(d, t, s1))



