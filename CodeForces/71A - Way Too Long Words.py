x = int(input())
s = ["none"]*x
for i in range(x):
    s[i] = input()
for i in range(x):
    if len(s[i]) <= 10:
        print(s[i])
    else:
        print((s[i])[0], end="")
        print(((len(s[i]))-2), end="")
        print((s[i])[-1])
