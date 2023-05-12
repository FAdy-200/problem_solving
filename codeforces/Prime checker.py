num = int(input())
x = num
y = 0
runNumber = 0
while x != 1 and x > 0:
    if num % (x-1) == 0:
        y += 1
    x -= 1
    runNumber += 1
if y > 1 or num == 1 or num == 0:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number\n")
print("it is dividable by", y, "numbers")