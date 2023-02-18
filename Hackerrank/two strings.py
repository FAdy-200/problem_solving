n = int(input())
for i in range(n):
    a = input()
    b = input()
    da = {}
    db = {}
    for l in a:
        if l not in da.keys():
            da[l] = 0
        else:
            da[l] += 1
    for l in b:
        if l not in db.keys():
            db[l] = 0
        else:
            db[l] += 1
    for l in da.keys():
        if l in db.keys():
            lol = True
            break
        else:
            lol = False
    if lol:
        print("YES")
    else:
        print("NO")