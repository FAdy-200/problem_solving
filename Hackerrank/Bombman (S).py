n, m, q = map(int, input().split())

x = []
cur = [list(input()) for i in range(n)]

def cp(l):
    ret = [x[:] for x in l]
    return ret
x.append(cp(cur))

while True:
    last = cp(x[-1])
    cur = cp(last)
    for i in range(n):
        for j in range(m):
            if last[i][j] == "O":
                cur[i][j] = "."
            elif (i > 0 and last[i-1][j] == "O") or (i < n-1 and last[i+1][j] == "O"):
                cur[i][j] = "."
            elif (j > 0 and last[i][j-1] == "O") or (j < m-1 and last[i][j+1] == "O"):
                cur[i][j] = "."
            else:
                cur[i][j] = "O"
    if cur in x:
        break
    else:
        x.append(cp(cur))
start = 0
for i in range(len(x)):
    if x[i] == cur:
        start = i
        break

if q == 1:
    for row in x[0]:
        print("".join(row))
elif q%2 == 0:
    print( ("O"*m+"\n")*n )
else:
    q = (q - (2*start + 1))//2

    ans = x[ start+ (q)%(len(x)-start) ]
    for row in ans:
        print("".join(row))









































































































