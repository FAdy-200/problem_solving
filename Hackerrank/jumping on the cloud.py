n = list(map(int, input().split()))
x = list(map(int, input().split()))
e = 100
place = 0
place = (place + n[1]) % n[0]
if x[place] == 1:
    e -= 3
else:
    e -= 1
while place != 0:
    place = (place + n[1]) % n[0]
    if x[place] == 1:
        e -= 3
    else:
        e -= 1
print(e)


# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
