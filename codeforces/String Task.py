s = input()
s = s.lower()
x = ["none"]*(len(s))
y = 0
for i in range(len(s)):
    x[i] = s[i]
while y < len(x):
    if x[y] == "a" or x[y] == "o" or x[y] == "y" or x[y] == "e" or x[y] == "u" or x[y] == "i":
        x.remove(x[y])
        y = 0
    else:
        y += 1
y = 0
x.insert(0, ".")
while y < (len(x)-1):
    if x[y] != ".":
        x.insert(y+1, ".")
    y += 1
if x[len(x)-1] == ".":
    x.remove(x[len(x)-1])
y = 0
while y < (len(x)):
    print(x[y], end="")
    y += 1
