n = int(input())
x = list(map(int, input().split()))
y = 1
while y:
    mi = min(x)
    cou = 0
    i = 0
    while i < (len(x)):
        x[i] -= mi
        if x[i] > 0:
            cou += 1
        elif x[i] == 0:
            cou += 1
            x.pop(i)
            i -= 1
        i += 1
    if len(x) == 0:
        y = 0
    print(cou)


# https://www.hackerrank.com/challenges/cut-the-sticks/problem















