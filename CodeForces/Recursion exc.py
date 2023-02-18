def lol(x):
    if x == 1:
        return 1
    else:
        return x + lol(x - 1)


def fab(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return fab(x - 2) + fab(x - 1)


l_counter = 0


def l(x):
    global l_counter
    y = x // 10
    l_counter += 1
    if y == 0:
        return l_counter
    else:
        return l(x // 10)


def h(x):
    if len(x) == 1:
        return x[0]
    elif int(x[0]) >= int(x[1]):
        x.remove(x[1])
        return h(x)
    else:
        x.remove(x[0])
        return h(x)


def h1(x):
    if len(x) == 1:
        return x[0]
    elif int(x[0]) <= int(x[1]):
        b = x[1:len(x)]
        return h1(b)
    else:
        b = x[2:len(x)]
        b.insert(0, x[0])
        return h1(b)


x = input()
X = x.split()
print(h1(X))
print(h(X))
