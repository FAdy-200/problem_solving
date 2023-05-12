letters = "abcdefghijklmnopqrstuvwxyzABCDEFJHIGKLMNOPQRSTUVWXYZ"
z = input()
Z = z.split()
Z[0] = int(Z[0])
Z[1] = int(Z[1])
x = []
X = []
for i in range(Z[0]):
    x.append(input())
for i in range(Z[1]):
    for c in range(Z[0]):
        X.append(x[c][i])
for i in range(1, len(X)+1):
    if X[-i] in letters:
        last = len(X)-i
        break
for i in range(last):
    if X[i] in letters:
        first = i
        break
for i in range(first, last):
    if X[i] not in letters:
        X[i] = " "
ans = []
s = 0
while s < last:
    if X[s] == " " and X[s+1] == " ":
        ans.append(X[s])
        s += 2
    else:
        ans.append(X[s])
        s += 1
for i in range(last, len(X)):
    ans.append(X[i])
for i in ans:
    print(i, end="")
