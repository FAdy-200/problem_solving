n, d, x, gg = int(input()), {}, list(map(int, input().split())), []
for i in range(n):
    if x[i] in d:
        d[x[i]] += 1
    else:
        d[x[i]] = 1
dm = max(d.values())
for i in d:
    if d[i] == dm:
        gg.append(i)
print(min(gg))











































