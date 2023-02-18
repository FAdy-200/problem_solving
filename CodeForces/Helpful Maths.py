s = input()
x = ["none"]*(len(s))
for i in range(len(s)):
    x[i] = s[i]
x.sort()
y = (len(x)-1)/2
y = int(y)
for z in range(y):
    x.remove(x[0])
    z += 1
z = 0
Z = (len(x)*2)-1
while z < Z:
    if z % 2 == 0:
        x.insert(z, "+")
    z += 1
x.remove(x[0])
for i in range(len(x)):
    print(x[i], end="")
