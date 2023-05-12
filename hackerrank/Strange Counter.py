# https://www.hackerrank.com/challenges/strange-code/problem

n = int(input())
sul = 0
su = 0
i = 0
while su < n:
    sul = su
    su += (2 ** i) * 3
    i += 1
# print((2 ** (i-1)) * 3)
# print(su)
print(su - n + 1)
