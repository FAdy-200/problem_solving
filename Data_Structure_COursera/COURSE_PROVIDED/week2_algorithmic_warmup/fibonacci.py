# Uses python3
def calc_fib(n):
    if n == 0:
        return 0
    p = 0
    c = 1
    for i in range(1, n):
        p, c = c, (c + p)
    return c



n = int(input())
print(calc_fib(n))
