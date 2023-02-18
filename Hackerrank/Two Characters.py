# https://www.hackerrank.com/challenges/two-characters/problem

class Whatever:
    def __init__(self, val, org):
        self.val = val
        self.org = org

    def __lt__(self, other):
        return self.val < other.val


n = int(input())

d = dict()

s = input()
for i in range(len(s)):
    if d.get(s[i]):
        d[s[i]].append(i)
    else:
        d[s[i]] = [i]

found = False
ans = 0
key = d.keys()
for i in key:
    for j in key:
        if i == j:
            continue
        x = d[i]
        y = d[j]
        xl = len(x)
        yl = len(y)
        if abs(xl - yl) > 1:
            continue
        xn = [Whatever(i, 0) for i in x]
        yn = [Whatever(i, 1) for i in y]
        new = list(sorted(xn + yn))
        ln = len(new)
        k = 0
        while k < (ln - 1):
            if new[k].org == new[k + 1].org:
                break
            k += 1
        if k == ln - 1:
            if ln > ans:
                ans = ln

print(ans)
