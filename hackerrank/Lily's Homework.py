# https://www.hackerrank.com/challenges/lilys-homework/problem

class Whatever:
    ind = 0

    def __init__(self, val):
        self.val = val
        self.ind = Whatever.ind
        Whatever.ind += 1
        self.sw = False

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __repr__(self):
        return self.val


_ = input()
x = list(map(Whatever, input().split()))
z = list(sorted(x))
ans = 0
for i in range(len(z)):
    if z[i] != x[i] and not x[i].sw:
        x[i], x[z[i].ind] = x[z[i].ind], x[i]
        x[i].sw = True
        ans += 1
print(ans)
