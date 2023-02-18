# https://www.hackerrank.com/challenges/icecream-parlor/problem

# idk = open("testCases.txt", "r")
n = int(input())


class Whatever:
    def __init__(self, value, ind):
        self.value = value
        self.ind = ind

    def __lt__(self, other):
        return self.value < other.value

    def __add__(self, other):
        return self.value + other.value


def make(st, n):
    x = list(map(int, st.split()))
    ans = [None] * n
    for i in range(n):
        ans[i] = Whatever(x[i], i + 1)
    return ans


for _ in range(n):
    k = int(input())
    n = int(input())
    x = make(input(), n)
    x = list(sorted(x))
    i = 0
    j = len(x) - 1
    for __ in range(j + 1):
        if x[j] + x[i] > k:
            j -= 1
        elif x[j] + x[i] < k:
            i += 1
        else:
            break
    ans = list(sorted([x[i].ind, x[j].ind]))
    print(ans[0], ans[1])
