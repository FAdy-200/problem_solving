def findPoint(px, py, qx, qy):
    x = -px + 2 * qx
    y = -py + 2 * qy
    return x, y


n = int(input())

for n_itr in range(n):
    pxPyQxQy = input().split()

    px = int(pxPyQxQy[0])

    py = int(pxPyQxQy[1])

    qx = int(pxPyQxQy[2])

    qy = int(pxPyQxQy[3])

    result = findPoint(px, py, qx, qy)

    print(' '.join(map(str, result)))

# https://www.hackerrank.com/challenges/find-point/problem