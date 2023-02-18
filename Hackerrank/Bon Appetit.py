n = (list(map(int, input().split())))
x = (list(map(int, input().split())))
y = int(input())
su = 0
for i in range(len(x)):
    if i == n[1]:
        continue
    else:
        su += x[i]
su = int(su/2)

if y == su:
    print("Bon Appetit")
else:
    print(abs(y-su))
