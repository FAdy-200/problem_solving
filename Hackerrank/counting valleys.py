n = int(input())
x = list(input())
d = 0
v = 0
g = 0
for i in x:

    if i == 'D':
        d += 1
    else:
        v += 1
    if d == v and i == 'U':
        g += 1
print(g)

# https://www.hackerrank.com/challenges/counting-valleys/problem
