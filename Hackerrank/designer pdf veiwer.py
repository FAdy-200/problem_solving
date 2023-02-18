l = "abcdefghijklmnopqrstuvwxyz"

x = list(map(int, input().split()))
c = []
s = input()
for i in s:
    c.append(x[l.index(i)])

print(max(c)*len(s))

