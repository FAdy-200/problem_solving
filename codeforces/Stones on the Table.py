num = int(input())
x = ["none"]*num
X = input()
y = 0
for i in range(num):
    x[i] = X[i]
for i in range(num-1):
    if x[i] == x[i+1]:
        y += 1
if y == num:
    y -= 1
print(y)
