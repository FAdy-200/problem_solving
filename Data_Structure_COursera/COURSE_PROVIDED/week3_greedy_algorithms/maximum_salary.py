# Uses python3
# TODO UNDERSTAND THIS MORE
def gr(x, y):
    return int(str(x) + str(y)) >= int(str(y) + str(x))


def largest_number(a):
    an = []
    while len(a) != 0:
        ma = ""
        for i in a:
            if gr(i, ma):
                ma = i
        an.append(str(ma))
        a.remove(ma)
    return " ".join(an)


def no(a):
    if len(a) <= 1:
        return a
    else:
        g = no(a[len(a)//2:])
        lg = len(g)
        v = no(a[:len(a)//2])
        lv = len(v)
        i = 0
        j = 0
        while i < len(g):
            if gr(v[j], g[i]):
                g.insert(i, v[j])
                j += 1
                i += 1
            i += 1
            if j == len(v):
                break
            if i == len(g) and j != len(v):
                g += v[j:]
                break
        return g



n = int(input())
x = list(map(int, input().split()))
y=x[:]
print(largest_number(x))
print(no(y))
