n = int(input())
x = list(map(int, input().split()))
z = 0
p = 0
ne = 0
for i in x:
    if i == 0:
        z += 1
    elif i < 0:
        ne += 1
    elif i > 0:
        p += 1
p = p/n
z = z/n
ne = ne/n
print('%.6f' % p)
print('%.6f' % ne)
print('%.6f' % z)

