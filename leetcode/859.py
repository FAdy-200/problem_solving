# https://leetcode.com/problems/maximum-frequency-stack/
from collections import defaultdict,deque
import bisect
import heapq


class FreqStack1:

    def __init__(self):
        self.global_i = 0
        self.freq = defaultdict(lambda: [0, [], 0])
        self.heap = []

    def push(self, val: int) -> None:
        self.global_i += 1
        self.freq[val] = [self.freq[val][0] + 1, self.freq[val][1] + [self.global_i], val]
        self.heap = list(sorted((self.freq.values())))
        # heapq.heapify(self.heap)
        pass

    def pop(self) -> int:
        mi = self.heap[-1]
        i = -1
        j = len(self.heap) - 1
        while self.heap and j >= 0 and self.heap[j][0] == mi[0]:
            t = self.heap[j]
            if t[1][-1] > mi[1][-1]:
                mi = t
                i = j
            j -= 1
        mi[0] -= 1
        mi[1].pop()
        if mi[1]:
            self.freq[mi[-1]] = mi
            self.heap[i], self.heap[j + 1] = self.heap[j + 1], self.heap[i]
        else:
            self.freq.pop(mi[-1])
            self.heap.pop(i)
        # self.heap.sort()
        # self.heap = list(sorted((self.freq.values())))
        # heapq.heapify(self.heap)
        return mi[-1]


class FreqStack:

    def __init__(self):
        self.global_i = 0
        self.d = defaultdict(lambda: [1, 0])
        self.a = defaultdict(lambda: [])

    def push(self, val: int) -> None:
        if val == 2189:
            pass
        self.global_i -= 1
        t = self.d[val]
        if t[0] > 0:
            t[0] = self.global_i
            t[1] += 1
            bisect.insort(self.a[1], [[t[0]], val])
        else:
            ele = self.a[t[1]].pop(bisect.bisect_left(self.a[t[1]], [[t[0]]]))
            ele[0].insert(0, self.global_i)
            bisect.insort(self.a[t[1] + 1], ele)
            t[0] = self.global_i
            t[1] += 1
        self.d[val] = t

    def pop(self) -> int:

        ele = self.a[len(self.a)].pop(0)
        if ele[-1] == 2189:
            pass
        if not self.a[len(self.a)]:
            self.a.pop(len(self.a))
        ele[0].pop(0)
        if ele[0]:
            bisect.insort(self.a[len(ele[0])], ele)
            self.d[ele[-1]] = [ele[0][0], self.d[ele[-1]][1]-1]
        else:
            self.d.pop(ele[-1])
        return ele[-1]


# x = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop", "pop"]
# y = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
f = open("test859_1", "r")
x = eval(f.read())
f.close()
f = open("test859_2", "r")
y = eval(f.read())
f.close()
S = FreqStack()
A = []
for i in range(1, len(x)):
    if x[i] == "push":
        S.push(y[i][0])
    else:
        A.append(S.pop())
        # print(A[-1])
print(A)
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
