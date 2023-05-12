n = int(input())
for _ in range(n):
    x = input()
    inq = int(input())
    z = []
    for i in range(len(x)):
        for j in range(i+1, len(x)+1):
            z.append(x[i:j])
    z = sorted(z)
    m = ("".join(z))
    print(m)
    print(m[inq-1])


# https://www.hackerrank.com/challenges/ashton-and-string/problem