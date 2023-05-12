n = int(input())
x = list(map(int, input().split()))
k = 1
for i in range(n):
    print(x.index(x.index(k) + 1) + 1)
    k += 1

# https://www.hackerrank.com/challenges/permutation-equation/problem
