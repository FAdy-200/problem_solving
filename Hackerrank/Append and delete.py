s1 = list(input())
s2 = list(input())
n = int(input())
e = 0
mi = min(len(s1), len(s2))
while e < mi and s1[e] == s2[e]:
    e += 1

t = len(s1) - e + len(s2) - e
if t == n or n >= len(s1)+len(s2):
    print('Yes')
elif t > n or (n - t) % 2:
    print('No')
else:
    print('Yes')