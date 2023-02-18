n = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = []
w = []
for i in range(max(x), min(y)+1):
    for j in x:
        if i % j == 0:
            if i not in z:
                z.append(i)
m = 0
zl = len(z)
while m < len(z):
    for j in x:
        if z[m] % j != 0:
            w.append(z[m])
    m += 1
k = 0
while k < len(z):
    for j in y:
        if j % z[k] != 0:
            w.append(z[k])
    k += 1
w = list(set(w))
for i in w:
    if i in z:
        z.remove(i)
print(len(z))