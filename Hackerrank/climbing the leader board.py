n1 = int(input())
X = (list(map(int, input().split())))
x = list(set(X))
x.sort()
x.reverse()
n1 = len(x)
n2 = int(input())
a = (list(map(int, input().split())))

for i in a:
    if i in x:
        print(x.index(i)+1)
    elif i >= x[0]:
        print(1)
    elif i <= x[-1]:
        print(len(x)+1)
    else:
        high = n1-1
        low = 0
        while low != high-1:
            guess = int((high + low) / 2)
            if i > x[guess]:
                high = guess
            else:
                low = guess
        print(high+1)






























































































