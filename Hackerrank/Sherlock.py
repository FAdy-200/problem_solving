x = input()
lol = 0
d = {}
dk = {}
for i in x:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
for i in d.values():
    if i not in dk.keys():
        dk[i] = 1
    else:
        dk[i] += 1
if len(x) == 1 or len(dk.items()) == 1:
    lol = True
elif len(dk.items()) != 2:
    lol = False
elif 1 in dk.keys():
    if dk[1] == 1:
        lol = True
elif max(dk.keys()) == min(dk.keys())+1 and dk[max(dk.keys())] == 1:
    lol = True
else:
    lol = False
if lol:
    print("YES")
else:
    print("NO")
