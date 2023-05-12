# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
import math


class Deq:
    def __init__(self, size):
        self.size = size
        self.de = [None] * size
        self.ind = 0
        self.front = -1
        self.back = -1

    def add_front(self, x):
        for i in x:
            if self.de[self.back] is None:
                self.back = self.size - 1
            self.front -= 1
            if self.front < 0:
                self.front = self.size - 1
            self.de[self.front] = i

    def add_back(self, x, rev=False):
        if rev:
            x = list(reversed(x))
        for i in x:
            self.back += 1
            self.de[self.back] = i
            if self.front == -1:
                self.front = 0

    def __str__(self):
        return str(self.de)

    def rotate(self, r):
        self.ind += r
        self.ind = self.ind % self.size

    def output(self):
        self.ind += 1
        if self.ind == self.size:
            self.ind = 0
            return self.de[self.size - 1]
        return self.de[self.ind - 1]

    def __len__(self):
        return self.size


class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.mi = min(m, n) // 2
        self.ma = max(m, n) // 2
        self.dequeues = []
        self.make_deq()

    def make_deq(self):
        x = 0
        gg = math.ceil(min(self.m, self.n) / 2)
        for i in range(gg):
            size = ((self.n - x) * 2 + (self.m - x - 2) * 2)
            self.dequeues.append(Deq(size))
            x += 2
        if gg == 0:
            size = ((self.n - x) * 2 + (self.m - x - 2) * 2)
            self.dequeues.append(Deq(size))

    def append(self, x):
        gg = self.m - self.mi
        for j in range(self.mi):
            imp = x[j][j:self.n - j]
            self.dequeues[j].add_back(imp)
            self.add_left(x[j][:j])
            self.add_right(x[j][len(x[j]) - j:])
        for j in range(self.mi, gg):
            self.add_left(x[j][:len(x[j]) // 2])
            self.add_right(x[j][len(x[j]) // 2:])
        for j in range(self.mi - 1, -1, -1):
            imp = x[self.m - 1 - j]
            self.dequeues[j].add_back(imp[j:self.n - j], True)
            self.add_left(imp[:j])
            self.add_right(imp[self.n - j:])

    def add_right(self, a):
        a.reverse()
        for i in range(len(a)):
            self.dequeues[i].add_back([a[i]])

    def add_left(self, a):
        for i in range(len(a)):
            self.dequeues[i].add_front([a[i]])

    def answer(self, r):
        for i in self.dequeues:
            i.rotate(r)
        z = 0
        ans = []
        for j in range(self.m):
            ans.append([None] * self.n)
        for i in self.dequeues:
            x = z
            y = z
            d = True
            h = True
            j = 0
            while j < len(i) + 1:
                if h:
                    ans[y][x] = i.output()
                if d:
                    if x < self.n - z - 1 and y < self.m - z - 1:
                        x += 1
                    elif x == self.n - z - 1 and y < self.m - z - 1:
                        y += 1
                    else:
                        d = False
                        h = False
                else:
                    h = True
                    if x > z and y > z:
                        x -= 1
                    elif x == z and y > z:
                        y -= 1
                j += 1
            z += 1
        return ans

    def __str__(self):
        s = ""
        for i in self.dequeues:
            s += str(i) + "\n"
        return s


m, n, r = map(int, input().split())
x = []
for i in range(m):
    x.append(list(input().split()))
mat = Matrix(m, n)
mat.append(x)
ans = mat.answer(r)
for i in ans:
    print(" ".join(i))
