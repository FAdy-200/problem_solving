x = int(input())
while x > 0:
    y = int(input())
    z = input()
    Z = z.split()
    for i in range(len(Z)):
        Z[i] = int(Z[i])
    Z.sort()
    result = Z[0]*Z[-1]
    lol = 0
    if len(Z) == 1:
        for i in range(2, Z[0]):
            if Z[0] % i == 0:
                lol = 1
                break
    count = 0
    for i in range(2, result):
        if (result/i) in Z:
            count += 1
    if count == len(Z) and lol == 0:
        print(result)
    else:
        print(-1)
    x -= 1