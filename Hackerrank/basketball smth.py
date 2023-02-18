n = int(input())
x = list(map(int, input().split()))
d = {"h": x[0], "l": x[0]}
h = 0
l = 0
for i in x:
    if i > d["h"]:
        h += 1
        d["h"] = i
    if i < d["l"]:
        l += 1
        d["l"] = i

print('{} {}'.format(h, l))
