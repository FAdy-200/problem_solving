n = int(input())
x = list(map(int, input().split()))
d = {}
for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(sum(d.values()) - max(d.values()))

# https://www.hackerrank.com/challenges/equality-in-a-array/problem
