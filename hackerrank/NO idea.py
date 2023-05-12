n = list(map(int, input().split(" ")))
x = input().split(" ")
a = (input().split(" "))
b = (input().split(" "))
h = 0
for i in x:
    if i in a:
        h += 1
    elif i in b:
        h -= 1

print(h)
# https://www.hackerrank.com/challenges/no-idea