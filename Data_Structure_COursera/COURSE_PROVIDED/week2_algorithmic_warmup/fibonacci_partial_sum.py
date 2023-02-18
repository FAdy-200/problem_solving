def getPattern(x):
    p = [x[0]]
    h = True
    i = 1
    while h:
        c = len(p)
        ff = x[c:c + c]
        if len(ff) < c:
            p += ff
            h = False
        elif ff == p:
            h = False
        else:
            p.append(x[c])
            i = 1
        i += 1
    return p

def calc_fib(n):
    if n == 0:
        return 0
    p = 0
    c = 1
    for i in range(1, n):
        p, c = c, (c + p)
    return c

m, n = map(int, (input().split()))
d = []
for i in range(120):
    d.append(calc_fib(i) % 10)
p = getPattern(d)
le = len(p)
if m == n:
    print(p[n % le])
elif n <= le:
    print(sum(p[m:n+1]) % 10)
elif m < le:
    s1 = sum(p[m:n-m+1])
    s2 = sum(p)*(n//le)
    s3 = sum(p[:n % le+1])
    print((s1+s2+s3) % 10)
else:
    s1 = sum(p[m % le:n-m+1])
    s2 = sum(p) * (n // le)
    s3 = sum(p[:n % le+1])
    print((s1+s2+s3) % 10)

