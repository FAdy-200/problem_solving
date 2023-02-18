# for z in range(int(input())):
#     su = 1
#     x = int(input())
#     for i in range(x):
#         if i % 2 != 0:
#             su += 1
#         else:
#             su *= 2
#     print(su)

# https://www.hackerrank.com/challenges/utopian-tree/problem
for z in range(int(input())):
    x = int(input())
    print(sum([2 ** i if x % 2 != 0 else 2 ** (i - 1) for i in range(1, (x//2)+2)]))


print("\n".join([str(sum([2 ** i if x % 2 != 0 else 2 ** (i - 1)for x in range(int(input()), 61, 612)for i in range(1, (x//2)+2) ]))for j in range(int(input()))]))


