x = list(map(int, input().split()))
l = [str(c) for c in range(x[0], x[1]+1)]
lr = []
z = 0
for i in l:
    lr.append(i[::-1])
l, lr = list(map(int, l)), list(map(int, lr))
for i in range(len(l)):
    if abs(l[i]-lr[i]) % x[2] == 0:
        z += 1

print(z)