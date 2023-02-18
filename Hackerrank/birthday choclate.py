n = int(input())
x = list(map(int, input().split()))
b = list(map(int, input().split()))
a = 0
for i in range(n):
    if sum(x[i:i+b[1]]) == b[0]:
        a += 1

print(a)

