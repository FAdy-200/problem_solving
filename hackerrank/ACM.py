n, m = map(int, input().split())
x = []
for i in range(n):
    x.append(input())
def top(a,b,c):
    if len(a) == 2:
        kk = 0
        for j in range(len(a[0])):
            if a[0][j] == "1" or a[1][j] == "1":
                kk += 1
        return a, 1, kk
    elif len(a) < 2:
        return a, b, c
    else:
        g = top(a[len(a)//2:], 0, 0)
        h = top(a[:len(a)//2], 0, 0)
        if g[2] >=h[2]:
            y=(g[0][:],g[1],g[2])
            lo=(h[0][:],h[1],h[2])
        else:
            y=(h[0][:],h[1],h[2])
            lo=(g[0][:],g[1],g[2])
        x=y[0][:]
        n=y[1]
        nt=y[2]
        ind = -1
        for i in y[0]:
            for o in range(len(lo[0])):
                kk = 0
                for j in range(len(i)):
                    if i[j] == "1" or lo[0][o][j] == "1":
                        kk += 1
                if kk > nt:
                    n = 1
                    nt = kk
                    x = [i, lo[0][o]]
                elif kk == nt:
                    n += 1
                    if ind != o:
                        x.append(lo[0][o])
                        ind = o
        return x, n, nt

z = top(x,0,0)
print(z[2])
print(z[1])


