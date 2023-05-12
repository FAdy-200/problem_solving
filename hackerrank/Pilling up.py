from collections import deque

n = int(input())
for i in range(n):
    k = int(input())
    x = list(map(int, (input().split())))
    x = deque(x)
    m = 2 ** 31

    p = 0
    for j in range(k):
        if x[-1] <= x[0] <= m:
            m = x[0]
            x.popleft()
            p += 1
        elif x[0] <= x[-1] <= m:
            m = x[-1]
            x.pop()
            p += 1
        else:
            break
    if p == k:
        print("Yes")
    else:
        print("No")
# https://www.hackerrank.com/challenges/piling-up/problem