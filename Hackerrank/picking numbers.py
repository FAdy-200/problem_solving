n = int(input())
x = list(map(int, input().split()))
ma = 0
for i in x:
    a = x.count(i)
    b = x.count(i-1)
    if a+b > ma:
        ma = a+b

print(ma)


# https://www.hackerrank.com/challenges/picking-numbers/problem