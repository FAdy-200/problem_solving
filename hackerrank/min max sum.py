x = (list(map(int, input().split())))
s = []
for i in range(len(x)):
    su = 0
    z = []
    for l in range(len(x)):
        if l != i:
            z.append(x[l])
    for l in z:
        su += l
    s.append(su)

print(min(s), max(s))