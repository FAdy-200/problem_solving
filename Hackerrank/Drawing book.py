n = int(input())
x = int(input())
if x <= n//2:
    print(x//2)
else:
    if n-x == 1 and n % 2 == 0:
        print(1)
    else:
        print((n-x)//2)
