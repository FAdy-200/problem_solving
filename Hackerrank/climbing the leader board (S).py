n1 = int(input())
x = (list(map(int, input().split())))
x = list(set(x))
x.sort()
x.reverse()
n1 = len(x)
n2 = int(input())
a = (list(map(int, input().split())))

for i in a:
    high = n1-1
    low = 0
    ans = n1
    while low <= high:
        guess = int(low + (high-low)/2)
        if i >= x[guess]:
            high = guess-1
            ans = guess
        else:
            low = guess + 1
    print(ans+1)






























































































