# Uses python3


def max_dot_product(a, b):
    a = sorted(a)
    b = sorted(b)
    s = 0
    for i in range(len(a)):
        s += (a[i] * b[i])
    return s










input()
x = list(map(int, input().split()))
y = list(map(int, input().split()))
print(max_dot_product(x, y))





