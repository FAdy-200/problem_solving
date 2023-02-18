# import re
#
# n = list(map(int, input().split()))
# a = []
# b = []
# for i in range(n[0]):
#     a.append(input())
# for i in range(n[1]):
#     b.append(input())
# a = "".join(a)
#
# for i in b:
#     p = i
#     f = re.finditer(p, a)
#     k = []
#     for j in f:
#         k.append(str(j.start() + 1))
#     if len(k) > 0:
#         print(" ".join(k))
#     else:
#         print("-1")
from collections import defaultdict
n = list(map(int, input().split()))
a = defaultdict(list)
for i in range(n[0]):
    a[input()].append(str(i+1))
for i in range(n[1]):
    m = input()
    if len(a[m]) > 0:
        print(" ".join(a[m]))
    else:
        print(-1)












