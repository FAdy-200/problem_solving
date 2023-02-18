x = int(input())
print("I hate", end="")
for i in range(2, x+1):
    if i % 2 == 0:
        print(" that I love", end="")
    else:
        print(" that I hate", end="")

print("it")
