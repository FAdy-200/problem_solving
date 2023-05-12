n = list(map(int, input().split()))
x = list(map(int, input().split()))
cou = [0]*(n[1])
for i in x:
    cou[(i % n[1])] += 1
ma = 0
for i in range(1, n[1]):
    if cou[i] > cou[-i]:
        max += cou[i]
if cou[0] > 0:
    max += 1
if n[1] % 2 == 0:
    max += 1
print(ma)


# https://www.hackerrank.com/challenges/non-divisible-subset/problem
