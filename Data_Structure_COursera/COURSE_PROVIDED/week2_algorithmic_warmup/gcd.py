# Uses python3


def gcd2(a, b, lo, g):
    g *= lo
    s = min(a, b)
    for i in range(2, s + 1):
        if a % i == 0 and b % i == 0:
            lo = i
            break
        elif i == s:
            return g
    if s == 1:
        return g
    return gcd2(a // lo, b // lo, lo, g)


def gcd3(a, b):
    h = True
    g = 1
    lo = 1
    while h:
        s = min(a, b)
        g *= lo
        if s == 1:
            h = False
        for i in range(2, s + 1):
            if a % i == 0 and b % i == 0:
                lo = i
                break
            elif i == s:
                h = False
        a = a // lo
        b = b // lo
    return g


def gcd4(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
print(gcd(a,b))



