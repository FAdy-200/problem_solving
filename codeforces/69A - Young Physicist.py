n = int(input())
x = 0
y = 0
z = 0
for i in range(n):
    l = list(map(int, input().split()))
    x += l[0]
    y += l[1]
    z += l[2]

if x == y == z == 0:
    print("YES")
else:
    print("NO")
