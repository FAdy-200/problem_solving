n = list(map(int, input().split()))
q = list(map(int, input().split()))
x1 = min(q) - 1
x2 = min(n[0] - q[0], q[1] - 1)
x3 = min(n[0] - q[0], n[0] - q[1])
x4 = min(q[0] - 1, n[0] - q[1])
ma = n[0] * 2 - 2 + x1 + x2 + x3 + x4
for i in range(n[1]):
    x = list(map(int, input().split()))
    if x[0] == q[0] and x[1] > q[1]:
        ma -= n[0]-x[1]+1
    if x[0] == q[0] and x[1] < q[1]:
        ma -= x[1]
    if x[1] == q[1] and x[0] > q[0]:
        ma -= n[0] - x[0] + 1
    if x[1] == q[1] and x[0] < q[0]:
        ma -= x[0]
    if abs(x[1]-q[1]) == abs(x[0]-q[0]):
        if x[1]-q[1] > 0 and x[0]-q[0] > 0 and abs(x[1]-q[1]) < x3:
            ma -= (x3-abs(x[1]-q[1]))+1
            x3 = abs(x[1]-q[1])-1
        if x[1] - q[1] > 0 > x[0] - q[0] and abs(x[1]-q[1]) < x4:
            ma -= (x4-abs(x[1]-q[1]))+1
            x4 = abs(x[1] - q[1])-1
        if x[1] - q[1] < 0 < x[0] - q[0] and abs(x[1]-q[1]) < x2:
            ma -= (x2-abs(x[1]-q[1]))+1
            x2 = abs(x[1] - q[1])-1
        if x[1] - q[1] < 0 and x[0] - q[0] < 0 and abs(x[1]-q[1]) < x1:
            ma -= (x1-abs(x[1]-q[1]))+1
            x1 = abs(x[1] - q[1])-1
print(ma)


# https://www.hackerrank.com/challenges/queens-attack-2/problem