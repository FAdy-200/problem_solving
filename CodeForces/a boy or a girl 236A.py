c = input()
d = {}
for i in c:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

if len(d.keys()) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")