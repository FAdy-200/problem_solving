# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
import re


# d = {}
# l = "abcdefghijklmnopqrstuvwxyz"
# for i in range(1, len(l) + 1):
#     d[l[i-1]] = i
def match(a: str, b: str) -> bool:
    count = 0
    ls = []
    for i in range(len(a)):
        for j in range(len(b)):
            # if i == b:
            #     continue
            if a[i] == b[j] and {i, j} not in ls:
                count += 1
                ls.append({i,j})
                break
    return count == len(a)


for _ in range(int(input())):
    st = input()
    # ls = []
    count = 0
    for i in range(1, len(st)):
        ls = []
        ns = []
        for j in range(len(st) - i + 1):
            ns.append(st[j:j + i])
        for j in range(len(ns)):
            for k in range(len(ns)):
                if j == k:
                    continue
                if  {j, k} not in ls and match(ns[j], ns[k]):
                    ls.append({j, k})
                    count += 1
    print(count)
