import re
n, x, y, p, w, ans = list(map(int, input().split())), [], [], r"[a-zA-Z]", 0, []
for i in range(n[0]):
    l = []
    for z in input():
        l.append(z)
    x.append(l)
for i in range(n[1]):
    for j in range(n[0]):
        y.append(x[j][i])
for i in range(len(y)):
    if re.match(p, y[i]) and w == 0:
        first = i
        w = 1
    if re.match(p, y[i]):
        last = i
for i in range(first, last + 1):
    if not re.match(p, y[i]):
        y[i] = " "
c = first
if last == len(y):
    last += 1
for i in range(first):
    ans.append(y[i])
while first <= c <= last:
    if y[c] == " " and y[c+1] == " ":
        ans.append(y[c])
        c += 1
    else:
        ans.append(y[c])
    c += 1
for i in range(last+1, len(y)):
    ans.append(y[i])
print("".join(ans))





