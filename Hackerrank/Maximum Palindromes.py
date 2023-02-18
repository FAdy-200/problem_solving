# https://www.hackerrank.com/challenges/maximum-palindromes/problem
import math

tst = open("test.txt", "r")
nan = open("output.txt", "r")
s = tst.readline()
freq = dict()
for i in range(len(s)):
    if freq.get(s[i]):

        freq[s[i]][0] += 1
        freq[s[i]][1].append(i)
    else:
        freq[s[i]] = [1, [i]]
for _ in range(int(tst.readline())):
    n, m = map(int, tst.readline().split())
    ans = dict()
    for i in range(n - 1, m):
        if ans.get(s[i]):
            continue
        else:
            ans[s[i]] = 0
            for j in freq[s[i]][1]:
                if m >= j + 1 > n - 1:
                    ans[s[i]] += 1
    length = 0
    odd = 0
    evens = []
    for j, i in ans.items():
        if i % 2 == 0:
            length += i
            evens.append((j, i // 2))
        elif i > 1:
            length += (i - 1)
            evens.append((j, (i - 1) // 2))
            odd += 1
        else:
            odd += 1
    length = length // 2
    gg = math.factorial(length)
    ff = 1
    for i in evens:
        ff *= math.factorial(i[1])
    if odd > 1:
        ns = ((gg // ff) * odd)
    else:
        ns = (gg // ff)
    ns = (ns % (10 ** 9 + 7))
    kkkkk = nan.readline()
    if ns != int(kkkkk):
        print(ans)
        print(kkkkk)
        print(ns)
