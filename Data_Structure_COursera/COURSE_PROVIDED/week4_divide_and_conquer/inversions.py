def merge(x):
    if len(x) == 1:
        return x, 0
    avg = len(x) // 2
    xl = merge(x[:avg])
    xr = merge(x[avg:])
    i = 0
    xll = len(xl[0])
    j = 0
    xrl = len(xr[0])
    k = xr[1]
    while True:
        if i >= xll or j >= xrl:
            break
        if xl[0][i] > xr[0][j]:
            xl[0][i], xr[0][j] = xr[0][j], xl[0][i]
            xr = merge(xr[0])
            i += 1
            k += 1 + xr[1]
        else:
            i += 1
    return xl[0] + xr[0], xl[1]+k


n = int(input())
x = list(map(int, input().split()))
print(merge(x)[1])
