# Uses python3
def lcm_naive(a, b):
    mi = min(a, b)
    ma = max(a, b)
    for l in range(mi, mi * ma + 1, mi):
        if l % a == 0 and l % b == 0:
            return l
    return a * b


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    k = a//g
    return k*b


a, b = map(int, input().split())
print(lcm(a, b))
