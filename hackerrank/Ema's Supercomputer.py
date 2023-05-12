import re

n, m = map(int, input().split())
# z = ""
# for _ in range(n):
#     z = z+input()
# print(z)
# p = []
# for i in range(1, max(n, m)-2):
#     pa = (('(G).{'+str(m-1)+'}')*(((n-i)//2)))+(('(G).{'+str(m-m)+'}'))\
#          +('(G){'+str(m-i)+'}')+(('(G).{'+str(m-m)+'}'))\
#          +(('(G).{'+str(m-1)+'}')*(((n-i)//2)))
#     p.append(pa)
# print(p)
z = []
for _ in range(n):
    z.append(input())
ans = {}
for i in range(len(z)):
    for j in range(len(z[0])):
        if z[i][j] == "G":
            v1 = 0
            v2 = 0
            h1 = 0
            h2 = 0
            for k in range(i, n):
                if z[k][j] == "G":
                    v1 += 1
                else:
                    break
            for k in range(i, -1, -1):
                if z[k][j] == "G":
                    v2 += 1
                else:
                    break
            for k in range(j, -1, -1):
                if z[i][k] == "G":
                    h1 += 1
                else:
                    break
            for k in range(j, m):
                if z[i][k] == "G":
                    h2 += 1
                else:
                    break
            s = min(v1, h1, v2, h2) * 4 - 3
            ans[s] = i, j
print(ans)
