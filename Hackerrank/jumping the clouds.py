n = int(input())
x = list(map(int, input().split()))
z = 0
j = 0
for i in x:
    if i == 0:
        z += 1
    else:
        j += (z//2)+1
        z = 0
j += (z//2)

print(j)


# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem







