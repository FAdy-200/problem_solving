x = list(map(int, input().split()))
if x[1]-x[3] != 0 and (x[2]-x[0]) >= (x[1]-x[3]):
    z = (x[2]-x[0])/(x[1]-x[3])
    if z > 0 and z % int(z) == 0:
        print('YES')
    else:
        print('NO')
elif x[2] == x[1]:
    print("YES")
else:
    print('NO')















