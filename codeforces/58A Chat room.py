import re

p = r'h+e+l+o+'
x = input()
if re.search(p, x):
    print("YES")
else:
    print("NO")
