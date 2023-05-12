orange = 0
apple = 0

home = list(map(int, input().split()))
ao = list(map(int, input().split()))
z = list(map(int, input().split()))
if z[0] != 0:
    a = list(map(int, input().split()))
if z[1] != 0:
    o = list(map(int, input().split()))
for i in range(z[0]):
    if ao[0]+a[i] in range(home[0], home[1]+1):
        apple += 1

for i in range(z[1]):
    if ao[1]+o[i] in range(home[0], home[1]+1):
        orange += 1

print(apple)
print(orange)

