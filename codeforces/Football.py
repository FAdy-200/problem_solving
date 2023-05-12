s = input()
x = 0
i = 0
while x < 1 and i in range(len(s)):

    if s[i:i+7] == "1111111"or s[i:i+7] == "0000000":
        x += 1
        print("YES")
    i += 1


if x == 0:
    print("NO")
