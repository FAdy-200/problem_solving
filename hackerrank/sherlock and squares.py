import numpy as np

n = int(input())
for i in range(n):
    co = 0
    x = list(map(int, input().split()))
    k = np.ceil(np.sqrt(x[0]))
    while True:
        if k ** 2 in range(x[0], x[1] + 1):
            co += 1
            k += 1
        else:
            break
    print(co)
