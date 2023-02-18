num = int(input())
x = 0
for i in range(num):
    Op = input()
    for y in range(2):
        if Op[y] == "+" and Op[y+1] == "+":
            x += 1
        elif Op[y] == "-" and Op[y+1]== "-":
            x -= 1
print(x)
