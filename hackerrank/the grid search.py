import re
cn = int(input())
for _ in range(cn):
    n, m = map(int, input().split())
    x = ""
    for __ in range(n):
        x = x+"."+input()
    q, w = map(int, input().split())
    loc = "({})".format(input())
    print(loc)
    for ___ in range(q-1):
        loc = loc+".{"+format(m-w+1)+"}"+"({}55)".format(input())
    se = re.search(loc, x)
    # re.findall()
    print(x)
    print(loc)
    print(se)
    if se:

        print("YES")
    else:
        print("NO")


# import re
#
# def gridSearch(G, P):
#     print(G, P)
#     n = len(P)
#     res = ''
#     for i in range(len(G)):
#         if P[0] not in G[i]:
#             pass
#         else:
#             # x= G[i].index(P[0])
#             x = [i.start() for i in re.finditer(P[0], G[i])]
#             print(x)
#             for u in range(1, n):
#                 z = re.search(P[u], G[i+u])
#                 if z:
#                     if z.span()[0] in x:
#                         if u == n-1:
#                             return 'YES'
#                 else:
#                     break
#     return 'NO'
#
# for _ in range(int(input())):
#     big = []
#     small = []
#     R, C = map(int, input().split())
#     for __ in range(R):
#         big.append(input())
#     r, c = map(int, input().split())
#     for __ in range(r):
#         small.append(input())
#     print(gridSearch(big, small))
