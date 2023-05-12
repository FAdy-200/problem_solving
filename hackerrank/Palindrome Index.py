# https://www.hackerrank.com/challenges/palindrome-index/problem


for _ in range(int(input())):
    s = input()
    sr = s[::-1]
    j = 0
    ls = len(s)
    while j < ls:
        if s[j] != sr[j]:
            break
        j += 1
    if j < ls:
        ns = s[:j]+s[j+1:]
        nl = ns[::-1]
        if ns == nl:
            print(j)
        else:
            print(ls-j - 1)
    else:
        print(-1)
