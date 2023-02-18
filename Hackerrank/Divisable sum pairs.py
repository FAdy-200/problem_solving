n = list(map(int, input().split()))
x = list(map(int, input().split()))
c = 0
d = {}

for i in range(n[0]):
    for j in range(i+1, n[0]):
        if (x[j]+x[i]) % n[1] == 0:
            c += 1
print(c)

