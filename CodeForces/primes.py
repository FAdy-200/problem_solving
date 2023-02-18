# n = int(input())
p = [2]

n = int(10e7)
for i in range(3, n):
    c = True
    for j in p:
        if i % j == 0:
            c = False
            break
    if c:
        p.append(i)
print(p)
# try:
#     if n-2 == p[-1]:
#         print(2, p[-1])
#     else:
#         print(-1)
# except:
#     print(-1)





































# https://codeforces.com/gym/102267/problem/B