# https://www.hackerrank.com/challenges/largest-permutation/
o = open("testCases.txt","r")
n, k = map(int, o.readline().split())

nn = 0


def make(x):
    global nn
    nn += 1
    return Whatever(int(x), nn - 1)


class Whatever:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __lt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return str(self.value)


x = list(map(make, o.readline().split()))
y = list(sorted(x))
i = 0

while k > 0 and i < n:
    if x[i] != y[i]:
        x[y[i].index], x[i] = x[i], x[y[i].index]
        x[y[i].index].index, x[i].index = x[i].index, x[y[i].index].index

        k -= 1
    i += 1
print(y)
for i in x:
    print(i, end=" ")
