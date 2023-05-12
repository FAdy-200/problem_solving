def stri(a, b, ans):
    if len(b) == 0:
        return ans + a
    elif len(a) == 0:
        return ans + b
    else:
        if (ans + a[0]) < (ans + b[0]):
            ans = ans + a[0]
            a = a[1:]
        elif (ans + a[0]) > (ans + b[0]):
            ans = ans + b[0]
            b = b[1:]
        else:
            if a[0] > b[0]:
                ans = ans + b[0]
                b = b[1:]
            else:
                ans = ans + a[0]
                a = a[1:]
    return stri(a, b, ans)


def morgan(a, b):
    a += 'z'
    b += 'z'
    ai = 0
    ab = 0
    for _ in range(len(a) + len(b) - 2):
        if a[ai:] < b[ab:]:
            yield a[ai]
            ai += 1
        else:
            yield b[ab]
            ab += 1


n = int(input())
for _ in range(n):
    a = input()
    b = input()
    a += 'z'
    b += 'z'
    ai = 0
    ab = 0
    ans = ""
    for __ in range(len(a) + len(b) - 2):
        if a < b:
            ans += a[0]
            a = a[1:]
        else:
            ans += b[0]
            b = b[1:]
    print(ans)
