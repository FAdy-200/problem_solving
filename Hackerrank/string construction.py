for asdasd in range(int(input())):
    x = input()
    su = len(x)
    d = {}
    for i in x:
        if i not in d.keys():
            d[i] = 0
        else:
            d[i] += 1
    for i in d.values():
        if i > 0:
            su -=i
    print(su)