# https://www.hackerrank.com/challenges/candies/

n = int(input())
x = []


class Whatever:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return str(self.value)


for i in range(n):
    x.append(Whatever(int(input()), i))

y = sorted(x)
z = [1] * n
for i in y:
    if i.index != 0:
        if i.index != n - 1:
            if i.value > x[i.index - 1].value \
                    and i.value > x[i.index + 1].value:
                z[i.index] = max(z[i.index - 1], z[i.index + 1]) + 1
            elif i.value > x[i.index - 1].value:
                z[i.index] = z[i.index - 1] + 1
            elif i.value > x[i.index + 1].value:
                z[i.index] = z[i.index + 1] + 1
        else:
            if i.value > x[i.index - 1].value:
                z[i.index] = z[i.index - 1] + 1
    else:
        if i.value > x[i.index + 1].value:
            z[i.index] = z[i.index + 1] + 1

print(sum(z))
