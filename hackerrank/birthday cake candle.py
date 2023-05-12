n = int(input())
x = (list(map(int, input().split())))
s = 0
maximum = max(x)
for i in range(n):
    if x[i] == maximum:
        s += 1
print(s)
