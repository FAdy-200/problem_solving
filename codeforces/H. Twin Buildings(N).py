num = int(input())
y = [0] * num
W = [0] * num
w = [0] * 2 * num


def max_size(we, qw):
    """

    :param qw:
    :param we:
    :return:
    """
    w = (we / 2) * qw
    z = (qw / 2) * we
    return max(w, z)


t = 0
for i in range(num):
    x = input()
    z = x.split()
    y[i] = max_size(int(z[0]), int(z[1]))
    while t < len(w) - 1:
        w[t + 1] = int(z[1])
        w[t] = int(z[0])
        t += 2
        break
u = 0
i = 0

while u < len(w) - 1:
    while i < len(W):
        W[i] = float(w[u]) * float(w[u + 1])
        i += 1
        break
    u += 2
gg = 0
while gg < len(w)-1:
    if max(W)/w[gg] == w[gg+1]:
        break
    gg += 1
g = 0
lol = max(W)
W.remove(max(W))
while g < len(w)-1:
    if max(W)/w[g] == w[g+1]:
        break
    g += 1


if float(max(y)) >= float(max(W)):
    print(max(y))
else:
    W.remove(max(W))
    print(float(max(W)))


"""
https://codeforces.com/problemset/problem/1252/H
"""