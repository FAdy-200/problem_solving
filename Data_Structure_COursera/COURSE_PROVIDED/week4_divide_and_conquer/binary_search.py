# Uses python3


def binary_search(a, x):
    l, r = 0, len(a)
    mid = ((r + l) // 2)
    mo = -1
    while x != a[mid]:
        mid = ((l + r) // 2)
        if x > a[mid]:
            l = mid
        elif x < a[mid]:
            r = mid
        if mo == mid:
            return -1
        mo = mid

    return mid





def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


A = list(map(int, input().split()))[1:]
X = list(map(int, input().split()))[1:]
for i in X:
    print(binary_search(A, i), end=" ")
