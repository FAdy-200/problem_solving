# https://www.hackerrank.com/challenges/circular-array-rotation/problem


k = list(map(int, input().split()))
x = list(map(int, input().split()))
for i in range(k[1]):
    temp = x.pop()
    x.insert(0, temp)

for i in range(k[2]):
    n = int(input())
    print(x[n])
