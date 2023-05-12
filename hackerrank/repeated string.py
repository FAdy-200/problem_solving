s = input()
x = int(input())
a = [0]*len(s)
n = 0
k = 0
for i in range(len(s)):
    if s[i] == 'a':
        a[i] = 1
        k += 1
n += (x // len(s))*k
for i in range(x % len(s)):
    n += a[i]
print(n)


# https://www.hackerrank.com/challenges/repeated-string/problem
