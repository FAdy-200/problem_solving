import math
n = int(input())
x = list(map(int, input().split()))
d = {}
z = 0
for i in x:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for i in d.values():
    if i >= 2:
        z += math.floor(i/2)

print(z)