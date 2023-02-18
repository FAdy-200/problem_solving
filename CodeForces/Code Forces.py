l = int(input())
for _ in range(l):
    x = list(map(int, input().split()))
    d = ['a'] * x[0]
    k = abs(1 - (1 + 4 * 1 * x[1] * 2) ** 0.5) / 2
    j = int(k)
    m = k - j
    if m == 0:
        d[-j], d[-j - 1] = "b", "b"
    else:
        n = x[1]-((j*(j+1))/2)
        n = int(n)
        d[-j-2],d[-n] = "b","b"

    print("".join(d))

