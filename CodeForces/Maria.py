n = int(input())
xs, ys = 10,3
l= [(6,6), (6,7),(7,6) ,(7,7), (9,2) ,(9,3),(9,10),(9,11),(10,2), (10,10)]
for _ in range(n):
    x, y = map(int, input().split())
    a= x
    b  = y
    c=0
    S =""
    check =False
    while a != 1 and b !=1:
        if (a,b) == (xs ,ys)  :
            check = True
            break
        elif (a,b) in l:
            a -=1
            b +=1
            c+=1
            S+="U"
        else:
            b-=1
            c+=1
            S+="L"
            if b == 1 and a != 1:
                while a!=1:
                    a-=1
                    c+=1
                    S+="U"
    if not check:
        c+=4
        S += 'RRDD'
    else:
        pass
    print(c)
    print(S)
