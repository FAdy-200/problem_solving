from copy import *
n = list(map(int, input().split()))
x = [list(input()) for i in range(n[0])]
pc = []
x3 = []
x5 = []
for i in range(1, n[2]):
    if i % 2 != 0:
        p = []
        for j in range(n[0]):
            for k in range(n[1]):
                if x[j][k] == "O":
                    p.append([j, k])

        if i == 1:
            for j in range(n[0]):
                for k in range(n[1]):
                    if x[j][k] == ".":
                        x[j][k] = "O"
        else:
            for [j, k] in pc:
                x[j][k] = "O"
                if not k == n[1] - 1:
                    x[j][k + 1] = "O"
                if not k == 0:
                    x[j][k - 1] = "O"
                if j != n[0] - 1:
                    x[j + 1][k] = "O"
                if j != 0:
                    x[j - 1][k] = "O"
        pc = p.copy()
    else:
        for [j, k] in p:
            x[j][k] = "."
            if not k == n[1]-1:
                x[j][k+1] = "."
            if not k == 0:
                x[j][k-1] = "."
            if j != n[0]-1:
                x[j+1][k] = "."
            if j != 0:
                x[j-1][k] = "."
    if i == 2:
        x3 = deepcopy(x)
    elif i == 4:
        x5 = deepcopy(x)
    if i >= 4:
        break
if (n[2]-1) % 4 == 0 and n[2] >= 4:
    for i in range(n[0]):
        print("".join(x5[i]))
elif (n[2]-1) % 2 == 0 and (n[2]-1) % 4 != 0 and n[2] >= 2:
    for i in range(n[0]):
        print("".join(x3[i]))
elif n[2] % 2 == 0:
    print(("O"*n[1]+"\n")*n[0])
else:
    for i in range(n[0]):
        print("".join(x[i]))







































































































