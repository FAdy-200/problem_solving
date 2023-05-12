z = 5
l = []
for i in range(int(input())):
    l .append(z//2)
    z = l[-1]*3
print(sum(l))