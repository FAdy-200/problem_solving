n = int(input())
for i in range(n):
    c = 0
    x = int(input())
    s = str(x)
    for j in s:
        if int(j) == 0:
            pass
        elif x % int(j) == 0:
            c += 1
    print(c)

# https://www.hackerrank.com/challenges/find-digits/problem
