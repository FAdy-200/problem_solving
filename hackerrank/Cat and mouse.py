n = int(input())
y = []
for i in range(n):
    x = list(map(int, input().split()))
    z = abs(x[0]-x[2])-abs(x[1]-x[2])
    if z == 0:
        y.append('Mouse C')
    elif z > 0:
        y.append('Cat B')
    else:
        y.append('Cat A')
for i in y:
    print(i)







































































































