import math
s = input().split()
s = ''.join(s)
z = len(s)
l = math.sqrt(z)
ma = math.ceil(l)
i = 0
while i < z and i < ma:
    print(s[i::ma], end=" ")
    i += 1






















































































