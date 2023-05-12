n = int(input())
for i in range(n):
    z = []
    s = 0
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    for j in range(x[0] + 1):
        if sum(y[:j]) > x[1]:
            z.append(y[:j])
    for j in z:
        if sum(j) - max(j) > x[1]:
            s = z.index(j) - 1
            break

    try:
        print((z[s].index(max(z[s]))) + 1)

    except:
        print(0)
























