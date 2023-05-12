d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))
d = d2[0] - d1[0]
m = d2[1] - d1[1]
y = d2[2] - d1[2]

if y < 0:
    print(10000)
elif m < 0 and y == 0:
    print(abs(500 * m))
elif d < 0 and m == 0 and y == 0:
    print(abs(15 * d))
else:
    print(0)

# https://www.hackerrank.com/challenges/library-fine/problem
