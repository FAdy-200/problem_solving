o = int(input())
for _ in range(o):
    y = list(map(int, input().split()))
    x = (y[1] + y[2] - 1) % y[0]
    if y[1]+y[2] < y[0]:
        print((y[1] + y[2]-1))
    elif x == 0:
        print(y[0])
    else:
        print(x)














