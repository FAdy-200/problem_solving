x = input()
y = input()
x = x.lower()
y = y.lower()
s = [x, y]
w = [x, y]
s.sort()
if x == y:
    print("0")
elif s == w:
    print("-1")
elif s != w:
    print("1")

