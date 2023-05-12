n = int(input())
xs, ys = 10,3
l= [(6,6), (6,7),(7,6) ,(7,7), (9,2) ,(9,3),(9,10),(9,11),(10,2), (10,10)]
for _ in range(n):
    x, y = map(int, input().split())
    a  = x-1
    c=1
    b=y
    while a > 1 and b >1:

        if (a,b) == xs ,ys  :
            return c
        elif (a-1,b) in l:
            # a -=1
            # b +=1
            up = 1
        elif (a, b-1) in l:
            left = 1
        # else:
        #     a-=1
        if left and not up:
            b -= 1
            c += 1
        elif up and not left:
            a -= 1
            c += 1
        if b == 1 and b != 1:
            a-=1
            c+= 1
