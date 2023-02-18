s = input()
n = ["none"]*len(s)
for i in range(len(s)):
    n[i] = s[i]
x = input()
z = ["none"]*len(x)
for i in range(len(x)):
    z[i] = x[i]
i = 0
while i < len(z)-1:
    if z[i] != " " and z[i+1] != " ":
        z[i] = (z[i]+z[i+1])
        z.remove(z[i+1])
    else:
        i += 1
i = 0
while i < len(n)-1:
    if n[i] != " " and n[i+1] != " ":
        n[i] = (n[i]+n[i+1])
        n.remove(n[i+1])
    else:
        i += 1
z.sort()
y = (len(z)-1)/2
y = int(y)
for i in range(y):
    z.remove(z[0])
    i += 1
advanced = 0
for t in range(len(z)):
    z[t] = int(z[t])
z.sort()
for i in range(len(z)):
    if int(z[i]) >= int(z[(int(n[0])-int(n[2]))]) and int(z[i]) != 0:
        advanced += 1
print(advanced)
